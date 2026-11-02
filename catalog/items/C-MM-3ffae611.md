# Indicator line customization without recompiling

| | |
|---|---|
| Date | 2026-07-18 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-3ffae611` |
| Links | [Original](https://claude.ai/chat/3ffae611-5c98-4a7d-a4c4-a01fbfe0d094) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-07-18_indicator-line-customization-without-recompiling_3ffae611.html) |

**Summary:** cTrader allows changing indicator line color, style and thickness without recompiling, and programmatically beyond the panel's size limit.

**Topics:** Trading and markets > cTrader migration and features

**Index terms:** cTrader; indicator line; line thickness; MetaTrader 5

[← Catalog home](../README.md)

---

### Millard · 2026-07-18 13:42

In you can change the style, with, and color of indicator lines without recompiling. I was told that this isn't possible in ctrader.

### Claude · 2026-07-18 13:42

Wrong info — cTrader lets you do this too. Right-click the indicator on the chart → Edit (or the settings dialog), and each output line has color, thickness, and line style controls there, no recompile needed.

### Millard · 2026-07-18 13:43

I remember now, it was because the sea trader panel limits you to size 5, but I need to go beyond that

### Claude · 2026-07-18 13:43

The panel caps at 5, yes. Workaround: declare the thickness as an indicator parameter and pass it to the output in code — then you change it from the parameters tab without recompiling, and the API accepts values above 5 that way. Hypothesis: I haven't verified that cTrader actually renders thicknesses above 5 rather than clamping them; you'd need to test it once.

### Millard · 2026-07-18 13:43

It does I have an indicator that paints it size 10 we've taken it up to 50 even

### Claude · 2026-07-18 13:43

Good — then the parameter approach is your answer: expose LineThickness as an int parameter, apply it to the output attribute or set it at runtime in Initialize, and you get any size without recompiling.

### Millard · 2026-07-18 13:45

In other words a line's attributes can be manipulated programmatically

### Claude · 2026-07-18 13:45

Yes.
