# Nvidia screen capture region selection

| | |
|---|---|
| Date | 2026-09-05 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-ac2c313e` |
| Links | [Original](https://claude.ai/chat/ac2c313e-32fe-4f51-bdf3-6ccc7c294adf) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-09-05_nvidia-screen-capture-region-selection_ac2c313e.html) |

**Summary:** Notes NVIDIA ShadowPlay cannot record a screen region and recommends LosslessCut for quick video cropping.

**Topics:** Practical & personal > Software tools and open-source projects; Practical & personal > Graphic design and images

**Index terms:** NVIDIA ShadowPlay; screen recording; LosslessCut; Clipchamp; video cropping

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-09-05 15:16

i'm trying to use NVidia screen capture to scrape video but can't find where to tell it what part of the screen to record.

### Claude · 2026-09-05 15:16

It doesn't have one — NVIDIA ShadowPlay records whole windows or the full desktop only, no region selection.

### Millard · 2026-09-05 15:17

Is there a super quick and easy video cropping tool I could use on the recording?

### Claude · 2026-09-05 15:17

ffmpeg one-liner: `ffmpeg -i in.mp4 -vf "crop=W:H:X:Y" -c:a copy out.mp4`, or Clipchamp (built into Windows 11) if you want to drag a box.

### Millard · 2026-09-05 15:18

Clipchamp is NOT super quick and easy -- bloated, slow, and unintuitive.

### Claude · 2026-09-05 15:18

LosslessCut — free, opens instantly, drag a crop box, exports without re-encoding.
