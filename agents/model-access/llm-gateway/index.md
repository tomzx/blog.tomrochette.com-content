---
title: LLM Gateway
created: 2026-10-04
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, llm-gateway, coding-subscription]
readability: 3
audience_notes: >
  Engineers choosing a hosted gateway or a flat-rate multi-model coding plan.
  Assumes you know per-token provider pricing and what a platform fee on a credit top-up does to small purchases.
---

LLM Gateway is a hosted model gateway from LLMGateway, Inc. (GitHub org theopenco) that routes 250+ models from 40+ providers behind one OpenAI-compatible endpoint at provider list prices with a 5% fee on credit top-ups, and sells DevPass, a flat-rate multi-model coding subscription at $29, $79, and $179 per month.
**It runs the OpenRouter playbook at a lower fee and bolts on the flat coding plan OpenRouter never built, which makes it the only member here selling percentage and flat-rate billing side by side.**

## What it is

A hosted gateway with a self-host option: pay per token at each provider's own rates with no token markup, a 5% platform fee when you buy credits, and BYOK routing with no platform fee at all.
The repo ships under a custom license with a commercial carve-out for the `ee/` directory, so "open-source" is the company's word, not an OSI license.
DevPass claims every $1 converts into $3 of model usage metered at provider rates, works from Claude Code, OpenCode, Cline, Cursor, or any OpenAI-compatible tool, and gates premium models (roughly $5+ per 1M input) behind a weekly fair-use share of credits.
The company reports SOC 2 Type II, a 30-day enterprise pilot with a 99.9% SLA, and site counters of 1T+ tokens and 80M+ requests routed, as of 2026-10-04.

## Status

Active and young: the repo was created 2025-04-12 and shows 1,671 stars and 192 forks as of 2026-10-04, pushed the previous night.
DevPass shipped across Q2 2026 with annual billing and integration guides, and the Q2 roundup puts deepseek-v4-pro at the top of its quarterly token table.
A Hacker News search this run returned no stories about the product, so the footprint is SEO and docs, not community debate.
On 2026-10-04 the DevPass page announced its first devaluation: from October 15, 2026 the monthly allowance falls from 3x to 2x the plan price.

## Strengths

- The fee undercuts OpenRouter's 5.5% credit fee and drops the $0.80 minimum entirely, while BYOK routing costs nothing at all.
- DevPass is the only flat-rate plan here spanning every frontier family (Claude, GPT-5, Gemini) plus the open-weight coders under one key, with a 14-day self-serve refund.
- Spend controls, prompt caching, per-project ceilings, and provider-compliance routing (SOC 2, ISO 27001, and GDPR providers only) are documented on the public pricing page.
- Self-hosting exists if the hosted fee is unacceptable, though enterprise features need a license.

## Cautions

- The community footprint is thin: no Hacker News stories, and the company's "best AI coding plans" post ranks DevPass first against Claude Max, OpenCode Go, and the GLM plan, which is marketing, not measurement.
- DevPass value drops on October 15, 2026, from 3x to 2x the plan price at renewal, the first cut since launch, and the weekly frontier fair-use cap means heavy premium-model users exhaust headroom before the allowance runs out.
- The 5% is charged per top-up, so the small-purchase math that punishes OpenRouter's $0.80 minimum applies here too for frequent small reloads.
- A one-year-old repo with 1,671 stars is early to hold custody of every provider key you own.

## Pricing

PAYG: free tier with 3 rate-limited free models, provider list prices, 5% fee on credit top-ups, BYOK free, non-US cards add 1.5%, and optional full payload retention costs $0.01 per 1M tokens, as of 2026-10-04.
DevPass: Lite $29/month (about $87 of usage), Pro $79/month (about $237), Max $179/month (about $537), 14-day self-serve refund, weekly frontier fair-use, worth 3x the plan price until October 15, 2026 and 2x after.
Lounge chat plans: fast models from $9/month, flagship models from $19/month.
Enterprise: custom, 30-day pilot, SAML SSO and SCIM, 99.9% SLA.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-04 | PAYG / DevPass | Baseline: PAYG at provider rates with 5% on credit top-ups and free BYOK; DevPass Lite $29, Pro $79, Max $179 per month at 3x usage value | https://llmgateway.io/pricing |
| 2026-10-15 | DevPass | Announced: included usage falls from 3x to 2x the plan price at first renewal on or after this date (new subscriptions start at 2x), prices unchanged | https://devpass.llmgateway.io/pricing |

## Compared to

[OpenRouter](../openrouter/index.md) is the same pay-as-you-go gateway idea with the deeper catalog and track record at 5.5% per credit purchase; choose LLM Gateway for the lower fee or for DevPass, OpenRouter for maturity and reach.
[Requesty](../requesty/index.md) meters 5% of upstream spend with EU residency; LLM Gateway's 5% sits on top-ups instead, which is kinder to steady spend but carries no residency story.
[LiteLLM](../litellm/index.md) is the self-hosted zero-fee incumbent; pick it when keys cannot leave your perimeter, LLM Gateway when you want someone else to run the gateway.

## Bottom line

Recommended for multi-model developers who want hosted gateway routing at a fee matching or beating every competitor here, and for flat-rate coding across all frontier families at DevPass prices.
Not for teams that need community scrutiny and a battle-tested gateway, or for premium-model-heavy users who would blow through the fair-use caps.
My disagreeable claim: DevPass at 3x (soon 2x) buys less leverage than OpenCode Go's 6x on open models, so its whole case rests on needing frontier families under one flat bill.

## Changes

- 2026-10-04 - Created when the new-entrant scan surfaced DevPass marketed against this category's members; added with the announced October 15 usage cut already on the price table.
- 2026-10-06 - Converted the Compared-to cross-references from plain-text paths into working links.

## See also

- [OpenRouter](../openrouter/index.md) - the gateway whose fee model this one undercuts.
- [Requesty](../requesty/index.md) - the other 5% gateway, metering spend instead of top-ups.
- [OpenCode Go](../opencode-go/index.md) - the flat-rate open-model alternative DevPass is priced against.
- [LiteLLM](../litellm/index.md) - the self-hosted zero-fee counterpoint.
- [Model provider feature matrix](../../model-provider-feature-matrix/index.md) - where these gateways meet their upstream vendors.

## References

- https://llmgateway.io/ - 250+ models from 40+ providers, 5% on top-ups, BYOK free, SOC 2 Type II, 1T+ tokens routed, self-host with licensed enterprise features (200, fetched 2026-10-04).
- https://llmgateway.io/pricing - free tier, 5% platform fee, BYOK included, retention pricing, plan comparison table (200, fetched 2026-10-04).
- https://devpass.llmgateway.io/ - DevPass $29/$79/$179, $1-to-$3 usage claim, frontier fair-use, 14-day refund, supported agents (200, fetched 2026-10-04).
- https://devpass.llmgateway.io/pricing - per-plan usage values and the October 15, 2026 3x-to-2x change notice (200, fetched 2026-10-04).
- https://llmgateway.io/blog/q2-2026-roundup - DevPass Q2 launch detail, SOC 2 Type II, top-routed models by tokens (200, fetched 2026-10-04).
- https://api.github.com/repos/theopenco/llmgateway - 1,671 stars, 192 forks, created 2025-04-12, pushed 2026-10-03 (200, fetched 2026-10-04).
- https://raw.githubusercontent.com/theopenco/llmgateway/main/LICENSE - custom license text with the ee/ commercial carve-out (200, fetched 2026-10-04).
- https://llmgateway.io/blog/best-ai-coding-plans - the company's self-ranking comparison against Claude Max, OpenCode Go, and the GLM plan, cited as marketing positioning rather than measurement (200, fetched 2026-10-04).
