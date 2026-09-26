---
title: OpenRouter
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, llm-gateway, pay-per-token]
readability: 3
audience_notes: >
  For engineers deciding whether to route model traffic through a gateway.
  Assumes you know per-token pricing and what an API aggregator does.
---

OpenRouter is the largest multi-provider LLM gateway, one API key and one prepaid credit balance across hundreds of models from dozens of providers, with automatic routing and fallback.
Facts below verified as of 2026-09-26.

## What it is

A marketplace gateway founded in early 2023 by Alex Atallah (OpenSea co-founder).
Provider token prices pass through unchanged; you fund prepaid credits and OpenRouter takes a fee on the purchase, not on inference.
Routing variants (:nitro for speed, :floor for price, :exacto for tool-calling quality, :free and :batch) change how requests are placed, and BYOK keeps your own provider keys behind OpenRouter's routing, analytics, and fallbacks.

## Status

**The scale is venture-grade: $113M Series B led by Alphabet's CapitalG at about $1.3B post-money in May 2026, with 8M users and roughly 100 trillion tokens per month.**
Annualized inference spend through the platform grew from $10M (October 2024) to over $100M (May 2025), per a tracked pricing blueprint.
On 2026-08-19 OpenRouter announced it is joining Stripe, with closing expected within weeks of the announcement; the post commits to the same product, name, roadmap, and provider-neutral routing, and states the platform now processes 10+ trillion tokens per day across 400+ models for more than 10 million developers.
The pricing page was rebuilt on 2026-09-20 into four tiers (Free, Standard, Business, Enterprise), and the pricing page itself renders client-side, so my fetch returned navigation only.

## Strengths

- Passthrough pricing is real: verified spot checks (Claude Opus 5 at $5/$25) match provider list prices.
- One key, one balance, automatic provider fallback, per-model price/latency comparison, and a fee structure published in full.
- Free tier is a genuine on-ramp: 25+ free models, 1,000 requests/day after a one-time $10 credit purchase.
- BYOK is free through $25,000/month of list-price inference, which covers most teams entirely.
- The Business tier makes EU-only or US-only routing self-serve instead of an Enterprise contract.

## Cautions

- **The 5.5% credit fee with a $0.80 minimum punishes small top-ups: a $5 purchase costs 16% in fees.**
- BYOK's free allowance is metered at OpenRouter list price, not your negotiated rate, so discounts do not slow the meter.
- Paid-tier rate limits are passthrough from providers, and 429s arrive without queueing or backoff; your client owns retries.
- No public SLA below Enterprise.
- Routing can silently move you to a different provider, and a provider price change flows straight to your bill.
- Credits may expire after one year per the terms.

## Pricing

Free: $0, 25+ free models, 20 requests/minute, 50 requests/day (1,000/day with $10 lifetime credits), workspace limit 5.
Standard: 5.5% fee per credit purchase, $0.80 minimum, crypto 5.0% flat, no subscription, workspace limit 5.
Business: 8% fee, inference locked to EU or US providers with no cross-region fallback, workspace limit 1,000 (launched 2026-09-07).
Enterprise: custom, volume commitments, SSO/SAML, contractual SLAs, $200,000/month free BYOK allowance.
BYOK: 5% of equivalent cost above the free allowance, as of 2026-09-26.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2023-05 | Launch | Baseline: passthrough tokens, prepaid credits, purchase fee | https://www.usagepricing.com/blueprint/openrouter |
| 2025-06-09 | Credit fee | Flattened to 5.5% with $0.80 minimum; crypto to 5.0% flat | https://www.usagepricing.com/blueprint/openrouter |
| 2026-07-14 | BYOK | Free allowance re-based from 1M/5M requests to $25,000/$200,000 of list-price inference | https://www.usagepricing.com/blueprint/openrouter |
| 2026-09-07 | Business | New self-serve tier at 8% fee for EU/US-only routing | https://www.usagepricing.com/blueprint/openrouter |
| 2026-09-20 | Table | Pay-as-you-go renamed Standard; workspace limits published (5/5/1000/Custom) | https://www.usagepricing.com/blueprint/openrouter |

## Compared to

OpenCode Go (../opencode-go/index.md) is a $10 subscription for open coding models with hard caps; choose OpenRouter when your usage is spiky or you need frontier models.
OpenCode Zen (../opencode-zen/index.md) is the curated coding gateway, usually pricier per token on open models; choose Zen when benchmarked endpoints and free stealth models matter more than unit cost.
Direct provider accounts are cheapest for one dominant model at scale, at the cost of N billing relationships and no cross-provider fallback.

## Bottom line

Recommended for multi-model teams and tinkerers who value breadth, fallback, and one bill.
Not for single-provider, high-volume workloads with negotiated rates, where the fee is pure overhead.
My disagreeable claim: I would pay the 5.5% rather than run the same multi-provider setup myself, because the fee buys uptime pooling, not just convenience.

## Changes

- 2026-09-26 - Created.

## See also

- [OpenCode Go](../opencode-go/index.md) - the flat-fee subscription alternative for open coding models.
- [OpenCode Zen](../opencode-zen/index.md) - the curated gateway that community benchmarks price against this one.
- [OpenRouter rankings](../../trackers-and-leaderboards/openrouter-rankings/index.md) - its sibling usage rankings page, tracked separately.
- [Model provider feature matrix](../../model-provider-feature-matrix/index.md) - gateway features compared across providers.
- [Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - choosing models once access is settled.

## References

- https://openrouter.ai/docs/faq - official fee statement (5.5%, $0.80 minimum, crypto 5%), BYOK dollar thresholds, no-markup position, free-tier limits (200).
- https://openrouter.ai/pricing - tier names and fee rows (200, JS-rendered shell; content corroborated via the sources below).
- https://www.usagepricing.com/blueprint/openrouter - funding history, tier timeline, workspace limits, dated pricing changes (200, facts checked 2026-09-24).
- https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/ - the joining-Stripe announcement, 2026-08-19: continuity commitments, 10+ trillion tokens per day, 400+ models, 10M+ developers (fetched 200, 2026-09-26).
- https://ofox.ai/blog/openrouter-pricing-hidden-markup-breakdown-2026/ - independent fee-stack verification, $0.80-minimum math, BYOK metering change (200).
- https://www.truefoundry.com/blog/openrouter-pricing - critical framing: fee at scale, BYOK, missing SLA (200, published 2026-08-25).
- https://costgoat.com/pricing/openrouter/ - per-model price snapshots used for cross-gateway comparison (200, as of 2026-09-25).
