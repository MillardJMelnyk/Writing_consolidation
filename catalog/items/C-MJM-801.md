# Google Drive sharing link requires account login

| | |
|---|---|
| Date | 2026-10-03 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-801` |
| Links | [Original](https://claude.ai/chat/a8169516-b4db-42c6-aa24-9118807cee78) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/801-2026-10-03-google-drive-sharing-link-requires-account-login.html) |

**Summary:** Google Drive public link demanding login, resetting an Edge profile, and fbi.gov apparently blocking visitors from Mexico but not via US VPN.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** Google Drive; sharing link; fbi.gov; geoblocking; VPN; Telmex; AT&T Mexico; Microsoft Edge

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-10-03 14:32

I created a sharing link to a video on Google Drive.It says anyone with the link can see the video, but when I use the link in a browser that isn't logged into Google, it requires me to choose a Google account before I can see the video. This is unacceptable.

### Claude · 2026-10-03 14:33

Saturday, October 3, 2026, [time not available to me] CST

"Anyone with the link" does not require a Google login, so the setting is not what you think it is, or the link is not the one you set. The causes, in rough order of likelihood:

1. **General access is org-scoped.** On a Workspace account, the dropdown can show your organization's name instead of "Anyone with the link." That forces a Google sign-in. Fix: Share → General access → select "Anyone with the link" → role Viewer.
2. **Admin policy blocks external sharing.** If "Anyone" is greyed out or missing, the Workspace admin (or a Shared Drive setting) has disabled public link sharing. Only the admin can change it (Admin console → Apps → Google Workspace → Drive and Docs → Sharing settings).
3. **Wrong URL copied.** A link taken from the address bar can contain `/u/0/` or `authuser=` parameters that trigger the account chooser. Use the Share dialog's "Copy link" button, or reduce it to `https://drive.google.com/file/d/FILE_ID/view`.
4. **Wrong item shared.** The link points to a folder or a different file than the one you changed.

Test in an incognito window after each change.

If #2 applies, the Drive workaround is to host the video in a personal (non-Workspace) account, or upload it as an unlisted YouTube video.

Which account type is this: personal Gmail or Workspace? And what does the General access dropdown currently display?

### Millard · 2026-10-03 14:36

images show the sequence.
DO NOT FUCKING GUESS. RESEARCH AND TELL ME HOW TO MAKE THIS WORK.

[File attached: 1791038164105\_image.png — contents not included in export]

[File attached: 1791038166632\_image.png — contents not included in export]

[File attached: 1791038169308\_image.png — contents not included in export]

[File attached: 1791038171610\_image.png — contents not included in export]

### Claude · 2026-10-03 14:36

Your screenshots rule out my earlier list. The account is personal Gmail, General access reads "Anyone with the link" with Viewer, and the URL is the standard `/file/d/ID/view?usp=sharing` form. Those were guesses on my part, and they were wrong for your case.

**Verified by sources:**

* Anyone with the link: anyone who has the link can use your file, without signing in to their Google Account. Your settings match this, so the link is not what requires sign-in.
* One guide on opening Drive links says to open the file link in a private or incognito browser window to get around account issues.

**Not found:** no source I located documents this exact behavior, so I can't name the cause with evidence.

**Observed in your screenshots:**

* The chooser lists 4 accounts, each labeled "Signed out."
* Your test browser (Edge) is retaining Google account state even though you are logged out. It is not a clean session.
* Screenshot 3 shows the Drive URL in the address bar but the Google homepage in the page body, which suggests a redirect was already in progress.

**Test to isolate it (2 steps):**

1. Open an **InPrivate** window in Edge and paste the link. Extensions are off by default there, and no stored Google account state carries over.
2. If it still shows the chooser, test on a phone over mobile data with no Google app signed in.

**Reading the results:**

* InPrivate works: the file and link are fine. The cause is in your regular Edge profile (stored Google state, cookie or tracking settings, or an extension). Anyone without that state opens it normally.
* Fails in InPrivate and on the phone: the problem is on Google's side for this specific file, and I need that result to go further.

Report the result of each test.

### Millard · 2026-10-03 14:38

This is probably related to another problem I'm having with Edge, which no one seems to know how to fix, which is that every time I close edge or put my machine to sleep, all of the Google accounts I had logged into get logged out, and I have to log back in the next time I start edge

### Claude · 2026-10-03 14:38

Connected, but only partly confirmed. I found no source covering the sleep case specifically. The closing-Edge case has documented causes, and your cookie-based sign-in loss and the "Signed out" chooser entries are both consistent with cookies being cleared. That link is my deduction, not something a source states.

**Documented causes of Google sign-in loss when Edge closes (check in this order):**

1. **Clear-on-exit setting.** Go to `edge://settings/clearBrowserData` → "Choose what to clear every time you close the browser." If "Cookies and other site data" is on, turn it off. Microsoft's Zoho-cited guidance and an Edge how-to both name this setting.
2. **Cookie exceptions.** Go to `edge://settings/content/cookies` and check for "Clear on exit" entries or blocked entries covering `google.com`, `accounts.google.com`, `drive.google.com`.
3. **Cookie-clearing extension.** Your toolbar shows several extensions. Disable all of them, or test in a fresh profile, and see whether sign-in survives a close and reopen. One support article names cookie-clearing extensions as a cause.
4. **Policy.** Open `edge://policy`. A policy such as `CookiesSessionOnlyForUrls` (documented by Microsoft staff) forces cookies to be cleared when the window closes. This applies even on a personal machine if software set it.
5. **Security or cleaner software.** Any tool that wipes browser data on exit or shutdown (the how-to lists this as a check item).

**Procedure to isolate:**

1. Create a new Edge profile with no extensions and sign in to Google.
2. Close Edge completely and reopen.
3. If it stays signed in, the cause is in your main profile (items 1–3). If it logs out, the cause is machine-level (items 4–5).
4. Repeat with a sleep cycle to test the sleep case separately.

Report what `edge://settings/clearBrowserData` shows under the on-exit list and what `edge://policy` lists.

### Millard · 2026-10-03 14:39

I ruled out all of those causes. This does not happen in Firefox, so it's not a machine-level issue. I'm not interested in troubleshooting. How can I simply reset the profile

### Claude · 2026-10-03 14:39

Two methods, in order of impact.

**1. Soft reset (keeps bookmarks, history, passwords)**

* Open `edge://settings/resetProfileSettings` and click **Reset**.
* Resets the default search engine, new tab page, and site permissions, and clears temporary data.
* Sources say this reset covers only limited data. If the cause is corrupted profile data, they say a full reset is needed.

**2. Full profile reset (new profile, all local data gone)**

1. Close Edge completely, including background processes (Task Manager).
2. Press Win+R, enter `%LOCALAPPDATA%\Microsoft\Edge\User Data`.
3. Rename the `Default` folder to `Default-Backup`.
4. Open Edge. It creates a fresh profile and runs first-run setup.
5. To undo, delete the new `Default` and rename the backup back.

**Before the full reset:**

* Bookmarks, passwords, and extensions are not carried over. Export bookmarks and passwords first (`edge://settings/profiles`, or `edge://favorites` → Export).
* If Edge sync is on, signing in to your Microsoft account in the new profile re-syncs your old data, and may bring back the setting causing the problem. Leave sync off for settings, or skip signing in until you've tested whether Google stays signed in after closing Edge.

Test after the reset: sign in to Google, close Edge fully, reopen.

### Millard · 2026-10-03 14:41

Okay, I'll do that later. What I want you to do right now is check to see you can access the video at https://drive.google.com/file/d/1NUJF\_s8dWTX6YvWSjkbLm05DgZuuAGhn/view?usp=sharing

### Claude · 2026-10-03 14:41

**Result: the page loads without authentication. Video playback is not verified.**

* My fetch was anonymous (no Google login). It returned the file's page with the title "22nd Battalion of the Carmeli Brigade before attacking Netzarim, Gaza in April 2024, singing 'May your village burn' with CAPTION.mp4 - Google Drive."
* There was no redirect: the final URL equals the requested URL, and neither an account chooser nor `accounts.google.com` came back as the destination.
* The only sign-in element in the returned content is a "Sign in" link, which is the header link on the Drive viewer page. It is not a gate.

**What this shows:** Google serves this file to a client with no Google session, so the link is public as configured. The account chooser you saw comes from your Edge profile's stored Google state, not from the file's sharing settings. This is consistent with the sign-in loss problem in Edge, though a fetch result alone does not prove that link.

**What I could not check:** my tool returns page HTML only. It cannot play the video or confirm that the stream works, so playback for a logged-out visitor is untested. A phone on mobile data, with no Google app signed in, is the clean test.

### Millard · 2026-10-03 15:08

fbi.gov is rejecting both Firefox and Edge from accessing it.

### Claude · 2026-10-03 15:08

**fbi.gov is up.** My anonymous fetch on Oct 3, 2026 returned the full homepage (last modified Oct 2, 2026) with no block. So the rejection is specific to your connection or client, not a site outage.

**Unverified:** I have no source showing what error you get or that fbi.gov uses Akamai. The documented pattern for "Access Denied" in several browsers at once, with a reference number and `errors.edgesuite.net`, is a CDN block on your public IP or request profile. Firefox and Edge failing together matches this, since the shared factor is your network, not either browser's profile.

**Documented tests, in order:**

1. Load fbi.gov from a phone on mobile data. A success there points to your IP being flagged.
2. Turn off any VPN or proxy, then retry.
3. Check your public IP at `https://www.akamai.com/us/en/clientrep-lookup`. Community answers say high reputation scores trigger these blocks, and that they clear in 10–30 minutes to a few hours after the score drops.
4. If the IP is flagged, get a new one. One user reported that changing the router's MAC address by one character produced a new ISP-assigned IP. This is anecdotal, not an Akamai or ISP-documented procedure.

I need the exact text on the rejection page, including any "Reference #" line. What does it say?

### Millard · 2026-10-03 15:08

I'm in Mexico, is that why?

### Claude · 2026-10-03 15:08

**Possibly, but no source shows Mexico is blocked.**

* One Wikimedia Commons file description (Aug 2024, user-uploaded, not an official source) says fbi.gov shows "The request has been blocked" for free or datacenter proxy IPs, and from Iran and China. Mexico is not mentioned.
* I found no documentation of fbi.gov geo-blocking Mexico.
* A separate source says reports are mixed on whether the FBI's records-request portal (edo.cjis.gov, a different site) is reachable from foreign IPs. That is not evidence about fbi.gov.
* From my side, fbi.gov loaded without a block.

**What discriminates country from IP:** load fbi.gov from your phone on mobile data. Both are Mexican connections, so:

* Works on mobile data, fails on home internet: your home IP is flagged, not the country.
* Fails on both: a country-level block is plausible, but still unconfirmed.

**The error wording matters.** "Access Denied" with a Reference # and "The request has been blocked" are different messages and imply different blockers. I can't tell which you're getting without the text. What does the page say, word for word?

### Millard · 2026-10-03 15:09

can you access https://www.fbi.gov/news/press-releases/fbi-releases-2024-reported-crimes-in-the-nation-statistics?

### Claude · 2026-10-03 15:09

**Yes. The page loaded in full.**

* Oct 3, 2026: my fetch returned "FBI Releases 2024 Reported Crimes in the Nation Statistics," dated August 5, 2025, with no block or challenge page.
* This is a second fbi.gov URL that loads for me, so the site is serving content from my connection.
* It tells nothing new about your block. It still points to your IP or connection, not to the site.

Your result is still undetermined. I still need two things from you:

1. What the rejection page says, word for word.
2. Whether fbi.gov loads on your phone over mobile data.

### Millard · 2026-10-03 15:18

I connected via VPN (Los Angeles) and both URLs loaded just fine.

[File attached: 1791040645125\_image.png — contents not included in export]

### Claude · 2026-10-03 15:18

**The block is on your Mexican connection, not your browsers or machine.** The VPN result confirms it: same browsers, same machine, different exit IP, and both pages loaded.

**Correction:** I framed this as an Akamai-style "Access Denied" block. Your screenshot shows a different message, "We're sorry... The request has been blocked." That text matches the one a Wikimedia Commons file description (user-uploaded, not official) documents for fbi.gov. It lists free or datacenter proxy IPs, plus Iran and China, as triggers. Mexico is not named there.

**Still undetermined:** whether the cause is Mexico as a country or your specific IP or ISP range. The VPN test can't separate them. One test can: load fbi.gov on your phone over mobile data in Mexico.

* Loads: your home IP or ISP range is flagged.
* Blocked: a country-level or Mexico-wide block is plausible, though unconfirmed.

**Workaround:** keep using the VPN for fbi.gov. A US exit that isn't on a datacenter blocklist works, as your Los Angeles exit shows.

### Millard · 2026-10-03 15:19

I get the same we're sorry page on my phone whether I try to connect via ISP (Telmex) or mobile data (AT&T)

### Claude · 2026-10-03 15:19

**Country-level block is now the best-supported explanation.** Two unrelated Mexican networks (Telmex fixed broadband and AT&T Mexico mobile) get the same block page. A single flagged IP or ISP range would not hit both. Your US VPN exit loads fine, which fits geography being the deciding variable.

**What this is and isn't:**

* Evidence: two independent Mexican networks blocked, one US exit allowed. That is observational, not an official statement from the FBI.
* No source I found documents Mexico on fbi.gov's block list. The only documented non-proxy examples are Iran and China (Wikimedia Commons, Aug 2024, user-uploaded). Mexico being blocked is therefore undocumented but now empirically supported.
* Not tested: a third Mexican network, or a non-US, non-Mexican VPN exit. Neither is needed for the practical answer.

**Practical result:** you can't fix this on your side without a US exit. Keep using the VPN (Los Angeles works) for fbi.gov. Use a residential or standard commercial VPN exit, because the same documentation says datacenter and free proxy IPs get blocked too.
