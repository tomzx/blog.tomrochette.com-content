---
title: OpenRouter Rankings
created: 2026-09-24
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, trackers-and-leaderboards, usage, market-share, open-data]
readability: 3
audience_notes: >
  Engineers who want to know what models developers actually spend tokens on, and how far a gateway's numbers can be trusted as market share.
  Assumes you know what an LLM gateway is.
---

OpenRouter Rankings ranks models by the tokens actually processed through the OpenRouter gateway, published with CC BY 4.0 licensing, a public Data API, and views by task, cost per session, market share, and app, and it is the only ranking in its category built on revealed spend rather than votes or benchmarks.

**Every other leaderboard in this category measures opinion; this one measures invoices.**

## What it is

A rankings surface inside openrouter.ai, the LLM gateway founded in early 2023 that claims 500T+ monthly tokens, 10M+ users, 80+ providers, and 500+ models.
The page states plainly what it does not measure: "They do not rank models by accuracy, reasoning ability, or benchmark performance", and it excludes private requests while bucketing usage into daily UTC aggregates per model variant.
Views include top models (today, week, month), top models by task share of spend, cost per session for coding agents, market share by model author, fastest models, and top apps (Hermes Agent, Claude Code, Kilo Code, and Cline led in tokens as of 2026-09-24).
Data access is unusually open: rankings are CC BY 4.0 with a required citation format, and the Data API serves `rankings-daily` (top 50 public models per day, history back to 2025-01-01, 30 requests/minute, live-updating) to any inference key.

## Status

Fresh and commercially central: the page showed "Usage data through Sep 23, 2026" on the day of verification, a one-day lag, and updates flow live as traffic arrives.
The underlying gateway is a top-of-category business: $113M Series B led by CapitalG in May 2026 at a reported $1.3B valuation, then an announced acquisition by Stripe on August 19, 2026 at a reported price above $7B, with the company claiming 10T+ tokens per day.
Its numbers are routinely quoted as market signal in press and on HN, and OpenRouter itself turned the dataset into research (a 100T-token empirical study that drew 207 points on HN).

## Strengths

- Revealed preference: tokens and spend through a paid gateway are harder to game with a demo day prompt than a vote or a benchmark run.
- Openness is a policy, not a favor: CC BY 4.0, a documented citation format, and a free JSON API with a year-plus of history.
- The by-task and cost-per-session views answer questions (what does a coding-agent session actually cost) that no benchmark board even frames.

## Cautions

- The sample is one gateway, and the page says so: "They do not include usage on a model provider's own API or across the whole market", and "token volume is not a count of requests, users, or spend" since verbosity and tokenization differ.
- Free-tier promotions distort the ranks: Max Woolf's analysis of the Tencent Hy3 model topping the leaderboard documents a free period on a single provider driving the rank, and the Kilo Code free-Grok episode did the same in 2025.
- Independence is now a clock: the rankings belong to a gateway being absorbed by Stripe, so treat "market share" as "OpenRouter's customers' share" and re-verify who publishes the numbers after the deal closes.
- Figures restate as snapshots refresh, so any number you cite needs its as-of date recorded alongside it.

## Pricing

Free to view and to query, CC BY 4.0 licensed with attribution.
OpenRouter monetizes the gateway (inference and enterprise controls), not the rankings.
No reader-facing price is stated, so no price history applies.

## Compared to

- [Artificial Analysis](../artificial-analysis/index.md): constructed measurement of quality, price, and speed; the rankings measure adoption, and the two disagree for good reasons.
- [LMArena](../lmarena/index.md): stated preference versus revealed preference.
- [LLM Stats](../llm-stats/index.md): benchmark aggregates with an agent-facing API; the rankings' API is the usage-side mirror.

## Bottom line

**Recommended for answering "what are developers actually paying for this week" with numbers you can legally republish, not for any claim about which model is more capable.**
My disagreeable claim: this is the most misused ranking in the category, cited as market truth from a sample that excludes every provider's first-party API traffic, and the Stripe acquisition makes reading its provenance, not its numbers, the skill that matters going forward.

## Changes

- 2026-09-24 - Created.
- 2026-09-26 - Linked the OpenRouter gateway profile in the new Model access category, where the fee structure and the Stripe acquisition are tracked.

## See also

- [OpenRouter](../../model-access/openrouter/index.md) - the gateway itself: fee structure, tiers, and the Stripe acquisition behind these rankings
- [Artificial Analysis](../artificial-analysis/index.md) - the quality-side measurement these usage numbers need as a counterweight
- [LMArena](../lmarena/index.md) - votes versus invoices as two theories of preference
- [AI Release Tracker](../ai-release-tracker/index.md) - the release stream that explains rank jumps the usage data cannot
- [Trackers and Leaderboards Feature Matrix](../trackers-and-leaderboards-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the cost-per-task thinking the session-cost view extends

## References

- https://openrouter.ai/rankings - methodology, caveats, windows, top apps, CC BY 4.0 note, data-through date (fetched 200, 2026-09-24)
- https://openrouter.ai/docs/cookbook/administration/data-api - Data API endpoints, limits, citation format, dataset history from 2025-01-01 (fetched 200, 2026-09-24)
- https://openrouter.ai/about - company scale claims and founding date (fetched 200, 2026-09-24)
- https://openrouter.ai/blog/announcements/series-b/ - $113M Series B and investors, May 2026 (fetched 200, 2026-09-24)
- https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/ - the Stripe acquisition announcement, August 2026 (fetched 200, 2026-09-24)
- https://techcrunch.com/2026/08/16/stripe-will-reportedly-acquire-ai-gateway-startup-openrouter-for-7b/ - the reported price and valuation (fetched 200, 2026-09-24)
- https://minimaxir.com/2026/05/openrouter-hy3/ - the free-tier distortion analysis behind the Hy3 rank (fetched 200, 2026-09-24)
- https://news.ycombinator.com/item?id=48317294 - the HN thread questioning free-driven ranks (fetched 200, 2026-09-24)
- https://news.ycombinator.com/item?id=48330499 - the "market signal" counterpoint (fetched 200, 2026-09-24)
- https://news.ycombinator.com/item?id=46154022 - the 100T-token study showing the dataset's research use (fetched 200, 2026-09-24)
