// Catalog search core: item parsing, segmentation, exact-word tokens, index container format.
// Shared by the page (Millards_master_writing_catalog.html), its build workers, and the Node test scripts.
(function (root) {
  'use strict';
  const ME = 'Millard J Melnyk';
  const AUTH = { me: 0, claude: 1, other: 2 };
  const LEVEL = { phrase: 0, sentence: 1, paragraph: 2, section: 3, work: 4 };

  // ---- markdown line -> plain text (deterministic; same at build and display time)
  function plainLine(s) {
    s = s.replace(/!\[[^\]]*\]\([^)]*\)/g, ' ');
    s = s.replace(/\[([^\]]*)\]\([^)]*\)/g, '$1');
    s = s.replace(/<[^>]+>/g, ' ');
    s = s.replace(/\\([\\`*_{}\[\]()#+\-.!>|~])/g, '$1');
    s = s.replace(/^\s{0,3}>\s?/, '');
    s = s.replace(/^\s{0,3}#{1,6}\s+/, '');
    s = s.replace(/^\s*(?:[-*+]|\d+[.)])\s+/, '');
    s = s.replace(/\*\*|__|`+/g, '');
    s = s.replace(/(^|[\s(])[*_]([^*_\s][^*_]*?)[*_](?=[\s).,;:!?]|$)/g, '$1$2');
    s = s.replace(/\|/g, ' ');
    return s.replace(/\s+/g, ' ').trim();
  }

  // ---- parse one item page (markdown text as published in catalog/items/<id>.md)
  // returns {plain, paras:[{start,end,author,section}], sections:[{start,end}]}
  function parseItem(md, byAuthor) {
    md = md.replace(/\r\n?/g, '\n');
    const home = md.indexOf('[← Catalog home]');
    let body = home >= 0 ? md.slice(md.indexOf('\n---\n', home) + 5) : md;
    const imgCut = body.lastIndexOf('\n---\n\n**Images**');
    if (imgCut >= 0) body = body.slice(0, imgCut);
    const isChat = /^\s*### (Millard|Claude) · /.test(body);
    const baseAuthor = byAuthor === ME ? AUTH.me : AUTH.other;
    let plain = '';
    const paras = [], sections = [];
    let author = isChat ? AUTH.me : baseAuthor;
    let secStart = -1, buf = [], bufQuote = false;
    function addText(t) {
      if (plain.length) plain += '\n';
      const st = plain.length; plain += t; return [st, plain.length];
    }
    function flush() {
      if (!buf.length) return;
      const t = plainLine(buf.join(' '));
      buf = [];
      if (!t) return;
      const [st, en] = addText(t);
      const a = isChat ? author : (bufQuote ? AUTH.other : baseAuthor);
      paras.push({ start: st, end: en, author: a, section: -1 });
    }
    function openSection() {
      if (secStart >= 0) closeSection();
      secStart = plain.length ? plain.length + 1 : 0;
    }
    function closeSection() {
      if (secStart < 0) return;
      const end = plain.length;
      if (end > secStart) sections.push({ start: secStart, end: end });
      secStart = -1;
    }
    openSection();
    for (const line of body.split('\n')) {
      const m = line.match(/^### (Millard|Claude) · /);
      if (isChat && m) {
        flush();
        if (m[1] === 'Millard') { closeSection(); openSection(); author = AUTH.me; }
        else author = AUTH.claude;
        continue;
      }
      if (!isChat && /^\s{0,3}#{1,6}\s+\S/.test(line)) { flush(); closeSection(); openSection(); }
      if (!line.trim()) { flush(); continue; }
      const q = /^\s{0,3}>/.test(line);
      if (buf.length && q !== bufQuote) flush();
      bufQuote = q; buf.push(line);
    }
    flush(); closeSection();
    if (!sections.length && plain.length) sections.push({ start: 0, end: plain.length });
    // assign paragraphs to sections
    let si = 0;
    for (const p of paras) {
      while (si < sections.length - 1 && p.start >= sections[si].end) si++;
      p.section = si;
    }
    return { plain, paras, sections };
  }

  // ---- sentences and phrases (character ranges inside one paragraph)
  const SENT_RE = /[.!?…]+["'”’)\]]*\s+(?=["'“‘(\[]?[A-Z0-9¿¡])/g;
  function splitSentences(text, base) {
    const out = []; let st = 0, m;
    SENT_RE.lastIndex = 0;
    while ((m = SENT_RE.exec(text))) {
      const en = m.index + m[0].trimEnd().length;
      if (en > st) out.push([base + st, base + en]);
      st = m.index + m[0].length;
    }
    if (st < text.length) out.push([base + st, base + text.length]);
    return out.filter(r => /[\p{L}\p{N}]/u.test(text.slice(r[0] - base, r[1] - base)));
  }
  const WORD_RE = /[\p{L}\p{N}]+(?:['’][\p{L}]+)*/gu;
  function wordSpans(text) {
    const out = []; let m; WORD_RE.lastIndex = 0;
    while ((m = WORD_RE.exec(text))) out.push([m.index, m.index + m[0].length, m[0].toLowerCase()]);
    return out;
  }
  const BREAK_RE = /[,;:()—–]|\s-\s|\b(?:because|which|although|whereas|while|but)\b/gi;
  function splitPhrases(sText, sBase) {
    // candidate cut points, then group words into phrases of 4-12 words
    const words = wordSpans(sText);
    if (words.length <= 12) return null; // phrase == sentence
    const cuts = new Set(); let m; BREAK_RE.lastIndex = 0;
    while ((m = BREAK_RE.exec(sText))) cuts.add(m.index);
    const groups = []; let cur = [];
    for (let i = 0; i < words.length; i++) {
      const w = words[i];
      const cutBefore = i > 0 && [...cuts].some(c => c >= words[i - 1][1] && c <= w[0]);
      if ((cutBefore && cur.length >= 4) || cur.length >= 12) { groups.push(cur); cur = []; }
      cur.push(w);
    }
    if (cur.length) {
      if (cur.length < 4 && groups.length) groups[groups.length - 1] = groups[groups.length - 1].concat(cur);
      else groups.push(cur);
    }
    return groups.map(g => [sBase + g[0][0], sBase + g[g.length - 1][1]]);
  }

  // ---- full segmentation of one item into the unit hierarchy
  // units: {lvl, start, end, parent(sentence for phrase, paragraph for sentence...), author}
  function segment(parsed) {
    const { plain, paras, sections } = parsed;
    const sec = sections.map(s => ({ start: s.start, end: s.end }));
    const par = [], sen = [], phr = [];
    paras.forEach(p => {
      const pi = par.length;
      par.push({ start: p.start, end: p.end, parent: p.section, author: p.author });
      const pt = plain.slice(p.start, p.end);
      for (const [a, b] of splitSentences(pt, p.start)) {
        const si = sen.length;
        sen.push({ start: a, end: b, parent: pi, author: p.author, ownPhrases: false });
        const ph = splitPhrases(plain.slice(a, b), a);
        if (ph) { sen[si].ownPhrases = true; for (const [c, d] of ph) phr.push({ start: c, end: d, parent: si, author: p.author }); }
      }
    });
    return { plain, sections: sec, paragraphs: par, sentences: sen, phrases: phr };
  }

  // ---- index container (documented in Search_index_format.md)
  // file: catalog_search_index.js = one line:  window.CATALOG_SEARCH_INDEX="<base64>";
  // base64 decodes to: "CSI1" | uint32 headerLength | header JSON (UTF-8) | padding to 4 bytes | binary arrays
  function packIndex(header, arrays) {
    const enc = new TextEncoder();
    header.arrays = [];
    let offset = 0;
    for (const [name, arr] of Object.entries(arrays)) {
      const bytes = arr.byteLength;
      header.arrays.push({ name, type: arr.constructor.name, offset, length: arr.length });
      offset += Math.ceil(bytes / 8) * 8;
    }
    const hj = enc.encode(JSON.stringify(header));
    const hpad = Math.ceil((8 + hj.length) / 8) * 8;
    const out = new Uint8Array(hpad + offset);
    out.set([67, 83, 73, 49], 0);
    new DataView(out.buffer).setUint32(4, hj.length, true);
    out.set(hj, 8);
    let i = 0;
    for (const arr of Object.values(arrays)) {
      out.set(new Uint8Array(arr.buffer, arr.byteOffset, arr.byteLength), hpad + header.arrays[i].offset); i++;
    }
    return out;
  }
  const TYPES = { Int8Array, Uint8Array, Int16Array, Uint16Array, Int32Array, Uint32Array, Float32Array };
  function unpackIndex(bytes) {
    if (bytes[0] !== 67 || bytes[1] !== 83 || bytes[2] !== 73 || bytes[3] !== 49) throw new Error('not a catalog search index');
    const hl = new DataView(bytes.buffer, bytes.byteOffset).getUint32(4, true);
    const header = JSON.parse(new TextDecoder().decode(bytes.subarray(8, 8 + hl)));
    const hpad = Math.ceil((8 + hl) / 8) * 8;
    const arrays = {};
    for (const a of header.arrays) {
      const T = TYPES[a.type];
      arrays[a.name] = new T(bytes.buffer, bytes.byteOffset + hpad + a.offset, a.length);
    }
    return { header, arrays };
  }

  root.CatalogCore = { ME, AUTH, LEVEL, plainLine, parseItem, segment, wordSpans, splitSentences, packIndex, unpackIndex };
})(typeof self !== 'undefined' ? self : (typeof window !== 'undefined' ? window : globalThis));
if (typeof module !== 'undefined') module.exports = globalThis.CatalogCore;
