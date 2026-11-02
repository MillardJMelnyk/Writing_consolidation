// BERT WordPiece tokenizer (uncased), matching Hugging Face BertTokenizer for all-MiniLM-L6-v2.
function makeTokenizer(vocabText) {
  const vocab = new Map();
  vocabText.split('\n').forEach((w, i) => { if (w.length) vocab.set(w, i); });
  const CLS = vocab.get('[CLS]'), SEP = vocab.get('[SEP]'), UNK = vocab.get('[UNK]');
  const isPunct = (ch) => {
    const c = ch.codePointAt(0);
    if ((c >= 33 && c <= 47) || (c >= 58 && c <= 64) || (c >= 91 && c <= 96) || (c >= 123 && c <= 126)) return true;
    return /\p{P}/u.test(ch);
  };
  const isCJK = (c) => (c >= 0x4E00 && c <= 0x9FFF) || (c >= 0x3400 && c <= 0x4DBF) || (c >= 0x20000 && c <= 0x2A6DF) ||
    (c >= 0x2A700 && c <= 0x2B73F) || (c >= 0x2B740 && c <= 0x2B81F) || (c >= 0x2B820 && c <= 0x2CEAF) ||
    (c >= 0xF900 && c <= 0xFAFF) || (c >= 0x2F800 && c <= 0x2FA1F);
  function basic(text) {
    let out = '';
    for (const ch of text) {
      const c = ch.codePointAt(0);
      if (c === 0 || c === 0xFFFD || (/\p{Cc}|\p{Cf}/u.test(ch) && ch !== '\t' && ch !== '\n' && ch !== '\r')) continue;
      if (/\s/u.test(ch)) { out += ' '; continue; }
      out += isCJK(c) ? ' ' + ch + ' ' : ch;
    }
    out = out.toLowerCase().normalize('NFD').replace(/\p{Mn}/gu, '');
    const toks = [];
    for (const w of out.split(' ')) {
      if (!w) continue;
      let cur = '';
      for (const ch of w) {
        if (isPunct(ch)) { if (cur) toks.push(cur); toks.push(ch); cur = ''; } else cur += ch;
      }
      if (cur) toks.push(cur);
    }
    return toks;
  }
  function wordpiece(tok) {
    const chars = Array.from(tok);
    if (chars.length > 100) return [UNK];
    const ids = []; let start = 0;
    while (start < chars.length) {
      let end = chars.length, found = null;
      while (start < end) {
        let sub = chars.slice(start, end).join('');
        if (start > 0) sub = '##' + sub;
        if (vocab.has(sub)) { found = vocab.get(sub); break; }
        end--;
      }
      if (found === null) return [UNK];
      ids.push(found); start = end;
    }
    return ids;
  }
  return function encode(text, maxLen = 256) {
    let ids = [];
    for (const t of basic(text)) { ids = ids.concat(wordpiece(t)); if (ids.length >= maxLen - 2) break; }
    return [CLS].concat(ids.slice(0, maxLen - 2), [SEP]);
  };
}
if (typeof module !== 'undefined') module.exports = { makeTokenizer };
