# HDMI connection not displaying on TV

| | |
|---|---|
| Date | 2026-09-05 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-0f3b02b0` |
| Links | [Original](https://claude.ai/chat/0f3b02b0-14f3-47c6-9e02-ed2ed6fb8992) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-09-05_hdmi-connection-not-displaying-on-tv_0f3b02b0.html) |

**Summary:** Troubleshoots an HDMI connection to a Vizio TV showing no signal, narrowing it to the computer side.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** HDMI; Vizio; display output; no signal

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-09-05 03:06

when ii plug in the hdmi to my vios tv, the computer ,akes a sound recognizing i input the hdmi but the tv screen stiil says no signal

### Claude · 2026-09-05 03:07

The TV is receiving power on the HDMI line but no video — the computer sees the handshake, the TV doesn't get a picture.

Check in this order:

1. TV input — press Input/Source on the Vizio remote and select the exact HDMI port the cable is in (HDMI-1, 2, 3). Ports are labeled on the back.
2. Windows display mode — Win+P, pick Duplicate or Extend. If it's set to "PC screen only," the TV gets nothing.
3. Swap the port — move the cable to a different HDMI jack on the TV. Vizio HDMI ports fail individually, and some are ARC/eARC-only quirky.
4. Swap the cable — cheap or long HDMI cables pass the handshake but drop the video signal.
5. Resolution — if your PC is outputting 4K/120Hz or HDR and the port only does 4K/60, you get no signal. Drop to 1920x1080 @ 60Hz in Windows display settings first, then raise it.
6. Cold boot — unplug the TV from the wall for 60 seconds with the HDMI still connected, plug back in. Clears a stuck EDID handshake.

Steps 1 and 5 fix this most of the time.

### Millard · 2026-09-05 03:08

we plugged in my gfs computer andit works soit must be on my computers end right

### Claude · 2026-09-05 03:08

Yes — assuming you used the same cable and same TV port.

On your PC:

1. Win+P → Duplicate or Extend.
2. Display settings → Detect. If the TV shows up but is blank, drop it to 1920x1080 @ 60Hz.
3. Update the GPU driver (NVIDIA/AMD/Intel site, not Windows Update). Bad or stale drivers pass the handshake and send nothing.
4. If you have both onboard video and a graphics card, make sure the cable is in the graphics card port, not the motherboard.
5. Check HDR — Settings → System → Display → HDR off. Some TVs go blank instead of falling back.

If your GF used a different cable or port, swap those onto your machine before blaming the PC.

### Millard · 2026-09-05 03:08

?

### Claude · 2026-09-05 03:08

Which part?
