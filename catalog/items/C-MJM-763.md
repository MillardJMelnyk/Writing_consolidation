# FMT vs HLS comparison

| | |
|---|---|
| Date | 2026-08-29 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-763` |
| Links | [Original](https://claude.ai/chat/7645873d-d0b0-4d8a-96c4-8962dc31d9cc) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/763-2026-08-29-fmt-vs-hls-comparison.html) |

**Summary:** Difference between FMT progressive MP4 and HLS segmented streams in a video downloader; FMT is more reliable.

**Topics:** Practical & personal > Software tools and open-source projects

**Index terms:** HTTP Live Streaming; MP4; video download; m3u8

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-08-29 20:07

what's the difference between FMT and HLS

[File attached: 1788034021865\_image.png — contents not included in export]

### Claude · 2026-08-29 20:07

FMT = direct progressive MP4 file (single file, one format ID from the site's format list).

HLS = HTTP Live Streaming source — originally segmented .ts chunks via an .m3u8 manifest, muxed into MP4 on download.

Practical differences:

* FMT is usually the more reliable/faster download; file is served as one unit.
* HLS depends on manifest/segment availability; more prone to partial failures, slower muxing, occasional AV sync issues.
* Same nominal quality (1080p) can differ in actual bitrate/encode between the two, since they're often separate encodes on the source CDN.

If both show 1080p and same duration (21:49), pick FMT first — fewer failure points.
