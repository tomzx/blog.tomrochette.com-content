---
title: Qwen Coding Plan
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, qwen, subscriptions, alibaba]
readability: 3
audience_notes: >
  For developers choosing a flat-rate model subscription for coding agents.
  Assumes familiarity with 5-hour usage windows, request quotas, and pay-as-you-go API billing.
---

The Qwen Coding Plan is Alibaba Cloud Model Studio's flat-rate subscription that sells Qwen plus rival models (Kimi, GLM, MiniMax) into coding agents through one plan-specific key.
**It is the only mainstream coding subscription I found that bundles competitors' models under one fee, but it carries the strictest automation ban in this category and its product line was restructured twice in six months.**

## What it is

A subscription from Alibaba Cloud (Model Studio, the international DashScope platform) now sold in two generations.
The older request-based Coding Plan charges $50/month for Pro and deducts per request; the newer credits-based Token Plan (Singapore region) deducts from a shared Credits pool spanning text, image, video, and speech models.
Both expose OpenAI-compatible and Anthropic-compatible endpoints and require a plan-specific `sk-sp-` key with a dedicated base URL, so one subscription feeds Claude Code, OpenCode, Codex, Cursor, Cline, Qwen Code, Qoder, Kilo CLI, and OpenClaw.
The Pro roster includes third-party flagships (kimi-k2.5, glm-5, MiniMax-M2.5) alongside qwen3.7-plus, qwen3.6-plus, and the qwen3-coder line.

## Status

Actively sold but mid-transition, and the transition is not cosmetic.
Coding Plan Lite closed to new subscriptions on 2026-03-20 and to renewals and upgrades on 2026-04-13.
The official Token Plan FAQ states that Coding Plan Pro was a limited-quantity offering that is "no longer available once sold out", recommends Token Plan instead, and provides no migration or upgrade path between the two products.
As of 2026-09-26 the coding-plan docs (updated 2026-09-11) still headline the $50 Pro plan while the Token Plan guide (updated 2026-09-25) sits above it in the docs nav, and Token Plan is Singapore-region only.

## Strengths

- **The multi-vendor roster is the real product.** One key routes to Qwen, Kimi-K2.5, GLM-5, MiniMax-M2.5, and on Token Plan DeepSeek-V4-Pro plus the image, audio, and video families.
- Token Plan entry is the cheapest on-ramp I verified in this category: $6/month limited-time ($8 list) for 11,500 Credits.
- $50 Coding Pro bought up to 90,000 requests per month, 6,000 per 5 hours, 45,000 per week, which undercuts pay-as-you-go for anyone spending over $100/month on these APIs.
- Fixed monthly billing with hard caps: when a window empties, calls pause instead of drawing on your account balance.

## Cautions

- **The terms ban automated scripts, CI/CD, batch processing, and application backends, and violations "may result in subscription suspension or API key revocation".**
- Critical coverage documents enforcement as automated and unpredictable: users report suspensions for rapid-fire long sessions and background-request tools, immediate loss of access for the rest of the billing period, and slow, opaque appeals; as the review puts it, "the suspension risk is not theoretical".
- Quota counts requests, not tokens: Alibaba's own docs say simple tasks burn 5-10 model calls and complex ones 10-30 or more, so 90,000 requests is far fewer agent runs than it sounds.
- Mixing the plan key with the general pay-as-you-go key produces unexpected API charges, a footgun the official FAQ dedicates a section to.
- Pro models are pinned to exact snapshots and third-party reviewers report the roster changing with little notice, so a subscription can silently change what it buys.
- Platform throttling under load is contractually "not considered a service interruption or a breach of contract", so slowdowns carry no recourse.

## Pricing

As of 2026-09-26 two price sheets coexist.
Coding Plan Pro: $50/month, capped at 6,000 requests per 5 hours, 45,000 per week, and 90,000 per month, whichever hits first (official docs, updated 2026-09-11).
Token Plan Personal (Singapore region): Lite $6 (list $8), Essential $10 (list $16), Standard $18 (list $25), Pro $68 (list $80) per month for 11,500/25,500/45,000/180,000 Credits, with team seats at $20/$75/$200 and extra bundles at $15 per 20,000 Credits.
A third-party tracker (data updated 2026-09-24) reports China-side early-bird pricing of ¥39/¥139/¥499 per month, a limited-time night rate of 40% of normal Credits from 22:00, and 88% over-limit billing.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-03 | Lite / Pro | Baseline: Lite listed at ¥40/month in China and promoted as low as $3/month internationally, Pro at $50/month | codingplan.org; vibecoding.app |
| 2026-03-20 | Lite | Discontinued for new subscriptions | Alibaba Cloud coding-plan docs |
| 2026-04-13 | Lite | Renewals and upgrades discontinued | Alibaba Cloud coding-plan docs |
| 2026-08 | Token Plan | Request-based Coding Plan upgraded to a credits-based Token Plan with China early-bird ¥39/¥139/¥499 per month | codingplan.org |
| 2026-09-26 | Token Plan (intl) | Lite $6/$8, Essential $10/$16, Standard $18/$25, Pro $68/$80 per month; team seats $20/$75/$200 | Alibaba Cloud Token Plan overview |

## Compared to

- [- GLM Coding Plan](../glm-coding-plan/index.md) wins on quota per dollar; choose Qwen when one subscription covering several vendors' models matters more.
- [- MiniMax Coding Plan](../minimax-coding-plan/index.md) follows the same China flat-fee pattern with a narrower roster and similar interactivity terms.
- [- OpenRouter](../openrouter/index.md) sells the opposite contract: pay per token, no interactivity restrictions, no suspension risk.

## Bottom line

Recommended for heavy interactive users inside supported harnesses who want Qwen and its rivals under one flat fee and can tolerate mid-cycle throttling.
Not for CI/CD, batch jobs, unattended agent farms, or anyone who cannot absorb losing access mid-billing-cycle with no guaranteed refund.
Claim to disagree with: the $50 Coding Plan Pro that Alibaba's docs still headline is now the wrong purchase for almost everyone, because Alibaba's own FAQ calls it a limited offering that is gone once sold out and steers new buyers to the credits-based Token Plan.

## Changes

- 2026-09-26 - Created when the owner asked for any remaining subscription providers.

## See also

- [- GLM Coding Plan](../glm-coding-plan/index.md) - the structural twin: same 5-hour window design, cleaner quota math.
- [- MiniMax Coding Plan](../minimax-coding-plan/index.md) - the other China flat-fee plan in this category.
- [- OpenRouter](../openrouter/index.md) - the pay-as-you-go alternative without usage-pattern enforcement.
- [- Model provider feature matrix](../../model-provider-feature-matrix/index.md) - cross-provider comparison where this plan's rows live.
- [- Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - how to judge whether Qwen models fit the work.

## References

- https://www.alibabacloud.com/help/en/model-studio/coding-plan - official Coding Plan docs: $50 Pro, 6,000/45,000/90,000 request caps, Lite dates of 2026-03-20 and 2026-04-13, automation ban, snapshot-pinned roster, `sk-sp-` key rules (fetched, HTTP 200).
- https://www.alibabacloud.com/help/en/model-studio/token-plan-overview - official Token Plan overview: USD tiers and Credits, Singapore-only availability, and the FAQ stating Coding Plan Pro was limited-quantity with no migration path (fetched, HTTP 200).
- https://www.alibabacloud.com/en/campaign/ai-scene-coding - official campaign and purchase page: limited-time USD prices, 2X credit promotion, Qwen3.8-Max positioning (fetched, HTTP 200).
- https://www.alibabacloud.com/help/en/model-studio/token-plan-guide - official docs hub placing Token Plan above Coding Plan in the product nav as of 2026-09-25 (fetched, HTTP 200).
- https://codingplan.org/en/plans/qwen - tracker: credits restructure, ¥39/¥139/¥499 early-bird, 40% night rate from 22:00, legacy ¥40/¥200 China prices (fetched, HTTP 200, data updated 2026-09-24).
- https://vibecoding.app/blog/alibaba-coding-plan-review - critical review: suspension reports, opaque appeals, no rollover, roster changes without notice (fetched, HTTP 200, updated 2026-06-17).
- https://common-buy-intl.alibabacloud.com/coding-plan - official purchase URL; fetch reached a 2FA verification wall, so no plan data was read from it (fetch blocked, disclosed).
