# Facebook notifications suddenly stopped

| | |
|---|---|
| Date | 2026-07-19 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-712` |
| Links | [Original](https://claude.ai/chat/8a8c2674-8cac-4345-b7d0-17ac24f7a037) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/712-2026-07-19-facebook-notifications-suddenly-stopped.html) |

**Summary:** Whether stopped Facebook notifications mean account suppression, and where account status and enforcement notices are found for personal profiles.

**Topics:** Practical & personal > Phones, WhatsApp, Facebook and social media accounts; US empire, politics and current events > Free speech and censorship

**Index terms:** Facebook; notification; Meta; account status; shadowban; Accounts Center

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-07-19 16:09

It's been weeks now. I used to get notifications of posts and mentions on Facebook, but they quite abruptly stopped and since then I get basically nothing with rare exceptions. Have I been sidelined somehow?

### Claude · 2026-07-19 16:09

No verifiable Facebook-side notification-suppression event surfaces in current reporting (search as of 2026-07-19) — no Meta announcement, no widespread outage report matching "notifications stopped for weeks."

Given that, "sidelined" (deliberate suppression targeting you specifically) is not empirically supported — Meta doesn't disclose individual-account throttling, and there's no public record to confirm or rule it out. Known, verifiable causes, not mutually exclusive:

1. **Notification settings drift** — app/OS updates periodically reset per-category notification toggles (posts, mentions, comments) without alerting the user. Check Settings → Notifications on both the FB app and OS-level app permissions.
2. **OS-level throttling** — iOS/Android battery optimization or "background app refresh" getting disabled (often silently, after an OS update) kills push delivery while the app itself works fine when opened.
3. **Engagement-based algorithmic ranking** (not targeting, general mechanism) — Meta's feed/notification systems weight delivery by predicted relevance/engagement; a drop in your own engagement (fewer opens, fewer reactions) lowers predicted relevance and reduces notification volume. This is a systemic mechanism, not evidence of individual sidelining.
4. **Account restriction/reduced distribution** — Meta does apply reduced-distribution states for policy-violation flags, but these usually come with an in-app notice under Account Status; check that page directly rather than inferring from notification volume alone.

No source-verifiable way to distinguish these from where I sit — you'd need to check: Settings → Notifications (app), OS notification permissions, and Account Status page. Those three checks would resolve most of the ambiguity empirically.

### Millard · 2026-07-19 16:11

#2 is ridiculous -- this is FB account specific, not device specific.
#3 -- something clearly changed.
what's the link to the account status page?

### Claude · 2026-07-19 16:11

facebook.com/support/dashboard/ (also reachable via Settings & Privacy → Account Status, or Meta Business Suite if you manage a Page).

Note: it surfaces content-policy restrictions (reduced distribution, strikes). It does **not** report engagement-based notification throttling (#3) — that mechanism isn't disclosed anywhere in-app. If Account Status shows nothing, #3 remains unfalsifiable from your side — Meta doesn't expose per-account relevance/delivery scores.

### Millard · 2026-07-19 16:13

no such page as facebook.com/support/dashboard/
I'm here (image), where do I go?

[File attached: 1784477586069\_image.png — contents not included in export]

### Claude · 2026-07-19 16:13

This menu doesn't show it because **Account Status is a Page/Professional-account feature, not a personal-profile feature** — it doesn't exist for standard personal accounts. That's a correction to my prior answer, not a navigation issue.

For a personal profile, the closest equivalents in what you're showing:

* **Accounts Center → Personal details / Account settings** — may show any restriction notices
* **Support Inbox**: facebook.com/support — shows any policy/enforcement notices Meta has sent you directly
* **Notifications** (visible in your list) — confirms whether the setting itself is toggled off, addressing the account-vs-device distinction you raised for #2

If you have a linked Page, Account Status exists there (Meta Business Suite → that Page → Account Status/Quality) — but it won't reflect your personal profile's notification behavior.
