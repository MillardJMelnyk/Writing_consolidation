# Start11 taskbar shortcuts storage location

| | |
|---|---|
| Date | 2026-01-18 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-599` |
| Links | [Original](https://claude.ai/chat/5f739ec8-a68e-484a-a1a9-37595218770f) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/599-2026-01-18-start11-taskbar-shortcuts-storage-location.html) |

**Summary:** Start11 taskbar pins are stored in the native Windows User Pinned TaskBar folder under AppData.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** Start11; Stardock; Windows 11 taskbar; pinned shortcut; AppData

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-01-18 14:23

where are the shortcuts pinned to the Start11 taskbar stored on a win 11 system?

### Claude · 2026-01-18 14:24

Sunday, January 18, 2026, 12:38 PM CST

Based on the search results:

**Start11 taskbar pins use the native Windows location:**

```
%AppData%\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar
```

Full path:

```
C:\Users\<username>\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar
```

Start11 doesn't maintain a separate storage location for standard taskbar pins—it hooks into the Windows taskbar system. Stardock's deployment documentation explicitly states that "pinned items on the taskbar are currently not supported for deployments", confirming they rely on the native Windows mechanism rather than their own storage.

**Note:** If you're using Start11 v2's "pinned folder menus" feature (the fly-out folder functionality specific to Start11), those are configured through Start11's settings and would be part of the Start11 backup/settings file, not stored as individual shortcuts in the above folder.
