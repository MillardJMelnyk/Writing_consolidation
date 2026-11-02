"""Turn raw Substack profile feed pages into a normalized entries.json and download images."""
import json, glob, os, sys, hashlib, html, time, urllib.request, io
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

RAW, IMGDIR, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
ME = 109147589

items = []
for f in sorted(glob.glob(os.path.join(RAW, 'page_*.json'))):
    items += json.load(open(f))['items']

esc = html.escape


def render(node):
    t = node.get('type')
    kids = ''.join(render(c) for c in node.get('content') or [])
    if t == 'text':
        s = esc(node.get('text', ''))
        for m in node.get('marks') or []:
            mt = m.get('type')
            if mt == 'bold': s = '<b>%s</b>' % s
            elif mt == 'italic': s = '<i>%s</i>' % s
            elif mt == 'link':
                href = (m.get('attrs') or {}).get('href', '')
                s = '<a href="%s">%s</a>' % (esc(href), s)
        return s
    if t == 'paragraph': return '<p>%s</p>' % kids
    if t == 'blockquote': return '<blockquote>%s</blockquote>' % kids
    if t == 'bulletList': return '<ul>%s</ul>' % kids
    if t == 'orderedList': return '<ol>%s</ol>' % kids
    if t == 'listItem': return '<li>%s</li>' % kids
    if t == 'hard_break' or t == 'hardBreak': return '<br>'
    if t == 'substack_mention':
        a = node.get('attrs') or {}
        return '@' + esc(str(a.get('name') or a.get('label') or ''))
    return kids


def body_html(c):
    if c.get('body_json'):
        return render(c['body_json'])
    return ''.join('<p>%s</p>' % esc(p) for p in (c.get('body') or '').split('\n') if p.strip())


def note_url(c):
    return 'https://substack.com/@%s/note/c-%s' % (c.get('handle') or '', c['id'])


images = {}  # url -> local filename


def img(url):
    if not url: return None
    if url not in images:
        images[url] = hashlib.sha1(url.encode()).hexdigest()[:16] + '.jpg'
    return images[url]


def video_cover(a):
    mu = a.get('mediaUpload') or {}
    if mu.get('post_id'):
        return 'https://substack-video.s3.amazonaws.com/video_upload/post/%s/%s/transcoded-00001.png' % (mu['post_id'], mu['id'])
    return 'https://substack-video.s3.amazonaws.com/video_upload/user/%s/%s/transcoded-00001.png' % (mu.get('user_id'), mu.get('id'))


def post_card(p, pub):
    pub = pub or {}
    return {'kind': 'post', 'title': p.get('title'), 'subtitle': p.get('subtitle') or p.get('description') or '',
            'preview': p.get('truncated_body_text') or '', 'url': p.get('canonical_url'),
            'cover': img(p.get('cover_image')), 'pub': pub.get('name') or '',
            'author': ', '.join(b.get('name', '') for b in p.get('publishedBylines') or []),
            'date': p.get('post_date')}


def attachments(c):
    out = []
    for a in c.get('attachments') or []:
        t = a.get('type')
        if t == 'image':
            out.append({'kind': 'image', 'img': img(a.get('imageUrl'))})
        elif t == 'video':
            out.append({'kind': 'video', 'img': img(video_cover(a))})
        elif t == 'link':
            m = a.get('linkMetadata') or {}
            out.append({'kind': 'link', 'url': m.get('url'), 'host': m.get('host'), 'title': m.get('title'),
                        'desc': m.get('description') or '', 'img': img(m.get('image'))})
        elif t == 'post' and a.get('post'):
            out.append(post_card(a['post'], a.get('publication')))
        elif t == 'comment' and a.get('comment'):
            q = a['comment']
            out.append({'kind': 'quote', 'name': q.get('name'), 'date': q.get('date'), 'html': body_html(q),
                        'url': note_url(q), 'atts': attachments(q)})
        elif t == 'publication' and a.get('publication'):
            p = a['publication']
            out.append({'kind': 'pub', 'name': p.get('name'), 'desc': p.get('hero_text') or '',
                        'url': 'https://%s.substack.com' % p.get('subdomain'), 'img': img(p.get('logo_url'))})
        elif t == 'missing':
            out.append({'kind': 'missing', 'reason': a.get('reason')})
    return out


entries = []
for i in items:
    ctx = (i.get('context') or {}).get('type')
    e = {'ctx': ctx, 'when': (i.get('context') or {}).get('timestamp')}
    if i['type'] == 'comment':
        c = i['comment']
        e.update({'name': c.get('name'), 'mine': c.get('user_id') == ME, 'date': c.get('date'),
                  'html': body_html(c), 'url': note_url(c), 'atts': attachments(c)})
    elif i['type'] == 'post':
        e.update({'card': post_card(i['post'], i.get('publication'))})
    elif i['type'] == 'chat':
        cp = i['community_post']
        e.update({'date': cp.get('created_at'), 'html': ''.join('<p>%s</p>' % esc(x) for x in (cp.get('body') or '').split('\n') if x.strip()),
                  'atts': [{'kind': 'image', 'img': img(m.get('url'))} for m in cp.get('media_assets') or [] if m.get('url')]})
    entries.append(e)


def fetch(item):
    url, name = item
    path = os.path.join(IMGDIR, name)
    if os.path.exists(path): return name, True
    for attempt in range(3):
        try:
            data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read()
            im = Image.open(io.BytesIO(data))
            im.seek(0)
            im = im.convert('RGB')
            if im.width > 1000:
                im = im.resize((1000, int(im.height * 1000 / im.width)))
            im.save(path, 'JPEG', quality=80)
            return name, True
        except Exception as ex:
            err = ex
            time.sleep(2)
    return name, False


with ThreadPoolExecutor(8) as ex:
    res = list(ex.map(fetch, images.items()))
failed = {n for n, ok in res if not ok}
print('images', len(images), 'failed', len(failed))

json.dump({'entries': entries, 'failed': sorted(failed)}, open(OUT, 'w'))
print('entries', len(entries))
