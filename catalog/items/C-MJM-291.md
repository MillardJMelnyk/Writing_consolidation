# Shortcut troubleshooting

| | |
|---|---|
| Date | 2025-10-03 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-291` |
| Links | [Original](https://claude.ai/chat/939e1f6f-1ea1-4ea6-b202-6a533d11cdf5) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/291-2025-10-03-shortcut-troubleshooting.html) |

**Summary:** A claude.ai URL shortcut that pre-filled Millard's conversation rules through the ?q= parameter stopped working; Claude lists alternatives.

**Topics:** AI chatbots and working with Claude > Claude account, limits and chat management; AI chatbots and working with Claude > Communication protocols and ground rules

**Index terms:** URL parameter; browser shortcut; custom instructions; Claude Projects

[← Catalog home](../README.md)

---

### Millard · 2025-10-03 20:20

My shortcut to you including terms for the conversation doesn't seem to be working anymore.

### Claude · 2025-10-03 20:20

I'd be happy to help troubleshoot your shortcut issue! To better understand what's happening, could you tell me:

1. What platform are you using the shortcut on? (iOS, Mac, etc.)
2. What was the shortcut supposed to do? (For example, was it meant to start conversations with specific instructions or context?)
3. What's happening now instead? (Does it fail to run, or does it run but the terms/instructions aren't being included?)

If you were using a shortcut that included custom instructions or system prompts at the beginning of conversations, it's worth noting that I don't have visibility into whether those are being received on my end - I just see the conversation as it appears. But I can definitely help you figure out what might have changed and suggest alternatives!

### Millard · 2025-10-03 20:20

Here is the shortcut. I contains conversation parameters so that I don't have to type them in every time
https://claude.ai/new?q=Be%20extremely%20curt%20and%20objective,%20NO%20BLATHER%20(unsolicited%20analysis).%20Facts%20only%E2%80%94no%20inferences%20unless%20requested.%20Quantify%20everything%20(ranges,%20dates,%20counts).%20No%20euphemisms%20or%20reputational%20softening.%20Expose%20all%20assumptions%20and%20weak%20points.%20Time-stamp%20changeable%20information%20and%20verify%20recency.%20Ask%20for%20clarification%20if%20uncertain.%20Steelman/counter-steelman%20briefly%20when%20relevant.%20Assume%20I%27m%20wrong%20and%20work%20backwards%E2%80%94attack%20this%20idea%20rigorously,%20find%20every%20flaw,%20don%27t%20soften%20language.%20When%20I%20say%20%27I%20need%20help%20[doing%20X]%27%20or%20%27help%20me%20[do%20X]%27,%20immediately%20DO%20the%20requested%20action.%20Output%20only%20the%20result/solution.%20Zero%20analysis,%20zero%20explanation%20of%20what%20you%27re%20doing.%20BE%20AS%20BRIEF%20AND%20TO%20THE%20POINT%20AS%20CONCEIVABLY%20POSSIBLE.

### Claude · 2025-10-03 20:21

The URL parameter approach likely stopped working due to changes in how Claude.ai handles URL parameters for new conversations.

**Current limitations:**

* URL-based custom instructions aren't officially supported by Claude.ai
* The `?q=` parameter may have been deprecated or changed
* No documented API for passing conversation parameters via URL

**Alternatives:**

1. **Custom Projects** (if available in your plan): Create a project with custom instructions that persist across conversations
2. **Saved prompt**: Keep your instructions in a text file/note app, paste at conversation start
3. **Browser extension**: Create/use an extension to auto-inject text into new Claude conversations
4. **Keyboard shortcuts**: Use OS-level text expansion (TextExpander, Alfred snippets, etc.) to insert instructions quickly

Test if Projects feature is available: Check your Claude.ai sidebar for "Projects" option. If present, this is the best native solution.
