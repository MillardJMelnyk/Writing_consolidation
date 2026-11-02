# Critical analysis of autism study claims

| | |
|---|---|
| Date | 2026-10-05 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-c63f27a4` |
| Links | [Original](https://claude.ai/chat/c63f27a4-8f7e-4dd7-89e8-c98237341c9f) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-10-05_critical-analysis-of-autism-study-claims_c63f27a4.html) |

**Summary:** Critiques a 2.5-million-child MMR timing study, showing it compared early versus later vaccination and cannot support Facebook claims of no autism link.

**Topics:** COVID, vaccines and medical fraud > Vaccines and autism studies; COVID, vaccines and medical fraud > Childhood vaccines, SIDS and cancer claims; Belief, truth and epistemics > Scientific consensus, peer review and replication

**Index terms:** MMR vaccine; autism; Epic Cosmos; electronic health record; study design; follow-up period

[← Catalog home](../README.md)

---

### Millard · 2026-10-05 13:19

Analyze This paper and be as critical as possible about its faults, limitations, and precisely what it does and does not show about an autism link. Then consider the second image and comment on two things.

1. Does the study actually support the claims made in the second image?
2. Does the study even intend to address those claims?
3. Is the study designed to address those claims?

### Claude · 2026-10-05 13:21

Monday, October 5, 2026, 7:19 AM CST

**Bottom line:** the paper shows no average association, inside one EHR network, between a first MMR dose at 11.5–24 months and later getting an autism diagnosis code, mostly recorded before about age 3. The Facebook post inflates that into something the study neither claims nor can deliver.

**Evidence gap:** the full text is paywalled. I worked from the abstract and detailed secondary reporting of the methods. Still unknown: the exact comparator rules, whether Cosmos captures doses given outside Epic systems, how MMRV doses were handled, whether the protocol was registered, and per-group case counts.

**What was done**  
The cohort was 2,560,035 children with at least one routine primary-care visit at 12–24 months, drawn from the Cosmos EHR database. Autism prevalence in the sample was 2.55%, and the outcome was a single specific diagnostic code. The analysis used Cox models with covariates chosen by causal diagrams, and the pneumococcal booster given at 12–15 months served as a negative control. The primary result was an adjusted hazard ratio of 0.97 (99% CI 0.91–1.03), and the negative control came out at 1.01.

**Faults, ranked by how much they bite**

1. **The real uncertainty comes from bias, not from sample size.** In the 14.5–17.5 and 17.5–24 month windows, vaccinated kids showed HRs of 0.90 and 0.92, and the authors attribute those to leftover bias rather than protection. That is an admission that the design can carry roughly 8–10% bias, about three times the margin the headline upper bound of 1.03 implies. Bias big enough to create a fake protective effect is big enough to hide a harmful effect of the same size. Highly likely that the 2.5 million sample size creates false precision.
2. **The comparator group is odd.** The unvaccinated comparison kids had to be unvaccinated at the window start and stay unvaccinated through follow-up. Their median follow-up was 366 days, against 853 days for vaccinated kids. Defining a group by what happens after the starting line is a selection problem. With follow-up starting at age 1, most "unvaccinated" kids drop out of the records around age 2, well before typical US diagnosis age, which is around 4. The few left at older ages are committed refusers, plus kids vaccinated somewhere Cosmos can't see. Those misclassified kids push the result toward null. A third group also matters: kids whose early warning signs make parents stop vaccinating. They land in the unvaccinated group with a diagnosis, which pushes the result toward "protective." Likely; I can't estimate how large any of this is without the methods section.
3. **The negative control can't catch the bias that matters most.** Nobody skips the pneumococcal booster out of autism fear, but people do skip MMR for exactly that reason. A flat PCV result therefore rules out general doctor-visit bias, not the selection specific to MMR. The dataset also had no family history of autism, and the neighborhood disadvantage measure was missing for 53% of children. Family history is the single most relevant confounder here. Highly likely.
4. **Opposing biases can cancel out.** Vaccinated kids see doctors more often, so they get diagnosed more, which makes MMR look harmful. Families with autism concerns skip MMR, which makes it look protective. A null result can be these two biases netting to zero, and this design cannot separate them.
5. **The outcome is a billing code, timed at diagnosis rather than onset.** The specific fear is regression shortly after the shot. A diagnosis code entered years later doesn't test when symptoms began. Short follow-up also undercounts later-diagnosed, often milder, cases.
6. **Rare susceptible subgroups would be invisible.** An upper bound of 1.03 on a 2.55% base allows about 1 extra case per 1,300 kids. Suppose 1 in 2,000 children were susceptible and every one of them developed autism from MMR: the average HR would move only about 2%, which is inside the confidence interval. Highly likely.
7. **Selection limits who the result applies to.** Requiring linked birth-parent records excluded a substantial share of otherwise eligible children. The cohort also leaves out kids who were never in regular care.

**What it shows:** In this population, there was no detectable average rise in autism diagnosis after a first MMR dose at 11.5–24 months. If bias is set aside, sampling error rules out an increase above about 3%.

**What it doesn't show:** that no causal link exists; that no susceptible subgroup exists; anything about onset or regression timing; anything about the second dose, MMRV, other vaccines, or the cumulative schedule.

**The Facebook post**

1. **Does the study support its claims?** Mostly no. It supports "no association found in this cohort," and nothing beyond that. The authors themselves describe the results as reinforcing existing evidence, which is the opposite of "groundbreaking." Nothing in the study supports "one of the most definitive verdicts in modern medical history," "conclusively," or a blanket "no link." "Tracked developmental trajectories" is false: the study used diagnosis codes, with no developmental measures at all. "Up to age eight" is only the cap; the median record ended around age 3. Highly likely.
2. **Does the study intend to address those claims?** No. Its stated aim was to reduce bias from exposure timing and healthcare use, and its conclusion is limited to "no association" in this cohort. Highly likely.
3. **Is the study designed to address them?** No. An observational null result can put a ceiling on an average effect. It cannot establish that there is no link, cannot track development, and cannot rule out effects in subgroups. Highly likely.

### Millard · 2026-10-05 13:25

Even in what you said I think there's still misleading ambiguity. The comparison was not between children who received MMR versus children who did not. It was a comparison of children, all of whom received MMR, between those who received it at one point in time versus those who received it later.

### Claude · 2026-10-05 13:26

You're right that my wording misled. The comparison group wasn't a separate population of unvaccinated kids: 94.5% of the whole cohort got MMR, at a median age of 377 days. So most children counted as "unvaccinated" at a given landmark age got their shot weeks or months later.

I also misread the comparison group's 366-day median follow-up as kids leaving the records. More likely, their follow-up stopped when they got vaccinated. That retracts that part of my fault #2.

**One thing for you to weigh:** the reporting says comparison kids had to stay unvaccinated throughout follow-up. Suppose each comparison child stops being counted the day they get their shot. Then most of their counted time ends around age 2, when autism diagnoses are rare. Nearly all autism diagnoses on the comparison side would come from the small group vaccinated very late or never. At the level of children, your "earlier vs. later" description fits. At the level of where the diagnoses actually come from, the contrast would be vaccinated vs. never or very-late vaccinated. How does that bear on your reading?

**Which reading holds turns on one rule in the methods.** Either kids not yet vaccinated stop being counted at their first MMR, or they stay in the group they were assigned at the landmark age.

* Stop being counted: Likely, because it fits the 366-day median and the reporting's wording.
* Stay in the assigned group, which is your reading exactly: Unlikely.

The journal version is paywalled, and SSRN blocked my download of the free preprint. The check: open the [SSRN preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6139617) and search the PDF for "censor." The preprint's methods could differ from the published version.

**Either way, the Facebook-post answers stay No and get stronger:**

* **If kids stay in their assigned groups:** the study only asks whether a few months' difference in timing matters. Any effect of MMR itself would hit both groups and cancel out.
* **If kids stop being counted at vaccination:** the MMR vs. no-MMR comparison rests on a small, never-vaccinated group, with the confounding problems already listed.

### Millard · 2026-10-05 13:30

So it is safe to say, highly likely, that presenting this study as having a definitive bearing on the autism link question is at least confusing if not misleading. And it's even more likely that using this study as if it definitively closes the question is misrepresentative.

### Claude · 2026-10-05 13:30

Yes.

### Millard · 2026-10-05 13:31

Okay now imagine a high school senior who read that Facebook post and read the abstract of the study and is completely confused because they can't understand how the Facebook claims are supported by the study, or even how the study is the least bit relevant to those claims. Summarize you're findings for them in a short paragraph or two.

### Claude · 2026-10-05 13:32

The study looked at the medical records of about 2.5 million American kids and asked a narrow question. Were kids who got their first MMR shot at a given age, between about 1 and 2 years old, diagnosed with autism more often than kids who hadn't gotten it yet at that age? It found no difference. But "hadn't gotten it yet" mostly meant "got it a little later," because 94.5% of all the kids eventually got the shot. The study also counted autism diagnosis codes in medical records rather than tracking how kids actually developed. For about half the vaccinated kids, the records stopped around age 3, which is earlier than many autism diagnoses happen. And because it's a look back at records rather than a controlled experiment, it can't rule out hidden factors or a small effect in a small group of kids. The authors themselves described their results modestly, as adding support to earlier research.

So the study is relevant to the question, and it fits with earlier research that also found no link. What the Facebook post did was turn it into something it isn't. "Groundbreaking," "one of the most definitive verdicts in modern medical history," "conclusively," and "tracked developmental trajectories" are the post's words, not things the study shows. The study wasn't built to settle the whole question, and no single study of this kind could. Being confused is the right reaction, because the post claims far more than the study supports.
