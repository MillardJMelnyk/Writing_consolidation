# MX Master S3 dongle compatibility

| | |
|---|---|
| Date | 2026-08-26 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-756` |
| Links | [Original](https://claude.ai/chat/975a29ea-604b-47fd-8513-484d212fa987) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/756-2026-08-26-mx-master-s3-dongle-compatibility.html) |

**Summary:** MX Master 3S uses the Logi Bolt receiver; FSearch is a Linux counterpart to Everything, with install steps for Mint.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; Practical & personal > Software tools and open-source projects

**Index terms:** Logitech MX Master 3S; Logi Bolt; FSearch; Everything; Linux Mint

[← Catalog home](../README.md)

---

### Millard · 2026-08-26 21:12

what kind of dongle does mx master s3 mouse work with, bolt?

### Claude · 2026-08-26 21:12

Logi Bolt USB receiver. It also pairs via Bluetooth Low Energy — no dongle required if using Bluetooth. It is not compatible with the older Logitech Unifying receiver used by prior MX Master models unless you're using an adapter workaround (unsupported by Logitech).

### Millard · 2026-08-26 22:11

is there a linux counterpart to voidtools Everything?

### Claude · 2026-08-26 22:11

Closest counterparts:

* **plocate/mlocate** — indexed filename search via `updatedb` cron job, near-instant results, filename-only (like Everything's default mode). Standard on most distros.
* **catfish** — GUI frontend for locate/find, closest visual analog to Everything's UI.
* **recoll** — indexes file contents too, not just names; heavier, more like a search engine.
* **fsearch** — the most direct clone: NTFS-style instant filename search, GTK UI, explicitly inspired by Everything.
* **ANGRYsearch** — another direct Everything clone, Python/PyQt, less maintained.

None match Everything's real-time NTFS MFT-level indexing exactly, since Linux filesystems (ext4, btrfs, xfs) don't expose an equivalent low-level change journal API that user-space tools can hook the same way. fsearch is the nearest architectural analog (uses inotify + periodic reindex rather than live MFT reads).

Status as of my knowledge cutoff (Jan 2026) — verify current maintenance state if it matters for your use case.

### Millard · 2026-08-26 22:12

how do I install fsearch

### Claude · 2026-08-26 22:12

Depends on distro:

**Arch / Manjaro**

```
sudo pacman -S fsearch
```

(or AUR: `yay -S fsearch-git` for latest)

**Debian/Ubuntu** — not in default repos; use the PPA:

```
sudo add-apt-repository ppa:christian-boxdoerfer/fsearch-daily
sudo apt update
sudo apt install fsearch
```

**Fedora**

```
sudo dnf copr enable rushosupreme/fsearch
sudo dnf install fsearch
```

**openSUSE**

```
sudo zypper install fsearch
```

**Flatpak** (distro-agnostic)

```
flatpak install flathub io.github.cboxdoerfer.FSearch
```

**From source**

```
git clone https://github.com/cboxdoerfer/fsearch.git
cd fsearch
meson build
ninja -C build
sudo ninja -C build install
```

Requires: gtk3, glib, pcre2, meson, ninja as build deps.

First launch triggers an initial index build; subsequent updates use inotify for incremental changes.

### Millard · 2026-08-26 22:12

minty

### Claude · 2026-08-26 22:12

Linux Mint (Ubuntu/Debian base):

```
sudo add-apt-repository ppa:christian-boxdoerfer/fsearch-daily
sudo apt update
sudo apt install fsearch
```

If the PPA add fails on Mint due to codename mismatch (Mint uses its own codenames like `virginia`/`wilma` instead of Ubuntu's), edit the resulting `.list` file in `/etc/apt/sources.list.d/` and replace the Mint codename with the underlying Ubuntu base codename (check with `. /etc/os-release; echo $UBUNTU_CODENAME`) before running `apt update`.

Flatpak avoids that issue entirely:

```
flatpak install flathub io.github.cboxdoerfer.FSearch
```

### Millard · 2026-08-26 22:12

mint

### Claude · 2026-08-26 22:12

Same answer as above — you'd already said "minty," which I read as Mint. Confirming: yes, Linux Mint.

```
sudo add-apt-repository ppa:christian-boxdoerfer/fsearch-daily
sudo apt update
sudo apt install fsearch
```

If PPA add fails on codename mismatch, use `$UBUNTU_CODENAME` from `/etc/os-release` in place of the Mint codename in the `.list` file. Flatpak sidesteps this:

```
flatpak install flathub io.github.cboxdoerfer.FSearch
```
