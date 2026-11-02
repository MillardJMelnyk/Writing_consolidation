# Reinstalling Windows 11 without data loss

| | |
|---|---|
| Date | 2026-08-24 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-9bf5a953` |
| Links | [Original](https://claude.ai/chat/9bf5a953-3ef2-479a-ada3-fc777e673eaf) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-08-24_reinstalling-windows-11-without-data-loss_9bf5a953.html) |

**Summary:** Instructions for repairing a Windows 11 update boot loop via in-place reinstall, DISM and sfc, plus exporting a list of installed apps.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** Windows 11; in-place repair install; DISM; sfc scannow; Windows Update; PowerShell

[← Catalog home](../README.md)

---

### Millard · 2026-08-24 18:26

I need blunt, simple, short, clear instructions how to reinstall Windows 11 from scratch without losing any data.

Windows just crashed, then instead of restarting, it went into a loop "installing updates", then "something didn't go as planned", then reboot, then "installing updates", then "something didn't go as planned", then reboot... After 3 cycles I hard-shut-down and had to do it a 2nd time because it went right back into the loop again. Finally I got it to break out of the loop.

Then it crashed again.

Here's the update page (attached). The update fails every time. (I've tried it almost 10 times now).

Should I follow the yellow "reinstall" button or is there a better way?

### Claude · 2026-08-24 18:26

Yes — "Reinstall Now" is the right button. It's an in-place repair install: keeps files, apps, and settings, replaces the OS files. Do this first, though:

**1. Back up anyway.** Copy MQL5 folders, code, manuscript to an external drive or cloud. Repair installs almost never eat data, but a machine that's already crashing mid-update is not one to trust.

**2. Try the cheap repair first** (10 min, often fixes 0x80070057). Admin PowerShell:

```
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

Reboot, retry the update once. If it fails again, go to step 3.

**3. Reset the update stack.** Admin PowerShell:

```
net stop wuauserv
net stop bits
ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
ren C:\Windows\System32\catroot2 catroot2.old
net start wuauserv
net start bits
```

Retry the update once.

**4. If still failing, click Reinstall Now.** Plugged in, no other work running, ~1 hour, several reboots. Don't hard-power-off during it.

**Alternative to step 4** if the button errors out: download the Windows 11 ISO from Microsoft, mount it, run `setup.exe` from inside Windows, choose **Keep personal files and apps**. Same result, more reliable.

One flag: repeated crashes plus repeated update failures can be a dying SSD or bad RAM, and a repair install won't fix that. Before step 4, run `chkdsk C: /scan` and check SMART status with CrystalDiskInfo. If the drive is throwing reallocated sectors, clone it before you do anything else.

### Millard · 2026-08-24 18:29

is there a way to get a list of all installed apps (same as listed on the Programs and Features page) along with full path installation locations?

### Claude · 2026-08-24 18:29

Yes. Admin PowerShell, one line:

```
Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*, HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*, HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\* | Where-Object DisplayName | Select-Object DisplayName, DisplayVersion, Publisher, InstallLocation, InstallDate, UninstallString | Sort-Object DisplayName | Export-Csv C:\installed_apps.csv -NoTypeInformation
```

That's exactly what Programs and Features reads from, plus paths.

Caveat: `InstallLocation` is blank for a lot of entries — the installer just never wrote it. `UninstallString` is in the output because it almost always contains the real path, so you can recover the location manually.

For Store apps (not in Programs and Features), separate command:

```
Get-AppxPackage | Select-Object Name, PackageFullName, InstallLocation | Export-Csv C:\store_apps.csv -NoTypeInformation
```

### Millard · 2026-08-24 18:30

where's it going to put the info?

### Claude · 2026-08-24 18:30

`C:\installed_apps.csv` and `C:\store_apps.csv` — root of the C: drive, exactly where the command says.

Windows 11 blocks writing to C:\ root without admin, so if PowerShell isn't elevated it errors. Change the path to `C:\Users\<you>\Desktop\installed_apps.csv` if you'd rather not run as admin.
