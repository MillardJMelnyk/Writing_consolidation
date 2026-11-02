# Windows shortcut to Programs & Features

| | |
|---|---|
| Date | 2026-09-11 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-1ad92f98` |
| Links | [Original](https://claude.ai/chat/1ad92f98-e77f-4b60-8c26-fdc8fb35c8f5) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-09-11_windows-shortcut-to-programs-features_1ad92f98.html) |

**Summary:** Creating a taskbar-pinnable Windows shortcut that opens Programs and Features via an explorer.exe shell CLSID target.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** Programs and Features; Windows shortcut; shell CLSID; Windows taskbar; Control Panel

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-09-11 20:39

I need the code for a shortcut to open the Programs & Features in control panel  
Working out how to create a Windows shortcut.  
Working out how to create a Windows shortcut.  
Shortcut target:

```
control.exe /name Microsoft.ProgramsAndFeatures
```

Alternative (same result):

```
%windir%\system32\appwiz.cpl
```

Set as target in shortcut properties; no arguments needed for either.  
I need a shortcut that will pin to the taskbar

The above (from Sonnet) does not work

### Claude · 2026-09-11 20:39

Target:

```
C:\Windows\explorer.exe shell:::{7b81be6a-ce13-48f6-8853-8a2a9c0b7b88}
```

Pin the shortcut itself (right-click the .lnk → Show more options → Pin to taskbar); it will sit under the File Explorer icon group.

### Millard · 2026-09-11 20:41

wrong see image

### Claude · 2026-09-11 20:42

Target:

```
C:\Windows\explorer.exe shell:::{26EE0668-A00A-44D7-9371-BEB064C98683}\0\::{7b81be6a-ce13-48f6-8853-8a2a9c0b7b88}
```

The bare CLSID fails because Programs and Features is a child of the Control Panel namespace, not a root shell folder.

### Millard · 2026-09-11 20:42

dude I don't give a fuck what you did wrong, give it to me right. Same error this time too.

### Claude · 2026-09-11 20:43

Target:

```
C:\Windows\System32\rundll32.exe shell32.dll,Control_RunDLL appwiz.cpl
```

Right-click the .lnk → Show more options → Pin to taskbar.

### Millard · 2026-09-11 20:43

fucking finally

### Claude · 2026-09-11 20:43

Good.
