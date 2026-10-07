---
showArticleList: false
title: Model access
created: 2026-09-26
visible: true
status: in progress
tags: [agents, model-access]
readability: 3
---

The layer that sells access to models themselves: gateways and routers taking a percentage or, in Vercel's case, nothing on the token itself, vendor plans selling a quota (including the consumer subscriptions that carry Claude Code and Codex), flat subscriptions selling a ceiling, and the self-hosted software (LiteLLM, Bifrost, Ollama, Magnitude, Plano, llamafile) that routes, serves, or distributes the same access for free.
Editors and harnesses live in their own categories; this is where the token bill gets paid.

- [Bifrost](bifrost/index.md) - Maxim's self-hosted Apache-2.0 Go gateway unifying 20-plus providers with failover, budgets, and an MCP gateway, the performance challenger to LiteLLM, 8.6k stars.
- [Cerebras Code](cerebras-code/index.md) - wafer-scale inference sold as speed, $50/$200 per month, currently sold out.
- [ChatGPT plans](chatgpt-plans/index.md) - OpenAI's subscription ladder from Go $8 to Pro tiers up to $500 per month, every tier carrying Codex.
- [Chutes](chutes/index.md) - decentralized inference with pay-as-you-go plus $10/$20 subscriptions capped at 5x pay-as-you-go value.
- [Claude plans](claude-plans/index.md) - Anthropic's Free/Pro/Max subscriptions, the only non-API way to run Claude Code, from $20 to $200 per month.
- [Experiential](experiential/index.md) - a YC-backed Apache-2.0 gateway at zero markup that mines agent traces to train routers and, on enterprise, a model you own.
- [GLM Coding Plan](glm-coding-plan/index.md) - Z.AI's flat monthly quota for the GLM line, from $18, restructured twice since launch.
- [Google AI plans](google-ai-plans/index.md) - the Google Plus/Pro/Ultra ladder carrying Antigravity and Gemini CLI, with credits over rate limits.
- [Kimi Code](kimi-code/index.md) - Moonshot's membership ladder for coding, $19 to $199 monthly with Code from the second tier.
- [LiteLLM](litellm/index.md) - a self-hosted MIT gateway unifying 100+ provider APIs behind one OpenAI-compatible endpoint, with routing, budgets, and spend tracking.
- [llamafile](llamafile/index.md) - Mozilla's single-file LLM distribution folding llama.cpp and Cosmopolitan Libc into one cross-platform executable, the family's distribute-instead-of-serve answer, 26.2k stars.
- [LLM Gateway](llm-gateway/index.md) - an open-source gateway charging 5% on credit top-ups with free BYOK, plus DevPass flat-rate coding plans from $29.
- [Magnitude](magnitude/index.md) - a self-optimizing local inference engine (YC S25) that tunes its kernels on your device, free under Apache-2.0.
- [MiniMax Coding Plan](minimax-coding-plan/index.md) - token-quota subscriptions for the MiniMax line, $22 to $132 per month, born from a silent plan replacement.
- [NanoGPT](nanogpt/index.md) - the community aggregator: hundreds of routes pay-as-you-go plus a $12 open-weight subscription.
- [Ollama](ollama/index.md) - the free local runtime and registry for open models, now paired with paid cloud tiers.
- [OpenCode Go](opencode-go/index.md) - the OpenCode team's $10/month open-model token pack, usable from any agent.
- [OpenCode Zen](opencode-zen/index.md) - the OpenCode team's curated pay-per-use gateway over benchmarked endpoints.
- [OpenRouter](openrouter/index.md) - the largest model gateway, passthrough tokens plus a 5.5% credit fee, now joining Stripe.
- [Plano](plano/index.md) - the Envoy-based self-hosted LLM gateway and agent data plane behind the Arch-Router routers, acquired by DigitalOcean in April 2026.
- [Qwen Coding Plan](qwen-coding-plan/index.md) - Alibaba Cloud's flat quota for the Qwen line plus bundled rivals, in transition to a Token Plan.
- [Requesty](requesty/index.md) - EU-residency gateway charging a flat 5% markup on upstream spend.
- [SuperGrok](supergrok/index.md) - xAI's subscription ladder from $30 to $300, one shared weekly pool across Grok chat, Grok Build, and API.
- [Synthetic](synthetic/index.md) - a flat $30/month subscription for open-weight coding LLMs aimed at agent users.
- [Vercel AI Gateway](vercel-ai-gateway/index.md) - Vercel's hosted gateway at provider list prices with 0% token markup, one-command setup for 29 coding agents, and no flat tier.

Its members are compared on shared rows in the [Model Access Feature Matrix](model-access-feature-matrix/index.md).

## Changes

- 2026-09-26 - Added Cerebras Code.
- 2026-09-26 - Added Chutes.
- 2026-09-26 - Added GLM Coding Plan.
- 2026-09-26 - Added Kimi Code.
- 2026-09-26 - Added MiniMax Coding Plan.
- 2026-09-26 - Added NanoGPT.
- 2026-09-26 - Added OpenCode Go.
- 2026-09-26 - Added OpenCode Zen.
- 2026-09-26 - Added OpenRouter.
- 2026-09-26 - Added Requesty.
- 2026-09-26 - Added Synthetic.
- 2026-09-26 - Added ChatGPT plans.
- 2026-09-26 - Added Claude plans.
- 2026-09-26 - Added Google AI plans.
- 2026-09-26 - Added Qwen Coding Plan.
- 2026-09-26 - Added SuperGrok.
- 2026-09-27 - Added LiteLLM.
- 2026-09-27 - Added Ollama.
- 2026-09-27 - Added Experiential.
- 2026-10-04 - Added LLM Gateway.
- 2026-10-06 - Added Magnitude.
- 2026-10-06 - Added Vercel AI Gateway.
- 2026-10-07 - Added Plano.
- 2026-10-07 - Added Bifrost.
- 2026-10-07 - Added llamafile.
