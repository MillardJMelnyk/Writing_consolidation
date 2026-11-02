# What is CPU-Z

| | |
|---|---|
| Date | 2026-08-12 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-739` |
| Links | [Original](https://claude.ai/chat/83552a79-e030-4cd0-a0a5-8076a17f0319) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/739-2026-08-12-what-is-cpu-z.html) |

**Summary:** What CPU-Z is, how to disable it, and that uninstalling it loses nothing functional.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; Practical & personal > Software tools and open-source projects

**Index terms:** CPU-Z; CPUID; system information utility; uninstall

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-08-12 17:59

what is cpu-z

### Claude · 2026-08-12 17:59

CPU-Z is a free system-information utility for Windows (also has an Android version) developed by CPUID. It reports real-time data on CPU (name, architecture, core/thread count, clock speeds, cache sizes), motherboard, RAM (timings, frequency, SPD data), and GPU.

### Millard · 2026-08-12 18:00

how do i disable it?

### Claude · 2026-08-12 18:00

Ambiguous. Clarify:

* Uninstall it entirely?
* Close/exit a running instance?
* Stop it from launching at Windows startup (it doesn't by default unless added)?
* Prevent a specific feature (e.g., validation/sensor polling)?

### Millard · 2026-08-12 18:00

all the above

### Claude · 2026-08-12 18:00

**1. Close a running instance**

* Right-click the CPU-Z icon in the system tray (if present) → Exit, or close the window / End Task via Task Manager (process: `cpuz.exe` or `cpuz_x64.exe`).

**2. Uninstall entirely**

* Settings → Apps → Installed apps → CPU-Z → Uninstall
* Or if portable (no installer used), just delete the folder/exe — nothing to uninstall.

**3. Prevent startup launch**

* Not a default behavior; CPU-Z does not auto-start unless manually added.
* If it is starting: Task Manager → Startup apps tab → find CPU-Z → Disable.
* Also check `shell:startup` folder and Task Scheduler for a manually-created entry.

**4. Disable specific features (sensors/validation)**

* CPU-Z itself has no background service or continuous sensor polling — it only reads data on demand while the window is open. No settings toggle exists for this because there's no persistent monitoring process to disable.

### Millard · 2026-08-12 18:01

what will i lose if i uninstall it?

### Claude · 2026-08-12 18:01

Nothing functional on the system. CPU-Z is read-only — it doesn't control, tune, or interface with hardware; it only queries and displays data (SPD, clocks, cache, etc.).

What you lose:

* The utility itself (no more on-demand CPU/RAM/GPU/motherboard readouts)
* Any saved validation reports/screenshots stored locally (not deleted by uninstall unless you manually remove them — they're separate files)
* CPU-Z's built-in stress-test/bench score history, if you used its benchmark feature (local only, not synced anywhere)

No drivers, services, or system settings are removed — it installs no persistent background component to begin with.
