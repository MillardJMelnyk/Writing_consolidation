"""Write one readable page per included item plus per-source data lists, from items.jsonl and agent tags."""
import json, glob, os, sys, csv

ITEMS, TAGS, CAT = sys.argv[1], sys.argv[2], sys.argv[3]
tags = {}
for f in sorted(glob.glob(os.path.join(TAGS, 'batch_*.jsonl'))):
    for line in open(f, encoding='utf-8'):
        line = line.strip()
        if line:
            t = json.loads(line); tags[t['id']] = t

items = [json.loads(l) for l in open(ITEMS, encoding='utf-8')]
missing = [i['id'] for i in items if i['id'] not in tags]
if missing:
    sys.exit('untagged items: %d e.g. %s' % (len(missing), missing[:5]))

os.makedirs(os.path.join(CAT, 'items'), exist_ok=True)
os.makedirs(os.path.join(CAT, 'data'), exist_ok=True)


def esc_md(s):
    return (s or '').replace('|', '\\|').replace('\n', ' ')


included, excluded = [], []
for it in items:
    t = tags[it['id']]
    if t.get('coding'):
        excluded.append((it, t)); continue
    included.append((it, t))
    lines = ['# %s' % esc_md(it['title']), '',
             '| | |', '|---|---|',
             '| Date | %s |' % it['date'], '| Type | %s |' % it['type'], '| Source | %s |' % it['source'],
             '| By | %s |' % esc_md(it['author']), '| Catalog ID | `%s` |' % it['id']]
    links = []
    if it.get('url_original'): links.append('[Original](%s)' % it['url_original'])
    if it.get('url_repo'): links.append('[Archived file](%s)' % it['url_repo'])
    if links: lines.append('| Links | %s |' % ' · '.join(links))
    lines += ['', '**Summary:** %s' % t.get('summary', ''), '']
    if t.get('topics'): lines.append('**Topics:** %s' % '; '.join(t['topics']))
    if t.get('terms'): lines.append('  \n**Index terms:** %s' % '; '.join(t['terms']))
    lines += ['', '[← Catalog home](../README.md)', '', '---', '', it['text']]
    if it.get('images'):
        lines += ['', '---', '', '**Images**', ''] + ['![](%s)' % u for u in it['images']]
    open(os.path.join(CAT, 'items', it['id'] + '.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')

FIELDS = ['id', 'date', 'type', 'title', 'author', 'summary', 'topics', 'terms', 'url_original', 'url_repo', 'page']
by_source = {}
for it, t in included:
    key = 'substack' if it['source'] == 'Substack' else 'ai_chats'
    by_source.setdefault(key, []).append((it, t))
for key, rows in by_source.items():
    with open(os.path.join(CAT, 'data', key + '.csv'), 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, FIELDS); w.writeheader()
        for it, t in rows:
            w.writerow({'id': it['id'], 'date': it['date'], 'type': it['type'], 'title': it['title'], 'author': it['author'],
                        'summary': t.get('summary', ''), 'topics': '; '.join(t.get('topics') or []),
                        'terms': '; '.join(t.get('terms') or []), 'url_original': it.get('url_original', ''),
                        'url_repo': it.get('url_repo', ''), 'page': 'items/%s.md' % it['id']})
with open(os.path.join(CAT, 'data', 'set_aside_coding_chats.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh); w.writerow(['id', 'date', 'title', 'url_repo'])
    for it, t in excluded:
        w.writerow([it['id'], it['date'], it['title'], it.get('url_repo', '')])
print('included', len(included), 'set aside (coding)', len(excluded))
