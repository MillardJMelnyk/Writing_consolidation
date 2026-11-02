# Firefox history search toolbar button

| | |
|---|---|
| Date | 2026-09-12 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-772` |
| Links | [Original](https://claude.ai/chat/b85d59d0-6b78-4895-99bd-508827110e46) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/772-2026-09-12-firefox-history-search-toolbar-button.html) |

**Summary:** Seeking a Firefox toolbar button that opens the history sidebar like Ctrl+H; none exists natively, so a minimal extension is proposed.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** Mozilla Firefox; history sidebar; toolbar button; WebExtension

[← Catalog home](../README.md)

---

### Millard · 2026-09-12 17:31

I want a toolbar button for Firefox that searches history

### Claude · 2026-09-12 17:31

Saturday, September 12, 2026 — time/timezone not available to me.

Clarification needed before proposing an approach:

1. **Trigger behavior**: does clicking the button open a popup with a search box, or does it just jump straight to `about:firefox` history page filtered somehow?
2. **Search scope**: full history, or only current session/recently closed tabs?
3. **Match target**: URL, page title, or both?
4. **Output**: dropdown list of matching results to click, or does it just open Firefox's native Library window pre-filtered?
5. **Manifest version**: MV2 or MV3 (affects `browser_action` vs `action` API and packaging)?

No code until this is settled per your directive.

### Millard · 2026-09-12 17:32

clicking the history button does this

[File attached: 1789234333469\_image.png — contents not included in export]

[File attached: 1789234366311\_image.png — contents not included in export]

### Claude · 2026-09-12 17:32

That's the native Firefox History toolbar button — already built in, no extension needed. Clicking "Search history" in that menu opens the Library window's search pane.

If the goal is to skip the intermediate menu and jump straight to search-history on a single click, that requires either:

1. Rebinding this button (not natively supported — Firefox doesn't expose a "search history direct" toolbar action), or
2. A separate WebExtension button using `browser.history.search()` API with a popup search box.

Which do you want — (a) a way to make the existing button skip straight to search, or (b) a new custom extension button with its own popup?

### Millard · 2026-09-12 17:34

I don't like the button at all. I'd like a button that does exactly what CTRL-H does.

### Claude · 2026-09-12 17:34

Firefox has a native toolbar button for exactly that — no extension needed.

1. Right-click the toolbar → **Customize Toolbar…**
2. In the palette, find **"History Sidebar"** (clock icon with a sidebar).
3. Drag it onto your toolbar.
4. Click **Done**.

That button toggles the History sidebar — identical behavior to Ctrl+H.

If it's not present in your build's palette (some ESR/rebrand variants strip it), the fallback is a minimal WebExtension using `commands` API bound to `Ctrl+H` triggering `sidebarAction`. But confirm the native option is missing first before going that route.

### Millard · 2026-09-12 17:35

where

[File attached: 1789234547689\_image.png — contents not included in export]

### Claude · 2026-09-12 17:35

Confirmed absent from this build's palette (Firefox 155.0.1). The "Library" item present here opens the Library *window* (Ctrl+Shift+H), not the sidebar — different behavior than Ctrl+H.

Native option doesn't exist here. Fallback: minimal WebExtension.

**Proposed approach:**

* `manifest.json` (MV3) with `sidebar_action` pointing to a page that mirrors Firefox's built-in history sidebar via `browser.history` API, plus a `browser_action` (toolbar button) that calls `browser.sidebarAction.toggle()`.
* Caveat: WebExtensions **cannot toggle Firefox's native built-in History sidebar** — that's internal browser UI, not exposed to the extension API. The extension can only toggle its *own* sidebar panel, which would need to be built from scratch (a page listing `browser.history.search()` results).
* So the realistic result is: a custom sidebar that looks/behaves like history, not literally invoking the native Ctrl+H panel.

Alternative: bind a **custom keyboard shortcut** to something under `about:config` — not possible either; Ctrl+H is hardcoded to the native sidebar, and no config flag re-exposes its toolbar button in newer Firefox.

Given that, do you want:

1. The WebExtension building a custom history-sidebar clone, or
2. Drop this and use **Library window (Ctrl+Shift+H)** via the existing "Library" toolbar button instead, since that's already available natively and shows full searchable history?
