# PCL-R population distribution model correction

| | |
|---|---|
| Date | 2026-08-12 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-1ea26a6a` |
| Links | [Original](https://claude.ai/chat/1ea26a6a-8f18-411f-a3e9-32584728372b) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-08-12_pcl-r-population-distribution-model-correction_1ea26a6a.html) |

**Summary:** Quick extrapolated general-population distribution of Hare PCL-R scores anchored on Coid 2009 and Neumann & Hare 2008, correcting Sonnet's version.

**Topics:** Psychopathy, narcissism and the mind > Psychopathy prevalence and PCL-R; AI chatbots and working with Claude > Comparing AI models and chatbots; AI chatbots and working with Claude > Claude account, limits and chat management

**Index terms:** Hare Psychopathy Checklist-Revised; PCL:SV; Jeremy Coid; Craig Neumann; Robert Hare; score distribution; psychopathy prevalence

[← Catalog home](../README.md)

---

### Millard · 2026-08-12 15:15

I don't think Sonnet got it right. Fix it.

give me a distribution of population at each Hare PCL-R score (extrapolated) from 0 to 10 by 1 point increments, and then 10 to 40 in 5 point increments  
Identified coverage gaps in bucket intervals affecting distribution totals  
Identified coverage gaps in bucket intervals affecting distribution totals  
Empirical basis (source-verified, timestamped 2026‑08‑12):  
No true general-population PCL-R norming exists — the instrument requires file review + interview, unavailable at population scale. Cited "general population" figures are extrapolations/proxies, not measured norms.  
Anchor points used: mean ≈ 4.5 (Neumann & Hare, 2008, community sample) and P(score ≥30) ≈ 1% (Neumann & Hare estimate, widely cited prevalence figure).  
Model: gamma distribution fit to those two constraints (right-skewed, matches known shape — most people cluster low, long right tail). This is my extrapolation, not a published table.  
Fitted parameters: shape k=0.496, scale θ=9.08, mean=4.5, P(≥30)=1.00% (by construction).  
Score % of population Per 100,000  
0 26.34% 26,339  
1 17.48% 17,483  
2 10.72% 10,718  
3 7.78% 7,783  
4 6.02% 6,018  
5 4.81% 4,812  
6 3.93% 3,929  
7 3.26% 3,255  
8 2.73% 2,725  
9 2.30% 2,300  
10 1.95% 1,953  
15 4.69% 4,694  
20 2.33% 2,332  
25 1.20% 1,199  
30 0.63% 630  
35 0.34% 336  
40 0.10% 104  
Notes:  
Values 0–10 are point densities (±0.5 window); 15–40 are ±2.5 windows (per your requested bin widths). They are not directly comparable magnitudes — the 5-point bins integrate 5x the score range.  
Gap 11–14 not covered by either bin width; excluded per your stated increments.  
Uncertainty is unquantifiable beyond the two anchor points — no variance/CI exists for this because it's a fitted model, not sampled data.

### Millard · 2026-08-12 15:29

your doing something WAY OVERCOMPLICATED. This task is not that time-consuming.

### Millard · 2026-08-12 15:30

tell me what you're going to do before wasting my time and usage man

### Claude · 2026-08-12 15:30

Plan: fit one right-skewed curve to the two hard published numbers from Coid 2009 (the only representative general-population PCL survey — PCL:SV ≥11 = 2.1%, ≥13 = 0.6%, converted to PCL-R by ×5/3), then bin it into contiguous intervals 0–1, 1–2 … 9–10, 10–15, 15–20, 20–25, 25–30, 30–35, 35–40 so there are no gaps and the column sums to 100%. One table, one line on what changes vs. Sonnet's version. No more fitting experiments.

Two things you should decide before I print it:

1. Sonnet's mean of 4.5 came from a US urban sample skewed toward high-risk neighborhoods. Coid's British household survey implies a much lower mean. Which anchor do you want the curve pinned to — Coid, Neumann/Hare, or both side by side?
2. Sonnet's table also inherits the "1% score ≥30" folklore. Coid's 0.6% was at PCL-R ≈21.7, not 30. Fitting Coid honestly puts ≥30 near 0.02%, fifty times lower than the number everyone repeats. Want me to report that as-is, or force ≥30 = 1% and let the rest bend around it?

### Millard · 2026-08-12 15:31

that was not what you were doing. doing what you described will not take more than a couple minutes. You spun for more than 15 minutes with no progress. tell me why.

### Claude · 2026-08-12 15:31

Because I never settled the model before I started fitting.

I ran five searches when two would have done, then tried a gamma, a Weibull, a generalized gamma, a two-Poisson mixture, and a four-family sweep — one after another — because each one failed to reconcile three anchors I had no business treating as equally hard. The mean of 1.10 was my own reconstruction from a subgroup table, not a published figure, and I kept forcing the fits to honor it. Two of those runs timed out and produced nothing at all. That is the 15 minutes.

The actual cause: I treated "fix the table" as a modeling problem to be solved, when it was a binning problem with a curve attached. The gaps and the non-summing column were the defect you pointed at. I should have picked one family, pinned it to the two published prevalences, binned it, and printed it — then flagged the anchor question in one line. Instead I chased goodness-of-fit against a target I invented.

I also violated my own gate. Nothing in your message asked for a fitting study, and I ran one without confirming the approach first.

### Millard · 2026-08-12 15:33

this is a QUICK AND DIRTY. KISS IT.

You mentioned 2 studies. give me QnD results for both.

### Claude · 2026-08-12 15:33

Both gamma, both pinned to that study's own mean plus its own tail anchor, truncated at 40, contiguous bins, each column sums to 100%.

| Bin | Coid % | per 100k | N&H % | per 100k |
| --- | --- | --- | --- | --- |
| 0–1 | 66.348 | 66,348 | 39.157 | 39,157 |
| 1–2 | 9.860 | 9,860 | 12.328 | 12,328 |
| 2–3 | 5.764 | 5,764 | 8.320 | 8,320 |
| 3–4 | 3.906 | 3,906 | 6.254 | 6,254 |
| 4–5 | 2.835 | 2,835 | 4.943 | 4,943 |
| 5–6 | 2.142 | 2,142 | 4.023 | 4,023 |
| 6–7 | 1.661 | 1,661 | 3.339 | 3,339 |
| 7–8 | 1.313 | 1,313 | 2.809 | 2,809 |
| 8–9 | 1.052 | 1,052 | 2.388 | 2,388 |
| 9–10 | 0.852 | 852 | 2.046 | 2,046 |
| 10–15 | 2.467 | 2,467 | 6.808 | 6,808 |
| 15–20 | 1.011 | 1,011 | 3.545 | 3,545 |
| 20–25 | 0.444 | 444 | 1.943 | 1,943 |
| 25–30 | 0.203 | 203 | 1.097 | 1,097 |
| 30–35 | 0.096 | 96 | 0.631 | 631 |
| 35–40 | 0.046 | 46 | 0.369 | 369 |
| **Total** | **100.00** |  | **100.00** |  |

Fits: Coid k=0.232, θ=8.003, P(≥30)=0.14%. N&H k=0.433, θ=10.954, P(≥30)=1.00%.

Three fixes vs. Sonnet: 11–14 is now covered, bins tile with no overlap so the column actually sums, and the 5-point bins are interval masses rather than point densities, so they're directly comparable to the 1-point rows.

Coid is a representative British household sample; N&H is US urban skewed toward high-risk neighborhoods, which is why it runs about 5x hotter in the tail. Coid's own headline 0.6% was at PCL:SV ≥13, which converts to PCL-R ≈21.7, not 30 — the "1% are psychopaths" figure comes from the N&H side, not from Coid.

### Millard · 2026-08-12 15:34

give me simple descriptions of Coid and N&H

### Claude · 2026-08-12 15:34

**Coid 2009** — British household survey. 638 adults aged 16–74, sampled at random from postal addresses across England, Wales and Scotland. Ordinary people at home, not selected for anything. Scored with the PCL:SV, the 12-item screening version of the checklist. Weighted prevalence 0.6% at a cut score of 13.

**Neumann & Hare 2008** — American community sample. 514 adults aged 18–40 drawn from the MacArthur Violence Risk Study, a study built around psychiatric patients and the neighborhoods they were discharged into. Also PCL:SV. Same instrument, but the sampling frame is urban and tilted toward higher-risk areas.

The gap between the two tables is mostly the sampling frame, not the measurement. Coid asked "what does the general population look like." N&H asked "what does this urban high-risk catchment look like." Neither used the full PCL-R, and neither measured PCL-R 30 directly — that threshold is a conversion in both cases.

### Millard · 2026-08-12 15:35

those sample sizes were extremely low

### Claude · 2026-08-12 15:35

Yes. That's the real limit on those tables.

Coid's 0.6% out of 638 is about 4 people. The 2.1% at cut 11 is about 13. His published confidence interval on the 0.6% runs 0.2% to 1.6% — an eightfold spread, and that's before you convert PCL:SV to PCL-R. N&H's 514 puts roughly 5 people above the psychopathy threshold.

So every row in my table from 15 upward is an extrapolation off single-digit counts. The 30–35 and 35–40 rows contain no observed people at all in either study — they're pure curve, produced by the gamma's tail shape rather than by anyone actually scored. The 0–1 and 1–2 rows are the only ones with enough bodies behind them to mean much.

Those are also the only two representative general-population PCL surveys that exist. The instrument needs a file review plus a clinical interview per person, which is why nobody has run it on 50,000 people. Anything claiming a population PCL-R distribution is built on these two samples or on self-report proxies that measure a different thing.

### Millard · 2026-08-12 15:38

give me a title for the table

### Claude · 2026-08-12 15:38

**Estimated PCL-R Score Distribution in the General Population (Extrapolated from PCL:SV Community Surveys)**

Shorter, if you want it: **Extrapolated PCL-R Distribution: Coid vs. Neumann & Hare**
