import json, sys, time, urllib.request, urllib.parse, os
out = sys.argv[1]
base = "https://substack.com/api/v1/reader/feed/profile/109147589"
cursor, page, total = None, 0, 0
while True:
    url = base + ("?cursor=" + urllib.parse.quote(cursor) if cursor else "")
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            data = json.load(urllib.request.urlopen(req, timeout=60)); break
        except Exception as e:
            print("retry", page, e, flush=True); time.sleep(5 * (attempt + 1))
    else:
        sys.exit("failed at page %d" % page)
    json.dump(data, open(os.path.join(out, "page_%04d.json" % page), "w"))
    n = len(data.get("items") or []); total += n
    if page % 20 == 0: print(page, total, flush=True)
    cursor = data.get("nextCursor"); page += 1
    if not cursor or n == 0: break
    time.sleep(0.7)
print("done pages", page, "items", total)
