---
title: NanoGPT
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, model-gateway, open-weights, privacy]
readability: 3
audience_notes: >
  For engineers choosing between model gateways and first-party lab subscriptions.
  Assumes familiarity with pay-as-you-go token pricing and the open-weight model ecosystem.
---

NanoGPT (nano-gpt.com) is an independent model-access gateway combining pay-per-token API access at list prices with a flat subscription that bundles open-weight model usage at no per-token cost.
**At $12 per month it is the cheapest flat-rate open-weight tier I can verify anywhere, but the deal quietly shrank over the past year.**
Facts below verified as of 2026-09-26.

## What it is

The service runs a hosted web chat and an OpenAI-compatible API at provider list prices with no markup, taking deposits from $0.10 in crypto or $1 by card.
The Pro subscription includes open-weight text and image models, currently framed as 60 million input tokens per week plus a 5% discount on eligible paid text models.
Coverage spans text, image, video, 3D, audio, and embedding models under one balance.
An independent operator runs it, and the pages I fetched name no corporate parent.

## Status

Active: the blog published within the week of verification (September 22, 2026), ships monthly crypto-payment statistics, and added zero-data-retention routing on September 3, 2026.
The Wayback Machine holds 57 captures from September 2024 through September 2026, so the service has operated continuously for at least two years.
Its own Hacker News footprint is nearly nil: two stories in late 2024 with zero comments, while the NanoGPT name on HN belongs to Karpathy's training repo (a 1,532-point story).

## Strengths

- List-price API with the exact cost printed on every request makes it a rare auditable gateway.
- The subscription undercuts every first-party lab plan while covering text and image generation.
- The privacy posture is concrete: crypto payments (Monero led deposits at 38.55% in August 2026), no-prompt-logging claims, and ZDR routing.

## Cautions

- The deal narrowed: September 2025 sold unlimited personal open-weight use at $8, September 2026 sells 60M input tokens per week at $12, a 50% rise with a new cap.
- Bring-your-own-key requests are billed at 5% of normal model cost, and pinning a specific provider adds another 5%.
- Governance is opaque: no funding, ownership, or company facts appear on fetched pages, so nobody is accountable if terms move again.
- Scrutiny lives in Discord and niche communities rather than HN, so fewer independent eyes check the claims.

## Pricing

Pro is $12/month as of 2026-09-26, including 60M input tokens per week, the 5% paid-text-model discount, and web plus API access.
Pay-as-you-go needs no subscription: a free tier with one web-only model, list-price API billing, and $0.10 crypto or $1 card deposit minimums.
In September 2025, Pro was $8/month with unlimited personal open-weight usage capped at 60,000 generations per month and 2,000 per day.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2025-09-01 | Pro | $8/month, unlimited personal open-weight usage (60,000 generations/month, 2,000/day) | http://web.archive.org/web/20250901063827/https://nano-gpt.com/subscription |
| 2026-09-26 | Pro | $12/month, 60M included input tokens per week, 5% paid-text-model discount | https://nano-gpt.com/pricing |

## Compared to

Kimi Code (../kimi-code/index.md) is the pick when you want one lab's frontier open-weight models with quota predictability at a similar monthly price.
MiniMax Coding Plan (../minimax-coding-plan/index.md) covers multimodal token volume cheaply but locks you out in 5-hour windows, which NanoGPT never does.
The free PAYG path also makes NanoGPT the lowest-commitment way to test a model before any subscription.

## Bottom line

Recommended for privacy-minded tinkerers and open-weight power users who want flat-cost breadth without quota-window lockouts.
Not for engineers whose work needs closed frontier models at subscription quotas, since the $12 tier's value lives almost entirely in open weights.
I will claim something arguable: at $12 with open weights included, this beats any $15-$20 first-party plan on value, because open-weight quality has closed enough of the gap that the labs' premium is now a convenience fee.

## Changes

- 2026-09-26 - Created.

## See also

- [Kimi Code](../kimi-code/index.md) - the first-party open-weight subscription to compare quota mechanics against.
- [MiniMax Coding Plan](../minimax-coding-plan/index.md) - the token-metered alternative with modality breadth.
- [Model provider feature matrix](../../model-provider-feature-matrix/index.md) - where gateways sit against first-party plans.
- [Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - choose models on evidence before choosing where to buy them.

## References

- https://nano-gpt.com/pricing - current Pro pricing ($12/month, 60M input tokens/week), PAYG minimums, 5% BYOK and pinning fees, as of 2026-09-26.
- http://web.archive.org/web/20250901063827/https://nano-gpt.com/subscription - September 2025 capture showing $8/month with unlimited personal open-weight usage.
- https://nano-gpt.com/blog - activity evidence: September 2026 posts, ZDR routing, monthly crypto-payment statistics.
- https://hn.algolia.com/api/v1/search?query=nano-gpt.com&restrictSearchableAttributes=url&tags=story&hitsPerPage=10 - the service's thin HN footprint (two 0-comment stories, 2024).
- https://hn.algolia.com/api/v1/search?query=NanoGPT&tags=story&hitsPerPage=10 - the name collision with Karpathy's repo dominating HN results.
