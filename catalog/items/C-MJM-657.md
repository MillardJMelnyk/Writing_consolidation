# Kimi Code extension setup after VS Code crash

| | |
|---|---|
| Date | 2026-02-17 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-657` |
| Links | [Original](https://claude.ai/chat/d4fbe83a-3f01-46e6-8726-c325d424adf4) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/657-2026-02-17-kimi-code-extension-setup-after-vs-code-crash.html) |

**Summary:** Reinstalling the Kimi Code VS Code extension and CLI on Windows after a crash, troubleshooting install conflicts and an unresponsive init.

**Topics:** Practical & personal > Software tools and open-source projects; AI chatbots and working with Claude > Comparing AI models and chatbots

**Index terms:** Kimi Code; Visual Studio Code; kimi-cli; Moonshot AI; VS Code extension

[← Catalog home](../README.md)

---

### Millard · 2026-02-17 16:14

I've been using the Kimi Code extension in VS Code, worked fine until a python script seems to have crashed VS Code, and now I can't get the KC extension to work. So, I uninstalled it and removed the moonshot folders from globalStorage and from .vscode. I need your help to get me set up again.

### Claude · 2026-02-17 16:14

Tuesday, February 17, 2026, time unknown (no timezone provided)

What specific behavior are you seeing now when you attempt to reinstall or launch Kimi Code? Error messages, failure to activate, settings not appearing, something else?

### Millard · 2026-02-17 16:14

assume we have a clean slate, help me get the extension installed and working again. Simple, crisp list of steps.

### Claude · 2026-02-17 16:14

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search "Kimi Code"
4. Click Install
5. Restart VS Code after installation completes
6. Open Command Palette (Ctrl+Shift+P)
7. Type "Kimi Code" to see available commands — look for sign-in or authentication option
8. Authenticate with your Moonshot account when prompted

If it fails at any step, tell me which one and what you see.

### Millard · 2026-02-17 16:29

it said initialization/loading might take 30 seconds. It took over 15 minutes, and this is what it says now:

[File attached: 1771345748152\_image.png — contents not included in export]

### Claude · 2026-02-17 16:29

What OS are you on? Windows, Mac, or Linux?

If Windows: you'll need Git Bash, WSL, or similar to run that curl command — or there may be a Windows-specific installer.

### Millard · 2026-02-17 18:29

don't I just run it in the terminal window inside VS Code?

### Claude · 2026-02-17 18:29

Depends on your OS:

* **Mac/Linux**: Yes, run it directly in VS Code terminal
* **Windows**: Only if your VS Code terminal is set to Git Bash or WSL. PowerShell/CMD won't execute that `| bash` syntax correctly.

Which OS?

### Millard · 2026-02-17 18:29

windows

### Claude · 2026-02-17 18:29

Options:

1. **If you have Git Bash installed**: Open VS Code terminal, click the dropdown arrow next to the "+" icon, select "Git Bash", then run the curl command
2. **If you have WSL installed**: Same process, select your WSL distro from the terminal dropdown, then run the command
3. **Neither installed**: Check if Kimi provides a Windows installer — run this in PowerShell to see if there's an .exe or .msi option:

   ```
   Invoke-WebRequest -Uri "https://cdn.kimi.com/binaries/kimi-cli/install.sh" -OutFile "install.sh"
   ```

   Then send me the contents of that file and I'll tell you what to do next.

Which path do you want to take?

### Millard · 2026-02-17 18:31

"click the dropdown arrow next to the "+" icon,"
dude, could you be any more vague?

### Claude · 2026-02-17 18:31

Fair point.

1. Open VS Code terminal (Ctrl+`)
2. Look at the top-right corner of the terminal panel
3. Find the **+** button (creates new terminal)
4. Immediately to its right is a small downward chevron **˅**
5. Click that chevron
6. Select "Git Bash" from the list

If Git Bash doesn't appear in that list, you don't have it installed.

### Millard · 2026-02-17 18:31

OH! IN THE TERMINAL PANEL! WHY DIDN'T YOU SAY SO? YUK YUK

### Claude · 2026-02-17 18:31

Yeah yeah. Did Git Bash show up in the list?

### Millard · 2026-02-17 18:32

It's there

[File attached: 1771353140799\_image.png — contents not included in export]

### Claude · 2026-02-17 18:32

1. Click "Git Bash"
2. Run: `curl -LsSf https://cdn.kimi.com/binaries/kimi-cli/install.sh | bash`
3. After it finishes, restart VS Code

Report back what happens.

### Millard · 2026-02-17 18:34

Millard@Millards-PC MINGW64 /c/Temp-C/MQL5
$ curl -LsSf https://cdn.kimi.com/binaries/kimi-cli/install.sh | bash
Resolved 123 packages in 3.97s
Prepared 2 packages in 733ms
Installed 123 packages in 2.79s
+ agent-client-protocol==0.7.0
+ aiofiles==25.1.0
+ aiohappyeyeballs==2.6.1
+ aiohttp==3.13.3
+ aiosignal==1.4.0
+ annotated-doc==0.0.4
+ annotated-types==0.7.0
+ anthropic==0.79.0
+ anyio==4.12.1
+ asyncssh==2.21.1
+ attrs==25.4.0
+ authlib==1.6.8
+ babel==2.18.0
+ certifi==2026.1.4
+ cffi==2.0.0
+ charset-normalizer==3.4.4
+ click==8.3.1
+ colorama==0.4.6
+ courlan==1.3.2
+ cryptography==46.0.5
+ cyclopts==4.5.3
+ dateparser==1.3.0
+ distro==1.9.0
+ dnspython==2.8.0
+ docstring-parser==0.17.0
+ docutils==0.22.4
+ email-validator==2.3.0
+ exceptiongroup==1.3.1
+ fastapi==0.129.0
+ fastmcp==2.12.5
+ frozenlist==1.8.0
+ google-auth==2.48.0
+ google-genai==1.63.0
+ h11==0.16.0
+ htmldate==1.9.4
+ httpcore==1.0.9
+ httptools==0.7.1
+ httpx==0.28.1
+ httpx-sse==0.4.3
+ idna==3.11
+ isodate==0.7.2
+ jaraco-classes==3.4.0
+ jaraco-context==6.1.0
+ jaraco-functools==4.4.0
+ jinja2==3.1.6
+ jiter==0.13.0
+ jsonschema==4.26.0
+ jsonschema-path==0.3.4
+ jsonschema-specifications==2025.9.1
+ justext==3.0.2
+ keyring==25.7.0
+ kimi-cli==1.12.0
+ kosong==0.42.0
+ lazy-object-proxy==1.12.0
+ loguru==0.7.3
+ lxml==6.0.2
+ lxml-html-clean==0.4.3
+ markdown-it-py==4.0.0
+ markupsafe==3.0.3
+ mcp==1.16.0
+ mdurl==0.1.2
+ more-itertools==10.8.0
+ multidict==6.7.1
+ openai==2.14.0
+ openapi-core==0.22.0
+ openapi-pydantic==0.5.1
+ openapi-schema-validator==0.6.3
+ openapi-spec-validator==0.7.2
+ pathable==0.4.4
+ pillow==12.1.0
+ prompt-toolkit==3.0.52
+ propcache==0.4.1
+ pyasn1==0.6.2
+ pyasn1-modules==0.4.2
+ pycparser==3.0
+ pydantic==2.12.5
+ pydantic-core==2.41.5
+ pydantic-settings==2.13.0
+ pygments==2.19.2
+ pykaos==0.7.0
+ pyperclip==1.11.0
+ python-dateutil==2.9.0.post0
+ python-dotenv==1.2.1
+ python-multipart==0.0.22
+ pytz==2025.2
+ pywin32==311
+ pywin32-ctypes==0.2.3
+ pyyaml==6.0.3
+ referencing==0.36.2
+ regex==2026.1.15
+ requests==2.32.5
+ rfc3339-validator==0.1.4
+ rich==14.2.0
+ rich-rst==1.3.2
+ ripgrepy==2.2.0
+ rpds-py==0.30.0
+ rsa==4.9.1
+ scalar-fastapi==1.6.2
+ shellingham==1.5.4
+ six==1.17.0
+ sniffio==1.3.1
+ socksio==1.0.0
+ sse-starlette==3.2.0
+ starlette==0.52.1
+ streamingjson==0.0.5
+ tenacity==9.1.2
+ tld==0.13.1
+ tomlkit==0.14.0
+ tqdm==4.67.3
+ trafilatura==2.0.0
+ typer==0.21.1
+ typing-extensions==4.15.0
+ typing-inspection==0.4.2
+ tzdata==2025.3
+ tzlocal==5.3.1
+ urllib3==2.6.3
+ uvicorn==0.41.0
+ watchfiles==1.1.1
+ wcwidth==0.6.0
+ websockets==15.0.1
+ werkzeug==3.1.5
+ win32-setctime==1.2.0
+ yarl==1.22.0
error: Executable already exists: kimi.exe (use `--force` to overwrite)
Millard@Millards-PC MINGW64 /c/Temp-C/MQL5
$ curl -LsSf https://cdn.kimi.com/binaries/kimi-cli/install.sh --force | bash
curl: option --force: is unknown
curl: try 'curl --help' or 'curl --manual' for more information
Millard@Millards-PC MINGW64 /c/Temp-C/MQL5

### Claude · 2026-02-17 18:34

The `--force` goes to the installer, not curl. Try:

```
curl -LsSf https://cdn.kimi.com/binaries/kimi-cli/install.sh | bash -s -- --force
```

### Millard · 2026-02-17 18:34

I still get
error: Executable already exists: kimi.exe (use `--force` to overwrite)

### Claude · 2026-02-17 18:35

Find and delete it manually:

1. Run: `which kimi` or `where kimi` to find its location
2. Delete that file
3. Rerun the original curl command

### Millard · 2026-02-17 18:39

OK, deleted them, it worked, what's next?
Installed 2 executables: kimi, kimi-cli

### Claude · 2026-02-17 18:39

1. Restart VS Code
2. Check if Kimi Code extension activates without the "CLI Not Found" error

Report back.

### Millard · 2026-02-17 18:42

more than 3 minutes later...

[File attached: 1771353714048\_image.png — contents not included in export]

### Claude · 2026-02-17 18:42

Check if VS Code can find the CLI:

1. Open a new PowerShell terminal in VS Code (not Git Bash this time)
2. Run: `kimi --version`

Does it return a version number or an error?

### Millard · 2026-02-17 18:42

PS C:\Temp-C\MQL5> kimi --version
kimi, version 1.12.0
PS C:\Temp-C\MQL5>

### Claude · 2026-02-17 18:42

CLI works. Extension probably can't find it.

1. Open VS Code Settings (Ctrl+,)
2. Search "kimi"
3. Look for a setting like "CLI Path" or "Executable Path"
4. If found, set it to the output of: `where kimi` (run in PowerShell, paste the full path)

What do you see in the Kimi settings?

### Millard · 2026-02-17 18:45

it just responded

[File attached: 1771353902772\_image.png — contents not included in export]

### Claude · 2026-02-17 18:45

Good, now we know the problem. It's looking at `C:\Users\Millard\.local\bin\` but the executable might be elsewhere.

1. In PowerShell run: `where kimi`
2. Copy the full path it returns
3. Click "Open Settings" in that Kimi dialog
4. Paste the full path into `kimi.executablePath`

What does `where kimi` return?

### Millard · 2026-02-17 18:45

Millard@Millards-PC MINGW64 /c/Temp-C/MQL5
$ where kimi
C:\Users\Millard\.local\bin\kimi.exe
Millard@Millards-PC MINGW64 /c/Temp-C/MQL5

### Claude · 2026-02-17 18:46

The CLI is where the extension expects. The issue is the setting shows the directory, not the full executable path.

1. Click "Open Settings"
2. Set `kimi.executablePath` to: `C:\Users\Millard\.local\bin\kimi.exe` (include the filename)
3. Restart VS Code

### Millard · 2026-02-17 18:48

the path in settings was empty, so why didn't it use the bundled CLI. The first time I set all this up, I didn't run into this problem.

### Claude · 2026-02-17 18:49

You deleted the moonshot folders from globalStorage — that's where the bundled CLI lives. Killing it forced manual installation.

Did setting the full path fix it?

### Millard · 2026-02-17 18:51

"You deleted the moonshot folders from globalStorage — that's where the bundled CLI lives. Killing it forced manual installation."
No. I deleted it, and then we did the curl command WHICH FOUND IT AND TREATED IT LIKE AN ERROR. So, I deleted the .exes and did the curl again and it succeeded. So what you said can't be the real reason.

### Claude · 2026-02-17 18:51

You're right, that doesn't track. The kimi.exe was in `.local\bin`, not globalStorage.

I don't know why the bundled CLI failed to initialize. Could be a corruption from the crash, a version mismatch, or a bug in the extension's bootstrap logic. No way to know without seeing their source or logs.

Did setting the explicit path fix it?

### Millard · 2026-02-17 18:53

well something happened, but it's just sitting there, I tried "kimi /init" in both PS and bash and in the Kimi chat window, too. Nuthin.

[File attached: 1771354391308\_image.png — contents not included in export]

### Claude · 2026-02-17 18:53

In the Kimi chat window, type just `/init` (not "kimi /init") and press Enter.

### Millard · 2026-02-17 18:54

I did both

### Claude · 2026-02-17 18:54

Check VS Code's Output panel:

1. View → Output (or Ctrl+Shift+U)
2. In the dropdown on the right side of the Output panel, look for "Kimi" or "Kimi Code"
3. See if there are any errors logged

What does it show?

### Millard · 2026-02-17 18:55

I also just typed slash, got what you see, clicked on the /init item.
Nuthin, just sits there.

[File attached: 1771354493295\_image.png — contents not included in export]

### Claude · 2026-02-17 18:56

That's a different issue than before — the extension is responding to input now.

Did you check the Output panel? (Ctrl+Shift+U, then select "Kimi" or "Kimi Code" from the dropdown on the right)

### Millard · 2026-02-17 18:57

```log
2026-02-17 12:56:14.912 [info] Extension host with pid 17852 started
2026-02-17 12:56:14.912 [info] Skipping acquiring lock for c:\Users\Millard\AppData\Roaming\Code\User\workspaceStorage\e154246849c79ead3ac06b6ecc23a1e6.
2026-02-17 12:56:15.057 [info] ExtensionService#\_doActivateExtension vscode.github-authentication, startup: false, activationEvent: 'onAuthenticationRequest:github'
2026-02-17 12:56:15.085 [info] ExtensionService#\_doActivateExtension mechatroner.rainbow-csv, startup: false, activationEvent: 'onLanguage:plaintext'
2026-02-17 12:56:15.090 [info] ExtensionService#\_doActivateExtension vscode.emmet, startup: false, activationEvent: 'onLanguage'
2026-02-17 12:56:15.110 [info] ExtensionService#\_doActivateExtension moonshot-ai.kimi-code, startup: false, activationEvent: 'onView:kimi.webview'
2026-02-17 12:56:15.937 [info] ExtensionService#\_doActivateExtension vscode.git-base, startup: true, activationEvent: '\*', root cause: vscode.git
2026-02-17 12:56:15.964 [info] ExtensionService#\_doActivateExtension vscode.git, startup: true, activationEvent: '\*'
2026-02-17 12:56:16.037 [info] ExtensionService#\_doActivateExtension vscode.github, startup: true, activationEvent: '\*'
2026-02-17 12:56:16.154 [info] ExtensionService#\_doActivateExtension ms-vscode.cpptools, startup: true, activationEvent: 'workspaceContains:{\*\*/\*.mqh,\*\*/\*.mq4,\*\*/\*.mq5}', root cause: L-I-V.mql-tools
2026-02-17 12:56:16.594 [info] ExtensionService#\_doActivateExtension vscode.terminal-suggest, startup: false, activationEvent: 'onTerminalShellIntegration:\*'
2026-02-17 12:56:17.689 [info] ExtensionService#\_doActivateExtension L-I-V.mql-tools, startup: true, activationEvent: 'workspaceContains:{\*\*/\*.mqh,\*\*/\*.mq4,\*\*/\*.mq5}'
2026-02-17 12:56:18.130 [info] Eager extensions activated
2026-02-17 12:56:18.150 [info] ExtensionService#\_doActivateExtension vscode.debug-auto-launch, startup: false, activationEvent: 'onStartupFinished'
2026-02-17 12:56:18.154 [info] ExtensionService#\_doActivateExtension vscode.merge-conflict, startup: false, activationEvent: 'onStartupFinished'
```

### Claude · 2026-02-17 18:57

That's the Extension Host log. Look in the dropdown for a channel specifically named "Kimi" or "Kimi Code" — it should have its own output channel separate from the general extension host.

### Millard · 2026-02-17 18:57

```mql-output
[2026-02-17T18:56:15.167Z] Kimi Code extension activating...
[2026-02-17T18:56:15.174Z] Kimi extension activated
2026-02-17T18:56:16.710Z kimi-sdk:protocol Spawning CLI: C:\Users\Millard\.local\bin\kimi.exe [ '--work-dir', 'c:\\Temp-C\\MQL5', '--wire', '--no-thinking' ]
2026-02-17T18:56:16.753Z kimi-sdk:protocol Sending initialize request: {
protocol\_version: '1.3',
client: { name: 'kimi-agent-sdk/0.1.4', version: '0.1.4' }
}
2026-02-17T18:56:16.754Z kimi-sdk:protocol >>> {
jsonrpc: '2.0',
id: '1\_1771354576753',
method: 'initialize',
params: {
protocol\_version: '1.3',
client: { name: 'kimi-agent-sdk/0.1.4', version: '0.1.4' }
}
}
```

### Claude · 2026-02-17 18:57

The CLI spawned and received the initialize request but never responded. It's hanging.

Try authenticating directly via CLI:

1. Open PowerShell terminal
2. Run: `kimi auth login` or `kimi login`

See if it prompts you to authenticate.

### Millard · 2026-02-17 18:59

"kimi login" just sits there, too

### Claude · 2026-02-17 18:59

Try with verbose output:

```
kimi --verbose login
```

or

```
kimi -v login
```

If that doesn't give more info, check if something is blocking it:

```
kimi --help
```

Does `--help` respond or also hang?

### Millard · 2026-02-17 19:01

well, at least --help didn't hangAttached file: unnamed

```
C:\Temp-C\MQL5> kimi --help
                                                                                     
 Usage: kimi [OPTIONS] COMMAND [ARGS]...                                             
                                                                                     
 Kimi, your next CLI agent.

╭─ Options ─────────────────────────────────────────────────────────────────────────╮
│ --version           -V                                         Show version and   │
│                                                                exit.              │
│ --verbose                                                      Print verbose      │
│                                                                information.       │
│                                                                Default: no.       │
│ --debug                                                        Log debug          │
│                                                                information.       │
│                                                                Default: no.       │
│ --work-dir          -w                      DIRECTORY          Working directory  │
│                                                                for the agent.     │
│                                                                Default: current   │
│                                                                directory.         │
│ --session           -S                      TEXT               Session ID to      │
│                                                                resume for the     │
│                                                                working directory. │
│                                                                Default: new       │
│                                                                session.           │
│ --continue          -C                                         Continue the       │
│                                                                previous session   │
│                                                                for the working    │
│                                                                directory.         │
│                                                                Default: no.       │
│ --config                                    TEXT               Config TOML/JSON   │
│                                                                string to load.    │
│                                                                Default: none.     │
│ --config-file                               FILE               Config TOML/JSON   │
│                                                                file to load.      │
│                                                                Default:           │
│                                                                ~/.kimi/config.to… │
│ --model             -m                      TEXT               LLM model to use.  │
│                                                                Default: default   │
│                                                                model set in       │
│                                                                config file.       │
│ --thinking                 --no-thinking                       Enable thinking    │
│                                                                mode. Default:     │
│                                                                default thinking   │
│                                                                mode set in config │
│                                                                file.              │
│ --yolo,--yes,--au…  -y                                         Automatically      │
│                                                                approve all        │
│                                                                actions. Default:  │
│                                                                no.                │
│ --prompt,--command  -p,-c                   TEXT               User prompt to the │
│                                                                agent. Default:    │
│                                                                prompt             │
│                                                                interactively.     │
│ --print                                                        Run in print mode  │
│                                                                (non-interactive). │
│                                                                Note: print mode   │
│                                                                implicitly adds    │
│                                                                `--yolo`.          │
│ --acp                                                          (Deprecated, use   │
│                                                                `kimi acp`         │
│                                                                instead) Run as    │
│                                                                ACP server.        │
│ --wire                                                         Run as Wire server │
│                                                                (experimental).    │
│ --input-format                              [text|stream-json  Input format to    │
│                                             ]                  use. Must be used  │
│                                                                with `--print` and │
│                                                                the input must be  │
│                                                                piped in via       │
│                                                                stdin. Default:    │
│                                                                text.              │
│ --output-format                             [text|stream-json  Output format to   │
│                                             ]                  use. Must be used  │
│                                                                with `--print`.    │
│                                                                Default: text.     │
│ --final-message-o…                                             Only print the     │
│                                                                final assistant    │
│                                                                message (print     │
│                                                                UI).               │
│ --quiet                                                        Alias for `--print │
│                                                                --output-format    │
│                                                                text               │
│                                                                --final-message-o… │
│ --agent                                     [default|okabe]    Builtin agent      │
│                                                                specification to   │
│                                                                use. Default:      │
│                                                                builtin default    │
│                                                                agent.             │
│ --agent-file                                FILE               Custom agent       │
│                                                                specification      │
│                                                                file. Default:     │
│                                                                builtin default    │
│                                                                agent.             │
│ --mcp-config-file                           FILE               MCP config file to │
│                                                                load. Add this     │
│                                                                option multiple    │
│                                                                times to specify   │
│                                                                multiple MCP       │
│                                                                configs. Default:  │
│                                                                none.              │
│ --mcp-config                                TEXT               MCP config JSON to │
│                                                                load. Add this     │
│                                                                option multiple    │
│                                                                times to specify   │
│                                                                multiple MCP       │
│                                                                configs. Default:  │
│                                                                none.              │
│ --skills-dir                                DIRECTORY          Path to the skills │
│                                                                directory.         │
│                                                                Overrides          │
│                                                                discovery.         │
│ --max-steps-per-t…                          INTEGER RANGE      Maximum number of  │
│                                             [x>=1]             steps in one turn. │
│                                                                Default: from      │
│                                                                config.            │
│ --max-retries-per…                          INTEGER RANGE      Maximum number of  │
│                                             [x>=1]             retries in one     │
│                                                                step. Default:     │
│                                                                from config.       │
│ --max-ralph-itera…                          INTEGER RANGE      Extra iterations   │
│                                             [x>=-1]            after the first    │
│                                                                turn in Ralph      │
│                                                                mode. Use -1 for   │
│                                                                unlimited.         │
│                                                                Default: from      │
│                                                                config.            │
│ --help              -h                                         Show this message  │
│                                                                and exit.          │
╰───────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────╮
│ login    Login to your Kimi account.                                              │
│ logout   Logout from your Kimi account.                                           │
│ term     Run Toad TUI backed by Kimi Code CLI ACP server.                         │
│ acp      Run Kimi Code CLI ACP server.                                            │
│ info     Show version and protocol information.                                   │
│ mcp      Manage MCP server configurations.                                        │
│ web      Run Kimi Code CLI web interface.                                         │
╰───────────────────────────────────────────────────────────────────────────────────╯

 Documentation:        https://moonshotai.github.io/kimi-cli/
 LLM friendly version: https://moonshotai.github.io/kimi-cli/llms.txt
```

[File attached: unnamed — contents not included in export]

### Claude · 2026-02-17 19:01

Try:

```
kimi --verbose login
```

or

```
kimi --debug login
```

See if it shows what it's waiting on.

### Millard · 2026-02-17 19:02

kimi --verbose login just hanged

### Claude · 2026-02-17 19:02

Try:

```
kimi --debug login
```

If that also hangs with no output, check if it's trying to open a browser:

* Is there a browser window or popup you might have missed?
* Any firewall/antivirus that might be blocking network access?

### Millard · 2026-02-17 19:02

kimi --debug login just hangs

### Claude · 2026-02-17 19:02

Check if it's a network issue:

```
curl -I https://kimi.moonshot.cn
```

or

```
ping kimi.moonshot.cn
```

Also: is there a browser window trying to open somewhere? The login might be waiting for OAuth callback.

### Millard · 2026-02-17 19:04

kimi --debug login is still hung

### Claude · 2026-02-17 19:04

Kill it (Ctrl+C) and check network connectivity:

```
curl -I https://kimi.moonshot.cn
```

Does that return anything or also hang?

### Millard · 2026-02-17 19:04

Ctrl-C does nothing. I've been having to close the terminal window.

### Claude · 2026-02-17 19:04

Open a new terminal and test network:

```
curl -I https://kimi.moonshot.cn
```

Also check if kimi processes are piling up:

```
tasklist | findstr kimi
```

### Millard · 2026-02-17 19:05

Being so clear and exacting again are you? WTF IS:
tasklist | findstr kimi

### Claude · 2026-02-17 19:05

`tasklist` lists all running processes on Windows. `findstr kimi` filters to only show lines containing "kimi".

The command checks if you have multiple hung kimi.exe processes stacking up from your attempts.

### Millard · 2026-02-17 19:06

How can you be so obtuse. WHAT DO I DO WITH THAT? Write it in notepad. Click start and type it? in a PS terminal window. bash? Kimi chat?
WHAT THE FUCK DUDE. YOU WASTE SO MUCH OF MY FUCKING TIME.

### Claude · 2026-02-17 19:07

You're right. I'll be explicit.

1. Open a new PowerShell terminal in VS Code (the dropdown, select PowerShell)
2. Run: `tasklist | findstr kimi`
3. Run: `curl -I https://kimi.moonshot.cn`

Tell me what both return.

### Millard · 2026-02-17 19:08

PS C:\Temp-C\MQL5> tasklist | findstr kimi
JUST HANGS

### Claude · 2026-02-17 19:08

Try just:

```
tasklist
```

Does that hang too, or does it list processes?

### Millard · 2026-02-17 19:08

hangs

### Claude · 2026-02-17 19:08

That's a system-level problem, not Kimi. `tasklist` is a basic Windows command.

1. Close VS Code entirely
2. Open PowerShell directly from Start Menu (not inside VS Code)
3. Run: `tasklist`

Does it hang there too?

### Millard · 2026-02-17 19:10

hangs in a command prompt too. Guess I need to restart Windows.

### Claude · 2026-02-17 19:11

Yes. Restart Windows, then try `kimi login` in PowerShell again. Report back.

### Millard · 2026-02-17 19:25

C:\Windows\System32>tasklist | findstr kimi
C:\Windows\System32>

### Claude · 2026-02-17 19:25

No hung processes. Now try:

```
kimi login
```

### Millard · 2026-02-17 19:27

C:\Windows\System32>kimi login
Please visit the following URL to finish authorization.
Verification URL: https://www.kimi.com/code/authorize\_device?user\_code=FBTH-MWVG
Logged in successfully.
C:\Windows\System32>

### Claude · 2026-02-17 19:27

Good. Now:

1. Open VS Code
2. Check if Kimi Code extension loads without hanging

### Millard · 2026-02-17 19:28

kimi seems to be working now, /init got it going

### Claude · 2026-02-17 19:28

Good. Done.
