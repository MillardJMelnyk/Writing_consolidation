# Detecting remote internet connections to your computer

| | |
|---|---|
| Date | 2026-09-03 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-f37ab00f` |
| Links | [Original](https://claude.ai/chat/f37ab00f-bf00-4dbb-8437-3777de80b956) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-09-03_detecting-remote-internet-connections-to-your-computer_f37ab00f.html) |

**Summary:** Lists Windows commands to detect remote connections to a computer, then explains the El Niño climate pattern.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; Science, nature and the cosmos > Earth science and natural phenomena

**Index terms:** netstat; Remote Desktop; network security; El Niño; La Niña; trade winds

[← Catalog home](../README.md)

---

### Millard · 2026-09-03 19:07

how can i see if someone is connected to my computer via the internet?

### Claude · 2026-09-03 19:07

Run these in an admin PowerShell/Command Prompt:

* `netstat -bno` — every open connection with the program behind it. Look at the ESTABLISHED lines and any foreign address you don't recognize.
* `query user` — lists anyone logged into the machine, including remote sessions.
* `qwinsta` — shows Remote Desktop sessions and their state.
* `Get-SmbSession` — anyone connected to your shared folders.

Also check Task Manager → Users tab for extra sessions, and Event Viewer → Windows Logs → Security, Event ID 4624 with Logon Type 10 (remote desktop) or 3 (network).

Quick lockdown check: Settings → System → Remote Desktop should be Off if you don't use it, and confirm you don't have TeamViewer/AnyDesk/Chrome Remote Desktop running in the system tray.

### Claude · 2026-09-03 19:08

You're not running as admin. Close that window, press Win, type "PowerShell", right-click it, choose "Run as administrator", then run `netstat -bno` again.

Or drop the `-b` — `netstat -no` works without elevation, but you won't see program names, just PIDs you'd have to match in Task Manager's Details tab.

### Claude · 2026-09-03 19:09

No. Every line is your machine reaching out — nothing is coming in.

Breakdown of what's there:

* **terminal64.exe → 100.30.130.4:1950** — MT5 to your broker.
* **cTrader.exe → 15.197.224.245 / 99.83.180.197:443** — cTrader to its servers.
* **msedge, msedgewebview2, chrome, steam, steamwebhelper, OneDrive, M365Copilot, SearchHost, svchost (CryptSvc/WpnService)** — normal Windows and browser traffic.
* **127.0.0.1 pairs** — Steam talking to itself, local only.
* **All the 192.168.100.1:53 TIME\_WAIT** — DNS lookups to your router. Closed already, harmless.

No 3389 (RDP), no 5900 (VNC), no AnyDesk/TeamViewer/Chrome Remote Desktop, no foreign address holding a session open into your box.

Two things worth noting:

1. `netstat -bno` shows connections but not open listening ports. To rule out a dormant backdoor waiting for a connection, run `netstat -bnoa` and look at the LISTENING lines with a foreign address of `0.0.0.0:0` on ports you don't recognize.
2. OneDrive and M365Copilot are stuck in SYN\_SENT to **172.31.255.254:443** — that's a private address, not Microsoft. Something on your network is resolving Microsoft hostnames to a local box. Usually that's an ISP router serving a block/redirect page, but it's DNS interception either way and it's why those apps aren't syncing.

### Millard · 2026-09-03 19:15

WHat is el nino?

### Claude · 2026-09-03 19:15

A recurring warming of the surface water in the central and eastern Pacific along the equator, off South America. Normally trade winds push warm water west toward Asia; when those winds weaken, the warm water sloshes back east.

That shifts where the atmosphere dumps its heat and moisture, so weather patterns move worldwide — typically wetter in the southern US and Peru, drier in Australia, Indonesia and southern Africa, fewer Atlantic hurricanes, and a bump in global average temperature. It runs in cycles of roughly two to seven years and usually peaks around December, which is why Peruvian fishermen named it after the Christ child.

Its opposite is La Niña, when that same water turns colder than normal.
