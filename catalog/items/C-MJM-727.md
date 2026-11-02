# Windows backup exclusion lists

| | |
|---|---|
| Date | 2026-08-07 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-727` |
| Links | [Original](https://claude.ai/chat/93b034b2-1250-4211-b9ad-6313bc328213) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/727-2026-08-07-windows-backup-exclusion-lists.html) |

**Summary:** Lists of Windows file extensions and folders to exclude from a backup compare, using a whitelist of user folders.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** backup; file exclusion list; Windows folders; whitelist; file comparison

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-08-07 18:35

give me a list of Windows file extensions to exclude from a folder file compare -- things that you'd typically not care about backing up.
In the form \*.xxx, one per line
Also give me a list of file folders to exclude, such as the \Windows and program file folders, and user folders that don't need to be backed up in order to preserve work I've done.

### Claude · 2026-08-07 18:35

Timestamp: facts below reflect common Windows conventions as of 2026; no single canonical list exists—verify against your own OS/app version before relying on it.

**Extensions to exclude:**

```
*.tmp
*.temp
*.bak
*.old
*.log
*.cache
*.chk
*.dmp
*.mdmp
*.etl
*.gid
*.ds_store
*.thumbs.db
*.lnk
*.ini
*.cab
*.msi
*.msp
*.crdownload
*.part
*.partial
*.download
*.swp
*.swo
*.~
*.~lock
*.pf
*.evtx
*.wer
*.searchindex
*.blf
*.regtrans-ms
*.tlog
*.pch
*.obj
*.ilk
*.pdb
*.idb
*.suo
*.user
*.sdf
*.opendb
```

**Folders to exclude:**

```
C:\Windows
C:\Program Files
C:\Program Files (x86)
C:\ProgramData
C:\$Recycle.Bin
C:\System Volume Information
C:\Recovery
C:\PerfLogs
C:\Users\<user>\AppData\Local\Temp
C:\Users\<user>\AppData\Local\Microsoft\Windows
C:\Users\<user>\AppData\Local\Packages
C:\Users\<user>\AppData\Local\CrashDumps
C:\Users\<user>\AppData\Local\Microsoft\Edge
C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\Cache
C:\Users\<user>\AppData\Local\Microsoft\OneDrive\logs
C:\Users\<user>\AppData\LocalLow
C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Recent
C:\Users\<user>\NTUSER.DAT*
C:\Users\Default
C:\Users\Public\Desktop (unless you deliberately store work there)
C:\Windows.old
```

Note: `AppData\Roaming` is not blanket-excludable — some apps (e.g., code editors, Git config, license files) store real user config there. Filter that one manually if you need it.

### Millard · 2026-08-07 18:36

I'm not interested in configurations, just work

### Claude · 2026-08-07 18:36

**Extensions to exclude — add these to the earlier list:**

```
*.ini
*.cfg
*.config
*.reg
*.manifest
*.pol
```

(These duplicate/extend what's already excluded — ini already listed.)

**Folders to exclude — add to the earlier list:**

```
C:\Users\<user>\AppData (entire folder, all subfolders)
C:\Users\<user>\.config
C:\Users\<user>\.vscode
C:\Users\<user>\.git (global config only, not repo working files)
C:\Users\<user>\NTUSER.DAT*
C:\Users\<user>\ntuser.ini
```

Rationale: excluding the entire `AppData` tree removes all app config/state/cache in one shot, since none of it is "work" — it's settings, license tokens, and app plumbing. This supersedes the earlier partial `AppData` exclusions (Temp, Local\Microsoft\Windows, etc.) — just exclude the whole tree instead of picking subfolders.

Caveat: if any of your MQL5/Python tooling stores project files under `AppData\Roaming` (some editors do, e.g. portable-app configs with embedded scripts) rather than in a normal project directory, blanket exclusion will drop that. You'd need to check case-by-case — I have no visibility into where your specific tools write.

### Millard · 2026-08-07 18:36

give me a complete list

### Claude · 2026-08-07 18:36

Timestamp: as of 2026-08-07; verify against your OS/app versions.

**Extensions to exclude:**

```
*.tmp
*.temp
*.bak
*.old
*.log
*.cache
*.chk
*.dmp
*.mdmp
*.etl
*.gid
*.lnk
*.ini
*.cfg
*.config
*.reg
*.manifest
*.pol
*.cab
*.msi
*.msp
*.crdownload
*.part
*.partial
*.download
*.swp
*.swo
*.~
*.~lock
*.pf
*.evtx
*.wer
*.searchindex
*.blf
*.regtrans-ms
*.tlog
*.pch
*.obj
*.ilk
*.pdb
*.idb
*.suo
*.user
*.sdf
*.opendb
*.ds_store
*.thumbs.db
```

**Folders to exclude:**

```
C:\Windows
C:\Windows.old
C:\Program Files
C:\Program Files (x86)
C:\ProgramData
C:\$Recycle.Bin
C:\System Volume Information
C:\Recovery
C:\PerfLogs
C:\Users\Default
C:\Users\<user>\AppData
C:\Users\<user>\.config
C:\Users\<user>\.vscode
C:\Users\<user>\NTUSER.DAT*
C:\Users\<user>\ntuser.ini
```

Note: `.git` config removed from prior list — a global `.gitconfig` file is ~1KB, not a folder, and excluding `.git` risks catching repo working files if misapplied. If you want it excluded specifically, target `C:\Users\<user>\.gitconfig` as a file, not a folder pattern.

Unresolved: whether your MQL5/Python tooling writes project files into `AppData\Roaming` — I don't have visibility into your specific tool configs. If any editor/framework stores actual work product there (not just settings), that data is dropped by this exclusion list.

### Millard · 2026-08-07 18:38

OK, for the folders, I think I want to exclude all \users\ folders/files, then include only the ones under my user name that will have meaningful data I should save.

### Claude · 2026-08-07 18:38

**Exclude:**

```
C:\Users
```

**Then include only these under your username (C:\Users<user>...):**

```
C:\Users\<user>\Documents
C:\Users\<user>\Desktop
C:\Users\<user>\Downloads
C:\Users\<user>\Pictures
C:\Users\<user>\Videos
C:\Users\<user>\Music
C:\Users\<user>\OneDrive (if used for active work, not just sync cache)
```

Everything else under `\Users\<user>\` (AppData, Contacts, Favorites, Links, Saved Games, Searches, NTUSER.DAT\*, .vscode, .config, etc.) stays excluded by default under this scheme.

Gap: if your MQL5/Python dev work lives in a custom path like `C:\Users\<user>\Projects` or `C:\Users\<user>\source\repos`, that's not in the default list above — I have no visibility into where you actually keep it. Confirm your project root(s) and I'll add them.

### Millard · 2026-08-07 18:38

I'll worry about that on an exception basis, as long as I'm catching everything else

### Claude · 2026-08-07 18:38

Confirmed — exclude-`C:\Users`-then-include-specific-subfolders is a whitelist approach: nothing new can silently slip through, since anything not explicitly included stays excluded by default. That structurally satisfies "catching everything else" for the folder scope — the only risk is a future subfolder you forget to add, not one that leaks past you unnoticed.
