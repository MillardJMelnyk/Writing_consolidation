# Dupeguru retaining wrong duplicate files

| | |
|---|---|
| Date | 2026-08-06 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-725` |
| Links | [Original](https://claude.ai/chat/49f0936b-a5ea-4c9a-b4c5-cc01269b1015) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/725-2026-08-06-dupeguru-retaining-wrong-duplicate-files.html) |

**Summary:** dupeGuru retained Recycle Bin copies over normal files; fix by excluding $RECYCLE.BIN via the Directories State column.

**Topics:** Practical & personal > Software tools and open-source projects; Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** dupeGuru; Recycle Bin; folder exclusion; duplicate file

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-08-06 23:14

using dupeGuru, it chose to retain Recycle Bin files instead of files in normal folders. What do I do?

[File attached: 1786058025526\_image.png — contents not included in export]

### Claude · 2026-08-06 23:14

Two options, in order of effort:

**1. Exclude the Recycle Bin from the scan (correct fix, requires rescan)**
Go to Directories tab → remove `F:\$RECYCLE.BIN` from the scanned folder list (or right-click it → Exclude) → rescan. Recycle Bin entries won't appear at all, so this can't recur.

**2. Fix selection on the current results without rescanning**
dupeGuru's reference (the bold blue row, never auto-deleted) is chosen by folder scan priority — normally by the order folders were added in the Directories tab, not by "real" vs "trash" location. Since `$RECYCLE.BIN` got added/scanned first or ranks higher in priority, its copies became reference.

To fix without rescanning: right-click on the row you want kept (the real-folder file) → check for a "Set as Reference" / "Move to Reference" option in the context menu (exists in current dupeGuru versions under the results right-click menu). This swaps which file in that group is protected. You'd have to do this per group — tedious for this many rows.

**Practical recommendation:** exclude `$RECYCLE.BIN` and rescan. It's the only fix that scales past a handful of groups and prevents the same misordering on future scans.

### Millard · 2026-08-06 23:15

exclude `$RECYCLE.BIN`
how?

### Claude · 2026-08-06 23:15

Directories tab → right-click `F:\$RECYCLE.BIN` in the folder list → **Remove** (or select it and press Delete/click the minus button) to drop it from the scan entirely.

If dupeGuru's version instead offers **"Set as Excluded"** on right-click, use that — it keeps the folder listed but skips it during scanning.

If neither option appears in the context menu, use the **Ignore List** (Actions menu → Ignore List, or File → Ignore List depending on version) and add a pattern like `$RECYCLE.BIN` or `*\$RECYCLE.BIN\*`.

After excluding, click **Actions → Scan** (or the Scan button) again to regenerate results without those entries.

### Millard · 2026-08-06 23:18

give me a wild card version that will work regardless of drive

### Claude · 2026-08-06 23:18

`*\$RECYCLE.BIN\*`

Matches the folder under any drive letter or parent path, since the pattern has no drive prefix.

### Millard · 2026-08-06 23:19

get your instructions right. right-clicking on that tab does nothing.

### Claude · 2026-08-06 23:19

Correction: no right-click. Per official docs:

Directories tab → click on the **State column cell** next to `F:\$RECYCLE.BIN` → a dropdown appears → select **Excluded**.

Alternative if the dropdown doesn't do it: select the `F:\$RECYCLE.BIN` row → click the **–** (minus/remove) button in that panel. Note: if `$RECYCLE.BIN` is a subfolder under a parent you added (e.g. you added `F:\` itself), clicking – sets it to Excluded rather than removing it — same result, different path.
