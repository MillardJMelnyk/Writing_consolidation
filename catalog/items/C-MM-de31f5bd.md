# GLM-5.3-Flash overview

| | |
|---|---|
| Date | 2026-08-27 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-de31f5bd` |
| Links | [Original](https://claude.ai/chat/de31f5bd-37c2-4758-9f8e-2b26a5052083) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-08-27_glm-5-3-flash-overview_de31f5bd.html) |

**Summary:** Describes Z.ai's GLM-5.3-Flash model, its pricing and context, and how to use it in VS Code via Kilo Code, Cline or Continue.

**Topics:** AI chatbots and working with Claude > Comparing AI models and chatbots

**Index terms:** GLM-5.3-Flash; Z.ai; open weights; VS Code; Kilo Code; Cline; OpenRouter

[← Catalog home](../README.md)

---

### Millard · 2026-08-27 15:18

GLM-5.3-Flash

Tell me about it

### Claude · 2026-08-27 15:18

GLM-5.3-Flash is Z.ai's cheap native-multimodal model, released August 26, 2026, under an MIT license with open weights.$0.075/M input, $0.25/M output, $0.015/M cache read. 1,048,576-token context, up to 131,072 output tokens. Takes text, images and video in, returns text. Supports function calling and JSON output (no schema enforcement).

Hybrid sparse/linear attention, aimed at coding and long-horizon agent work.It was the stealth "Ox Alpha" model on OpenRouter

, and it's live for GLM Coding Plan users with triple the GLM-5.3 quota.

The bigger sibling, GLM-5.3, is the flagship — text-only, always reasoning, claimed 50% coding gain over GLM-5.2 from post-training alone on the same base model. Vendor benchmarks, unverified.

### Millard · 2026-08-27 15:18

Speak to me like a human being

### Claude · 2026-08-27 15:18

Sure.

It's Z.ai's new cheap model, out yesterday. Dirt cheap — about 7.5 cents per million tokens in, 25 cents out. Huge context, a million tokens. Takes text, images, and video. Open weights, MIT license, so you can run it yourself if you want.

It was the mystery "Ox Alpha" model people were testing on OpenRouter for the past week.

It's built for coding and long agent tasks. Whether it's actually good is still an open question — the benchmark numbers are Z.ai's own.

### Millard · 2026-08-27 15:19

How do I try it on a coding problem?

### Claude · 2026-08-27 15:19

Three easy ways, cheapest first:

**Just chat with it** — go to z.ai and use their web assistant. Free, no setup. Paste your problem, see what you get. This is the right first step if you just want to size it up.

**OpenRouter** — sign up, add a few dollars, get an API key. One endpoint, works with anything that speaks the OpenAI API format. Good if you want to script it or run it against your own test cases.

**Inside a coding tool** — Z.ai has a Coding Plan subscription that plugs into Claude Code, Cline, OpenCode, and Codex. That's the one if you want it working on real files in your project rather than answering questions in a chat box.

For a first look, use the web chat. Give it something you already know the answer to so you can judge it honestly.

### Millard · 2026-08-27 15:21

I use GPT and Claude in VS code. Is there an extension for GLM-5.3-Flash?

### Claude · 2026-08-27 15:21

There's no dedicated GLM extension, but you don't need one — the extensions you'd use are model-agnostic. Pick whichever you like and point it at Z.ai.

Easiest options:

**Kilo Code** or **Cline** — both in the VS Code marketplace, both list Z.ai as a provider with GLM-5.3 and Flash in the model dropdown. Install, paste your API key, pick the model. That's it.

**Continue** — same idea, but you edit a config file instead of clicking a dropdown. Z.ai's API is OpenAI-compatible, so you just set the base URL and model name.

One gotcha worth knowing: if you're on a Coding Plan subscription, the base URL is the coding endpoint — `https://api.z.ai/api/coding/paas/v4` — not the general API one. Mixing them up is the usual first-try failure.

Two ways to pay: a Coding Plan subscription starting around $18/month, or straight pay-as-you-go API credits. For just kicking the tires, buy a few dollars of API credit — no commitment.
