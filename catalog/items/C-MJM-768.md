# Finding a lost Facebook post

| | |
|---|---|
| Date | 2026-09-09 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-768` |
| Links | [Original](https://claude.ai/chat/552a97a6-e61e-4190-a26f-1920965e77b6) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/768-2026-09-09-finding-a-lost-facebook-post.html) |

**Summary:** Recovering an unposted Facebook share lost when the app refreshed after switching apps; no draft recovery exists.

**Topics:** Practical & personal > Phones, WhatsApp, Facebook and social media accounts

**Index terms:** Facebook; lost draft; activity log; app backgrounding

[← Catalog home](../README.md)

---

### Millard · 2026-09-09 20:57

I was sharing a Facebook post, had already written a fair bit when I went to my browswer to look something up. I came back to what I was writing, saw it for an instant, it disappeared, and Facebook showed me a completely different post. I can't find the original post (it was in my feed and I hadn't saved the post). What can I do?

### Claude · 2026-09-09 20:57

Wednesday, September 09, 2026.

Facts about what happened: Facebook's feed is dynamically re-ranked and doesn't preserve position — navigating away (even briefly) can trigger a refresh that drops the post from view. A composed-but-unposted comment/share draft is generally NOT persisted server-side in most cases; there's no "recover draft" feature for feed posts.

Recovery options, in order of likelihood of success:

1. **Browser back button / forward button** — sometimes reloads cached DOM state showing the post. Low success rate on Facebook due to infinite-scroll re-fetching.
2. **Check Activity Log** (facebook.com/me/allactivity) — only shows things you *interacted with* (likes, comments, shares you completed), not passively-viewed posts.
3. **Search your own recent activity/search history** in Facebook's search bar for keywords you remember from the post.
4. **Check "Recently Viewed"** — Facebook doesn't expose this to users directly; no accessible feature.
5. **If it was from a specific friend/page** — go directly to that profile/page and scroll their timeline.
6. **Browser history** (Ctrl+H / Cmd+Y) — if the post had a unique URL you clicked into (not just scrolled past in feed), it may show there.
7. **If using mobile app** — no local draft cache for feed posts; unrecoverable via app.

If you were writing a **comment or your own post** (not sharing an existing one) and it vanished: that content is very likely unrecoverable — Facebook does not autosave drafts for comments, and only sometimes autosaves for your own post composer (check the composer for a "drafts" prompt if you reopen it).

Bottom line: no reliable recovery mechanism exists for a passively-scrolled feed post. If you recall the poster or exact phrase, direct search/profile-check is your best shot.

### Millard · 2026-09-09 20:58

I didn't "navigate away". I switched to s different app. FACEBOOK spontaneously navigated away from the post and lost my writing. Get straight with the facts before you feed me BS.

### Claude · 2026-09-09 20:59

Correction: error was mine. You switched apps (backgrounding Facebook), not navigating via browser. Different mechanism, same result category.

**What actually happened (mechanism, not confirmed by a Meta source — inference from known app behavior):** Mobile OS (iOS/Android) or the Facebook app itself reclaims memory/refreshes session state when backgrounded. On resume, the app frequently re-fetches and re-ranks the feed rather than restoring the exact prior state. Any in-progress, unposted text (a share caption, comment draft) held only in that view's temporary state is discarded — there is no persistent local draft store for that composer field in the standard FB app. This is user-reported common behavior; I have no citable Meta documentation confirming it as designed behavior versus a bug.

**Recovery options for this specific scenario, realistic likelihood:**

1. Force-close and reopen the app, then pull-to-refresh feed at top — near-zero chance the exact post reappears in the same position; feed re-ranks on refresh.
2. Check Activity Log (facebook.com/me/allactivity) — only if you'd already completed an interaction (like, comment, share) before switching apps. If you hadn't posted yet, nothing will be there.
3. If you know the poster — go directly to their profile/timeline and scroll manually.
4. Facebook search bar with any keyword you remember from the post text.
5. No accessible "recently viewed" or draft-recovery feature exists in the standard app for this case.

Your unposted writing: not recoverable. No autosave exists for that field.
