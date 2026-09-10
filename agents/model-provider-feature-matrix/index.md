---
title: "Model Provider Feature Matrix"
created: 2026-09-08
updated: 2026-09-10
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, model-selection, llm-pricing]
readability: 3
audience_notes: >
  Engineers choosing which model vendor to point their coding agent at, comparing the providers as bundles rather than single models.
  Assumes you know what input, output, and cached tokens cost and what a prompt cache does.
---

This matrix compares the seven model providers behind every model in the [Model Selection guide](../model-selection-for-coding-tasks/index.md), provider by provider, so the vendor choice is as visible as the model choice.
Everything below was re-verified against live sources on 2026-09-10: each cell traces to the guide's verified pricing table, to provider pages fetched during this run, or to the models.dev list reference the guide uses for model ids, release dates, and context windows.

**Provider choice is a bundle decision, list price, cache discount, batch policy, context flatness, weights, and where your subscription does and does not transfer, and the challengers win that bundle on every axis except subscriptions.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the provider's canonical pricing page; every cell traces to the guide or to a source cited in its references.

## The matrix

| Provider | [Alibaba (Qwen)](https://help.aliyun.com/zh/model-studio/billing-for-model-studio) | [Anthropic (Claude)](https://docs.claude.com/en/docs/about-claude/pricing) | [DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/) | [Google (Gemini)](https://cloud.google.com/vertex-ai/generative-ai/pricing) | [Moonshot AI (Kimi)](https://platform.kimi.ai/docs/pricing/chat-k3) | [OpenAI (GPT)](https://platform.openai.com/docs/pricing) | [Zhipu (GLM)](https://docs.z.ai/guides/overview/pricing) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flagship model | Qwen3.8-Max, $2 / $6 | Claude Fable 5.1, $10 / $50 | DeepSeek V4 Pro, $1.32 / $3.96 peak, routes to V4.1-Flash from 2026-09-14 | Gemini 3.1 Pro Preview, $2 / $12 | Kimi K3, $3 / $15 | GPT-6 Astra, $10 / $50 | GLM-5.3, $1.40 / $4.40 |
| Workhorse model | Qwen3.8-Max doubles as the workhorse | Claude Sonnet 5, $2 / $10 | deepseek-flash (V4.1-Flash), $0.30 / $1.20 peak | Gemini 3.1 Pro Preview, $2 / $12 | kimi-k2.7-code, $0.71 / $3.50 on OpenRouter | gpt-5.6-terra, $2 / $12 | GLM-5.3 covers the class at $1.40 / $4.40 |
| Cheap model | Qwen3.8-Flash, $0.15 / $0.47 | Claude Haiku 4.5, $1 / $5 | deepseek-flash doubles as the cheap tier, $0.15 / $0.60 off-peak | Flash-Lite $0.25 / $1.50, 3.6 Flash $0.75 intro | k2.7-code doubles as the cheap tier | gpt-5.6-luna, $0.20 / $1.20 | GLM-5.3-Flash, $0.15 / $0.50, GLM-4.7-Flash free |
| Coding-specialized model | ? none in this guide (the open Coder family is separate) | ✗ none, the general lineup carries coding | ✗ none in the guide | ✗ none in the guide | ✓ kimi-k2.7-code | ✓ gpt-5.3-codex, $1.75 / $14 | ✗ none in the guide |
| Cached input discount | ~ discount stated, rate unpublished | ✓ one tenth, the Fable pair at one fortieth | ✓ about one fiftieth on Flash, the deepest | ✓ about one tenth | ✓ one tenth on K3, one fifth on k2.7-code | ✓ about one tenth | ✓ about one fifth |
| Long-context policy | ✓ 1M flat | ✓ 1M flat from Claude 4.6 onward | ✓ 1M flat, 384K max output | ~ doubles past thresholds, Pro beyond 200K | ~ K3 flat 1M, k2.7-code 256K | ~ doubles past thresholds | ✓ 1M flat |
| Batch or time discounts | ~ batch half price on Max | ✓ batch half price | ~ off-peak half price instead of batch | ✓ batch half price | ? not stated | ✓ batch half price | ? not stated |
| Live pricing windows | ~ 1M-token free quota for new accounts, 90 days | ~ Sonnet 5's planned increase was cancelled | ~ off-peak is standing policy; V4 Pro routes to Flash rates from 2026-09-14 | ~ Flash intro rate ends 2026-12-31 | ~ HighSpeed variant at $1.90 / $8.00 | ~ Sol promo through 2026-11-21 | ✓ none; the 50% promo ended 2026-09-09 into the $0.15 / $0.50 list |
| Weights | ✓ open weights (27B and Flash-Next) | ✗ closed | ✓ open weights | ✗ closed | ✓ open weights (K3, K2.7) | ✗ closed | ✓ open weights |
| Subscription includes an agent | ? none verified | ✓ Claude Code from Pro $20 to Max 20x $200 | ✗ API and BYOK only | ~ the Antigravity platform is free | ~ Kimi OAuth reuse via Kimi Code | ✓ Codex from ChatGPT Free tier up | ~ coding plans from $18/month |
| BYOK harness fit | ~ OpenAI-compatible, rides OpenRouter or any compatible endpoint | ~ subscription does not transfer to third-party harnesses | ✓ native OpenCode provider, plus an Anthropic-format endpoint | ? not verified here | ✓ native OpenCode provider | ~ API key works everywhere, subscription locked to Codex | ✓ native OpenCode provider |

## Reading the matrix

I read this table as a bundle scorecard rather than a price list, because the rows move together in ways the model-level table hides.
**The big three monetize closed frontier weights plus subscriptions, and the four challengers monetize cheap tokens plus open weights, with almost no overlap in which rows they win.**
On the price rows the challengers sweep: every challenger flagship costs less out than the big-three workhorses, and Zhipu's free GLM-4.7-Flash has no big-three analogue at any price.
On the policy rows the field is closer than list prices suggest, and this is the part I check before switching: DeepSeek's cache discount is the deepest at about one fiftieth on Flash, Alibaba leaves its cache rate unpublished, and batch is half price at the big three and Qwen but unverified at Moonshot and Zhipu.
Long context splits cleanly by flatness: Anthropic, DeepSeek, Alibaba, Moonshot K3, and Zhipu keep 1M pricing flat, while OpenAI and Google double past thresholds, which decides whole-repository prompting before any model-quality question.
The weights row is the quiet differentiator: open weights from Alibaba, DeepSeek, Moonshot, and Zhipu mean a private deployment path the closed big three do not offer at all.
The subscription row runs the other way: only OpenAI and Anthropic ship a first-party agent on subscription, and Anthropic's is the one that explicitly does not transfer to third-party harnesses.

## Choosing between providers

- Default workhorse loop: OpenAI, Anthropic, and Google price identically at the tier, so pick by harness fit and let the challenger prices below pressure that default yearly.
- Price-floor BYOK loops: DeepSeek and Zhipu, with Alibaba close behind at flagship quality for $6 out.
- Flat 1M context: Anthropic, DeepSeek, Alibaba, Moonshot K3, and Zhipu, the five vendors that keep whole-repository reads predictable.
- Coding-specialized spend: Moonshot's k2.7-code or OpenAI's gpt-5.3-codex, the only two columns with a model built for the job.
- Weights you can host: Alibaba, DeepSeek, Moonshot, or Zhipu, and none of the big three at any price.
- Subscription-first teams: OpenAI or Anthropic, and read the transfer row before assuming the subscription follows your harness.

## See also

- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the model-level pricing table every cell here traces to
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the client side of the same purchase, capability by capability
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the four-layer map that puts model vendors in context
- [Kimi Code](../kimi-code/index.md) - a vendor building its own harness to sell its own tokens
- [OpenCode](../opencode/index.md) - the lean BYOK harness the challenger provider columns ride

## References

- https://platform.openai.com/docs/pricing - GPT-5.6 family, gpt-5.3-codex, and GPT-6 Astra prices, batch discount, long-context doubling (verified 2026-09-10)
- https://docs.claude.com/en/docs/about-claude/pricing - Claude lineup prices, cache multipliers, 1M-context policy (verified 2026-09-10)
- https://cloud.google.com/vertex-ai/generative-ai/pricing - Gemini 3 family prices, intro windows, long-context and batch rates (verified 2026-09-10)
- https://help.aliyun.com/zh/model-studio/billing-for-model-studio - Qwen3.8-Max and Qwen3.8-Flash official prices, batch half price, cache discount, free quota (fetched 2026-09-10)
- https://api-docs.deepseek.com/news/news260910 - the 2026-09-10 V4.1-Flash release and V4 Pro routing announcement behind the DeepSeek column's workhorse and windows cells (fetched 2026-09-10)
- https://openrouter.ai/api/v1/models - USD international listings for the Qwen pair and kimi-k2.7-code (fetched 2026-09-10)
- https://models.dev - the community model list reference: model ids, release dates, and context windows behind the lineup (fetched 2026-09-10)
