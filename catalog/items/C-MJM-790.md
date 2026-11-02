# Customizing revision display in Word 365 document comparison

| | |
|---|---|
| Date | 2026-09-28 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-790` |
| Links | [Original](https://claude.ai/chat/12c8e0d6-4745-406c-9d38-c23ffc0ccd49) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/790-2026-09-28-customizing-revision-display-in-word-365-document-comparison.html) |

**Summary:** Repeated wrong instructions for Word 365 revision display settings until Claude correctly points to the Tracking group dialog launcher.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps; AI chatbots and working with Claude > AI honesty, bias and guardrails

**Index terms:** Microsoft Word 365; document comparison; Tracking group; Track Changes Options; markup

[← Catalog home](../README.md)

---

### Millard · 2026-09-28 15:31

How do I change the settings in Word 365 for how revisions appear when I compare two documents

### Claude · 2026-09-28 15:31

Monday, September 28, 2026

**Compare dialog (what is compared and where results go):**

1. Review > Compare > Compare...
2. Select the two documents, then click **More >>**.
3. Set the comparison options: Insertions and deletions, Moves, Comments, Formatting, Case changes, White space.
4. Set **Show changes at**: Character level or Word level.
5. Set **Show changes in**: Original document, Revised document, or New document.

**Markup appearance (colors, insertion/deletion formatting, balloons):**

1. Review > Track Changes group > click the dialog launcher (small arrow at lower right) > **Advanced Options...**
2. Set Insertions, Deletions, Changed lines, Moves, Formatting, and Balloons/margin display.

**Display mode:** Review > Display for Review dropdown: Simple Markup, All Markup, No Markup, or Original.

**Which changes are shown:** Review > Show Markup dropdown, to toggle Insertions and Deletions, Formatting, Comments, and reviewer filters.

### Millard · 2026-09-28 15:31

bullshit

[File attached: 1790609512565\_image.png — contents not included in export]

### Claude · 2026-09-28 15:31

My list was incomplete. It omitted five settings shown in your screenshot: Tables, Headers and footers, Footnotes and endnotes, Textboxes, and Fields. It also didn't say that Insertions and deletions is locked on and can't be unchecked.

This dialog controls only what is compared and where the result goes. It has no setting for how revisions look (colors, underline/strikethrough, balloons). That is under Review > Track Changes dialog launcher > Advanced Options..., as stated earlier.

If the appearance is what's wrong, tell me what you see vs. what you want.

### Millard · 2026-09-28 15:33

DO NOT FUCKING GUESS. RESEARCH AND GIVE ME THE CORRECT INSTRUCTIONS!!!

[File attached: 1790609609672\_image.png — contents not included in export]

### Claude · 2026-09-28 15:33

Sources: Microsoft Support and Microsoft Q&A, retrieved Sep 28, 2026. I did not test these steps in build 16.0.20430.20032.

**The Compare dialog has no appearance settings.** Under Show changes in, you choose whether the results go in the Original document, the Revised document, or a new document. Choosing Original or Revised modifies that document. The result is displayed as ordinary Track Changes markup, so the appearance is controlled by the Track Changes settings below.

**Colors and formatting of insertions, deletions, moves, and changed lines:**

1. Review > Tracking Dialog Launcher (small arrow, lower right of the group) > Advanced Options. Microsoft's page calls this the Markup group, while other sources call it the Tracking group. Look for the launcher arrow at the group's lower right.
2. Set the Color dropdowns to By author or a fixed color. Insertions default to Underline and Deletions to Strikethrough, and you can change both formats.
3. These settings apply to your computer only. Other people see the changes in their own settings.

**Balloons versus inline:**

1. Review > Show Markup > Balloons, then choose the display type.
2. Inline shows deletions as strikethroughs instead of in balloons. Balloons require Print Layout or Web Layout view.

**If markup doesn't appear at all:**

1. Set Display for Review to All Markup.
2. In Show Markup, make sure Insertions and Deletions is checked.
3. In Balloons, choose Show All Revisions Inline or Show Only Comments and Formatting in Balloons.

**Behavior that often looks like a bug:** If either document contains tracked changes, Word offers to accept them before comparing. The result then shows only changes from the revised document as tracked changes.

Tell me which appearance problem you are seeing and I'll narrow this down.

### Millard · 2026-09-28 15:34

BULLSHIT AGAIN

[File attached: 1790609685760\_image.png — contents not included in export]

### Claude · 2026-09-28 15:35

This dropdown (For Everyone / Just Mine / Lock Tracking) has no Advanced Options entry. My earlier steps pointed you to the wrong group. I wrote "Track Changes group" in my first answer, and my second answer named the wrong group too.

In your screenshot, Track Changes, Accept, Reject, Previous, and Next sit in the Changes group. The Tracking group, which holds Show Markup and the Reviewing Pane, is to its left. The small arrow at the lower-left edge of your screenshot is that group's dialog launcher.

1. Close this dropdown.
2. Click that launcher arrow at the lower right of the Tracking group. This opens Track Changes Options.
3. Click **Advanced Options...** in that dialog.
4. Set the Color and format for Insertions, Deletions, Changed lines, and Moves.

I verified the dialog launcher path from the Microsoft Support and Q&A sources in my last reply. I have not verified the group's exact position in build 16.0.20430.20032. Your screenshot is the only evidence for it.

If that arrow isn't there, send a screenshot of the full Review tab.
