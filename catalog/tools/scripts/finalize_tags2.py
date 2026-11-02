"""Merge pass-2 tags: fold NEW topics in, normalize terms, write tags_final2.jsonl and tree_with_counts2.md."""
import json, glob, os, sys, collections

CAT = sys.argv[1]
DROP_TERMS = {'substack note', 'image post', 'millard j melnyk', 'untitled conversation', 'empty record', 'empty note',
              'media-only note', 'image', 'meme'}

tree, order, top = {}, [], None
for l in open(os.path.join(CAT, 'tree_v1.md'), encoding='utf-8'):
    l = l.rstrip()
    if l.startswith('# '): top = l[2:]; tree[top] = []; order.append(top)
    elif l.startswith('- '): tree[top].append(l[2:])
base_paths = {'%s > %s' % (t, s) for t in tree for s in tree[t]}

recs = {}
for f in sorted(glob.glob(os.path.join(CAT, 'out2', 'batch_*.jsonl'))):
    for line in open(f, encoding='utf-8'):
        if line.strip():
            r = json.loads(line); recs[r['id']] = r

old = {json.loads(l)['id']: json.loads(l) for l in open(os.path.join(CAT, 'tags_final.jsonl'), encoding='utf-8')}
fix = json.load(open(os.path.join(CAT, 'empty_fix.json')))
skip = set(fix['drop']) | set(fix['recover'])
order_ids = [json.loads(l)['id'] for l in open(os.path.join(CAT, 'items.jsonl'), encoding='utf-8')]
want = [i for i in order_ids if not old[i].get('coding') and i not in skip]
missing = [i for i in want if i not in recs]
if missing: sys.exit('missing %d: %s' % (len(missing), missing[:5]))

forms = collections.defaultdict(collections.Counter)
for i in want:
    r = recs[i]
    tops = []
    for p in r.get('topics') or []:
        p = p[4:].strip() if p.startswith('NEW:') else p.strip()
        if p not in tops: tops.append(p)
    r['topics'] = tops
    r['terms'] = [t.strip() for t in r.get('terms') or [] if t.strip() and t.strip().lower() not in DROP_TERMS]
    for t in r['terms']: forms[t.lower()][t] += 1
canon = {k: v.most_common(1)[0][0] for k, v in forms.items()}
for i in want:
    r = recs[i]; seen, out = set(), []
    for t in r['terms']:
        c = canon[t.lower()]
        if c not in seen: seen.add(c); out.append(c)
    r['terms'] = out

with open(os.path.join(CAT, 'tags_final2.jsonl'), 'w', encoding='utf-8') as fh:
    for i in want: fh.write(json.dumps(recs[i], ensure_ascii=False) + '\n')

cnt = collections.Counter(); topset = collections.defaultdict(set)
for i in want:
    for p in recs[i]['topics']:
        cnt[p] += 1; topset[p.split(' > ')[0]].add(i)
full = collections.OrderedDict((t, list(tree[t])) for t in order)
for p in cnt:
    t, s = p.split(' > ', 1)
    full.setdefault(t, [])
    if s not in full[t]: full[t].append(s)
lines = []
for t in sorted(full, key=lambda t: -len(topset[t])):
    lines.append('# %s (%d items)%s' % (t, len(topset[t]), '' if t in tree else '  [NEW]'))
    for s in sorted(full[t], key=lambda s: -cnt['%s > %s' % (t, s)]):
        p = '%s > %s' % (t, s)
        lines.append('- %s (%d)%s' % (s, cnt[p], '' if p in base_paths else '  [NEW]'))
    lines.append('')
open(os.path.join(CAT, 'tree_with_counts2.md'), 'w', encoding='utf-8').write('\n'.join(lines))
tc = collections.Counter(len(recs[i]['topics']) for i in want)
print('items', len(want), 'topics', len(full), 'subheadings', sum(len(v) for v in full.values()),
      'distinct terms', len(canon), 'subheadings per item', sorted(tc.items()),
      'empty subheadings', sum(1 for t in full for s in full[t] if cnt['%s > %s' % (t, s)] == 0))
