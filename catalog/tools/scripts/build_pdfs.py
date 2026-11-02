"""Render entries.json into searchable PDFs, each under a size budget."""
import json, os, sys, html
from playwright.sync_api import sync_playwright

ENTRIES, IMGDIR, OUTDIR = sys.argv[1], sys.argv[2], sys.argv[3]
BUDGET = 70 * 1024 * 1024
data = json.load(open(ENTRIES))
entries, failed = data['entries'], set(data['failed'])
esc = html.escape


def d(s):
    return (s or '')[:10]


def imgtag(name, cls='img'):
    if not name or name in failed: return '<div class="noimg">[image unavailable]</div>' if name else ''
    return '<img class="%s" src="file://%s">' % (cls, os.path.join(IMGDIR, name))


def link(url, text=None):
    return '<a href="%s">%s</a>' % (esc(url or ''), esc(text or url or ''))


def att(a):
    k = a['kind']
    if k == 'image': return imgtag(a['img'])
    if k == 'video': return '<div class="vid"><div class="lbl">Video (cover image)</div>%s</div>' % imgtag(a['img'])
    if k == 'link':
        return '<div class="card">%s<div class="host">%s</div><div class="ttl">%s</div><div class="desc">%s</div><div class="url">%s</div></div>' % (
            imgtag(a.get('img'), 'thumb'), esc(a.get('host') or ''), esc(a.get('title') or ''), esc(a.get('desc') or ''), link(a.get('url')))
    if k == 'post': return postcard(a)
    if k == 'quote':
        return '<div class="card quote"><div class="hdr"><b>%s</b> · %s</div>%s%s<div class="url">%s</div></div>' % (
            esc(a.get('name') or ''), d(a.get('date')), a.get('html') or '', ''.join(att(x) for x in a.get('atts') or []), link(a.get('url')))
    if k == 'pub':
        return '<div class="card">%s<div class="ttl">%s</div><div class="desc">%s</div><div class="url">%s</div></div>' % (
            imgtag(a.get('img'), 'thumb'), esc(a.get('name') or ''), esc(a.get('desc') or ''), link(a.get('url')))
    if k == 'missing': return '<div class="noimg">[attachment %s]</div>' % esc(a.get('reason') or 'missing')
    return ''


def postcard(p):
    return '<div class="card post">%s<div class="pub">%s%s</div><div class="ttl">%s</div><div class="desc">%s</div><div class="prev">%s</div><div class="url">%s · %s</div></div>' % (
        imgtag(p.get('cover')), esc(p.get('pub') or ''), (' · ' + esc(p['author'])) if p.get('author') else '',
        esc(p.get('title') or ''), esc(p.get('subtitle') or ''), esc(p.get('preview') or ''), d(p.get('date')), link(p.get('url')))


LABEL = {'note': 'Note', 'comment_restack': 'You restacked a note', 'post': 'Post', 'post_restack': 'You restacked a post',
         'chat_subscribed': 'Chat'}


def entry(e):
    lab = LABEL.get(e['ctx'], e['ctx'])
    if 'card' in e:
        return '<div class="entry"><div class="lab">%s · %s</div>%s</div>' % (lab, d(e.get('when')), postcard(e['card']))
    who = esc(e.get('name') or 'Millard J Melnyk')
    hdr = '<div class="lab">%s%s</div><div class="hdr"><b>%s</b> · %s</div>' % (
        lab, (' · ' + d(e.get('when'))) if e['ctx'] == 'comment_restack' else '', who, d(e.get('date')))
    body = (e.get('html') or '') + ''.join(att(a) for a in e.get('atts') or [])
    url = '<div class="url">%s</div>' % link(e['url']) if e.get('url') else ''
    return '<div class="entry">%s%s%s</div>' % (hdr, body, url)


CSS = """
body{font-family:Georgia,serif;font-size:11pt;color:#111;margin:0}
.profile{border-bottom:2px solid #333;padding-bottom:10px;margin-bottom:16px}
.profile h1{margin:0;font-size:20pt}.profile .sub{color:#555}
.entry{border-bottom:1px solid #ccc;padding:10px 0 12px;}
.lab{font-family:Arial,sans-serif;font-size:8.5pt;color:#777;text-transform:uppercase;letter-spacing:.04em}
.hdr{font-family:Arial,sans-serif;font-size:10pt;margin:2px 0 4px}
p{margin:4px 0}blockquote{border-left:3px solid #bbb;margin:6px 0;padding-left:10px;color:#333}
.img{max-width:100%;max-height:820px;display:block;margin:6px 0;break-inside:avoid}
.thumb{max-width:180px;max-height:140px;float:right;margin-left:8px}
.card{border:1px solid #ddd;border-radius:6px;padding:8px;margin:6px 0;overflow:hidden;font-family:Arial,sans-serif;font-size:9.5pt}
.card .ttl{font-weight:bold;font-size:10.5pt}.card .desc,.card .prev{color:#444}.host,.pub{color:#777;font-size:8.5pt}
.url{font-family:Arial,sans-serif;font-size:8pt;color:#1a5fb4;word-break:break-all;margin-top:4px;clear:both}
a{color:#1a5fb4}.noimg{color:#999;font-style:italic;font-size:9pt}
.vid .lbl{font-family:Arial,sans-serif;font-size:8.5pt;color:#777}
"""

# split into parts by image bytes
def ebytes(e):
    names = []
    def walk(a):
        for k in ('img', 'cover'):
            if a.get(k): names.append(a[k])
        for x in a.get('atts') or []: walk(x)
    walk(e)
    if 'card' in e: walk(e['card'])
    return sum(os.path.getsize(os.path.join(IMGDIR, n)) for n in names if n not in failed and os.path.exists(os.path.join(IMGDIR, n)))

parts, cur, size = [], [], 0
for e in entries:
    b = ebytes(e)
    if cur and size + b > BUDGET:
        parts.append(cur); cur, size = [], 0
    cur.append(e); size += b
parts.append(cur)

os.makedirs(OUTDIR, exist_ok=True)
with sync_playwright() as pw:
    br = pw.chromium.launch()
    pg = br.new_page()
    for n, part in enumerate(parts, 1):
        first, last = d(part[0].get('when') or part[0].get('date')), d(part[-1].get('when') or part[-1].get('date'))
        head = ''
        if n == 1:
            head = '<div class="profile"><h1>Millard J Melnyk</h1><div class="sub">@millardjmelnyk · Dismantling the mentality of codependence and servility · ReLOVEution NOW!</div><div class="sub">Everything listed on https://substack.com/@millardjmelnyk, newest first. Captured 2026-11-01. %d items in %d parts.</div></div>' % (len(entries), len(parts))
        htmldoc = '<html><head><meta charset="utf-8"><style>%s</style></head><body>%s<div class="lab">Part %d of %d · %s back to %s</div>%s</body></html>' % (
            CSS, head, n, len(parts), first, last, ''.join(entry(e) for e in part))
        hp = os.path.join(OUTDIR, 'part%d.html' % n)
        open(hp, 'w', encoding='utf-8').write(htmldoc)
        pg.goto('file://' + hp, wait_until='load', timeout=600000)
        name = 'Substack_millardjmelnyk_profile_part%d_of_%d_%s_to_%s.pdf' % (n, len(parts), first, last)
        pg.pdf(path=os.path.join(OUTDIR, name), format='Letter', margin={'top': '0.6in', 'bottom': '0.6in', 'left': '0.6in', 'right': '0.6in'},
               print_background=True, display_header_footer=True, header_template='<span></span>',
               footer_template='<div style="font-size:8px;width:100%%;text-align:center;color:#888">Part %d · page <span class="pageNumber"></span> of <span class="totalPages"></span></div>' % n)
        os.remove(hp)
        print(name, len(part), os.path.getsize(os.path.join(OUTDIR, name)) // 1048576, 'MB', flush=True)
    br.close()
