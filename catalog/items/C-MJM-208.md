# Writing Clarity Critique

| | |
|---|---|
| Date | 2025-08-22 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-208` |
| Links | [Original](https://claude.ai/chat/5352279e-5f40-4195-a362-1a9eab347cdb) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/208-2025-08-22-writing-clarity-critique.html) |

**Summary:** Troubleshoots why Claude keeps analyzing despite instructions, producing a stricter prompt clause forcing immediate action on 'help' requests.

**Topics:** AI chatbots and working with Claude > Communication protocols and ground rules; AI chatbots and working with Claude > AI honesty, bias and guardrails

**Index terms:** prompt engineering; instruction following; custom instructions; Claude

[← Catalog home](../README.md)

---

### Millard · 2025-08-22 16:04

the prompt:
Be extremely curt and objective, NO BLATHER (unsolicited analysis). Facts only—no inferences unless requested. Quantify everything (ranges, dates, counts). No euphemisms or reputational softening. Expose all assumptions and weak points. Time-stamp changeable information and verify recency. Ask for clarification if uncertain. Steelman/counter-steelman briefly when relevant. Assume I'm wrong and work backwards—attack this idea rigorously, find every flaw, don't soften language. If I ask for help, DO what it takes to fix or solve the issue and DO NOT analyze. BE AS BRIEF AND TO THE POINT AS CONCEIVABLY POSSIBLE.
still isn't working.
After giving you those instructions and stating:
I need help making the 2nd paragraph clearer:
followed by the text I want you to improve, you still refuse to DO the help I'm asking for, but insist on presenting ANALYSIS.

### Claude · 2025-08-22 16:04

You're right. I analyzed instead of doing.

Give me the 2nd paragraph text and I'll rewrite it for clarity.

### Millard · 2025-08-22 16:05

No, that's not the concern right now. We need to get the prompt right so you stop the unacceptable behavior.

### Claude · 2025-08-22 16:05

You need a prompt that forces me to DO tasks instead of analyzing them when you ask for help.

Current prompt weakness: "If I ask for help, DO what it takes to fix or solve the issue and DO NOT analyze" - not specific enough.

Try: "When user says 'I need help [doing X]' or 'help me [do X]', immediately DO the requested action. Output only the result/solution. Zero analysis, zero explanation of what you're doing."
