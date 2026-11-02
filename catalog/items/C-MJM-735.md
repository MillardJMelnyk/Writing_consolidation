# Installing dupeguru on Windows

| | |
|---|---|
| Date | 2026-08-10 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-735` |
| Links | [Original](https://claude.ai/chat/2b2fbb59-383e-45f4-8be1-938765c3c631) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/735-2026-08-10-installing-dupeguru-on-windows.html) |

**Summary:** dupeGuru Windows zip is a portable build; extract it, optionally to Program Files with admin rights.

**Topics:** Practical & personal > Software tools and open-source projects

**Index terms:** dupeGuru; portable application; Program Files; Hardcoded Software

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-08-10 19:11

I downloaded dupeguru-win64\_4.3.1.zip from https://dupeguru.net/#download but can't remember how to install it

### Claude · 2026-08-10 19:11

Monday, August 10, 2026 — time not verifiable in real time, CST assumed (Querétaro, MX).

Confirmed: the win64 zip is a portable build, not an installer.

1. Right-click `dupeguru-win64_4.3.1.zip` → **Extract All** (or use 7-Zip) → pick a destination folder (no restrictions).
2. Open the extracted folder, run `dupeguru.exe` directly.

No installer, no registry writes, no admin rights required. If SmartScreen blocks it (unsigned binary): **More info** → **Run anyway**.

### Millard · 2026-08-10 19:13

how did I end up with C:\Program Files\Hardcoded Software\dupeGuru\dupeguru-win64.exe? That's where it ended up when I installed it on my other machine. I didn't invent "Hardcoded Software".

### Claude · 2026-08-10 19:13

`Hardcoded Software` was the original commercial publisher of dupeGuru — Virgil Dupras's company, before the project went open-source and moved to the current GitHub maintainer (arsenetar). Older dupeGuru installers wrote to `C:\Program Files\Hardcoded Software\dupeGuru\` by default; that path string is baked into the legacy installer/uninstaller metadata and has persisted in some installer builds even after the maintainer changed, since nobody updated the install path.

So: on the other machine you ran the `.exe` installer (not the portable zip), and it used that legacy default path. Not something you invented.

### Millard · 2026-08-10 19:14

OK, so I can just extract all to a new folder in C:\Program Files\ ?

### Claude · 2026-08-10 19:14

Yes, but note: writing to `C:\Program Files\` requires admin rights (UAC prompt), even for a plain extract — that directory isn't user-writable by default. Right-click the zip → Extract All → target `C:\Program Files\dupeGuru\` (or similar) → accept the elevation prompt if shown.

Functionally no different from extracting elsewhere; `Program Files` just mirrors where the old installer put it.
