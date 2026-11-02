"""Build Master_catalog.html: a standalone copy of the master catalog page with full-text search of every item."""
import json, sys, re, gzip, base64, collections, datetime, html

ITEMS, TAGS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
BASE = 'https://github.com/MillardJMelnyk/Writing_consolidation/blob/main/catalog/'
tags = [json.loads(l) for l in open(TAGS, encoding='utf-8')]
allitems = {json.loads(l)['id']: json.loads(l) for l in open(ITEMS, encoding='utf-8')}
items = [allitems[t['id']] for t in tags]


def plain(md):
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', md or '')
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'[*_#>`|]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


rows = [[it['id'], it['date'], it['type'], it['title'], plain(it['title'] + ' ' + it['text'])] for it in items]
blob = base64.b64encode(gzip.compress(json.dumps(rows, ensure_ascii=False).encode('utf-8'), 9)).decode('ascii')

terms = set(); topics = set(); subs = set()
for t in tags:
    terms.update(t.get('terms') or [])
    for p in t.get('topics') or []:
        topics.add(p.split(' > ')[0]); subs.add(p)
src = collections.Counter(it['source'] for it in items)
srcline = ', '.join('{:,} {}'.format(n, s.replace('AI chat', 'AI chats') if s.startswith('AI chat') else s) for s, n in src.most_common())
today = datetime.date.today().isoformat()


def a(path, text):
    return '<a href="%s%s">%s</a>' % (BASE, path, html.escape(text))


page = '''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Master catalog of Millard J Melnyk's work</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:-apple-system,"Segoe UI",Arial,sans-serif;max-width:900px;margin:30px auto;padding:0 20px;color:#1f2328;line-height:1.5}
h1{font-size:28px;border-bottom:1px solid #d0d7de;padding-bottom:8px}h2{font-size:21px;border-bottom:1px solid #d0d7de;padding-bottom:6px;margin-top:28px}
a{color:#0969da}#q{width:70%%;font-size:16px;padding:7px 9px;border:1px solid #8c959f;border-radius:6px}
button{font-size:16px;padding:7px 14px;border-radius:6px;border:1px solid #8c959f;background:#f6f8fa;cursor:pointer}
#status{color:#59636e;margin:8px 0}.r{padding:8px 0;border-bottom:1px solid #eaeef2}.r .m{color:#59636e;font-size:13px}.r .s{font-size:14px;color:#333}
mark{background:#fff8c5}
</style></head><body>
<h1>Master catalog of Millard J Melnyk's work</h1>
<p>Last updated: %(today)s</p>
<p><b>New here? Read %(howto)s.</b></p>
<p>%(total)s items: %(srcline)s.</p>
<h2>Search all items</h2>
<p><input id="q" type="text" placeholder="Word or phrase" autofocus> <button id="go">Search</button></p>
<div id="status">Loading search…</div><div id="results"></div>
<ol>
<li><b>%(all)s</b> — every item, by date or by title.</li>
<li><b>%(az)s</b> — %(nterms)s subjects, names and terms.</li>
<li><b>%(top)s</b> — %(ntop)d topics, %(nsub)d subheadings.</li>
</ol>
<p>Spreadsheet lists: %(csv1)s · %(csv2)s</p>
<h2>About each part</h2>
<ul><li>%(howto)s</li><li>%(o1)s</li><li>%(o2)s</li><li>%(o3)s</li></ul>
<h2>Updating the catalog</h2>
<ul><li>%(u1)s — how to add new material and rebuild the catalog.</li>
<li>%(u2)s — the full topic tree with the number of items under each topic and subheading.</li>
<li>%(u3)s — the 190 coding chats waiting to be added.</li></ul>
<script>
const BASE=%(base)s; const BLOB="%(blob)s"; let DATA=null;
async function load(){
  const bin=Uint8Array.from(atob(BLOB),c=>c.charCodeAt(0));
  const txt=await new Response(new Blob([bin]).stream().pipeThrough(new DecompressionStream('gzip'))).text();
  DATA=JSON.parse(txt).map(r=>({id:r[0],date:r[1],type:r[2],title:r[3],text:r[4],low:r[4].toLowerCase()}));
  document.getElementById('status').textContent='Search ready: '+DATA.length.toLocaleString()+' items.';
}
function esc(s){return s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function search(){
  const q=document.getElementById('q').value.trim(); const out=document.getElementById('results');
  if(!DATA){return;} if(!q){out.innerHTML='';document.getElementById('status').textContent='Type a word or phrase.';return;}
  const ql=q.toLowerCase(); const hits=[];
  for(const d of DATA){const i=d.low.indexOf(ql); if(i>=0){let n=0,j=i;while(j>=0){n++;j=d.low.indexOf(ql,j+ql.length);} hits.push([d,i,n]);}}
  hits.sort((x,y)=>y[0].date.localeCompare(x[0].date));
  document.getElementById('status').textContent=hits.length.toLocaleString()+' items contain "'+q+'" (newest first).';
  out.innerHTML=hits.map(([d,i,n])=>{const s=Math.max(0,i-120),e=Math.min(d.text.length,i+ql.length+160);
    const snip=esc(d.text.slice(s,i))+'<mark>'+esc(d.text.slice(i,i+ql.length))+'</mark>'+esc(d.text.slice(i+ql.length,e));
    return '<div class="r"><a href="'+BASE+'items/'+d.id+'.md">'+esc(d.title)+'</a><div class="m">'+d.date+' · '+esc(d.type)+' · '+n+' match'+(n>1?'es':'')+'</div><div class="s">'+(s>0?'…':'')+snip+(e<d.text.length?'…':'')+'</div></div>';}).join('');
}
document.getElementById('go').onclick=search;
document.getElementById('q').addEventListener('keydown',e=>{if(e.key==='Enter')search();});
load().catch(e=>{document.getElementById('status').textContent='Search could not load: '+e;});
</script></body></html>
''' % {
    'today': today, 'howto': a('How_to_use_the_catalog.md', 'How to use the catalog'), 'total': '{:,}'.format(len(items)),
    'srcline': srcline, 'all': a('list/All_items.md', 'All items'), 'az': a('index/A-Z_index.md', 'A–Z index'),
    'nterms': '{:,}'.format(len(terms)), 'top': a('topics/Topic_outline.md', 'Topic outline'), 'ntop': len(topics), 'nsub': len(subs),
    'csv1': a('data/ai_chats.csv', 'ai_chats.csv'), 'csv2': a('data/substack.csv', 'substack.csv'),
    'o1': a('list/About_the_item_lists.md', 'About_the_item_lists.md'), 'o2': a('index/About_the_A-Z_index.md', 'About_the_A-Z_index.md'),
    'o3': a('topics/About_the_topic_outline.md', 'About_the_topic_outline.md'),
    'u1': a('tools/How_to_update_the_catalog.md', 'How_to_update_the_catalog.md'),
    'u2': a('tools/Topic_tree_with_counts.md', 'Topic_tree_with_counts.md'),
    'u3': a('data/set_aside_coding_chats.csv', 'set_aside_coding_chats.csv'),
    'base': json.dumps(BASE), 'blob': blob}
open(OUT, 'w', encoding='utf-8').write(page)
print('items', len(items), 'html bytes', len(page))
