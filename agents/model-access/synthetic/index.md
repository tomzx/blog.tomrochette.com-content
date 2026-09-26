---
title: Synthetic
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, open-weight-models, llm-subscription, coding-agents]
readability: 3
audience_notes: >
  For developers running coding agents (OpenCode, Cline, Kilo, Roo) who want
  flat-cost access to open-weight models and care about prompt privacy.
---

Synthetic (synthetic.new) sells flat monthly subscriptions and pay-per-token billing for open-weight LLMs served on its own US and EU infrastructure, aimed squarely at coding-agent users.
Facts below verified as of 2026-09-26.

**It is the closest thing to Claude Pro for open-weight models: $30/month for 500 requests per 5 hours across models like DeepSeek-V4.1-Flash, GLM-5.3-Flash, and Kimi-K3, with prompts never stored longer than 14 days.**

## What it is

A privacy-focused inference provider that runs open-weight models itself rather than reselling closed APIs, with "always-on" models included in subscriptions and usage-based billing for enterprise and on-demand needs.
Any OpenAI-compatible tool works against api.synthetic.new/v1 (Anthropic-compatible /messages endpoints exist too), and OpenCode ships Synthetic as a native provider you select with /connect.

## Status

- Launched via Show HN on 2025-08-28 (31 points, 21 comments), with the founder answering questions in-thread.
- By September 2025 third parties described it as 19 always-on models for $20-60/month; as of 2026-09-26 the site markets a single $30/month pack plus usage-based billing.
- Distribution is real, with OpenCode, Kilo Code, Crush, Claude Code, GitHub Copilot, and OpenClaw all listed in its docs, and its marketing has also gotten visible enough to attract pushback, including one 2026 Reddit thread warning users away and another accusing its community of astroturfing.

## Strengths

- Flat cost with forgiving metering: requests are counted per API call, so a parallel tool-call batch is one request, per the founder on HN.
- Privacy is specific rather than vibes: API prompts and completions cannot be stored longer than 14 days and only for debugging, and Kilo's docs confirm no training on your data.
- syn: aliases (syn:large:text) auto-route to the latest recommended model, protecting you from pinning names that later 404.

## Cautions

- A 2026 r/opencodeCLI thread titled "Stay away from synthetic.new" reports the 3x-Claude-limits framing did not hold in practice, with limits hitting much sooner than expected, possibly from inefficient tool calling in the Chinese open models.
- One pack allows only 1 concurrent request per model; you must buy more packs to raise parallelism, which matters for multi-agent setups.
- Model rotation is a documented risk: their own docs warn that pinned model names will eventually 404.
- An r/kimi thread from mid-2026 accuses Synthetic community moderators of coordinated affiliate-link promotion; I cannot verify the accusation, so I treat surrounding hype with care.

## Pricing

- Subscription pack: $30/month ($1/day) for 500 requests per 5 hours, advertised as 3x the rate limits of Claude's $20/month plan, with 1 concurrent request per model and UI plus API access (as of 2026-09-26).
- Usage-based: pay-per-token on always-on models and pay-per-minute on-demand, pitched at enterprise.
- All always-on models plus embeddings are included in every subscription, and embeddings do not count against the rate limit.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2025-10-08 | Standard | $20/month, 135 messages per 5 hours | Wayback capture of synthetic.new/pricing |
| 2025-10-08 | Pro | $60/month, 1,350 messages per 5 hours | Wayback capture of synthetic.new/pricing |
| 2026-09-26 | Pack (x1) | $30/month ($1/day), 500 requests per 5 hours, 1 concurrent request per model; the exact date the $20/$60 tiers ended is not in my sources | synthetic.new/pricing |

## Compared to

- Requesty ([../requesty/index.md](../requesty/index.md)): a general gateway metered at 5% of spend; pick Synthetic when you want a fixed bill and open-weight models only.
- Claude Pro / Claude Code: 1.5x the price ($30 vs $20) for closed frontier models; pick Claude for peak quality, Synthetic for privacy and flat cost.
- Direct open-model hosts (DeepSeek, Z.ai): pay per token and often cheaper at low volume; Synthetic wins when agent request volume would blow past token budgets.

## Bottom line

Recommended for OpenCode or Kilo users who hit rate limits daily, want a predictable $30/month, and prefer prompts not retained beyond 14 days.
Not for anyone needing frontier closed models, guaranteed capacity, or high concurrency on a single pack.
My most contestable claim: the "3x Claude limits" line is the weakest reason to buy, because the most detailed public user report says real-world limits feel closer to Claude's than the marketing implies.

## Changes

- 2026-09-26 - Created.

## See also

- [Requesty](../requesty/index.md) - the percentage-markup gateway alternative in this same category.
- [OpenCode](../../harnesses/opencode/index.md) - the harness that ships Synthetic as a native provider.
- [Kilo Code](../../harnesses/kilo-code/index.md) - documents Synthetic as a first-class provider.

## References

- https://synthetic.new/pricing - current $30/month pack, 500 requests/5hr, 1 concurrent request per model, usage-based option (as of 2026-09-26; JS-rendered page, text extracted from fetched HTML)
- https://web.archive.org/web/20251008095830id_/https://synthetic.new/pricing - October 2025 pricing: Standard $20/135 messages per 5h, Pro $60/1,350
- https://hn.algolia.com/api/v1/items/45055763 - Show HN launch thread; founder on request counting, 14-day retention, and GLM-4.5 as flagship (2025-08-28)
- https://dev.synthetic.new/docs/api/models - current always-on model list, syn: aliases, model-rotation warning (as of 2026-09-26)
- https://dev.synthetic.new/docs/guides/opencode - native OpenCode provider setup
- https://kilo.ai/docs/ai-providers/synthetic - Kilo integration, no-training and 14-day auto-delete privacy claims
- https://www.reddit.com/r/opencodeCLI/comments/1rfdadw/stay_away_from_syntheticnew/ - critical user report on real-world limits; direct fetch returned 403, content recovered via search-result extraction
