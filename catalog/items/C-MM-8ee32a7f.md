# MQL5 template tester thin lines issue

| | |
|---|---|
| Date | 2026-07-06 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-8ee32a7f` |
| Links | [Original](https://claude.ai/chat/8ee32a7f-5a93-474b-af28-b91181a95d68) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-07-06_mql5-template-tester-thin-lines-issue_8ee32a7f.html) |

**Summary:** Diagnosing thin high-to-high and low-to-low lines in the MT5 Strategy Tester template, suspected bid and ask lines.

**Topics:** Trading and markets > Brokers, accounts and platforms

**Index terms:** MetaTrader 5; Strategy Tester; chart template; bid line; ask line

[← Catalog home](../README.md)

---

### Millard · 2026-07-06 13:52

Image 1 is the attached MQL5 template tester.tpl, on a live chart window. This is the template used by the Strategy tester. Image two is that same template during a strategy tester run. Same chart bars are shown.

Look at the .tpl and find out why in the ST the template paints thin lines from high to high and low to low.

### Claude · 2026-07-06 13:54

Read the tpl. Facts from the file:

```
bidline=1
askline=0
lastline=0
askline_color=255        ← pure red
bidline_color=10061943   ← gray-blue (same value as grid_color)
```

The upper thin red line in the tester shot matches `askline_color=255` exactly; the lower gray line matches `bidline_color`. Those two lines are the chart's **Ask line and Bid line**, not anything from your indicator (all 5 BarID graph plots have `draw=0` = DRAW\_NONE, and the tpl contains no other indicators or line objects).

Why they look like high-to-high / low-to-low polylines only in the Strategy Tester: on a live chart, bid/ask lines are horizontal lines at the current price, so Image 1 looks clean. The visual tester instead renders them as historical polylines — per bar it plots the extreme ask (≈ high + spread, hugging the highs, red) and the extreme bid (the lows, gray). Note the tester ignores `askline=0` and draws the ask line anyway when the bid line display is active — that's tester behavior, not something in your file.

Fix in the tpl: set `bidline=0` (and leave/keep `askline=0`), save, rerun. Or in the running tester chart: Properties → Show → untick Bid/Ask price lines.

Hypothesis (only unproven part): that the tester force-enables the ask line; everything else above is straight from the file and the pixel colors.

### Millard · 2026-07-06 14:03

changed the setting, the lines still appear.

See image. What is "show ticker"?

### Claude · 2026-07-06 14:03

"Show ticker" = the symbol info line in the chart's top-left corner ("XAUUSD, M1: Gold vs US Dollar") — nothing to do with ticks or the status box.

On the lines still showing: if you changed this dialog on the live chart, it won't touch the tester — the tester rebuilds its chart from tester.tpl on disk each run. If you changed it on the tester chart itself and the lines survived, my ask/bid hypothesis is dead — say which chart you changed and I'll dig further.

### Millard · 2026-07-06 14:05

I changed and saved the template on a live chart. You can't change that kind of thing on a chart in the ST itself.

### Claude · 2026-07-06 14:05

Then my hypothesis is unproven and the flag change disproves half of it. Two isolation tests, one rerun each:

1. In tester.tpl set `askline_color` and `bidline_color` to garish values (e.g. 65280 = lime, 65535 = yellow), rerun. Colors change → the lines ARE bid/ask lines and the tester ignores the on/off flags. Colors unchanged → not bid/ask lines at all.
2. If test 1 comes back unchanged: delete the entire BarID `<indicator>` block from tester.tpl, rerun. Lines gone → the tester is force-drawing those buffers despite `draw=0`. Lines remain → they're hard tester rendering, not controllable from the template.

Also confirm the saved file actually landed as `MQL5\Profiles\Templates\tester.tpl` and now reads `bidline=0` — worth 10 seconds before trusting either test.
