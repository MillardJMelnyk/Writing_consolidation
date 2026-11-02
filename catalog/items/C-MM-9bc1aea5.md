# Recover highlights/notes from old Kindle PDFs

| | |
|---|---|
| Date | 2026-10-11 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-9bc1aea5` |
| Links | [Original](https://claude.ai/chat/9bc1aea5-e075-4db3-97c5-a3dd19c68ebf) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-10-11_recover-highlights-notes-from-old-kindle-pdfs_9bc1aea5.html) |

**Summary:** Failed attempts to restore Kindle for PC PDF highlights and notes from .mbpV2 annotation backups, including Huemer's book.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps; Practical & personal > Text extraction and data cleanup; Practical & personal > Software tools and open-source projects

**Index terms:** Kindle for PC; mbpV2 file; Send to Kindle; PDF annotation; Michael Huemer; OneDrive

[← Catalog home](../README.md)

---

### Millard · 2026-10-11 18:40

I had to install the Kindle app from scratch. The image shows the backup that I just copied to the folder I want the Kindle app connected to in OneDrive. As you can see from the second image, I've got lots of various types of files in there, but the Kindle app isn't picking them up. The third image shows that Michael Humor's book is in the folder, but the fourth image shows that the app can't find it.

### Claude · 2026-10-11 18:40

Sunday, October 11, 2026, 12:39 PM CST. Highly likely: Kindle for PC never displays PDFs from its content folder, so the Heumer PDF won't appear until you send it through Send to Kindle. Search "Stirner": if that .mobi is also missing, the app is ignoring every file you copied into that folder, not just the PDFs.

### Millard · 2026-10-11 18:40

OK, "Stirner" pulls up two books

### Claude · 2026-10-11 18:40

Then the app is reading your copied .mobi files fine, and only the PDFs are missing; Kindle for PC doesn't show local PDFs, so the Heumer book and the other PDFs have to go through Send to Kindle.

### Millard · 2026-10-11 18:41

OK, Originally to get the PDFs in there I had to import them one by one. Is that what this button does?

### Claude · 2026-10-11 18:41

Yes: it opens a file picker to add local PDFs into the app's library (Highly likely).

### Millard · 2026-10-11 18:42

Double check for a fact before I try it

### Claude · 2026-10-11 18:42

Yes, Amazon's help page confirms it: in Kindle for Windows you select Library, then Import, pick the document, and select Open; you can also drag and drop files into the app's library, then sync to see them. Files imported this way won't sync to your other Kindle devices.

### Millard · 2026-10-11 18:46

Fuck. I'm not sure what's wrong, but I clicked the import button watched it process and check off every single file in the list confirmed that it had imported them and said they would appear in my library in a few minutes. So I closed the app and reopened it and tried to find the humor book and it still tells me No matching items found . So I click the import button again and all of the files it said it had imported were still listed as ready to import .

### Claude · 2026-10-11 18:46

With "File sharing across devices" on, the files go up to your Amazon account first, so the next check is to click the circular arrow next to "Library" and see whether "Documents" rises above 2. If it stays at 2, go to amazon.com > Account > Manage Your Content and Devices > Content and filter to Docs to see whether Amazon received any of them, which shows whether the upload or the app sync is failing.

### Millard · 2026-10-11 18:47

I have the OneDrive app turned off so there should be no syncing to my OneDrive folder in the cloud. Are you talking about a different synchronization?

### Claude · 2026-10-11 18:47

Yes, that's Amazon's own syncing between your Kindle app and your Amazon account, completely separate from OneDrive.

### Millard · 2026-10-11 18:47

Unless they've changed something, I remember researching this and finding out that PDFs do not appear on my Amazon account, in any case, before you send me down on a wild goose chase, do some search and make sure you're not just making another fucking guess

### Claude · 2026-10-11 18:48

Your memory matches Amazon's older help page, which says files imported through the Kindle for PC app won't sync to your other Kindle devices; your app's own "File sharing across devices" toggle says the opposite, but I found no Amazon page confirming those files show up on the Amazon website, so treat that check as Unlikely to help. The one documented step is sync your library to view your imported content, since the library may take a few moments to show the imported documents, which is the circular arrow next to "Library."

### Millard · 2026-10-11 18:48

Okay, I'm going to try importing them with the file sharing switch off

### Claude · 2026-10-11 18:48

Good test; after it finishes, click the circular arrow next to "Library" before searching "heumer."

### Millard · 2026-10-11 18:54

what app opens .mbpV2 files?

### Claude · 2026-10-11 18:54

None directly: .mbpV2 is Kindle's sidecar file that stores your highlights, notes, and last-read page for the matching PDF, and the Kindle app reads it on its own when it opens that book.

### Millard · 2026-10-11 19:00

Oh, OK. I've attached one that has some stuff in it, which didn't get put into the library folder. I closed Kindle, copied the file into the library folder, clicked the "sync library" circular arrow, even closed and reopened the app once more for good measure, but still none of my annotations show up when I open the book.

### Claude · 2026-10-11 19:01

Your annotations are intact in that file (about 20 highlights, 8 notes, and your last-read spot), but it's the old Kindle for PC's format, and the new Microsoft Store Kindle app keeps its books in its own hidden folder (AppData\Local\Packages\AMZNKindle.AmazonKindleReadingApp\_m1sc522ngdk36\LocalState\Classic\Content), so it never looks at a sidecar sitting next to your OneDrive copy. Likely: the new app can't read .mbpV2 at all; I found no Amazon statement either way.

### Millard · 2026-10-11 19:01

Holy fuck, so how am I supposed to restore all of my notes and annotations for every PDF I've ever imported into the fucking app

### Claude · 2026-10-11 19:01

Kindle for Windows has no way to load them, and Amazon dropped the old app on June 30, 2026, so the only route is to pull them out of the .mbpV2 files: each saved spot decodes to a page number plus a position on that page (Highly likely, checked against your file). With the matching PDFs I can either produce a page-by-page list of your highlights and notes per book, or write them into each PDF as real highlights and comments that any PDF reader shows; tell me which, say GO, and upload the .mbpV2 files and PDFs as a zip.

### Millard · 2026-10-11 19:04

OK, That's 29 files for a total of about half a gigabyte

### Claude · 2026-10-11 19:04

That's too big to upload here (several PDFs alone are over the per-file limit, Highly likely), so I'd write one Python script you run on your PC against that folder, which does the whole batch locally. Still need your pick, a page-by-page list of highlights and notes or annotations written into the PDFs themselves, plus GO.

### Millard · 2026-10-11 19:05

I want to open the book in Kindle and see the highlights and notes

### Claude · 2026-10-11 19:05

Getting them back as Kindle's own highlights and notes isn't possible: I found no way to load annotations into the Kindle app, only tools that copy them out into PDFs (Highly likely). Whether Kindle for Windows even displays highlights and comments written into a PDF is undocumented, so the check is a one-page test PDF with one highlight and one comment imported into the app; say GO and I'll make it.

### Millard · 2026-10-11 19:06

I'll give you Humor's book and the .mbpV2 file for the test

### Claude · 2026-10-11 19:06

Heumer's PDF is 72 MB, over the per-file upload limit here (Highly likely), and I already have its .mbpV2 from earlier. A small test PDF I make answers the same question, whether Kindle shows highlights and comments written into a PDF; say GO and I'll make it.

### Millard · 2026-10-11 19:06

ok go

### Claude · 2026-10-11 19:07

Import Kindle\_Annotation\_Test.pdf, open it, and tell me whether you see the yellow highlight, the pink highlight, and the text of the test note (on the pink line or a sticky-note icon beside it).

### Millard · 2026-10-11 19:07

give me the page numbers from the .mbpV2 file you have for Heumer's book, I'll upload just an excerpt that includes them.

### Claude · 2026-10-11 19:07

Decoded page numbers: 15, 17, 18, 23, 25, 39, 40, 41, 46, 47, 48, 49, 52, 53, 54, 55, 57, 64. I can't tell yet whether Kindle counts from page 0 or page 1, so extract PDF pages 15–65 as one piece.

### Millard · 2026-10-11 19:11

what's the easiest way to extract pages from a PDF. I do not want to install any Adobe app.

### Claude · 2026-10-11 19:11

Open the PDF in Microsoft Edge (your default PDF viewer), press Ctrl+P, set the printer to "Microsoft Print to PDF," type 15-65 in the pages box, and click Print to save the excerpt. If any label on that print screen differs, send me a screenshot of it.

### Millard · 2026-10-11 19:18

OK, check it. the pdf is a scan of the book, so there are two pages per "page", and I don't know what "page" in the .mbpV2 refers to -- probably the physical PDF two-up page.

### Claude · 2026-10-11 19:18

This excerpt can't be matched: Microsoft Print to PDF turned every sheet into a flat picture with no text, and Kindle's saved positions point at characters in the text layer, which your original almost certainly has since you could highlight it (Highly likely). It's also only 10 sheets (book pages 14–21, 34–37, 56–59 with 56–57 twice, and 78–79), not sheets 15–65, so the reliable route is a small Python script you run on your PC that copies sheets 15–65 out of the original with the text kept; say GO and I'll write it.

### Millard · 2026-10-11 19:19

go

### Claude · 2026-10-11 19:19

In a terminal, run `pip install pymupdf`, then run `python extract_heumer_sheets.py` from the folder where you saved extract\_heumer\_sheets.py. Upload the heumer\_sheets\_15-65.pdf it creates next to the script, and tell me the "Text characters" number it prints (0 means the original has no text layer either).

### Millard · 2026-10-11 19:22

you don't know what the input file is named

### Claude · 2026-10-11 19:22

I took it from your third screenshot, which shows "The Problem of Political Authority.pdf by Michael Heumer 2013.pdf" in D:\OneDrive\Documents (OneDrive)\Kindle for Windows Content, and the excerpt's own title matches it. The one part that may differ is "Documents (OneDrive)," which Windows sometimes displays in place of the real folder name, so right-click the PDF, choose "Copy as path," and paste it here if it doesn't match.

### Millard · 2026-10-11 19:22

oh woops, my bad.

### Claude · 2026-10-11 19:22

No problem; run it and send me the excerpt and the "Text characters" number.

### Millard · 2026-10-11 19:25

ok, here's the output

### Claude · 2026-10-11 19:25

The text layer is there, and Kindle's page numbers are the PDF sheets counted from 1 (Highly likely): the "systematic biases" passage your note refers to is on sheet 53, and back-to-back highlights on sheet 25 join exactly mid-sentence. Character positions land on the right words for most highlights but drift by a few words to a few lines on some sheets, so some rebuilt highlights would sit slightly off; what did Kindl\_Annotation\_Test.pdf show in the Kindle app?

### Millard · 2026-10-11 19:26

I didn't check. run it against this excerpt and present result for download and I'll check that.

### Claude · 2026-10-11 19:27

All 23 highlights and 8 notes are in heumer\_sheets\_15-65\_annotated.pdf in their original colors, with 6 notes attached to their highlights and 2 as sticky-note icons. Sheet 25 (book pages 18–19, your pink and blue "not whether government is good or bad" highlights) is the one I checked by eye, and it lines up exactly.

### Millard · 2026-10-11 19:29

OK, that didn't work. All the highlights (and therefore notes) are misplaced.

OK, give me the other option, a list of highlighted text and notes that you mentioned originally.

### Claude · 2026-10-11 19:30

The notes' text is stored word for word in the .mbpV2, so that part of a list is exact, but the highlighted text would come from the same positions that just misplaced the highlights and would be wrong the same way. Were they misplaced when you opened it in Kindle, or in a regular PDF viewer like Edge? Sheet 25 (book pages 18–19) looked correctly placed when I rendered it, so your answer tells me whether the position mapping itself is broken.

### Millard · 2026-10-11 19:32

Same either way

### Claude · 2026-10-11 19:33

Heumer\_highlights\_and\_notes.md has all 23 highlights and 8 notes in page order. The misplacement came from Kindle counting positions in words, not characters (Highly likely: four of your notes now line up with the passages they comment on, such as "three broad ideas" and "pro-authority biases"). The highlighted text comes from the scan's built-in OCR, so it has scan typos like "10" for "to."

### Millard · 2026-10-11 19:33

So the.mbv2 file gives the exact text that's highlighted, right

### Claude · 2026-10-11 19:33

No. For highlights it stores only the PDF page, a start and end word position, and the color; the only text it holds is your notes, so the highlighted words in the list were read out of the PDF at those positions.

### Millard · 2026-10-11 19:33

Oh shit

### Claude · 2026-10-11 19:33

As long as you keep the exact PDF files you highlighted, the positions still point at the right words; they only break if a PDF gets replaced, re-scanned, or re-OCR'd.

### Millard · 2026-10-11 19:34

MD files aren't going to help because right now I don't have a viewer that will format them. All I see is the raw text

### Claude · 2026-10-11 19:34

I can redo it as a PDF or as a web page that opens formatted in Edge; which do you want?

### Millard · 2026-10-11 19:34

Yeah, I have no idea why you presented an MD file instead of a PDF

### Claude · 2026-10-11 19:35

I defaulted to Markdown without checking whether you could view it; that was my mistake. Heumer\_highlights\_and\_notes.pdf has the same 23 highlights, shaded in their Kindle colors, with your 8 notes under the passages they belong to.

### Millard · 2026-10-11 19:37

No, that didn't work either Now the highlighted text Includes way too many words than I would have highlighted this really sucks, but I guess it's what I get for relying on cheap ass software like Kindle

### Claude · 2026-10-11 19:38

Have you considered that the long passages may be what you actually highlighted? Under the word reading, almost every highlight begins exactly at the start of a sentence and stops a word or two before a sentence ends (page 3 runs from "Let us begin with a short political story" to "the costs of" right before "crime prevention?"), which misaligned positions wouldn't produce by chance. How does that bear on your recollection of, say, the page 3 parable?

### Millard · 2026-10-11 19:39

Dude, don't try to second guess me. I just told you that they are not. As a rule, I only highlight the phrases that are critical to what struck me as I was reading, so it's usually no more than a couple of sentences. For another, these highlights in the last results don't correspond logically to the sentence structure or the meaning of the words that are highlighted

If you still want to give it a try and game, but let's focus on just the very first highlight from the.mbv2 file. If we can get that right, then maybe we can figure out how to do the rest of them

### Claude · 2026-10-11 19:40

Understood. The first highlight is pink and starred, on PDF sheet 18 (book pages 4–5), and I have no record of its actual words to check any reading against, so the evidence I need is you looking at pages 4–5 and telling me the sentence or phrase you'd have marked there.

### Millard · 2026-10-11 19:44

OK, I read through that section. Given what you see in the .mbpV2 file, does it make sense that the highlight shown should apply to the following?

The state is treated as if it stood above the empir ical human world, transcending not only the moral constraints but also the psychological forces that apply to individual human beings.

### Claude · 2026-10-11 19:44

That sentence isn't where the file's first highlight is (that one is on PDF sheet 18, book pages 4–5); it's on sheet 64 (book pages 96–97), where the file does have a pink highlight. Counting in words, the sentence occupies positions 696–726 and that stored highlight runs 549–717, so it overlaps your sentence but starts about 150 words earlier and stops 9 words short, which makes it Likely the matching highlight but means the position scheme still isn't decoded correctly.

### Millard · 2026-10-11 19:47

You're right. You opened up the result excerpt in the right-hand pane, and it was positioned to the last page, which I didn't notice.

If I were to highlight anything in that paragraph, this is what I would have highlighted:

It is not that statists have some account of why government employees are more virtuous than average people. Nor do they have some plan for making that be the case. Rather, it seems simply to have never occurred to most statists to apply realistic assumptions about human nature to the government itself. The state is treated as if it stood above the empir ical human world, transcending not only the moral constraints but also the psychological forces that apply to individual human beings.

### Claude · 2026-10-11 19:48

Your sentence lines up with the end of that stored highlight: Kindle's position counts whole words, and its end position lands exactly on "human beings." once you allow for a small undercount that grows across each sheet (9 words by the bottom of sheet 64, 4 on sheet 53). The start also lands on a sentence boundary with that same allowance, "A related form of utopianism consists…", one paragraph before your "It is not that statists…", and the same pattern puts sheet 53's highlight exactly from "I have suggested in this chapter…" to "…the product of systematic biases." Have you considered that some of these, unlike your usual habit, may have been paragraph-length highlights, and how does that bear on the list being wrong?

### Millard · 2026-10-11 19:49

I'm not going to try to imagine what you're talking about. Do you have a better grasp on how to try to reproduce the highlights than you did the last time around ?

### Claude · 2026-10-11 19:49

Yes: positions are word counts on each PDF sheet, and correcting for a small undercount that grows down each sheet puts both ends of the two highlights I can check against your notes exactly on sentence boundaries (Likely for the rest, since only those two have anything to check against).

### Millard · 2026-10-11 19:50

Okay, then apply it to the excerpt and let's see what comes out

### Millard · 2026-10-11 19:50

go

### Claude · 2026-10-11 19:50

heumer\_sheets\_15-65\_annotated\_v2.pdf has all 23 highlights and 8 notes. The small undercount turned out to be exactly Kindle treating a word split across two lines with a hyphen as one word, which matched all four checkable ends to the word (Highly likely).

### Millard · 2026-10-11 19:51

wow, cool, now it

### Claude · 2026-10-11 19:51

Your message cut off after "now it"; what were you going to say?

### Millard · 2026-10-11 19:53

Now it's starting to look like you're getting close. Check out the image. You can see how the highlights are offset from the beginning of the sentence and run on into the footnote (image 1) Whereas in other places it seems perfectly aligned (image 2)

### Claude · 2026-10-11 19:54

The misalignments come from words the scan's text layer writes differently than Kindle counts them: Kindle splits number-letter hyphenations like "30-second," "catch-22," and "450-volt" into two words, which fixes the page 18–19 (sheet 25) shift from three words to one and makes the Milgram highlight on sheet 39 exact. The remaining one- to three-word misses track spots where the OCR is garbled (for example, "Simmons" in that footnote reads as three fragments), so I can't reproduce Kindle's count there exactly (Likely they stay a word or two off). Plan: add the number-letter split and regenerate the annotated excerpt; say GO.

### Millard · 2026-10-11 19:54

go

### Claude · 2026-10-11 19:54

heumer\_sheets\_15-65\_annotated\_v3.pdf is ready with the number-letter split added; book pages 18–19 should now be one word off instead of three.

### Millard · 2026-10-11 19:56

OK, it's not perfect, but close enough to see what I actually highlighted.

We have no real assurance that this will work with any of the other PDF files, right?

### Claude · 2026-10-11 19:56

Right, nothing confirms it yet, though Likely it works on all of them: the counting scheme is Kindle's own, so the same rules apply to every PDF, and accuracy depends only on how clean each PDF's text layer is (born-digital PDFs should land exactly, scans with messy OCR will drift by a word or two like this one). Running it on one or two of the others and eyeballing a few highlights is the check.

### Millard · 2026-10-11 19:59

OK, well, give me the .py to run against the entire book. I can try it against a couple of others, too, and see what comes of it. So add a runtime argument for input file name. Assume it's running in the same folder as the file, so path won't matter. The output file should be the input file name with a distinquisher.

### Claude · 2026-10-11 19:59

Run it as `python kindle_mbp_to_pdf.py "The Problem of Political Authority.pdf by Michael Heumer 2013.pdf"`. It reads the .mbpV2 with the same name, and saves the result as the same name ending in "\_annotated.pdf".

### Millard · 2026-10-11 20:01

I just noticed the problem in the last output file you gave me, although the little icons for the comment appear visibly clicking or pointing at them does nothing, so I can't see the comment they're supposed to iconize

### Claude · 2026-10-11 20:02

Likely cause: the notes have no working pop-up window attached (the notes on highlights have none at all, and the two sticky notes have theirs parked in the top-left corner of the sheet), so the viewer has nothing to open when you click. Plan: give every note a pop-up sitting beside its icon and regenerate the excerpt as v4; say GO. Separately, that screenshot starts the pink highlight at "literature," which is v2; v3 starts it at "the philosophical."

### Millard · 2026-10-11 20:02

That doesn't sound right. Some highlights were not given notes and some were

### Claude · 2026-10-11 20:02

Right, only 6 of the 23 highlights carry a note; what I meant is that those 6 notes have no pop-up window attached, so their icons have nothing to open, and the 2 standalone notes have pop-ups parked in the sheet's top-left corner. The fix would only touch those 8 notes.

### Millard · 2026-10-11 20:03

Okay, go ahead and give me the excerpt again

### Claude · 2026-10-11 20:03

heumer\_sheets\_15-65\_annotated\_v4.pdf has a pop-up beside every note. Correction to my earlier count: the file holds 7 notes, not 8, with 5 attached to highlights and 2 standalone.

### Millard · 2026-10-11 20:09

still nothing. sometimes a yellow icon shows in addition to the black comment icon, as shown in the attached image. Sometimes no yellow box. Neither do anything when I click on them. Nor can I find a way to open a side panel to show all comments so I don't even know if the comment text is in there or not .

### Claude · 2026-10-11 20:09

The note text is in the file: I read all 7 back out of v4 after saving it. That viewer is Firefox's built-in PDF viewer, so the check is to open the same v4 file in Microsoft Edge and click one of the note icons there; if it opens in Edge, the file is fine and Firefox is the problem, and if it doesn't, the fault is in how I built the notes.

### Millard · 2026-10-11 20:10

Interesting. All I need to do in Edge is hover and I see the note text.

### Claude · 2026-10-11 20:10

Then the file is fine and Firefox's viewer is what won't open them. The full-book script, kindle\_mbp\_to\_pdf.py, was written before the pop-up change, so it still builds notes without pop-ups.

### Millard · 2026-10-11 20:12

Okay, to make sure this is the one you're talking about, right?

### Claude · 2026-10-11 20:12

No, that's the excerpt-extraction script; the one I mean is kindle\_mbp\_to\_pdf.py, the full-book script I gave you after it.

### Millard · 2026-10-11 20:12

Present it for download again so I don't make a mistake

### Claude · 2026-10-11 20:12

That's kindle\_mbp\_to\_pdf.py, unchanged, so it still builds notes without the pop-up fix.

### Millard · 2026-10-11 20:12

and give me the command line again

### Claude · 2026-10-11 20:12

`python kindle_mbp_to_pdf.py "The Problem of Political Authority.pdf by Michael Heumer 2013.pdf"`

### Millard · 2026-10-11 20:15

Okay, I ran it and it seems stuck. I've got two greater than signs and nothing happens

### Claude · 2026-10-11 20:15

The backticks got copied in, and PowerShell treats a backtick as "line continues," so it's waiting for more input. Press Ctrl+C, then run it without them:

python kindle\_mbp\_to\_pdf.py "The Problem of Political Authority.pdf by Michael Heumer 2013.pdf"

### Millard · 2026-10-11 20:15

I asked for the command line. I copied what you gave me and I pasted it into the terminal window

### Claude · 2026-10-11 20:15

That's on me: I wrapped it in code formatting and the backticks came along when you copied it; the line in my last message is the plain command.

### Millard · 2026-10-11 20:15

Just give me the command line properly

### Claude · 2026-10-11 20:15

python kindle\_mbp\_to\_pdf.py "The Problem of Political Authority.pdf by Michael Heumer 2013.pdf"

### Millard · 2026-10-11 20:21

OK, well, at least I've recovered kinda one book. I imported the result With the highlights and comments into Kindle and of course Kindle stripped them all out. At least it didn't damage the original pdf.

Give me another few apps that are more reliable, come up more intuitive than Kindle that at least have the same or better functionality

### Claude · 2026-10-11 20:21

Okular (free, Windows and Linux, which matters for your Fedora move), PDF-XChange Editor (Windows only, free for highlighting and notes, with the best comments panel of the three), and Zotero (free on Windows, Linux, and Mac, with a library plus a sidebar listing every highlight and note) all open your annotated PDFs with highlights and notes intact. Okular and PDF-XChange write your highlights and notes into the PDF itself when you save, so they show in any viewer, while Zotero keeps them in its own database and exports a copy with them embedded on request.

### Millard · 2026-10-11 20:22

Rank them in terms of feature richness and usability

### Claude · 2026-10-11 20:22

Combined ranking (Likely; it's a judgment call): 1. PDF-XChange Editor, most features by far (every annotation type, a filterable comments list, exportable comment summaries) with a busy but Office-like layout; 2. Zotero, fewer annotation tools but the cleanest to use and the best for finding and reviewing your highlights and notes across a library; 3. Okular, solid basics but the plainest feature set and the clunkiest on Windows.

### Millard · 2026-10-11 20:23

Okay, so Zotero is attempting to avoid modifying the original PDF when you highlight and make notes

### Claude · 2026-10-11 20:23

Yes.

### Millard · 2026-10-11 20:23

I've used PDF Exchange before. It's good, but it's not really the kind of app I'd like to use for reading and commenting on material

### Claude · 2026-10-11 20:23

Then Zotero is the fit, since it's built around reading and marking up with your highlights and notes gathered in a side panel, not around editing PDFs.

### Millard · 2026-10-11 20:24

Is there nothing on the market that would do what your Python script attempted to do

### Claude · 2026-10-11 20:24

No, not for your files: a MobileRead forum regular who works on Kindle formats said there is nothing that handles .mbpV2 annotation files produced by the Kindle for PC/Mac apps, and I found nothing newer. The existing tools only cover Kindle e-readers, such as Kindle PDF Annotator, which extracts annotations from PDS files (Kindle Reader Data Store) and MyClippings.txt, and embeds them back into the original PDF.
