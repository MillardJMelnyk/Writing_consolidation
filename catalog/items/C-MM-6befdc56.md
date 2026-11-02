# Identifying startup processes and logs

| | |
|---|---|
| Date | 2026-09-26 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-6befdc56` |
| Links | [Original](https://claude.ai/chat/6befdc56-2770-42b2-a917-fa117de08cef) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-09-26_identifying-startup-processes-and-logs_6befdc56.html) |

**Summary:** Logging which programs launch black console windows at Windows startup, and how Path of Exile support gems must be linked.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; Games, movies and entertainment > Path of Exile

**Index terms:** process creation auditing; Event ID 4688; PowerShell; startup program; support gem; linked socket

[← Catalog home](../README.md)

---

### Millard · 2026-09-26 22:02

is there a command i can runa fter starting my computer that checks the logs to see what is opening when startyup happens? Justa bunch of black boxes pop up on startup and i want to know what they are

### Claude · 2026-09-26 22:02

Windows doesn't log what starts at boot by default, so you have to turn that logging on once, reboot, then read the log. This assumes the boxes appear in Windows, not Fedora.

**One-time setup** (PowerShell as Administrator):

```
auditpol /set /subcategory:"Process Creation" /success:enable
```

```
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\Audit /v ProcessCreationIncludeCmdLine_Enabled /t REG_DWORD /d 1 /f
```

**After each reboot**, once the boxes have appeared (PowerShell as Administrator):

```
Get-WinEvent -FilterHashtable @{LogName='Security';Id=4688;StartTime=(Get-Date).AddMinutes(-15)} | Select-Object TimeCreated,@{n='Program';e={$_.Properties[5].Value}},@{n='CommandLine';e={$_.Properties[8].Value}},@{n='LaunchedBy';e={$_.Properties[13].Value}} | Sort-Object TimeCreated | Out-GridView
```

A sortable window opens listing every program started in the last 15 minutes. The black boxes will show as `cmd.exe`, `powershell.exe`, or `conhost.exe` rows. The **CommandLine** column shows what each one ran, and **LaunchedBy** shows what started it.

**No setup needed**, but this only shows what's scheduled to start, not a log of what actually ran:

```
Get-CimInstance Win32_StartupCommand | Select-Object Name,Command,Location | Out-GridView
```

### Millard · 2026-09-26 22:11

.in path of exile do support gems need to be linked to the gem it supports via a weapon or amor or can i place them in any open socket?

### Claude · 2026-09-26 22:11

It depends on which game you mean.

In **Path of Exile 1**, support gems must go in a socket that's linked to the skill gem, on the same item. Linked sockets are the ones joined by a bar. An open socket that isn't linked does nothing for the skill.

In **Path of Exile 2**, there are no item links. Support gems go directly into the skill gem's own sockets, which you open in the skill gem panel.
