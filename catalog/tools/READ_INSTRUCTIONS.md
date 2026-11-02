# Catalog reading task

You are tagging items for a personal catalog of Millard J Melnyk's work: AI chats he had with Claude (IDs starting `C-`) and items from his Substack profile (IDs starting `S-`: his notes and posts, plus other people's notes/posts he restacked).

## Inputs
- Your batch file: `/home/claude/cat/batches/batch_NN.txt` (NN is given in your task). Each item starts with a line
  `=== ID: <id> | <type> | <date> | <title>` followed by a digest of the item (for chats: his messages and the first/last Claude reply, possibly truncated with […]).
- The topic outline: `/home/claude/cat/seed_tree.md` (`# Topic` lines, `- Subheading` lines under them).

Read the WHOLE batch file (use the Read tool with offset/limit in chunks until you reach the end) and the whole outline. Every item in the batch must get exactly one output record.

## For each item, decide
1. `coding` — true if the item is mainly about writing, debugging or reviewing code or software (MQL5, Python, scripts, indicators, Expert Advisors, PowerShell, spreadsheets formulas, app/tool building). General tech support or how-to without code is NOT coding. Substack items are never coding.
2. `summary` — one plain sentence, at most 25 words, saying what the item is about (for restacks: what the restacked content says). No praise, no "In this chat…".
3. `topics` — 1 to 3 entries, each exactly `Topic > Subheading` using names copied character-for-character from the outline. If nothing in the outline fits, use `NEW: Topic > Subheading`, where Topic is an existing topic name if one fits, or a new topic name; keep new names short and specific. Coding items: give `[]`.
4. `terms` — 3 to 8 index terms, like the index of a book: specific subjects, concepts, people, organizations, places, works (books, laws, films), events. Canonical form: people as "Firstname Lastname" (full name when known), organizations by common full name, concepts as short noun phrases in lowercase unless a proper noun (e.g. "codependence", "informed consent", "Nuremberg Code"). Singular. No generic words ("discussion", "question", "AI response", "chat"). Coding items: give `[]`.

## Output
Write a JSON Lines file to `/home/claude/cat/out/batch_NN.jsonl` — one line per item, in batch order:
`{"id": "<id>", "coding": false, "summary": "...", "topics": ["Topic > Subheading"], "terms": ["term", "term"]}`
Valid JSON on every line (escape quotes). Create the folder if needed. If the file would be very long, write it in parts with Bash appends (e.g. a heredoc with a quoted delimiter) — but the final file must contain every item exactly once.

Then verify with Bash: count the `=== ID:` lines in the batch file and the lines in your output, and check that every ID appears once (e.g. a short python3 -I one-off). Fix any gaps.

Reply with only: batch number, item count, output line count, number of coding items, and any `NEW:` topics you used.
