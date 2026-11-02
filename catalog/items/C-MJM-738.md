# Hare PCL-R score population distribution

| | |
|---|---|
| Date | 2026-08-12 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-738` |
| Links | [Original](https://claude.ai/chat/634cf001-788c-4804-a3b6-009a9ac7dae1) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/738-2026-08-12-hare-pcl-r-score-population-distribution.html) |

**Summary:** Extrapolated general-population distribution of Hare PCL-R scores from 0 to 40, modeled as a gamma distribution.

**Topics:** Psychopathy, narcissism and the mind > Psychopathy prevalence and PCL-R

**Index terms:** Hare Psychopathy Checklist-Revised; Robert Hare; Craig Neumann; psychopathy prevalence; gamma distribution

[← Catalog home](../README.md)

---

### Millard · 2026-08-12 15:12

give me a distribution of population at each Hare PCL-R score (extrapolated) from 0 to 10 by 1 point increments, and then 10 to 40 in 5 point increments

### Claude · 2026-08-12 15:13

**Empirical basis (source-verified, timestamped 2026‑08‑12):**

* No true general-population PCL-R norming exists — the instrument requires file review + interview, unavailable at population scale. Cited "general population" figures are extrapolations/proxies, not measured norms.
* Anchor points used: mean ≈ 4.5 (Neumann & Hare, 2008, community sample) and P(score ≥30) ≈ 1% (Neumann & Hare estimate, widely cited prevalence figure).
* Model: gamma distribution fit to those two constraints (right-skewed, matches known shape — most people cluster low, long right tail). This is **my extrapolation, not a published table.**

Fitted parameters: shape k=0.496, scale θ=9.08, mean=4.5, P(≥30)=1.00% (by construction).

| Score | % of population | Per 100,000 |
| --- | --- | --- |
| 0 | 26.34% | 26,339 |
| 1 | 17.48% | 17,483 |
| 2 | 10.72% | 10,718 |
| 3 | 7.78% | 7,783 |
| 4 | 6.02% | 6,018 |
| 5 | 4.81% | 4,812 |
| 6 | 3.93% | 3,929 |
| 7 | 3.26% | 3,255 |
| 8 | 2.73% | 2,725 |
| 9 | 2.30% | 2,300 |
| 10 | 1.95% | 1,953 |
| 15 | 4.69% | 4,694 |
| 20 | 2.33% | 2,332 |
| 25 | 1.20% | 1,199 |
| 30 | 0.63% | 630 |
| 35 | 0.34% | 336 |
| 40 | 0.10% | 104 |

Notes:

* Values 0–10 are point densities (±0.5 window); 15–40 are ±2.5 windows (per your requested bin widths). They are not directly comparable magnitudes — the 5-point bins integrate 5x the score range.
* Gap 11–14 not covered by either bin width; excluded per your stated increments.
* Uncertainty is unquantifiable beyond the two anchor points — no variance/CI exists for this because it's a fitted model, not sampled data.
