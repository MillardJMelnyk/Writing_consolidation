# Disabling Yandex human verification

| | |
|---|---|
| Date | 2026-09-11 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-0d5331eb` |
| Links | [Original](https://claude.ai/chat/0d5331eb-b65c-47aa-8340-b3700adb6aa8) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-09-11_disabling-yandex-human-verification_0d5331eb.html) |

**Summary:** Stopping Yandex's repeated human-verification checks in Firefox by adjusting cookies, JavaScript and Enhanced Tracking Protection for the site.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** Yandex; CAPTCHA; Firefox Enhanced Tracking Protection; browser fingerprinting; cookie

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-09-11 20:06

how do I get yandex to stop checking if I'm human?

### Claude · 2026-09-11 20:06

You mostly can't — it's triggered by your IP and browser fingerprint, so the fix is removing the things that flag you: turn off VPN/proxy, allow cookies and JavaScript for yandex domains, drop aggressive anti-fingerprint extensions, and use a normal browser profile rather than incognito.

### Millard · 2026-09-11 20:07

how do I check cookies and javascript for yandex?

### Claude · 2026-09-11 20:07

In Chrome: Settings → Privacy and security → Third-party cookies (allow, or add `[*.]yandex.com` under "Allowed to use third-party cookies"), then Settings → Privacy and security → Site settings → JavaScript → confirm Allowed and that yandex isn't in the blocked list.

### Millard · 2026-09-11 20:07

this is firefox

### Claude · 2026-09-11 20:07

Cookies: click the shield icon left of the address bar while on yandex.com and turn Enhanced Tracking Protection off for that site; also Settings → Privacy & Security → Cookies and Site Data → Manage Exceptions → add `https://yandex.com` as Allow.

JavaScript: Firefox has no UI toggle — it's on unless you set `javascript.enabled` to false in `about:config` or an extension (NoScript, uBlock scripting) is blocking it.

### Millard · 2026-09-11 20:08

it shows that enhanced tracking is on

### Claude · 2026-09-11 20:08

Click the shield, then flip the toggle at the top of the panel to off — that's the per-site switch for the page you're on, and it reloads yandex with protection disabled.
