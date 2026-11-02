# WiFi network adapter keeps disconnecting

| | |
|---|---|
| Date | 2026-08-26 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-753` |
| Links | [Original](https://claude.ai/chat/5c68c65d-fb47-4a4a-9275-f89aab7a8057) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/753-2026-08-26-wifi-network-adapter-keeps-disconnecting.html) |

**Summary:** Windows Wi-Fi adapter repeatedly asking for the password on a Megacable network; steps to forget, disable random MAC and update driver.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** Wi-Fi; Megacable; network adapter; random hardware address; device driver

[← Catalog home](../README.md)

---

### Millard · 2026-08-26 14:26

No matter how many times I enter the password on this network adapter for this wifi, it keeps disconnecting and telling me something's changed, forcing me to enter it again. What's wrong?

[File attached: 1787754385747\_image.png — contents not included in export]

### Claude · 2026-08-26 14:26

Common causes, in order of likelihood:

1. **Stored profile/password mismatch** — Windows cached credential is corrupted or out of sync with the router. Fix: forget the network entirely (Settings → Network & Internet → Wi-Fi → Manage known networks → Forget), then reconnect fresh.
2. **Router security mode changed or is inconsistent** — e.g., router broadcasting WPA2/WPA3 mixed mode, or MEGACABLE's ISP-supplied router periodically resets/re-provisions its own config (common on ISP routers with remote management). Check router admin panel for security mode changes or recent reboots/firmware pushes.
3. **Wi-Fi adapter driver bug** — outdated or buggy driver mishandles the network profile handshake. Check Device Manager → Network adapters → driver date; update from chipset vendor (Intel/Realtek/Qualcomm), not just Windows Update.
4. **MAC randomization conflict** — Windows is randomizing your MAC per-connection while the router has a fixed lease/ACL tied to a specific MAC, causing repeated "new device" handshakes. Check Settings → Wi-Fi → network properties → Random hardware addresses → set to Off (use device MAC) for this network.
5. **Corrupted network profile in Windows** — delete via `netsh wlan delete profile name="MEGACABLE-5G-75A6"` in an elevated command prompt, then reconnect.

Fastest diagnostic: forget network → turn off MAC randomization for it → update Wi-Fi driver → reconnect. If it still loops, the fault is on the router side (security-mode flapping or firmware issue), not the PC.

### Millard · 2026-08-26 14:29

give me simple instructions in sequence

### Claude · 2026-08-26 14:29

1. Settings → Network & Internet → Wi-Fi → Manage known networks → select MEGACABLE-5G-75A6 → Forget.
2. Settings → Wi-Fi → click MEGACABLE-5G-75A6 (won't connect yet, just to open its properties) — actually: after forgetting, click the Wi-Fi icon in taskbar → find MEGACABLE-5G-75A6 → click it → check "Random hardware addresses" toggle → set to **Off**.
3. Open Device Manager → Network adapters → right-click your Wi-Fi adapter → Update driver → Search automatically. If nothing found, get the driver from the manufacturer's site (Intel/Realtek/Qualcomm) manually.
4. Reboot the PC.
5. Reconnect to MEGACABLE-5G-75A6, enter the password once.
6. If it still loops after this — reboot the router itself (unplug 30 sec, plug back in), then reconnect.
7. If it loops even after a router reboot — problem is the router/ISP side (log into router admin page, check security mode isn't set to a mixed/auto WPA2/WPA3 mode — pin it to WPA2-PSK/AES only).
