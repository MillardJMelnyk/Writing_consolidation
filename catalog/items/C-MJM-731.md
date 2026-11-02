# Windows error 5 in dupeGuru

| | |
|---|---|
| Date | 2026-08-09 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-731` |
| Links | [Original](https://claude.ai/chat/d6a542b3-d4cd-44ba-b9ba-69fc1e2ed9e1) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/731-2026-08-09-windows-error-5-in-dupeguru.html) |

**Summary:** dupeGuru Windows error 5 on OneNote cache files, what .dml and cache files are, and whether an old Windows system image is still useful.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** dupeGuru; access denied; OneNote cache; WindowsImageBackup; system image

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-08-09 15:43

using dupeGuru, what is Windows error 5

[File attached: 1786290233465\_image.png — contents not included in export]

### Claude · 2026-08-09 15:44

WinError 5 = ERROR\_ACCESS\_DENIED. The process lacks NTFS permissions to read/delete those OneNote cache files — typically because they're owned by SYSTEM/TrustedInstaller, locked by another process (OneNote/search indexer), or you're not running dupeGuru elevated.

Fix: close OneNote, run dupeGuru as Administrator, or take ownership of the `OneNote Cache` folder (icacls / Properties→Security→Advanced).

### Millard · 2026-08-09 15:46

does deleting onenote cache data clobber the actual OneNote data in the .one files?

### Claude · 2026-08-09 15:46

No. The OneNote Cache folder (`%LOCALAPPDATA%\Microsoft\OneNote\<version>\OneNoteOfflineCache_Files` or similar) stores the sync engine's local working copy/transaction logs used to reconcile with OneDrive/SharePoint — it's derived data, not the canonical store.

The actual notebook content lives in the `.one`/`.onetoc2` files themselves (local notebooks) or server-side (cloud notebooks), separate from that cache directory.

Risk profile:

* **Local-only notebooks**: cache deletion is safe: `.one` files are the source of truth.
* **Synced (OneDrive/SharePoint) notebooks**: safe if fully synced at deletion time. OneNote rebuilds the cache from the server on next launch. If there are unsynced pending changes, those changes can be lost — the cache is where unsynced edits live until upload completes.

Check sync status (all notebooks green/synced) before deleting, or don't delete while OneNote is running mid-edit.

### Millard · 2026-08-09 15:47

So, given all those errors were for files in a backup copy, it would be safe to delete them?

### Claude · 2026-08-09 15:47

Yes, on two conditions:

1. It's not being actively read/synced by a running OneNote instance (it's inert backup data, not a live cache) — access denial itself confirms it's not the live cache path, but check nothing has that backup drive/folder open.
2. You don't need that snapshot for anything other than dedup purposes — deleting it just removes stale sync-engine data from a point-in-time backup, not primary notebook content, which is unaffected regardless.

The WinError 5 is blocking dupeGuru's *deletion*, not indicating anything about data integrity. To actually delete: take ownership/grant permissions on that folder tree, or run elevated.

### Millard · 2026-08-09 18:02

what's a .dml file?

### Claude · 2026-08-09 18:02

No single fixed format — extension is overloaded across unrelated applications. Documented uses:

* **DynaScript web page**: dynamic HTML script, syntax comparable to ASP/ColdFusion created with DyanScript, a dynamic HTML scripting language compatible with ECMAScript, similar to ColdFusion code and Microsoft Active Server Pages.
* **WD (Western Digital) backup software**: Data Manipulation Language File used in WD's backup/sync tools — most likely candidate given your context (backup drive consolidation).
* **Drillbench**: Drilling engineering markup language file format used by Drillbench, a dynamic drilling simulation software — irrelevant to you.
* **Moderieren (teambits)**: meeting script used by Moderieren online event organization and management web application, saved as XML-encoded markup — irrelevant.
* **Medical Manager**: legacy healthcare system script — irrelevant.

If you have a specific `.dml` file in front of you: post its path/parent folder, or run `file <name>.dml` / open in a text editor and paste the header bytes — that'll disambiguate instead of guessing from extension alone.

### Millard · 2026-08-09 18:04

[File attached: 1786298694559\_image.png — contents not included in export]

### Claude · 2026-08-09 18:05

Path: `...\Sync.4.0.deposit\a\`. Sequentially numbered `.dml` files, 13-108 KB, no readable names.

That's the signature of **SyncBackSE/SyncBackPro** (2BrightSparks) deposit/history format — the `Sync.X.X.deposit` folder naming is specific to it, not WD or DynaScript. Under "history"/"deposit" mode, SyncBack stores versioned file backups renamed to sequential numeric IDs, with the mapping between original filename↔numbered file kept in a separate index/database (often `.dat` or embedded in the sync job's history log elsewhere in that tree).

To confirm: check for an accompanying index file in the same folder or parent (`Sync.4.0.deposit` root) — SyncBack typically keeps one nearby. Without it, these numbered `.dml` files are orphaned/unmappable back to original names.

### Millard · 2026-08-09 18:06

all I can find

[File attached: 1786298785726\_image.png — contents not included in export]

### Claude · 2026-08-09 18:06

Confirms it: `Sync.4.0.db` is the index/mapping database, `Sync.4.0.option` is the job's config file, `Sync.4.0.deposit` is the versioned-file store — this is the complete SyncBackSE (2BrightSparks) history/deposit set for sync job #4.

The `.dml` files inside `deposit\` are unrecoverable to original names without opening `Sync.4.0.db` — it's the file that maps sequential ID → original filename/path/timestamp. It's a proprietary DB format (not a queryable standard like SQLite necessarily — 2BrightSparks used a custom format in older SyncBack versions).

To read it: open the actual job in SyncBackSE/Pro if still installed (File → Restore, pointing at this job), which will present the versioned files under original names. Without the original software, the `.db` needs to be identified/parsed independently — do you want me to check its header bytes to identify the format, or are you looking to just recover the underlying files by content instead of by name?

### Millard · 2026-08-09 18:06

I don't need techie shit, tell me what these files are

### Claude · 2026-08-09 18:06

These are old versioned backup copies made by a program called SyncBack, from March–April 2007.

Every time SyncBack backed up your files, instead of just overwriting the old backup, it kept the previous version too — renamed to a number (`0.dml`, `1.dml`, etc.) so multiple versions of the same file could coexist. `Sync.4.0.db` is the lookup file that says which number corresponds to which original file and name. `Sync.4.0.option` is just the settings for that backup job.

So: this is a stash of old file version history, not primary data, from a 2007 backup job. To see what's actually in them by original name, you'd need SyncBack itself (or the same version) to open the job and browse the history — the numbered files alone tell you nothing without that.

### Millard · 2026-08-09 18:07

what will I lose if I delete them?

### Claude · 2026-08-09 18:07

You'll lose the ability to recover older versions of whatever files that 2007 SyncBack job was backing up — not the current/latest files themselves, since this deposit folder only holds prior versions kept for rollback, not primary data.

Concretely: if any of those tracked files still exist elsewhere in a current, later, or more complete state, deleting this changes nothing for you. If some file was deleted or overwritten after 2007 and this was your only surviving copy of an old version, that's what disappears — permanently, since there's no other copy of "version history" data by definition.

Given the date (2007) and that this is buried in an old backup drive labeled "Sync.4.0," the practical risk is low unless you specifically need a 17+ year-old version of a file that no longer exists elsewhere. Check `Sync.4.0.db` (via SyncBack, if installed) before deleting if you want certainty on what's actually in there — otherwise this is disposable.

### Millard · 2026-08-09 18:07

so if the source/original file is gone, these do nothing for me?

### Claude · 2026-08-09 18:07

No — reverse of that. If the original/source file is gone, these numbered `.dml` files are the *only* thing that could get it back (an older version of it, not necessarily the last version before deletion).

They only "do nothing for you" if the original file **still exists** elsewhere in a current or equivalent state — in that case the deposit is redundant, since you already have the content.

So: original gone = deposit files are your last surviving copy of that data, risk of loss is highest. Original still exists = deposit is disposable, safe to delete.

### Millard · 2026-08-09 18:08

so these could help recover old content?

### Claude · 2026-08-09 18:08

Yes — if the source file was deleted, corrupted, or overwritten since 2007, one of those numbered `.dml` files could be an old surviving copy of it.

Caveat: you can't tell which number corresponds to which original file, or which version is which, without going through `Sync.4.0.db` — either by opening it in SyncBack (if you still have/can get that version installed) or by parsing the `.db` format directly to extract the name/path mapping.

Without that mapping step, the `.dml` files are just anonymous numbered blobs — recoverable in principle, but not usable in practice until decoded.

### Millard · 2026-08-09 18:43

this is a year and a half old. I made an image because I moved and wanted a backup in case my hard drive got damaged. No good to me now, is it?

[File attached: 1786300984556\_image.png — contents not included in export]

### Claude · 2026-08-09 18:43

Correct — it's dead weight now, for practical purposes.

`WindowsImageBackup` is a full-disk image (Windows Backup and Restore) — a snapshot of your entire OS/drive state as of 2/7/2025. It's not designed for pulling individual files out casually; restoring from it means either:

1. A full system restore (wipes current drive, reverts everything to that exact 2025 state) — destructive to 1.5 years of subsequent work, or
2. Mounting the `.vhd`/`.vhdx` inside it as a virtual disk to browse/extract individual files — doable, but that's the "techie shit" you said to skip.

Since your system is presumably running fine now and this wasn't meant as a file-recovery archive (just an emergency OS-loss safety net for the move), and 18 months have passed with no drive failure: yes, it's obsolete. Its only residual value is emergency full-restore to a stale system state, which you almost certainly don't want.

Safe to delete unless you specifically want to dig out one old file via VHD-mount — tell me if that's the case and I'll walk you through it.
