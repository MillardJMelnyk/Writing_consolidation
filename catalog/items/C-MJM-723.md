# Converting gigabytes to kilobytes

| | |
|---|---|
| Date | 2026-08-06 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-723` |
| Links | [Original](https://claude.ai/chat/f754eda3-4242-4930-abca-8148a3da5349) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/723-2026-08-06-converting-gigabytes-to-kilobytes.html) |

**Summary:** Converts 5 GB to kilobytes and explains how dupeGuru chooses which duplicate is the retained reference file.

**Topics:** Practical & personal > Unit conversions; Practical & personal > Software tools and open-source projects

**Index terms:** gigabyte; kilobyte; dupeGuru; reference file; folder priority

[← Catalog home](../README.md)

---

### Millard · 2026-08-06 19:31

how many KBs is 5 GB?

### Claude · 2026-08-06 19:31

5 GB = 5,000,000 KB (decimal, GB=10⁹ bytes, KB=10³ bytes).

If binary (GiB/KiB, 1024 base): 5 GiB = 5,242,880 KiB.

### Millard · 2026-08-06 20:12

dupeGuru results. The highlighted files will be retained and the checked files will be deleted?

[File attached: 1786047092404\_image.png — contents not included in export]

### Claude · 2026-08-06 20:12

Yes. In dupeGuru, each group's bolded reference row (no checkbox, shown in blue/bold) is kept — it's excluded from deletion. Every checked row beneath it is marked for deletion when you run the delete/remove action.

Status bar confirms: "58/58 (106.78 GB / 106.78 GB) duplicates marked" — all 58 checked duplicates will be removed, leaving the reference copies.

### Millard · 2026-08-06 20:12

what controls which duplicate with be bolded?

### Claude · 2026-08-06 20:12

dupeGuru picks the reference (bolded) file per group based on folder priority order — set via **Directories tab → right-click a folder → "Move Up"/"Move Down"** to rank folders, or drag to reorder. Highest-priority folder's copy becomes the reference in every group.

If no custom priority is set, default ranking falls back to scan order (folders as added/listed in Directories tab, top = highest priority).

You can also change ranking criteria under **Actions → Priorize (sic) / Re-Prioritize** dialog, which lets you sort by criteria (folder path, size, modification date, etc.) rather than manual folder order.
