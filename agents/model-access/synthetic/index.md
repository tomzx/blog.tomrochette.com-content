---
title: Synthetic
created: 2026-09-26
updated: 2026-10-19
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, open-weight-models, llm-subscription, coding-agents]
readability: 3
audience_notes: >
  For developers running coding agents (OpenCode, Cline, Kilo, Roo) who want
  flat-cost access to open-weight models and care about prompt privacy.
---

Synthetic (synthetic.new) sells flat monthly subscriptions and pay-per-token billing for open-weight LLMs served on its own US and EU infrastructure, aimed squarely at coding-agent users.

**It is the closest thing to Claude Pro for open-weight models: Go $9, Standard $30, and Big $90 per month now buy weekly-regenerating credit quotas spent as tokens at discounted model rates (as of 2026-10-19), across models like DeepSeek-V4.1-Flash, GLM-5.3-Flash, and Kimi-K3, with prompts never stored longer than 14 days.**

## What it is

A privacy-focused inference provider that runs open-weight models itself rather than reselling closed APIs, with "always-on" models included in subscriptions and usage-based billing for enterprise and on-demand needs.
Any OpenAI-compatible tool works against api.synthetic.new/v1 (Anthropic-compatible /messages endpoints exist too), and OpenCode ships Synthetic as a native provider you select with /connect.

## Status

- Launched via Show HN on 2025-08-28 (31 points, 21 comments), with the founder answering questions in-thread.
- By September 2025 third parties described it as 19 always-on models for $20-60/month; through mid-October 2026 the site marketed a single $30/month pack at 500 requests per 5 hours.
- On 2026-10-19 the pricing page renders a three-tier lineup (Go $9, Standard $30, Big $90 per month) on weekly-regenerating credit quotas, replacing the per-5-hours request framing, and adds Fast and Infinite modes plus a Big-plan-only background path.
- Distribution is broad, with OpenCode, Kilo Code, Crush, Claude Code, GitHub Copilot, and OpenClaw all listed in its docs, and its marketing has also gotten visible enough to attract pushback, including one 2026 Reddit thread warning users away and another accusing its community of astroturfing.

## Strengths

- Flat cost with forgiving metering: requests are counted per API call, so a parallel tool-call batch is one request, per the founder on HN.
- Privacy is specific rather than vibes: API prompts and completions cannot be stored longer than 14 days and only for debugging, and Kilo's docs confirm no training on your data.
- syn: aliases (syn:large:text) auto-route to the latest recommended model, protecting you from pinning names that later 404.

## Cautions

- A 2026 r/opencodeCLI thread titled "Stay away from synthetic.new" reports the 3x-Claude-limits framing did not hold in practice, with limits hitting much sooner than expected; that evidence dates to the old per-5-hours pack, so I treat it as a warning about marketing generosity, not a measurement of the new credit system.
- Under the old pack the documented limit was 1 concurrent request per model, fixable only by buying more packs; the new page states no concurrency number, so parallelism on the new tiers is unverified.
- Model rotation is a documented risk: their own docs warn that pinned model names will eventually 404.
- An r/kimi thread from mid-2026 accuses Synthetic community moderators of coordinated affiliate-link promotion; I cannot verify the accusation, so I treat surrounding hype with care.

## Pricing

- Subscription tiers (as of 2026-10-19): Go $9/month, Standard $30/month, and Big $90/month, each carrying a weekly-regenerating credit quota spent as tokens at discounted model rates, with larger limits, higher priority, and more beta access at higher tiers.
- Each plan includes 1 usage reset per month, and extra tokens are always buyable at usage-based pricing.
- Fast mode: requests run up to 2x faster while each request consumes 2x of the rate limit.
- Infinite mode (Big plan, beta): built for background agents, requests never count against the rate limit but run much slower, currently DeepSeek V4.1 Flash only.
- Usage-based pay-per-token on always-on models remains available outside or on top of subscriptions, per the dev docs.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2025-10-08 | Standard | $20/month, 135 messages per 5 hours | Wayback capture of synthetic.new/pricing |
| 2025-10-08 | Pro | $60/month, 1,350 messages per 5 hours | Wayback capture of synthetic.new/pricing |
| 2026-09-26 | Pack (x1) | $30/month ($1/day), 500 requests per 5 hours, 1 concurrent request per model; the exact date the $20/$60 tiers ended is not in my sources | synthetic.new/pricing |
| 2026-10-19 | Subscriptions | The single $30 pack became a three-tier lineup, Go $9, Standard $30, Big $90 per month, on weekly-regenerating credit quotas at discounted model rates, with Fast mode, a Big-only Infinite mode, and 1 usage reset per month; the per-5-hours request framing is gone | synthetic.new/pricing |

## Compared to

- [Requesty](../requesty/index.md): a general gateway metered at 5% of spend; pick Synthetic when you want a fixed bill and open-weight models only.
- Claude Pro / Claude Code: 1.5x the price ($30 vs $20) for closed frontier models; pick Claude for peak quality, Synthetic for privacy and flat cost.
- Direct open-model hosts (DeepSeek, Z.ai): pay per token and often cheaper at low volume; Synthetic wins when agent request volume would blow past token budgets.

## Bottom line

Recommended for OpenCode or Kilo users who hit rate limits daily, want a predictable $30/month on the Standard tier, and prefer prompts not retained beyond 14 days.
Not for anyone needing frontier closed models, guaranteed capacity, or verified high concurrency on the entry tiers.
My most contestable claim: the "3x Claude limits" line is the weakest reason to buy, because the most detailed public user report says practical limits feel closer to Claude's than the marketing implies.

## Changes

- 2026-09-26 - Created.
- 2026-10-06 - Repaired the Compared-to Requesty link, which was double-wrapped and rendered its file path as the link text; pricing page re-verified unchanged.
- 2026-10-19 - Pricing overhaul recorded: the single $30 pack (500 requests per 5 hours, 3x-Claude framing) became a Go $9 / Standard $30 / Big $90 lineup on weekly-regenerating credit quotas with Fast and Infinite modes, and the pricing page fetched with content for the first time since 2026-10-06; headline, Status, Cautions, Pricing, and price history moved with it.

## See also

- [Requesty](../requesty/index.md) - the percentage-markup gateway alternative in this same category.
- [OpenCode](../../harnesses/opencode/index.md) - the harness that ships Synthetic as a native provider.
- [Kilo Code](../../harnesses/kilo-code/index.md) - documents Synthetic as a first-class provider.

## References

- https://synthetic.new/pricing - the 2026-10-19 lineup: Go $9, Standard $30, Big $90 per month, weekly-regenerating credit quotas at discounted model rates, Fast and Infinite modes, 1 usage reset per month (fetched 200 with full text on 2026-10-19; the JS-rendered page had fetched empty on 2026-10-11, 2026-10-12, and 2026-10-14, so the previous $30-pack figures stood dated 2026-10-06)
- https://web.archive.org/web/20251008095830id_/https://synthetic.new/pricing - October 2025 pricing: Standard $20/135 messages per 5h, Pro $60/1,350
- https://hn.algolia.com/api/v1/items/45055763 - Show HN launch thread; founder on request counting, 14-day retention, and GLM-4.5 as flagship (2025-08-28)
- https://dev.synthetic.new/docs/api/models - current always-on model list, syn: aliases, model-rotation warning (as of 2026-09-26; re-fetched 2026-10-19 with GLM-5.3-Flash, DeepSeek-V4.1-Flash, and Kimi-K3 still listed and the syn: alias recommendation unchanged)
- https://dev.synthetic.new/docs/guides/opencode - native OpenCode provider setup
- https://kilo.ai/docs/ai-providers/synthetic - Kilo integration, no-training and 14-day auto-delete privacy claims
- https://www.reddit.com/r/opencodeCLI/comments/1rfdadw/stay_away_from_syntheticnew/ - critical user report on practical limits; direct fetch returned 403, content recovered via search-result extraction
