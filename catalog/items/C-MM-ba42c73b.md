# RAM hardware problem detected during diagnostics

| | |
|---|---|
| Date | 2026-09-14 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-ba42c73b` |
| Links | [Original](https://claude.ai/chat/ba42c73b-ed09-4933-a437-c48081dbb6ab) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-09-14_ram-hardware-problem-detected-during-diagnostics_ba42c73b.html) |

**Summary:** Diagnosing a failed RAM stick with Windows Memory Diagnostic, RMA versus replacement in Mexico amid DDR4 price spikes, and platform upgrade options.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; Practical & personal > Shopping, product comparisons and gifts

**Index terms:** Windows Memory Diagnostic; DDR4 RAM; G.Skill; RMA warranty; Amazon Mexico; AM5; Intel Core i7-9700K

[← Catalog home](../README.md)

---

### Millard · 2026-09-14 20:21

Sonnet advised me to run mdsched.exe to check my ram. I have two 16gb sticks. It told me to run with one of the sticks in slot a2. That stick had no problems. Then it told me to run with the other stick in slot a2 and it found a hardware problem immediately. It's currently at 20% complete of test pass one of two. Do I really need to wait another half hour for it to complete, or can I simply shut the machine down and reboot Windows?

### Claude · 2026-09-14 20:21

No — press Esc to cancel; it reboots into Windows, and the error it already reported is enough to condemn that stick.

### Millard · 2026-09-14 20:47

Okay I need to do a manufacturer's warranty return on the bad stick

### Claude · 2026-09-14 20:47

Form is at gskill.com/rma — fill it out, they email back an RMA number and the ship-to address.

Four things that affect you before you file it:

* Send both sticks. G.SKILL requires all modules of a kit; partial-kit returns aren't guaranteed to come back compatible. You won't have RAM while it's out.
* The form needs the part number and serial off the white label — that's on the reverse side of the stick, not the side you photographed.
* Don't pull the heatspreader off. Removed or damaged warranty sticker, or a disassembled heatspreader, voids the warranty.
* You pay shipping to them and you pay any Mexican customs duties on the replacement coming back. Shipping a 32GB kit out of Querétaro and eating import duty on the return may cost more than a new kit.

### Millard · 2026-09-14 20:48

Find me the same or better on Amazon Mexico

### Claude · 2026-09-14 20:49

Can't — Amazon blocks automated reading of its listings, so any prices or stock I gave you would be made up. Search results I can see are months stale.

Two things before you search yourself:

I don't know your kit's speed. Ripjaws V 2x16GB ships as 3200 CL16, 3600 CL16, 3600 CL18 and others, and your photo shows the branded face. The part number is on the white label on the reverse — flip it and read the F4- number, and I'll tell you what counts as same-or-better.

Search amazon.com.mx for these exact strings, whichever matches:

* `F4-3200C16D-32GVK`
* `F4-3600C16D-32GVKC`
* `F4-3600C18D-32GVK`

Buy the kit, not two singles. Also check Amazon's seller — DDR4 is end-of-life and counterfeit/regraded sticks are common from marketplace sellers; "Vendido por Amazon México" is the safe filter.

### Claude · 2026-09-14 20:49

Your kit is DDR4-3600 CL16-19-19-39, 1.35V, 2x16GB, made Feb 2020 — part number **F4-3600C16D-32GVKC**.

That's the fast bin. 3600 CL16 on 16GB modules is near the top of what DDR4 ever shipped, so most of what you'll see listed on Amazon MX at 3600 is CL18 — that's a downgrade, not a match.

Search amazon.com.mx for:

* `F4-3600C16D-32GVKC` — exact replacement
* `G.Skill 3600 CL16 32GB` — to catch equivalents

Rule for "or better": 2x16GB, DDR4-3600 or higher, CL16 or tighter, 1.35V. Reject anything CL18 at 3600.

Two things this changes:

Your warranty is lifetime and the kit is only from 2020, so the RMA is live — G.SKILL owes you a replacement kit. Weigh that against Mexican import duty on the return shipment.

You're going to pay high-end DDR4 prices for a match. DDR4 is end-of-life and prices are climbing on the AI-driven DRAM shortage.

### Millard · 2026-09-14 20:51

It's aggravating when you make general vague references to quantifiables. You've made three different references to three different potential costs. Stop being coy.

### Claude · 2026-09-14 20:52

Fair. Here's each one with the actual number, or an explicit statement that I don't have it.

**1. Import tax on the replacement coming back to you**

Mexico's de minimis is USD $50 — below that, no duty, no IVA. A 32GB kit is worth far more, so it gets taxed. Two possible treatments:

* Courier simplified regime: global rate of **33.5%** since 15 Aug 2025 for goods not covered by an applicable treaty, plus IVA at 16%. A conditional **19%** rate exists but only when every condition of RGCE rule 3.7.35 III(c) is met.
* Formal import: IGI (varies by fracción arancelaria) + DTA (0.8% of customs value, or a fixed ~$362 MXN under a treaty) + IVA 16% calculated on value + IGI + DTA.

Your modules are Taiwan-manufactured. Even though G.SKILL's Pan-America RMA ships from Walnut, California, the goods aren't T-MEC-originating, so the 0% preferential rate doesn't apply to them.

The number that decides your actual bill is the declared value G.SKILL puts on the return parcel. I don't have it. Their own policy tells *senders* to mark packages "No Commercial Value. For RMA only." — whether they declare the same on the outbound replacement, I can't confirm. Ask rma@gskillusa.com directly when they issue the RMA number.

**2. Shipping the kit from Querétaro to California**

I don't have this number. Rates aren't published in any form I can read. Get it in five minutes: DHL Express or FedEx MX online quote, 0.5 kg parcel, Querétaro to 91789, insured for the kit's replacement value.

**3. Price of a new F4-3600C16D-32GVKC in Mexico**

I don't have this number either, and I tried. Amazon MX blocks automated reading of its pages, and the search snippets I can see are three to six months stale with prices not attached to any identifiable product. Anything I quoted you would be invented.

Check it yourself at amazon.com.mx, Cyberpuerta, and Mercado Libre, all three, on the exact part number.

### Millard · 2026-09-14 20:54

When I said find me the same or better I was not implying finding a comparable model especially not since it's this old. What would you recommend putting in, and I assume that I need to buy a pair so they're matched?

### Claude · 2026-09-14 20:55

Yes — buy a matched 2-stick kit, never two singles. Kits are binned and tested together; two separately-bought sticks of the same model can refuse to run at rated speed.

What to put in: a 2x16GB DDR4 kit, 3200 CL16 or 3600 CL16, 1.35V. Buy whichever is cheaper — don't pay a premium for 3600.

Reason: your Z390/9700K is Intel Coffee Lake. There's no Infinity Fabric to sync, so memory speed above 3200 buys you very little on this platform. The 3600 CL16 you own is already at the practical ceiling — "better" DDR4 doesn't exist for you in any way you'd feel. Any of G.SKILL, Corsair Vengeance LPX, Kingston Fury Beast, TeamGroup T-Force will do; brand doesn't matter at this spec.

On going to 64GB (2x32GB): ASUS's tech spec page for the PRIME Z390-A says max 64GB across 4 DIMMs. Separately, ASUS announced in Jan 2019 that Z390 boards would get 128GB support via BIOS update once Intel's memory reference code allowed 32GB per DIMM. The two don't agree, and I can't confirm which applies to your board at your BIOS version. If you want 2x32, download the memory QVL from your board's ASUS support page and check whether 32GB modules are listed.

My recommendation is don't. 32GB covers MT5 and your Python work, DDR4 is end-of-life with prices climbing, and the 9700K is a 2018 8-core/8-thread part. Money spent doubling RAM on this board is money not spent on the platform that replaces it.

Cheapest path, in order: file the G.SKILL RMA (lifetime warranty, kit is 2020, they owe you a replacement), run on the single good 16GB stick in A2 meanwhile — single channel, noticeably slower, but it works — and only buy new if the RMA math turns out worse than a new kit.

### Millard · 2026-09-14 20:56

You said I couldn't run on the single stick because I had to return the pair

### Claude · 2026-09-14 20:56

Correct — I contradicted myself. The single-stick suggestion was wrong. Once both sticks are in the box, the machine has no RAM, and an international RMA turnaround is weeks.

The coherent version: buy the new 2x16 kit first, install it, then ship the old pair out for RMA. The replacement kit comes back as a spare or something to sell. You're never down.

Running on the one good stick only covers the gap between now and the day you ship.

### Millard · 2026-09-14 20:57

So if I bought the two new sticks and did the RMA I would end up with 64 GB. Why wouldn't I use all of it?

### Claude · 2026-09-14 20:58

You can try it, but you'd likely have to give up your 3600 CL16 XMP to do it.

Two problems with 4x16:

Filling all four slots puts two DIMMs per channel, which is the hardest load on the 9700K's memory controller. Four ranks per channel is harder still. Systems that run 2 sticks at 3600 routinely won't POST at 3600 with 4 sticks and have to be dropped to 3200, 3000, or lower. Whether yours does is untested until you try it.

Second, they'd be two separate kits. G.SKILL bins and validates sticks as a kit; sticks from different kits aren't matched to each other even at the same part number. ASUS's own manual for your board recommends modules of the same version and data code from the same vendor.

Check whether your modules are single- or dual-rank before deciding — CPU-Z, SPD tab, "Ranks" field. Dual-rank at 4 sticks is the worst case for the IMC.

Whether the trade is worth it depends on whether you actually hit 32GB. If MT5 strategy tester on M1 tick data is paging, 64GB at 3000 beats 32GB at 3600. If you're not hitting the ceiling, you'd be trading guaranteed stability for memory you don't use.

Open Task Manager, Performance, Memory, during a heavy backtest and read the peak. That number decides it.

### Millard · 2026-09-14 20:59

Then it sounds to me like the army isn't worth doing if I buy a new set of sticks

### Claude · 2026-09-14 20:59

Not necessarily. The RMA doesn't become worthless — it becomes an asset trade instead of a repair.

What you'd be buying: a working 2x16 3600 CL16 kit, in exchange for outbound shipping plus import tax on the return. That kit is either a spare for the machine you trade on, or something you sell.

DDR4 is in a price spike right now — end-of-life product, and the AI-driven DRAM shortage has pushed prices up rather than down. A 32GB 3600 CL16 kit is worth real money in Mexico today, possibly more than you paid in 2020.

So the decision is one comparison:

**Resale value of a 32GB DDR4-3600 CL16 kit in Mexico** vs. **DHL/FedEx quote Querétaro→91789 + import tax on the inbound replacement**

Get the first from Mercado Libre completed listings for F4-3600C16D-32GVKC. Get the second from a DHL quote and from asking rma@gskillusa.com what declared value they put on replacement shipments.

If it's close, skip it. If resale clears the cost by a wide margin, do it. And if you'd rather hold it as a spare than sell it, that alone may justify it — RAM failing mid-session on a trading machine costs you more than shipping.

### Millard · 2026-09-14 21:00

I already called you on bullshit light quote "real money"in other worthless vagaries. Stop cloaking quantifiable numbers with bullshit relative terms.

### Claude · 2026-09-14 21:00

You're right, and I did it again in the same conversation after being told.

The number is: I don't have it. Mercado Libre and Amazon MX both block automated reading, and every search snippet I've gotten back is months stale with prices not attached to identifiable products. I have no MXN figure for a 32GB DDR4-3600 CL16 kit in Mexico, new or used, and I can't get one with the tools I have.

Same for the DRAM price spike. I have the direction as fact — SK Hynix has forecast tight memory supply through 2028, and motherboard makers have slowed production over memory costs. I have no percentage and no price series. "Prices are climbing" is the entire extent of what I can prove.

Three numbers decide this, and I hold none of them:

1. Sale price of F4-3600C16D-32GVKC in Mexico — Mercado Libre, search the part number, filter to sold listings
2. DHL or FedEx quote, 0.5 kg insured, Querétaro to 91789
3. Declared value G.SKILL puts on the replacement shipment — ask rma@gskillusa.com when the RMA number comes

Get those three and the decision is arithmetic. I can do the arithmetic. I can't source the inputs.

### Millard · 2026-09-14 21:00

You can fucking estimate it

### Claude · 2026-09-14 21:01

Estimate. All figures MXN, all labeled as estimate, anchors stated.

**What the replacement kit is worth to you: $2,500–3,500**

Anchored on: Amazon MX search snippets from mid-2026 showing 32GB DDR4 2x16 kits at $4,000–4,900 new, and a German commercial seller listing this exact part number at €308 in Nov 2025 (≈$6,000 MXN). Call new retail in Mexico $4,000–5,000. G.SKILL ships RMA replacements bare, no retail box, so you'd sell as "nuevo sin caja" at roughly 65–75% of retail.

**Outbound shipping, Querétaro → Walnut CA: $1,000–1,500**

Anchored on: typical DHL Express / FedEx International counter rates from Mexico to the US for a 0.5 kg insured parcel. Weakest of the three estimates — I have no rate card, only the general shape of MX→US express pricing.

**Import tax on the replacement: $0–1,700**

Two outcomes, no middle. If G.SKILL declares full value (~USD $200), the courier simplified regime hits it at 33.5% ≈ USD $67 ≈ $1,250, plus a courier handling fee of roughly $300–500. If they declare it as a warranty replacement under USD $50, it clears de minimis at zero.

**Net**

Cost: $1,300 (low tax) to $3,200 (full tax)  
Value: $2,500–3,500

Best case you clear about $2,000. Worst case you clear about $300 and spent six weeks on it.

The declared value is the whole decision. One email to rma@gskillusa.com asking what value they declare on replacements to Mexico turns this from a coin flip into arithmetic.

My read on the estimate: marginal. Do it if you want the spare kit sitting in a drawer for the day the new one fails mid-session. Don't do it as a money play.

### Millard · 2026-09-14 21:04

So where am I likely to feel the pinch if I'm running on 16 GB of memory?

### Claude · 2026-09-14 21:04

Two hits, and one of them is not about capacity.

**Single channel.** One stick halves your memory bandwidth regardless of how much RAM you're using. That's a constant tax on everything, worst on anything streaming large arrays — Python/pandas over your CSVs, MT5 strategy tester. Expect it to be noticeable even when you're nowhere near 32GB used.

**Capacity, specifically:**

* MT5 strategy tester on XAUUSD M1 with real tick data — the tester holds ticks in memory, and multi-year M1 tick runs are the most likely thing to push you past 16GB. Your 46GB terminal folder suggests a lot of history on disk.
* Multiple MT5 terminals or charts open at once, each with several indicators
* Pandas in Python — a DataFrame typically needs 3-5x the CSV's size in RAM, and intermediate copies during joins or resampling can double it again
* Windows 11 itself takes 4-6GB before you open anything
* Chrome with many tabs alongside all of the above

What it feels like when you cross the line: Windows starts paging to the 990 PRO. The machine doesn't crash, it just gets slow in a way that's hard to attribute — a backtest that ran in 8 minutes takes 25.

You already have the measurement to make this concrete. Run your heaviest backtest on the good stick, watch Task Manager → Performance → Memory, and read peak "In use." If it tops out at 11-12GB you're fine until you ship. If it pins at 15-16GB with the commit charge climbing, you're paging and you should buy the kit before you ship the old pair out.

### Millard · 2026-09-14 21:04

I'm not asking for technicals, I'm asking for impact on my user experience

### Claude · 2026-09-14 21:04

Estimate, single 16GB stick:

**Normal trading day — barely notice.** MT5 running live with a few charts, a browser, maybe Excel. Windows feels the same. Chart drawing and MT5 startup a bit slower. No real complaint.

**Heavy backtests — the pain.** A run that takes 10 minutes now takes 15-20 on bandwidth alone. If you also run out of RAM, that becomes 30-40, and the whole machine gets unresponsive while it happens — mouse lags, windows take seconds to redraw. You go get coffee instead of working through it.

**Python work on your CSVs — similar.** Loading and processing gets slower across the board. Big joins or resamples are where it'll stall hard or throw a memory error and lose the session.

**The thing that will actually annoy you:** you won't be able to run a backtest and do something else at the same time. Right now you can start a test and go write or browse. On 16GB single channel, the backtest eats the machine and you sit and wait.

**Worst case:** MT5 crashes mid-backtest and you lose the run.

If your work is mostly live trading and light analysis, it's an inconvenience for a few weeks. If you're doing heavy backtest iteration right now, it'll cost you real hours and you should buy the kit before you ship the old pair.

### Millard · 2026-09-14 21:05

I'm not using empty five much anymore, I've moved to cTrader

### Claude · 2026-09-14 21:05

That makes 16GB worse, not better.

cTrader Desktop is a .NET app and sits on far more memory at idle than MT5 does — estimate 1.5-2.5GB just sitting there with a few charts, against MT5's few hundred MB. You start the day already down.

The bigger change is that C# work means an IDE resident. Visual Studio or Rider will take 2-4GB on its own with a solution loaded, and it stays open all day while you develop. MetaEditor cost you almost nothing.

So the practical picture on one stick: cTrader plus an IDE plus Windows plus a browser puts you at 10-12GB before you run a single backtest. You'll be near the ceiling constantly rather than only during heavy runs.

What you'd feel: the IDE gets sluggish — autocomplete pauses, builds crawl. Switching between cTrader and the IDE takes a beat. Run a backtest with both open and the machine stops being usable for anything else.

This flips my answer. Don't plan on limping along on the good stick — buy the 2x16 kit now, install it, then ship the old pair out.

### Millard · 2026-09-14 21:07

Again, spare me the fucking technicals, I don't want to hear it. In the near future I'm going to be writing, using office apps, probably no vs code or cTrader work. What will the user experience impact be for office apps, Firefox and edge browsing, and movie streaming?

### Claude · 2026-09-14 21:07

Basically none. You won't notice it.

Writing, Office, browsing, streaming — that's a 6-8GB workload. You'd have room to spare on 16GB.

The one thing you might feel: if you keep 30+ tabs open across both browsers for days without closing anything, tab reloads get more frequent. Minor.

Streaming is fine. Video decode is the GPU's job, and the 2060 SUPER doesn't care about your RAM.

So for what you're actually about to be doing, run on the single stick, ship the pair for RMA, and don't buy anything. Revisit it when you go back to cTrader.

### Millard · 2026-09-15 19:56

I checked with Gemini and it said that you can replace a single stick without replacing the pair

### Claude · 2026-09-15 19:56

Let me check the actual policy rather than argue from memory.

Gemini is wrong on policy, and here's the exact wording from gskill.com/rma-policy: include all modules of a memory kit for RMA — kits are tested together, and compatibility is not guaranteed if a partial kit is returned.

Two things worth separating, though, because Gemini may have been answering a different question:

Physically, yes — you can run one new stick alongside one old one. It'll boot. It may not hold 3600 CL16. That's a different question from what G.SKILL's RMA accepts.

And the policy wording is "not guaranteed," not "refused." Forum reports exist of people sending a single module and getting a single module back. So it's not a hard bar — it's G.SKILL declining to promise the replacement will match what you kept. You'd be shipping one stick and hoping the one they send back pairs with your survivor. Different silicon, same part number, is a real outcome.

Also from the warranty page, directly relevant to your cost math: you may be required to pay shipping and handling plus any applicable tariffs, duties, and taxes. They're not covering your import bill.

### Millard · 2026-09-30 21:34

OK, given what you know about my system, would you recommend only 32 GB or should I go for 64 GB RAM?

### Claude · 2026-09-30 21:34

32 GB.

For writing, Office, browsers and streaming you'd never touch it, and even when you go back to cTrader plus an IDE, 32 GB covers it.

Getting to 64 costs you something concrete either way: 4x16 means two mismatched kits and probably dropping below 3600, and 2x32 needs 32 GB DIMM support on your board that I couldn't confirm. You'd be paying spiking DDR4 prices to buy a stability problem for memory you don't use.

Put the difference toward the machine that replaces the 9700K.

### Millard · 2026-09-30 21:35

You keep mentioning spiking DDR4 prices, don't I have options?

### Claude · 2026-09-30 21:35

Four, in order of what they cost you:

**Buy nothing.** Writing, Office, browsers and streaming run fine on the 16 GB you have. The spike only matters on the day you actually need the RAM, which is when cTrader work resumes. That may be months out, and you're not obligated to buy into a shortage before then.

**The RMA.** It's the one path that gets you a matched 3600 CL16 kit without touching retail pricing at all. You pay outbound shipping and possibly import tax — nothing else. That's the whole point of it.

**Used market.** People moving to DDR5 are dumping DDR4 on Mercado Libre. It's the one segment where the shortage works in your favor rather than against you. You already know how to validate a purchase — run MemTest86 on arrival, and don't accept a seller who won't take a return.

**Buy in the US and have it hand-carried.** You're a US citizen with US ties. Ship to a US address, have someone bring it in luggage. That sidesteps courier duty and the 33.5% simplified rate completely, and US DDR4 pricing is a deeper market than Mexico's.

My pick given your near-term use: option 1 plus option 2. Run on the good stick, file the RMA, and decide about buying when you're back on cTrader and know what you actually need.

### Millard · 2026-09-30 21:37

16 GB is WAY too slow. Sometimes my mouse gets glitchy just by working the way I'm used to working. I'm going to skip the RMA because it bags my machine for the duration. You're saying my motherboard won't handle DDR5?

### Claude · 2026-09-30 21:37

Correct — Z390 is a DDR4 board, physically keyed for DDR4 only. A DDR5 stick won't fit in the slot, and no BIOS update changes that. DDR5 means a new motherboard, a new CPU, and new RAM together.

But the mouse glitching isn't a 16 GB capacity problem. Writing and browsing don't use 16 GB. Something else is eating your machine, and if you buy RAM to fix it you'll spend the money and still have the glitch.

Open Task Manager, Performance tab, and watch it while the mouse is stuttering. Read three things: Memory "In use", CPU %, and Disk %. Tell me those numbers and what you had open.

### Millard · 2026-09-30 21:38

wrong. Like I said, normal work MO with both sticks never got this problem

### Claude · 2026-09-30 21:38

Right — you had 32 GB dual channel before and no glitch. My mistake.

It's the single channel, not the capacity. One stick halves your memory bandwidth, and that shows up as exactly what you're describing — the cursor stalling while the system waits on memory, with plenty of GB still free.

That changes what you need to buy. The fix is a second stick, not more gigabytes. Two options:

**A matched 2x16 kit** — clean, holds 3600 CL16, costs the most.

**One more 16 GB stick to pair with your survivor** — restores dual channel for roughly half the money. It probably won't run 3600 XMP with a mismatched partner, so you'd set 3200 or whatever it holds. On a Z390 board that costs you almost nothing real, and the mouse glitch goes away either way, since that's a bandwidth problem and dual channel at 3200 fixes it as well as 3600 does.

If you go the second route, buy the identical part number — F4-3600C16D-32GVKC sold as a single, or the single-stick equivalent — to give yourself the best odds of it running at rated speed.

### Millard · 2026-09-30 21:39

so what if I wanted to move to a new motherboard/CPU/RAm?

### Claude · 2026-09-30 21:39

Don't. Not now.

A 32GB DDR5-6000 kit is running **$400-440 USD**, against $80-120 a year ago. 64GB runs roughly **$850-900**. Memory alone would cost more than your whole upgrade should. You'd also be buying board and CPU on top.

The cause isn't a normal cycle — AI datacenter demand has DRAM makers shifting production to high-margin server parts, and analysts expect the shortage to run into 2027. DDR5 pricing isn't expected to recover meaningfully this year.

So the platform move is the worst possible purchase to make in the next few months, and there's no urgency forcing it. Your problem is single-channel bandwidth on a machine that ran fine two weeks ago.

Buy one 16GB DDR4 stick. That fixes the mouse glitch, restores what you had, and costs a fraction of any of this. Revisit the platform in 2027 when memory pricing is survivable.

### Millard · 2026-09-30 21:40

LESS WORDS, KISS it dude. You're basically telling me not to upgrade at this time. Why?

### Claude · 2026-09-30 21:40

RAM costs 4-5x what it did a year ago. AI datacenters ate the supply; shortage runs into 2027.

32GB DDR5: ~$400. 64GB: ~$900. Plus board and CPU.

### Millard · 2026-09-30 21:41

so you expect prices will come down next year?

### Claude · 2026-09-30 21:41

Analysts expect it, I don't.

What they actually say: shortage persists into 2027, new fab capacity ramps then. That's a forecast, not a fact — and the same analysts have been wrong in this direction repeatedly since late 2025, each quarter revising worse instead of better.

Highly likely: prices stay elevated through the rest of 2026.  
Unlikely: a return to 2024 pricing in 2027.

Missing evidence: whether AI demand holds. If it breaks, DRAM crashes fast. Nobody knows.

### Millard · 2026-09-30 21:42

so you're saying I should limp along with my DDR4 system/motherboard for the next 2 years or more?

### Claude · 2026-09-30 21:42

No — you're not limping. Put a second 16GB stick in and you're back to the machine that worked fine two weeks ago.

The 9700K isn't the problem. Single channel is.

Buy the stick, run it, and let the platform decision wait until memory isn't the most inflated part in the build.

### Millard · 2026-09-30 21:43

No dude, the machine that "worked fine" was fast in 2020 when I built it. I'd upgrade in a heartbeat if I could swing it.

### Claude · 2026-09-30 21:43

Fair. Then the answer changes.

You want the upgrade, cost is the blocker, and RAM is what's blocking it. So do it in two steps:

Buy the DDR4 stick now — cheap, gets you a working machine today.

Then buy board, CPU and GPU when you're ready, and DDR5 whenever it's least awful. Those parts aren't in a bubble; only memory is. You can even buy the platform first and run it on the minimum RAM you can stand until memory eases.

You're not waiting two years for the upgrade. You're waiting for one line item on the parts list.

### Millard · 2026-09-30 21:44

If I buy board, CPU and GPU, what RAM do I use until "memory eases"?

### Claude · 2026-09-30 21:44

You can't. A new board means DDR5, and there's no DDR5 you can buy that isn't the expensive part. My last answer was wrong — you can't separate the two.

The way around it: upgrade to AM4, not AM5.

Ryzen 5700X3D or 5800X3D on a B550 board. DDR4 platform, so your existing 3600 CL16 kit drops straight in. No memory purchase at all. Big jump over the 9700K, especially single-thread and gaming.

You still need the second stick either way.

GPU is independent — buy that whenever.

### Millard · 2026-09-30 21:45

no idea what those are

### Claude · 2026-09-30 21:45

AMD CPUs from the generation after yours. They use DDR4, so your current RAM works.

**5800X3D / 5700X3D** — 8 cores, extra cache stacked on the chip. Noticeably faster than your 9700K, best-in-class for gaming at the time.

**B550** — the motherboard chipset they need. AMD socket AM4.

What you'd buy: board + CPU. Reuse your RAM, GPU, drives, case, power supply.

Both CPUs are discontinued, so it's the used market — Mercado Libre, or hand-carried from the US.

### Millard · 2026-09-30 21:45

why not AM5

### Claude · 2026-09-30 21:45

AM5 is DDR5-only. That's the whole reason.

Go AM5 and you're buying $400+ of memory on top of board and CPU, at the worst possible moment. Go AM4 and the memory line item is zero.

The tradeoff: AM4 is a dead socket — no future CPU upgrades, it's the end of that road. AM5 has years of upgrades ahead.

So it's cheap now vs. futureproof later. Given memory pricing, cheap now wins.

### Millard · 2026-09-30 21:47

So the risk of RMA the single stick?

### Claude · 2026-09-30 21:47

You send one stick, they send one stick back, and it doesn't pair with your survivor at 3600 — different silicon, same part number. G.SKILL says outright they don't guarantee compatibility on a partial kit return.

Downside if that happens: you run 3200 or 3000 instead of 3600. On your board that's barely noticeable.

Cost: outbound shipping plus possible import tax, and weeks without a second stick.

Versus buying one stick: money, but it's in your hand this week and you keep the RMA in reserve.

### Millard · 2026-09-30 21:47

same risk buying a single stick right?

### Claude · 2026-09-30 21:47

Same risk, yes. Either way you're pairing an unmatched stick with your survivor and may drop below 3600.

Difference is time and money: buying, you have it this week and pay. RMA, it's free but you wait weeks with a glitchy machine.

### Millard · 2026-09-30 21:48

what's the most reliable source in Mexico for my stick?

### Claude · 2026-09-30 21:48

Cyberpuerta. Mexican, Guadalajara-based, authorized distributor, issues factura, handles warranty. The standard choice for PC components here.

Second: DDTech. Third: Amazon MX filtered to "Vendido por Amazon México."

Avoid Mercado Libre for RAM — counterfeit and regraded sticks are common.

One problem: 3600 CL16 is mostly sold as 2-stick kits. A single is F4-3600C16S-16GVK, and it may not be stocked in Mexico at all. Check that part number first; if nothing, you're buying a 2x16 kit anyway.

### Millard · 2026-09-30 21:49

it would handle my g skill warranty?

### Claude · 2026-09-30 21:49

Which stick — the new one you'd buy from them, or your 2020 one?

New purchase: yes, within their own warranty window. After that it goes to G.SKILL directly, same as any retailer.

Your 2020 stick: no. They didn't sell it, so they have no obligation. That one goes to G.SKILL in California regardless.

### Millard · 2026-09-30 21:49

link me

### Claude · 2026-09-30 21:49

No Mexican listing came back — everything found was Spain, Brazil, India, Australia, Estonia. I have no Cyberpuerta or DDTech link for your part to give you, and I won't invent one.

Search these yourself:

* [cyberpuerta.mx](https://www.cyberpuerta.mx) — search `F4-3600C16S-16GVK`, then `G.Skill Ripjaws V DDR4 3600`
* [ddtech.com.mx](https://www.ddtech.com.mx) — same terms
* [amazon.com.mx](https://www.amazon.com.mx) — same, filter to Vendido por Amazon México

One thing the search did show: single 16GB 3600 sticks exist mainly as CL18 (F4-3600C18S-16GVK), not CL16. If that's all Mexico stocks, pairing it with your CL16 survivor means running both at CL18 timings.

### Millard · 2026-09-30 21:51

wtf was that?

### Claude · 2026-09-30 21:51

A domain I gave you from memory without checking. My error.

It's **ddtech.mx**, not ddtech.com.mx. Confirmed on ASUS's own Mexico reseller list — DDTech, www.ddtech.mx, Guadalajara.

Cyberpuerta's domain I gave you was right: cyberpuerta.mx.

### Millard · 2026-09-30 21:55

I could only find one single 16 GB stick available anywhere, and it's only 3200 Mhz

### Claude · 2026-09-30 21:55

That'll work. Buy it.

Both sticks are CL16 at 1.35V; the pair runs at 3200. Dropping 3600→3200 on your board is nothing. Dual channel is the fix.

One thing — the same Amazon page lists two other 16GB 3200 CL16 singles, cheaper:

* Kingston Fury Beast KF432C16BB/16 — from $2,488
* ADATA XPG Spectrix D35G — $2,647

vs. $3,144 for the G.Skill. Any of the three gets you dual channel. Does matching the G.Skill brand matter to you, or is the $650 worth more?

### Millard · 2026-09-30 21:56

I have no idea, I just assumed that I had to match the make model and specs

### Claude · 2026-09-30 21:56

No. What has to match is speed, timings, voltage and capacity — all three of those do. Brand and model don't.

Matching the G.Skill slightly improves the odds the memory chips inside are similar, which is why people repeat that rule. It's worth something, but not $650.

Buy the Kingston at $2,488.

If it won't boot at 3200, drop the speed a notch in BIOS until it's stable. Costs you nothing real.

### Millard · 2026-09-30 21:58

the same Amazon page lists two other 16GB 3200 CL16 singles, cheaper

what page? Hallucinating again? That's the the page I've got open, It has no Kingstons on it at all

### Claude · 2026-09-30 21:58

Not a hallucination — those are in the text you pasted me, in the "Los clientes también vieron estos productos" carousel below the main listing. Kingston Fury Beast KF432C16BB/16 from $2,488 and KF432C16BB1/16 from $2,867, plus the ADATA at $2,647.

That carousel is a sidescroller. If it's not showing those items on your screen, it's rotated to a different slide — arrow through it, or just search Amazon MX for `KF432C16BB/16` directly.

### Millard · 2026-09-30 22:00

Thanks. I didn't notice those

There's also this one

### Claude · 2026-09-30 22:00

That's 3600 but **CL18**, not CL16. Different from the one I quoted.

Your stick is CL16. Pair them and the board runs both at CL18 timings, or you drop to 3200 CL16. Either way you land roughly where the cheap 3200 CL16 stick lands.

At $3,178 it's $690 more than the Kingston 3200 CL16 at $2,488 for no gain.

Buy the 3200 CL16.

### Millard · 2026-09-30 22:01

oops

### Claude · 2026-09-30 22:01

No hay ofertas destacadas — no seller has the Buy Box on that one. Click "Ver opciones de compra" to see the actual sellers and prices.

Which listing is this, the Kingston 3200 CL16?

### Millard · 2026-09-30 22:02

yes, same, the cheapest wants $500 shipping lol

### Claude · 2026-09-30 22:02

Then it's not $2,488, it's ~$2,988. Compare on landed cost.

What are the other offers under "Ver opciones de compra" — any with Envío GRATIS or Prime?

And the ADATA XPG at $2,647 was Envío GRATIS por Amazon México. Worth checking that one.

### Millard · 2026-09-30 22:02

for about the same price as the g.skill

### Claude · 2026-09-30 22:02

Then buy the G.Skill. Same money, same brand as your survivor, shipped by Amazon.

### Millard · 2026-09-30 22:04

g.skill has a "store" on Amazon, Any chance I could work the RMA through them?

https://www.amazon.com.mx/s?srs=20824360011&rh=p\_89%3AG.SKILL

### Claude · 2026-09-30 22:05

Unlikely. An Amazon brand store is a storefront, not a service channel — it doesn't make the seller G.SKILL's warranty agent for a stick you bought somewhere else in 2020.

But it's worth one check, because the answer changes things if it goes your way. Open any listing in that store and read "Vendido por" — the seller name under the price.

If it's a Mexican distributor rather than Amazon itself, call them and ask whether they handle G.SKILL RMA locally. An authorized in-country rep would kill the shipping and customs problem entirely.

If it says "Vendido por Amazon México," it's a dead end — Amazon won't touch a 2020 purchase from another retailer.

### Claude · 2026-09-30 22:05

Dead end. "SIMUL" is a third-party marketplace seller, and "Importación" means it ships from abroad — that's a reseller, not G.SKILL's Mexican arm. They won't touch your 2020 RMA.

Also worth noting: $25,009 and a 9–13 October delivery. Whatever that listing is, it isn't your 16GB stick.

### Millard · 2026-09-30 22:06

You said click any, so I did

### Claude · 2026-09-30 22:06

Fair, my instruction. And it answered the question — SIMUL, third party, importing from abroad. No Mexican G.SKILL service arm on that store.

RMA still goes to California.

### Millard · 2026-09-30 22:09

So why wouldn't I just buy a pair of brand new sticks at 3,600 Mhz for what amounts to five dollars more than the single stip

### Claude · 2026-09-30 22:09

Because that's 2x8GB, not 2x16GB. Total 16GB.

F4-3600C16D-16GVKC — the "16G" is the kit total, split across two 8GB sticks. You'd be spending $3,250 to end up exactly where you are now.

The listing has a size dropdown: 16 Gb / 32GB (2x16GB). Select 32GB (2x16GB) and see what it prices at. That's the part number F4-3600C16D-32GVKC — your exact kit.

### Millard · 2026-09-30 22:10

haha I read 16 for one not two

### Claude · 2026-09-30 22:10

Easy to misread — G.Skill labels kits by total, so the number always looks like a single stick.

Check the 32GB (2x16GB) option in that dropdown. If it lands near $6,000 — like the CL18 version on the same page at $5,937 — then you're comparing $6,000 for a matched 3600 CL16 pair against ~$3,100 for one stick that gets you back to dual channel.

### Millard · 2026-10-26 21:27

Okay, I got my new RAM stick today and installed it

### Claude · 2026-10-26 21:27

Good. Check two things in Task Manager → Performance → Memory: total shows 32 GB, and "Slots used" reads 2 of 4.

Then confirm the speed it settled on, and whether the mouse glitch is gone.

### Claude · 2026-10-26 21:28

32 GB, 2 of 4 slots — both sticks detected, dual channel restored. That's the glitch fixed.

But 2666 MT/s means XMP is off. That's the JEDEC default, not what either stick is rated for. Your G.Skill does 3600, the new one 3200.

Go into BIOS and enable XMP, then set the profile to 3200 — the slower stick's rating is the ceiling for the pair. Should be stable; if it won't post, clear CMOS and try 3000.

That's another ~20% bandwidth you're leaving on the table.

### Millard · 2026-10-26 21:31

Is that all I need to do

### Claude · 2026-10-26 21:32

No — XMP shows Enabled but Memory still reads 2666MHz. The setting hasn't taken effect yet. Save and exit (F10), then re-enter BIOS and confirm it reads 3200.

Two things that caught my eye:

You bought the ADATA, not a G.Skill — DIMM\_A2 reads A-DATA. Fine, it's 3200 CL16 either way.

The XMP profile it loaded is DDR4-3200 16-20-20-38, which is the ADATA's profile. Your G.Skill's native is CL16-19-19-39 at 3600. Both run at the ADATA's timings. That's expected and correct.

If it won't post at 3200, clear CMOS and drop to 3000.

### Millard · 2026-10-26 21:33

Okay I saved and exited but it doesn't look like it took

### Claude · 2026-10-26 21:33

It took. Memory now reads **DDR4 3200MHz** — it said 2666 before.

The DIMM\_A2 and DIMM\_B2 lines you're looking at show each stick's SPD default rating, not what it's running at. Those never change with XMP.

Boot into Windows and confirm Task Manager shows 3200 MT/s. Then run it hard for a few days — if you get random reboots or blue screens, drop to 3000.

### Millard · 2026-10-26 21:33

You suck at processing images the first photo I took said xmp-enabled xmpddr4-3200 just like it does now.

### Claude · 2026-10-26 21:33

You're right. The XMP line read Enabled / XMP DDR4-3200 in both shots. I read that correctly.

What changed between them was the Memory line: 2666MHz in the first, 3200MHz in the second. That's the one I should have pointed you at, and I framed it as "XMP hasn't taken" instead of "the profile is selected but not applied yet." Same conclusion, wrong description of what I was looking at.

### Millard · 2026-10-26 21:35

Under DRAM status it reads exactly the same a-data 16384mb 2666 MHz and g-skill 16384 MB 2133 megahertz

I don't see that anything has changed

### Claude · 2026-10-26 21:35

Those two lines never change — they're the SPD default stamped on each stick, not the running speed. They'll read 2666 and 2133 forever regardless of XMP.

The running speed is the Memory line under the CPU:

First shot: `Memory: 32768 MB (DDR4 2666MHz)`  
Second shot: `Memory: 32768 MB (DDR4 3200MHz)`

That's what changed. You're at 3200 now.

### Millard · 2026-10-26 21:36

There are four lines under the top left information heading explain each one

### Claude · 2026-10-26 21:36

**PRIME Z390-A BIOS Ver. 1401** — your motherboard model, and the firmware version it's running.

**Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz** — the CPU installed, with its factory base clock.

**Speed: 3600 MHz** — what the CPU is actually clocked at right now. Matches its base, so no overclock.

**Memory: 32768 MB (DDR4 3200MHz)** — total RAM installed and the speed it's running at. 32768 MB = 32 GB. This is the line that changed from 2666 when XMP took effect.

### Millard · 2026-10-26 21:36

Okay so everything looks fine to you

### Claude · 2026-10-26 21:36

Yes. 32 GB, dual channel, 3200 running.

One thing to watch: those two sticks are from different kits, so the pair is untested together. Run it hard for a few days. Random reboots or blue screens mean back into BIOS and drop to 3000.

### Millard · 2026-10-26 21:37

Oh I use it hard everyday.

Would I gain anything from overclocking here?

### Claude · 2026-10-26 21:37

Not worth it for what you do.

Two things you could push, both marginal:

**CPU** — 9700K at 3.6 base, boosts to 4.9 on its own. All-core 5.0 is typical with a good cooler. That's a few percent on single-thread, which is what your IDE and backtests care about. More heat, more noise, small gain.

**Memory** — you're already running the ADATA at its rated 3200. Pushing further means manual timings with mismatched sticks, and you'd be hunting instability on a machine you work on daily.

Your bottleneck isn't clocks. It's a 2018 8-core CPU. Overclocking won't move that enough to notice, and it trades stability you need for speed you won't feel.

Leave it.
