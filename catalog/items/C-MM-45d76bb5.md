# Claude chat storage in VS Code

| | |
|---|---|
| Date | 2026-07-08 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-45d76bb5` |
| Links | [Original](https://claude.ai/chat/45d76bb5-0c3c-4716-98aa-15d9e70a1537) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-07-08_claude-chat-storage-in-vs-code_45d76bb5.html) |

**Summary:** Where Claude Code stores VS Code chat transcripts as JSONL and a PowerShell script to convert them to searchable HTML.

**Topics:** AI chatbots and working with Claude > Chat archives and moving chats; Practical & personal > Software tools and open-source projects

**Index terms:** Claude Code; Codex; JSONL; Visual Studio Code; PowerShell; chat transcript

[← Catalog home](../README.md)

---

### Millard · 2026-07-08 14:09

I use both CODEX and Claude in VS code. CODEX Stores chat transcripts as JSONL files in dated folder in a "Sessions" folder. How does Claude do it?

### Claude · 2026-07-08 14:09

Same idea, different location. Claude Code writes each session as a JSONL file, one JSON object per line (messages, tool calls, metadata), stored at:

`C:\Users\<you>\.claude\projects\<sanitized-project-path>\<session-uuid>.jsonl`

The project path is flattened into the folder name with dashes — your workspace would land in something like `C--Temp-C-MQL5`. So the grouping is per-project-folder rather than per-date, and files are named by session UUID rather than timestamp. `claude --resume` reads these same files to restore sessions.

I couldn't verify against live docs from here; the format has been stable, but if the folder isn't where I said, check `%USERPROFILE%\.claude\projects` and it'll be obvious from there.

### Millard · 2026-07-08 14:17

There's a utility for converting CODEX chats to html for reference and TEXT SEARCHING -- which is something I'm baffled about, why VS Code or at least the CODEX and Claude extensions don't offer one natively.

& "C:\Temp-C\MQL5\Convert-CodexChat.ps1.txt" "pathname-of-chat.jsonl"

Is there something comparable or a comparable way to handle Claude chats?

### Claude · 2026-07-08 14:17

Nothing native, same gap. Options:

1. **Raw text search works today, no conversion.** The JSONL is plain UTF-8, so:  
   `Select-String -Path "$env:USERPROFILE\.claude\projects\*\*.jsonl" -Pattern "TickTravel"`  
   finds every session mentioning a term. Ugly output, but instant full-corpus search.
2. **Built-in `/export`** — inside a Claude Code session, `/export` writes the current conversation to a file or clipboard. Per-session, manual, no batch mode.
3. **Community converters** exist (e.g. `claude-code-log` on PyPI, which renders whole `~/.claude/projects` trees to HTML) — but I haven't verified current state or names against live sources, so treat that as a pointer, not a recommendation.
4. **Direct equivalent of your Codex script.** The JSONL schema is simple: each line has a `type` field (`user`/`assistant`), message content, timestamps. A `Convert-ClaudeChat.ps1` doing the same job as your Codex one — JSONL in, searchable HTML out — is maybe 60–80 lines.

Want me to write option 4? Plan: standalone PS1 script, takes a `.jsonl` path (or a project folder for batch), emits one HTML per session with user/assistant turns styled distinctly, tool calls collapsed, plain text preserved for Ctrl+F. Written as a normal script file, no here-docs. Say GO and I'll produce it here for you to drop into `C:\Temp-C\MQL5`.

### Millard · 2026-07-08 14:18

2, cool, what export formats are possible?
==========================================

### Claude · 2026-07-08 14:18

Two destinations, one format: `/export` gives you a choice of copying to clipboard or saving to a file, and the content is plain-text/Markdown — the conversation rendered as readable text. No HTML, no JSON, no PDF options.

So for Ctrl+F-able reference it's fine (Markdown in any editor is text-searchable), but it won't give you the styled-HTML experience your Codex script produces, and it's one session at a time from inside that session.

Caveat stated as fact, not insurance: my docs access is blocked from this environment, and `/export` has been evolving across releases — current builds may have grown format flags. `claude /help` or typing `/export` and looking at the prompt in your installed version is ground truth.

### Millard · 2026-07-08 14:19

sure, write me an option #4

### Claude · 2026-07-08 14:20

Done. Single file or folder (recursive batch), one HTML per session, user/assistant/tool-output turns color-coded, tool calls and thinking collapsed in `<details>`, everything HTML-encoded plain text so Ctrl+F works. Output lands next to the source unless you pass `-OutDir`.

Two honest caveats: no PowerShell in this environment, so it's untested — syntax is careful but expect possibly one shakedown run. And the schema handling (`type`, `message.content` as string-or-blocks, tool\_result-only user lines relabeled "tool output") is from knowledge of the format, not verified against your live files; the `default` branch dumps any unrecognized block as raw JSON so nothing silently disappears. If a real session renders wrong, paste me one anonymized line and I'll fix the mapping.
