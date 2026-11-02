# Display rulers in Word 365

| | |
|---|---|
| Date | 2025-12-30 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-551` |
| Links | [Original](https://claude.ai/chat/aeb2ea56-830a-43e1-a255-cd9063e22a4f) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/551-2025-12-30-display-rulers-in-word-365.html) |

**Summary:** Explains how to keep both horizontal and vertical rulers permanently visible in Word 365 via Options and Normal.dotm.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** Microsoft Word 365; ruler; Normal.dotm; Print Layout

[← Catalog home](../Master_catalog.md)

---

### Millard · 2025-12-30 18:50

how do I set Word 365 to always show both horizontal and vertical rulers?

### Claude · 2025-12-30 18:50

In Word 365:

1. **View tab** → check **Ruler** in the Show group (enables horizontal ruler)
2. For the **vertical ruler**: **File** → **Options** → **Advanced** → scroll to **Display** section → check **Show vertical ruler in Print Layout view**

The vertical ruler only appears in Print Layout view. The horizontal ruler setting persists per session but may need to be re-enabled. The vertical ruler setting in Options is persistent across sessions.

### Millard · 2025-12-30 18:51

I want both rulers permanently visible without resetting each session.

### Claude · 2025-12-30 18:51

The vertical ruler setting (in Options → Advanced) is already persistent.

For the horizontal ruler to persist, modify the Normal.dotm template:

1. Press **Win+R**, type `%appdata%\Microsoft\Templates`, press Enter
2. Open **Normal.dotm**
3. Go to **View** tab → check **Ruler**
4. Save and close Normal.dotm

This embeds the ruler setting in your default template, making it persist across all new documents and sessions.
