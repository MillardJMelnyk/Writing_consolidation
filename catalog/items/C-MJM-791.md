# Document comparison revision settings

| | |
|---|---|
| Date | 2026-09-28 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-791` |
| Links | [Original](https://claude.ai/chat/7aeeaa26-2936-4578-826e-cc8719c2dbbe) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/791-2026-09-28-document-comparison-revision-settings.html) |

**Summary:** Exact Word 365 steps for changing compare-documents revision appearance after Copilot and Sonnet failed to give a real answer.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps; AI chatbots and working with Claude > Comparing AI models and chatbots

**Index terms:** Microsoft Word 365; document comparison; Track Changes Options; Microsoft Copilot; Claude Sonnet

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-09-28 15:37

Unbelievable neither co-pilot nor Sonnet can give me an actual answer. All they do is guess and bullshit
How do I change the settings for how revisions appear when I compare two documents.
DO NOT FUCKING GUESS. FIND THE EXACT INSTRUCTIONS FOR THE VERSION SHOWN

[File attached: 1790609823336\_image.png — contents not included in export]

### Claude · 2026-09-28 15:37

Monday, September 28, 2026

I found no Microsoft documentation specific to build 16.0.20430.20032. The steps below are from Microsoft's Word for Microsoft 365 documentation and other sources, and I have not run them on your build. Your question could mean either of two settings, so both are listed.

**A. Appearance of the revisions (colors, underline, strikethrough)**

1. Review tab → click the dialog launcher at the bottom-right corner of the **Tracking** group. Then, in the Track Changes Options dialog, click Advanced Options.
2. Set the format and color for Insertions, Deletions, Moved text, table cells and Formatting. Insertions default to Underline with the color By author, and Deletions default to Strikethrough with the color By author.
3. Select All Markup in the Display for Review dropdown, or the changes you set in that dialog won't all show.

These color settings apply to your computer only.

**B. How the comparison itself is generated**

1. Review tab → Compare → Compare…
2. Click **More >>** in the dialog.
3. Under Show changes at, select Character level or Word level. Word level replaces whole words on any edit, while Character level pinpoints individual letters or digits.
4. Under Show changes in, select Original document, Revised document or New document. New document leaves both source files untouched, while the other two apply the markup directly into that file.
5. Under Comparison settings, tick or untick items such as formatting, case changes, and white space. These match the VBA `CompareDocuments` parameters, which default to True for formatting and case changes.

Sources: Microsoft Support "Change the track changes color" and "Track Changes Options"; Microsoft Learn `Application.CompareDocuments`. The Compare dialog steps in B come from a third-party guide (Online Computer Tips, July 25, 2026), not from a Microsoft page.
