# MT5 take profit line display issue

| | |
|---|---|
| Date | 2026-02-02 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-632` |
| Links | [Original](https://claude.ai/chat/f88afbd4-1fb2-4dd7-ba7d-24ed82358c67) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/632-2026-02-02-mt5-take-profit-line-display-issue.html) |

**Summary:** Troubleshooting MetaTrader 5 not showing take-profit lines despite Show trade levels being enabled; suspects line color matching background.

**Topics:** Trading and markets > Brokers, accounts and platforms

**Index terms:** MetaTrader 5; take profit; trade levels; chart properties

[← Catalog home](../README.md)

---

### Millard · 2026-02-02 02:32

how do I get MT5 to show my take profit line on the chart. It used to, but I can't get it back.

### Claude · 2026-02-02 02:32

Sunday, February 01, 2026, 12:00 PM CST

In MT5, take profit lines visibility is controlled by:

**Chart Settings:**

1. Right-click on the chart → **Properties** (or press F8)
2. Go to the **Show** tab
3. Enable **"Show trade levels"**

**Alternative method:**

* Menu: **Charts** → **Properties** → **Show** tab → check **"Show trade levels"**

This displays entry price, stop loss, and take profit lines for open positions and pending orders.

If that setting is already enabled and lines still don't appear, verify you have an open position or pending order with a TP actually set on that symbol's chart.

### Millard · 2026-02-02 02:33

I did exactly that.

[File attached: 1769999603581\_image.png — contents not included in export]

### Claude · 2026-02-02 02:33

"Show trade levels" is enabled, so that's not the issue.

Clarifying questions:

1. Do you have an **open position** on USDJPY.a specifically (not just a pending order)?
2. Does the position actually have a TP value set? (Check in the **Toolbox** → **Trade** tab — the TP column should show a price, not 0.00000)
3. Is the TP price **within the visible chart range**, or is it far above/below current price? The line won't render if it's outside the viewable area.
4. Do you see the **entry price line** and/or **SL line** for the position, just not the TP?

### Millard · 2026-02-02 02:34

1. yes
2. yes
3. yes
4. neither, no SL set

### Claude · 2026-02-02 02:34

Since "Show trade levels" is on but neither entry nor TP lines are visible:

**Most likely cause — line color matches background:**

1. In the same Properties dialog, go to the **Colors** tab
2. Look for **"Trade levels"** color setting
3. If it's set to the same color as your chart background (appears to be dark/black), the lines are rendering but invisible
4. Change it to a visible color (e.g., white, yellow, lime)

If that's not it, try forcing a chart refresh by switching timeframe and switching back.
