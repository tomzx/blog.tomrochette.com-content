---
title: Claude plans
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, subscriptions, claude-code, anthropic]
readability: 3
audience_notes: >
  Engineers deciding which Claude subscription to buy for Claude Code.
  Assumes you know what a rate limit does to an agent loop and what per-token API pricing looks like.
---

Claude plans are Anthropic's consumer subscriptions, Free, Pro, and Max, and from Pro upward they are the only way to run Claude Code without paying per token.

**The subscription is a multiplier on an unpublished quota, not a token bucket: you are buying 1x, 5x, or 20x of a number Anthropic never publishes, drawn from one shared pool that chat, desktop, and Claude Code all drain together.**

## What it is

Three consumer tiers from Anthropic (PBC): Free at $0 with no Claude Code, Pro at $20 per month ($17 per month billed annually at $200 up front), and Max from $100 per month in 5x and 20x versions.
Pro carries Claude Code, Claude Science, Design, Slides, Docs, and Projects; Max adds priority access at high-traffic times, higher output limits, and early access.
Team seats run $25 per month ($20 annual) for Standard and $100 ($125 monthly, $100 annual) for Premium with 5x Standard usage; Enterprise is custom.

## Status

Active and the default way engineers pay for Claude Code, with the pricing page fetched and current as of 2026-09-26.
The 2026 record is lively: an April pricing-page test briefly removed Claude Code from Pro and was reverted within a day, a caching bug behind spring "usage drain" complaints was postmortemed on April 23 with limits reset, 5-hour limits were permanently doubled on May 6, and the weekly-limit promotion of May 13 was extended through August 19, 2026.
**The subscription has been repricing its value, not its price: the dollar figures are stable while the quota they buy keeps moving, which makes old guides the main hazard.**

## Strengths

- Flat pricing against metered fear: one widely cited power user pushed roughly 10 billion tokens through eight months, about $15,000 at Opus API rates, on a $200 Max subscription (secondary writeup, hold loosely).
- Usage credits continue a session past the plan limit at API rates under a cap you set, so a long task need not die at the wall.
- Max gets priority access at peak times, which is when Pro users feel throttling.
- The limits moved in your favor twice in spring 2026, permanently for the 5-hour clock.

## Cautions

- One shared pool: a morning of claude.ai chat shrinks the afternoon Claude Code session, and agent teams burn about 7x a normal session in plan mode, per Anthropic's own costs docs.
- Fable 5.1, the flagship, is capped at 50% of weekly limits on Max and is available on Pro only through usage credits, the first tightening of 2026 (July 20).
- Anthropic does not publish token quotas for any plan; multipliers are all you get, and third-party figures like "220,000 tokens per 5 hours" are estimates.
- The weekly-limit promotion lapsed on paper on August 19, 2026, so weekly walls may now arrive about a third sooner than spring habits suggest.
- A June 15 plan to move programmatic usage (Agent SDK, headless runs) to separate credit pools was paused the day it was due and never shipped; watch for it to return.

## Pricing

Free: $0, no Claude Code.
Pro: $20/month, $17/month billed annually ($200 up front), Claude Code included.
Max 5x: $100/month, 5x Pro usage.
Max 20x: $200/month, 20x Pro usage, monthly billing only.
Team Standard $25/seat/month ($20 annual), Team Premium $100/seat/month ($100 annual), Enterprise custom; usage credits extend any plan at API rates under a spending cap.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-26 | Pro / Max | Baseline: Pro $20/month ($17 annual), Max 5x $100/month, Max 20x $200/month, Fable on Pro via usage credits and on Max at 50% of weekly limits | https://claude.com/pricing |
| 2026-05-06 | Usage | 5-hour limits permanently doubled for Pro, Max, Team, and seat-based Enterprise; peak-hour throttling removed | https://ccforeveryone.com/guides/claude-code-limits-and-pricing |
| 2026-05-13 | Usage | Weekly limits raised 50% as a promotion, extended three times through 2026-08-19 | https://ccforeveryone.com/guides/claude-code-limits-and-pricing |
| 2026-07-20 | Fable | Fable 5.1 added to Max, Team Premium, and Enterprise up to 50% of weekly limits; Pro and Team Standard only via usage credits, the year's first tightening | https://ccforeveryone.com/guides/claude-code-limits-and-pricing |
| 2026-07-25 | Models | Opus 5 released on all paid plans at unchanged subscription prices, default on Max | https://ccforeveryone.com/guides/claude-code-limits-and-pricing |

## Compared to

- [GLM Coding Plan](../glm-coding-plan/index.md): the price-floor challenger at $18, with published credit mechanics and China-based routing; Claude plans cost more and publish less, and buy the stronger frontier model.
- [ChatGPT plans](../chatgpt-plans/index.md): the direct rival subscription, which publishes per-model message ranges and credit rates where Anthropic publishes multipliers only.
- API billing ([Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md)): still the right path for CI and automation, and the comparison that makes Max look cheap only works at genuinely heavy usage.

## Bottom line

Recommended for engineers whose daily driver is Claude Code and who can live with a shared pool and unpublished quotas; start at Pro and upgrade on the second real weekly cap.
Not for automation-heavy workloads, where the API or a flat open-model plan fits better.
My disagreeable claim: most Max subscribers are paying for a productivity feeling rather than a quota, because the median engineer never hits the Pro weekly wall that justifies 5x.

## Changes

- 2026-09-26 - Created when the owner asked why the Claude and OpenAI subscriptions were missing from this category.

## See also

- [Claude Code](../../harnesses/claude-code/index.md) - the harness these plans meter, with its own token-overhead numbers.
- [ChatGPT plans](../chatgpt-plans/index.md) - the rival subscription, more published mechanics at the same price points.
- [GLM Coding Plan](../glm-coding-plan/index.md) - the price-floor alternative for the same daily-driver role.
- [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md) - Anthropic's API-side bundle, where the subscription row meets per-token reality.

## References

- https://claude.com/pricing - plan prices, annual discount, Claude Code inclusion matrix, Fable access rules (fetched 200, 2026-09-26)
- https://ccforeveryone.com/guides/claude-code-limits-and-pricing - the 2026 change log (May 6 doubling, May 13 promotion, July 20 Fable tightening, paused Agent SDK split), limit mechanics, Team seat prices, the API-versus-subscription math (fetched 200, updated 2026-08-05)
- https://www.ssdnodes.com/blog/claude-code-pricing-in-2026-every-plan-explained-pro-max-api-teams/ - independent plan walkthrough, the instrumented-usage cost comparison it cites (fetched via search extraction, 2026-09-26)
- https://www.layer3labs.io/guides/claude-pro-vs-max-for-teams - the weekly-cap skepticism and the upgrade heuristics (fetched via search extraction, 2026-09-26)
- https://support.claude.com/en/articles/11049741-what-is-the-max-plan - the Max plan article: $100/$200 tiers, monthly-only billing, 5-hour and weekly limit mechanics, the discretionary-limits reservation (fetched 200, 2026-09-26)
