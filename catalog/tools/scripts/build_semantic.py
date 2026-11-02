"""Build the meaning-search index: split every catalogued item into passages and store an int8 fingerprint for each.

Usage: python3 build_semantic.py items.jsonl tags_final2.jsonl model_dir out_dir
model_dir must hold model_quantized.onnx and tokenizer.json (Xenova/all-MiniLM-L6-v2).
Writes out_dir/sem_vectors.bin (int8, 384 per passage) and out_dir/sem_refs.json ([[item_index, word_start], ...]).
Item order matches build_html.py, so item_index points into the same list the HTML search uses.
"""
import json, sys, re, os, time
import numpy as np
import onnxruntime as ort
from tokenizers import Tokenizer

ITEMS, TAGS, MODEL, OUT = sys.argv[1:5]
WORDS, STRIDE, BATCH = 150, 120, 64


def plain(md):  # must match build_html.py
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', md or '')
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'[*_#>`|]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


tags = [json.loads(l) for l in open(TAGS, encoding='utf-8')]
allitems = {json.loads(l)['id']: json.loads(l) for l in open(ITEMS, encoding='utf-8')}
items = [allitems[t['id']] for t in tags]

refs, texts = [], []
for n, it in enumerate(items):
    words = plain(it['title'] + ' ' + it['text']).split(' ')
    start = 0
    while True:
        chunk = words[start:start + WORDS]
        if chunk and any(chunk):
            refs.append([n, start]); texts.append(' '.join(chunk))
        if start + WORDS >= len(words): break
        start += STRIDE

tok = Tokenizer.from_file(os.path.join(MODEL, 'tokenizer.json'))
tok.enable_truncation(max_length=256)
tok.enable_padding(pad_id=0, pad_token='[PAD]')
opts = ort.SessionOptions(); opts.intra_op_num_threads = os.cpu_count()
sess = ort.InferenceSession(os.path.join(MODEL, 'model_quantized.onnx'), opts)
names = [i.name for i in sess.get_inputs()]

vecs = np.zeros((len(texts), 384), dtype=np.int8)
t0 = time.time()
for b in range(0, len(texts), BATCH):
    enc = tok.encode_batch(texts[b:b + BATCH])
    ids = np.array([e.ids for e in enc], dtype=np.int64)
    mask = np.array([e.attention_mask for e in enc], dtype=np.int64)
    feed = {'input_ids': ids, 'attention_mask': mask}
    if 'token_type_ids' in names: feed['token_type_ids'] = np.zeros_like(ids)
    hidden = sess.run(None, feed)[0]
    m = mask[:, :, None].astype(np.float32)
    emb = (hidden * m).sum(1) / np.maximum(m.sum(1), 1e-9)
    emb /= np.linalg.norm(emb, axis=1, keepdims=True)
    vecs[b:b + BATCH] = np.clip(np.round(emb * 127), -127, 127).astype(np.int8)
    if (b // BATCH) % 50 == 0:
        print('%d/%d passages, %.0fs' % (b, len(texts), time.time() - t0), flush=True)

os.makedirs(OUT, exist_ok=True)
vecs.tofile(os.path.join(OUT, 'sem_vectors.bin'))
json.dump(refs, open(os.path.join(OUT, 'sem_refs.json'), 'w'))
print('done: %d passages from %d items in %.0fs' % (len(texts), len(items), time.time() - t0))
