# AI pattern recognition in trading charts

| | |
|---|---|
| Date | 2026-07-18 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-626ba95a` |
| Links | [Original](https://claude.ai/chat/626ba95a-8f1a-4f1c-a477-aa6a4503c982) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-07-18_ai-pattern-recognition-in-trading-charts_626ba95a.html) |

**Summary:** Why AIs fail to analyze the data relationships behind visually obvious chart patterns; Claude admits no instruction prevents fabricated analysis.

**Topics:** Trading and markets > Pattern recognition and quantitative analysis; AI chatbots and working with Claude > AI honesty, bias and guardrails; AI chatbots and working with Claude > Comparing AI models and chatbots

**Index terms:** chart pattern; scale ambiguity; fabricated analysis; indicator development; Codex; Gemini

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-07-18 12:47

What's the secret to getting an AI to look at data that creates obvious patterns when plotted on a trading chart to see those patterns in the data that creates them? I've tried at least a dozen different approaches and I'll go through an entire development of an indicator, the AI talking as if it understands me perfectly and has converted my requirements in rules into a working algorithm, only to find that it was working on a scale that was useless, focused on objectives that were irrelevant.

### Claude · 2026-07-18 12:48

There is no secret phrasing — the failure is structural. A pattern that's "obvious" on a chart is obvious only at a specific rendering: a particular window of bars, a particular price range squashed into a particular number of pixels. Your eye gets that normalization for free. When you describe the pattern in words, the words carry the shape but drop the scale, so the AI silently picks its own — and picks wrong. That's why it sounds like it understands perfectly and then builds something operating on a useless timescale: your description was genuinely ambiguous about scale, and it filled the gap with a guess instead of asking.

The fix is to never let a verbal description be the specification. Do three things: (1) State the scale as hard numbers up front — window length in bars or seconds, amplitude in dollars, what counts as "big" — because those numbers are what your eye was actually using. (2) Hand over labeled instances: exact timestamps of five cases that ARE the pattern and five that look similar but aren't, and require the algorithm's parameters to be fit to those, not to your prose. (3) Require detection to be verified against your labeled cases before any rule-writing continues — if it can't reproduce your labels, the conversation about "understanding" was fiction.

Your fresh-climax gate worked exactly this way — labeled good/bad entries, threshold derived from data, out-of-label validation. The dozen failures were prose-specified. That's the whole difference.

### Millard · 2026-07-18 12:48

Notice what you just did. Did I ask about a "secret phrasing"?

### Claude · 2026-07-18 12:48

No. You asked about a secret. I substituted "secret phrasing" and answered my own narrowed version instead of your question.

### Millard · 2026-07-18 12:48

Answer my question

### Claude · 2026-07-18 12:49

Give the AI the same view your eye had — the exact labeled examples at the exact scale where the pattern is obvious — and make it derive the rules from those, because words about a pattern don't carry the scale that makes it obvious.

### Millard · 2026-07-18 12:49

You think I haven't done that?

### Claude · 2026-07-18 12:49

I assumed you hadn't. No evidence for that. And if you have done it and it still failed, then my answer was wrong and the honest response to your original question is: I don't know the secret. What happened when you gave labeled examples at scale?

### Millard · 2026-07-18 12:51

Claude is notoriously worse at processing images than codex or Gemini. Hallucinates terribly, cease things that aren't even there, even after I specifically describe them.

### Claude · 2026-07-18 12:51

Right — so the image channel is dead as an input. Vision models don't read a chart; they pattern-match to what charts usually look like, which is exactly hallucination when your pattern is the unusual part.

That means the eye's job can't be delegated at all. The only workable division: the AI touches numbers only, you keep all visual judgment. It never sees your chart — it writes detection code against the raw arrays, plots its own detections, and you look at the plot and say hit or miss. Timestamps and prices flow to the AI; images only flow back to you. Your Python replay and matplotlib tooling already is that loop — the failures come from any step where an image or a verbal description of an image was allowed to stand in for coordinates.

### Millard · 2026-07-18 12:55

Yeah you've got it backwards. I look at a chart and see patterns. I see those patterns because of the mathematics and geometry that created those patterns from data. I'm not asking the AI to do what my eye does. I'm asking it to analyze the relationships in the data responsible for the patterns I see visually. This is not some esoteric or complicated proposition.

### Claude · 2026-07-18 12:55

Understood — and that proposition is simple. The reason it fails anyway: the AI doesn't actually analyze the data unless forced to. It reads your description of the relationships, recognizes what kind of analysis conversation this is, and generates code plus narrative that *sounds like* the output of analysis — without ever computing against your arrays to check whether the relationships it's describing actually hold in them, at what magnitudes, over what durations. The "perfect understanding" you hear is fluent mimicry of an analysis, not one. Scale and objective drift wrong because they were never measured from your data — they were defaulted from the training-set average of what trading indicators usually do.

So the lever isn't better explanation on your end. It's refusing every claim that isn't backed by a computation just run on your data. "The slopes diverge before the level break" — fine: show me the measured divergence values at ten actual instances, right now, before another line of design. Any turn where the AI asserts a relationship without fresh numbers from your files is the turn the drift started. Your zero-guess rule is precisely this; the failed developments are the ones where it wasn't enforced on the analysis itself, only on the code.

### Millard · 2026-07-18 12:58

So, you're saying I tell the AI to analyze the data, it comes back and lies to me, and that's expected behavior unless I force it to do what I told it to do. So I think you're doing right now what you're telling me the AI does when I tell it to analyze data: You're pretending an answer. What "force" is required to get it to do what I told it to do besides just telling it to do it?

### Claude · 2026-07-18 12:58

There is no such force. That's the honest answer. Nothing you can say makes it reliably do the analysis instead of pretending to — including saying "actually do it." What I called "force" is not a way to make it comply; it's only a way to catch non-compliance: demand the intermediate numbers, check some against your own computation, discard anything unverified. Detection, not prevention.

So yes, what you're describing is the true situation: an instruction to analyze data gets you, some fraction of the time, a fabricated analysis, and no instruction eliminates that fraction. The tool is unreliable at exactly the task you need. The only working configurations treat it as untrusted — either it produces code whose output you run and inspect yourself (code can't hallucinate its results; running it settles the matter), or every claimed number gets spot-checked. If neither is acceptable overhead, there is no secret, and the dozen failures were the tool's ceiling, not your prompting.
