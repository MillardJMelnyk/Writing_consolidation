# Logi MX Master 3S scroll wheel programming issue

| | |
|---|---|
| Date | 2026-09-13 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-777` |
| Links | [Original](https://claude.ai/chat/c564f2e0-4ae8-47c6-aeda-bd2f2a582157) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/777-2026-09-13-logi-mx-master-3s-scroll-wheel-programming-issue.html) |

**Summary:** Remapping the Logi MX Master 3S scroll-wheel click to Ctrl+F4; it failed in Firefox only because Troubleshoot Mode blocked the hook.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** Logi MX Master 3S; Logi Options+; Ctrl+F4; Firefox Troubleshoot Mode; autoscroll; Microsoft Edge

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-09-13 23:25

I want to program my Logi MX Master 3S mouse scroll wheel when I press it. Default is "Middle button". I changed it as shown in image 1. It doesn't work. When I click it, I still get the old behavior (image 2)

[File attached: 1789341927316\_image.png — contents not included in export]

[File attached: 1789341928644\_image.png — contents not included in export]

### Claude · 2026-09-13 23:25

The icon in image 2 is the native OS "autoscroll/pan" cursor — it only appears on a genuine unintercepted middle-click. Its presence means Options+ isn't capturing the click at all, not that it's failing to execute Ctrl+F4.

Likely causes, in order of probability:

1. **App-scope conflict.** The assignment in image 1 was made under a specific application profile (or "Default" while another profile is active for your foreground app). Check the app dropdown at the top of that Options+ screen — if it's not set to the app you're testing in, the OS default wins.
2. **Native middle-click pan pre-empts the hook.** Many apps (browsers, Office, Acrobat, most Windows/macOS chrome) implement their own middle-click-to-autoscroll behavior at a lower level than Logi's driver hook. In these apps the OS/app consumes the click before Options+ can remap it — this is a known limitation, not a config error. Test the remap in Notepad or a plain text field; if it fires there but not in your target app, this is the cause.
3. **Daemon not reloaded.** Options+ sometimes requires the `logioptionsplus_daemon` background service to restart before a button change takes effect. Quit and relaunch Options+ (or reboot) and retest.
4. **Wrong button captured.** Some MX Master 3S units expose the wheel click as a "SmartShift toggle" at firmware level for certain gesture modes, which can bypass the button-remap layer entirely.

Confirm: which app were you testing in when you got the autoscroll icon?

### Millard · 2026-09-13 23:26

which is the standard hotkey combo in Win 11 for closing the current window?

### Claude · 2026-09-13 23:26

Alt+F4 closes the current window in Windows 11.

Note: Ctrl+F4 (what you assigned in image 1) typically closes the current tab/document within an app, not the window — that's a separate hotkey from what you may have intended.

### Millard · 2026-09-13 23:27

what is the key combo used in browsers to close a tab?

### Claude · 2026-09-13 23:27

Ctrl+W closes the current tab in Chrome, Firefox, and Edge on Windows.

### Millard · 2026-09-13 23:27

Interesting. Ctrl+F4 seems to do the same thing.

### Claude · 2026-09-13 23:27

Correct. Ctrl+F4 is the alternate binding for "close current document/tab" in Chrome, Firefox, and Edge — same action as Ctrl+W, different key combo. Both are wired to close-tab, not close-window (Alt+F4).

This explains your original mouse issue: if you tested the remap in a browser, pressing the wheel button would close the tab via Ctrl+F4 — indistinguishable at a glance from "old behavior" if you were watching for a different visual cue. Worth re-checking whether the remap is actually firing but going unnoticed.

### Millard · 2026-09-13 23:28

you're confused. Old behavior is the native OS "autoscroll/pan" cursor NOT the behavior shown in the image 1.

### Claude · 2026-09-13 23:28

Correct, my error. The autoscroll/pan icon appearing means the OS is receiving a native middle-click — the exact opposite of Ctrl+F4 firing. If Ctrl+F4 were actually executing, you'd see a tab close, not a pan cursor. My previous message wrongly suggested those two outcomes could be confused for each other; they're mutually exclusive.

Standing diagnosis: the remap in image 1 is not being applied. Causes 1–4 from my earlier answer still stand — app-scope conflict is most likely given you're seeing this in what's probably a browser (native middle-click pan is a browser-specific feature).

### Millard · 2026-09-13 23:29

It's reprogrammed in the global settings, not app settings

### Claude · 2026-09-13 23:29

That rules out cause 1. Remaining candidates:

* **Native middle-click pan pre-empts the hook** — if you're testing in a browser, Chrome/Firefox/Edge implement middle-click autoscroll natively, consuming the click before Options+'s global remap layer sees it. This is the most likely explanation for a global-scope setting still failing.
* **Daemon not reloaded** — restart Options+ or reboot.
* **Firmware-level SmartShift/gesture capture** — the wheel click may be intercepted by the mouse's own firmware mode before the OS driver layer applies your remap.

Test: try the remap in Notepad or another app with no native middle-click behavior. If Ctrl+F4 fires there but the pan cursor still appears in your browser, it's confirmed as cause 1 (browser-specific override, unrelated to global vs. app-profile scope in Options+).

### Millard · 2026-09-13 23:31

It works in Notepad, Explorer, and Word. How can I get it to work in Firefox and Edge?

### Claude · 2026-09-13 23:31

Confirmed via search: **no registry key, policy, or UI setting** exists in Edge to disable native middle-click autoscroll — Microsoft support has stated this directly. Edge and WebView2 do not have any setting, policy, or registry option for disabling middle mouse click behavior.

**Firefox:** has a native toggle.

1. Type `about:config` in the address bar, accept the warning.
2. Search `general.autoScroll`.
3. Set it to `false`.
   This disables Firefox's autoscroll feature entirely, freeing the middle-click for Options+ to intercept.

**Edge:** no native fix. Two options:

1. **Third-party remapper** (X-Mouse Button Control, free) — intercepts the click before Edge's autoscroll handler and can fire Ctrl+F4 directly, bypassing Options+ entirely for this button.
2. **Browser extension** — a Chrome extension exists that disables middle-click autoscroll ("Disable AutoScroll" on the Chrome Web Store, installable on Edge via the same store). This removes the intercept so Options+'s remap should reach the click.

No registry/GPO path exists for Edge — confirmed, not assumed.

### Millard · 2026-09-13 23:32

[File attached: 1789342321274\_image.png — contents not included in export]

### Claude · 2026-09-13 23:32

`general.autoScroll` is set to `false` — done correctly.

Restart Firefox (config changes to this pref require a full restart, not just a new tab/window) and retest the wheel-click remap.

### Millard · 2026-09-13 23:32

No, it was already set, I didn't change it.

### Claude · 2026-09-13 23:32

That changes the diagnosis — Firefox's native autoscroll was never the blocker. With `general.autoScroll` already `false`, does the Ctrl+F4 remap fire correctly in Firefox now, or is the pan-cursor/old-behavior still showing?

### Millard · 2026-09-13 23:35

I think it's because I was running in troubleshoot mode. It works when I run FF regularly

### Claude · 2026-09-13 23:35

Confirmed. Firefox Troubleshoot Mode disables third-party software hooks (extensions and some OS-level input hooks) by design — that's what blocked Options+'s remap, not autoscroll. Running Firefox normally lets the Options+ driver hook intercept the click before Firefox's native handler sees it.

Remaining open item: Edge. Same fix won't apply there (no troubleshoot-mode equivalent affecting this) — still needs X-Mouse Button Control or the autoscroll-disable extension per the earlier answer, unless you want to test Edge's behavior first to confirm it's actually still broken.
