# Catalog tagging task (pass 2)

You are tagging items for a personal catalog of Millard J Melnyk's work: AI chats he had with Claude (IDs starting `C-`) and items from his Substack profile (IDs starting `S-`: his notes and posts, plus other people's notes/posts he restacked). Coding chats have already been removed.

## Inputs
- Your batch file: `/home/claude/cat/batches2/batch_NN.txt` (NN given in your task). Each item starts with
  `=== ID: <id> | <type> | <date> | <title>` followed by a digest (for chats: his messages and the first/last Claude reply, possibly truncated with […]).
  Some Substack items end with an `IMAGES:` line listing local image files. Those notes have little or no text: OPEN EVERY listed image with the Read tool and use what the image shows (text in it, people, subject, context) to describe and tag the item.
- The topic outline: `/home/claude/cat/tree_v1.md` (`# Topic` lines, `- Subheading` lines under them).

Read the WHOLE batch file (Read tool with offset/limit in chunks until the end) and the whole outline. Every item must get exactly one output record.

## For each item
1. `summary` — one plain sentence, at most 25 words, saying what the item is about (for restacks: what the restacked content says). For items with images, describe what the image shows and its point. No praise, no "In this chat…".
2. `caption` — ONLY for items with an `IMAGES:` line: a short factual description of the image(s), at most 40 words, including any readable headline or key text. Omit the field for other items.
3. `topics` — EVERY subheading in the outline that the item's content substantially fits, 1 to 9 entries, each exactly `Topic > Subheading` copied character-for-character from the outline. File by what the item is ABOUT (its content), never by what kind of item it is. Do not pad: only subheadings the content genuinely addresses. If nothing in the outline fits, use `NEW: Topic > Subheading` (an existing topic name if one fits, else a new short, specific, content-describing topic).
4. `terms` — 3 to 8 index terms, as in the index of a book: specific subjects, concepts, people, organizations, places, works (books, laws, films), events. Canonical form: people as "Firstname Lastname" (full name only when it is actually stated or unmistakable — never invent), organizations by common full name, concepts as short noun phrases in lowercase unless a proper noun. Singular. No generic words ("discussion", "question", "AI response", "chat", "Substack note", "image").

## Output
Write JSON Lines to `/home/claude/cat/out2/batch_NN.jsonl` — one line per item, in batch order:
`{"id": "<id>", "summary": "...", "caption": "...", "topics": ["Topic > Subheading"], "terms": ["term"]}` (no "caption" key when there are no images).
Valid JSON on every line. Create the folder if needed. For long output, write in parts with Bash appends (heredoc with a quoted delimiter); the final file must contain every item exactly once.

Then verify with a short `python3 -I` check: every `=== ID:` in the batch appears exactly once in your output, every line parses, and every non-NEW topic matches the outline exactly. Fix any problems.

Reply with only: batch number, item count, output line count, and any `NEW:` topics you used.
