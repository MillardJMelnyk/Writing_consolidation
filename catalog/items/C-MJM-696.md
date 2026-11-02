# New AI workstation

| | |
|---|---|
| Date | 2026-04-11 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-696` |
| Links | [Original](https://claude.ai/chat/18a0039e-9a19-4095-ad10-9d676eb7feae) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/696-2026-04-11-new-ai-workstation.html) |

**Summary:** Choosing local LLMs for document search and book editing, required PC specs, building versus buying, and importing parts to Mexico from B&H.

**Topics:** AI chatbots and working with Claude > Local LLMs and AI document search; Practical & personal > Windows, Linux and PC hardware troubleshooting; Practical & personal > Shopping, product comparisons and gifts; Practical & personal > Residency, passports, visas and travel

**Index terms:** Ollama; local LLM; 70B model; GPU VRAM; B&H Photo; RFC; CURP

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-04-11 16:18

what is Ollama?

### Claude · 2026-04-11 16:18

Saturday, April 11, 2026, 11:02 AM CST

Ollama is an open-source tool that lets you run large language models locally on your own hardware. It handles model downloading, packaging, and serving via a local REST API (default: `localhost:11434`), mimicking the OpenAI API interface.

Key facts:

* Supports models like Llama 3, Mistral, Gemma, Phi, Qwen, and others in GGUF format
* Runs on macOS, Linux, and Windows
* Uses llama.cpp as its inference backend
* GPU acceleration supported (NVIDIA CUDA, Apple Metal, AMD ROCm)
* Models are pulled from Ollama's registry (`ollama pull modelname`)
* No internet connection required after model download

Primary use case: private, offline LLM inference without cloud API costs or data exposure.

### Millard · 2026-04-11 16:22

here is my system. I want to use a local AI for 2 purposes:
Manage and search my research documentation stored in a variety of forms
Serve as a personal editor for the books I write.
3 questions:
1. Which is the best AI model for my purposes (that can be run locally)
2. Which can my current system support?
3. What specs would I need in a new system to run the AI model (#1)?

[File attached: 1775924467699\_image.png — contents not included in export]

### Claude · 2026-04-11 16:23

**Q1: Best model for your purposes**

**Llama 3.1 70B** or **Qwen2.5 72B** (Q4 quantization). Both offer 128K context windows, strong instruction-following, and high writing quality — the two properties your use cases demand most. For RAG (document search), either pairs well with a retrieval pipeline (e.g., LlamaIndex or Ollama + ChromaDB).

Qwen2.5 72B edges ahead on writing/editing tasks in benchmarks; Llama 3.1 70B is marginally stronger on reasoning and has broader community support.

---

**Q2: What your current system supports**

Your bottleneck is the RTX 2060 SUPER — **8 GB VRAM**.

| Model Size | Fits in VRAM? | Speed | Usable? |
| --- | --- | --- | --- |
| 7B Q4 | Yes (~4.5 GB) | Fast | Yes, but quality limited |
| 13B Q4 | Partial (~8 GB, tight) | Moderate | Marginal |
| 30B Q4 | No — CPU offload | Slow | Barely |
| 70B Q4 | No — heavy offload | Very slow | No |

Your 32 GB RAM allows offloading larger models to system RAM, but CPU inference on offloaded layers is roughly 10–20× slower than GPU. A 70B model in your current setup would be unusably slow for interactive editing.

**Realistic ceiling on your current system: 13B models.** That's a significant quality drop from 70B for book editing.

---

**Q3: Specs for a new system to run 70B properly**

Qwen2.5 72B at Q4\_K\_M ≈ **43 GB**. To run it fully in VRAM (fast, interactive):

**Minimum viable (with some CPU offload):**

* GPU: RTX 4090 — 24 GB VRAM; ~56% of 70B fits in VRAM, rest offloads. Usable but not optimal.
* RAM: 64 GB DDR5
* CPU: Modern (i9 or Ryzen 9) to handle offload layers faster

**Optimal (fully in VRAM, fast):**

* GPU: Dual RTX 4090 (48 GB total VRAM) — fits 70B Q4 fully, fast inference
* Or: NVIDIA RTX 6000 Ada (48 GB single card) — ~$6,800 as of mid-2025
* RAM: 64 GB DDR5
* CPU: Any modern high-core-count

**Note:** RTX 5090 (32 GB VRAM, released early 2025) is a middle option — better than a single 4090, still doesn't fully fit 70B Q4. Verify current pricing; the market may have shifted since August 2025.

For your use case, a **single RTX 4090 with 64 GB RAM** is the practical price/performance entry point. Dual 4090 or RTX 6000 Ada if you want full-speed 70B with no compromise.

### Millard · 2026-04-11 16:25

find me the 3 top "sweet spot" models of PC that fit the "optimal" configuration,

### Claude · 2026-04-11 16:26

Important development since my initial answer: the GPU landscape has shifted. The **RTX PRO 6000 Blackwell** (96GB GDDR7) now exists — single-card solution that fits 70B Q4 with room to spare. This makes dual-4090 and RTX 6000 Ada largely obsolete for this use case.

Here are the 3 sweet-spot prebuilts as of April 2026:

---

**#1 — Empowered PC Sentinel AI Workstation**
*(Best single-system, purpose-built for local AI)*

RTX PRO 6000 Blackwell (96GB GDDR7), Intel Core Ultra 9 285K, 128GB DDR5, 4TB Gen5 SSD + 2×4TB SSD

* GPU alone is ~$7,900 (currently sold out at EmpoweredPC); full system pricing not publicly listed — request a quote
* Purpose-built for local LLM inference; marketed explicitly for running large AI models locally
* Best in class for your use case; no compromises on 70B

---

**#2 — Corsair Vengeance i8200**
*(Best mainstream prebuilt with strong specs — single RTX 4090)*

RTX 4090, i9-14900KF, 64GB DDR5 @ 6600MT/s, 4TB Gen4 NVMe SSD, 360mm AIO, 1000W 80+ Gold PSU — ~$3,500

* **Caveat:** Only 24GB VRAM. 70B won't fit fully in VRAM; you'll get CPU offload with slower inference (~5–8 tok/s vs. 20+ for full VRAM fit)
* Good if you run 13B–34B models primarily and accept 70B at reduced speed
* Widely available, solid warranty

---

**#3 — CLX HORUS**
*(Mid-range value with RTX 4090 + 64GB)*

i9-14900KF 3.2GHz 24-core, 64GB DDR5, RTX 4090 24GB GDDR6X, 2TB NVMe + 6TB HDD, WiFi, Win 11

* Same VRAM caveat as #2
* Adds 6TB HDD — useful for your document research corpus
* Typically priced ~$3,000–3,300; better storage value than Corsair

---

**Bottom line on the sweet spot:**

The honest answer is there's a cliff between consumer prebuilts (~$3–4K, single 4090, 24GB VRAM, no full 70B) and true AI workstations (~$15K+, RTX PRO 6000 Blackwell, 96GB VRAM, full 70B). As of April 2026 the RTX PRO 6000 Blackwell card alone runs $8,500–9,200 at retail. There is no prebuilt mid-market option that cleanly fits 70B in VRAM for under ~$10K right now.

If budget is the constraint, the Corsair i8200 (#2) is the best-built consumer option and runs 70B with offload. If 70B at full speed is the requirement, the Empowered PC Sentinel with RTX PRO 6000 is the only prebuilt path.

### Millard · 2026-04-11 16:32

1. Give me a feel for the difference between 70B with offload and 70B at full speed
2. Empowered PC Sentinel is out of my realistic budget unless I could finance it.
3. I built my current system. How hard would it be to build a system comparable to Empowered PC Sentinel, and how much might that bring price down?

### Claude · 2026-04-11 16:33

**1. 70B offload vs. full VRAM — practical feel**

Full VRAM (RTX PRO 6000, 96GB): roughly 20–30 tokens/second. At that rate, a paragraph generates in 2–4 seconds. Feels like a fast human typist. Usable for iterative editing — you prompt, it responds, you react in real time.

CPU offload (single 4090, 24GB): roughly 3–8 tokens/second depending on how many layers offload. A paragraph takes 15–40 seconds. Usable for batch tasks — "edit this chapter while I make coffee." Painful for iterative back-and-forth editing sessions. For document search/RAG queries it's more tolerable since you're waiting for one answer, not a dialogue.

For your two use cases specifically: document search tolerates offload; interactive editing does not.

---

**2. Acknowledged.**

---

**3. DIY vs. Empowered PC Sentinel**

Since you've built before, this is straightforward. The Sentinel is not exotic — it's a standard ATX build. No proprietary form factors, no custom cooling loops, no server-grade complexity.

**Estimated DIY savings: 20–35%** over a prebuilt AI workstation at this tier. The system markup on a $15K+ prebuilt is substantial.

Rough DIY component breakdown (April 2026 estimates):

| Component | Est. Price |
| --- | --- |
| RTX PRO 6000 Blackwell (96GB) | $8,500–9,200 |
| Intel Core Ultra 9 285K | $550–620 |
| Z890 motherboard (high-end) | $400–550 |
| 128GB DDR5 (4×32GB) | $350–450 |
| 4TB Gen5 NVMe SSD | $350–450 |
| Additional storage (2×4TB) | $300–400 |
| 1200W 80+ Platinum PSU (required for 600W TGP card) | $200–280 |
| Case (full tower — card is 12" long, dual slot, needs airflow) | $150–250 |
| 360mm AIO cooler | $120–180 |
| **Total estimate** | **~$11,000–12,400** |

vs. Empowered PC Sentinel at likely $14,000–17,000 fully configured.

**Practical notes:**

The RTX PRO 6000 Blackwell draws 600W at full load. That plus CPU puts your system near 900W peak. A 1200W PSU is not optional — 1000W is too close to the margin. Airflow matters more than usual; plan the case around it.

The card is 12" long and dual-slot — verify case clearance before buying. Most full-tower cases handle it but mid-towers need checking.

No other complexity. If you built your i7-9700K system, you can build this. The GPU is the entire challenge and it's just a PCIe slot.

**The real barrier isn't build difficulty — it's the $8,500–9,200 GPU price, which is fixed regardless of whether you buy prebuilt or DIY.**

### Millard · 2026-04-11 16:35

where would the best place be to get components?

### Claude · 2026-04-11 16:35

For most components, the answer is straightforward. For the RTX PRO 6000 Blackwell specifically, it's more complicated.

---

**RTX PRO 6000 Blackwell (the critical component)**

This is not a consumer card. It's sold through authorized professional/workstation channels:

* **B&H Photo** (bhphotovideo.com) — carries professional NVIDIA cards, often has stock when others don't
* **PNY direct** (pny.com) — PNY is a primary board partner for RTX Pro cards
* **Provantage** (provantage.com) — business/pro AV supplier, competitive pricing
* **Micro Center** (in-store only, ~25 US locations) — confirmed in-stock at some locations per earlier search results
* **NVIDIA Marketplace** (marketplace.nvidia.com) — direct, but currently showing out of stock
* **VRLA Tech** (vrlatech.com) — carries it, ships to Canada/Mexico

Avoid Amazon for this card — third-party sellers at this price point are a warranty and authenticity risk.

---

**Everything else**

| Component | Best Sources |
| --- | --- |
| CPU, RAM, SSD, PSU, Case | Newegg, Micro Center (if near one), Amazon |
| Motherboard | Newegg or manufacturer direct (ASUS, Gigabyte) |
| Price tracking | camelcamelcamel.com (Amazon), pcpartpicker.com |

**PCPartpicker.com** is worth using for the full build — it aggregates prices across retailers, flags compatibility issues, and tracks price history.

---

**One practical note:** Given you're in Mexico, import duties and cross-border shipping on a $9,000 GPU are non-trivial. If you have a US shipping address available (forwarding service or contact), that's the cleaner path for the GPU. Mexican customs on electronics at that declared value will attract significant attention.

### Millard · 2026-04-11 16:37

I've dealt with B&H before, that's how I built my current PC. Do they ship to Mexico?

### Claude · 2026-04-11 16:37

Yes, B&H ships worldwide, Mexico included.

Two things you need to know specific to Mexico:

Recent changes to Mexican tax requirements mandate that all shipments include RFC or CURP information, and any discrepancies between those numbers and other information on the shipping label could cause delays or cancellation — with return costs deducted from your refund.

So have your RFC ready before ordering. For a $9,000 GPU that's not optional — customs will flag it regardless, and a documentation mismatch at that value is a serious problem.

The second issue is the declared value itself. A single item at $8,500–9,200 will attract significant Mexican import duties (typically 16% IVA + potential aranceles on electronics). That could add $1,500–2,000+ to the landed cost. Worth pricing that out before committing to direct Mexico shipment vs. routing through a US address if you have access to one.

### Millard · 2026-04-11 16:38

what good would a US address do, since I still need to get it into Mexico.

### Claude · 2026-04-11 16:38

You're right. The duty and IVA apply at the border regardless of how it gets here — shipping direct or carrying it across yourself. A US address only avoids the issue if someone else in the US is using the equipment. In your case it changes nothing material.

The only scenarios where a US address would have made a difference:

* You were having someone bring it across as personal baggage and declaring it as used personal property (gray area, risky at that value)
* You intended to leave it in the US

Neither applies. Direct B&H shipment to your Tequisquiapan address with your RFC in order is the straightforward path. Just price the total landed cost — component price + shipping + IVA + aranceles — before committing, so the final number isn't a surprise.

### Millard · 2026-04-11 16:39

and only residents can get RFC and CURP numbers, right?

### Claude · 2026-04-11 16:39

Not exactly.

**RFC:** The SAT issues RFC to both residents and non-residents who have taxable activity in Mexico. As a permanent resident (once granted) or even as someone with legal immigration status, you can obtain one. You may already qualify now depending on your current visa status.

**CURP:** This one is tied to legal presence in Mexico — it's issued to Mexican citizens and foreign nationals with legal residency or immigration status. If you have a valid visa (FM2/FM3 equivalent, or temporary/permanent residency card), you're eligible.

Given that you're actively pursuing permanent residency through family unity, you almost certainly already have a legal immigration status that qualifies you for both. If you're currently on a temporary residency card (tarjeta de residente temporal), that's sufficient to obtain both RFC and CURP.

Practically: if you don't already have them, getting CURP is straightforward online via gob.mx for registered foreigners. RFC requires a SAT appointment or a gestor, and takes longer.

What's your current immigration document status — temporary resident card, or still on a visa?
