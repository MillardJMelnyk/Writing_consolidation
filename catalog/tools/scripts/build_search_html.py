"""Build Millards_master_writing_catalog.html with built-in meaning and exact-word search.

Usage: python3 build_search_html.py items.jsonl tags_final2.jsonl sem_dir out.html
sem_dir holds: page_template.html, app.js, core.js, marked.umd.js, tokenizer.js, ort.wasm.min.js, ort-wasm-simd-threaded.mjs,
ort-wasm-simd-threaded.wasm, model_quantized.onnx, vocab.txt, projection.json
The page contains no item text; on first use it reads the item pages from GitHub and builds catalog_search_index.js.
"""
import json, sys, os, gzip, base64, collections, datetime, html
import numpy as np

ITEMS, TAGS, SEM, OUT = sys.argv[1:5]
BASE = 'https://github.com/MillardJMelnyk/Writing_consolidation/blob/main/catalog/'
P = lambda f: os.path.join(SEM, f)
tags = [json.loads(l) for l in open(TAGS, encoding='utf-8')]
allitems = {json.loads(l)['id']: json.loads(l) for l in open(ITEMS, encoding='utf-8')}
items = [allitems[t['id']] for t in tags]

terms, topics, subs = set(), set(), set()
for t in tags:
    terms.update(t.get('terms') or [])
    for p in t.get('topics') or []:
        topics.add(p.split(' > ')[0]); subs.add(p)
src = collections.Counter(it['source'] for it in items)
srcline = ', '.join('{:,} {}'.format(n, s.replace('AI chat', 'AI chats') if s.startswith('AI chat') else s) for s, n in src.most_common())


def a(path, text):
    return '<a href="%s%s">%s</a>' % (BASE, path, html.escape(text))


b64 = lambda b: base64.b64encode(b).decode('ascii')
gzb64 = lambda path: b64(gzip.compress(open(path, 'rb').read(), 6))
mjs = open(P('ort-wasm-simd-threaded.mjs'), encoding='utf-8').read()
old = '(new URL("ort-wasm-simd-threaded.wasm",import.meta.url)).href'
assert mjs.count(old) == 1
mjs = mjs.replace(old, '"ort-wasm-simd-threaded.wasm"')  # the page supplies the engine binary itself
proj = json.load(open(P('projection.json')))
projbytes = np.concatenate([np.array(proj['mean'], np.float32), np.array(proj['W'], np.float32).reshape(-1)]).tobytes()
meta = [{'id': it['id'], 'date': it['date'], 'type': it['type'], 'title': it['title'], 'by': it['author']} for it in items]


def js_text(s):
    return s.replace('</script', '<\\/script')


page = open(P('page_template.html'), encoding='utf-8').read()
rep = {
    '@@TODAY@@': datetime.date.today().isoformat(),
    '@@HOWTO@@': a('How_to_use_the_catalog.md', 'How to use the catalog'),
    '@@TOTALS@@': '{:,} items: {}.'.format(len(items), srcline),
    '@@ALL@@': a('list/All_items.md', 'All items'), '@@AZ@@': a('index/A-Z_index.md', 'A–Z index'),
    '@@NTERMS@@': '{:,}'.format(len(terms)), '@@TOP@@': a('topics/Topic_outline.md', 'Topic outline'),
    '@@NTOP@@': str(len(topics)), '@@NSUB@@': str(len(subs)),
    '@@CSV1@@': a('data/ai_chats.csv', 'ai_chats.csv'), '@@CSV2@@': a('data/substack.csv', 'substack.csv'),
    '@@O1@@': a('list/About_the_item_lists.md', 'About_the_item_lists.md'),
    '@@O2@@': a('index/About_the_A-Z_index.md', 'About_the_A-Z_index.md'),
    '@@O3@@': a('topics/About_the_topic_outline.md', 'About_the_topic_outline.md'),
    '@@U1@@': a('tools/How_to_update_the_catalog.md', 'How_to_update_the_catalog.md'),
    '@@U2@@': a('tools/Topic_tree_with_counts.md', 'Topic_tree_with_counts.md'),
    '@@U3@@': a('data/set_aside_coding_chats.csv', 'set_aside_coding_chats.csv'),
    '/*@@ORTJS@@*/': js_text(open(P('ort.wasm.min.js'), encoding='utf-8').read()),
    '/*@@TOKENIZER@@*/': js_text(open(P('tokenizer.js'), encoding='utf-8').read()),
    '/*@@CORE@@*/': js_text(open(P('core.js'), encoding='utf-8').read()),
    '/*@@MARKED@@*/': js_text(open(P('marked.umd.js'), encoding='utf-8').read()),
    '/*@@ITEMS@@*/': js_text(json.dumps(meta, ensure_ascii=False)),
    '/*@@MJS@@*/': b64(mjs.encode('utf-8')),
    '/*@@WASM@@*/': gzb64(P('ort-wasm-simd-threaded.wasm')),
    '/*@@MODEL@@*/': gzb64(P('model_quantized.onnx')),
    '/*@@PROJ@@*/': b64(projbytes),
    '/*@@VOCAB@@*/': json.dumps(open(P('vocab.txt'), encoding='utf-8').read()),
    '/*@@DIM@@*/': str(proj['dim']), '/*@@SCALE@@*/': str(proj['scale']),
    '/*@@APP@@*/': js_text(open(P('app.js'), encoding='utf-8').read()),
}
for k, v in rep.items():
    assert k in page, k
    page = page.replace(k, v)
open(OUT, 'w', encoding='utf-8').write(page)
print('items', len(items), 'html MB %.1f' % (len(page) / 1e6))
