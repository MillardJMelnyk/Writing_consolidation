# How to use the catalog

[← Master catalog](Master_catalog.md)

## Two ways to use the catalog

- **On GitHub:** open the master catalog page (below). Everything is one click from there.
- **From your own computer:** download **Millards_master_writing_catalog.html** and **Millards_master_writing_catalog_manager.py** into one folder and start the catalog with Millards_master_writing_catalog_manager.py. You get the same links as the master catalog page, plus a **search box** that searches all items by meaning or by exact words.

### Downloading the two files

1. Click https://github.com/MillardJMelnyk/Writing_consolidation/blob/main/catalog/Millards_master_writing_catalog.html, then, at the top right of the file next to **Raw**, click the download button (the arrow pointing down).
2. Do the same for https://github.com/MillardJMelnyk/Writing_consolidation/blob/main/catalog/Millards_master_writing_catalog_manager.py
3. Move both files into the same folder.
4. Remove Windows' "downloaded from the internet" mark from both: open PowerShell in that folder and run
   `Unblock-File "Millards_master_writing_catalog.html"; Unblock-File "Millards_master_writing_catalog_manager.py"`
   (or right-click each file, choose **Properties**, tick **Unblock** on the **General** tab, and click **OK**).

Millards_master_writing_catalog_manager.py needs Python 3.9 or newer on your computer.

### Starting the catalog

- **The first time:** double-click **Millards_master_writing_catalog_manager.py** (or a shortcut to it). It sets up search (see below) and opens the catalog in your browser. Its window shows what it's doing; leave it open until the search index is built. It closes by itself, unless something went wrong, in which case it stays open showing the error.
- **After that:** open the catalog either way: double-click Millards_master_writing_catalog.html, or run Millards_master_writing_catalog_manager.py again.

The two files must keep matching names: the script's name is the page's name plus "_manager".

### First start: search setup

The first time, Millards_master_writing_catalog_manager.py gets the parts it needs (Python packages and the meaning model, about 25 MB), and the page sets up the search. A yellow box at the top of the page shows each step and how long is left.

- It reads every catalog item from GitHub, so you need an internet connection.
- Keep the page open until it says **Search setup finished**. The links work in the meantime.
- The finished index is saved as **catalog_search_index.js** in the same folder, and search switches on by itself. After that, search is ready within seconds whichever way you open the catalog.
- If the catalog page is replaced by a newer version with different items, run Millards_master_writing_catalog_manager.py again to set up search for it.

### Searching

1. Type a word, phrase or idea in the search box and press Enter or click **Search**. The results open on their own page; the browser's back button, or **← Master catalog** at the top or bottom, takes you back.
2. **By meaning** finds passages that express the idea, even in different words. **Exact words** finds the words exactly as typed, in that order.
3. **Level** sets what each result is: a phrase, a sentence, a paragraph, a passage or section, or a whole item. A result counts if what you searched for is present anywhere in it.
4. **Strictness** (meaning search only): move it right for closer matches only, left for looser ones.
5. **Only my own words** leaves out Claude's replies and other people's restacked or quoted text. **Type** and **From / to** limit the results by kind of item and by date.
6. **Sort**: *Strongest first* puts first the results most taken up with what you searched for; *Newest first* sorts by date.
7. Each result shows the item's title (click it to open the item), date, type, strength, and an excerpt with the match highlighted. Excerpts and items are read from GitHub, so they need an internet connection; the search itself does not.

## Opening the catalog

1. Click this link: https://github.com/MillardJMelnyk/Writing_consolidation/blob/main/catalog/Master_catalog.md — it opens the master catalog page directly.
2. Bookmark that page. From then on, opening the catalog is one click.

The master catalog page has three links: **All items**, **A–Z index** and **Topic outline**.

## Finding things by topic

1. On the master catalog page, click **Topic outline**. Every topic is listed with its number of items, and its subheadings underneath.
2. Click a topic name to see every item under it, or click a subheading to see only its items.
3. At the top of every list page: the number of items and **Sort: by date · by title**. Click either to jump to that version of the list.
4. Click any title to open that item.

## Finding a name, subject or term

1. On the master catalog page, click **A–Z index**, then click a letter.
2. Each entry shows its number of items in brackets. Click the entry to see its items, sortable the same way.

## Browsing everything

1. On the master catalog page, click **All items**.
2. Click a year (newest first) or a letter (by title).

## On an item's page

- At the top: date, type, source, and links to the **Original** (the Substack note, post, or claude.ai chat) and the **Archived file**.
- Then the summary, the image description (for image notes), its topics and its index terms.
- Below the line: the full text, and any images at the end.
- **← Catalog home** at the top, or your browser's back button, takes you back.

## Searching for a word

Type the word in the search box at the top of any page of the repository and press Enter. GitHub lists the catalog pages that contain it.

## Data lists

On the master catalog page, the **ai_chats** and **substack** links open one list per source as a table: every item with its date, title, summary, topics and index terms.
