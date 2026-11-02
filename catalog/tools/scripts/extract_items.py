"""Extract every catalog item (Substack + AI chats) into items.jsonl, digests in batches, and a titles list."""
import json, glob, os, re, sys, urllib.parse
from bs4 import BeautifulSoup
from markdownify import markdownify as md

SUB_RAW, SUB_ENTRIES, CHATS, OUT = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
os.makedirs(os.path.join(OUT, 'batches'), exist_ok=True)
BATCH_CHARS = 200_000

items = []

# ---------- Substack ----------
raw = []
for f in sorted(glob.glob(os.path.join(SUB_RAW, 'page_*.json'))):
    raw += json.load(open(f))['items']
entries = json.load(open(SUB_ENTRIES))['entries']
assert len(raw) == len(entries)
TYPE = {'note': 'Substack note', 'comment_restack': 'Substack restacked note', 'post': 'Substack post',
        'post_restack': 'Substack restacked post', 'chat_subscribed': 'Substack chat'}


def img_urls(r):
    urls = []
    def walk_att(atts):
        for a in atts or []:
            t = a.get('type')
            if t == 'image': urls.append(a.get('imageUrl'))
            elif t == 'video':
                mu = a.get('mediaUpload') or {}
                kind, oid = ('post', mu['post_id']) if mu.get('post_id') else ('user', mu.get('user_id'))
                urls.append('https://substack-video.s3.amazonaws.com/video_upload/%s/%s/%s/transcoded-00001.png' % (kind, oid, mu.get('id')))
            elif t == 'link' and (a.get('linkMetadata') or {}).get('image'): urls.append(a['linkMetadata']['image'])
            elif t == 'post' and (a.get('post') or {}).get('cover_image'): urls.append(a['post']['cover_image'])
            elif t == 'comment' and a.get('comment'): walk_att(a['comment'].get('attachments'))
    if r.get('comment'): walk_att(r['comment'].get('attachments'))
    if r.get('post') and r['post'].get('cover_image'): urls.append(r['post']['cover_image'])
    if r.get('community_post'):
        urls += [m.get('url') for m in r['community_post'].get('media_assets') or [] if m.get('url')]
    return [u for u in urls if u]


def att_md(atts):
    out = []
    for a in atts or []:
        k = a['kind']
        if k == 'link':
            out.append('> **Link:** [%s](%s)  \n> %s' % (a.get('title') or a.get('url'), a.get('url'), (a.get('desc') or '').replace('\n', ' ')))
        elif k == 'post':
            out.append('> **Post:** [%s](%s) — %s%s  \n> %s' % (a.get('title') or '', a.get('url') or '', a.get('pub') or '',
                       (' · ' + a['author']) if a.get('author') else '', a.get('subtitle') or ''))
        elif k == 'quote':
            q = md(a.get('html') or '').strip().replace('\n', '\n> ')
            out.append('> **Quoted note — %s, %s:** [link](%s)  \n> %s' % (a.get('name') or '', (a.get('date') or '')[:10], a.get('url'), q))
            out += att_md(a.get('atts'))
        elif k == 'pub':
            out.append('> **Publication:** [%s](%s) — %s' % (a.get('name') or '', a.get('url') or '', a.get('desc') or ''))
        elif k == 'video':
            out.append('*(video — cover image below)*')
        elif k == 'missing':
            out.append('*(attachment %s)*' % (a.get('reason') or 'missing'))
    return out


for r, e in zip(raw, entries):
    ctx = e['ctx']
    date = (e.get('date') or e.get('when') or '')
    if 'card' in e:
        c = e['card']
        title = c.get('title') or '(untitled post)'
        text = '**%s**  \n%s%s\n\n%s\n\n%s' % (title, c.get('pub') or '', (' · ' + c['author']) if c.get('author') else '',
                                           c.get('subtitle') or '', c.get('preview') or '')
        url = c.get('url')
        date = e.get('when') or c.get('date') or ''
        author = c.get('author') or c.get('pub') or ''
    else:
        body = md(e.get('html') or '').strip()
        parts = [body] + att_md(e.get('atts'))
        text = '\n\n'.join(p for p in parts if p)
        first = re.sub(r'\s+', ' ', re.sub(r'[*_>#\[\]]', '', body)).strip()
        title = (first[:90] + ('…' if len(first) > 90 else '')) or '(no text)'
        url = e.get('url') or 'https://substack.com/@millardjmelnyk'
        author = e.get('name') or 'Millard J Melnyk'
        if ctx == 'comment_restack': date = e.get('when') or date
    items.append({'id': 'S-' + r['entity_key'], 'source': 'Substack', 'type': TYPE.get(ctx, ctx), 'date': date[:10],
                  'title': title, 'author': author, 'url_original': url, 'url_repo': '', 'text': text, 'images': img_urls(r)})

# ---------- AI chats ----------
def chat_files():
    for acct, folder in (('MJM', 'Claude MJM export chats on 2026-10-31'), ('MM', 'Claude M.M export chats on 2026-10-31')):
        for f in sorted(glob.glob(os.path.join(CHATS, folder, 'chats', '*.html'))):
            yield acct, folder, f


for acct, folder, f in chat_files():
    soup = BeautifulSoup(open(f, encoding='utf-8').read(), 'html.parser')
    title = soup.find('h1').get_text(strip=True)
    meta = soup.find(class_='meta').get_text(' ', strip=True)
    m = re.search(r'Created (\d{4}-\d\d-\d\d)', meta)
    date = m.group(1) if m else ''
    orig = soup.find(class_='meta').find('a')
    orig = orig['href'] if orig else ''
    msgs = []
    for d in soup.find_all('div', class_='msg'):
        cls = d.get('class')
        who_el = d.find(class_='who')
        who_txt = who_el.get_text(' ', strip=True) if who_el else ''
        human = ('human' in cls) or ('h' in cls) or who_txt.upper().startswith('MILLARD')
        ts = re.search(r'\d{4}-\d\d-\d\d \d\d:\d\d', who_txt)
        if who_el: who_el.extract()
        msgs.append({'human': human, 'ts': ts.group(0) if ts else '', 'md': md(str(d)).strip()})
    stem = os.path.basename(f)[:-5]
    cid = 'C-%s-%s' % (acct, stem.split('-')[0] if acct == 'MJM' else stem.rsplit('_', 1)[-1])
    text = '\n\n'.join('### %s · %s\n\n%s' % ('Millard' if x['human'] else 'Claude', x['ts'], x['md']) for x in msgs)
    rel = '%s/chats/%s' % (folder, os.path.basename(f))
    items.append({'id': cid, 'source': 'AI chat (%s account)' % acct, 'type': 'AI chat', 'date': date, 'title': title,
                  'author': 'Millard & Claude', 'url_original': orig,
                  'url_repo': 'https://github.com/MillardJMelnyk/AI_Chats/blob/main/' + urllib.parse.quote(rel),
                  'text': text, 'msgs': msgs, 'images': []})

ids = [i['id'] for i in items]
assert len(ids) == len(set(ids)), 'duplicate ids'


def cap(s, n):
    s = re.sub(r'\s+', ' ', s).strip()
    return s if len(s) <= n else s[:n] + ' […]'


def digest(it):
    if it['type'] == 'AI chat':
        msgs = it['msgs']
        hum = [m['md'] for m in msgs if m['human']]
        cl = [m['md'] for m in msgs if not m['human']]
        parts, used = [], 0
        for h in hum:
            if used >= 3500: break
            c = cap(h, min(700, 3500 - used)); parts.append('MILLARD: ' + c); used += len(c)
        if cl: parts.append('CLAUDE (first reply): ' + cap(cl[0], 700))
        if len(cl) > 1: parts.append('CLAUDE (last reply): ' + cap(cl[-1], 700))
        body = '\n'.join(parts)
    else:
        body = cap(it['text'], 2500)
    return '=== ID: %s | %s | %s | %s\n%s\n' % (it['id'], it['type'], it['date'], it['title'], body)


batches, cur, size = [], [], 0
for it in items:
    d = digest(it)
    if cur and size + len(d) > BATCH_CHARS:
        batches.append(cur); cur, size = [], 0
    cur.append(d); size += len(d)
batches.append(cur)
for n, b in enumerate(batches, 1):
    open(os.path.join(OUT, 'batches', 'batch_%02d.txt' % n), 'w', encoding='utf-8').write('\n'.join(b))

with open(os.path.join(OUT, 'titles.txt'), 'w', encoding='utf-8') as fh:
    for it in items:
        fh.write('%s | %s | %s | %s\n' % (it['id'], it['type'], it['date'], cap(it['title'], 100)))

with open(os.path.join(OUT, 'items.jsonl'), 'w', encoding='utf-8') as fh:
    for it in items:
        it.pop('msgs', None)
        fh.write(json.dumps(it, ensure_ascii=False) + '\n')

print('items', len(items), 'substack', sum(1 for i in items if i['source'] == 'Substack'),
      'chats', sum(1 for i in items if i['type'] == 'AI chat'), 'batches', len(batches))
