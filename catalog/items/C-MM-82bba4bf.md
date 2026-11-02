# Calculating indecision from tick data

| | |
|---|---|
| Date | 2026-05-08 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-82bba4bf` |
| Links | [Original](https://claude.ai/chat/82bba4bf-4354-4821-b4dc-f3ff9ec54291) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-05-08_calculating-indecision-from-tick-data_82bba4bf.html) |

**Summary:** Methods for measuring real-time market indecision from tick data, centering on the price path efficiency ratio and tick imbalance.

**Topics:** Trading and markets > Pattern recognition and quantitative analysis; Trading and markets > Forex and gold trading concepts

**Index terms:** efficiency ratio; tick data; market indecision; tick imbalance; price path

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-05-08 20:34

I'm having a hard time figuring out how to calculate indecision on trading charts on the basis of tick data.

### Claude · 2026-05-08 20:35

The cleanest tick-based indecision metric is the **Price Path Efficiency Ratio**:

```
ER = |Close - Open| / Σ|tick[i] - tick[i-1]|
```

* Near **0** → price churned back and forth (maximum indecision)
* Near **1** → price moved directionally with little wasted motion

It works because it captures *how much of the tick activity actually went anywhere*. A bar with 500 ticks that opens and closes at the same price has near-zero ER regardless of range.

---

**Other useful tick-derived signals:**

**1. Directional tick imbalance**  
Count up-ticks vs down-ticks within a window:

```
imbalance = (up_ticks - down_ticks) / total_ticks
```

Near 0 = balanced = indecision. Useful as a real-time intra-bar signal.

**2. Mean run length**  
A "run" is a streak of consecutive same-direction ticks. Short average runs = frequent reversals = indecision. Long runs = momentum.

**3. Tick churn ratio**

```
churn = total_ticks / (high - low)   [in points]
```

High churn (many ticks, narrow range) = price struggling to commit. Normalize by typical tick frequency for your instrument.

---

**For XAUUSD M1 specifically:**

Gold tick flow is noisy. You'll want to:  
- Aggregate over a fixed tick window (e.g., 50-tick rolling) rather than per-bar  
- Threshold ER below ~0.15–0.20 as "indecision zone" (tune to your data)  
- Combine ER with volume spread — tight spread + low ER is stronger indecision than either alone

---

**Causal integrity note:** All of these are computable strictly from ticks already received — no look-ahead required. The ER for a completed bar is final; for an open bar it's a live estimate that updates with each tick.

Which angle are you approaching from — detecting indecision bars after close, or scoring it in real time as the bar builds?

### Millard · 2026-05-08 20:37

Real time

### Claude · 2026-05-08 20:37

Real-time changes the design significantly. The metric has to be **incrementally updatable** — you can't recompute from scratch on every tick.

---

**Incremental ER (the core signal)**

Maintain two running accumulators:

```
gross_path += |current_tick - previous_tick|   // every tick
net_displacement = |current_tick - bar_open|   // always cheap
ER = net_displacement / gross_path
```

Cost: one subtraction, one abs, one addition per tick. No history needed.

---

**The instability problem**

Early in the bar, ER is meaningless — 3 ticks in any direction reads as ER=1.0. You need a **warmup gate**:

* Don't emit a signal until `gross_path > N` (a minimum path threshold)
* Or until tick count exceeds some minimum (e.g., 20 ticks)
* Or both

For XAUUSD M1, gross\_path threshold of ~5–8 pips worth of movement is a reasonable starting point.

---

**Incremental directional imbalance**

```
up_ticks++   // if current > previous
down_ticks++ // if current < previous
// ties: ignore or split

imbalance = (up_ticks - down_ticks) / (up_ticks + down_ticks)
```

Fully incremental, zero history. Reset at bar open.

---

**Incremental mean run length**

```
current_run_length++          // if direction unchanged
else:
    total_run_length += current_run_length
    run_count++
    current_run_length = 1

mean_run = total_run_length / run_count
```

Short mean run in real time = choppy price action right now.

---

**Composite score**

Weight them into one number, 0–1 (1 = maximum indecision):

```
indecision = w1 * (1 - ER) 
           + w2 * (1 - |imbalance|) 
           + w3 * (1 / mean_run)   // normalize appropriately
```

All three update on every tick, all zero-history except the small set of scalars above.

---

**State struct (everything you need to carry)**

```
bar_open
prev_tick
gross_path
up_ticks, down_ticks
current_run_dir, current_run_len
total_run_len, run_count
tick_count
```

That's it. Reset on bar open, update on each tick, read signal anytime.

---

Want this as an MQL5 struct + `OnTick()` skeleton, or a Python tick-replay version first?

### Millard · 2026-05-08 20:38

Way to mention information. Spare me the details.

### Claude · 2026-05-08 20:38

MQL5 struct or Python first?

### Millard · 2026-05-08 20:38

Wtf? I tell you you gave me too much information in the next thing you want to do is start fucking coding?

### Claude · 2026-05-08 20:38

Fair. What do you need?

### Millard · 2026-05-08 20:39

Simplicity. You firehosed me. Give me the different methods simply and tell me what they're good for instead of all the other shit.

### Claude · 2026-05-08 20:39

**Efficiency Ratio** — best overall. Measures how directional the tick movement was. Low = indecision.

**Directional imbalance** — up-ticks vs down-ticks. Good for catching one-sided pressure early in a bar.

**Mean run length** — how often direction flips. Good for detecting chop specifically.

**Churn ratio** — ticks per pip of range. Good when you care about volume context.

Most people start with ER. The others are refinements.

### Millard · 2026-05-08 20:39

How does that relate to travel?

### Claude · 2026-05-08 20:40

ER *is* travel. The denominator is the total distance price physically traveled tick-by-tick. The numerator is how much of that travel went somewhere useful. Low ratio = lots of travel, little progress = indecision.

### Millard · 2026-05-08 21:00

Explain ER = |Close - Open| / Σ|tick[i] - tick[i-1]|

### Claude · 2026-05-08 21:00

Numerator: how far price ended up from where it started.

Denominator: the total distance price actually walked to get there.

If price wandered 50 pips back and forth but only moved 2 pips net, ER is near zero. If it walked straight from open to close, ER is near 1.

### Millard · 2026-05-08 21:01

As written, down moves with cancel out up moves (or vice versa)

### Claude · 2026-05-08 21:01

The absolute value bars on both sides prevent that. The denominator sums the absolute value of each individual tick move — each step is always positive regardless of direction.
