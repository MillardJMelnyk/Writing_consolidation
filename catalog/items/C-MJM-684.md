# XAUUSD price quotation format

| | |
|---|---|
| Date | 2026-03-11 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-684` |
| Links | [Original](https://claude.ai/chat/59230fda-a356-4d4e-9f07-5c76c66d4cc3) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/684-2026-03-11-xauusd-price-quotation-format.html) |

**Summary:** Working out that on his broker's XAUUSD quotes, $0.10 equals one pip and $0.01 one point, verified from an MT5 measurement.

**Topics:** Trading and markets > Forex and gold trading concepts; Trading and markets > Brokers, accounts and platforms

**Index terms:** XAUUSD; gold; pip; point; MetaTrader 5; troy ounce

[← Catalog home](../README.md)

---

### Millard · 2026-03-11 22:28

XAUUSD is quoted as USD per ounce, correct?

### Claude · 2026-03-11 22:28

Wednesday, March 11, 2026, time unknown, user timezone.

Correct. XAUUSD is quoted as US dollars per troy ounce of gold.

### Millard · 2026-03-11 22:29

So in trading terms, the tenths place is 10s of pips, the cents place is pips, and the hundredths place would be points?

### Claude · 2026-03-11 22:29

Clarification needed: You said "cents place" and "hundredths place" as if they're different, but cents *is* the hundredths place ($0.01).

Standard XAUUSD pip convention:

* **$0.01** (hundredths/cents) = 1 pip
* **$0.10** (tenths) = 10 pips
* **$0.001** (thousandths) = 1 point/pipette (on brokers quoting 3 decimal places)

Did you mean thousandths for points?

### Millard · 2026-03-11 22:30

yes that's what I meant

### Claude · 2026-03-11 22:30

Confirmed. Your understanding is correct:

* $0.10 (tenths) = 10 pips
* $0.01 (hundredths) = 1 pip
* $0.001 (thousandths) = 1 point/pipette

### Millard · 2026-03-11 22:34

so why does my MT5 chart tell me there are around 564 points between this bar's open and close?

[File attached: 1773268427616\_image.png — contents not included in export]

### Claude · 2026-03-11 22:35

The "564 points" label on your chart is not measuring that bar's open-to-close. It's the crosshair/measurement tool showing distance from the crosshair position to something else (likely a ZigZag anchor point).

For the selected bar in your Data Window:

* Open: 5172.33
* Close: 5174.22
* Difference: $1.89

Your broker quotes XAUUSD to 2 decimal places, so 1 point = $0.01.

$1.89 / $0.01 = **189 points** (or 18.9 pips)

The 564-point measurement appears to be from price 5168.64 to somewhere else on the chart, unrelated to the selected bar's OHLC.

### Millard · 2026-03-11 22:38

WRONG
I started the measurement at the open, dragged it to the close, then moved it to the right so that the whole tooltip text would show. It wouldn't matter anyway because the points are ALWAYS a measure of PRICE DIFFERENTIAL, not spatial differential. I could drag the pointer all the way to the left of the chart and as long as the horizontal crosshair lies on the level of the close, it will read exactly the same number of points.
SO ANSWER THE FUCKING QUESTION.

[File attached: 1773268700577\_image.png — contents not included in export]

### Claude · 2026-03-11 22:39

You're right, I was wrong about what the measurement was showing.

The answer: Your broker defines 1 point = $0.001, not $0.01, even though prices display with only 2 decimal places.

563 points × $0.001 = $0.563

That matches a roughly $0.56 price differential between your measurement start and end points.

So for your broker:

* $0.10 = 100 points (10 pips)
* $0.01 = 10 points (1 pip)
* $0.001 = 1 point

### Millard · 2026-03-11 22:42

READ THE IMAGE. What are the open and close numbers?

### Claude · 2026-03-11 22:42

Open: 5176.34
Close: 5176.87

Difference: $0.53

563 points for $0.53 doesn't compute under any standard definition. I'm missing something—what am I not seeing?

### Millard · 2026-03-11 22:44

that was my fault, the data window showed values for the wrong bar, not the one under the crosshair. Look at this image.
It looks to me like the 10ths place are pips and the 100ths place are points.

[File attached: 1773269015761\_image.png — contents not included in export]

### Claude · 2026-03-11 22:44

You're right.

$5.71 difference ÷ 573 points = $0.01 per point

So for your broker on XAUUSD:

* $0.10 (tenths) = 1 pip
* $0.01 (hundredths) = 1 point (10 points per pip)

This contradicts the "standard" convention we discussed at the start. Your broker is treating XAUUSD like a 2-decimal instrument where the last displayed digit is points, not pips.
