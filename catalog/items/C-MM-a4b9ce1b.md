# PDF conversion request

| | |
|---|---|
| Date | 2026-10-29 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-a4b9ce1b` |
| Links | [Original](https://claude.ai/chat/a4b9ce1b-1387-47d6-860d-4ba6a7330539) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-10-29_pdf-conversion-request_a4b9ce1b.html) |

**Summary:** Converting a past perfect worksheet to PDF, then setting a 5-pip MT5-style trailing stop on cTrader and planning a cBot.

**Topics:** Trading and markets > cTrader migration and features; Trading and markets > Forex and gold trading concepts; ESL teaching > Grammar worksheets and exercises

**Index terms:** cTrader; trailing stop; MetaTrader 5; cBot; XAUUSD; past perfect

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-10-29 16:11

convert this to a pdf

### Claude · 2026-10-29 16:11

Thursday, October 29, 2026, 10:11 AM CST

Here's past\_perfect\_worksheet.pdf, three pages.

### Millard · 2026-10-29 17:12

on ctrader, how do i do a trailing stop of 5 pips so that after my trad appreciate to 5 pips it follows it form there like it does in mt5?

### Claude · 2026-10-29 17:12

cTrader's built-in trailing stop has no "start after X profit" setting — it trails at the size of your regular stop loss from the moment you set it — so for MT5-style behavior you need a cBot like EarnForex's free [Trailing Stop on Profit](https://www.earnforex.com/metatrader-expert-advisors/Trailing-Stop-on-Profit/), where the stop-loss follows the price gradually but only once a certain level of profit is attained. Check your broker's gold pip size in cTrader's symbol info first, since on many cTrader feeds 5 pips on XAUUSD is only a $0.05 move.

### Millard · 2026-10-29 17:21

so if i put it at 5 pips it will trail at 5 pips?

### Claude · 2026-10-29 17:21

Yes — the stop stays 5 pips behind the best price, but it starts trailing immediately from entry (stop begins at −5 pips), not after you're 5 pips in profit like MT5.

### Millard · 2026-10-29 17:22

can you write me a script to get it to do it like mt5?

### Claude · 2026-10-29 17:22

Plan: a cTrader cBot you attach to an XAUUSD chart that, for every open XAUUSD position, does nothing until the trade is 5 pips in profit, then moves the stop to 5 pips behind price and only ever ratchets it in your favor — both inputs adjustable, cTrader must stay open for it to work. Say GO, or tell me if it should cover all symbols instead of just the chart's symbol.
