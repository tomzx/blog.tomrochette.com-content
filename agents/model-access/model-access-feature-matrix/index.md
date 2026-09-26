---
title: "Model Access Feature Matrix"
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, model-access, llm-pricing]
readability: 3
audience_notes: >
  Engineers deciding where to buy model access for coding agents: gateway, vendor coding plan, or flat subscription.
  Assumes you know per-token pricing and what a rate limit does to an agent loop.
---

This matrix compares the eleven model access providers in this category, the layer that sells you tokens rather than an editor or a harness.

**The same token carries a toll from 0 to 8 percent or sits inside a flat monthly price, and the flat plans only win if your volume actually reaches their quotas.**

Legend: ✓ yes, ✗ no, ~ partial, ? not verified.
Every cell traces to the column's research note, verified as of 2026-09-26; volatile cells carry their own dates.

## The matrix

| Feature | [Cerebras Code](../cerebras-code/index.md) | [Chutes](../chutes/index.md) | [GLM Coding Plan](../glm-coding-plan/index.md) | [Kimi Code](../kimi-code/index.md) | [MiniMax Coding Plan](../minimax-coding-plan/index.md) | [NanoGPT](../nanogpt/index.md) | [OpenCode Go](../opencode-go/index.md) | [OpenCode Zen](../opencode-zen/index.md) | [OpenRouter](../openrouter/index.md) | [Requesty](../requesty/index.md) | [Synthetic](../synthetic/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | speed-first inference subscription | decentralized inference market with subscriptions | vendor coding plan (Z.AI) | vendor membership ladder (Moonshot) | vendor token plan | community aggregator plus subscription | token-pack subscription | curated pay-per-use gateway | passthrough gateway | governance gateway | flat open-model subscription |
| Billing mechanics | flat monthly with token-per-day caps | PAYG plus $10/$20 tiers adding quota and 6-10% off | flat monthly converted to credits, peak multipliers | monthly membership tiers over a shared quota pool | monthly token quotas in 5-hour and weekly windows | PAYG deposits plus a $12 open-weight subscription | $10/month for per-model dollar bundles | per-token, no markup claimed, card fees at cost | passthrough tokens, 5.5% credit fee ($0.80 minimum, Business 8%) | flat 5% of upstream spend | $30 pack or per-token |
| Cheapest paid entry | Pro $50/month (sold out 2026-09-26) | Plus $10/month (PAYG from cents) | Lite $18/month | Moderato $19/month ($15 annual) | Plus $22/month | Pro $12/month (PAYG from $0.10) | $10/month | $20 auto-reload, usage-priced | free tier, then the credit fee | free tier, then 5% | $30/month pack |
| Top tier | Max $200/month | Pro $20/month | Max $168/month | Vivace $199/month ($159 annual) | Ultra $132/month | the $12 Pro tier is the top | one $10/month tier | none, usage-based | Enterprise custom | Enterprise custom | stacked $30 packs |
| Models you can reach | fast Qwen and GLM coding lines | open weights (GLM-5.2, Kimi K3, Qwen, DeepSeek) | the GLM line | the Kimi line, K3 from Pro up | the MiniMax line | hundreds of routes, open weights included | open coding models only (Qwen, Grok, Luna lines) | open plus Claude, GPT, Gemini, and Grok lines | the largest catalog, frontier and open | 600+ models | the open-weight always-on lineup |
| Limit or quota form | 24M/120M tokens per day, TPM caps | daily quota, then discounted PAYG, capped at 5x value | credits per 5 hours and week, 3x peak burn on flagships | one shared pool across chat, research, and code | 5-hour and weekly windows, dynamic peak limits | 60M input tokens per week | per-model monthly dollars ($15-$60), 5-hour and weekly windows | balance only, auto-reload below $5 | provider rate limits pass through | budget caps you set | 500 requests per 5 hours per pack, 1 concurrent per model |
| The catch | sold out, and measured speed fell far short of the marketing | terms changed three times in early 2026, capacity rides on miners | non-refundable, peak burn cuts effective quota, China-based routing | quota shared with chat and Deep Research, ladder moved twice in 2026 | quota drained with zero calls per a June 2026 issue, no refunds | the deal narrowed from $8 unlimited to $12 capped, opaque governance | no longer general API access, agent traffic only, monthly catalog churn | measured at more than 4x OpenRouter on identical open models | the fee punishes small top-ups, credits can expire within a year | the 5% grows with spend, hosted-only, 30-day default log retention | the 3x-Claude framing is contested, packs stack for parallelism, pinned models eventually 404 |
| Frontier models | ✗ open lines only | ✗ open weights | ✗ GLM only | ✗ Kimi only | ✗ MiniMax only | ~ closed models on PAYG, open in the sub | ✗ open models only | ✓ Claude, GPT, Gemini, Grok | ✓ nearly all | ✓ 600+ including frontier | ✗ open models only |
| Works from any agent | ✓ API key | ✓ OpenAI-compatible | ~ supported tools only, special endpoints | ~ first-party clients emphasized, API on higher tiers | ✓ OpenAI-compatible | ✓ OpenAI-compatible | ✓ any agent, coding-agent headers required since 2026-09 | ✓ OpenAI/Anthropic/Google-compatible endpoints | ✓ one key, any client | ✓ one OpenAI-compatible endpoint | ✓ OpenAI-compatible |
| Price trajectory | stable $50/$200 since 2025-08 | free tier retired, Base tier cut | $6/$30 to $18/$80/$168 within a year | promos became standard pricing 2026-09 | Plus $20 to $22 in three months, plan replaced overnight | $8 to $12 with a new cap | $5 promo removed, $15 flagship standard | baseline 2026-09-26, heavy deprecation churn | fee flattened to 5.5% (2025-06), Business 8% added (2026-09) | unchanged since tracking began (2026-09-26) | $20/$60 tiers replaced by a $30 pack |

## Reading the matrix

I read the billing-mechanics row first, because it decides who this provider is for: passthrough gateways meter reality, vendor plans sell a quota, and flat subscriptions sell a ceiling.
**The gateways (OpenRouter, Requesty, Zen) monetize a percentage, the vendor plans (GLM, Kimi, MiniMax) monetize commitment, and the community subs (NanoGPT, Synthetic, Chutes, Go) monetize the gap between list price and what self-hosted open models actually cost to serve.**
On price trajectories, only Requesty and Zen have not moved, and Zen's baseline is one day old, so the stable-looking rows are the youngest ones.
The frontier-models row is the real segmentation: if your loop needs Claude or GPT, the flat open-model subscriptions are irrelevant and the choice is gateway versus vendor subscription.
The catches cluster into two kinds: mechanical limits you can engineer around (concurrency, windows, peak multipliers) and trust problems you cannot (quota draining, silent plan replacement, narrowed deals), and I weight the second kind higher.

## Choosing an access provider

- Default BYOK loop across many providers: OpenRouter for breadth, Requesty if EU residency or budget governance is required.
- One vendor's models all day: that vendor's plan (GLM, Kimi, MiniMax), after checking the peak-hour mechanics against your working hours.
- Open models at a flat ceiling: OpenCode Go or Synthetic for agent-shaped workloads, NanoGPT for breadth beyond coding, Chutes for the cheapest per-token open rates.
- Frontier models without a subscription: OpenCode Zen, paying the measured curation premium only where a mis-served provider would silently degrade your agent.
- Raw speed: Cerebras Code, when it is in stock and your context fits the window.

## Changes

- 2026-09-26 - Created with eleven columns when the owner-directed Model access category was seeded.

## See also

- [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md) - the vendors behind these access products, compared as bundles
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the per-model, per-token economics this layer packages
- [OpenCode](../../harnesses/opencode/index.md) - the harness whose Zen gateway and Go subscription anchor two columns here
- [Trackers and Leaderboards Feature Matrix](../../trackers-and-leaderboards/trackers-and-leaderboards-feature-matrix/index.md) - where usage and price signals about this layer get measured

## References

- https://opencode.ai/docs/go - Go subscription tiers, model limit table (fetched 200, 2026-09-26)
- https://opencode.ai/docs/zen/ - Zen per-model price table and free models (fetched 200, 2026-09-26)
- https://openrouter.ai/docs/faq - OpenRouter billing and routing FAQ (fetched 200, 2026-09-26)
- https://requesty.ai/pricing - Requesty tier table and 5% markup quote (fetched 200, 2026-09-26)
- https://nano-gpt.com/pricing - NanoGPT subscription and per-token prices (fetched 200, 2026-09-26)
- https://platform.minimax.io/docs/guides/pricing-token-plan - MiniMax Token Plan tiers (fetched 200, 2026-09-26)
- https://docs.z.ai/devpack/overview - GLM Coding Plan documentation (fetched 200, 2026-09-26)
- https://chutes.ai/pricing - Chutes PAYG and subscription tiers (fetched 200, 2026-09-26)
- https://synthetic.new/pricing - Synthetic subscription pack pricing (fetched 200, 2026-09-26)
