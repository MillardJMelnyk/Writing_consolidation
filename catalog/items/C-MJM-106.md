# Substack Draft Heading Links

| | |
|---|---|
| Date | 2025-07-26 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-106` |
| Links | [Original](https://claude.ai/chat/9b6c0849-f6e3-4446-9faa-6c3b601f6eb3) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/106-2025-07-26-substack-draft-heading-links.html) |

**Summary:** How to link to a heading inside a Substack draft; Millard's solution is copying the anchor link from the preview.

**Topics:** Writing, Substack and publishing > Substack posts and article drafts

**Index terms:** Substack; anchor link; heading; draft preview; email newsletter

[← Catalog home](../README.md)

---

### Millard · 2025-07-26 15:55

how do I insert a link to a heading in a Substack post while it's still in draft?

### Claude · 2025-07-26 15:55

In Substack's draft editor, you can create links to headings within your post using anchor links. Here's how:

**Method 1: Using Substack's built-in anchor functionality**

1. Create your heading in the draft (use the heading format from the toolbar)
2. Substack automatically generates an anchor ID for each heading
3. To link to it, highlight the text you want to turn into a link
4. Click the link button in the toolbar
5. In the URL field, type `#` followed by the heading text in lowercase with hyphens replacing spaces
   * For example, if your heading is "My Important Section", use `#my-important-section`

**Method 2: Manual anchor creation**

1. Switch to HTML view (if available in your editor)
2. Add an anchor tag before your heading: `<a name="section-name"></a>`
3. Then link to it using `#section-name`

**Method 3: Using the heading's auto-generated ID**

1. After publishing or previewing, you can inspect the heading element to see its actual ID
2. Right-click on the heading and "Inspect element" to find the exact ID
3. Use that ID with the `#` symbol

The link will work both in the draft preview and once published. When readers click the link, it will automatically scroll them to that heading in the post.

Note that anchor links only work within the same post - you can't link to headings in other Substack posts this way.

### Millard · 2025-07-26 15:58

it tells me it's an invalid link

[File attached: image.png — contents not included in export]

### Claude · 2025-07-26 15:59

I can see the issue! You're trying to create a link to the heading "lkzajdf" at the bottom of your post, but the format `#lkzajdf` isn't working.

Here are a few things to try:

**1. Check the actual heading format**
Make sure "lkzajdf" is formatted as an actual heading (H1, H2, H3, etc.) using Substack's heading tools, not just bold text.

**2. Try different anchor formats**
Substack might be generating the anchor differently. Try these variations:

* `#lkzajdf` (what you have)
* `#Lkzajdf` (capitalized first letter)
* Just `lkzajdf` (without the #)

**3. Use Substack's automatic anchor generation**
Some versions of Substack create anchors automatically. Try:

* Publish or preview the post first
* Then right-click on the heading and "Inspect element" to see the actual ID that was generated
* Use that exact ID with the # symbol

**4. Alternative method**
You could also try:

* Selecting the heading text itself
* Copying it
* Then when creating the link, paste it and Substack might automatically create the proper anchor link

The "invalid link" error suggests Substack isn't recognizing `#lkzajdf` as a valid internal anchor. The heading might not be properly formatted as a heading element, or Substack might be using a different ID format than expected.

### Millard · 2025-07-26 16:00

It's formatted as H1. None of your suggestions work.

### Claude · 2025-07-26 16:00

Based on the official Substack documentation, I see the issue now. Substack's anchor links only work after publishing the post - you need to publish your post first, then hover over the H1 header and click on the link icon that appears to get the anchor link automatically copied to your clipboard.

The problem is that **Substack doesn't generate anchor links for headings while the post is still in draft mode**. The anchor functionality only becomes available after publication.

Here's what you need to do:

1. **Publish your post first** (you can always edit it later)
2. **After publishing**, go back to your post and hover over the H1 heading "lkzajdf"
3. **Click the link icon** that appears when you hover - this will automatically copy the proper anchor link to your clipboard
4. **Go back to edit mode** and paste that anchor link where you want to reference the heading

Alternatively, if you don't want to publish yet, you could try using the preview function to see if the anchor links work there, but the official process requires publication first.

This explains why the manual `#lkzajdf` format isn't working - Substack generates its own anchor IDs that may be different from just the heading text.

### Millard · 2025-07-26 16:01

I've done that before. It's nonsense. It means that the email sent to subscribers won't contain the links I want them to have.

### Claude · 2025-07-26 16:02

You're absolutely right - that's a terrible workflow! If you can't create internal links until after publishing, then email subscribers get a version without the navigation links you intended, which defeats the purpose.

Let me search for more current information about Substack's internal linking capabilities:

I found one potential workaround! One Substack writer mentions using the "secret draft link" - you can copy/paste your draft link in a new window, then hover your mouse to the left of the header to make the icon appear.

Let me search for more details about this draft preview method:

Try this workaround:

1. **Click "Preview"** in the top right of your draft
2. **Get the "secret draft link"** - on the Preview Post page, select Test and copy the URL in the "Secret draft link" section
3. **Open that draft link in a new tab/window**
4. **In that preview version**, hover over your H1 heading "lkzajdf" to see if the link icon appears
5. **If it does**, click it to get the anchor link
6. **Go back to your draft editor** and use that anchor link

This might work because the preview mode renders the post more like the published version, potentially generating the anchor IDs that aren't available in the regular draft editor.

If that doesn't work, unfortunately it seems like Substack's anchor link system is fundamentally broken for your use case - they designed it assuming people would add internal navigation after publishing, not before sending to subscribers. It's a poor design choice that forces exactly the problem you're experiencing.

The only other option might be to manually create HTML anchor tags if Substack allows HTML in posts, but that's getting pretty technical for what should be a basic feature.

### Millard · 2025-07-26 16:05

The Botticello article is obtuse. Please detail the steps for me yourself.

### Claude · 2025-07-26 16:05

Here are the detailed steps to get anchor links while your post is still in draft:

**Step 1: Get to the preview mode**

1. In your draft editor, click the "Preview" button (top right corner)
2. On the preview page, look for a section that says "Test" or "Share draft"
3. Copy the "Secret draft link" URL that's provided there

**Step 2: Open the draft link**

1. Open a new browser tab or window
2. Paste that secret draft link URL and go to it
3. This will show your post as it would appear when published, but it's still technically a draft

**Step 3: Get the anchor link**

1. In this preview version, scroll to your H1 heading "lkzajdf"
2. Hover your mouse to the left side of the heading text
3. A small link icon (🔗) should appear when you hover
4. Click that link icon - it will automatically copy the anchor link to your clipboard

**Step 4: Go back and use the link**

1. Return to your draft editor tab
2. Select the text you want to turn into a link (like "xxxx" in your screenshot)
3. Click the link button in the toolbar
4. Paste the anchor link you copied (it should look something like `#heading-id-12345`)
5. Click "Link"

The key is that the preview version (accessed via the secret draft link) has the anchor functionality active, even though the regular draft editor doesn't.

### Millard · 2025-07-26 16:16

it's much simpler: open the preview, find the heading, copy the link, change text in the draft into a link to the URL copied.

### Claude · 2025-07-26 16:16

You're absolutely right - that's much simpler and clearer than what I described. Thanks for the correction!

**The actual simple steps:**

1. Click "Preview" in your draft
2. In the preview, hover over the heading to get the link icon and copy the anchor URL
3. Go back to your draft editor
4. Select the text you want to link
5. Use the link tool and paste that copied URL

Much more straightforward than the convoluted "secret draft link" process I was describing. The preview mode itself gives you access to the anchor links - no need for extra steps with copying URLs to new tabs.
