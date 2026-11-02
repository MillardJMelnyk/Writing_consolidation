# Extracting comments and annotations from PDFs

| | |
|---|---|
| Date | 2026-09-04 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-6b66bfd3` |
| Links | [Original](https://claude.ai/chat/6b66bfd3-df89-4ea2-8dc3-f03f6bf911f9) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-09-04_extracting-comments-and-annotations-from-pdfs_6b66bfd3.html) |

**Summary:** Explains how to list PDF annotations and why Google Drive downloads do not include comments made in Drive.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps; Practical & personal > Text extraction and data cleanup

**Index terms:** PDF annotation; Adobe Acrobat; Google Drive; PyMuPDF; comment export

[← Catalog home](../README.md)

---

### Millard · 2026-09-04 17:57

how do you get a list of comments, highlights, annotations, etc., made to a PDF?

### Claude · 2026-09-04 17:58

Ambiguous — reader or code?

* Reader: Acrobat's Comments pane lists all of them; Export Comments writes them to a file.
* Code: PyMuPDF, iterate `page.annots()` per page and pull type, rect, contents, author, date.

### Millard · 2026-09-04 18:19

Not ambiguous for a normal person. I have a PDF. I made annotations, highlights, and notes. There is a way to list them.

### Claude · 2026-09-04 18:19

Open the Comments pane in your PDF reader — Acrobat: View > Comments > Comments List, or the speech-bubble icon in the right sidebar. It lists every highlight, note, and annotation with page number and text. Export Comments saves that list to a file.

### Millard · 2026-09-04 18:40

I opened the file up to comments, comments show up when looking at the online copy, but I want a local copy including the comments. Downloading doesn'

### Claude · 2026-09-04 18:40

Which online viewer — Google Drive, Acrobat web, Dropbox, something else?

### Millard · 2026-09-04 18:40

downloading doesn't carry the comments with it.

### Claude · 2026-09-04 18:40

Because those comments aren't in the PDF — they're stored in the viewer's database, not the file. Downloading gives you the original PDF only.

Which viewer? Google Drive can't merge them in; Acrobat web can (Download with comments).

### Millard · 2026-09-04 18:42

I understand that, what I don't understand is why there isn't an option to include them. I see them in my web browser (Edge). I'm looking at the shared file in Google Drive

### Claude · 2026-09-04 18:42

Google never built it. Drive's PDF comments live in Drive's comment database, and the download path just hands you the stored file bytes — there's no merge step. Same for Docs-style comments on any file Drive previews.

Your options: open the Comments panel (the sidebar you're seeing), select all, copy to a text file; or ask Robert to make his comments in Acrobat/a real PDF editor so they get written into the file itself.
