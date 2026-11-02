(function () {
'use strict';
const C = window.CatalogCore, A = window.CATALOG_ASSETS, ITEMS = window.CATALOG_ITEMS;
const DIM = A.dim, SCALE = A.scale;
const $ = (s, el) => (el || document).querySelector(s);
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const ORTJS = document.scripts[0].textContent;
let IDX = null, SESSION = null, ENCODE = null, PROJ = null, ENGINE = null;

// ---------- small helpers
const b64ToBytes = b64 => { const bin = atob(b64); const u = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) u[i] = bin.charCodeAt(i); return u; };
async function gunzip(bytes) { return new Uint8Array(await new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'))).arrayBuffer()); }
function decodeLarge(b64) { // chunked base64 -> bytes
  const n = Math.floor(b64.length / 4) * 3 - (b64.endsWith('==') ? 2 : b64.endsWith('=') ? 1 : 0);
  const out = new Uint8Array(n); const CH = 4 * 1048576; let o = 0;
  for (let i = 0; i < b64.length; i += CH) { const bin = atob(b64.slice(i, i + CH)); for (let j = 0; j < bin.length; j++) out[o++] = bin.charCodeAt(j); }
  return out;
}
function encodeLargeParts(bytes) { // bytes -> array of base64 strings that concatenate correctly
  const parts = []; const CH = 3 * 262144;
  for (let i = 0; i < bytes.length; i += CH) { const sub = bytes.subarray(i, i + CH); let s = ''; for (let j = 0; j < sub.length; j += 32768) s += String.fromCharCode.apply(null, sub.subarray(j, j + 32768)); parts.push(btoa(s)); }
  return parts;
}
async function engineAssets() {
  if (ENGINE) return ENGINE;
  const wasm = await gunzip(b64ToBytes(A.wasm)), model = await gunzip(b64ToBytes(A.model));
  const proj = new Float32Array(b64ToBytes(A.proj).buffer); // mean (384) then W (384 x DIM, row-major)
  ENGINE = { wasm, model, proj, mjs: atob(A.mjs) };
  return ENGINE;
}
function projectRow(v, mean, W, out, o) { // v: Float32(384) normalized -> out[o..o+DIM) int8
  const p = new Float32Array(DIM); let n = 0;
  for (let k = 0; k < DIM; k++) { let s = 0; for (let i = 0; i < 384; i++) s += (v[i] - mean[i]) * W[i * DIM + k]; p[k] = s; n += s * s; }
  n = Math.sqrt(n) || 1;
  for (let k = 0; k < DIM; k++) { let q = Math.round(p[k] / n * SCALE); out[o + k] = q > 127 ? 127 : q < -127 ? -127 : q; }
}
// worker source: same embedding code, run off the main thread
const WORKER_SRC = `
let sess=null, enc=null, mean=null, W=null, DIM=0, SCALE=0;
${projectRow.toString()}
self.onmessage = async (e) => {
  const d = e.data;
  try {
    if (d.init) {
      importScripts(URL.createObjectURL(new Blob([d.ortjs], {type:'text/javascript'})));
      importScripts(URL.createObjectURL(new Blob([d.tokjs], {type:'text/javascript'})));
      ort.env.wasm.numThreads = 1; ort.env.wasm.wasmBinary = d.wasm;
      ort.env.wasm.wasmPaths = { mjs: URL.createObjectURL(new Blob([d.mjs], {type:'text/javascript'})) };
      sess = await ort.InferenceSession.create(d.model, { executionProviders: ['wasm'] });
      enc = makeTokenizer(d.vocab); DIM = d.dim; SCALE = d.scale;
      mean = new Float32Array(d.proj, 0, 384); W = new Float32Array(d.proj, 384 * 4, 384 * DIM);
      self.postMessage({ ready: true }); return;
    }
    const ids = d.texts.map(t => enc(t)); const L = Math.max(...ids.map(a => a.length)), B = ids.length;
    const ii = new BigInt64Array(B * L), am = new BigInt64Array(B * L), tt = new BigInt64Array(B * L);
    ids.forEach((a, b) => a.forEach((v, j) => { ii[b * L + j] = BigInt(v); am[b * L + j] = 1n; }));
    const out = await sess.run({ input_ids: new ort.Tensor('int64', ii, [B, L]), attention_mask: new ort.Tensor('int64', am, [B, L]), token_type_ids: new ort.Tensor('int64', tt, [B, L]) });
    const h = out[Object.keys(out)[0]].data; const H = 384; const res = new Int8Array(B * DIM); const v = new Float32Array(H);
    for (let b = 0; b < B; b++) {
      v.fill(0); const len = ids[b].length;
      for (let j = 0; j < len; j++) { const base = (b * L + j) * H; for (let i = 0; i < H; i++) v[i] += h[base + i]; }
      let n = 0; for (let i = 0; i < H; i++) { v[i] /= len; n += v[i] * v[i]; } n = Math.sqrt(n) || 1; for (let i = 0; i < H; i++) v[i] /= n;
      projectRow(v, mean, W, res, b * DIM);
    }
    self.postMessage({ job: d.job, res }, [res.buffer]);
  } catch (err) { self.postMessage({ error: String(err), job: d.job }); }
};`;

// ---------- setup (first run): read items, segment, fingerprint, save index file
function setupMsg(html, frac) { $('#setup').style.display = 'block'; $('#setupmsg').innerHTML = html; if (frac != null) $('#setupbar').style.width = (100 * frac).toFixed(1) + '%'; }
async function buildIndex() {
  const t0 = Date.now();
  window.addEventListener('beforeunload', warnLeave);
  setupMsg('<b>Setting up search — first time only.</b> Step 1 of 3: reading the catalog items… Keep this page open.', 0);
  const secItem = [], secStart = [], secEnd = [];
  const parSec = [], parStart = [], parEnd = [], parAuth = [];
  const senPar = [], senStart = [], senEnd = [], senWords = [], senText = [];
  const phrSen = [], phrStart = [], phrEnd = [], phrWords = [], phrW0 = [], phrText = [];
  const posting = new Map(); // term -> [sen, pos, sen, pos, ...]
  const itemWords = new Uint32Array(ITEMS.length);
  const parsed = new Array(ITEMS.length);
  let done = 0, next = 0;
  async function fetchOne(n) {
    for (let attempt = 0; attempt < 4; attempt++) {
      try { const r = await fetch(A.raw + ITEMS[n].id + '.md'); if (r.ok) return await r.text(); } catch (e) { }
      await new Promise(r => setTimeout(r, 1500 * (attempt + 1)));
    }
    throw new Error('could not read item ' + ITEMS[n].id + ' from GitHub');
  }
  await Promise.all(Array.from({ length: 8 }, async () => {
    while (next < ITEMS.length) {
      const n = next++; const md = await fetchOne(n);
      parsed[n] = C.segment(C.parseItem(md, ITEMS[n].by));
      done++; if (done % 25 === 0) setupMsg('<b>Setting up search — first time only.</b> Step 1 of 3: reading the catalog items… ' + done.toLocaleString() + ' of ' + ITEMS.length.toLocaleString() + '. Keep this page open.', 0.05 * done / ITEMS.length);
    }
  }));
  parsed.forEach((s, n) => {
    const secBase = secItem.length, parBase = parSec.length;
    s.sections.forEach(x => { secItem.push(n); secStart.push(x.start); secEnd.push(x.end); });
    s.paragraphs.forEach(x => { parSec.push(secBase + x.parent); parStart.push(x.start); parEnd.push(x.end); parAuth.push(x.author); });
    const senBase = senPar.length;
    s.sentences.forEach(x => {
      const si = senPar.length, text = s.plain.slice(x.start, x.end), ws = C.wordSpans(text);
      senPar.push(parBase + x.parent); senStart.push(x.start); senEnd.push(x.end); senWords.push(Math.min(ws.length, 65535)); senText.push(text);
      ws.forEach((w, pos) => { if (pos > 65535) return; let a = posting.get(w[2]); if (!a) posting.set(w[2], a = []); a.push(si, pos); });
      itemWords[n] += ws.length;
    });
    s.phrases.forEach(x => {
      const sg = senBase + x.parent, text = s.plain.slice(x.start, x.end), ws = C.wordSpans(text);
      const before = C.wordSpans(s.plain.slice(senStart[sg], x.start)).length;
      phrSen.push(sg); phrStart.push(x.start); phrEnd.push(x.end); phrWords.push(ws.length); phrW0.push(before); phrText.push(text);
    });
    parsed[n] = null;
  });
  // fingerprints
  const nS = senText.length, nP = phrText.length, total = nS + nP;
  const vecS = new Int8Array(nS * DIM), vecP = new Int8Array(nP * DIM);
  const order = Array.from({ length: total }, (_, i) => i);
  const textOf = i => i < nS ? senText[i] : phrText[i - nS];
  order.sort((a, b) => textOf(a).length - textOf(b).length);
  const jobs = []; for (let i = 0; i < total; i += 32) jobs.push(order.slice(i, i + 32));
  const eng = await engineAssets();
  const hc = navigator.hardwareConcurrency || 2;
  const nW = hc <= 2 ? hc : Math.min(6, hc - 1);
  const wurl = URL.createObjectURL(new Blob([WORKER_SRC], { type: 'text/javascript' }));
  let finished = 0, nextJob = 0; const tFp = Date.now();
  await new Promise((resolve, reject) => {
    let active = 0;
    for (let w = 0; w < nW; w++) {
      const wk = new Worker(wurl); active++;
      const give = () => {
        if (nextJob >= jobs.length) { wk.terminate(); if (--active === 0) resolve(); return; }
        const j = nextJob++; wk.postMessage({ job: j, texts: jobs[j].map(textOf) });
      };
      wk.onmessage = e => {
        const d = e.data;
        if (d.error) { reject(new Error(d.error)); return; }
        if (d.ready) { give(); return; }
        jobs[d.job].forEach((idx, k) => { const dst = idx < nS ? vecS : vecP, o = (idx < nS ? idx : idx - nS) * DIM; dst.set(d.res.subarray(k * DIM, (k + 1) * DIM), o); });
        finished += jobs[d.job].length;
        if (finished % 640 < 32) {
          const rate = finished / ((Date.now() - tFp) / 1000), left = (total - finished) / rate;
          setupMsg('<b>Setting up search — first time only.</b> Step 2 of 3: fingerprinting ' + finished.toLocaleString() + ' of ' + total.toLocaleString() +
            ' phrases and sentences, about ' + Math.max(1, Math.round(left / 60)) + ' minutes left. Keep this page open; you can use the links meanwhile.', 0.05 + 0.9 * finished / total);
        }
        give();
      };
      wk.onerror = e => reject(new Error(e.message || 'worker error'));
      wk.postMessage({ init: true, ortjs: ORTJS, tokjs: makeTokenizer.toString(), mjs: eng.mjs, wasm: eng.wasm.slice().buffer, model: eng.model.slice().buffer, vocab: A.vocab, proj: eng.proj.slice().buffer, dim: DIM, scale: SCALE });
    }
  });
  setupMsg('<b>Setting up search — first time only.</b> Step 3 of 3: saving the index…', 0.97);
  // word index
  const terms = [...posting.keys()].sort();
  const postOff = new Uint32Array(terms.length + 1); let tot = 0;
  terms.forEach((t, i) => { postOff[i] = tot; tot += posting.get(t).length / 2; }); postOff[terms.length] = tot;
  const postSen = new Uint32Array(tot), postPos = new Uint16Array(tot); let k = 0;
  terms.forEach(t => { const a = posting.get(t); for (let i = 0; i < a.length; i += 2) { postSen[k] = a[i]; postPos[k] = a[i + 1]; k++; } });
  const header = {
    format: 'catalog-search-index', version: 1, created: new Date().toISOString(),
    model: 'Xenova/all-MiniLM-L6-v2, model_quantized.onnx; mean pooling, L2-normalized, then projected 384->' + DIM + ' with proj_mean/proj_W, re-normalized, multiplied by scale and rounded to int8',
    dim: DIM, scale: SCALE, text_source: A.raw + '<item id>.md', items: ITEMS.map(x => x.id), terms,
    authors: ['me', 'claude', 'other']
  };
  const u32 = a => Uint32Array.from(a), u16 = a => Uint16Array.from(a), u8 = a => Uint8Array.from(a);
  const packed = C.packIndex(header, {
    proj: eng.proj, item_words: itemWords,
    sec_item: u32(secItem), sec_start: u32(secStart), sec_end: u32(secEnd),
    par_sec: u32(parSec), par_start: u32(parStart), par_end: u32(parEnd), par_author: u8(parAuth),
    sen_par: u32(senPar), sen_start: u32(senStart), sen_end: u32(senEnd), sen_words: u16(senWords), sen_vec: vecS,
    phr_sen: u32(phrSen), phr_start: u32(phrStart), phr_end: u32(phrEnd), phr_words: u16(phrWords), phr_w0: u16(phrW0), phr_vec: vecP,
    term_off: postOff, post_sen: postSen, post_pos: postPos
  });
  const blob = new Blob(['window.CATALOG_SEARCH_INDEX="'].concat(encodeLargeParts(packed), ['";\n']), { type: 'text/javascript' });
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'catalog_search_index.js'; document.body.appendChild(a); a.click();
  window.removeEventListener('beforeunload', warnLeave);
  const mins = Math.round((Date.now() - t0) / 60000);
  setupMsg('<b>Search setup finished</b> (' + mins + ' minutes). Your browser has saved <b>catalog_search_index.js</b> to your Downloads folder. ' +
    'Move it into the folder where this page (Master_catalog.html) is, then reload this page. You only do this once.', 1);
  window.CATALOG_BUILD_DONE = true;
}
function warnLeave(e) { e.preventDefault(); e.returnValue = ''; }

// ---------- loading the saved index
function loadIndex() {
  const { header, arrays } = C.unpackIndex(decodeLarge(window.CATALOG_SEARCH_INDEX));
  window.CATALOG_SEARCH_INDEX = null;
  const X = Object.assign({ header }, arrays);
  const itemPos = new Map(ITEMS.map((x, i) => [x.id, i]));
  X.itemMeta = header.items.map(id => ITEMS[itemPos.get(id)] || { id, date: '', type: '', title: id, by: '' });
  X.nS = X.sen_par.length; X.nP = X.phr_sen.length;
  X.parWords = new Uint32Array(X.par_sec.length); X.secWords = new Uint32Array(X.sec_item.length);
  for (let s = 0; s < X.nS; s++) X.parWords[X.sen_par[s]] += X.sen_words[s];
  for (let p = 0; p < X.par_sec.length; p++) X.secWords[X.par_sec[p]] += X.parWords[p];
  X.senOwnPhr = new Uint8Array(X.nS); for (let p = 0; p < X.nP; p++) X.senOwnPhr[X.phr_sen[p]] = 1;
  X.termIndex = new Map(header.terms.map((t, i) => [t, i]));
  return X;
}
async function loadModel() {
  const eng = await engineAssets();
  ort.env.wasm.numThreads = 1; ort.env.wasm.wasmBinary = eng.wasm;
  ort.env.wasm.wasmPaths = { mjs: URL.createObjectURL(new Blob([eng.mjs], { type: 'text/javascript' })) };
  SESSION = await ort.InferenceSession.create(eng.model, { executionProviders: ['wasm'] });
  ENCODE = makeTokenizer(A.vocab);
  PROJ = { mean: new Float32Array(eng.proj.buffer, eng.proj.byteOffset, 384), W: new Float32Array(eng.proj.buffer, eng.proj.byteOffset + 384 * 4, 384 * DIM) };
}
async function embedQuery(q) {
  const ids = ENCODE(q), L = ids.length;
  const ii = new BigInt64Array(L), am = new BigInt64Array(L), tt = new BigInt64Array(L);
  ids.forEach((v, j) => { ii[j] = BigInt(v); am[j] = 1n; });
  const out = await SESSION.run({ input_ids: new ort.Tensor('int64', ii, [1, L]), attention_mask: new ort.Tensor('int64', am, [1, L]), token_type_ids: new ort.Tensor('int64', tt, [1, L]) });
  const h = out[Object.keys(out)[0]].data, v = new Float32Array(384);
  for (let j = 0; j < L; j++) for (let i = 0; i < 384; i++) v[i] += h[j * 384 + i];
  let n = 0; for (let i = 0; i < 384; i++) { v[i] /= L; n += v[i] * v[i]; } n = Math.sqrt(n); for (let i = 0; i < 384; i++) v[i] /= n;
  const q8 = new Int8Array(DIM); projectRow(v, PROJ.mean, PROJ.W, q8, 0);
  return q8;
}

// ---------- search
function unitOf(level, sen) { // sentence index -> unit id at level (>=1)
  const X = IDX; if (level === 1) return sen; const par = X.sen_par[sen]; if (level === 2) return par;
  const sec = X.par_sec[par]; if (level === 3) return sec; return X.sec_item[sec];
}
function itemOfSen(sen) { return IDX.sec_item[IDX.par_sec[IDX.sen_par[sen]]]; }
function passesFilters(sen, f) {
  const X = IDX;
  if (f.me && X.par_author[X.sen_par[sen]] !== 0) return false;
  const m = X.itemMeta[itemOfSen(sen)];
  if (f.type && m.type !== f.type) return false;
  if (f.from && m.date < f.from) return false;
  if (f.to && m.date > f.to) return false;
  return true;
}
async function runSearch(f) {
  const X = IDX, level = f.level;
  const hits = new Map(); // unit key -> {matched, best, bestSen, bestPhr}
  const note = (key, matched, score, sen, phr) => {
    let h = hits.get(key); if (!h) hits.set(key, h = { matched: 0, best: -1, sen, phr });
    h.matched += matched; if (score > h.best) { h.best = score; h.sen = sen; h.phr = phr; }
  };
  if (f.mode === 'meaning') {
    const q = await embedQuery(f.q), cut = f.cut * SCALE * SCALE;
    const sScore = new Float32Array(X.nS), senHit = new Uint8Array(X.nS);
    for (let s = 0; s < X.nS; s++) { let d = 0; const o = s * DIM; for (let k = 0; k < DIM; k++) d += X.sen_vec[o + k] * q[k]; sScore[s] = d; if (d >= cut) senHit[s] = 1; }
    const phrMatched = new Float32Array(X.nS), phrBest = new Float32Array(X.nS).fill(-1e9), phrBestIdx = new Int32Array(X.nS).fill(-1);
    for (let p = 0; p < X.nP; p++) {
      let d = 0; const o = p * DIM; for (let k = 0; k < DIM; k++) d += X.phr_vec[o + k] * q[k];
      if (d < cut) continue;
      const s = X.phr_sen[p]; if (!passesFilters(s, f)) continue;
      if (level === 0) { note('p' + p, X.phr_words[p], d, s, p); continue; }
      phrMatched[s] += X.phr_words[p]; if (d > phrBest[s]) { phrBest[s] = d; phrBestIdx[s] = p; }
    }
    for (let s = 0; s < X.nS; s++) {
      const hitBySen = senHit[s] === 1, m = phrMatched[s];
      if (!hitBySen && !m) continue;
      if (!passesFilters(s, f)) continue;
      if (level === 0) { if (hitBySen && !X.senOwnPhr[s]) note('s' + s, X.sen_words[s], sScore[s], s, -1); continue; }
      const matched = hitBySen ? X.sen_words[s] : Math.min(m, X.sen_words[s]);
      let best = -1e9, bp = -1;
      if (hitBySen) best = sScore[s];
      if (phrBestIdx[s] >= 0 && phrBest[s] > best) { best = phrBest[s]; bp = phrBestIdx[s]; }
      note(unitOf(level, s), matched, best, s, bp);
    }
  } else {
    const terms = C.wordSpans(f.q).map(w => w[2]);
    if (!terms.length) return [];
    const ti = terms.map(t => X.termIndex.get(t));
    if (ti.some(x => x === undefined)) return [];
    const sets = ti.slice(1).map(t => { const s = new Set(); for (let k = X.term_off[t]; k < X.term_off[t + 1]; k++) s.add(X.post_sen[k] * 65536 + X.post_pos[k]); return s; });
    const t0 = ti[0];
    for (let k = X.term_off[t0]; k < X.term_off[t0 + 1]; k++) {
      const s = X.post_sen[k], pos = X.post_pos[k];
      let ok = true; for (let j = 0; j < sets.length; j++) if (!sets[j].has(s * 65536 + pos + j + 1)) { ok = false; break; }
      if (!ok || !passesFilters(s, f)) continue;
      if (level === 0) {
        let phr = -1; // find phrase containing pos
        if (X.senOwnPhr[s]) for (let p = phraseStart(s); p < X.nP && X.phr_sen[p] === s; p++) if (pos >= X.phr_w0[p] && pos < X.phr_w0[p] + X.phr_words[p]) { phr = p; break; }
        note(phr >= 0 ? 'p' + phr : 's' + s, terms.length, 1, s, phr);
      } else note(unitOf(level, s), terms.length, 1, s, -1);
    }
  }
  // strength and ranking
  const out = [];
  for (const [key, h] of hits) {
    let words, item;
    if (level === 0) { words = typeof key === 'string' && key[0] === 'p' ? X.phr_words[h.phr] : X.sen_words[h.sen]; item = itemOfSen(h.sen); }
    else if (level === 1) { words = X.sen_words[key]; item = itemOfSen(key); }
    else if (level === 2) { words = X.parWords[key]; item = itemOfSen(h.sen); }
    else if (level === 3) { words = X.secWords[key]; item = X.sec_item[key]; }
    else { words = X.item_words[key]; item = key; }
    const strength = Math.min(1, words ? h.matched / words : 0);
    out.push({ key, sen: h.sen, phr: h.phr, item, strength, best: h.best });
  }
  out.sort(f.sort === 'date' ? (a, b) => (X.itemMeta[b.item].date || '').localeCompare(X.itemMeta[a.item].date || '') || b.strength - a.strength
                             : (a, b) => b.strength - a.strength || b.best - a.best);
  return out;
}
let PHR_START = null;
function phraseStart(s) { // first phrase index of sentence s (phrases are stored in sentence order)
  if (!PHR_START) { PHR_START = new Int32Array(IDX.nS).fill(-1); for (let p = IDX.nP - 1; p >= 0; p--) PHR_START[IDX.phr_sen[p]] = p; }
  return PHR_START[s];
}

// ---------- excerpts (read live from the item page on GitHub)
const MD_CACHE = new Map();
async function itemPlain(n) {
  const id = IDX.itemMeta[n].id;
  if (!MD_CACHE.has(id)) MD_CACHE.set(id, fetch(A.raw + id + '.md').then(r => r.text()).then(md => C.parseItem(md, IDX.itemMeta[n].by).plain));
  return MD_CACHE.get(id);
}
async function excerptHTML(r, f) {
  const X = IDX, plain = await itemPlain(r.item);
  const par = X.sen_par[r.sen], ps = X.par_start[par], pe = X.par_end[par];
  let hs, he;
  if (r.phr >= 0) { hs = X.phr_start[r.phr]; he = X.phr_end[r.phr]; } else { hs = X.sen_start[r.sen]; he = X.sen_end[r.sen]; }
  let s = Math.max(ps, hs - 220), e = Math.min(pe, he + 260);
  let body = esc(plain.slice(s, hs)) + '<mark>' + esc(plain.slice(hs, he)) + '</mark>' + esc(plain.slice(he, e));
  if (f.mode === 'exact') {
    const words = C.wordSpans(f.q).map(w => w[2]);
    const re = new RegExp('\\b(' + words.map(w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('\\W+') + ')\\b', 'gi');
    body = body.replace(re, '<mark class="w">$1</mark>');
  }
  return (s > ps ? '…' : '') + body + (e < pe ? '…' : '');
}

// ---------- UI
const LEVELS = ['phrase', 'sentence', 'paragraph', 'passage / section', 'whole item'];
function buildPanels() {
  const types = [...new Set(ITEMS.map(x => x.type))].sort();
  document.querySelectorAll('.panel').forEach(p => {
    p.appendChild($('#paneltpl').content.cloneNode(true));
    const sel = $('.type', p); types.forEach(t => { const o = document.createElement('option'); o.value = t; o.textContent = t; sel.appendChild(o); });
    const cut = $('.cut', p), cv = $('.cutv', p); cut.oninput = () => cv.textContent = (+cut.value).toFixed(2);
    p.querySelectorAll('.mode').forEach(r => { r.name = 'mode' + p.dataset.p; r.onchange = () => { $('.strict', p).style.display = $('.mode:checked', p).value === 'meaning' ? '' : 'none'; }; });
    $('.go', p).onclick = () => submit(p);
    $('.q', p).addEventListener('keydown', e => { if (e.key === 'Enter') submit(p); });
  });
}
function readPanel(p) {
  return { q: $('.q', p).value.trim(), mode: $('.mode:checked', p).value, level: +$('.level', p).value, cut: +$('.cut', p).value,
    me: $('.me', p).checked, type: $('.type', p).value, from: $('.from', p).value, to: $('.to', p).value, sort: $('.sort', p).value };
}
function fillPanel(p, f) {
  $('.q', p).value = f.q; p.querySelectorAll('.mode').forEach(r => r.checked = r.value === f.mode); $('.level', p).value = f.level;
  $('.cut', p).value = f.cut; $('.cutv', p).textContent = (+f.cut).toFixed(2); $('.me', p).checked = !!f.me; $('.type', p).value = f.type || '';
  $('.from', p).value = f.from || ''; $('.to', p).value = f.to || ''; $('.sort', p).value = f.sort || 'strength';
  $('.strict', p).style.display = f.mode === 'meaning' ? '' : 'none';
}
function submit(p) { const f = readPanel(p); if (!f.q) return; location.hash = '#search?' + new URLSearchParams(Object.entries(f).map(([k, v]) => [k, String(v)])).toString(); }
function readyText() {
  if (window.CATALOG_INDEX_MISSING) return window.CATALOG_BUILD_DONE ? 'Search will be ready once the index file is in place and the page is reloaded.' : 'Search is being set up (see the yellow box above). It can be used once setup is finished.';
  if (!IDX) return 'Loading search…';
  if (!SESSION) return 'Exact-word search is ready; meaning search is loading…';
  return 'Search ready: ' + IDX.header.items.length.toLocaleString() + ' items, ' + (IDX.nS + IDX.nP).toLocaleString() + ' phrases and sentences.';
}
function refreshReady() { document.querySelectorAll('.ready').forEach(el => el.textContent = readyText()); }
let RESULTS = [], SHOWN = 0, CURF = null;
async function route() {
  const h = location.hash;
  if (!h.startsWith('#search?')) { $('#resview').style.display = 'none'; $('#home').style.display = ''; return; }
  const sp = new URLSearchParams(h.slice(8));
  const f = { q: sp.get('q') || '', mode: sp.get('mode') || 'meaning', level: +(sp.get('level') || 2), cut: +(sp.get('cut') || 0.5),
    me: sp.get('me') === 'true', type: sp.get('type') || '', from: sp.get('from') || '', to: sp.get('to') || '', sort: sp.get('sort') || 'strength' };
  $('#home').style.display = 'none'; $('#resview').style.display = ''; window.scrollTo(0, 0);
  fillPanel($('.panel[data-p="2"]'), f);
  const st = $('#status'); $('#results').innerHTML = ''; $('#more').style.display = 'none';
  if (!IDX) { st.textContent = readyText(); return; }
  if (f.mode === 'meaning' && !SESSION) { st.textContent = 'Meaning search is still loading — try again in a few seconds.'; return; }
  st.textContent = 'Searching…';
  const t = performance.now();
  RESULTS = await runSearch(f); CURF = f; SHOWN = 0;
  st.textContent = RESULTS.length.toLocaleString() + ' ' + LEVELS[f.level] + (RESULTS.length === 1 ? '' : 's') + ' found for "' + f.q + '"' +
    (f.mode === 'meaning' ? ' by meaning' : ' (exact words)') + ' — ' + (f.sort === 'date' ? 'newest first' : 'strongest first') + '. (' + Math.round(performance.now() - t) + ' ms)';
  showMore();
}
async function showMore() {
  const X = IDX, f = CURF, box = $('#results'), batch = RESULTS.slice(SHOWN, SHOWN + 50); SHOWN += batch.length;
  for (const r of batch) {
    const m = X.itemMeta[r.item], div = document.createElement('div'); div.className = 'r';
    div.innerHTML = '<a href="' + A.page + m.id + '.md">' + esc(m.title) + '</a><div class="m">' + m.date + ' · ' + esc(m.type) +
      ' · strength ' + Math.round(r.strength * 100) + '%' + (f.mode === 'meaning' ? ' · closest match ' + (r.best / SCALE / SCALE).toFixed(2) : '') + '</div><div class="s">loading excerpt…</div>';
    box.appendChild(div);
    excerptHTML(r, f).then(html => { $('.s', div).innerHTML = html; }).catch(() => { $('.s', div).textContent = '(excerpt unavailable offline — open the item)'; });
  }
  $('#more').style.display = SHOWN < RESULTS.length ? '' : 'none';
}

// ---------- start
buildPanels();
document.querySelectorAll('.back').forEach(a => a.onclick = e => { e.preventDefault(); location.hash = ''; });
$('#more').onclick = showMore;
window.addEventListener('hashchange', route);
refreshReady();
(async () => {
  if (window.CATALOG_INDEX_MISSING || !window.CATALOG_SEARCH_INDEX) {
    window.CATALOG_INDEX_MISSING = true; refreshReady();
    try { await buildIndex(); } catch (e) { setupMsg('<b>Search setup stopped:</b> ' + esc(e.message || e) + '. Reload the page to try again.', null); window.removeEventListener('beforeunload', warnLeave); }
    refreshReady(); return;
  }
  await new Promise(r => setTimeout(r, 30));
  IDX = loadIndex(); refreshReady(); route();
  try { await loadModel(); } catch (e) { console.error(e); }
  refreshReady(); window.CATALOG_READY = true;
})();
route();
})();
