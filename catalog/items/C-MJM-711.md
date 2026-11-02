# cTrader ECN routing and deal desk bypass

| | |
|---|---|
| Date | 2026-07-17 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-711` |
| Links | [Original](https://claude.ai/chat/5b788bba-0ea5-4984-a527-b924966ea05b) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/711-2026-07-17-ctrader-ecn-routing-and-deal-desk-bypass.html) |

**Summary:** cTrader does not itself route orders to ECNs; execution model and dealing-desk bypass depend on the broker's backend.

**Topics:** Trading and markets > cTrader migration and features; Trading and markets > Brokers, accounts and platforms

**Index terms:** cTrader; Spotware; ECN; dealing desk; B-book; STP execution

[← Catalog home](../README.md)

---

### Millard · 2026-07-17 13:05

I was told by an AI that cTrader routes trades directly to ECNs, bypassing the broker's deal desk.

### Claude · 2026-07-17 13:06

The claim is false as stated. cTrader is a trading platform (developed by Spotware), not an execution model. It does not itself route orders anywhere — the broker configures where orders go (own liquidity bridge, ECN/STP aggregation, or their own dealing desk/B-book). Whether a given cTrader broker uses "no dealing desk" execution depends entirely on that broker's backend setup, not on the platform.

Evidence against the claim:

* Brokers can and do run cTrader as a dealing-desk (market-maker) operation while marketing "ECN-style" execution — the platform doesn't prevent this.
* "ECN routing" claims for retail brokers (any platform: MT4/MT5/cTrader) are broker-disclosed, not independently verifiable by the trader unless the broker publishes LP names and provides raw tick/depth data matching those LPs.
* cTrader does offer Depth of Market (DOM) and is popular with brokers claiming NDD/ECN models, which is likely the source of the conflation — but popularity with that broker segment ≠ platform-enforced routing.

To verify for a specific broker: check if they disclose named liquidity providers, provide a Level II DOM feed, and whether their terms/regulatory disclosures state STP/NDD execution vs. market making. Platform choice alone tells you nothing.
