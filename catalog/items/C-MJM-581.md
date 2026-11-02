# Pinning a Word file to taskbar via command line

| | |
|---|---|
| Date | 2026-01-12 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-581` |
| Links | [Original](https://claude.ai/chat/a9049c23-63c8-44cf-8f32-d0a9745027ae) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/581-2026-01-12-pinning-a-word-file-to-taskbar-via-command-line.html) |

**Summary:** Building a Windows taskbar shortcut to open a long-named Word document using start command and the Start in field.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** Windows shortcut; taskbar pinning; Microsoft Word; start command; case-based reasoning

[← Catalog home](../README.md)

---

### Millard · 2026-01-12 17:39

give me the command line for a shortcut that I can pin to my taskbar to open the following Word file:
"C:\Users\Millard\AppData\Roaming\MetaQuotes\Terminal\73B7A2420D6397DFF9014A20F1201F97\MQL5\Indicators\My MT5 Indicators\Case-Based Reasoning (CBR) System for MT5 time-series data - Gemini 3 Flash convo, requirements, architecture, AI prompts 2026-01-12.docx"

### Claude · 2026-01-12 17:39

```
start "" "C:\Users\Millard\AppData\Roaming\MetaQuotes\Terminal\73B7A2420D6397DFF9014A20F1201F97\MQL5\Indicators\My MT5 Indicators\Case-Based Reasoning (CBR) System for MT5 time-series data - Gemini 3 Flash convo, requirements, architecture, AI prompts 2026-01-12.docx"
```

To pin to taskbar:

1. Create a new shortcut (.lnk file)
2. Paste the command above as the target
3. Right-click the shortcut → Pin to taskbar

Alternatively, paste just the full file path in quotes in the shortcut target if Word should open it automatically.

### Millard · 2026-01-12 17:40

what does the <<start "">> do?

### Claude · 2026-01-12 17:40

`start` launches a new process. The `""` (empty quotes) sets the window title to nothing—it's a required placeholder when you're passing a file path directly after it. Without the `""`, Windows would interpret the first quoted string as the window title rather than the file to open.

### Millard · 2026-01-12 17:45

the file name is too long for the shortcut. I'll need a shortcut with "Start """ followed by the filename and put the path in the "Start in:" box.

### Claude · 2026-01-12 17:45

**Target:**

```
start "" "Case-Based Reasoning (CBR) System for MT5 time-series data - Gemini 3 Flash convo, requirements, architecture, AI prompts 2026-01-12.docx"
```

**Start in:**

```
C:\Users\Millard\AppData\Roaming\MetaQuotes\Terminal\73B7A2420D6397DFF9014A20F1201F97\MQL5\Indicators\My MT5 Indicators\
```

### Millard · 2026-01-12 18:02

I can't save the shortcut.

[File attached: 1768240923180\_image.png — contents not included in export]
