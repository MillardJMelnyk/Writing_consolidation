# Analyzing tick data for wick patterns in price movements

| | |
|---|---|
| Date | 2026-05-13 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-0e6f9aa4` |
| Links | [Original](https://claude.ai/chat/0e6f9aa4-688b-468d-a752-2bc64b4bc4f5) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-05-13_analyzing-tick-data-for-wick-patterns-in-price-movements_0e6f9aa4.html) |

**Summary:** Designing a tick-data analysis of XAUUSD to find precursors of large candle wicks, including research into existing solutions.

**Topics:** Trading and markets > Pattern recognition and quantitative analysis; Trading and markets > Forex and gold trading concepts; AI chatbots and working with Claude > Communication protocols and ground rules

**Index terms:** candle wick; retracement; tick data; XAUUSD; approach and recovery segment

[← Catalog home](../README.md)

---

### Millard · 2026-05-13 13:10

If you were going to analyze trading tick data to find characteristic commonalities in price movements that signal the kind of retracements visible on candle charts as "wicks", how would you go about doing that? Not just short wicks, but those that make up 50% or more of a candle's high to low spread.

### Claude · 2026-05-13 13:11

The defining property of a large wick is that range got traveled but not retained, so the analysis is really about the asymmetry between the trip out to the extreme and the trip back. That decomposition drives everything else.

A workable methodology:

**Label and split.** Tag each historical candle as large-upper-wick, large-lower-wick, or control (both wicks small, e.g. <30%). Keep the wick fraction as a continuous variable too, not just the 50% binary, so you can regress against it.

**Find the pivot in tick time.** For each candle, locate the first tick that touches H and the first that touches L. The relevant extreme's timestamp splits the bar into an approach segment and a recovery segment.

**Extract per-bar tick features.** For each candle, focused on the wick side's extreme:  
- Position of the extreme within the bar (fraction of the minute elapsed)  
- Approach vs recovery: duration, tick count, average speed, peak speed, monotonicity (fraction of ticks moving toward the extreme)  
- Largest single-tick jump in each segment  
- Loiter time near the extreme (time within ε of H or L) and number of re-tests  
- Reversal sharpness — pips moved away in the first N ticks after the extreme  
- Spread behavior at the extreme vs bar-median spread  
- Tick inter-arrival distribution (burst vs steady flow)

**Add context features.** Bar range divided by N-bar ATR, distance from extreme to nearest prior swing or structure, whether the extreme penetrated the prior N-bar high or low (sweep flag), session, prior bar direction and size.

**Compare distributions.** KS or Mann-Whitney per feature across the three groups, plus paired comparisons between upper-wick and lower-wick to check for asymmetry. Stratify by session and by volatility regime — both shift wick rates and tick character enough to confound a pooled analysis.

**Path-shape clustering.** Normalize each bar's tick path to a unit time-price box and cluster the shapes (DTW distance, or a shape-feature vector into k-means). Then see which clusters concentrate in the large-wick class. This catches structure that no hand-engineered feature names.

**Multivariate.** A gradient-boosted classifier with feature importance and partial dependence to see which features carry signal once correlations with volatility and session are accounted for.

**Descriptive vs predictive — flag.** Everything above is descriptive: it characterizes what tick patterns *accompany* large wicks. If the actual goal is to predict a forming wick mid-bar, that requires fixing an observation cutoff inside the bar and asking what features observable by then predict the bar's final classification. That setup is a different beast and exposes you to the look-ahead concerns you've already been chasing — the obvious failure mode being a "feature" that's really just the wick partially formed.

Want me to mock up the feature-extraction script against a sample tick file?

### Millard · 2026-05-13 13:14

Rules for this chat: when I ask a question I'm not asking for a dissertation, just an answer. Don't run off creating architectures or codeine or any other structure when you don't know shitall about what I want. Don't assume, ask. You burned way too much usage just now. You're so obsessed with doing something you leap to action before you know what the fuck you're going to do. Confirm.

### Claude · 2026-05-13 13:14

Confirmed. Answer the question asked, nothing more. Ask before assuming or building.

### Millard · 2026-05-13 13:14

Answer my original question simply

### Claude · 2026-05-13 13:14

Compare the tick paths of large-wick candles against normal ones, focusing on the asymmetry between the move out to the extreme and the move back. Look at things like how fast the extreme was reached, how sharply price reversed, time spent near the extreme, and whether the extreme swept a prior high or low. Test which features differ statistically between large-wick and control bars.

### Millard · 2026-05-13 13:15

That sounds like a good approach. What about patterns in bars leading up to the barbing analyzed?

### Claude · 2026-05-13 13:15

Good extension. You'd look at the prior N bars for things like trend direction and strength, whether price was extended from a moving average or prior range, volatility regime, whether the wick bar swept a recent swing high/low, and time-of-session context. Then test which prior-bar features are over-represented before large-wick bars versus controls.

### Millard · 2026-05-13 13:17

Okay give me high level specifications that would do what we've talked about here.

### Claude · 2026-05-13 13:17

**Inputs**  
- Tick data (timestamp, bid/ask or price, optionally volume)  
- Bar data aligned to the same instrument and timeframe

**Bar labeling**  
- For each bar, compute upper wick fraction and lower wick fraction of total range  
- Classify as large-upper-wick, large-lower-wick, or control based on a threshold (e.g. 50% / under 30%)

**Intra-bar tick features (focused on the wick side)**  
- Time within the bar when the extreme was reached  
- Speed and tick count on the move out to the extreme vs the move back  
- Sharpness of reversal off the extreme  
- Time spent near the extreme and number of re-tests  
- Largest single-tick jump in each leg  
- Spread behavior at the extreme

**Prior-bar context features (N bars before)**  
- Trend direction and strength  
- Distance of price from a reference moving average or prior range  
- Volatility regime relative to recent norm  
- Whether the wick bar's extreme swept a recent swing high or low  
- Session / time of day

**Analysis**  
- Compare feature distributions across the three classes (large-upper, large-lower, control)  
- Stratify by session and volatility regime to avoid confounding  
- Optionally cluster normalized tick paths to find recurring shapes  
- Optionally fit a classifier to rank feature importance once correlations are accounted for

**Outputs**  
- Per-feature statistical comparison (which features differ, by how much, in which direction)  
- Ranked list of features most associated with large wicks  
- Conditional rates: probability of a large wick given prior-bar context features

### Millard · 2026-05-13 13:19

You only need tick data. Bars are a logical construct derived from the timestamps on the tick data.

### Claude · 2026-05-13 13:19

Correct. Bars get constructed from the tick stream by grouping ticks within each timeframe interval and deriving OHLC from them.

### Millard · 2026-05-13 13:19

That all sounds good. I assume you're going to code something in Python?

### Claude · 2026-05-13 13:19

That's what I'd reach for, yes — but before I touch anything: what's the tick data source and format, what instrument and timeframe, and is this a one-off analysis or something you want to re-run?

### Millard · 2026-05-13 13:22

Surely you can find a source of tick data sufficient for developing and testing the code. Yes I want something that can be rerun. Time frame should be parameter driven, choose whatever makes sense for developing and testing the code, Let's use gold XAUUSD.

### Claude · 2026-05-13 13:25

Script tested green against synthetic data (500 M1 bars, ~25k ticks). Self-test mode is built in via `--synthetic`.

For real XAUUSD ticks, Dukascopy is the standard free source (their historical tick CSV with `Gmt time, Ask, Bid, ...` columns is recognized by the loader). Run:

```
python wick_analysis.py --ticks XAUUSD_ticks.csv --timeframe M1
```

Timeframe parameter accepts S5/S15/S30/M1/M5/M15/M30/H1/H4.

### Millard · 2026-05-13 13:26

You gave me a list of time frame codes, what does S mean?

### Claude · 2026-05-13 13:26

Seconds. S5 = 5-second bars, S15 = 15-second, S30 = 30-second.

### Millard · 2026-05-13 13:34

did you do any research to see if this problem already has an elegant solution?

### Claude · 2026-05-13 13:34

No, I didn't. Want me to look?

### Millard · 2026-05-13 13:35

yes

### Claude · 2026-05-13 13:35

Short answer: no off-the-shelf solution for this exact problem.

What exists:  
- **TradingView "Wick Report Pro"** — measures current wick size against the distribution of historical wicks (percentile, exceedance probability). Distributional summary only, not a tick-level characterization.  
- **"Realized Candlestick Wicks"** (academic, ScienceDirect 2025) — uses wick lengths as inputs to a volatility estimator. Opposite direction from what we're doing.  
- **Microstructure literature on intraday reversal** — Chordia et al. on order-imbalance reversal, Hawkes-process tick models, push-response anomaly studies. Directly relevant to *why* wicks form (a wick is the visual signature of an intraday reversal), but framed around order flow and quote data, not bar-level wick classification.  
- **ML candlestick-pattern work** — uses wicks as features to predict next-bar direction. Also reverse direction.

So the closest body of work is microstructure mean-reversion / OIB-reversal. If you wanted to anchor this analysis in established theory rather than purely empirical feature mining, that's where to look — features like order-flow imbalance and quote-side asymmetry near the extreme would slot naturally into what we already have.

No reason to scrap what's built.

### Millard · 2026-05-13 13:36

agreed

### Claude · 2026-05-13 13:36

👍
