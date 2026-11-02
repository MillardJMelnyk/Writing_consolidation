# Mobile hotspot disabled after adapter issue

| | |
|---|---|
| Date | 2026-08-04 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-7dfde0a3` |
| Links | [Original](https://claude.ai/chat/7dfde0a3-78bb-4cec-9fb8-66cfd3f4f4ae) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-08-04_mobile-hotspot-disabled-after-adapter-issue_7dfde0a3.html) |

**Summary:** Re-enabling the Microsoft Wi-Fi Direct Virtual Adapter in Windows to restore a laptop's mobile hotspot after disabling it.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** mobile hotspot; Microsoft Wi-Fi Direct Virtual Adapter; network adapter; netcfg

[← Catalog home](../README.md)

---

### Millard · 2026-08-04 21:23

i disabled an adapter while my mobile hotspot was on because i didnt recognize it and now i cant turn back on the mobile hotspot on my laptop

### Claude · 2026-08-04 21:23

That adapter was almost certainly one of the virtual "Microsoft Wi-Fi Direct Virtual Adapter" entries (shows as "Local Area Connection\* 1/2/3..." in Network Connections) — Windows uses it to run the hotspot.

Fix: Win+R → `ncpa.cpl` → find the disabled "Microsoft Wi-Fi Direct Virtual Adapter" (or "Local Area Connection\*" entry) → right-click → Enable. Then try turning on Mobile Hotspot again.

If you don't see it or it still won't enable, run in an admin PowerShell/CMD:

```
netcfg -d
```

then reboot — this resets all network adapters and lets Windows recreate the virtual ones.
