# Understanding Immortal Time Bias

| | |
|---|---|
| Date | 2025-07-12 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-074` |
| Links | [Original](https://claude.ai/chat/788893fe-7640-4338-941a-74476b2cad08) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/074-2025-07-12-understanding-immortal-time-bias.html) |

**Summary:** Definition of immortal time bias, an observational-study error that misattributes outcome-free time to an exposure group.

**Topics:** Belief, truth and epistemics > Scientific consensus, peer review and replication; COVID, vaccines and medical fraud > mRNA shot injuries, deaths and excess mortality

**Index terms:** immortal time bias; observational study; epidemiology; cohort study

[← Catalog home](../README.md)

---

### Millard · 2025-07-12 21:22

what is immortal time bias;

### Claude · 2025-07-12 21:22

Immortal time bias is a systematic error that occurs in observational studies when there's a period of time during which the outcome of interest (like death or disease) cannot possibly occur by design of the study, but this time is incorrectly attributed to one exposure group rather than another.

The bias gets its name because during this "immortal" period, subjects are essentially immortal with respect to the outcome being studied. The problem arises when this immortal time is misclassified or attributed to the wrong exposure group, leading to an artificial protective effect.

Here's how it typically happens:

**Common scenario**: Studies comparing treated vs. untreated patients where treatment status is defined by whether someone received treatment during a follow-up period. Patients who die early in the follow-up period before receiving treatment are classified as "untreated," but they had immortal time from study entry until death (since they couldn't have received treatment while dead). Meanwhile, patients who survived long enough to receive treatment have this same early period counted as "treated" time.

**Classic example**: A study examines whether a medication reduces mortality by comparing patients who received the drug during hospitalization vs. those who didn't. Patients who die on day 1 of hospitalization are classified as "untreated," but patients who receive the drug on day 5 have days 1-4 counted as "treated" time, even though they weren't actually treated during those days.

**Why it matters**: This bias typically makes treatments appear more effective than they actually are, because the immortal time artificially inflates the survival time in the treated group.

**Prevention**: The bias can be avoided by using time-dependent analysis methods, landmark analysis, or proper classification of exposure time that accounts for when treatment actually began.
