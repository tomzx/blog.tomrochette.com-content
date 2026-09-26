---
title: GLM Coding Plan
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, subscription, coding]
readability: 3
audience_notes: >
  For developers evaluating Z.ai's subscription against Claude-style coding plans. Assumes familiarity with 5-hour usage windows and prompt-based quotas.
---

The GLM Coding Plan is Z.ai's subscription that sells access to the GLM model family inside coding agents, currently $18/$80/$168 per month for Lite/Pro/Max.
**It is the cheapest quota-per-dollar coding subscription I verified, but a multiplier system governs the quota, so the sticker price is only the start of the math.**

## What it is

A credit-based subscription from Z.ai (Zhipu) for GLM-5.3 and GLM-5.3-Flash, consumed inside supported coding tools (Claude Code, Cline, OpenCode, Kilo Code, Cursor, Z.ai's own ZCode, and others).
You point the tool at Z.ai's Anthropic- or OpenAI-compatible endpoints with a plan key, and requests to older GLM versions are auto-routed to 5.3.
Plans bundle exclusive MCP servers (vision, web search, web reader, Zread).
Usage outside officially supported tools is contractually prohibited, which makes this a walled-garden subscription rather than an API credit pack.

## Status

Actively developed and restructured twice in a year: prompt-based plans at launch in 2025, then a credits-based system for new subscribers on July 30, 2026, with legacy plans grandfathered to the end of their billing cycle.
The plan rode the GLM release cadence (GLM-4.5 in 2025, GLM-5.2 in June 2026, GLM-5.3 in August 2026), and tier prices rose at each step.
Promotional quota mechanics (off-peak discounts, Flash campaigns) changed repeatedly through 2026, so published value figures have a short shelf life.
I found no reliable subscriber counts.

## Strengths

- Quota per dollar is unmatched in this category: Z.ai itself documents quota worth approximately 15-30x the monthly fee at API rates.
- Lite at $18, or $12.60 effective on yearly billing, undercuts every $20 rival I checked.
- Off-peak usage (outside Mon-Fri 14:00-18:00 UTC+8) deducts credits at 50%, a standing discount for most time zones.
- Hard-stop quota means spend is fixed: when quota runs out, calls pause and your account balance is never touched.

## Cautions

- Subscriptions are non-refundable once purchased, per the official FAQ.
- The flagship model burns quota up to 3x faster at peak (a usage multiplier, not a price change), so effective throughput can be a third of the headline prompts.
- Strict supported-tools-only terms and special endpoints block custom integrations.
- Third-party reviewers report slow and unreliable periods under load, and prompts route through China-based infrastructure, a blocker for residency-bound teams.

## Pricing

Current tiers as of 2026-09-26: Lite $18/month (per Z.ai docs), Pro $80 and Max $168 per August 2026 snapshots of the subscribe page, with 20% off quarterly and 30% off yearly billing (effective $12.60/$56/$117.60 per month).
The July 2026 credits system allocates 2,000/10,000 credits per 5 hours/week on Lite, 12,000/60,000 on Pro, 28,000/140,000 on Max.
Credits deduct per token type with multipliers (GLM-5.3: input 6.9, cached input 1.7, output 24, over 10,000), plus per-call charges for bundled MCP tools.
Under the legacy prompts system, Z.ai documented quota as roughly 80/400/1,600 prompts per 5-hour window, with one prompt estimated at 15-20 model invocations.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2025-09 | Lite / Pro | Baseline: launched at $6/$30 per month with first-month promos of $3/$15 | Cline blog, Sep 18, 2025 |
| 2026-06-18 | Lite / Pro / Max | List prices $18/$72/$160, yearly effective $12.60/$50.40/$112 | HyScaler |
| 2026-07-30 | All plans | Credits-based plans replace prompt-based plans for new subscribers | docs.z.ai usage-revision notice |
| 2026-08-14 | Lite / Pro / Max | Pro to $80 and Max to $168; 20% quarterly and 30% yearly discounts | emergent.sh |

## Compared to

- [- Cerebras Code](../cerebras-code/index.md) sells speed at $50/$200; choose it when latency dominates, GLM when volume per dollar dominates.
- [- Chutes](../chutes/index.md) sells cheap pay-as-you-go across many model families; choose it for flexibility, GLM for a large fixed quota on one frontier family.
- Z.ai's own [ZCode](../../harnesses/zcode/index.md) is the intended surface, but any supported harness works with the same quota.

## Bottom line

Recommended for high-volume, human-in-the-loop coding where quota per dollar is the binding constraint and you can work off-peak.
Not for long-horizon autonomous agent runs (aggregator tracking puts GLM-5.2 at about half of Claude Opus 4.8's SWE-Marathon score), Claude-ecosystem power users, or residency-bound teams.
Claim to disagree with: the rational entry is a single month of $18 Lite and never the discounted yearly plan, because the plan is non-refundable and its terms changed twice in a year.

## Changes

- 2026-09-26 - Created.

## See also

- [- Cerebras Code](../cerebras-code/index.md) - the speed-first alternative subscription.
- [- Chutes](../chutes/index.md) - the cheap multi-model alternative.
- [- ZCode](../../harnesses/zcode/index.md) - Z.ai's own coding surface for this plan.
- [- Cline](../../harnesses/cline/index.md) - one of the first tools the plan targeted.
- [- Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - how to decide whether GLM models fit your tasks.

## References

- https://docs.z.ai/devpack/overview - current credit allowances (2,000/12,000/28,000 per 5h), credit formula, off-peak 50% rule, "starting at 18 USD" (fetched, HTTP 200).
- https://docs.z.ai/devpack/notice/usage-revision - July 30, 2026 credits transition; legacy 15-30x value claim and per-plan prompt ceilings (fetched, HTTP 200).
- https://docs.z.ai/devpack/faq - non-refundable policy, supported-tools restriction, no balance deduction, quota reset cards (fetched, HTTP 200).
- https://cline.bot/blog/zai-cline-3-dollar-ai-coding - launch-era pricing: $6/$30 with $3/$15 first-month promos, 120/600 prompts per 5 hours (fetched, HTTP 200, Sep 18, 2025).
- https://hyscaler.com/insights/glm-coding-plan-review/ - June 2026 tiers at $18/$72/$160, 3x peak multiplier, competitive framing (fetched, HTTP 200).
- https://www.digitalapplied.com/blog/glm-coding-plan-worth-it-2026-value-analysis - critical analysis, Jul 3, 2026: multiplier math, non-refundability, China residency, long-horizon benchmark gap (fetched, HTTP 200).
- https://emergent.sh/learn/glm-5-3-pricing - August 2026 tiers at $18/$80/$168 with yearly equivalents; GLM-5.3 has no per-token API rate yet (fetched, HTTP 200).
