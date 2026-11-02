# Everything subfolders button not working

| | |
|---|---|
| Date | 2026-08-13 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-a7f6fb66` |
| Links | [Original](https://claude.ai/chat/a7f6fb66-14d5-4788-8ff0-9a230234c715) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-08-13_everything-subfolders-button-not-working_a7f6fb66.html) |

**Summary:** The Everything search tool's main-window Subfolders checkbox not overriding Advanced Search, and filtering extensionless files in FreeFileSync.

**Topics:** Practical & personal > Software tools and open-source projects

**Index terms:** Everything (search tool); subfolder search; FreeFileSync; file filter; file extension

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-08-13 14:59

the subfolders button in the Everything window doesn't work. It has no effect on or off. The Search/Advanced Search controls whether subfolders are included. The main window "Subfolders" checkbox does not override it.

### Claude · 2026-08-13 14:59

Correct — Advanced Search's "Include subfolders" is a separate, per-search setting; the main window checkbox doesn't sync with or override it.

### Millard · 2026-08-13 15:01

NO NOT "CORRECT".

You're saying that the main window checkbox "correctly" does NOTHING.

### Claude · 2026-08-13 15:01

No proof found either way from search. Retracting "correct" — I don't have evidence that a checkbox doing nothing is intended behavior.

### Millard · 2026-08-13 15:02

Take as a fact that it's not intended behavior (it's stupid to think so).

Find the fix.

### Claude · 2026-08-13 15:02

The checkbox only has an effect when a folder is actually **selected** in the Folders sidebar tree (left panel). If no folder is selected there — which is the case in your screenshot — the checkbox has nothing to act on, so toggling it does nothing.

Fix: click a folder in the Folders tree (e.g. click on D:) to select it, then the Subfolders checkbox will control whether that selection's subfolders are searched.

### Millard · 2026-08-13 15:05

FreeFileSync question: how do I filter (include or exclude) files with NO extension?

### Claude · 2026-08-13 15:05

Not directly possible — FreeFileSync's filter syntax only supports `*` and `?` wildcards, with no "does not contain a dot" pattern. Workaround: Include filter `*.*` matches only files with extension (i.e., excludes no-extension files), but it also pulls in folders that have a dot in their name.
