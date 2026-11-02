# ZigZag indicator parameters explained

| | |
|---|---|
| Date | 2026-01-05 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-562` |
| Links | [Original](https://claude.ai/chat/4bec3014-549f-4f6c-b467-d90c39d2e46c) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/562-2026-01-05-zigzag-indicator-parameters-explained.html) |

**Summary:** Explains how ZigZag indicator Depth, Deviation and Backstep parameters shape plotted pivots, agreeing Backstep's minimum meaningful value is 2.

**Topics:** Trading and markets > Pattern recognition and quantitative analysis; Trading and markets > Forex and gold trading concepts

**Index terms:** ZigZag indicator; depth; deviation; backstep; swing pivot

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-01-05 22:04

Explain in simple terms how the 3 typical parameters for a ZigZag indicator affect the plotted lines.

### Claude · 2026-01-05 22:04

The three typical ZigZag parameters:

**1. Depth**
Minimum number of bars that must separate swing highs and lows. Higher depth = fewer, more spaced-out zigzag points. Lower depth = more frequent reversals plotted.

**2. Deviation**
Minimum price movement (in percentage or points) required to register a new swing point. Higher deviation = only larger price moves create zigzag lines, filtering out smaller fluctuations. Lower deviation = more sensitive, captures smaller reversals.

**3. Backstep**
Minimum bars between two consecutive extremes on the same side (two highs or two lows). Prevents the indicator from plotting multiple swing points too close together. Higher backstep = more separation enforced between same-type swings.

**Net effect:** Increasing all three makes the ZigZag filter out more noise and show only major trends. Decreasing them makes it more responsive but noisier.

### Millard · 2026-01-05 22:05

So Backstep prevents pivots (at top or at bottom) from being too close?

### Claude · 2026-01-05 22:06

Yes. Backstep prevents two pivots of the **same type** from being too close together:

* Two swing highs can't be closer than backstep bars apart
* Two swing lows can't be closer than backstep bars apart

It does NOT restrict distance between a high and a low - that's controlled by Depth.

### Millard · 2026-01-05 22:08

when you say "bars apart", by definition, two pivots of the same type MUST have a least one bar in between them, so the minimum reasonable value for Backstep would be 2, right?

### Claude · 2026-01-05 22:08

Correct. Two same-type pivots inherently require at least one intervening bar to form the opposite movement between them.

So backstep = 2 is the minimum meaningful value. Backstep = 1 would be redundant since that scenario is already structurally impossible.
