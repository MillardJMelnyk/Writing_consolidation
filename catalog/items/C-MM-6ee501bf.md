# Disabling Daemon Tools startup

| | |
|---|---|
| Date | 2026-10-21 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-6ee501bf` |
| Links | [Original](https://claude.ai/chat/6ee501bf-b413-450f-b5d1-794e73a01563) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-10-21_disabling-daemon-tools-startup_6ee501bf.html) |

**Summary:** How to stop DAEMON Tools from launching at Windows startup via Task Manager or its Autorun preference.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** DAEMON Tools; Task Manager; startup apps; autorun

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-10-21 05:20

how to stop daemon tools from starting on startup?

### Claude · 2026-10-21 05:20

Tuesday, October 20, 2026, time unavailable, CST: Press Ctrl+Shift+Esc to open Task Manager, go to **Startup apps**, select the DAEMON Tools entry, and click **Disable**.

### Millard · 2026-10-21 05:20

in daemon tools

### Claude · 2026-10-21 05:20

Open **Preferences** → **General** tab, uncheck **Autorun** (it launches the tray agent at system startup) and also **Automount**, since Automount starts the tray agent after startup to create the virtual drives. Click **Apply** to save.
