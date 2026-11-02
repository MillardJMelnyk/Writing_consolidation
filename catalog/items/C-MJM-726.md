# Everything subfolder search settings

| | |
|---|---|
| Date | 2026-08-07 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-726` |
| Links | [Original](https://claude.ai/chat/b49d8e6d-eeea-43cb-9ba2-3db3cebb1eee) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/726-2026-08-07-everything-subfolder-search-settings.html) |

**Summary:** Voidtools Everything showing only top-level folder contents because the sidebar Subfolders checkbox was unchecked.

**Topics:** Practical & personal > Software tools and open-source projects

**Index terms:** Everything; voidtools; subfolder search; file search

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-08-07 15:35

where is the setting in Everything that controls whether results will include subfolder contents?

### Claude · 2026-08-07 15:36

Two different things, depending on which "subfolders" you mean:

**1. Global search results (default behavior)** — Everything has no on/off toggle for this; it always searches the entire flat index, so subfolder contents are included by default. To *restrict* to a folder without subfolders, you use search syntax, not a setting: `parent:<path>` (v1.5) or a custom filter with `parent:$param:` (per the voidtools forum — see the "Permanently exclude subfolders" thread ).

**2. Folders sidebar (Everything 1.5)** — if you mean the treeview pane on the left, there's a **"Subfolders" checkbox** right in that pane. In the folders sidebar pane, you can uncheck "Subfolders." That's the actual UI setting controlling whether subfolder contents show for the selected folder.

**3. Indexing scope (what gets indexed at all)** — Tools > Options > Indexes > Folders, where each added folder indexes its subfolders by default unless excluded via Tools > Options > Indexes > Exclude, per the forum threads above.

Which one are you after — restricting a live search, the sidebar treeview, or the index scope?

### Millard · 2026-08-07 15:37

I mean #1. Yes, what you described as default is what I'm used to. Now it's only showing me the contents of a given folder, nothing from inside its subfolder.

### Claude · 2026-08-07 15:37

Setting: **Search menu → uncheck "Match Path"** (and confirm no other Search-menu option is checked except the Everything filter itself). Enabling Match Path under the Search menu caused someone's search to stop showing folder contents recursively, and unchecking it fixed it.

Two other things to check under the same **Search** menu:

1. **Trailing `\*` in your search bar or a saved filter.** In v1.5, `c:\path\*` explicitly means "direct children only, no subfolders." Adding \* to a path excludes subfolders — c:\windows\* finds files/folders directly in c:\windows with no results from subfolders. If you or a filter appended that, remove it.
2. **Active filter restricting to parent-only.** A user-created filter of the form parent:search: (or parent:$param: in v1.5) is designed to show only items directly under a folder, excluding subfolders — if you or someone else added such a filter and it's toggled on in the Search menu, that would produce exactly this symptom.

Quickest diagnostic: clear the search box entirely, retype the folder name plainly with no modifiers, and check the Search menu — everything under it should be unchecked except possibly "Everything" filter itself.

### Millard · 2026-08-07 15:38

[File attached: 1786117104263\_image.png — contents not included in export]

### Claude · 2026-08-07 15:38

None of the toggles here are checked — "Match Path" is off, and "Everything" (bullet) is the active filter, which is correct default. So the restriction isn't coming from this menu.

Next place to check: **Search → Advanced Search...** dialog. It has an explicit depth/subfolder control separate from these quick toggles. Open it and check that field.

If that's also clear, the remaining candidates are:

* A literal `\*` (or similar) sitting in the search box itself — trailing `\*` restricts to direct children only.
* A custom filter (not "Everything") that got selected via the **filter bar** (View → Filters) rather than this dropdown — the dropdown only shows one bullet, but if you have a filter bar visible separately, check what's selected there too.

Can you open Advanced Search and post what's in the folder/depth field?

### Millard · 2026-08-07 15:38

[File attached: 1786117136746\_image.png — contents not included in export]

### Claude · 2026-08-07 15:39

"Include subfolders" is checked. Not the source.

Ruled out so far: Search-menu toggles, active filter, Advanced Search dialog. That leaves the search box itself. Post the exact text currently in the search bar — check specifically for a trailing `\*`, a `parent:` prefix, or a filter macro token (e.g. `::parent:`) hiding in it.

### Millard · 2026-08-07 15:40

Obviously, my C: drive has more than 36 items in it.

[File attached: 1786117197803\_image.png — contents not included in export]

### Claude · 2026-08-07 15:40

Found it. Left sidebar, below the Folders tree: **"Subfolders" checkbox — unchecked.**

That's the setting. It's not a search-bar toggle at all — it's the Folders sidebar (View → Folders) driving this. With Local Disk (C:) selected there and "Subfolders" off, you get direct children only, which is exactly the flat 36-ish-item C:\ listing you're seeing.

Check that box and you'll get the full recursive contents back.

### Millard · 2026-08-07 15:40

lol, little invisible runt

### Claude · 2026-08-07 15:40

That's it exactly — small, unlabeled scope, easy to lose track of once you've selected a drive in the sidebar.
