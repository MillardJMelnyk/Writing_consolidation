# Understanding the stochastic indicator

| | |
|---|---|
| Date | 2026-07-18 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-e109b2a4` |
| Links | [Original](https://claude.ai/chat/e109b2a4-d931-40b5-a2b7-5413d3f2deff) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-07-18_understanding-the-stochastic-indicator_e109b2a4.html) |

**Summary:** Plain explanation of what the stochastic oscillator measures and its K period, slowing and D period calculation steps.

**Topics:** Trading and markets > Forex and gold trading concepts

**Index terms:** stochastic oscillator; %K; %D; slowing; price range

[← Catalog home](../README.md)

---

### Millard · 2026-07-18 13:04

Explain simply and without the use of formulaic syntax exactly what the stochastic indicator measures.

### Claude · 2026-07-18 13:04

It measures where the current price sits inside the recent high-to-low range. If price is at the very top of the range covered over the last N bars, the reading is near 100; at the very bottom, near 0. So it's telling you how close price is closing to the recent extremes — nothing more.

### Millard · 2026-07-18 13:06

Do a step-by-step of the calculation, again without symbolic notation

### Claude · 2026-07-18 13:06

1. Pick a lookback window, say the last 14 bars.
2. Find the highest high in that window.
3. Find the lowest low in that window.
4. Take the current close and measure how far it sits above that lowest low.
5. Measure the total distance from the lowest low to the highest high.
6. Divide the first distance by the second and express it as a percentage. That's the raw stochastic (%K): 0 means closing at the window's low, 100 means closing at its high.
7. Smooth that raw line by averaging its last few values (usually 3). That average is the signal line (%D).

### Millard · 2026-07-18 13:07

That implies two inputs. The typical stochastic indicator supplied with trading platforms ask for three: k, d, and smoothing.

### Claude · 2026-07-18 13:08

Correct — the third one is an extra smoothing stage in between. The full chain:

1. K period (e.g. 14): the lookback window for the raw calculation I described.
2. Slowing (e.g. 3): the raw line gets averaged over this many bars first. This turns the "fast" stochastic into the "slow" one — with slowing set to 1 you get the fast version. What's plotted as %K is this smoothed line, not the raw one.
3. D period (e.g. 3): the signal line, an average of the already-slowed %K.

So it's raw calculation → smoothed once (slowing) → smoothed again (%D).
