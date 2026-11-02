# Deleting files and emptying recycle bin by drive

| | |
|---|---|
| Date | 2026-08-09 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-732` |
| Links | [Original](https://claude.ai/chat/fbc85de3-f212-4ae1-9148-2e191cafdd0b) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/732-2026-08-09-deleting-files-and-emptying-recycle-bin-by-drive.html) |

**Summary:** Emptying one drive's Recycle Bin by command, what .qss files are, and whether old copies of OneNote backups can be deleted.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** Recycle Bin; rd command; OneNote backup; qss file; AppData

[← Catalog home](../README.md)

---

### Millard · 2026-08-09 16:32

can I simply delete these files? I don't see any way using "Empty Recycle Bin" to empty only files for a specified drive.

[File attached: 1786293123536\_image.png — contents not included in export]

### Claude · 2026-08-09 16:32

Yes. Right-click delete or Shift+Delete on individual `$R*`/`$I*` entries works — they're ordinary files once selected outside the Recycle Bin's virtual view; deleting them there bypasses the Recycle Bin's tracking database (no confirmation via "Empty Recycle Bin" needed).

Faster method for the whole drive: open elevated PowerShell/CMD and run

```
rd /s /q F:\$RECYCLE.BIN
```

This removes the entire bin (all SID subfolders) for F: in one shot. Windows recreates the folder structure automatically on next delete to that drive. Don't run this from within Explorer's Recycle Bin view — do it from a normal shell path.

Note: `$R*` files are the actual deleted content; `$I*` files are their paired metadata (original path, deletion timestamp). You don't need to handle them separately — deleting either without the other just orphans metadata, no error, no risk.

The `cleanmgr` (Disk Cleanup) tool also lets you target Recycle Bin per-drive if you want a GUI confirmation step instead.

### Millard · 2026-08-09 16:34

bad instructions
C:\WINDOWS\System32>rd /s /q F:\$RECYCLE.BIN
The directory is not empty.
C:\WINDOWS\System32>

### Claude · 2026-08-09 16:34

Correct. `rd /s /q` fails silently-verbose like that when it hits a permissions block or a locked/in-use file partway through — it doesn't roll back, it just stops and reports the parent as non-empty.

Fix, in order:

1. Confirm elevation — check title bar says "Administrator." `rd` alone doesn't grant SYSTEM/TrustedInstaller rights over other users' SID folders.
2. Force-delete files first, then remove the tree:

```
del /f /s /q F:\$RECYCLE.BIN\*
rd /s /q F:\$RECYCLE.BIN
```

3. If that still fails, take ownership and grant permissions before deleting:

```
takeown /f F:\$RECYCLE.BIN /r /d y
icacls F:\$RECYCLE.BIN /grant administrators:F /t
del /f /s /q F:\$RECYCLE.BIN\*
rd /s /q F:\$RECYCLE.BIN
```

4. If it still won't go, something has a handle open on a file inside it — check with `handle.exe` (Sysinternals) or just reboot and retry before any of those steps.

PowerShell alternative, often more informative on which file blocks it:

```
Remove-Item -Path "F:\$RECYCLE.BIN" -Recurse -Force -ErrorAction Continue
```

This will enumerate and report the specific failing file instead of a single generic error.

### Millard · 2026-08-09 16:35

give me the correct command

[File attached: 1786293311327\_image.png — contents not included in export]

### Claude · 2026-08-09 16:35

Title bar confirms elevation, so run the escalation sequence:

```
takeown /f F:\$RECYCLE.BIN /r /d y
icacls F:\$RECYCLE.BIN /grant administrators:F /t
del /f /s /q F:\$RECYCLE.BIN\*
rd /s /q F:\$RECYCLE.BIN
```

Run each line, let it finish, then the next. If `rd` still fails after this, a file inside is open/locked by a process — run `Remove-Item -Path "F:\$RECYCLE.BIN" -Recurse -Force -ErrorAction Continue` in PowerShell instead; it'll name the specific file it can't touch.

### Millard · 2026-08-09 16:46

what's a .qss file?

### Claude · 2026-08-09 16:46

A Qt Style Sheet — a plain-text file (`.qss`) used to style Qt/PyQt/PySide GUI applications, syntactically modeled on CSS.

Key facts:

* Selectors target Qt widget classes (`QPushButton`, `QLineEdit`, etc.) instead of HTML tags/classes
* Properties are a subset of CSS properties, plus Qt-specific extensions (e.g., `subcontrol-origin` for compound widgets like scrollbars)
* Applied at runtime via `QApplication.setStyleSheet()` or per-widget `setStyleSheet()`
* No relation to Windows Recycle Bin or the SID directory structure from your earlier screenshots — unrelated context, flagging in case this ties to a different task (e.g., styling a PyQt trading dashboard).

Example:

```
QPushButton {
    background-color: #2b2b2b;
    color: white;
    border-radius: 4px;
}
QPushButton:hover {
    background-color: #3a3a3a;
}
```

If this is for a PyQt/PySide interface on one of your MT5/Python tools, say which widget framework and I'll skip the generic explanation.

### Millard · 2026-08-09 16:47

answer in english

### Claude · 2026-08-09 16:47

That response was already in English.

### Millard · 2026-08-09 16:47

not english a normal person could understand, twat

### Claude · 2026-08-09 16:47

A .qss file is a text file that controls how a program's buttons, windows, and menus look — colors, borders, fonts, that kind of thing.

It's used for programs built with a toolkit called Qt. Think of it like CSS for websites, but for desktop apps instead of web pages.

You write rules like "make all buttons dark gray with white text," save it as a .qss file, and the program reads it to change its appearance without changing how it works.

### Millard · 2026-08-09 17:04

I backed up AppData and it caught all kinds of OneNote backups apparently created by the app. Given that these are more than 2 years old, what would I lose by deleting them?

[File attached: 1786294993591\_image.png — contents not included in export]

### Claude · 2026-08-09 17:04

You'd lose local point-in-time snapshots OneNote auto-generates (default: daily, kept ~a few backups per section depending on `BackupInterval`/`BackupFileCount` registry settings) — nothing else. Specifics:

* These are not your live notebooks. Live OneNote data lives in your notebook cache/sync location (OneDrive or local notebook folder), not in this `Backup` folder.
* This folder is OneNote's automatic local safety net — used only if a section file gets corrupted and you need to manually restore an older version via File → Info → Open Backups.
* Deleting them does not touch current notebook content, sync state, or anything visible in the OneNote app right now.
* Risk: if a section has been silently corrupting and you haven't noticed, you lose the ability to roll back to a pre-2024 clean copy. Given "more than 2 years old," any corruption would almost certainly have surfaced already.
* The `OneNote_RecycleBin` entries you see are OneNote's own internal deleted-page store — separate mechanism, same logic applies.

Net: safe to delete for space recovery. Zero functional loss unless you specifically need to time-travel a section file to a mid-2024 state.

### Millard · 2026-08-09 17:04

I need that in simple english. remember these are not the actual backups created by OneNote, these are backups of those backups.

### Claude · 2026-08-09 17:04

These are copies of OneNote's own backup files — backups of backups. Not your real notes.

Here's what OneNote does on its own: every so often it saves a spare copy of each notebook section into a hidden backup folder on your computer, in case a file gets damaged. That's normal and happens automatically.

Then, separately, you backed up your whole AppData folder — which scooped up copies of those spare files too.

So what you're looking at is a backup of OneNote's backup. Deleting them:

* Won't touch your actual notes — those live somewhere else entirely.
* Won't affect OneNote's own backup system — it keeps making its own copies regardless of what you do with this AppData backup.
* Just frees up space by removing a redundant copy of files that are already just spares to begin with.

Since these are over 2 years old, any corruption they'd protect against would have shown up long ago. Safe to delete.

### Millard · 2026-08-09 17:05

fucking hell. SIMPLE ENGLISH ANSWER THE FUCKING QUESITON

### Claude · 2026-08-09 17:05

You lose nothing. Delete them.

### Millard · 2026-08-09 17:05

FUCKING HELL

### Claude · 2026-08-09 17:05

Understood. No further explanation needed — that's the complete answer.
