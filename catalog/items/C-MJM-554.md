# Understanding projects and their use cases

| | |
|---|---|
| Date | 2025-12-31 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-554` |
| Links | [Original](https://claude.ai/chat/3d0a9f17-59d3-4c9e-afc0-474d3c790e6c) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/554-2025-12-31-understanding-projects-and-their-use-cases.html) |

**Summary:** Explains how Claude Projects work, their knowledge base and instructions, and how to move existing chats into a project.

**Topics:** AI chatbots and working with Claude > Claude account, limits and chat management; AI chatbots and working with Claude > Chat archives and moving chats

**Index terms:** Claude Projects; knowledge base; custom instructions; chat organization

[← Catalog home](../Master_catalog.md)

---

### Millard · 2025-12-31 20:17

I haven't used projects yet, please explain how they work and what use cases they support

### Claude · 2025-12-31 20:18

**Claude Projects** are self-contained workspaces that maintain persistent context across conversations.

**Core Mechanics:**

1. **Project Knowledge Base** — Upload documents (PDF, DOCX, CSV, TXT, HTML, code files, etc.) that Claude references across all chats within that project. 200,000 token context window (~500 pages). Paid plans automatically enable RAG mode when approaching limits.
2. **Custom Instructions** — Define persistent behavioral directives for all chats within the project (tone, role, response format, domain constraints).
3. **Conversation History** — All chats within a project are organized and accessible from the project page. Context is *not* shared between chats unless added to the knowledge base.
4. **Memory Segmentation** — Claude maintains separate memory summaries per project, distinct from non-project chats.

**Availability:**

* Free accounts: 5 projects max
* Pro/Max: Unlimited projects
* Team/Enterprise: Sharing and collaboration features (permission levels: "Can use" vs "Can edit")

**Primary Use Cases:**

| Use Case | Application |
| --- | --- |
| Codebase assistance | Upload documentation, style guides, architecture docs |
| Client work | Per-client projects with contracts, transcripts, requirements |
| Content creation | Style guides, brand voice docs, past examples |
| Research | Source documents, literature, ongoing notes |
| Course/training | Syllabi, materials, FAQs for consistent reference |

**Operational Notes:**

* Project name/description are for *your* organization only — Claude doesn't see them
* Files uploaded *during* a chat aren't automatically added to project knowledge; you must explicitly add them
* You can move existing standalone chats into projects
* Archiving resets all sharing permissions

**Access:** claude.ai/projects (left sidebar → Projects)

### Millard · 2025-12-31 20:19

Can I move stand-alone chats into a project after the fact of the chat?

### Claude · 2025-12-31 20:19

Yes.

**Methods:**

1. **From within the chat** — Click the dropdown arrow next to the chat name → "Add to project" → select destination project
2. **Bulk from chat history** — Go to claude.ai/recents → select multiple chats → click the move icon next to the selection count → choose project

You can also remove chats from projects or move them between projects using the same dropdown menu.
