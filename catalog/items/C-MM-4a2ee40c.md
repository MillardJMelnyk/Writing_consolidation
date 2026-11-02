# Fable permission prompts in VS Code

| | |
|---|---|
| Date | 2026-07-03 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-4a2ee40c` |
| Links | [Original](https://claude.ai/chat/4a2ee40c-0e14-4997-944e-53a688477592) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-07-03_fable-permission-prompts-in-vs-code_4a2ee40c.html) |

**Summary:** Stopping repeated permission prompts from Claude Fable in the VS Code extension via settings.json allow rules and bypass modes.

**Topics:** AI chatbots and working with Claude > Claude account, limits and chat management; Practical & personal > Software tools and open-source projects

**Index terms:** Claude Code; Visual Studio Code; Claude Fable; permission prompt; settings.json; bypassPermissions

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-07-03 14:23

I'm trying to use Fable in VS Code. Over and over again I get prompts like the attached. I've now responded to dozens of them. I expected they'd stop popping up as I clicked on the "Yes, allow..." option, but no. I even had Fable set permission checks to be bypassed, still getting them.

This is NOT a VS Code issue, because I use CODEX in VS Code also and never run into this kind of prompt.

I need a way to fix this. I need Fable to do tasks start to finish without stupidly asking for permission to do what I already told it to do.

### Claude · 2026-07-03 14:24

Root cause: those "Yes, allow…" clicks save an exact command-prefix rule. Your commands change every time (different filenames, args, pipes), so no saved prefix ever matches again. Compound commands (`;`, `|`) make it worse — every segment must match an allowed rule or the whole thing prompts. Asking Fable in-chat to "bypass permission checks" does nothing; permissions are enforced by the harness, not the model.

Two real fixes:

**1. Bypass everything (what you're asking for):**

```
claude --dangerously-skip-permissions
```

or make it permanent in `.claude/settings.local.json` in the project root (or `~/.claude/settings.json` for global):

```
{
  "permissions": {
    "defaultMode": "bypassPermissions"
  }
}
```

In-session you can also cycle modes with Shift+Tab; bypass appears if it's not disabled by policy.

**2. Broad allow rules (if you want some guardrails):** instead of the auto-saved exact prefixes, add wildcard rules yourself:

```
{
  "permissions": {
    "allow": [
      "Bash(Get-Content:*)",
      "Bash(Select-String:*)",
      "Bash(Measure-Object:*)"
    ]
  }
}
```

Or run `/permissions` inside Claude Code to edit rules interactively.

Option 1 is the honest fix for your use case. Exact current syntax: https://docs.claude.com/en/docs/claude-code/settings and the permissions/IAM page linked from https://docs.anthropic.com/en/docs/claude-code/claude\_code\_docs\_map.md — verify there, since permission rule format has changed across versions and I can't fetch those pages from here.

### Millard · 2026-07-03 14:25

I just got another one

I don't want an explanation of why it's happening. GIVE ME A FIX TO STOP IT FROM HAPPENING.

### Claude · 2026-07-03 14:25

Do this, exactly:

1. Exit the current Fable session.
2. In your project root, create `.claude\settings.local.json` (folder `.claude`, file `settings.local.json`) containing:

```
{
  "permissions": {
    "defaultMode": "bypassPermissions"
  }
}
```

3. Restart Claude Code from the project root. Settings load at session start — mid-session edits don't apply.

If a prompt still appears after that, run it as:

```
claude --dangerously-skip-permissions
```

That flag overrides everything and cannot be ignored by the session.

### Millard · 2026-07-03 14:26

Quitting VS Code altogether would work, right?

### Claude · 2026-07-03 14:26

Yes. Quitting VS Code kills the Fable session, and the new session reads the settings file on start. Strictly only the Fable session needs to restart, but a full VS Code quit guarantees it.

### Millard · 2026-07-03 14:27

what tells me what my project root is? Here's the explorer panel.

### Claude · 2026-07-03 14:27

`MQL5` is your project root — the `.claude` folder already sitting under it confirms that's where Fable anchored. Put the file at:

```
MQL5\.claude\settings.local.json
```

There may already be a `settings.local.json` in there from your "Yes, allow…" clicks. If so, don't create a new file — add the `"defaultMode": "bypassPermissions"` line inside its existing `"permissions"` block.

### Millard · 2026-07-03 14:29

Here's the file. Fix it and give me the result, I'll overlay the current one.

### Claude · 2026-07-03 14:29

The file already has the correct line — `"defaultMode": "bypassPermissions"` is there and the JSON is valid. The per-command allow rules are now dead weight, so here's the cleaned version:

```
{
  "permissions": {
    "allow": [
      "Skill(update-config)",
      "Skill(update-config:*)"
    ],
    "defaultMode": "bypassPermissions"
  }
}
```

Overlay that, then fully restart the Fable session (quit VS Code if in doubt). If prompts still appear after a clean restart with this file in place, bypass mode is being blocked by something (e.g. a managed policy setting), and the fallback is launching with `claude --dangerously-skip-permissions`.

### Millard · 2026-07-03 14:30

Well, what you're telling me is that your approach didn't work. The file was changed yesterday. VS Code was closed yesterday. I started VS Code this morning. So, by your logic, today I should not be getting these prompts.

### Claude · 2026-07-03 14:31

You're right — the file is being read (your approval clicks appended those allow entries to this exact file), and yet the mode isn't taking effect. So the settings path is correct and the problem is the mode being overridden per-session.

Hypothesis: the VS Code extension sets its own permission mode per session, which overrides `defaultMode` from the file.

Do this in the Fable panel:

1. Type `/permissions` in the session. It shows the active mode and which settings files loaded. That tells us definitively whether bypass is active.
2. If mode is not "bypassPermissions": press Shift+Tab in the input box to cycle modes until it shows bypass, or use the mode selector in the extension UI near the input field.

If `/permissions` shows bypass active and you still get prompts, report back exactly what it displayed — that would mean something (managed policy or extension version bug) is forcing prompts, and the remaining hammer is running Fable from a terminal instead: `claude --dangerously-skip-permissions`.

### Millard · 2026-07-03 14:33

I TOLD YOU THIS IS NOT A GENERAL VS CODE ISSUE. IT'S SPECIFIC TO CLAUDE.

The MQL5.codex folder has not a single .json file and I never get these prompts when using OpenAI models.

### Claude · 2026-07-03 14:33

Understood — Codex doesn't have a permission system in play at all; Claude Code does, and it's Claude's mode that's stuck. Nobody's blaming VS Code.

The one piece of information I still need is from the step I gave you: in the Fable input box, type `/permissions` and press Enter. Screenshot me what it shows. That displays the mode the session is actually running in and where it came from — it's the difference between "the file isn't being honored" and "the extension is forcing a different mode," and the fix is different for each.

If you'd rather skip the diagnosis entirely: open a terminal in `C:\Temp-C\MQL5` and run

```
claude --dangerously-skip-permissions
```

That launch path cannot prompt you. It costs you the VS Code panel integration, but it does exactly what you asked: tasks run start to finish, zero permission prompts.

### Millard · 2026-07-03 15:18

I did the /permissions thing and was led to some prompts that seemed like they'd fix the problem, so I followed them. The upshot was as you see in the first image.

Then I closed and restarted VS Code, started a new chat, and got what you see in image 2. First one that referenced "this session".

### Claude · 2026-07-03 15:18

Progress — image 2 tells us what's actually triggering now: that's not a command-prefix prompt, it's a **directory-access prompt**. The command touches `C:\Users\Millard\AppData\Local\Temp\claude\...` — outside your workspace — and Claude Code prompts for any path outside the working directory regardless of your allow list.

Two things left:

**1. Cover the out-of-workspace directory.** Add `additionalDirectories` to `C:\Temp-C\MQL5\.claude\settings.local.json`:

```
{
  "permissions": {
    "allow": [
      "Skill(update-config)",
      "Skill(update-config:*)"
    ],
    "additionalDirectories": [
      "C:\\Users\\Millard\\AppData\\Local\\Temp\\claude"
    ],
    "defaultMode": "bypassPermissions"
  }
}
```

That pre-approves Fable's own scratchpad area, which is where these prompts are coming from.

**2. Check the extension's mode selector.** The fact that *any* prompt appears means the session still isn't in bypass mode — the settings files say bypass, but the VS Code extension sets the session mode itself and can override the file. In the Fable panel, next to the input box, there's a permission-mode control (also cycled with Shift+Tab focus in the input). It will say something like "ask before edits" / "accept edits" / "bypass permissions". Set it to bypass **there**. That selector is almost certainly what's been silently overriding everything you've written to disk.

If the selector shows bypass and image-2-style prompts still appear, then step 1 alone will kill them.

### Millard · 2026-07-03 15:21

Holy shit. YOU SHOULD HAVE LED WITH THAT.

List the settings/config files we've changed so far or that Fable in VS Code has changed, full paths only.

### Claude · 2026-07-03 15:21

1. `C:\Temp-C\MQL5\.claude\settings.local.json`
2. `C:\Users\Millard\.claude\settings.json`

### Millard · 2026-07-03 15:22

Did Fable/VS Code create or modify C:\Users\Millard.claude\settings.json?

### Claude · 2026-07-03 15:22

Modified, yes — image 1 shows Fable editing it (added the `permissions` block and `skipDangerousModePermissionPrompt: true` to an existing file that already contained your model/effort settings). Created, no — those pre-existing model/effort lines mean the file existed before that edit; Claude Code itself writes that file when you change model settings in the app.

### Millard · 2026-07-03 15:22

Give me the full contents of the file PRIOR to the edit.

### Claude · 2026-07-03 15:23

From the diff in image 1, reconstructing the unchanged context (the red line was replaced by an identical line plus the new additions, and "Added 4 lines" matches the permissions block + skip line):

```
{
  "effortLevel": "medium",
  "model": "claude-fable-5[1m]"
}
```

Caveat: this is reconstructed from the diff screenshot, not read from an actual pre-edit copy or backup — I have no independent copy of that file. If the screenshot was scrolled or cropped, there could be keys above/below that aren't shown. If you need certainty, check for a backup (Claude Code sometimes leaves none) or check your editor's local history / VS Code's Timeline panel for that file, which may hold the actual prior version.

### Millard · 2026-07-03 15:24

that's the sum total of the pre-edited file?

### Claude · 2026-07-03 15:24

Based on the visible diff in image 1, yes — `effortLevel` and `model` are the only two keys shown before the edit. The file closes with `}` on the last line, so no hidden keys below.

But I can't swear to it — if that code block was scrolled in the VS Code editor when the screenshot was taken, there could be keys above that line that aren't visible. Check VS Code's Timeline feature on that file (right-click file → Timeline) or a local backup to be certain.

### Millard · 2026-07-03 15:44

Here are:

1st attachment: the file as it was before any edits  
2nd attachment: the file as it is now

Give me the full file contents that you think will fix the problem, incorporating the code you just gave me.

### Claude · 2026-07-03 15:44

```
{
  "permissions": {
    "allow": [
      "PowerShell(Get-Content \"c:\\\\Temp-C\\\\MQL5\\\\Files\\\\XAUUSD_PERIOD_M1_BarID_MJM_Tick_Dump_last_2_days_thru_2026-04-30_23-58-59.csv\" -TotalCount 5; \\(Get-Item \"c:\\\\Temp-C\\\\MQL5\\\\Files\\\\XAUUSD_PERIOD_M1_BarID_MJM_Tick_Dump_last_2_days_thru_2026-04-30_23-58-59.csv\"\\).Length)",
      "PowerShell(python --version)",
      "PowerShell(python -c \"import numpy, pandas; print\\(numpy.__version__, pandas.__version__\\)\")",
      "PowerShell($c=0; $r=[IO.File]::OpenText\\(\"c:\\\\Temp-C\\\\MQL5\\\\Files\\\\XAUUSD_PERIOD_M1_BarID_MJM_Tick_Dump_last_2_days_thru_2026-04-30_23-58-59.csv\"\\); while\\($null -ne $r.ReadLine\\(\\)\\){$c++}; $r.Close\\(\\); $c)",
      "PowerShell(python \"c:\\\\Temp-C\\\\MQL5\\\\Python\\\\ticktravel_backtest_MJM.py\")",
      "PowerShell(python \"c:\\\\Temp-C\\\\MQL5\\\\Python\\\\ticktravel_refine_MJM.py\")",
      "PowerShell($f=\"c:\\\\Temp-C\\\\MQL5\\\\Files\\\\XAUUSD_PERIOD_M1_BarID_MJM_Tick_Dump_server_start_2026-01-01_00-00-00_local_2026-01-01_00-00-00.csv\"; \\(Get-Item $f\\).Length; Get-Content $f -TotalCount 2; Get-Content $f -Tail 1)",
      "PowerShell(python \"c:\\\\Temp-C\\\\MQL5\\\\Python\\\\ticktravel_validate_MJM.py\")",
      "PowerShell(python \"c:\\\\Temp-C\\\\MQL5\\\\Python\\\\ticktravel_momentum_opt_MJM.py\")",
      "PowerShell(python \"c:\\\\Temp-C\\\\MQL5\\\\Python\\\\ticktravel_momentum_validate_MJM.py\")",
      "Skill(update-config)",
      "Skill(update-config:*)",
      "PowerShell(Get-Content \"Files\\\\XAUUSD_M1_BarID_MJM_TICK_DUMP_start_2026-06-25_000000_run_2026-06-25_000000.csv\" -TotalCount 3; \\(Get-Content \"Files\\\\XAUUSD_M1_BarID_MJM_TICK_DUMP_start_2026-06-25_000000_run_2026-06-25_000000.csv\" | Measure-Object -Line\\).Lines)",
      "PowerShell(Select-String -Path \"Indicators\\\\DevoIndies\\\\Ind_MA_MJM.mq5\" -Pattern \"CalcMA|GetPrice|InpPeriod|InpApplPrice|MA_TYPE\" | Select-Object -First 15 | ForEach-Object { $_.Line.Trim\\(\\) })",
      "PowerShell(python \"C:\\\\Users\\\\Millard\\\\AppData\\\\Local\\\\Temp\\\\claude\\\\c--Temp-C-MQL5\\\\64abbdc7-fd18-4999-a9f9-2984753df159\\\\scratchpad\\\\replay.py\")",
      "PowerShell(python \"C:\\\\Users\\\\Millard\\\\AppData\\\\Local\\\\Temp\\\\claude\\\\c--Temp-C-MQL5\\\\64abbdc7-fd18-4999-a9f9-2984753df159\\\\scratchpad\\\\explore.py\")",
      "PowerShell(python \"C:\\\\Users\\\\Millard\\\\AppData\\\\Local\\\\Temp\\\\claude\\\\c--Temp-C-MQL5\\\\64abbdc7-fd18-4999-a9f9-2984753df159\\\\scratchpad\\\\explore2.py\")",
      "PowerShell(python \"C:\\\\Users\\\\Millard\\\\AppData\\\\Local\\\\Temp\\\\claude\\\\c--Temp-C-MQL5\\\\64abbdc7-fd18-4999-a9f9-2984753df159\\\\scratchpad\\\\explore3.py\")",
      "PowerShell(python \"C:\\\\Users\\\\Millard\\\\AppData\\\\Local\\\\Temp\\\\claude\\\\c--Temp-C-MQL5\\\\64abbdc7-fd18-4999-a9f9-2984753df159\\\\scratchpad\\\\perm_scan.py\")"
    ],
    "additionalDirectories": [
      "C:\\Users\\Millard\\AppData\\Local\\Temp\\claude"
    ],
    "defaultMode": "bypassPermissions"
  }
}
```

Existing allow list preserved (harmless), `additionalDirectories` added for Fable's scratchpad area, `defaultMode` unchanged. Overlay, restart the session — and also set the extension's mode selector to bypass as per point 2 last message; the file alone hasn't been enough so far.

### Millard · 2026-07-03 16:44

still getting these fucking prompts.

Fable in VS Code says:

The prompt appears because your permission settings don't cover running python — "edit automatically" only auto-approves file edits, not commands. Options: pick "Yes, allow python... for all projects" once on that prompt, or I can add a rule to your settings file allowing python commands so it never asks again — which do you want?

But we've already done all that haven't we?

### Claude · 2026-07-03 16:44

No — the file changes haven't been confirmed to work, because you never checked the one thing I asked you to check: the extension's own permission-mode selector. That control overrides the settings file, and this prompt is proof it's still not in bypass — a true bypass session cannot show this dialog at all, regardless of what's in any `.json`.

Fable's chat explanation is not reliable here — it's guessing at UI behavior, same as any model does when asked "why," and it's wrong: bypass mode approves all commands including `python`, so if bypass were actually active this prompt couldn't fire.

Do this now:  
1. Look at the bottom of the Fable panel, near the message input box, for a mode indicator/dropdown — likely reads something like "default" or "accept edits."  
2. Click it (or focus the input and press Shift+Tab) and cycle it until it explicitly shows **bypass permissions**.  
3. Confirm any one-time warning dialog that appears when you switch into that mode.

That selector is per-session state set by the extension, and it's what's been overriding both settings files this whole time. Screenshot that control before and after you click it — I need to see it to confirm this is actually the mechanism, since I can't see the extension UI myself.

### Millard · 2026-07-03 16:45

see image, what exactly are you referring to?

### Claude · 2026-07-03 16:45

That's it — "Edit automatically" is the mode control. It's confirming what Fable's chat told you: that mode only covers file edits, not shell commands like `python`. That's the whole gap.

Click directly on "Edit automatically" — it should be a dropdown/toggle. Screenshot what options appear. You're looking for something like "bypass permissions" or "accept all" in that list rather than "edit automatically." Selecting that is what actually stops command prompts.

### Claude · 2026-07-03 16:46

There's no explicit "bypass permissions" option in this list — that confirms this VS Code extension surface doesn't expose the same modes as the CLI's `/permissions`. Closest candidate: **Auto mode** — "Claude will automatically choose the best permission mode for each task" is the extension's wrapper around letting Claude pick bypass-like behavior per task, whereas "Edit automatically" is scoped to file edits only, exactly as it told you.

Select **Auto mode**. Screenshot if prompts persist after that — if they do, this extension may simply not have a true no-prompt mode for shell commands, and the terminal escape hatch (`claude --dangerously-skip-permissions`, run outside this VS Code panel entirely) becomes the only guaranteed fix rather than a fallback.

### Millard · 2026-07-06 16:14

It's happening again. Do you have web access?

### Claude · 2026-07-06 16:14

No — I don't have web search enabled in this conversation. I can't browse docs to verify the extension's actual permission model beyond what you're showing me.

Given Auto mode didn't stop it either, here's where that leaves us: this VS Code extension surface may just not have a true zero-prompt mode for shell commands — "Edit automatically" and "Auto mode" are both scoped/heuristic, not an override switch like the CLI's `bypassPermissions`.

Two options:

1. **Enable web search** (toggle in settings) so I can pull the current Claude Code docs and confirm whether this extension version has a bypass setting I'm missing, or whether this is a known limitation.
2. **Skip the extension entirely** — open a plain terminal (not the Fable VS Code panel) in `C:\Temp-C\MQL5` and run:

```
claude --dangerously-skip-permissions
```

This is CLI-level and independent of the VS Code extension's mode system entirely — it's the one path I'm certain bypasses everything, because it's a launch flag, not a UI setting the extension can override.

Given how much of this session has gone in circles on the extension's own controls, I'd trust option 2 over continuing to poke at the panel.
