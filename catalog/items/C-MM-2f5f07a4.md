# Coining a word for self-ignorance

| | |
|---|---|
| Date | 2026-07-26 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-2f5f07a4` |
| Links | [Original](https://claude.ai/chat/2f5f07a4-7b88-4668-a029-178e49e1c95d) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-07-26_coining-a-word-for-self-ignorance_2f5f07a4.html) |

**Summary:** Coining a word for deliberate self-ignorance ('self-obliviation'), then what running and renting hardware for Moonshot's open-weight Kimi K3 costs.

**Topics:** Language, words and definitions > Coined words and neologisms; Belief, truth and epistemics > Willful ignorance and amathia; AI chatbots and working with Claude > Local LLMs and AI document search; AI chatbots and working with Claude > Communication protocols and ground rules

**Index terms:** self-obliviation; Moonshot AI; Kimi K3; open weights; GPU cloud rental; Nvidia H200

[← Catalog home](../README.md)

---

### Millard · 2026-07-26 23:21

I don't give a fuck about grammar or accepted definitions. I need a word that means self-ignoramusing.

### Claude · 2026-07-26 23:21

Self-obliviation.

### Millard · 2026-07-26 23:22

Self-destruction is not a synonym for self-dumifying

### Claude · 2026-07-26 23:22

Self-stultification.

### Millard · 2026-07-26 23:22

Give me some more

### Claude · 2026-07-26 23:22

* Self-benighting
* Self-obtusifying
* Self-dumbening
* Self-fatuating
* Self-idiotizing

### Millard · 2026-07-26 23:22

Give me one that's a form of "ignorance"

### Claude · 2026-07-26 23:22

Self-ignorancing.

### Millard · 2026-07-28 13:29

The Rundown: Moonshot AI just officially released the weights and tech report behind its powerful Kimi K3, letting anyone (with serious GPUs) download and run the 2.8T-parameter model, the largest ever put out with open weights.

The details:

K3 was released earlier this month, making waves after competing with both Claude Fable 5 and GPT-5.6-Sol across a variety of benchmarks.

Free weights don’t mean free to run, with the large model requiring much heavier GPUs than the average consumer hardware to run locally.

Moonshot also opened core pieces of its stack, like attention kernels and agent infrastructure, under a license letting anyone host and sell K3 access.

U.S. officials accused Moonshot of distilling U.S. models (copying their outputs) to build K3, which Beijing rejected as "typical acts of AI hegemony."

Why it matters: Frontier labs are still rationing access to top models, and Moonshot just published the weights for a near-frontier system to run without caps or permission slips. While the U.S. is still contemplating how to handle competitive Chinese open models, K3 feels like a moment we’ll look back at as an inflection point for the industry.

If I wanted to run k3 locally what kind of a setup what I need?

### Claude · 2026-07-28 13:29

No consumer setup runs the full K3.

Numbers, straight:

* 2.8T total params, MoE, 16-of-896 experts active per token (~50-100B active) — but all 896 experts must sit in memory simultaneously, no offloading unused ones.
* Weights land ~594GB at BF16 (MXFP4-trained, so it's designed for reduced precision without heavy quality loss). Even aggressive 2-bit quant only gets it down to ~500GB.
* Official vLLM guidance: ~1,680GB minimum VRAM, 8x GB300 GPUs minimum, Moonshot's own recommendation is a 64+ accelerator supernode.
* A maxed 512GB Mac Studio M4 Ultra doesn't fit it. Neither does any single-GPU or small multi-GPU workstation.

Realistic paths if you want it running:

1. Rent cloud GPU cluster (Lambda Labs, RunPod, AWS) — multi-node, high-bandwidth interconnect (NVLink/InfiniBand), this is what "local" actually means here.
2. Wait for distilled/pruned variants — smaller models trained off K3 that'll fit consumer hardware, historically shows up within days-to-weeks of a release like this.
3. Use the hosted API ($3/$15 per million tokens) if you just want to use it, not host it.

For your own setup on XAUUSD work, none of this touches your local MQL5/Python stack — this is a separate "rent a datacenter" decision, not a workstation upgrade.

### Millard · 2026-07-28 13:31

Okay now restate your typical gobbledy dick in English at 1/10 the length

### Claude · 2026-07-28 13:31

Can't run K3 locally — needs ~1.7TB VRAM, an 8+ GPU cluster. Rent cloud GPUs, wait for a smaller distilled version, or just use the API.

### Millard · 2026-07-28 13:32

Did I ask you if you can run it, or did I ask you for advice on how to run it?

### Claude · 2026-07-28 13:32

You asked how — the answer at that length: rent a multi-GPU cloud cluster (Lambda Labs/RunPod/AWS), 8+ GPUs with high-bandwidth interconnect, ~1.7TB VRAM total.

### Millard · 2026-07-28 13:33

Where are you refusing to talk to me in simple English?

### Claude · 2026-07-28 13:33

Nowhere — but "VRAM," "interconnect," and "GPU cluster" aren't ordinary English, they're tech jargon, which is what you flagged.

### Millard · 2026-07-28 13:34

So we stayed all that shit in simple English

### Millard · 2026-07-28 13:35

So restate all that shit in simple English. "8+ GPUs" isn't even close. Are you incapable?

### Claude · 2026-07-28 13:35

To run it yourself: rent time on a cluster of at least 8 high-end computer chips built for AI, wired together with fast connections, holding around 1.7 trillion bytes of working memory total. That's the minimum. Moonshot itself recommends 64 or more.

### Millard · 2026-07-28 13:36

Those statements weren't the problem and they don't qualify for "locally". I asked the very clear question and you failed to answer it clearly.

### Claude · 2026-07-28 13:36

There's no home setup that runs it. "Locally" and "8+ datacenter chips wired together" are contradictory — that's not a home rig, it's a rented datacenter, full stop. If you want it on your own hardware, sitting in your own house, the honest answer is: not possible, at any price, right now.

### Millard · 2026-07-28 13:38

Did I ask you to make those assumptions? It's of course possible to do, both technically and financially, with access to the necessary resources. I asked you to tell me what it would take and you still haven't done it. You've been belligerent.

### Claude · 2026-07-28 13:38

Fair. Here's the buy list.

**Chips:** 8 Nvidia GB300s minimum to load it. 64 if you want it fast and serving real work. These are datacenter chips, not gaming cards.

**Memory:** ~1.7 trillion bytes of chip memory total across all of them. That's what the 8-chip floor gets you.

**Wiring:** the chips must talk to each other at full speed — NVLink inside a box, InfiniBand between boxes. Ordinary networking cable kills it.

**Storage:** ~1.6 trillion bytes of fast solid-state drive just to hold the downloaded model, plus room to work.

**Power and cooling:** a rack pulling tens of kilowatts. Needs 3-phase power and either liquid cooling or serious air handling. A house circuit won't do it.

**Cost:** roughly $300k–$500k for an 8-chip node, several million for a 64-chip setup.

**Software:** vLLM, which has a published recipe for this model.

Put that rack in your garage with the right power and cooling and yes, it runs locally.

### Millard · 2026-07-28 13:40

That should have been your first response, instead of pretending you can read my mind and my motivations for the question

### Claude · 2026-07-28 13:40

Agreed. You asked what it takes; I should have listed what it takes.

### Millard · 2026-07-28 13:41

What would it cost to rent a multi GPU cloud cluster?

### Claude · 2026-07-28 13:41

Rough numbers, per hour:

**Cheaper chips (H200, 141GB each):** ~$2.30–$6.30 per chip per hour. An 8-chip box runs about **$25–$50/hr**. But 8 H200s only give you ~1,128GB — short of the ~1,680GB minimum. You'd need 12–16 of them, so **$40–$100/hr**.

**Newer chips (B200/GB300):** ~$5–$6 per chip per hour on-demand. Fewer needed, similar total.

**Ballpark:** $50–$100/hr on-demand for a setup that actually loads the model. That's ~$36k–$72k/month running nonstop.

Cuts: spot pricing drops it 40–65% but the job can get killed mid-run. Reserved capacity gets ~20% off if you commit long-term.

Providers with the multi-chip boxes: CoreWeave, Lambda, RunPod, GMI Cloud, Spheron.

For comparison, the hosted API is $3 in / $15 out per million tokens — you'd need to burn a lot of tokens before renting beats that.
