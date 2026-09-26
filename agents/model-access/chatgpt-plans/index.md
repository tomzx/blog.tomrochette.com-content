---
title: ChatGPT plans
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, subscriptions, codex, openai]
readability: 3
audience_notes: >
  Engineers deciding which ChatGPT subscription to buy for Codex.
  Assumes you know what a rate limit does to an agent loop and what per-token API pricing looks like.
---

ChatGPT plans are OpenAI's consumer and team subscriptions, and every tier from Free upward now carries Codex, which makes them the subscription path to OpenAI's coding models.

**OpenAI publishes message ranges and credit rates where Anthropic publishes multipliers, but it spends the savings on complexity: six tiers, credits, speed multipliers, and a shared pool that Work, images, and voice all drain.**

## What it is

The 2026 lineup: Free ($0), Go ($8/month), Plus ($20/month), Pro from $100/month in 5x and 20x versions, Business ($25/user/month, $20 annual, minimum 2 seats), and Enterprise custom.
Codex ships on web, CLI, IDE extension, and iOS, with cloud integrations (GitHub code review, Slack, Linear) from Plus up, and ChatGPT Work usage draws the same pool and rates as Codex.
The GPT-6 lineup (Astra, Sol, Luna) carries the plans; GPT-5.5 retires from ChatGPT, Work, and Codex on all plans on October 14, 2026.

## Status

Active, with the developer pricing page fetched and current as of 2026-09-26, and the widest subscription reach of any vendor here.
The 2026 lineup changed materially: Business replaced the Team plan on April 2, the same day Codex billing moved from per-message to token-based credits, and the Go tier appeared below Plus.
The current GPT-6 lineup (Astra, Sol, Luna) carries the plans, with Sol and Luna launched 2026-09-22 per the [Model Selection guide](../../model-selection-for-coding-tasks/index.md) and already listed as included on Plus and Pro in the fetched plan documentation.

## Strengths

- The most published mechanics in the category: official per-model message ranges per 5-hour window, for example GPT-6 Luna at 350-3,000 local messages on Plus versus 7,000-56,000 on Pro 20x.
- Credits extend usage past included limits without upgrading, and Business sits at $25/user with SSO and no training on your data, the sensible team floor.
- The Go tier at $8 is the cheapest named subscription carrying an agentic coder in this category.
- Cloud tasks open pull requests end to end, the strongest hosted-agent story among the vendor plans.

## Cautions

- Everything shares one allowance: Codex, ChatGPT Work, image generation (3-5x faster burn), and desktop voice all draw the same pool, and cloud chats run GPT-5.6 Sol, which may consume more than local messages.
- A practitioner's note from real engagements: two engineers on one shared window exhausted it by early afternoon, the April switch to credits changed budgeting for everyone.
- Real-world cost lands near $100-$200 per active developer per month once usage is heavy, which is Pro territory, not Plus.
- Speed configurations and fast mode multiply credit burn, so the same prompt costs differently depending on settings you may not remember touching.
- The consumer pricing page blocks automated fetches (403 this run), so plan verification runs through the developer docs.

## Pricing

Free: $0, Codex for quick tasks with limited usage.
Go: $8/month, lightweight coding.
Plus: $20/month, a few focused sessions a week, GPT-6 Sol and Luna included.
Pro: $100/month for 5x Plus usage, $200/month for 20x.
Business: $25/user/month ($20 annual, minimum 2 seats), Codex via workspace credits.
Enterprise: custom, flexible credit pricing.
Credits purchase past included limits; API-key Codex usage bills at API rates outside any plan.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-26 | Free to Pro | Baseline: Free $0, Go $8, Plus $20, Pro $100 (5x) and $200 (20x) per month | https://developers.openai.com/codex/pricing |
| 2026 | Pro | Split into the $100 (5x) and $200 (20x) usage tiers; a single-tier Pro preceded it | https://automationatlas.io/answers/chatgpt-codex-pricing-explained-2026 |
| 2026-04-02 | Business | Team at $30/user replaced by Business at $25/user ($20 annual, minimum 2 seats) | https://automationatlas.io/answers/chatgpt-codex-pricing-explained-2026 |
| 2026-04-02 | Billing | Codex usage moved from per-message to token-based credit billing across Plus, Pro, Business, and Enterprise | https://automationatlas.io/answers/chatgpt-codex-pricing-explained-2026 |

## Compared to

- [Claude plans](../claude-plans/index.md): the mirror subscription at identical price points; OpenAI publishes ranges, Anthropic publishes multipliers, and the models themselves decide more than the mechanics.
- [GLM Coding Plan](../glm-coding-plan/index.md): the price-floor alternative, roughly one-seventh of Plus for the GLM line.
- API billing ([Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md)): per-token and uncapped, the right path for CI, and the escape hatch when shared windows keep interrupting real work.

## Bottom line

Recommended for engineers inside the OpenAI ecosystem who want hosted agent features (cloud tasks, code review, Slack) with usage they can budget from published tables; Plus to start, Pro 5x when sessions interrupt.
Not for predictable maximum throughput per dollar, where flat open-model plans win.
My disagreeable claim: the published message ranges are more concrete than Anthropic's multipliers but just as unusable in practice, because model choice, context size, and tool calls swing real consumption by an order of magnitude inside those ranges.

## Changes

- 2026-09-26 - Created when the owner asked why the Claude and OpenAI subscriptions were missing from this category.

## See also

- [Codex](../../harnesses/codex/index.md) - the harness these plans meter and the CLI that can bypass them via API key.
- [Claude plans](../claude-plans/index.md) - the rival subscription at the same price points with opposite disclosure habits.
- [OpenCode Go](../opencode-go/index.md) - the flat open-model alternative at a third of Plus.
- [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md) - OpenAI's API-side bundle, where the subscription row meets per-token reality.

## References

- https://developers.openai.com/codex/pricing - plan prices, per-model message ranges, credit rates, GPT-5.5 retirement, feature availability matrix (fetched 200, 2026-09-26)
- https://automationatlas.io/answers/chatgpt-codex-pricing-explained-2026 - the April 2 Business replacement, the credit-billing switch, Business seat pricing, the real-world cost range and shared-window practitioner note (fetched 200, updated 2026-07-31)
- https://www.simplemetrics.xyz/chatgpt-codex-limits-2026 - independent limit analysis, the ranges-vs-fixed-caps framing, GPT-5.6 family tables (fetched via search extraction, updated 2026-09-09)
- https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu - the business credit rate card and the August 31 GPT-5.4 retirement note (linked from the fetched developer pricing page; not separately fetched)
- https://chatgpt.com/pricing - the consumer plan page (403 to automated fetchers this run; plan prices verified through the developer docs instead)
