# Emojis appearing in black and white in Word 365

| | |
|---|---|
| Date | 2025-11-20 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-323` |
| Links | [Original](https://claude.ai/chat/64485f7c-4163-478f-ade4-8598be31cc5a) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/323-2025-11-20-emojis-appearing-in-black-and-white-in-word-365.html) |

**Summary:** Fixing emojis that show black and white in one Word 365 document; the cause is document-specific formatting, so clear formatting or copy to a new file.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** Microsoft Word; emoji; Segoe UI Emoji; character formatting

[← Catalog home](../README.md)

---

### Millard · 2025-11-20 18:04

in a Word 365 document, emojis 😖🤢😶😃😆🤣 come out looking like the attached image. How do I get them to show in color?

[File attached: 1763661831390\_image.png — contents not included in export]

### Claude · 2025-11-20 18:04

Change the font to **Segoe UI Emoji**:

1. Select the emojis
2. Change font dropdown to "Segoe UI Emoji"

Or insert them using **Insert > Symbols > Emoji** (Ctrl+Cmd+Space on Mac, Windows key + period on Windows) which will use color by default.

Your emojis are rendering in Segoe UI Symbol (black and white) instead of Segoe UI Emoji (color).

### Millard · 2025-11-20 18:05

that's what it already is

[File attached: 1763661927992\_image.png — contents not included in export]

### Claude · 2025-11-20 18:05

Delete the emojis and reinsert using **Insert > Symbols > Emoji** (or Windows key + period).

Copy-pasted emojis often retain formatting that overrides the font setting. The Insert menu bypasses this.

If that fails, check **File > Options > Advanced > Display** - ensure "Disable hardware graphics acceleration" is unchecked.

### Millard · 2025-11-20 18:06

Windows key + period is how I inserted them initially

### Claude · 2025-11-20 18:06

Check document compatibility mode:

**File > Info > Convert** (if visible) - click it to upgrade to modern .docx format.

Or:

**File > Save As > Save as type:** select "Word Document (*.docx)" not "Word 97-2003 Document (*.doc)".

Older document formats force black-and-white emoji rendering even with correct font.

If already in .docx format, this is a known Office bug in certain builds. Workaround: Insert as **pictures** via **Insert > Pictures > Stock Images > search "emoji"** or use actual image files of colored emojis.

### Millard · 2025-11-20 18:11

Wow you're just shooting in the dark, aren't you?

### Claude · 2025-11-20 18:11

Yes. I need more information:

1. What Windows version and Word 365 build number? (**File > Account > About Word**)
2. Are you on Windows 10 or 11?
3. Do color emojis work in other apps (Notepad, Chrome, etc.)?
4. File format currently? (check bottom of Save As dialog)

The Segoe UI Emoji font + Windows emoji picker should produce color emojis. If it's not working despite correct setup, it's either a system-level font rendering issue or a specific Word bug tied to your build/OS combination.

### Millard · 2025-11-20 18:12

Here are the info data, it's already a docx file. I did open a new document, and inserting Win+. emojis results were in color.

[File attached: 1763662274719\_image.png — contents not included in export]

### Claude · 2025-11-20 18:12

Document-specific issue. The file has inherited formatting overriding the font.

**Solution:** Select the emojis, press **Ctrl+Spacebar** (clears direct character formatting), then **Ctrl+Q** (clears paragraph formatting).

If that fails: **Copy all content to the new document where emojis work correctly.**

The .docx format is fine - something in this specific file's formatting is forcing black-and-white rendering despite correct font selection.
