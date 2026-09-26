---
title: Chutes
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, inference, pay-as-you-go, bittensor]
readability: 3
audience_notes: >
  For developers deciding where to buy model access on a small budget. Assumes familiarity with per-million-token API pricing and coding agents that accept an OpenAI-compatible endpoint.
---

Chutes is a model-access platform built on Bittensor (subnet 64) that sells per-token inference on open-weight models, optional monthly plans, and private GPU deployments.
**Its per-token prices were the lowest I verified in this category, and price is the main reason to pick it.**

## What it is

Chutes serves open-weight models (Qwen, DeepSeek, Kimi, GLM, Mistral, Gemma) from hosted instances and charges by the million tokens, with no subscription required.
Featured models run on confidential TEE compute, and billing accepts USD or TAO from a Bittensor wallet.
A CLI can also deploy a private chute on self-serve GPU capacity billed per second, with a one-time deployment fee scaled to the GPU choice.

## Status

Active and shipping changes as of September 2026, with a live pricing page, status page, and regular community announcements.
2026 was a repair year for the business model: on February 27 the team retired the free 200-requests-per-day Early Access perk, capped subscriptions at 5x pay-as-you-go value, and cut frontier models from the $3 Base tier after its tables showed top users extracting up to 324x their subscription price.
A March 20 update reports tokens served down 45% over six weeks while revenue per million tokens rose 37.7% since February 1, after ending roughly 10B tokens/day of free-quota serving to about 11,000 users.
I could not verify funding or traffic figures.

## Strengths

- Lowest per-token list prices I found this run, for example DeepSeek-V3.2 at $1.00/$1.00 per 1M in/out and Mistral-Nemo at $0.0245/$0.0978.
- Many model families behind one OpenAI-compatible key, so switching models costs nothing.
- Pay-as-you-go works with no plan attached, keeping commitment near zero.
- TEE enclaves on featured models, a privacy posture most cheap providers lack.

## Cautions

- Terms changed three times in early 2026 (free tier removed, 5x cap, Base tier model cuts), so treat any quota as provisional.
- InfoWorld's reviewer found performance underwhelming, called the privacy policy ambiguous, and needed a VPN workaround to sign up.
- The March 2026 update cites a global GPU shortage limiting inventory, so capacity depends on miner participation.
- The 6%/10% plan discounts apply only beyond the bundled daily quota, so heavy users are pushed back to full PAYG rates.

## Pricing

PAYG is the default as of 2026-09-26: GLM-5.2 $1.25 in / $3.95 out per 1M, Kimi-K3 $3.00/$15.00, Qwen3-235B-A22B-Thinking $0.2989/$1.1957, DeepSeek-V3.2 $1.00/$1.00.
Plus costs $10/month for a bundled daily quota plus 6% off PAYG beyond it, and Pro costs $20/month for a larger quota plus 10% off.
Since February 27, 2026, every subscription is capped at 5x the equivalent PAYG value, with overflow billing at standard PAYG.
Private chutes run on an RTX Pro 6000 at $1.80/hour plus a $5.40 one-time deployment fee (3x the hourly rate).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2025-07-31 | Subscriptions | Pricing tiers announced, "coming next Monday" (live early August 2025) | Chutes news post, July 31, 2025 |
| 2026-02 | Base / Plus / Pro | Baseline: $3 / $10 / $20 per month tiers existed | Feb 27, 2026 community announcement usage tables |
| 2026-02-27 | Early Access | Free 200-requests/day perk cut off from TEE models, fully retired March 15, 2026 | same announcement |
| 2026-02-27 | All subscriptions | Value capped at 5x PAYG equivalent; GLM-5, Kimi K2.5, Qwen 3.5, MiniMax M2.5 removed from Base | same announcement |
| 2026-09-26 | Base | No longer listed on the pricing page, which shows only Plus $10, Pro $20, and Enterprise | chutes.ai/pricing |

## Compared to

- [- Cerebras Code](../cerebras-code/index.md) sells raw speed on one coding model at $50/$200; choose it when latency dominates, Chutes when price dominates.
- [- GLM Coding Plan](../glm-coding-plan/index.md) sells a large fixed quota on one model family; choose it if you will burn the quota, Chutes for variety without commitment.

## Bottom line

Recommended for hobbyists and cost-driven developers who want many open models cheaply and can tolerate churn in terms and capacity.
Not for teams needing SLAs, contractual stability, or closed frontier models.
Claim to disagree with: after the 5x cap, Plus and Pro make little sense for coders, because PAYG with a small prepaid balance delivers the same upside without a recurring bill.

## Changes

- 2026-09-26 - Created.

## See also

- [- Cerebras Code](../cerebras-code/index.md) - the speed-first subscription alternative.
- [- GLM Coding Plan](../glm-coding-plan/index.md) - the fixed-quota rival that wins on coding throughput per dollar.
- [- OpenRouter rankings](../../trackers-and-leaderboards/openrouter-rankings/index.md) - where provider model traffic becomes visible.
- [- Model provider feature matrix](../../model-provider-feature-matrix/index.md) - how access providers compare feature by feature.

## References

- https://chutes.ai/pricing - current PAYG model rates, Plus $10 / Pro $20 with 6%/10% PAYG discounts, private GPU pricing (fetched, HTTP 200, as of 2026-09-26).
- https://chutes.ai/news/community-announcement-february - February 27, 2026 changes: Early Access retirement, 5x subscription cap, Base tier model removals, abuse tables (fetched, HTTP 200).
- https://chutes.ai/news/from-volume-to-value-building-a-sustainable-ai-inference-platform-2 - March 20, 2026 economics: tokens down 45%, revenue per token up 37.7%, free-tier costs (fetched, HTTP 200).
- https://chutes.ai/news/coming-soon - July 31, 2025 post announcing the first pricing tiers (fetched, HTTP 200).
- https://chutes.ai/docs/cli/deploy - private chute deployment mechanics and deployment fee structure (fetched, HTTP 200).
- https://www.infoworld.com/article/4075825/how-to-vibe-code-for-free-or-almost-free.html - critical third-party review: underwhelming performance, ambiguous privacy policy, signup bugs; confirms the $3 entry tier in October 2025 (fetched, HTTP 200).
