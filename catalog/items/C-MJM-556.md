# Pepperstone Razor vs Standard accounts

| | |
|---|---|
| Date | 2026-01-01 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-556` |
| Links | [Original](https://claude.ai/chat/2a1c3378-dc97-4d86-9eb4-91a28646c97e) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/556-2026-01-01-pepperstone-razor-vs-standard-accounts.html) |

**Summary:** Compares Pepperstone Razor and Standard account costs and spreads, and explains bulk-compiling MQ5 files via MetaEditor command line.

**Topics:** Trading and markets > Brokers, accounts and platforms; Trading and markets > Forex and gold trading concepts

**Index terms:** Pepperstone; Razor account; spread; commission; MetaEditor; MetaTrader 5

[← Catalog home](../README.md)

---

### Millard · 2026-01-01 16:05

I'm opening a demo trading account with Pepperstone. I see this on the set up page. Tell me about Razor and Standard accounts.

[File attached: 1767283511376\_image.png — contents not included in export]

### Claude · 2026-01-01 16:05

**Razor Account:**

* Raw spreads from 0.0 pips with a commission charge applied. Popular with scalpers and for clients running Expert Advisors.
* Commission: USD 3.50 per side ($7 round-turn) per standard lot on MT4/MT5; USD 6 round-turn on cTrader.
* Typical all-in cost: ~0.6 pips on EUR/USD (spread + commission).

**Standard Account:**

* 1 pip markup on the raw spread with no commissions charged. Popular for those wanting a simple account—perfect for beginners who prefer having the commission built into the spread.
* Typical EUR/USD spread: ~1.0 pip during liquid sessions.

**Bottom line for cost:**
The Razor Account wins on raw pricing and lower total cost, making it ideal for active, high-volume, and algorithmic traders.

For a demo account, the choice doesn't affect you financially—pick whichever pricing model you want to practice with. If you plan to eventually trade live with any frequency, Razor will be cheaper per trade despite the commission.

### Millard · 2026-01-01 16:06

At what point does the razor account make sense?

### Claude · 2026-01-01 16:06

**Cost comparison per trade:**

| Lot Size | Standard Cost (1 pip spread) | Razor Cost (0 pip + commission) |
| --- | --- | --- |
| 0.01 (micro) | $0.10 | ~$0.04 |
| 0.1 (mini) | $1.00 | ~$0.70 |
| 1.0 (standard) | $10.00 | ~$7.00 |

Razor is cheaper from the first trade at any lot size.

**Why Standard exists:**
Simplicity. No separate commission line to track. Some traders prefer seeing one all-in spread rather than calculating spread + commission.

**Practical answer:**
If you care about cost at all, Razor makes sense immediately. Standard is only advantageous if you value simplified accounting over saving ~30% per trade.

### Millard · 2026-01-01 16:08

the information you gave is contradictory. It's either $7 round-trip per trade or not.

### Claude · 2026-01-01 16:08

You're right. I conflated commission with total cost.

**Corrected breakdown for 1 standard lot EUR/USD:**

**Razor:**

* Commission: $7 round-turn (fixed)
* Spread: ~0.1-0.2 pips average = ~$1-2
* **Total: ~$8-9**

**Standard:**

* Commission: $0
* Spread: ~1.0 pip = $10
* **Total: ~$10**

Razor saves ~$1-2 per standard lot, not $3.

For micro lots (0.01), the savings are negligible—roughly $0.01-0.02 per trade. At that scale, the simplicity argument for Standard has more weight.

**Revised answer:** Razor makes meaningful sense when you're trading at least 0.1 lots regularly. Below that, the cost difference is trivial.

### Millard · 2026-01-01 16:09

what lot size would = $7?

### Claude · 2026-01-01 16:10

On Standard (1 pip spread):

1 pip = $10 per standard lot

$7 ÷ $10 = **0.7 lots**

At 0.7 lots, Standard spread cost = Razor commission. Below that, Razor's fixed $7 commission exceeds Standard's spread cost.

### Millard · 2026-01-01 16:10

So the spread is lower for Razor?

### Claude · 2026-01-01 16:11

Yes. Razor spread is near zero; Standard spread is ~1 pip.

I made an error. The $7 commission scales with lot size—it's $7 *per standard lot*, not a flat fee.

**Corrected:**

| Lot Size | Standard (1 pip spread) | Razor (~0 spread + commission) |
| --- | --- | --- |
| 0.01 | $0.10 | ~$0.07 |
| 0.1 | $1.00 | ~$0.70 |
| 1.0 | $10.00 | ~$7.00 |

Razor is ~30% cheaper at all lot sizes. My earlier statement about the breakeven at 0.7 lots was wrong.

### Millard · 2026-01-01 16:57

isn't there a way in the MT5 editor to compile MQ5 files in bulk?

### Claude · 2026-01-01 16:58

No built-in "Compile All" button in MetaEditor's GUI. F7 compiles the currently open file only.

**Command line method:**

```
metaeditor64.exe /compile:"MQL5\Experts" /include:"MQL5" /log
```

This compiles all MQ5 files in the specified folder. You can point `/compile:` at a directory rather than a single file.

**Full example batch script:**

```
SET MT5_PATH="C:\Program Files\MetaTrader 5\metaeditor64.exe"
%MT5_PATH% /compile:"MQL5\Experts" /include:"MQL5" /log
%MT5_PATH% /compile:"MQL5\Scripts" /include:"MQL5" /log
%MT5_PATH% /compile:"MQL5\Indicators" /include:"MQL5" /log
```
