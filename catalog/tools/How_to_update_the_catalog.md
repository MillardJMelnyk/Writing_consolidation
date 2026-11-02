# Catalog tools — how the catalog was built and how to update it

[← Catalog home](../Master_catalog.md)

Everything needed to add new material and rebuild the catalog. Built 2026-11-02.

## What's here

- `scripts/` — the programs that built the catalog:
  - `pull_feed.py` — pulls every item listed on substack.com/@millardjmelnyk.
  - `build_entries.py` — turns the pulled Substack data into clean entries and downloads the images.
  - `build_pdfs.py` — makes the searchable Substack PDFs.
  - `extract_items.py` — reads the Substack entries and the AI chat files (from the AI_Chats repo) into one item list, and cuts the reading batches for the helper agents.
  - `finalize_tags.py`, `finalize_tags2.py` — merge the helper agents' tags (first pass, second pass) into one file and build the topic tree with counts.
  - `build_catalog.py` — writes all catalog pages: item pages, item lists, A–Z index, topic outline, data lists.
  - `build_search_html.py` — writes `Master_catalog.html`, the downloadable copy of the master catalog page with search by meaning and by exact words. It uses the files in `search_build/`.
  - `fit_projection.py` — fits the fingerprint shrinking stored in `search_build/projection.json`.
  - `build_html.py`, `build_semantic.py` — earlier versions, replaced by `build_search_html.py`.
- `search_build/` — the search page's parts: page template and code, the meaning model and its browser engine, tokenizer and projection.
- `Search_index_format.md` — the layout of the `catalog_search_index.js` file the page builds, for use by other programs.
  - `build_items.py` — older item-page builder, replaced by `build_catalog.py`.
- `READ2_INSTRUCTIONS.md` — the instructions the helper agents follow when tagging items (current version). `READ_INSTRUCTIONS.md` is the first-pass version.
- `tree_v1.md` — the current topic tree the agents tag against. `seed_tree.md` is the first draft.
- `data/` — the working data:
  - `items.jsonl` — every item with its full text (Substack + all chats, including coding and empty chats).
  - `tags_final2.jsonl` — the final tags for the 2,270 catalogued items: summary, image caption, topics (up to 9), index terms.
  - `tags_final.jsonl` — first-pass tags; holds the coding / not-coding decision for every chat.
  - `empty_fix.json` — the 46 empty chats that were dropped (31 with no messages, 15 deleted from claude.ai).
  - `substack_raw/`, `substack_entries.json` — the Substack data as pulled on 2026-11-01.

## Rules agreed so far

- Every discrete item (note, post, chat, page, file) gets its own page with full text and a link to the original.
- Items are filed under every topic subheading that fits (up to 9) and get 3–8 index terms.
- Headings describe content, never the type of item.
- Coding chats are left out for now (listed in `../data/set_aside_coding_chats.csv`).
- Empty chats are dropped. Empty Substack notes are kept.
- Every list is shown both by date and by title.

## Adding new material

1. Put the new material where it can be read (a new export in a repo, or a source that can be pulled).
2. Turn it into items in the same form as `data/items.jsonl`, with new permanent IDs that never reuse old ones.
3. Have helper agents tag only the new items with `READ2_INSTRUCTIONS.md` against `tree_v1.md`; any new branches they propose get added to the tree.
4. Add the new tags to `data/tags_final2.jsonl` and rerun `build_catalog.py` to rebuild every page.
   Then rerun `build_search_html.py` to rebuild `Master_catalog.html`. Note: the search index people build on their own computers is not updated automatically; handling updates is still to be designed.
5. Check links and counts, then upload.
