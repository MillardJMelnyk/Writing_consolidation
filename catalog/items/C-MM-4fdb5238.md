# Cursor changing file modified dates unexpectedly

| | |
|---|---|
| Date | 2026-05-19 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-4fdb5238` |
| Links | [Original](https://claude.ai/chat/4fdb5238-8069-4c63-8caa-136dd8537525) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-05-19_cursor-changing-file-modified-dates-unexpectedly_4fdb5238.html) |

**Summary:** Cursor IDE altering file modified dates on startup is a known bug; where to report it and Anysphere's ownership.

**Topics:** Practical & personal > Software tools and open-source projects

**Index terms:** Cursor; Anysphere; Michael Truell; file modification date; line ending

[← Catalog home](../README.md)

---

### Millard · 2026-05-19 12:26

I'm using Cursor, see image.

Why does Cursor change the modified dates on files that have not been modified by anything I've done in Cursor? It happens even by merely opening the app.

### Claude · 2026-05-19 12:27

It's a known, acknowledged bug in Cursor — not something specific to your setup. Cursor staff have confirmed it on the forum, and it's been reported continuously across versions 2.0 through the 3.x line you're on.

**What's actually happening**

When Cursor's Agent or Composer mode touches a file (even sessions ago), Cursor caches that edit as a pending change. When the IDE restarts, files that Agent or Composer previously edited get marked as modified, usually due to EOF or whitespace changes. On restart, Cursor tries to "rehydrate" these pending modifications, often messing with line endings or injecting whitespace. The three flavors people see are: a trailing newline added at EOF, CRLF↔LF line-ending flips, and stray empty lines appearing mid-file.

A separate, related bug: When quitting Cursor, a trailing newline is automatically added to files that don't have one, even with files.insertFinalNewline set to false in workspace settings. This causes git status to show these files as modified every time you reopen the editor. So the obvious workaround setting is itself broken right now.

That's why "just opening the app" is enough — Cursor is replaying ghost edits and/or re-normalizing line endings, both of which rewrite the file and bump mtime.

**Workarounds (none are perfect)**

From the Cursor team and forum consensus:

* `Ctrl+Shift+P` → **Developer: Reload Window** often clears the rehydrate cycle for the session.
* For specific stuck files: open in Source Control, click **Keep**, delete the injected blank/newline, save. Sometimes "waking up" the Keep All button requires making a small change in any file, then staging and committing.
* Pin your line endings explicitly with a `.gitattributes` (`* text=auto eol=lf` or whatever matches your repo) so at least the CRLF/LF flips stop showing as diffs.
* `git config --local apply.whitespace nowarn` and `git diff -w` to ignore whitespace-only changes while the bug persists.
* Close chats/agent sessions that touched the affected files before quitting Cursor — reduces the rehydrate surface.

Cursor staff claimed it was fixed in 2.3.x; users on 2.3.23 and later (including February 2026 reports) still see it. Worth submitting your own report with your 3.4.20 version info since the team appears to still be tracking it.

### Millard · 2026-05-19 12:28

where do I report it?

### Claude · 2026-05-19 12:28

The forum's Bug Reports category — that's where Cursor staff (like the deanrie who replied in the thread I cited) actively respond:

**https://forum.cursor.com/c/support/bug-report/6**

Click "+ New Topic". There's a structured template (Where does the bug appear / Describe the Bug / Steps to Reproduce / Expected Behavior / OS / Cursor Version / Does this stop you from using Cursor). The version block from your About dialog (the "Copy" button in the screenshot you sent) is exactly what goes in the version field.

Before posting, search the existing threads for "modifying files on startup" and "phantom unsaved changes" — if one is still open on 3.x, replying there with your version info carries more weight than a fresh duplicate. If they're all closed, open a new one and link the prior threads as related.

Anthropic doesn't run Cursor and has no channel for Cursor bugs, in case that wasn't obvious.

### Millard · 2026-05-19 12:29

who owns Cursor?

### Claude · 2026-05-19 12:29

Cursor is owned by **Anysphere, Inc.**, a private San Francisco company. It was incorporated in 2022 by Michael Truell, Sualeh Asif, Arvid Lunnemark, and Aman Sanger while they were students at MIT. Michael Truell is CEO.

It's venture-backed, not public. A $2.3 billion Series D closed in November 2025, co-led by Accel and Coatue, valuing the company at $29.3 billion, with participation from Google and Nvidia. The four co-founders each reportedly hold around 4.5% — roughly 18% combined — so the majority of the company is held by VCs (Thrive Capital, Andreessen Horowitz, Accel, Coatue, DST Global) plus strategic investors OpenAI, Google, and Nvidia.

Arvid Lunnemark left in October 2025 to start a safety-focused AI lab, Integrous Research, but reportedly kept his stake. There are unconfirmed reports of a further funding round at $50B+ in early 2026, but nothing closed publicly that I can find.
