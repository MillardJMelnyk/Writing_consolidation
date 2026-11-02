# Everything app PNG preview issue

| | |
|---|---|
| Date | 2026-10-26 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-819` |
| Links | [Original](https://claude.ai/chat/918a1133-9d17-4991-91ca-6df0610fbc5b) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/819-2026-10-26-everything-app-png-preview-issue.html) |

**Summary:** Fixing missing PNG thumbnails in the Everything search app, then Millard's passage calling medical-science followers cultists and a psychopath empathy-switch study.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; COVID, vaccines and medical fraud > VaXXX cultists and pandemic denial; Cultism and psychosis > Institutional and national cultism; Psychopathy, narcissism and the mind > Empathy, perspective-taking and ego boundaries; Psychopathy, narcissism and the mind > Psychopaths in power

**Index terms:** Everything search; thumbnail; shell_item_image_factory; medical science; cultism; psychopathy; empathy switch; BBC News

[← Catalog home](../README.md)

---

### Millard · 2026-10-26 17:22

[image attached — not included in export]

I'm having trouble with the Everything app. It regularly fails to render icons/previews for.png files. Windows Explorer has no trouble with the same files.

[File attached: 1793035247119\_image.png — contents not included in export]

### Claude · 2026-10-26 17:23

Monday, October 26, 2026 (time and timezone unavailable)

Everything doesn't make its own thumbnails; it asks the Windows thumbnail handler associated with the file type, through IShellItemImageFactory or IExtractImage. That is the same handler Explorer uses, so the PNGs are Highly unlikely to be the problem. Your screenshot shows 2 of 12 PNGs rendering, which also makes Everything's global thumbnail on/off settings Highly unlikely as the cause.

Three checks will tell you which cause applies:

1. **Help → About Everything.** Check whether the version line ends in (x86) or (x64). When a user reported Everything thumbnails not matching Explorer's, the first response was to ask whether they had tried the x64 build. If yours says x86, that cause is Likely.
2. **Task Manager → Details tab.** Right-click any column header, choose **Select columns**, tick **Elevated**, and check Everything.exe. The developer's guidance is to make sure Everything is installed correctly and running as a standard user. If Elevated shows Yes, that cause is Likely.
3. **Does the same file fail every time, or only sometimes?** One user found that after an Explorer crash, Everything stopped showing thumbnails while Explorer still did, restarting Everything didn't help, and only a reboot fixed it. If your failures come and go and a reboot clears them, that cause is Likely.

If all three come back clean (x64, not elevated, consistent failures), none of these causes fits.

### Millard · 2026-10-26 17:23

If I open one of the files missing, a preview, and then close it, the preview appears in everything afterwards

### Claude · 2026-10-26 17:24

That's diagnostic: Everything can show a thumbnail once Windows has one cached, but it fails when it has to make one itself. Opening the file Likely got Windows to make and cache the thumbnail, and Everything then picked up the cached copy.

This narrows things to checks 1 and 2 from before, x86 build or running elevated, since both are about Everything's own process making thumbnails. Check 3 (the post-Explorer-crash state that only a reboot clears) is now Unlikely, because your failures are per-file and opening the file clears them.

One more check: open the folder in Explorer at Large icons, then go back to Everything. Do the missing previews appear without opening the files? If not, Explorer is caching a different thumbnail size than the one Everything asks for.

### Millard · 2026-10-26 17:26

[image attached — not included in export]

[image attached — not included in export]

1. x64
2. You're hallucinating again
3. I did the one more check, but it didn't help

[File attached: 1793035559257\_image.png — contents not included in export]

[File attached: 1793035564438\_image.png — contents not included in export]

### Claude · 2026-10-26 17:26

On item 2, I left out a step. The **Elevated** column is further down that same list; you have to scroll the Select columns box to reach it. Tick it, click **OK**, and check what it says for Everything.exe.

Item 3 failing rules out a thumbnail-size mismatch between Explorer and Everything as the cause (Likely).

### Millard · 2026-10-26 17:29

[image attached — not included in export]

[image attached — not included in export]

Right, you are, my bad .
As you can see, there's only one window open for Everything, but two lines listed in Task Manager Details, one elevated, one not

[File attached: 1793035695439\_image.png — contents not included in export]

[File attached: 1793035696825\_image.png — contents not included in export]

### Claude · 2026-10-26 17:29

That's normal. The SYSTEM, elevated copy is the Everything Service, which indexes your drives on behalf of the window and doesn't make thumbnails (Highly likely). To confirm, add the **Command line** column the same way; the service's line ends in `-svc`. The copy under Millard (Elevated: No) is the window making thumbnails, so check 2 is clean.

All three checks are now clean, so the next step is the developer's own fix for this symptom. Everything gets thumbnails one of two ways; turning off the first one forces it to use the other:

1. **Tools → Options → Advanced** (left side).
2. In **Show settings containing**, type `shell`.
3. Select **shell\_item\_image\_factory** and set it to **false**.
4. Click **OK**, then restart Everything and look at a folder you haven't opened files from.

If nothing changes, set it back to **true**. Then search `extract`, set **extract\_image** to **false**, and test again.

The **Advanced** tab only exists in Everything 1.5. If you don't see it, tell me the version number under Help → About Everything.

### Millard · 2026-10-26 17:30

[image attached — not included in export]

[File attached: 1793035829631\_image.png — contents not included in export]

### Claude · 2026-10-26 17:30

That's 1.5, so the **Advanced** tab is there; go ahead with the **shell\_item\_image\_factory** steps.

### Millard · 2026-10-26 17:35

Setting shell\_item\_image\_factory to false fixed it . why ?

### Claude · 2026-10-26 17:35

Everything has two ways to ask Windows for a thumbnail. The one you turned off goes through Windows' thumbnail cache. In your setup it returned thumbnails already in the cache but handed back the plain file icon instead of making new ones. That's why opening a file, which put its thumbnail in the cache, made it show up (Likely).

The other way, which Everything now uses, asks the PNG handler to make the thumbnail directly, so the cache no longer matters.

Why the first way gave up instead of making the thumbnail is something only voidtools can answer. It depends on exactly how Everything makes that request, and that isn't visible from outside. support@voidtools.com is the place to ask.

### Millard · 2026-10-26 17:54

A lot of people say that you “medical science” groupies are stupid.
I don't agree.
You're not stupid—you're addicted.
You're cultists.
Your minds are compartmentalized, and whenever you encounter a situation or a topic that belongs to one of your “I'm a good little citizen-codependent-cultist” boxes, you immediately lose the power to think, feel, and behave as a fully human adult.
Instead, you become dependent, subordinate, obedient, compliant—a quisling who betrays your own intelligence, judgment, and embodied wisdom.
You instantly become a non-human appendage, a vestige of whichever group or ideology or religion or movement or party or “leaders” you’d love to make babies for.
“Follower” is not a compliment.
And then, as soon as you re-enter your “element”, back to where you feel competent and empowered, you switch right back out of your cult infantilism just as instantly.
So, I guess you're different from a typical addict in that way. Or maybe not. Maybe it’s the same as the difference between riding your high and jonesing for a fix. Maybe the only difference is the instantaneous, circumstantial nature of the flip-flop switch.
Something psychopaths are noted for.
Give me a link to a short clear article that talks about how psychopaths can turn empathy on or off at will.

### Claude · 2026-10-26 17:54

[Psychopathic criminals have empathy switch](https://www.bbc.com/news/science-environment-23431793). It's the BBC News write-up from July 25, 2013, of the Meffert, Keysers et al. brain-scan study published in *Brain*.

That study doesn't cover "at will" switching. In it, researchers told 18 psychopathic offenders to empathize, and their brain activity then switched to empathy mode. The authors' own press release says it remains unestablished whether psychopaths switch empathy on and off by themselves depending on the social situation.
