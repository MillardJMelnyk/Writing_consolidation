# Firefox microphone access on Google Translate

| | |
|---|---|
| Date | 2026-10-25 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-815` |
| Links | [Original](https://claude.ai/chat/7a374cff-4d30-4d62-b45c-d0f3cffe9a1d) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/815-2026-10-25-firefox-microphone-access-on-google-translate.html) |

**Summary:** Firefox cannot use the microphone on Google Translate because it lacks the browser speech-to-text the site relies on.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** Firefox; Google Translate; speech-to-text; Web Speech API; microphone

[← Catalog home](../README.md)

---

### Millard · 2026-10-25 16:29

[image attached — not included in export]

How can I set Firefox to allow me to use my microphone on Google Translate

[File attached: 1792945769268\_image.png — contents not included in export]

### Claude · 2026-10-25 16:29

Sunday, October 25, 2026, time unavailable, timezone unavailable

You can't; no setting in release Firefox fixes this (Highly likely, as of Oct 25, 2026).

That tooltip doesn't mean the microphone is blocked. Google Translate's mic button depends on browser-side speech-to-text, which Firefox doesn't provide. Mozilla's own wiki says Chrome, Edge, Safari and Opera support this speech-to-text, so sites that rely on it work in those browsers but not in Firefox. Mozilla only ever tested support in Nightly builds, held there while it worked on the spec with Google and others. Their testing instructions pointed to a test-only server from 2019, so it isn't a usable route.

Use Chrome or Edge for Translate's mic.

Missing evidence: Mozilla release notes from 2025–2026 confirming this hasn't shipped since. The tooltip on your screen points the same way.

Sources:

* [Web Speech API - Speech Recognition (MozillaWiki)](https://wiki.mozilla.org/Web_Speech_API_-_Speech_Recognition)
* [MozillaWiki revision diff](https://m.wiki.mozilla.org/Special:MobileDiff/1218961)
* [MozillaWiki revision diff](https://m.wiki.mozilla.org/Special:MobileDiff/1218965)
