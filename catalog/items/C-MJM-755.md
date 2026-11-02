# Finding network adapters in Linux Mint

| | |
|---|---|
| Date | 2026-08-26 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-755` |
| Links | [Original](https://claude.ai/chat/d9616b55-f556-4c6f-9ed4-38a5859d3756) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/755-2026-08-26-finding-network-adapters-in-linux-mint.html) |

**Summary:** Finding and selecting a USB Wi-Fi adapter in Linux Mint via commands or the graphical nm-connection-editor.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** Linux Mint; NetworkManager; nmcli; USB Wi-Fi adapter; nm-connection-editor

[← Catalog home](../README.md)

---

### Millard · 2026-08-26 20:30

how do I find available network adapters in linux mint?

### Claude · 2026-08-26 20:30

`ip link show` lists all network interfaces (adapters), up or down.

`nmcli device status` — better for Mint (Cinnamon uses NetworkManager); shows device, type, state, connection.

`lshw -C network` — lists physical adapter hardware, including ones without drivers loaded (needs sudo).

`lspci | grep -i network` (or `-i ethernet`, `-i wireless`) — shows adapters at the PCI hardware level, regardless of driver/interface state.

`iwconfig` (if installed) — wireless-specific, older tool, may be absent by default on newer Mint.

For an adapter with no driver bound (won't show in `ip link` or `nmcli`), `lspci`/`lshw` are the ones that will still find it.

### Millard · 2026-08-26 20:33

I have a built-in adapter, and I just plugged in a USB adapter. I want to see the usb adapter, enable it, and connect to wifi using it not the built-in adapter.

### Claude · 2026-08-26 20:33

1. **Identify the USB adapter:**

```
ip link show
```

Look for a new interface that appeared after plugging in (commonly `wlan1`, `wlx<mac>`, or similar — the built-in is usually `wlan0`).

Confirm it's recognized at the hardware level:

```
lsusb
```

and cross-check driver binding:

```
nmcli device status
```

This lists all devices with TYPE (wifi) and STATE (disconnected/unavailable/connected). If the USB adapter doesn't show here, the driver isn't loaded — check `dmesg | tail -30` right after plugging it in for driver errors.

2. **Enable it (bring interface up), if not already:**

```
sudo ip link set <usb_iface> up
```

3. **Connect to wifi using specifically the USB adapter:**

```
nmcli device wifi list ifname <usb_iface>
nmcli device wifi connect "<SSID>" password "<password>" ifname <usb_iface>
```

The `ifname` flag forces NetworkManager to use that specific device rather than whichever it'd pick by default.

4. **Make sure the built-in adapter doesn't interfere:**
   If both are trying to auto-connect, disconnect/disable the built-in one:

```
nmcli device disconnect <builtin_iface>
```

or disable its autoconnect permanently:

```
nmcli connection modify <builtin_connection_name> connection.autoconnect no
```

Replace `<usb_iface>` and `<builtin_iface>` with actual names from step 1's `ip link show` output — post it if you want exact commands filled in.

### Millard · 2026-08-26 20:34

wtf isn't there a graphical interface like Network Adapters in Win 11?

### Claude · 2026-08-26 20:34

Yes.

**Cinnamon's built-in one:** Menu → Network → or run `nm-connection-editor` — this is the closest analog to Windows' "Network Connections" panel. Shows all adapters, lets you enable/disable, set per-adapter connection preferences.

Also: **Settings → Network** (System Settings applet) — simpler view, shows Wired/Wifi devices, toggle on/off.

For picking which adapter to use for a specific wifi connection: `nm-connection-editor` → Wi-Fi tab → Edit/Add connection → **General tab → "Restrict to this device"** — this is the GUI equivalent of `ifname` above, binds an SSID connection to a specific physical adapter.

The Cinnamon applet (network icon in system tray) will let you pick which *adapter's* SSID list to browse if multiple wifi devices are present, but it won't show enable/disable per-adapter as cleanly as `nm-connection-editor`.

If neither applet shows the USB adapter at all, it's not bound to a driver — GUI won't help, back to `dmesg`/`lsusb`.
