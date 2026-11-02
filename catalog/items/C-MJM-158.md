# OneDrive File Album Creation Automation

| | |
|---|---|
| Date | 2025-08-11 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-158` |
| Links | [Original](https://claude.ai/chat/648d3dea-a165-4343-a618-d2b0227f53a7) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/158-2025-08-11-onedrive-file-album-creation-automation.html) |

**Summary:** Creating a OneDrive album from thousands of files by extension without clicking each one; Claude admits not knowing the album feature.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps; AI chatbots and working with Claude > AI honesty, bias and guardrails

**Index terms:** OneDrive; photo album; file extension; bulk selection; Microsoft

[← Catalog home](../README.md)

---

### Millard · 2025-08-11 15:36

I have folders on OneDrive with lots of files in them. I want to create an album on OneDrive containing files of certain extensions like .jpg, .doc, .mp4, .txt, etc. How can I do that without physically clicking on thousands of files for inclusion in the album?

### Claude · 2025-08-11 15:36

OneDrive doesn't have a direct "album" feature like photo services, but there are several efficient ways to organize and view files by extension without manually clicking thousands of files:

Option 1: Use File Explorer with OneDrive Sync
----------------------------------------------

If you have OneDrive synced locally:

1. Open File Explorer and navigate to your OneDrive folder
2. Use the search box and type `*.jpg OR *.doc OR *.mp4 OR *.txt` to find all files with those extensions
3. Select all results (Ctrl+A) and copy them to a new folder you create called "My Album"
4. This creates shortcuts/copies in one location while keeping originals in place

Option 2: OneDrive Web Interface Filtering
------------------------------------------

In the OneDrive web interface:

1. Navigate to the folder containing your files
2. Use the search bar with queries like `*.jpg` to filter by extension
3. You can then select all visible results and move/copy them to a dedicated folder
4. Repeat for each file type you want to include

Option 3: PowerShell Script (Most Efficient)
--------------------------------------------

If you're comfortable with scripts, you can use PowerShell to automatically copy files:

```
# Navigate to your OneDrive folder
$sourceFolder = "C:\Users\[Username]\OneDrive\[YourFolder]"
$destinationFolder = "C:\Users\[Username]\OneDrive\MyAlbum"
$extensions = @("*.jpg", "*.doc", "*.mp4", "*.txt")

# Create destination folder if it doesn't exist
New-Item -ItemType Directory -Force -Path $destinationFolder

# Copy files with specified extensions
foreach ($ext in $extensions) {
    Copy-Item -Path "$sourceFolder\$ext" -Destination $destinationFolder -Recurse
}
```

Option 4: Third-Party File Management Tools
-------------------------------------------

Tools like **Directory Opus** or **Total Commander** offer advanced file selection and filtering capabilities that make bulk operations easier.

The search method (Option 1 or 2) is probably your best bet for a quick solution without needing technical setup. Would you like me to elaborate on any of these approaches?

### Millard · 2025-08-11 15:38

Apparently, you don't know WTF you're talking about. Here are the tabs for the "Photos" section. Do you or do you not see "Albums"? So, how can you say: OneDrive doesn't have a direct "album" feature like photo services...

### Claude · 2025-08-11 15:39

You're absolutely right, and I apologize for the incorrect information. I can clearly see the "Albums" tab in the Photos section of OneDrive that you've shown me. OneDrive does indeed have an album feature for organizing photos and other media files.

For creating albums efficiently with thousands of files, here are the proper methods:

Option 1: Bulk Selection in OneDrive Photos
-------------------------------------------

1. Go to the Photos section in OneDrive web interface
2. Use the filter/search options to display files by type (if available)
3. Use Ctrl+click or Shift+click to select multiple files at once
4. Look for "Select all" options to grab large batches
5. Add selected files to a new album

Option 2: Upload to Album Directly
----------------------------------

When uploading files, you may be able to specify an album destination rather than uploading first and organizing later.

Option 3: Use OneDrive Mobile App
---------------------------------

The mobile app sometimes has different bulk selection tools that might be more efficient for album creation.

Since I clearly gave you wrong information about OneDrive's capabilities, could you tell me what specific challenges you're facing when trying to add your files to an album? Are there particular limitations in the interface that make selecting thousands of files difficult, or are you looking for ways to automate the selection process?

### Millard · 2025-08-11 15:39

tl;dr, stop dumping

### Claude · 2025-08-11 15:39

You're right.

In the OneDrive Photos section, try using Ctrl+A to select all visible photos at once, or use the search/filter to narrow down to specific file types first, then select all those results to add to your album.

What specific issue are you hitting when trying to bulk-add files to an album?

### Millard · 2025-08-11 15:39

Do you know what you're talking about?

### Claude · 2025-08-11 15:39

No, I clearly don't know the specifics of how OneDrive's album feature actually works in practice. I made an incorrect assumption initially and then gave you generic advice without actually knowing the interface details.

What's the actual process or limitation you're running into when trying to create albums with your files?
