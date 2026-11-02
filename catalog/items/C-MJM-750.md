# Claude login issue in VS Code

| | |
|---|---|
| Date | 2026-08-24 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-750` |
| Links | [Original](https://claude.ai/chat/ca54df77-9951-4286-830b-c0c6eb15208f) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/750-2026-08-24-claude-login-issue-in-vs-code.html) |

**Summary:** Claude login failure in VS Code traced to Cloudflare DNS triggering a 403 challenge; reverting DNS fixed it.

**Topics:** AI chatbots and working with Claude > Claude account, limits and chat management; Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** Claude Code; Visual Studio Code; Cloudflare; DNS; HTTP 403

[← Catalog home](../README.md)

---

### Millard · 2026-08-24 19:10

I can't log in to Claude using VS Code. Never had a problem before. see image

[File attached: 1787598624265\_image.png — contents not included in export]

### Claude · 2026-08-24 19:10

Known issue class, no single confirmed cause. Reported triggers and fixes (as of Aug 2026):

1. **Stale/corrupt OAuth token or config** — most common. Fix: fully quit VS Code, delete cached credentials, retry.
   * macOS/Linux: `rm -rf ~/.claude/` (or wherever `CLAUDE_CONFIG_DIR` points — if you've customized it, that's a separate known bug, see #4)
   * Windows: delete `%USERPROFILE%\.claude\`
2. **Multiple concurrent VS Code windows/extension instances** — refresh tokens are single-use; a second instance racing the first invalidates it, throws 400 next refresh. Fix: close all but one VS Code window with the extension active, re-login.
3. **Network path to claude.ai blocked or intercepted** — corporate proxy, VPN, or Cloudflare challenge blocking the OAuth callback. Test: `curl -sSI https://claude.ai/` — if you get a 403 with `cf-mitigated: challenge`, that's your problem, not the extension.
4. **Non-default `CLAUDE_CONFIG_DIR`** — open bug specifically in the extension (works fine via CLI `/login`). If you've set this env var, unset it and retest.

Fastest diagnostic: run `claude` in a terminal (not the VS Code panel) and try `/login` there. If terminal login works and only the panel fails, it's #2 or #4. If both fail, it's #1 or #3.

No official patched-version fix confirmed yet — these are open GitHub issues as of this month.

### Millard · 2026-08-24 19:17

where do I execute `curl -sSI https://claude.ai/`

### Claude · 2026-08-24 19:17

In a terminal — any shell will do:

* **VS Code**: Terminal → New Terminal (or `` Ctrl+` ``)
* **macOS**: Terminal.app
* **Linux**: your terminal emulator
* **Windows**: PowerShell or Command Prompt (if using WSL, run it inside the WSL shell, not native Windows, since that's where Claude Code actually runs)

Run it as-is, no substitutions needed. Look at the response headers: a `403` with `cf-mitigated: challenge` confirms network/Cloudflare blocking; a normal `200` rules that out.

### Millard · 2026-08-24 19:18

C:\WINDOWS\System32>curl -sSI https://claude.ai/
HTTP/1.1 403 Forbidden
Date: Mon, 24 Aug 2026 19:18:06 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 5357
Connection: close
Accept-Ch: Sec-CH-UA-Bitness, Sec-CH-UA-Arch, Sec-CH-UA-Full-Version, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA-Platform-Version, Sec-CH-UA-Full-Version-List, Sec-CH-UA-Platform, Sec-CH-UA, UA-Bitness, UA-Arch, UA-Full-Version, UA-Mobile, UA-Model, UA-Platform-Version, UA-Platform, UA
Cf-Mitigated: challenge
Content-Security-Policy: default-src 'none'; script-src 'nonce-RPYZvFQBSlnjX6UDdn2RKx' 'unsafe-eval' https://challenges.cloudflare.com; script-src-attr 'none'; style-src 'unsafe-inline'; img-src 'self' https://challenges.cloudflare.com; connect-src 'self' https://challenges.cloudflare.com; frame-src 'self' https://challenges.cloudflare.com blob:; child-src 'self' https://challenges.cloudflare.com blob:; worker-src blob:; form-action http: https:; base-uri 'self'
Server: cloudflare
Critical-Ch: Sec-CH-UA-Bitness, Sec-CH-UA-Arch, Sec-CH-UA-Full-Version, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA-Platform-Version, Sec-CH-UA-Full-Version-List, Sec-CH-UA-Platform, Sec-CH-UA, UA-Bitness, UA-Arch, UA-Full-Version, UA-Mobile, UA-Model, UA-Platform-Version, UA-Platform, UA
Cross-Origin-Embedder-Policy: require-corp
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Resource-Policy: same-origin
Origin-Agent-Cluster: ?1
Permissions-Policy: accelerometer=(),camera=(),clipboard-read=(),clipboard-write=(),geolocation=(),gyroscope=(),hid=(),magnetometer=(),microphone=(),payment=(),publickey-credentials-get=(),screen-wake-lock=(),serial=(),sync-xhr=(),usb=(),xr-spatial-tracking=\*
Referrer-Policy: same-origin
Server-Timing: chlray;desc="a304b373aba147af"
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
set-cookie: \_\_cf\_bm=CebftgyG43iYOkobZ.LSiwO2rsPPWIitV.bVkLbkGsw-1787599086.6709063-1.0.1.1-kZgglvhkntiDqKdfpCMyPMeI9prTwUCsxeR6GHxLzDS7yME1TliCXSjNpenRzGE4afj8fyJGmidyDGnyrgb1ciSHsp21UkGDqkJFofA0v\_H9qhmw2CT0M2MNb9Z8C1lK; HttpOnly; SameSite=None; Secure; Path=/; Domain=claude.ai; Expires=Mon, 24 Aug 2026 19:48:06 GMT
CF-RAY: a304b373aba147af-DFW
alt-svc: h3=":443"; ma=86400
C:\WINDOWS\System32>

### Claude · 2026-08-24 19:18

Confirmed: `Cf-Mitigated: challenge`. Network path is blocked, not the extension.

This is a Cloudflare JS challenge — it's triggered by something in your request path that looks bot-like to Cloudflare (curl's TLS/HTTP fingerprint alone can trigger this even for legitimate users, or an actual network intermediary is involved). Not something you fix by retrying the extension.

Checks, in order:

1. **VPN/proxy active?** Disable and retest with the same curl command. Datacenter/VPN IP ranges get challenged disproportionately.
2. **Corporate/antivirus TLS inspection?** If this is a work machine, check for Zscaler, Netskope, Fortinet, or similar SSL-inspecting software — these rewrite TLS handshakes and commonly trigger Cloudflare bot mitigation.
3. **Does it work in an actual browser right now?** Open `https://claude.ai/` in Chrome/Edge and see if you get challenged there too, or if it loads normally. If the browser works fine but curl doesn't, the issue may be curl-specific fingerprinting rather than your whole network path — in which case the VS Code extension's underlying HTTP client could be hitting the same wall the browser avoids.

Report back which of these applies — that determines whether the fix is "disable VPN," "get IT to whitelist claude.ai," or something else.

### Millard · 2026-08-24 19:19

I switched DNS to cloudflare to resolve video streaming issues. I just reset it to dynamic.

### Claude · 2026-08-24 19:19

Good move — that's a plausible cause; Cloudflare's own DNS resolving Cloudflare-fronted domains can produce odd routing/fingerprint interactions. Retest:

```
curl -sSI https://claude.ai/
```

If it returns `200` instead of `403`, retry `/login` in VS Code. Report the result either way.

### Millard · 2026-08-24 19:22

I'm in

### Claude · 2026-08-24 19:22

Confirmed fixed. DNS was the cause.
