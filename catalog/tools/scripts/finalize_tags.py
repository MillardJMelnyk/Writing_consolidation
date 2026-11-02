"""Merge agent outputs into tags_final.jsonl: fold NEW topics in, merge duplicates, normalize terms; write tree with counts."""
import json, glob, os, sys, collections

CAT = sys.argv[1]
SEED = os.path.join(CAT, 'seed_tree.md')
EMPTY = 'Unsorted > Empty or untitled chats'
MERGE = {
    'Uncategorized > Empty chats': EMPTY, 'Uncategorized > Empty chat': EMPTY, 'Uncategorized > Empty or untitled chat': EMPTY,
    'AI chatbots and working with Claude > Empty or untitled chats': EMPTY,
    'Writing, Substack and publishing > Empty or textless items': 'Writing, Substack and publishing > Media-only notes',
    'Writing, Substack and publishing > Empty or media-only notes': 'Writing, Substack and publishing > Media-only notes',
    'Practical & personal > Online scams and marketing schemes': 'Practical & personal > Scams and fraud checks',
}
DROP_TERMS = {'substack note', 'image post', 'millard j melnyk', 'untitled conversation', 'empty record', 'empty note', 'media-only note'}

seed, order, top = {}, [], None
for l in open(SEED, encoding='utf-8'):
    l = l.rstrip()
    if l.startswith('# '): top = l[2:]; seed[top] = []; order.append(top)
    elif l.startswith('- '): seed[top].append(l[2:])
seed_paths = {'%s > %s' % (t, s) for t in seed for s in seed[t]}

recs = {}
for f in sorted(glob.glob(os.path.join(CAT, 'out', 'batch_*.jsonl'))):
    for line in open(f, encoding='utf-8'):
        if line.strip():
            r = json.loads(line); recs[r['id']] = r

items = [json.loads(l)['id'] for l in open(os.path.join(CAT, 'items.jsonl'), encoding='utf-8')]
missing = [i for i in items if i not in recs]
if missing: sys.exit('missing %d: %s' % (len(missing), missing[:5]))

term_forms = collections.defaultdict(collections.Counter)
for r in recs.values():
    if r.get('coding'): r['topics'], r['terms'] = [], []; continue
    empty = any(t.strip().lower() == 'empty record' for t in r.get('terms') or [])
    tops = []
    for p in r.get('topics') or []:
        p = p[4:].strip() if p.startswith('NEW:') else p.strip()
        p = MERGE.get(p, p)
        if p not in tops: tops.append(p)
    if empty: tops = [EMPTY]
    r['topics'] = tops
    terms = [t.strip() for t in r.get('terms') or [] if t.strip() and t.strip().lower() not in DROP_TERMS]
    if EMPTY in tops: terms = []
    if 'Writing, Substack and publishing > Media-only notes' in tops: terms = [t for t in terms if t.lower() != 'substack']
    r['terms'] = terms
    for t in terms: term_forms[t.lower()][t] += 1

canon = {k: v.most_common(1)[0][0] for k, v in term_forms.items()}
for r in recs.values():
    seen, out = set(), []
    for t in r['terms']:
        c = canon[t.lower()]
        if c not in seen: seen.add(c); out.append(c)
    r['terms'] = out

with open(os.path.join(CAT, 'tags_final.jsonl'), 'w', encoding='utf-8') as fh:
    for i in items: fh.write(json.dumps(recs[i], ensure_ascii=False) + '\n')

# tree with counts
cnt = collections.Counter(); topcnt = collections.defaultdict(set)
for r in recs.values():
    for p in r['topics']:
        cnt[p] += 1; topcnt[p.split(' > ')[0]].add(r['id'])
tree = collections.OrderedDict((t, list(seed[t])) for t in order)
for p in cnt:
    t, s = p.split(' > ', 1)
    tree.setdefault(t, [])
    if s not in tree[t]: tree[t].append(s)
tops_sorted = sorted(tree, key=lambda t: (t == 'Unsorted', -len(topcnt[t])))
lines = []
for t in tops_sorted:
    lines.append('# %s (%d items)%s' % (t, len(topcnt[t]), '' if t in seed else '  [NEW]'))
    for s in sorted(tree[t], key=lambda s: -cnt['%s > %s' % (t, s)]):
        p = '%s > %s' % (t, s)
        lines.append('- %s (%d)%s' % (s, cnt[p], '' if p in seed_paths else '  [NEW]'))
    lines.append('')
open(os.path.join(CAT, 'tree_with_counts.md'), 'w', encoding='utf-8').write('\n'.join(lines))
nc = sum(1 for r in recs.values() if r.get('coding'))
print('records', len(recs), 'coding', nc, 'catalogued', len(recs) - nc, 'top', len(tree), 'subs', sum(len(v) for v in tree.values()),
      'distinct terms', len(canon))
