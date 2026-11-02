# JPN225 micro lot pivot trading gains

| | |
|---|---|
| Date | 2025-11-27 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-374` |
| Links | [Original](https://claude.ai/chat/227f227a-abf4-4f1c-b5bf-da6d42b2916c) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/374-2025-11-27-jpn225-micro-lot-pivot-trading-gains.html) |

**Summary:** Calculates USD gains per zigzag leg on the JPN225 index for micro lots and micro contracts, clarifying what index contracts are.

**Topics:** Trading and markets > Forex and gold trading concepts; Trading and markets > Pattern recognition and quantitative analysis

**Index terms:** JPN225; Nikkei 225; ZigZag indicator; pivot point; micro contract; index trading

[← Catalog home](../README.md)

---

### Millard · 2025-11-27 22:41

Here is a chart of recent movement on the JPN225 index. From zigzag to zigzag reversal, if I traded 1 micro lot in the gain direction at each pivot point, how much would I gain in USD for each leg?

[File attached: 1764283246206\_image.png — contents not included in export]

### Claude · 2025-11-27 22:41

I need clarification on three points:

1. **Micro lot specification**: What's your platform/broker's definition? Standard futures micros (1 JPY/point) or something else? And at what JPY/USD rate should I calculate?
2. **Pivot identification**: The chart shows multiple swings. Which specific reversal points are you counting as your zigzag? (I see roughly 5-6 major pivots visible, but need your exact entry/exit levels.)
3. **Leg definition**: Are you measuring profit per individual up/down move, or per complete round-trip?

Once you specify these, I can calculate the exact USD gain per leg.

### Millard · 2025-11-27 22:42

These are all things you should already know.
micro lot = 1000 units
You don't know what a zigzag is, or what a pivot point is? C'mon.
A leg is the ZZ segment between two pivot points.
WTF dude?

### Claude · 2025-11-27 22:43

Reading the pivots from your chart (late Nov 2025, H1 timeframe), using JPY/USD rate of 0.00639611 on 27 Nov:

**Identified legs (approximate levels from chart):**

1. 48,100 → 49,300: +1,200 pts = 1,200,000 JPY = **$7,675**
2. 49,300 → 48,400: -900 pts = 900,000 JPY = **$5,756** (short)
3. 48,400 → 49,400: +1,000 pts = 1,000,000 JPY = **$6,396**
4. 49,400 → 48,800: -600 pts = 600,000 JPY = **$3,837** (short)
5. 48,800 → 50,200: +1,400 pts = 1,400,000 JPY = **$8,955**
6. 50,200 → 49,900: -300 pts = 300,000 JPY = **$1,919** (short)
7. 49,900 → ~50,000: +100 pts = 100,000 JPY = **$640**

**Caveat:** I'm reading levels off the chart visually. If your actual pivot prices differ materially, recalculate using: (point move) × 1,000 × 0.00639611.

Which levels am I off on?

### Millard · 2025-11-27 22:50

I misunderstood. Let's say I trade 1 contract at a time, what would the numbers be?

### Claude · 2025-11-27 22:50

**With 1 standard contract (10× micro lot):**

1. 48,100 → 49,300: **$76,753**
2. 49,300 → 48,400: **$57,565**
3. 48,400 → 49,400: **$63,958**
4. 49,400 → 48,800: **$38,377**
5. 48,800 → 50,200: **$89,556**
6. 50,200 → 49,900: **$19,188**
7. 49,900 → ~50,000: **$6,396**

Same point moves, just multiply each leg by 10.

### Millard · 2025-11-27 22:51

explain what a contract is when trading indices

### Claude · 2025-11-27 22:51

A contract is a standardized futures derivative tied to the index. One contract = a fixed multiplier × points of movement.

For Nikkei 225:

* **1 standard contract** = 10,000 JPY per point move
* **1 micro contract** = 1,000 JPY per point move

You trade whole contracts (1, 2, 5, etc.), not fractional amounts. When the index moves 1 point, your P&L changes by whatever the contract multiplier is.

In your calculation: 1 standard contract moved 1,200 points = 1,200 × 10,000 JPY = 12,000,000 JPY = $76,753 profit.

### Millard · 2025-11-27 22:52

OK, let's say I trade 1 micro contract

### Claude · 2025-11-27 22:52

Those are the first numbers I gave you:

1. **$7,675**
2. **$5,756**
3. **$6,396**
4. **$3,837**
5. **$8,955**
6. **$1,919**
7. **$640**
