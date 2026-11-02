"""Build the full catalog (item pages, data lists, item lists, A-Z index, topic outline) as GitHub Markdown."""
import json, os, sys, re, csv, collections, unicodedata, datetime

ITEMS, TAGS, CAT = sys.argv[1], sys.argv[2], sys.argv[3]
tags = [json.loads(l) for l in open(TAGS, encoding='utf-8')]
tagmap = {t['id']: t for t in tags}
allitems = {json.loads(l)['id']: json.loads(l) for l in open(ITEMS, encoding='utf-8')}
items = [allitems[t['id']] for t in tags]
for d in ('items', 'data', 'list', 'index', 'index/terms', 'topics'):
    os.makedirs(os.path.join(CAT, d), exist_ok=True)
TODAY = datetime.date.today().isoformat()


def cell(s):
    return re.sub(r'\s+', ' ', (s or '')).replace('|', '\\|').replace('[', '\\[').replace(']', '\\]').strip()


def slug(s, used=None):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:80] or 'x'
    if used is not None:
        base, n = s, 2
        while s in used: s = '%s-%d' % (base, n); n += 1
        used.add(s)
    return s


def title_key(it):
    return re.sub(r'^[^A-Za-z0-9]+', '', it['title']).lower() or it['title'].lower()


def first_letter(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'^[^A-Za-z0-9]+', '', s)
    c = s[:1].upper()
    return c if c.isalpha() else '0-9'


# ---------- item pages ----------
for it in items:
    t = tagmap[it['id']]
    L = ['# %s' % cell(it['title']), '', '| | |', '|---|---|', '| Date | %s |' % it['date'], '| Type | %s |' % it['type'],
         '| Source | %s |' % it['source'], '| By | %s |' % cell(it['author']), '| Catalog ID | `%s` |' % it['id']]
    links = []
    if it.get('url_original'): links.append('[Original](%s)' % it['url_original'])
    if it.get('url_repo'): links.append('[Archived file](%s)' % it['url_repo'])
    if links: L.append('| Links | %s |' % ' · '.join(links))
    L += ['', '**Summary:** %s' % t.get('summary', '')]
    if t.get('caption'): L += ['', '**Image:** %s' % t['caption']]
    L += ['', '**Topics:** ' + '; '.join(t.get('topics') or []),
          '', '**Index terms:** ' + '; '.join(t.get('terms') or []),
          '', '[← Catalog home](../Master_catalog.md)', '', '---', '', it['text'] or '*(no text)*']
    if it.get('images'):
        L += ['', '---', '', '**Images**', ''] + ['![](%s)' % u for u in it['images']]
    open(os.path.join(CAT, 'items', it['id'] + '.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

# ---------- data lists ----------
FIELDS = ['id', 'date', 'type', 'title', 'author', 'summary', 'caption', 'topics', 'terms', 'url_original', 'url_repo', 'page']
groups = collections.defaultdict(list)
for it in items:
    groups['substack' if it['source'] == 'Substack' else 'ai_chats'].append(it)
for key, rows in groups.items():
    with open(os.path.join(CAT, 'data', key + '.csv'), 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, FIELDS); w.writeheader()
        for it in rows:
            t = tagmap[it['id']]
            w.writerow({'id': it['id'], 'date': it['date'], 'type': it['type'], 'title': it['title'], 'author': it['author'],
                        'summary': t.get('summary', ''), 'caption': t.get('caption', ''), 'topics': '; '.join(t.get('topics') or []),
                        'terms': '; '.join(t.get('terms') or []), 'url_original': it.get('url_original', ''),
                        'url_repo': it.get('url_repo', ''), 'page': 'items/%s.md' % it['id']})


# ---------- shared list writer ----------
def table(rows, prefix):
    out = ['| Date | Title | Type |', '|---|---|---|']
    for it in rows:
        out.append('| %s | [%s](%sitems/%s.md) | %s |' % (it['date'], cell(it['title']), prefix, it['id'], it['type']))
    return out


def item_list_page(path, heading, intro, rows, prefix, back):
    by_date = sorted(rows, key=lambda i: i['date'], reverse=True)
    by_title = sorted(rows, key=title_key)
    L = ['# %s' % heading, '', back, '']
    if intro: L += intro + ['']
    L += ['%d items · Sort: [by date](#by-date) · [by title](#by-title)' % len(rows), '', '## By date', ''] + table(by_date, prefix)
    L += ['', '## By title', ''] + table(by_title, prefix) + ['']
    open(path, 'w', encoding='utf-8').write('\n'.join(L))


HOME = '[← Catalog home](../Master_catalog.md)'

# ---------- full item list (split by year / by letter) ----------
years = collections.defaultdict(list); letters = collections.defaultdict(list)
for it in items:
    years[it['date'][:4] or 'undated'].append(it)
    letters[first_letter(it['title'])].append(it)
for y, rows in years.items():
    L = ['# All items — %s (by date)' % y, '', HOME + ' · [All items](All_items.md)', '', '%d items' % len(rows), ''] + \
        table(sorted(rows, key=lambda i: i['date'], reverse=True), '../') + ['']
    open(os.path.join(CAT, 'list', 'by-date-%s.md' % y), 'w', encoding='utf-8').write('\n'.join(L))
for c, rows in letters.items():
    L = ['# All items — %s (by title)' % c, '', HOME + ' · [All items](All_items.md)', '', '%d items' % len(rows), ''] + \
        table(sorted(rows, key=title_key), '../') + ['']
    open(os.path.join(CAT, 'list', 'by-title-%s.md' % c), 'w', encoding='utf-8').write('\n'.join(L))
L = ['# All items', '', HOME, '', '%d items.' % len(items), '', '## By date (newest first)', '']
L += ['- [%s](by-date-%s.md) — %d items' % (y, y, len(years[y])) for y in sorted(years, reverse=True)]
L += ['', '## By title', '', ' · '.join('[%s](by-title-%s.md)' % (c, c) for c in sorted(letters, key=lambda c: (c == '0-9', c))), '']
open(os.path.join(CAT, 'list', 'All_items.md'), 'w', encoding='utf-8').write('\n'.join(L))

# ---------- A-Z index ----------
term_items = collections.defaultdict(list)
for it in items:
    for term in tagmap[it['id']].get('terms') or []:
        term_items[term].append(it)
used = set(); term_slug = {}
for term in sorted(term_items, key=str.lower):
    term_slug[term] = slug(term, used)
    item_list_page(os.path.join(CAT, 'index', 'terms', term_slug[term] + '.md'), cell(term), None, term_items[term], '../../',
                   '[← Catalog home](../../Master_catalog.md) · [A–Z index](../A-Z_index.md) · [%s](../%s.md)' % (first_letter(term), first_letter(term)))
by_letter = collections.defaultdict(list)
for term in term_items: by_letter[first_letter(term)].append(term)
letter_list = sorted(by_letter, key=lambda c: (c == '0-9', c))
nav = ' · '.join('[%s](%s.md)' % (c, c) for c in letter_list)
for c in letter_list:
    L = ['# Index — %s' % c, '', '[← Catalog home](../Master_catalog.md) · [A–Z index](A-Z_index.md)', '', nav, '']
    L += ['- [%s](terms/%s.md) (%d)' % (cell(t), term_slug[t], len(term_items[t])) for t in sorted(by_letter[c], key=str.lower)]
    open(os.path.join(CAT, 'index', c + '.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
L = ['# A–Z index', '', HOME, '', 'Subjects, names and terms, like the index of a book. %d entries. Each entry opens the list of items it appears in.' % len(term_items), '']
L += ['- [%s](%s.md) — %d entries' % (c, c, len(by_letter[c])) for c in letter_list]
open(os.path.join(CAT, 'index', 'A-Z_index.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

# ---------- topic outline ----------
topic_items = collections.defaultdict(dict); sub_items = collections.defaultdict(list)
for it in items:
    for p in tagmap[it['id']].get('topics') or []:
        top, sub = p.split(' > ', 1)
        topic_items[top][it['id']] = it
        sub_items[(top, sub)].append(it)
used = set(); tslug = {t: slug(t, used) for t in topic_items}
sslug = {k: tslug[k[0]] + '--' + slug(k[1]) for k in sub_items}
tops_sorted = sorted(topic_items, key=lambda t: -len(topic_items[t]))
L = ['# Topic outline', '', HOME, '', '%d topics. Click a topic or a subheading to see its items.' % len(tops_sorted), '']
for t in tops_sorted:
    subs = sorted([k for k in sub_items if k[0] == t], key=lambda k: -len(sub_items[k]))
    L.append('## [%s](%s.md) (%d)' % (cell(t), tslug[t], len(topic_items[t])))
    L.append('')
    L += ['- [%s](%s.md) (%d)' % (cell(k[1]), sslug[k], len(sub_items[k])) for k in subs]
    L.append('')
    sublinks = ['- [%s](%s.md) (%d)' % (cell(k[1]), sslug[k], len(sub_items[k])) for k in subs]
    item_list_page(os.path.join(CAT, 'topics', tslug[t] + '.md'), cell(t), ['**Subheadings:**', ''] + sublinks,
                   list(topic_items[t].values()), '../', '[← Catalog home](../Master_catalog.md) · [Topic outline](Topic_outline.md)')
    for k in subs:
        item_list_page(os.path.join(CAT, 'topics', sslug[k] + '.md'), '%s › %s' % (cell(t), cell(k[1])), None, sub_items[k], '../',
                       '[← Catalog home](../Master_catalog.md) · [Topic outline](Topic_outline.md) · [%s](%s.md)' % (cell(t), tslug[t]))
open(os.path.join(CAT, 'topics', 'Topic_outline.md'), 'w', encoding='utf-8').write('\n'.join(L))

# ---------- home ----------
src = collections.Counter(it['source'] for it in items)
L = ['# Master catalog of Millard J Melnyk\'s work', '', 'Last updated: %s' % TODAY, '', '**New here? Read [How to use the catalog](How_to_use_the_catalog.md).**', '',
     '%d items: %s.' % (len(items), ', '.join('%d %s' % (n, s) for s, n in src.most_common())), '',
     '1. **[All items](list/All_items.md)** — every item, by date or by title.',
     '2. **[A–Z index](index/A-Z_index.md)** — %d subjects, names and terms.' % len(term_items),
     '3. **[Topic outline](topics/Topic_outline.md)** — %d topics, %d subheadings.' % (len(topic_items), len(sub_items)), '',
     'Data lists (one per source): ' + ' · '.join('[%s](data/%s.csv)' % (k, k) for k in sorted(groups)) + '.', '',
     'Not yet included: 190 coding chats ([list](data/set_aside_coding_chats.csv)).', '']
open(os.path.join(CAT, 'Master_catalog.md'), 'w', encoding='utf-8').write('\n'.join(L))
print('items', len(items), 'terms', len(term_items), 'topics', len(topic_items), 'subheadings', len(sub_items))
