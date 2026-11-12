---
title: Qwen Coding Plan
created: 2026-09-26
updated: 2026-11-12
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
The Pro roster pins exact model snapshots (qwen3.7-plus, qwen3.6-plus, qwen3.5-plus, kimi-k2.5, glm-5, MiniMax-M2.5), and the docs page updated 2026-10-11 no longer lists the qwen3-coder line, stating that models not listed are not supported.

## Status

Actively sold but mid-transition, and the transition is not cosmetic.
Coding Plan Lite closed to new subscriptions on 2026-03-20 and to renewals and upgrades on 2026-04-13.
The official Token Plan FAQ stated that Coding Plan Pro was a limited-quantity offering that is "no longer available once sold out", recommended Token Plan instead, and provided no migration or upgrade path between the two products, with the 2026-10-28 fetch its last live reading.
As of 2026-10-14 the coding-plan docs (updated 2026-10-11) still headlined the $50 Pro plan while the Token Plan guide sat above it in the docs nav, and Token Plan is Singapore-region only.
At the 2026-11-04 re-fetch the docs rebuilt the same day: the nav labels the Coding Plan legacy, the Token Plan overview became a Bailian CLI quick-start flow (with the token-plan.ap-southeast-1.maas.aliyuncs.com base URL) that no longer carries the USD tier table, the Singapore-only row, or the sold-out FAQ text, and the new FAQ page covers Team Edition only.

## Strengths

- **The multi-vendor roster is the actual product.** One key routes to Qwen, Kimi-K2.5, GLM-5, MiniMax-M2.5, and on Token Plan DeepSeek-V4-Pro plus the image, audio, and video families.
- Token Plan entry is the cheapest on-ramp I verified in this category: $3/month limited-time ($8 list) for 11,500 Credits, the promotional price since the 2026-11-04 halving.
- $50 Coding Pro bought up to 90,000 requests per month, 6,000 per 5 hours, 45,000 per week, which undercuts pay-as-you-go for anyone spending over $100/month on these APIs.
- Fixed monthly billing with hard caps: when a window empties, calls pause instead of drawing on your account balance.

## Cautions

- **The terms ban automated scripts, application backends, and other non-interactive scenarios, and violations "may result in subscription suspension or API key revocation" (the wording on the 2026-11-04 docs; the CI/CD and batch-processing phrasing stood through the 2026-10-28 read).**
- Critical coverage documents enforcement as automated and unpredictable: users report suspensions for rapid-fire long sessions and background-request tools, immediate loss of access for the rest of the billing period, and slow, opaque appeals; as the review puts it, "the suspension risk is not theoretical".
- Quota counts requests, not tokens: Alibaba's own docs say simple tasks burn 5-10 model calls and complex ones 10-30 or more, so 90,000 requests is far fewer agent runs than it sounds.
- Mixing the plan key with the general pay-as-you-go key produces unexpected API charges, a footgun the official FAQ dedicates a section to.
- Pro models are pinned to exact snapshots and third-party reviewers report the roster changing with little notice, so a subscription can silently change what it buys.
- Platform throttling under load is contractually "not considered a service interruption or a breach of contract", so slowdowns carry no recourse.

## Pricing

As of 2026-11-04 (rotation re-verification) two price sheets coexist.
Coding Plan Pro: $50/month, capped at 6,000 requests per 5 hours, 45,000 per week, and 90,000 per month, whichever hits first (official docs, page updated and re-fetched 2026-11-04, now labeled legacy in the docs nav, with slots still first-come, first-served).
Token Plan Personal (Singapore region): Lite $3 (list $8), Essential $5 (list $16), Standard $18 (list $25), Pro $68 (list $80) per month for 11,500/25,500/45,000/180,000 Credits per the campaign page fetched 2026-11-04, where the Lite and Essential promotional prices halved from the $6/$10 standing on 2026-10-28 with list prices and Credits unchanged, and team seats hold at $20/$75/$200 for 25,000/100,000/250,000 Credits per seat; the $15-per-20,000-Credits bundle rows that stood on the pre-rebuild overview left the docs with the 2026-11-04 rebuild.
A third-party tracker (data updated 2026-09-24) reports China-side early-bird pricing of ¥39/¥139/¥499 per month, a limited-time night rate of 40% of normal Credits from 22:00, and 88% over-limit billing.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-03 | Lite / Pro | Baseline: Lite listed at ¥40/month in China and promoted as low as $3/month internationally, Pro at $50/month | codingplan.org; vibecoding.app |
| 2026-03-20 | Lite | Discontinued for new subscriptions | Alibaba Cloud coding-plan docs |
| 2026-04-13 | Lite | Renewals and upgrades discontinued | Alibaba Cloud coding-plan docs |
| 2026-08 | Token Plan | Request-based Coding Plan upgraded to a credits-based Token Plan with China early-bird ¥39/¥139/¥499 per month | codingplan.org |
| 2026-09-26 | Token Plan (intl) | Lite $6/$8, Essential $10/$16, Standard $18/$25, Pro $68/$80 per month; team seats $20/$75/$200 | Alibaba Cloud Token Plan overview |
| 2026-11-04 (observed) | Token Plan Lite / Essential | Campaign promotional prices halved: Lite $6 to $3/month and Essential $10 to $5/month (list prices $8 and $16 unchanged, Credits grants unchanged, Standard and Pro unchanged, Team seats unchanged) | https://www.alibabacloud.com/en/campaign/ai-scene-coding |

## Compared to

- [GLM Coding Plan](../glm-coding-plan/index.md) wins on quota per dollar; choose Qwen when one subscription covering several vendors' models matters more.
- [MiniMax Coding Plan](../minimax-coding-plan/index.md) follows the same China flat-fee pattern with a narrower roster and similar interactivity terms.
- [OpenRouter](../openrouter/index.md) sells the opposite contract: pay per token, no interactivity restrictions, no suspension risk.

## Bottom line

Recommended for heavy interactive users inside supported harnesses who want Qwen and its rivals under one flat fee and can tolerate mid-cycle throttling.
Not for CI/CD, batch jobs, unattended agent farms, or anyone who cannot absorb losing access mid-billing-cycle with no guaranteed refund.
Claim to disagree with: the $50 Coding Plan Pro that Alibaba's docs still headline is now the wrong purchase for almost everyone, because Alibaba's own FAQ calls it a limited offering that is gone once sold out and steers new buyers to the credits-based Token Plan.

## Changes

- 2026-09-26 - Created when the owner asked for any remaining subscription providers.
- 2026-10-06 - Cleaned the Compared-to and See also link labels (stray leading dashes inside the link text), and the Coding Plan Pro quota terms re-verified on the official docs.
- 2026-10-11 - Roster check: the docs (updated the same day) dropped the qwen3-coder line from the Pro plan's supported-models list, which now pins qwen3.7-plus, qwen3.6-plus, qwen3.5-plus, kimi-k2.5, glm-5, and MiniMax-M2.5 and states that unlisted models are not supported; every stated price re-verified unchanged.
- 2026-10-28 - Rotation re-verification: every cited source re-fetched live (the four Alibaba Cloud docs and campaign pages, the codingplan.org tracker, and the vibecoding.app critical review) with the $50 Pro plan, its 6,000/45,000/90,000 caps, the "not supported" roster line, the $6/$10/$18/$68 Token Plan tiers, and the tracker's early-bird rows all unchanged; the common-buy purchase URL still serves a login wall.
- 2026-11-04 - Rotation re-verification caught two moves: the campaign page halved the Token Plan Lite and Essential promotional prices ($6 to $3, $10 to $5, list prices and Credits unchanged, Standard and Pro and Team seats unchanged), and the Alibaba docs rebuilt the same day (Coding Plan labeled legacy in the nav, the Token Plan overview rebuilt into a Bailian CLI quick-start that dropped the USD tier table, the Singapore-only row, and the sold-out FAQ text); the legacy plan's $50 price, caps, pinned roster, suspension language, and the 5-10/10-30 calls-per-task figures re-verified unchanged; the automation-ban caution reworded to the current docs text; price history row appended.

## See also

- [GLM Coding Plan](../glm-coding-plan/index.md) - the structural twin: same 5-hour window design, cleaner quota math.
- [MiniMax Coding Plan](../minimax-coding-plan/index.md) - the other China flat-fee plan in this category.
- [OpenRouter](../openrouter/index.md) - the pay-as-you-go alternative without usage-pattern enforcement.
- [Model provider feature matrix](../../model-provider-feature-matrix/index.md) - cross-provider comparison where this plan's rows live.
- [Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - how to judge whether Qwen models fit the work.

## References

- https://www.alibabacloud.com/help/en/model-studio/coding-plan - official Coding Plan docs: $50 Pro, 6,000/45,000/90,000 request caps, Lite dates of 2026-03-20 and 2026-04-13, automation ban, snapshot-pinned roster, `sk-sp-` key rules (fetched, HTTP 200; re-fetched 2026-10-14 with the page still dated 2026-10-11 and the roster and prices unchanged; re-fetched 2026-10-25 unchanged; re-fetched 2026-10-26 with the $50/month row, the 6,000/45,000/90,000 caps, the pinned roster ending in "Models not listed above are not supported", and the `sk-sp-` key rules all confirmed; re-fetched 2026-10-28 with the same rows confirmed again; re-fetched 2026-11-04 with the page updated that day, the plan labeled legacy in the docs nav, the $50 price, caps, roster line, suspension and throttling language, and the 5-10/10-30 calls figures all confirmed, and the automation ban reading "automated scripts, application backends, or other non-interactive scenarios")
- https://www.alibabacloud.com/help/en/model-studio/token-plan-overview - official Token Plan overview: USD tiers and Credits, Singapore-only availability, and the FAQ stating Coding Plan Pro was limited-quantity with no migration path (fetched, HTTP 200; re-fetched 2026-10-25 with the $6/$10/$18/$68 tiers and Singapore-only row unchanged; re-fetched 2026-10-26 with the $6 and $68 tiers, the 11,500-Credits entry, and the Singapore rows confirmed; re-fetched 2026-10-28 with the tiers and Credits rows confirmed again; re-fetched 2026-11-04 with the page (updated that day) rebuilt into a Bailian CLI quick-start, and the tier table, the Singapore-only row, and the sold-out FAQ text all gone from the page)
- https://www.alibabacloud.com/en/campaign/ai-scene-coding - official campaign and purchase page: limited-time USD prices, 2X credit promotion, Qwen3.8-Max positioning (fetched, HTTP 200; re-fetched 2026-10-25 unchanged; re-fetched 2026-10-26 with the $6 and $68 price points and the 11,500-Credits entry present; re-fetched 2026-10-28 unchanged; re-fetched 2026-11-04 with Lite at $3/$8 monthly (62% off, $65/$96 yearly) and Essential at $5/$16 monthly (68% off, $100/$192 yearly), Standard $18/$25 and Pro $68/$80 unchanged, Credits grants and Team seats unchanged)
- https://www.alibabacloud.com/help/en/model-studio/token-plan-guide - official docs hub placing Token Plan above Coding Plan in the product nav as of 2026-09-25 (fetched, HTTP 200; re-fetched 2026-10-25 unchanged; re-fetched 2026-10-26 unchanged; re-fetched 2026-10-28 unchanged; re-fetched 2026-11-04 with the page (updated that day) rebuilt as a thin "Get Started" nav page with no Coding Plan entry in the visible nav)
- https://www.alibabacloud.com/help/en/model-studio/token-plan-faq - the Team Edition FAQ page that now carries the Token Plan questions, with no sold-out or migration statement (fetched 200, 2026-11-04, page updated that day; grounds the relocation of the FAQ content out of the overview)
- https://codingplan.org/en/plans/qwen - tracker: credits restructure, ¥39/¥139/¥499 early-bird, 40% night rate from 22:00, legacy ¥40/¥200 China prices (fetched, HTTP 200, data updated 2026-09-24; re-fetched 2026-10-25, tracker data still dated 2026-09-24; re-fetched 2026-10-26, tracker data still dated 2026-09-24 with the early-bird and night-rate rows present; re-fetched 2026-10-28, tracker data still dated 2026-09-24; re-fetched 2026-11-04, tracker data still dated 2026-09-24 with the same rows).
- https://vibecoding.app/blog/alibaba-coding-plan-review - critical review: suspension reports, opaque appeals, no rollover, roster changes without notice (fetched, HTTP 200, updated 2026-06-17; re-fetched 2026-10-25 unchanged; re-fetched 2026-10-26 with the suspension, appeal, and rollover sections present; re-fetched 2026-10-28 unchanged; re-fetched 2026-11-04 unchanged).
- https://common-buy-intl.alibabacloud.com/coding-plan - official purchase URL; fetch reached a 2FA verification wall, so no plan data was read from it (fetch blocked, disclosed; re-attempted 2026-10-25, 2026-10-26, 2026-10-28, and 2026-11-04, still walled behind the login UI).
