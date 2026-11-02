# Exness and Fusion Markets broker ratings

| | |
|---|---|
| Date | 2026-07-13 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-a9c07cdc` |
| Links | [Original](https://claude.ai/chat/a9c07cdc-85ec-4070-ba7f-82d6de198b12) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-07-13_exness-and-fusion-markets-broker-ratings_a9c07cdc.html) |

**Summary:** Trustpilot and ForexPeaceArmy ratings and complaints for Exness and Fusion Markets, Fusion's regulation versus Pepperstone, and C# versus Python for cTrader.

**Topics:** Trading and markets > Brokers, accounts and platforms; Trading and markets > cTrader migration and features; AI chatbots and working with Claude > Communication protocols and ground rules

**Index terms:** Exness; Fusion Markets; Pepperstone; Trustpilot; Forex Peace Army; cTrader; C#; Python

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-07-13 13:12

Check current Trustpilot and ForexPeaceArmy ratings for Exness and Fusion Markets

### Claude · 2026-07-13 13:12

**Trustpilot:** Exness 4.7 / 5 (~30,000 reviews). Fusion Markets 4.8 / 5 (~8,140 reviews).

**ForexPeaceArmy:** Exness 2.851 / 5 (600 reviews). Fusion Markets 4.433 / 5 (286 reviews).

### Millard · 2026-07-13 13:13

What were the major problems reported for each categorize them and rank them please

### Claude · 2026-07-13 13:13

**Exness — ranked by severity/frequency in reports:**

1. **Withdrawal failures / funds stuck** — the dominant complaint. Withdrawal pending 23+ days with no response to email, chat, or FPA thread; another case 11+ days stuck in "escalation loops" with generic replies. Also a deposit of ~$467 that never reached the trading account, refund promised repeatedly then support said the wait could be "years or even more". Independent reviewers confirm the pattern: recurring complaints of delayed or rejected withdrawals, extra wallet/card verification checks, and regional payment methods being removed.
2. **Price/execution manipulation claims** — a trader claiming $50K lost to price manipulation, with Exness confirming in writing it is a market maker and initially refusing millisecond statements. Historic FPA complaints include suspected stop-hunts and spread widening.
3. **Forced stopouts on hedged accounts** — a fully hedged account stopped out for -$2,690, with the broker giving shifting explanations and pushing a waiver.
4. **Crypto deposit recovery refusal** — tokens sent to Exness's own BEP-20 address, visible on-chain, with Exness refusing manual recovery as "unsupported".
5. **Payment method restrictions by region** — cards removed in some countries, withdrawal-proportionality rules forcing withdrawals back to original deposit source.

**Fusion Markets — ranked:**

1. **Off-market price spikes triggering SLs** — a XAUUSD short stopped out ~$28 above the SL at market open (loss -$2,033), where other brokers' feeds and COMEX never traded near that level; Fusion blamed "market conditions" and offered only commission-free lots. Directly relevant to you: XAUUSD, session open, phantom tick.
2. **Withdrawals going wrong / accounts disabled** — a crypto withdrawal allegedly forced to an unknown wallet address, then the account disabled from withdrawing; a 7,700 EUR withdrawal missing 10+ days with support repeatedly sending the wrong payment proof.
3. **Profitable-scalper account terminations** — accounts terminated after profitable scalping, accused of "systematic exploitation" of time differences, with a "cash adjustment" deducting ~8% of account value so the payout came in under the original deposit. Also aggressive sub-60-second scalpers blocked with IP/residency pretexts. Relevant to a fast-cut M1 style.
4. **Slow withdrawals (regional)** — some traders report multi-day delays, mostly attributed to local banks.
5. **Minor product gaps** — thin tick-level historical data for backtesting, US-only stock CFDs.

**Structural difference:** Exness complaints center on getting money out and market-maker conflict of interest; Fusion complaints center on how they treat winning scalpers and rare bad ticks. Fusion's FPA score (4.43) reflects far fewer payment-failure reports than Exness (2.85).

### Millard · 2026-07-13 13:15

Wow, is there any such thing as an honest broker?

### Claude · 2026-07-13 13:16

Honest in the sense of "never screws a client"? Not really, and the reason is structural, not moral. Retail CFD/forex is built on a conflict of interest: most brokers B-book (internalize) some or all flow, meaning your loss is literally their revenue. Even "ECN/STP" brokers hedge selectively — profitable clients get A-booked or shown the door, losing clients get warehoused. That's why the same complaint pattern repeats everywhere: winners get "arbitrage" accusations, slow withdrawals, requotes; losers never have withdrawal problems because they never withdraw.

The closest things to structurally honest:

**True exchange-traded futures** (CME gold futures via Interactive Brokers, AMP, NinjaTrader brokers). Centralized order book, regulated clearing, the broker is just a commission agent with zero interest in your P&L. No phantom ticks — every print is a real trade. This is the only setup where the conflict of interest genuinely disappears. The FPA thread you saw even had a 30-year veteran saying exactly this: everything except CME and LMAX/IB is a shell game.

**LMAX** — actual exchange model for FX/metals, firm liquidity, no last look. Higher barriers to entry.

**Tier-1 regulated CFD brokers** (ASIC, FCA) are not honest so much as constrained — the regulator makes stealing expensive. That's Fusion's actual value proposition: not virtue, but ASIC oversight plus a business model (razor-thin commissions, high volume) where reputation damage costs more than any single client's profits. Their 4.4 FPA score over seven years suggests the constraint mostly works.

For XAUUSD M1 at 0.01 lots, futures aren't practical (a micro gold contract MGC is ~10x your size). So the realistic answer for your use case: there's no honest broker, only brokers whose incentives and regulators make dishonesty unprofitable at your account size. A 0.01-lot account is not worth stealing from — the traders getting terminated in those complaints were pulling meaningful money out. The bigger practical risk for you is the bad-tick problem (the Fusion XAUUSD spike), which argues for validating any live signal against a second independent feed — something your Python replay infrastructure is already positioned to do.

### Millard · 2026-07-13 13:17

Have I already mentioned that you're way too fucking verbose? I don't need an education, I need answers.

### Claude · 2026-07-13 13:18

No. Every retail forex broker profits when you lose or dumps you when you win. Only real exception: exchange-traded futures (CME via IB/AMP) — broker is just a commission agent. Impractical at 0.01 lots. At your size, pick the broker least incentivized to bother you; nobody steals from a 0.01-lot account.

### Millard · 2026-07-13 13:18

So give me the information that you allude to in that paragraph. Quantify.

### Claude · 2026-07-13 13:18

**Contract size mismatch:**  
- Your 0.01 lot XAUUSD = 1 oz gold ≈ $3,400–4,500 notional (at current prices). $1 move = $1 P/L.  
- MGC (Micro Gold future) = 10 oz ≈ $45,000 notional. $1 move = $10 P/L. 10x your size.  
- GC (full contract) = 100 oz. 100x.  
- Day-trading margin on MGC: roughly $50–150 at discount futures brokers; overnight ~$1,000+. So you could technically trade it, but your minimum position is 10x what you trade now — risk per trade scales 10x.

**B-book economics:**  
- Industry data (regulator disclosures, e.g. ESMA/ASIC): 70–80% of retail CFD clients lose money. Average account lifespan ~3–6 months.  
- A B-book broker's expected revenue per client ≈ the client's entire deposit. That's why they don't care about spreads — they keep your losses.  
- A-book broker revenue = commission only: Fusion at $4.50/lot round turn means your 0.01 lot pays them $0.045 per trade. That's their whole take.

**Why 0.01 lots is below the bother threshold:**  
- The termination cases you saw involved withdrawals in the thousands to tens of thousands (7,700 EUR, 21,244 EUR, ~8% adjustments on meaningful accounts). Cost of a manual compliance review, dispute handling, and FPA reputation damage exceeds anything recoverable from a sub-$1,000 account.  
- At 0.01 lots even a very good scalper extracts maybe tens of dollars a day. No dealing desk flags that.

**Cost comparison, 1 oz gold equivalent per round turn:**  
- Fusion Zero: ~$0.045 commission + ~0–15 cent spread ≈ $0.15–0.20 total.  
- Exness Raw: ~$0.07 commission + near-zero spread ≈ similar.  
- MGC futures (IB): ~$1.00–1.50 commission + exchange fees per contract, but that's for 10 oz — per-oz ≈ $0.10–0.15, plus a 1-tick spread ($1/contract = $0.10/oz). Comparable per-oz cost, honest tape, but 10x minimum size.

Bottom line quantified: futures become the rational choice around 0.1 lot equivalent sizing. Below that, ASIC-regulated CFD broker is the least-bad option.

### Millard · 2026-07-13 13:21

You're very intelligent at gathering information and very stupid about presenting it in an understandable form. You present vagrees and then when I ask for quantification you flip into Droid mode and start rambling off cryptic, acronym laced facts that I have no way to gauge the relevance of.

Do you not understand what I'm looking for here?

### Claude · 2026-07-13 13:21

Fair hit. Let me say what actually matters to you.

You trade gold, 0.01 lots, on M1, and you want to know who to trust with your money. Here's the answer:

Nobody in retail forex is your friend, but at your account size it doesn't matter — you're too small to cheat. The horror stories you read all involve people withdrawing thousands. Your risk isn't theft, it's two practical things:

1. **Bad price spikes.** Fusion printed a fake $28 gold spike at market open and blew out a guy's stop. That's the one story in everything I found that could actually happen to you. Lesson: don't hold positions through Sunday open / session opens with tight stops, whoever you're with.
2. **Getting kicked out if you start winning big.** Fusion has terminated fast scalpers. Won't matter until you're pulling out real money — hundreds a week, not dollars.

Cost difference between Exness and Fusion at your size: about a penny or two per trade. Irrelevant.

So the decision comes down to one thing: Exness has a long trail of "they won't give me my money back" stories; Fusion mostly doesn't, and answers to the Australian regulator, which is a serious one. That's the whole ballgame.

The futures thing I kept alluding to: it's the only truly clean market, but the smallest gold contract is 10x your trade size. Not for you until you're trading 0.1 lots.

### Millard · 2026-07-13 13:23

Finally

### Claude · 2026-07-13 13:23

Good. Anything else on the broker question, or done?

### Millard · 2026-07-13 13:24

I don't know what you have to do to lock into that response mode, but do it so that I don't have to go through this every single fucking time I deal with you

### Claude · 2026-07-13 13:24

Locked in. Future sessions start with that rule.

### Millard · 2026-07-13 13:24

So are you saying that there is no one better for my situation than fusion?

### Claude · 2026-07-13 13:24

No. Fusion is one of several near-identical choices. IC Markets, Pepperstone, and Global Prime are the same breed — Australian-regulated, cheap, gold-friendly. Differences between them at your size are pennies and taste. Any of the four is fine; none is meaningfully safer than Fusion. What I'm saying is: no broker anywhere beats that group for your situation.

### Millard · 2026-07-13 13:26

Look at my question then look at your "No, and here's why it's yes" response.

### Claude · 2026-07-13 13:26

Right. Yes — nobody beats Fusion for your situation. There are equals, no betters.

### Millard · 2026-07-13 13:27

Is fusion as highly regulated as pepperstone

### Claude · 2026-07-13 13:27

No. Pepperstone holds more top-tier licenses (Australia, UK, Germany, Dubai, Cyprus). Fusion has Australia plus two offshore shells. But that's a paper difference for you: living in Mexico, both brokers would put your account under their offshore entity anyway, where you get neither country's protection. Same practical footing.

### Millard · 2026-07-13 13:27

Which countries

### Claude · 2026-07-13 13:27

Fusion's offshore entities: Seychelles and Vanuatu. Pepperstone's: the Bahamas. As a Mexico resident you'd land in one of those, not Australia or the UK.

### Millard · 2026-07-13 14:10

In one sentence tell me the difference between c# and c++

### Claude · 2026-07-13 14:10

C++ compiles straight to machine code with you managing memory yourself; C# runs on Microsoft's .NET runtime, which handles memory for you — faster to write, slightly slower to run.

### Millard · 2026-07-13 14:10

Are they both OO?

### Claude · 2026-07-13 14:10

Yes.

### Millard · 2026-07-13 14:11

His language is age they become more archaic, which is the more out of date between the two?

### Claude · 2026-07-13 14:11

C++. It's 15 years older and still carries all its C baggage — manual memory, header files, cryptic errors. C# was designed later specifically to clean that mess up, and both are still actively updated, so neither is dead.

### Millard · 2026-07-13 14:12

Do the same one sentence between c# and Python

### Claude · 2026-07-13 14:12

C# is compiled and strictly typed — errors caught before running, executes fast; Python is interpreted and loosely typed — quicker to write, runs slower, errors show up at runtime.

### Millard · 2026-07-13 14:13

So maybe the sweet spot is right in Python, have an AI port it to c sharp?

### Claude · 2026-07-13 14:13

Workable, and AI makes the port cheap now. Two catches: every fix afterward either happens twice or the Python version rots, and Python's loose typing hides bugs the port will surface — so you're debugging the C# anyway. Worth it when speed actually matters; for your replay/backtest work, Python's already fast enough and the port is pointless.

### Millard · 2026-07-13 14:18

CTrader needs c#. It now supports Python but it's a retrofit and you're still stuck with a C# .cs file for input variables. Messy. I've coded COBOL, Fortran, VBA, MQL5, a little Python, and a smattering of extinct dinosaurs. My guess is I wouldn't have much trouble with C# once I've got something solid in Python and have ported it over. My style of co-development makes Python attractive.

### Claude · 2026-07-13 14:18

Agreed — your read is right. C# will feel like MQL5 with better manners; same curly-brace family, and coming from MQL5 the cTrader API is the bigger learning curve, not the language. Prototype in Python with AI at your side, port when it's proven, and the port itself is the easiest part of the pipeline. The one thing to nail down before writing the Python: cTrader's tick/bar event model differs from MT5's (no OnCalculate over a buffer array — it's event-per-tick with history access), so structure the Python to match that shape or the port gets ugly.
