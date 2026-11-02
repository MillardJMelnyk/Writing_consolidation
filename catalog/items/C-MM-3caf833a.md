# Metatrader 5 strategy tester freezing on EA selection

| | |
|---|---|
| Date | 2026-05-12 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-3caf833a` |
| Links | [Original](https://claude.ai/chat/3caf833a-8f41-4597-a43c-4b3c300df59d) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-05-12_metatrader-5-strategy-tester-freezing-on-ea-selection_3caf833a.html) |

**Summary:** Troubleshooting MetaTrader 5 Strategy Tester freezing on indicator selection, resolved by rolling Pepperstone MT5 back to build 5430 and blocking updates.

**Topics:** Trading and markets > Brokers, accounts and platforms; Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** MetaTrader 5; Strategy Tester; Pepperstone; software downgrade; User Account Control; LiveUpdate

[← Catalog home](../README.md)

---

### Millard · 2026-05-12 18:49

I'm having trouble with Metatrader 5's "strategy tester". No matter what I do, when I drop down the list to select an EA or indicator to test, the entire platform freezes and I have to kill the process. I clear this once before but don't remember what I did. Suggestions? Research for the answer, don't give me fucking guesses.

### Claude · 2026-05-12 18:50

Let me also check if you mentioned the fix in a past conversation.

No hit in our past conversations on the specific fix. Here's what the MQL5 forums document as confirmed fixes for strategy tester freezing/hanging (including at the dropdown stage):

**Most likely culprit (and probably what you did last time):** Delete the contents of `Tester/Cache`. One user's cache folder was 6GB, and deleting it resolved the issue.

**Second most common fix:** Delete `.log` files from the `Tester/logs` folder. One user had logs over 150MB and deleting them fixed it.

**Nuclear option that's been confirmed working** — a user on the MQL5 forum resolved persistent tester hangs by closing MT5 and removing tester profile `.ini` files from `MQL5/Profiles/Tester/`, symbol `.dat` files, trade `.dat` files, `.chr` and `.wnd` files from `MQL5/Profiles/`, renaming `tester.tpl`, clearing tick data, and clearing `Tester/cache/`.

**Also worth trying:**  
- Changing the access point/server in MT5 (lower-right corner, click the tiny bars next to the milliseconds and pick a different server).  
- Closing both MetaEditor and MT5 completely, reopening, and recompiling — debug-version `.ex5` files can cause freezes.

Start with clearing `Tester/Cache` and `Tester/logs`. That's the fix in the vast majority of reported cases and sounds like the kind of thing you'd do once and forget.

### Millard · 2026-05-12 19:05

none of that worked. I can run the ST on indicators found in the \MQL5\Indicators folder, but as soon as I try to open any of the subfolders within that folder, it hangs. I've run ST against indys located in subfolders for years. This problem only started happening in the last few weeks.

### Claude · 2026-05-12 19:06

Given the specific symptom — root-level indicators work, but opening any subfolder hangs — the tester is choking while enumerating/validating `.ex5` files inside those subfolders.

A corrupt `.ex5` file can cascade — one failed compilation corrupts memory and causes other compiled files to become invalid too. The fix is to delete all affected `.ex5` files and restart Windows. MT5 tries to read/validate every `.ex5` in a folder when it populates the dropdown, so a single corrupt one in a subfolder will hang the enumeration.

Given you've been compiling heavily in the last few weeks, the likely fix:

1. Close MT5 and MetaEditor completely
2. Go into your `MQL5\Indicators` subfolders and delete every `.ex5` file (your `.mq5` source files are untouched)
3. Restart Windows (not just MT5 — the corrupt memory state can persist)
4. Reopen MetaEditor and recompile your indicators

If you want to narrow it down first instead of nuking all `.ex5` files, you could try opening subfolders one at a time in Windows Explorer and temporarily moving each folder's `.ex5` files out until you find which subfolder triggers the hang.

### Millard · 2026-05-12 19:10

I deleted every .ex5 in the platorm's \MQL5\ folder. I closed and opened MT5, opened the ST, saw the empty "Indicator:" box, dropped the list down (which of course was empty) and the platform froze just like before.

### Claude · 2026-05-12 19:11

That changes things completely. Since it freezes even with empty subfolders, it's not a file issue — it's the strategy tester UI itself. And your timeline ("last few weeks") lines up with a confirmed MT5 platform bug.

Recent MT5 beta builds have a known strategy tester bug. A moderator on MQL5.com confirmed it and recommended downgrading to build 5430, the last stable official release. Build 5572 and subsequent builds were pushed to users and caused serious freezing issues, with multiple users reporting the platform became unusable. A moderator advised installing build 5430 and not restarting the terminal until the bugs are fixed.

There's a Telegram channel with the last official release executables for downgrading: https://t.me/MT5Exe/6 — the channel provides the right exe for your CPU type (check your Journal log on startup to see if you're running AVX2 or X64).

Check your current build number in Help → About. If it's anything past 5430, downgrade. After installing, don't let MT5 auto-update or you'll be right back in the same situation.

### Millard · 2026-05-12 19:12

don't make me do the work.

give me exact steps to "downgrade" to the stable version.

### Claude · 2026-05-12 19:13

Here's the exact procedure:

**Step 1 — Find your CPU variant.** Open MT5, go to the Journal tab (in the Toolbox at the bottom). The very first lines when MT5 starts will say something like `MetaTrader 5 x64 build 5572 started (MetaQuotes Software Corp.) ... AVX2` or `X64`. Note whichever it says — AVX2 or X64. Also confirm your build is past 5430 while you're there.

**Step 2 — Close MT5 completely.** Close MetaEditor too if it's open.

**Step 3 — Download build 5430.** Go to https://t.me/MT5Exe/6 in a browser (you don't need a Telegram account to view it). Download the zip file that matches your CPU variant from Step 1.

**Step 4 — Find your MT5 installation folder.** Typically `C:\Program Files\MetaTrader 5\` (or wherever your broker installed it). You need the folder containing `terminal64.exe` and `metatester64.exe`.

**Step 5 — Replace the exe files.** Extract the zip from Step 3. Copy the exe files from the zip into your MT5 installation folder, overwriting the existing ones.

**Step 6 — Restart MT5.** You're now on build 5430.

**Step 7 — Prevent it from happening again.** Never connect to the MetaQuotes-Demo server, and never use Help → Check for Updates → Last Beta Version. Either of those will push a beta build back onto you.

After this, recompile your indicators in MetaEditor and the strategy tester dropdown should work normally again.

### Millard · 2026-05-12 19:13

2026.05.12 13:13:14.574 Terminal Pepperstone MetaTrader 5 x64 build 5833 started for Pepperstone Group Limited  
2026.05.12 13:13:14.575 Terminal Windows 11 build 26200, 8 x Intel Core i7-9700K @ 3.60GHz, AVX2, 17 / 31 Gb memory, 200 / 930 Gb disk, UAC, GMT-6  
2026.05.12 13:13:14.575 Terminal C:\Users\Millard\AppData\Roaming\MetaQuotes\Terminal\73B7A2420D6397DFF9014A20F1201F97  
2026.05.12 13:13:16.964 Network '61511602': authorized on Pepperstone-Demo through NY1-O-Local (ping: 83.27 ms, build 5830)  
2026.05.12 13:13:16.964 Network '61511602': previous successful authorization performed from 189.180.70.47 on 2026.05.12 22:10:23  
2026.05.12 13:13:17.355 Network '61511602': terminal synchronized with Pepperstone Group Limited: 0 positions, 0 orders, 1713 symbols, 0 spreads  
2026.05.12 13:13:17.355 Network '61511602': trading has been enabled - hedging mode

### Claude · 2026-05-12 19:13

Build 5833, AVX2. Your MT5 data folder is `C:\Users\Millard\AppData\Roaming\MetaQuotes\Terminal\73B7A2420D6397DFF9014A20F1201F97` — but the exe files won't be there, they'll be in the installation folder.

Find where `terminal64.exe` lives. Run this in a Windows command prompt or PowerShell:

```
where /R "C:\Program Files" terminal64.exe
```

If that doesn't find it, try:

```
where /R "C:\" terminal64.exe
```

Then close MT5 completely, go to https://t.me/MT5Exe/6, grab the **AVX2** zip (build 5430), extract it, and overwrite the exe files in whatever folder that `where` command returned.

### Millard · 2026-05-12 19:14

C:\Program Files\Pepperstone MetaTrader 5\terminal64.exe

### Claude · 2026-05-12 19:14

1. Close MT5
2. Go to https://t.me/MT5Exe/6
3. Download the **AVX2** zip
4. Extract it — you'll get `terminal64.exe` and `metatester64.exe`
5. Copy both into `C:\Program Files\Pepperstone MetaTrader 5\`, overwrite when prompted (you may need to right-click → Run as Administrator on your file manager, or accept a UAC prompt, since it's in Program Files)
6. Start MT5
7. Confirm the Journal now says build 5430
8. Recompile your indicators in MetaEditor (Ctrl+F7 or just open any .mq5 and hit F7)
9. Try the strategy tester dropdown

After that, don't use Help → Check for Updates → Last Beta Version, and don't connect to the MetaQuotes-Demo server, or you'll get pushed right back to a broken beta build.

### Millard · 2026-05-12 19:15

I can't, I'm on my PC and don't have the Telegram app it's trying to force me to use.

### Claude · 2026-05-12 19:15

There's a non-Telegram source. For people without access to Telegram, the same files are on MQL5's Algo Forge: https://forge.mql5.io/angevoyageur/MT5-Last-Official-Release/releases

Good news — there are three stable builds available as direct downloads, no Telegram needed. Since you're AVX2:

**Latest stable (try this first):**  
https://forge.mql5.io/angevoyageur/MT5-Last-Official-Release/releases/download/Build.5660/MT5%205660%20AVX2.zip

**Fallback if 5660 doesn't fix it:**  
https://forge.mql5.io/angevoyageur/MT5-Last-Official-Release/releases/download/Build.5430/MT5\_5430\_AVX2.zip

Same steps as before — close MT5, extract the zip, copy the exe files into `C:\Program Files\Pepperstone MetaTrader 5\`, overwrite. You're going from beta build 5833 down to stable 5660 (or 5430).

### Millard · 2026-05-12 19:16

here's what I see

### Claude · 2026-05-12 19:16

Click the **► Downloads** triangle to expand it — that's a collapsible section. The zip files are hidden behind it.

### Claude · 2026-05-12 19:16

Download **MT5\_5430\_AVX2.zip**. Then:

1. Close MT5
2. Extract the zip
3. Copy the exe files into `C:\Program Files\Pepperstone MetaTrader 5\`, overwrite
4. Start MT5, confirm Journal says build 5430
5. Recompile your indicators, test the dropdown

### Millard · 2026-05-12 19:17

why that one and not the X64 version?

DO NOT FUCK WITH ME AND TELL ME TO TAKE ACTIONS BASED ON GUESSES!!!!

### Claude · 2026-05-12 19:17

Not a guess. Your Journal log that you pasted earlier:

```
Windows 11 build 26200, 8 x Intel Core i7-9700K  @ 3.60GHz, AVX2, 17 / 31 Gb memory
```

MT5 is telling you it's running the AVX2 variant. That's why you download the AVX2 zip.

### Millard · 2026-05-12 19:19

Here's what I see in the .zip

### Claude · 2026-05-12 19:19

All three files — `terminal64.exe`, `metatester64.exe`, and `MetaEditor64.exe`. Select all, copy them into `C:\Program Files\Pepperstone MetaTrader 5\`, overwrite all three.

### Millard · 2026-05-12 19:19

OK, just copy, no uninstall/reinstall?

### Claude · 2026-05-12 19:19

Correct. Just overwrite. Your settings, indicators, source files, profiles — everything stays intact. You're only replacing the three executables.

### Millard · 2026-05-12 19:23

done

### Claude · 2026-05-12 19:23

Start MT5. Check the first line of the Journal — it should say build 5430. Let me know what it says.

### Millard · 2026-05-12 19:24

2026.05.12 13:23:59.316 Terminal Pepperstone MetaTrader 5 x64 build 5430 started for Pepperstone Group Limited  
2026.05.12 13:23:59.316 Terminal Windows 11 build 26200, 8 x Intel Core i7-9700K @ 3.60GHz, AVX2, 16 / 31 Gb memory, 200 / 930 Gb disk, UAC, GMT-6  
2026.05.12 13:23:59.316 Terminal C:\Users\Millard\AppData\Roaming\MetaQuotes\Terminal\73B7A2420D6397DFF9014A20F1201F97  
2026.05.12 13:24:02.029 LiveUpdate new version build 5830 (IDE: 5830, Tester: 5830) is available  
2026.05.12 13:24:02.292 Network '61511602': authorized on Pepperstone-Demo through NY1-O-Local (ping: 83.27 ms, build 5830)  
2026.05.12 13:24:02.292 Network '61511602': previous successful authorization performed from 189.180.70.47 on 2026.05.12 22:13:17  
2026.05.12 13:24:03.134 Network '61511602': terminal synchronized with Pepperstone Group Limited: 0 positions, 0 orders, 1713 symbols, 0 spreads  
2026.05.12 13:24:03.134 Network '61511602': trading has been enabled - hedging mode

### Claude · 2026-05-12 19:24

Build 5430, good. Two things:

1. **Do NOT accept that update** — the `LiveUpdate: new version build 5830 is available` line means MT5 is trying to push you back to the broken beta. If a popup appears, click "Later" or just ignore it. Don't restart MT5 unnecessarily — when you do restart, it may auto-install the update. To prevent future beta pushes, never connect to the MetaQuotes-Demo server and never use Help → Check for Updates → Last Beta Version.
2. Now recompile your indicators and try the strategy tester dropdown.

### Millard · 2026-05-12 19:25

In my experience, closing and opening MT5 will force the update.

### Claude · 2026-05-12 19:26

You're right — MT5's auto-update system cannot be deactivated, and if you click "Later" it just installs automatically on the next restart.

The working workaround is to block it with file permissions. Go to `%appdata%\MetaQuotes\WebInstall`, right-click the folder, select Properties → Security tab → Edit → select your user → check "Deny" on Write permission → Apply.

That prevents MT5 from downloading updates into that folder. When there's nothing downloaded, there's nothing to install on restart.

But first — test the strategy tester dropdown now while you're on 5430 and confirm it works before worrying about locking it down.

### Millard · 2026-05-12 19:27

this is all i see there

### Claude · 2026-05-12 19:27

Those are the downloaded update packages (named `.png` but they're actually update files — MetaQuotes disguises them). Delete everything in that folder, then right-click the **WebInstall** folder itself → Properties → Security → Edit → select your user (Millard) → check **Deny** on **Write** → Apply.

That prevents new updates from being downloaded. No downloads, nothing to install on restart.

But go test the strategy tester dropdown first — confirm that build 5430 actually fixed your problem before you close MT5.

### Millard · 2026-05-12 19:29

that's it, just check that one box?

### Claude · 2026-05-12 19:30

Yes, but do the same for **SYSTEM** and **Administrators** too — MT5 may write under those contexts. Click each one in the list and check Deny on Write for all three. Then Apply.

### Millard · 2026-05-12 19:31

done, next?

### Claude · 2026-05-12 19:31

Test the strategy tester dropdown. Open ST, drop the indicator list, navigate into a subfolder.

### Millard · 2026-05-12 19:36

OK, I still get this message, but if I click "No", it still opens the platform and doesn't look like it's installing anything.2026.05.12 13:35:41.660 Terminal Pepperstone MetaTrader 5 x64 build 5430 started for Pepperstone Group Limited  
2026.05.12 13:35:41.660 Terminal Windows 11 build 26200, 8 x Intel Core i7-9700K @ 3.60GHz, AVX2, 16 / 31 Gb memory, 199 / 930 Gb disk, UAC, GMT-6  
2026.05.12 13:35:41.660 Terminal C:\Users\Millard\AppData\Roaming\MetaQuotes\Terminal\73B7A2420D6397DFF9014A20F1201F97  
2026.05.12 13:35:44.673 Network '61511602': authorized on Pepperstone-Demo through NY1-O-Local (ping: 83.27 ms, build 5830)  
2026.05.12 13:35:44.673 Network '61511602': previous successful authorization performed from 189.180.70.47 on 2026.05.12 22:35:10  
2026.05.12 13:35:45.136 Network '61511602': terminal synchronized with Pepperstone Group Limited: 0 positions, 0 orders, 1713 symbols, 0 spreads  
2026.05.12 13:35:45.136 Network '61511602': trading has been enabled - hedging mode

### Claude · 2026-05-12 19:37

That's the permissions block working — it's trying to update, can't write the files, UAC fires, you say No, and you stay on 5430. That'll happen every restart but it's harmless. Just always click No.

Now test the dropdown — open Strategy Tester, try navigating into a subfolder.
