# Setting MS Paint default DPI to 300

| | |
|---|---|
| Date | 2026-07-24 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-716` |
| Links | [Original](https://claude.ai/chat/19e74c67-96b1-44b3-b6d3-464ec51ffced) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/716-2026-07-24-setting-ms-paint-default-dpi-to-300.html) |

**Summary:** MS Paint has no default DPI setting; debate over whether a file's DPI changes how text renders on its canvas.

**Topics:** Practical & personal > Graphic design and images; Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** Microsoft Paint; DPI; canvas resolution; font rendering; image metadata

[← Catalog home](../README.md)

---

### Millard · 2026-07-24 17:12

How can I set the default for MS Paint to use 300 DPI?

### Claude · 2026-07-24 17:12

No default-DPI setting exists in MS Paint. It hardcodes 96 DPI on save, with no global preference to override this.

**Workarounds (all indirect):**

1. Set canvas pixel dimensions to match 300 DPI at your intended print size (e.g., 8×10 in → 2400×3000 px), then export. The DPI metadata tag still reads 96, but pixel density at that print size is effectively 300.
2. Some third-party tools (IrfanView, GIMP, Photoshop) let you rewrite the DPI metadata tag directly without resampling pixels — use one of those post-export if the tag value itself matters (e.g., for a print vendor requiring 300 in the file header).

If your actual goal is a print job requiring 300 DPI metadata, Paint isn't the tool — no configuration achieves it.

### Millard · 2026-07-24 17:13

can't you open paint specifying a file to initially open?

### Claude · 2026-07-24 17:13

Yes.

```
mspaint.exe "C:\path\to\file.png"
```

Or via `start`:

```
start mspaint "C:\path\to\file.png"
```

This opens Paint with that file loaded — doesn't affect DPI handling, just the initial-file-open question you asked.

### Millard · 2026-07-24 17:13

If the file is 300 DPI, the canvas is 300 DPI, right?

### Claude · 2026-07-24 17:13

No. The canvas in Paint is a pixel grid — it has no DPI property of its own during editing.

What happens: Paint reads the source file's DPI metadata (if present) into Image Properties, which Paint uses to compute the "print size in inches/cm" shown there. That metadata is not preserved reliably — most reports confirm classic Paint rewrites the DPI tag to 96 on save regardless of the source file's original value.

So opening a 300 DPI file doesn't make your Paint "canvas" 300 DPI in any operative sense, and saving from Paint will typically discard the 300 DPI tag and write 96 instead.

### Millard · 2026-07-24 17:15

wrong. For example, the result of creating text on a 168 DPI (it's NOT 96) canvas is completely different than that same text on a blank 300 DPI blank file canvas.

### Claude · 2026-07-24 17:15

Correct — I overstated it. Admitted.

Mechanism: Text tools that use point-based sizing convert points to pixels via `pixels = points × DPI / 72`. If Paint reads the file's DPI metadata and uses it for that conversion, identical point-size text renders at different pixel heights on a 168 DPI canvas vs. a 300 DPI canvas — confirmed generic behavior in Paint.NET and Photoshop, and consistent with standard Windows GDI font scaling.

What I don't have a direct source confirming: whether classic `mspaint.exe` (not Paint.NET) actually reads the source file's DPI tag for this point-to-pixel conversion, or whether it always assumes 96 regardless of the file's tag. If you're seeing a real difference in rendered text size between the two files at the same point setting, that's empirical evidence it does use the file's DPI value — I have no result contradicting that.

Net effect on your original question: even if true, this doesn't restore a default-DPI *setting* — it just means the per-file DPI tag, read at open time, drives point-size rendering behavior during that editing session.
