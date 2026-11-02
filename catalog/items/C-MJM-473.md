# US measles fatality trends and vaccine introduction

| | |
|---|---|
| Date | 2025-12-16 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-473` |
| Links | [Original](https://claude.ai/chat/d05d969f-86d5-409d-9320-ca9585936826) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/473-2025-12-16-us-measles-fatality-trends-and-vaccine-introduction.html) |

**Summary:** Graphs US measles deaths by decade since the 1800s on a linear scale, marking vaccine introduction and showing pre-vaccine declines.

**Topics:** COVID, vaccines and medical fraud > Vaccine history, measles and polio

**Index terms:** measles mortality; measles vaccine; United States; vital statistics; comorbidity

[← Catalog home](../Master_catalog.md)

---

### Millard · 2025-12-16 22:29

Decade by decade since 1850 (or whenever the stats started), graph the fatality counts in the USA attributed to measles, NOT including deaths involving comorbidities. On the graph, place an arrow when measles vaccines were first administered.

### Claude · 2025-12-16 22:29

Clarification required before proceeding:

**Data limitation issue**: Historical US mortality statistics (CDC, vital statistics records) do not systematically distinguish "measles as sole cause of death" from "measles with comorbidities." Death certificates and reporting systems—particularly before mid-20th century—recorded measles as cause of death without parsing whether pneumonia, encephalitis, or other complications were comorbid conditions or direct sequelae of measles infection.

The available data sources (CDC mortality reports, Historical Statistics of the United States, vital statistics yearbooks) report **total measles-attributed deaths**, which includes:

* Deaths where measles was primary cause
* Deaths where measles complications (pneumonia, encephalitis) were proximate cause
* Deaths where measles exacerbated existing conditions

**Question**: Do you want me to:

1. **Proceed with total measles-attributed mortality data** (the only consistently available metric), with explicit notation that comorbidity separation is not possible from historical records?
2. **Search for any studies that attempted retrospective comorbidity separation** (likely limited, possibly non-existent for pre-1950 data)?
3. **Something else** you have in mind regarding the comorbidity distinction?

Also confirming: US national mortality registration began ~1900 (partial) and became comprehensive ~1933. Pre-1900 data would be fragmentary estimates. Is fragmentary pre-1900 data acceptable, or start from 1900?

### Millard · 2025-12-16 22:30

1

### Claude · 2025-12-16 22:32

I have sufficient data. Let me compile and create the graph.

Now I'll create the graph with the compiled data.

**Data compiled. Graph created.**

**Key findings:**

| Decade | Est. Annual Deaths | Source |
| --- | --- | --- |
| 1910s | ~6,000 | CDC: avg 6,000/yr (1912-1922 reporting) |
| 1920s | ~4,500 | CDC MMWR: 7,575 deaths in 1920 |
| 1930s | ~2,500 | Death rate 3.2/100k |
| 1940s | ~600 | Death rate 0.5/100k |
| 1950s | ~450 | CDC: 400-500/yr pre-vaccine |
| **1960s** | ~300 | **1963: Vaccine introduced** |
| 1970s | ~40 | Widespread vaccination |
| 1980s | ~3 | Near elimination |
| 1990s | ~40 | 1989-91 outbreak (~123 total deaths) |
| 2000s | ~1 | Eliminated 2000 |
| 2010s | <1 | Sporadic |
| 2020s | ~2 | 2025 outbreak ongoing |

**Vaccine arrow placement:** 1963 (first measles vaccine licensed in US)

**Data limitations noted on graph:**

* Pre-1912: No national reporting
* Pre-1933: Incomplete national mortality registration
* Comorbidity separation: Not available in any historical vital statistics records

### Millard · 2025-12-16 22:34

You said the graph was created, but the page had an error. I see no graph anywhere.

### Claude · 2025-12-16 22:37

This should render. If it still fails, I'll generate a static image using Python instead.

### Millard · 2025-12-16 22:38

That looks like a logarithmic scale chart.

[File attached: 1765924711202\_image.png — contents not included in export]

### Claude · 2025-12-16 22:38

Correct. The Y-axis uses a logarithmic scale.

Reason: The data spans 4 orders of magnitude (from ~6,000 deaths/year in the 1910s to <1 death/year in the 2010s). On a linear scale, the post-1970s data would be visually indistinguishable from zero, making the post-vaccine trend invisible.

Do you want a linear scale version instead?

### Millard · 2025-12-16 22:39

Yes, linear

### Claude · 2025-12-16 22:39

Note: On this linear scale (0–7,000), all post-1970s values appear at or near zero—the decline from 40 to 3 to 1 death/year is not visually distinguishable.

### Millard · 2025-12-16 22:44

You lost all this good info (image attached).
Redo, linear, include the footer data, and add 2 lines to the X axis labels:
1. Death count (absolute)
2. % reduction compared to previous decade.

### Millard · 2025-12-16 22:44

sorry, forgot the image.

[File attached: 1765925079222\_image.png — contents not included in export]

### Claude · 2025-12-16 22:46

X-axis now shows 3 lines per decade:

1. Decade name
2. Death count
3. % change vs previous decade (green for reductions, red for increases)
