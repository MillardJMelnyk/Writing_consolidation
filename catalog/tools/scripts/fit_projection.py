"""Fit the 384->128 projection used to shrink fingerprints (PCA on a sample of catalog pieces) and test its fidelity.
Usage: python3 fit_projection.py model_dir pieces.json out.json"""
import json, sys, os, numpy as np, onnxruntime as ort, time
from tokenizers import Tokenizer
MODEL, PIECES, OUT = sys.argv[1:4]
DIM, SCALE = 256, 283.0
tok = Tokenizer.from_file(os.path.join(MODEL, 'tokenizer.json')); tok.no_padding(); tok.enable_truncation(max_length=256)
sess = ort.InferenceSession(os.path.join(MODEL, 'model_quantized.onnx'))
def embed(texts):
    res = []
    for b in range(0, len(texts), 64):
        enc = [tok.encode(t).ids for t in texts[b:b+64]]; L = max(map(len, enc))
        ids = np.zeros((len(enc), L), np.int64); mask = np.zeros_like(ids)
        for i, e in enumerate(enc): ids[i, :len(e)] = e; mask[i, :len(e)] = 1
        h = sess.run(None, {'input_ids': ids, 'attention_mask': mask, 'token_type_ids': np.zeros_like(ids)})[0]
        m = mask[:, :, None].astype(np.float32); e = (h * m).sum(1) / m.sum(1)
        res.append(e / np.linalg.norm(e, axis=1, keepdims=True))
    return np.concatenate(res)
pieces = json.load(open(PIECES)); t = time.time()
E = embed(pieces); print('embedded', len(E), 'in %.0fs' % (time.time() - t))
fit, test = E[:20000], E[20000:]
mean = fit.mean(0); U, S, Vt = np.linalg.svd(fit - mean, full_matrices=False); W = Vt[:DIM].T
print('variance kept %.3f' % ((S[:DIM] ** 2).sum() / (S ** 2).sum()))
def reduce(X):
    P = (X - mean) @ W; P /= np.linalg.norm(P, axis=1, keepdims=True); return P
Pt = reduce(test); Q = np.clip(np.round(Pt * SCALE), -127, 127)
print('clipped share %.5f' % (np.abs(Pt * SCALE) > 127).mean())
full = test @ test.T; red = (Q @ Q.T) / SCALE ** 2
iu = np.triu_indices(len(test), 1)
print('cosine agreement (corr) %.4f' % np.corrcoef(full[iu], red[iu])[0, 1])
# top-10 neighbour overlap
ov = []
for i in range(300):
    a = set(np.argsort(-full[i])[1:11]); b = set(np.argsort(-red[i])[1:11]); ov.append(len(a & b) / 10)
print('top-10 neighbour overlap %.3f' % np.mean(ov))
json.dump({'dim': DIM, 'scale': SCALE, 'mean': mean.round(6).tolist(), 'W': W.round(6).tolist()}, open(OUT, 'w'))
