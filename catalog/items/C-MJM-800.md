# Embedding subtitles in video without quality loss

| | |
|---|---|
| Date | 2026-10-03 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-800` |
| Links | [Original](https://claude.ai/chat/0d563ba5-484c-48b0-925b-54e3c7357e82) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/800-2026-10-03-embedding-subtitles-in-video-without-quality-loss.html) |

**Summary:** Burning a subtitle into a video of Carmeli Brigade soldiers chanting May your village burn before attacking Netzarim, without bloating file size.

**Topics:** Israel, Zionism and the Gaza genocide > Gaza genocide and casualty figures; Israel, Zionism and the Gaza genocide > Israeli state terrorism and its history; Practical & personal > Graphic design and images

**Index terms:** Carmeli Brigade; 22nd Battalion; Netzarim; Gaza; subtitle burn-in; H.264; video encoding

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-10-03 14:16

can you embed the subtitle confined to the bottom 1/8th of the screen:
Ahead of deployment into Netzarim, Gaza in April 2024, the 22nd Battalion of the Carmeli Brigade clearly declared their objective, soldiers and officers cheering, “May your village burn!”
To appear throughout the attached video without degrading the video quality?

[File attached: 22nd Battalion of the Carmeli Brigade before attacking Netzarim, Gaza in April 2024, singing 'May your village burn'.mp4 — contents not included in export]

### Claude · 2026-10-03 14:17

Saturday, October 03, 2026, 08:16 AM CST

Done. The subtitle runs the full 14.9 s, in 3 lines, and sits inside the bottom 100 px of the 720×800 frame (the lowest 1/8th). Text occupies roughly y=733–790.

* **Quality:** re-encoded H.264 at CRF 14, same resolution, frame rate and pixel format. Audio is copied unchanged. Burning in subtitles requires a re-encode, so it cannot be fully lossless. File bitrate went from about 1.49 Mbps to about 3.9 Mbps.

[File attached: frame.png — contents not included in export]

### Millard · 2026-10-03 14:18

you almost tripled the size of the file. was that necessary?

### Claude · 2026-10-03 14:18

No. CRF 14 was my choice, and it was overkill for this source.

The source video stream was 1.36 Mbps. Mine came out at 3.91 Mbps, about 2.9x larger. That extra data buys nothing: the source is already a compressed, low-quality clip, so a lower-bitrate encode would be visually indistinguishable. Roughly CRF 20-23 (or a bitrate cap near 1.4 Mbps) would have kept the size close to the original.

My earlier line compared the source's total bitrate (1.49 Mbps) against my video stream alone (3.9 Mbps). The like-for-like figures are 1.36 vs 3.91 Mbps.

### Millard · 2026-10-03 14:20

Embed the same subtitle confined to the bottom 1/8th of the screen of the same attached video without degrading the video quality and without needlessly bloating the file size. DO NOTHING YET, JUST ANSWER MY QUESTION:
What are you going to do to satisfy my requirements?

### Claude · 2026-10-03 14:20

1. **Subtitle:** same text, same 3-line layout, confined to the bottom 100 px of the 720×800 frame (the bottom 1/8th), shown for the full 14.9 s.
2. **Encoding:** burning in a subtitle forces a re-encode of the video stream, so some generational loss is unavoidable. I will keep it small:

   * Same resolution, frame rate, pixel format, and H.264 High profile.
   * Audio copied untouched.
   * x264 at the slow preset, with the rate set to match the source video bitrate (about 1.36 Mbps) instead of CRF 14. I will use two-pass average-bitrate encoding, or a CRF value tuned until the output lands at about the source size.
3. **Verification before delivery:**

   * Compare the output against the source with SSIM and PSNR, measured on the region above the subtitle band, where the pixels should be unchanged. This puts a number on the quality loss.
   * Compare file size and video bitrate against the source.
   * Extract a frame to confirm the text sits inside the bottom 1/8th.
   * If the size overshoots the source by more than a few percent, or the SSIM is visibly low, I adjust and re-run.
4. **Delivery:** one MP4, with the measured figures (bitrate, size, SSIM/PSNR) reported against the source.

I have not run anything. Awaiting your GO.

### Millard · 2026-10-03 14:22

OK, use the bottom 150 px, increasing font size proportionally. GO

### Claude · 2026-10-03 14:22

Done.

**Subtitle:** font size 28 (up from 19), 4 lines, inside the bottom 150 px (y=650–800). Text spans about y=680–790. Line 2 runs nearly edge to edge, about 8 px from each side. Shown for the full 14.9 s.

**Size:**

|  | Whole file | Video bitrate |
| --- | --- | --- |
| Source | 2,781,387 B | 1,355,714 bps |
| Output | 2,748,736 B | 1,338,197 bps |

The output file is 1.2% smaller than the source. Audio is a stream copy.

**Quality, top 650 px (unchanged region) vs source:**

* SSIM: 0.9875
* PSNR: 42.4 dB average (min 39.3 dB)

Resolution, frame rate, pixel format and profile are unchanged (720×800, 30 fps, yuv420p, High). The measured loss is the cost of the re-encode at the source bitrate, which cannot be avoided when burning in a subtitle. A higher bitrate would raise these figures but would add size.

[File attached: frame2.png — contents not included in export]
