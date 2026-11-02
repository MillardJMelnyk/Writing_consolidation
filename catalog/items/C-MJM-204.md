# URL Parameter Syntax

| | |
|---|---|
| Date | 2025-08-22 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-204` |
| Links | [Original](https://claude.ai/chat/dbb73b46-8e28-4f9f-811d-42c3e8d04ab9) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/204-2025-08-22-url-parameter-syntax.html) |

**Summary:** Explains that multiple URL query parameters are separated by ampersands after the first question mark, using a Grok URL example.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** URL query string; ampersand; Grok; URL parameter

[← Catalog home](../README.md)

---

### Millard · 2025-08-22 14:58

what's the correct syntax for multiple URL parameters. For example, what should replace the second "?" mark in the following:
https://grok.com/?ref=aiappvn.com?q=

### Claude · 2025-08-22 14:59

The correct syntax for multiple URL parameters uses `&` (ampersand) to separate parameters after the first `?` (question mark).

Your example should be:

```
https://grok.com/?ref=aiappvn.com&q=
```

The general pattern is:

* `?` marks the beginning of the query string
* `&` separates each additional parameter
* Each parameter follows the format `key=value`

So for multiple parameters, it would look like:

```
https://example.com/?param1=value1&param2=value2&param3=value3
```

In your specific example:

* `ref=aiappvn.com` is the first parameter
* `q=` is the second parameter (with an empty value)
