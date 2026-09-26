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

This matrix compares the sixteen model access providers in this category, the layer that sells you tokens rather than an editor or a harness, from passthrough gateways to the consumer subscriptions that carry Claude Code, Codex, Antigravity, and Grok Build.

**The same token carries a toll from 0 to 8 percent or sits inside a flat monthly price, and the flat plans only win if your volume actually reaches their quotas.**

Legend: ✓ yes, ✗ no, ~ partial, ? not verified.
Every cell traces to the column's research note; volatile cells carry their own dates.

## The matrix

| Feature | [Cerebras Code](../cerebras-code/index.md) | [ChatGPT plans](../chatgpt-plans/index.md) | [Chutes](../chutes/index.md) | [Claude plans](../claude-plans/index.md) | [GLM Coding Plan](../glm-coding-plan/index.md) | [Google AI plans](../google-ai-plans/index.md) | [Kimi Code](../kimi-code/index.md) | [MiniMax Coding Plan](../minimax-coding-plan/index.md) | [NanoGPT](../nanogpt/index.md) | [OpenCode Go](../opencode-go/index.md) | [OpenCode Zen](../opencode-zen/index.md) | [OpenRouter](../openrouter/index.md) | [Qwen Coding Plan](../qwen-coding-plan/index.md) | [Requesty](../requesty/index.md) | [SuperGrok](../supergrok/index.md) | [Synthetic](../synthetic/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | speed-first inference subscription | vendor consumer subscription (OpenAI) | decentralized inference market with subscriptions | vendor consumer subscription (Anthropic) | vendor coding plan (Z.AI) | vendor consumer subscription (Google) | vendor membership ladder (Moonshot) | vendor token plan | community aggregator plus subscription | token-pack subscription | curated pay-per-use gateway | passthrough gateway | vendor coding plan (Alibaba Cloud) | governance gateway | vendor consumer subscription (xAI) | flat open-model subscription |
| Billing mechanics | flat monthly with token-per-day caps | flat monthly, credit-based usage in 5-hour windows over a shared pool | PAYG plus $10/$20 tiers adding quota and 6-10% off | flat monthly, usage multipliers over a shared 5-hour and weekly clock | flat monthly converted to credits, peak multipliers | flat monthly over rate limits plus a flexible AI credit pool | monthly membership tiers over a shared quota pool | monthly token quotas in 5-hour and weekly windows | PAYG deposits plus a $12 open-weight subscription | $10/month for per-model dollar bundles | per-token, no markup claimed, card fees at cost | passthrough tokens, 5.5% credit fee ($0.80 minimum, Business 8%) | flat monthly converted to request or credit quotas with 5-hour, weekly, and monthly caps | flat 5% of upstream spend | flat monthly over one shared weekly pool spanning chat, Build, and API | $30 pack or per-token |
| Cheapest paid entry | Pro $50/month (sold out 2026-09-26) | Go $8/month | Plus $10/month (PAYG from cents) | Pro $20/month ($17 annual) | Lite $18/month | AI Plus (about CA$13.99/month on the fetched Canadian page) | Moderato $19/month ($15 annual) | Plus $22/month | Pro $12/month (PAYG from $0.10) | $10/month | $20 auto-reload, usage-priced | free tier, then the credit fee | Token Plan Lite $6/month (list $8, Singapore) | free tier, then 5% | SuperGrok $30/month (Lite $10 in testing) | $30/month pack |
| Top tier | Max $200/month | Pro 20x $200/month | Pro $20/month | Max 20x $200/month | Max $168/month | AI Ultra 20x (about $200/month, secondhand) | Vivace $199/month ($159 annual) | Ultra $132/month | the $12 Pro tier is the top | one $10/month tier | none, usage-based | Enterprise custom | Token Plan Pro $68/month (list $80) | Enterprise custom | SuperGrok Heavy $300/month (third-party reported) | stacked $30 packs |
| Models you can reach | fast Qwen and GLM coding lines | the GPT-6 and GPT-5.6 lines | open weights (GLM-5.2, Kimi K3, Qwen, DeepSeek) | the Claude line, Fable via credits on Pro | the GLM line | the Gemini line via Antigravity and Gemini CLI | the Kimi line, K3 from Pro up | the MiniMax line | hundreds of routes, open weights included | open coding models only (Qwen, Grok, Luna lines) | open plus Claude, GPT, Gemini, and Grok lines | the largest catalog, frontier and open | the Qwen line plus bundled Kimi, GLM, and MiniMax on some tiers | 600+ models | the Grok line (4.6, 4.7) via Grok Build | the open-weight always-on lineup |
| Limit or quota form | 24M/120M tokens per day, TPM caps | shared agentic pool, published per-model message ranges per 5 hours | daily quota, then discounted PAYG, capped at 5x value | one shared pool, unpublished multipliers (1x/5x/20x), 5-hour plus weekly clocks | credits per 5 hours and week, 3x peak burn on flagships | 5-hour Ultra credit refresh, Never or Always overage modes | one shared pool across chat, research, and code | 5-hour and weekly windows, dynamic peak limits | 60M input tokens per week | per-model monthly dollars ($15-$60), 5-hour and weekly windows | balance only, auto-reload below $5 | provider rate limits pass through | whichever of the 5-hour, weekly, or monthly caps hits first | budget caps you set | one weekly pool shared across chat, Build, and API | 500 requests per 5 hours per pack, 1 concurrent per model |
| The catch | sold out, and measured speed fell far short of the marketing | Work, images, and voice drain the same pool; real cost lands near $100-$200 per developer once heavy | terms changed three times in early 2026, capacity rides on miners | chat and code share one pool, quotas unpublished, Fable capped at 50% of weekly limits on Max | non-refundable, peak burn cuts effective quota, China-based routing | US dollar prices render client-side, credit purchase needs sign-in, storage numbers disagree across Google pages | quota shared with chat and Deep Research, ladder moved twice in 2026 | quota drained with zero calls per a June 2026 issue, no refunds | the deal narrowed from $8 unlimited to $12 capped, opaque governance | no longer general API access, agent traffic only, monthly catalog churn | measured at more than 4x OpenRouter on identical open models | the fee punishes small top-ups, credits can expire within a year | Coding Plan Pro sold out with no migration path, and the predecessor plan suspended automation users | the 5% grows with spend, hosted-only, 30-day default log retention | Lite and Heavy dollar figures are not on the official card, and the shared pool means chat competes with your agent | the 3x-Claude framing is contested, packs stack for parallelism, pinned models eventually 404 |
| Frontier models | ✗ open lines only | ✓ own frontier | ✗ open weights | ✓ own frontier | ✗ GLM only | ✓ own frontier | ✗ Kimi only | ✗ MiniMax only | ~ closed models on PAYG, open in the sub | ✗ open models only | ✓ Claude, GPT, Gemini, Grok | ✓ nearly all | ✓ own frontier | ✓ 600+ including frontier | ✓ own frontier | ✗ open models only |
| Works from any agent | ✓ API key | ~ subscription locked to first-party surfaces, the CLI rides an API key instead | ✓ OpenAI-compatible | ✗ subscription locked to first-party harnesses, third-party use rides API keys | ~ supported tools only, special endpoints | ~ Antigravity and Gemini CLI first-party, other agents ride API keys | ~ first-party clients emphasized, API on higher tiers | ✓ OpenAI-compatible | ✓ OpenAI-compatible | ✓ any agent, coding-agent headers required since 2026-09 | ✓ OpenAI/Anthropic/Google-compatible endpoints | ✓ one key, any client | ~ one key across coding tools, automation restricted | ✓ one OpenAI-compatible endpoint | ~ Grok Build first-party, partner sign-in for others, API key otherwise | ✓ OpenAI-compatible |
| Price trajectory | stable $50/$200 since 2025-08 | Pro split into $100/$200, Business replaced Team, credit billing since April | free tier retired, Base tier cut | prices stable since the Max launch, but the quota behind them moved twice in spring 2026 | $6/$30 to $18/$80/$168 within a year | AI Premium renamed Plus and the ladder gained a Plus rung | promos became standard pricing 2026-09 | Plus $20 to $22 in three months, plan replaced overnight | $8 to $12 with a new cap | $5 promo removed, $15 flagship standard | baseline 2026-09-26, heavy deprecation churn | fee flattened to 5.5% (2025-06), Business 8% added (2026-09) | Lite discontinued, Pro sold out, the Token Plan restructure replaced both | unchanged since tracking began (2026-09-26) | Lite announced in March, Plus observed by September | $20/$60 tiers replaced by a $30 pack |

## Reading the matrix

I read the billing-mechanics row first, because it decides who this provider is for: passthrough gateways meter reality, vendor plans sell a quota, and flat subscriptions sell a ceiling.
**The gateways (OpenRouter, Requesty, Zen) monetize a percentage, the vendor plans (GLM, Kimi, MiniMax, Qwen, and the consumer subscriptions) monetize commitment, and the community subs (NanoGPT, Synthetic, Chutes, Go) monetize the gap between list price and what self-hosted open models actually cost to serve.**
On price trajectories, only Requesty, Zen, and the Claude price tags have not moved, and Zen's baseline is one day old, so the stable-looking rows are the youngest ones.
The frontier-models row is the real segmentation: if your loop needs Claude, GPT, Gemini, or Grok, the flat open-model subscriptions are irrelevant and the choice is gateway versus vendor subscription.
The catches cluster into two kinds: mechanical limits you can engineer around (concurrency, windows, peak multipliers) and trust problems you cannot (quota draining, silent plan replacement, narrowed deals), and I weight the second kind higher.

## Choosing an access provider

- Default BYOK loop across many providers: OpenRouter for breadth, Requesty if EU residency or budget governance is required.
- First-party subscription loops: Claude plans, ChatGPT plans, Google AI plans, or SuperGrok, matched to the model family your daily driver uses.
- One vendor's models all day: that vendor's plan (GLM, Kimi, MiniMax, Qwen), after checking the peak-hour mechanics against your working hours.
- Open models at a flat ceiling: OpenCode Go or Synthetic for agent-shaped workloads, NanoGPT for breadth beyond coding, Chutes for the cheapest per-token open rates.
- Frontier models without a subscription: OpenCode Zen, paying the measured curation premium only where a mis-served provider would silently degrade your agent.
- Raw speed: Cerebras Code, when it is in stock and your context fits the window.

## Changes

- 2026-09-26 - Created with eleven columns when the owner-directed Model access category was seeded.
- 2026-09-26 - Extended from eleven to thirteen columns with ChatGPT plans and Claude plans on owner instruction, re-sorted; the vendor consumer subscriptions that carry Claude Code and Codex joined the category.
- 2026-09-26 - Extended from thirteen to sixteen columns with Qwen Coding Plan, Google AI plans, and SuperGrok on the owner's completeness question, re-sorted; every frontier vendor's subscription now has a column.

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
