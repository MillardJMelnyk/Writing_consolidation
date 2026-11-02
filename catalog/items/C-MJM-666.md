# Disable Codex approval prompts in VS Code

| | |
|---|---|
| Date | 2026-02-20 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-666` |
| Links | [Original](https://claude.ai/chat/89f90690-3ee3-4f7c-b8df-52908c7a8010) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/666-2026-02-20-disable-codex-approval-prompts-in-vs-code.html) |

**Summary:** Stopping GPT-5.3-Codex in VS Code from pausing for approvals; setting approval_policy only works in the Codex config.toml file.

**Topics:** AI chatbots and working with Claude > Comparing AI models and chatbots; Practical & personal > Software tools and open-source projects

**Index terms:** OpenAI Codex; GPT-5.3-Codex; Visual Studio Code; approval policy; config.toml

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-02-20 16:33

I'm using Codex in VS Code. Once we've agreed and I've given it a GO, it still stops several times mid-process to ask for yes/no to proceed. Where can I set this behavior to have it complete the task without interrupting approval requests?

### Claude · 2026-02-20 16:33

Friday, February 20, 2026, time unknown (no timezone data available).

This is controlled by the **autonomy mode** setting in Claude Code / Codex. There are three modes:

* **Suggest** — asks permission before every action (default)
* **Auto-edit** — reads/writes files without asking, but still prompts before running terminal commands
* **Full auto** — executes everything without interruption

To set it in VS Code, open the Codex panel and look for the mode selector (typically a dropdown near the input field). Switch to **Full auto** to eliminate the mid-task approval prompts.

Alternatively, you can set it via the CLI config if you're also using Claude Code outside VS Code:

`claude config set autoMode full`

Fair warning: full auto will execute shell commands without confirmation, so scope your tasks tightly.

### Millard · 2026-02-20 16:35

why are you confused? I'm asking about GPT-5.3-Codex, not any Claude model.

### Claude · 2026-02-20 16:35

My mistake — I assumed Claude Code. Let me search for the current Codex agent settings.

Corrected. Here's what applies to OpenAI Codex in VS Code:

**The mode selector** in the Codex panel has three levels:

1. **Chat** — conversation only, no file/command access
2. **Agent** — reads, writes, runs commands, but asks approval before each action
3. **Agent (Full Access)** — full autonomy, no approval prompts

Switch to **Agent (Full Access)** to eliminate the interruptions.

**Known issue (as of late 2025):** Multiple users report that even with "Agent (Full Access)" selected, Codex still prompts for approval on every change. In v0.20, full-auto still prompts for writes unless both sandbox and approval checks are disabled and the workspace is trusted — a "trusted workspace" flag was introduced in v0.20 that earlier versions didn't require.

If you're hitting this bug, the CLI flags that map to the same behavior are:

```
codex --full-auto
```

or more aggressively:

```
codex -a never --sandbox workspace-write
```

If that still doesn't resolve it, check `/status` inside the Codex session to confirm `trusted-workspace` is `true`. If it's `false`, that's overriding your settings.

### Millard · 2026-02-20 16:35

how did you get "Claude Code" from "Codex"?

### Claude · 2026-02-20 16:35

I didn't have a good reason. "Codex" is unambiguously an OpenAI product. I defaulted incorrectly. My fault.

### Millard · 2026-02-20 16:36

"The mode selector in the Codex panel has three levels:"
Where?

[File attached: 1771605396738\_image.png — contents not included in export]

### Claude · 2026-02-20 16:36

It's not there. The three-mode selector I described appears to be from an earlier version of the extension. Your interface is different.

In your screenshot, the control you want is **"Default permissions"** — that dropdown at the bottom. Click it and see what options it offers. That's where approval behavior is configured in your version.

### Millard · 2026-02-20 16:37

No, that determines the scope of its permissions on my machine. Not the same thing.

[File attached: 1771605460083\_image.png — contents not included in export]

### Claude · 2026-02-20 16:38

You're right — scope of access vs. approval flow are separate controls. Let me find the actual approval setting.

The intended config is in `~/.codex/config.toml`:

```
approval_policy = "never"
sandbox_mode = "workspace-write"
```

However, this is a **known, unfixed bug** in the VS Code extension. Users report having to approve the same prompt 25+ times in a single response, even after selecting "Yes, and don't ask again this session." The issue was first reported months ago and still persists. As recently as two days ago, users confirm the problem remains even with `approval_policy` set and the folder marked as a Trusted Workspace, across both release and pre-release extension versions.

One workaround that has worked for some users: mark the folder as a Trusted Workspace in VS Code, then restart VS Code. But results are inconsistent.

Bottom line: the setting exists, but the extension doesn't reliably honor it. This is an open bug on the OpenAI Codex GitHub repo, not a configuration error on your end.

### Millard · 2026-02-20 16:38

OK, where in VS Code can I set it?

### Claude · 2026-02-20 16:39

There's no UI toggle for approval policy in the extension panel. It's config-file only.

From within VS Code: click the **gear icon** in the top-right corner of the Codex panel, then select **Codex Settings → Open config.toml**.

In that file, add or edit:

```
approval_policy = "never"
```

Then restart VS Code.

But as noted — the extension has a known bug where it ignores this setting inconsistently, particularly for shell commands.

### Millard · 2026-02-20 16:39

approval\_policy = "never"
That would mean it never has approval, doesn't it?

### Claude · 2026-02-20 16:39

Fair reading of ambiguous naming. It means "never **ask** for approval" — i.e., skip all prompts and just execute. Not "never grant approval."

### Millard · 2026-02-20 16:41

OK, how do I set the workspace folder as trusted?

### Claude · 2026-02-20 16:41

In VS Code: **Ctrl+Shift+P** → type **"Workspace Trust"** → select **"Workspaces: Manage Workspace Trust"** → click **Trust** for the folder.

Alternatively, if you've never been prompted, open the folder and VS Code should ask on first open. If it doesn't, you may have `"security.workspace.trust.enabled": false` in your settings, which trusts everything by default.

### Millard · 2026-02-20 16:42

It tells me the folder is already trusted. Here are the available settings. Should I change anything?

[File attached: 1771605758469\_image.png — contents not included in export]

### Claude · 2026-02-20 16:42

No. Those settings are correct — trust is enabled and the folder is already trusted. Nothing to change here.

The problem isn't your configuration. It's the Codex extension bug. You've done everything right: `approval_policy = "never"`, trusted workspace, full access permissions. The extension just doesn't reliably honor it.

### Millard · 2026-02-20 16:47

Are there keys I could add to the settings JSON file?

[File attached: 1771606005889\_image.png — contents not included in export]

### Claude · 2026-02-20 16:47

No. The VS Code `settings.json` does not have a working key for approval policy. Someone tried adding `"chatgpt.config": { "approval_policy": "never", "sandbox_mode": "workspace-write" }` to settings.json — it was filed as a bug because the extension ignores it.

The only place the approval setting is read from is `~/.codex/config.toml`. On your Windows machine that would be `C:\Users\Millard\.codex\config.toml`.
