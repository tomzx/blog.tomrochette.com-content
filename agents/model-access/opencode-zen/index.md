---
title: OpenCode Zen
created: 2026-09-26
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.4, llm=glm-5.3-flash, model-access, ai-gateway, pay-per-use]
readability: 3
audience_notes: >
  For engineers comparing pay-per-use model gateways for coding agents.
  Assumes familiarity with per-token API pricing.
---

OpenCode Zen is the OpenCode (Anomaly) team's curated pay-per-use AI gateway, one API key over a tested catalog that spans open models and the Claude, GPT, Gemini, and Grok lines, renamed OpenCode Console on the docs by the 2026-10-29 read while the /docs/zen/ URL and the zen/ legacy endpoints still serve.
By the 2026-11-27 read the /docs/zen/ URL resolves to the Console models page at opencode.ai/docs/console/models/, which states that free-tier chat models require OpenCode, with paid models or Go working from other clients.

## What it is

Zen (now branded Console) is a billing and routing gateway, not a model: you add credits, get a key, and call OpenAI-compatible, Anthropic-compatible, Google, or Responses endpoints, served under `opencode.ai/inference/...` on the current docs with the older `opencode.ai/zen/v1` base URL still accepted by third-party integrations.
The team benchmarks each model/provider pair and serves what passes, their answer to getting a degraded version of a model through a generic router.
It also sells to teams (workspaces, roles, member spending caps, model toggles, BYOK for OpenAI and Anthropic keys), and free stealth and promo models rotate through the catalog.

## Status

Active, with heavy catalog churn managed through a public deprecation table, workspaces free during the beta with team pricing unannounced, and a product rename in flight: the docs page now titles itself "OpenCode Console" and calls the gateway Console throughout (read 2026-10-29), while the /docs/zen/ URL, the Docker Agent integration doc, and the zen/ base URLs still carry the Zen name.
By 2026-11-27 the docs live at opencode.ai/docs/console/models/ and call the product Console throughout, while the Docker integration doc and the zen/ base URLs keep the Zen name.
The Reddit thread "Opencode Zen is astoundingly more expensive than OpenRouter" (July 2026) is the sharpest public criticism and remains the note's key stress test.
**Zen sells curation and reliability, and community measurements plus today's catalog reads say that premium can exceed 3x the cheapest gateway on identical models.**

## Strengths

- Every endpoint is benchmarked for coding-agent use, so you avoid badly served providers.
- A stable of free models (twelve free rows as of 2026-11-27, thirteen at the 2026-11-08 read: the Big Pickle, Tidepool Alpha Free, Seaglass Alpha Free, and Iceman Free stealth models, DeepSeek V4.1 Flash Free, Beam Free, Flint 40B Free, Hy4 flash Free, MiMo-V2.6-Flash Free, Nemotron 3.5 Lightning Free, Nemotron 3.5 Super VL Free, and Jev 1.13 Free) with documented data caveats, though free-tier chat models now require OpenCode.
- Markups are claimed to be zero beyond the processing fee on credit purchases (4.6% + $0.31 per transaction as of 2026-10-29, up from 4.4% + $0.30).
- US- and EU-hosted per the docs as of 2026-10-11, with zero-retention on most models and exceptions listed per model.
- Same balance backs the Go subscription's overflow, and the key works from any agent.

## Cautions

- The July 2026 community test measured Zen at more than 4x OpenRouter on Kimi K2.6 and MiniMax M2.7; per the OpenRouter catalog API as of 2026-11-27 the gap depends on the model: Zen's GLM 5.3 Flash sits at the same $0.15/$0.50 as OpenRouter's listing (the 4.5x and 6.0x gap of 2026-11-08 closed on the listing side), GLM 5.3 lists at $1.40/$4.40 against OpenRouter's $0.0699/$1.40 (20x input, 3.1x output, and 8x and 1.3x on the $0.56/$1.76 promo row), Kimi K2.6 at $0.95/$4.00 against $0.65/$3.41 (1.5x and 1.2x), while MiniMax M2.7 now reads cheaper on Zen at $0.30/$1.20 against OpenRouter's $0.60/$1.80.
- Auto-recharge buys credits when the balance runs low, last verified at $20 per top-up below a $5 floor; the current console billing page renders client-side and no longer states the amounts in fetchable text.
- Deprecated models vanish on published dates (DeepSeek V4 Flash on October 26, 2026, GLM 5.1 and 5.2 on November 19, 2026, and LongCat-2.0 on November 22, 2026, per the 2026-11-27 table, which dropped the Pulse Alpha Free row after its November 6 date), so configs need migrations, and free stealth models may use your data to improve the model during their free window.

## Pricing

Pay-as-you-go per 1M tokens, as of 2026-11-27: GLM 5.3 $1.40/$4.40 list, GLM 5.3 Flash $0.15/$0.50, Kimi K3 $3/$15, Kimi K3.1 Pro $2/$10, Qwen3.6 Plus $0.50/$3.00 and Qwen3.5 Plus $0.20/$1.20 (Qwen3.7 Plus left the table since 2026-10-29), Qwen3.8 Max $2/$6 and Qwen3.8 Flash $0.15/$0.47, DeepSeek V4.1 Flash $0.30/$1.20 list, DeepSeek V4 Pro $1.74/$3.48, MiniMax M3 $0.30/$1.20.
Frontier lines: Claude Sonnet 5 $2/$10, Claude Opus 5.5 $4/$20, Claude Fable 5.1 $10/$50, GPT 5.5 $5/$30, GPT 6 Astra $10/$50, GPT 6 Sol $2/$10, GPT 6.1 Sol $2/$10, GPT 5.6 Terra $2/$12, Gemini 3.8 Flash $1.50/$7.50 list, Grok 4.7 $2/$6, with long-context surcharge tiers documented per model (the GPT rows doubling above 272K tokens); Claude Sonnet 5.5 ($2/$10), Claude Fable 5.2 ($8/$40), and GPT 6.2 Astra ($8/$40) joined the table between the 2026-11-08 and 2026-11-27 reads.
Mistral Large 4 carries a 50%-off promo row ($0.68/$2.09, struck from $1.36/$4.18), Gemini 4 Argon a second one ($2.00/$10.00, struck from $4.00/$20.00, through November 30, 2026), and Jev 1.13 charges $0.042 per input with free output, Jev 1.14 the same; three more promo rows stood at the 2026-11-27 read, GLM 5.3 at 60% off ($0.56/$1.76), DeepSeek V4.1 Flash at 60% off ($0.12/$0.48), and Gemini 3.8 Flash at 50% off ($0.75/$3.75), each striking its unchanged list price.
Twelve models are free as of 2026-11-27, down from thirteen at the 2026-11-08 read: the Big Pickle, Tidepool Alpha Free, Seaglass Alpha Free, and Iceman Free stealth models, DeepSeek V4.1 Flash Free, Beam Free, Flint 40B Free, Hy4 flash Free, MiMo-V2.6-Flash Free, two Nemotron 3.5 free rows, and Jev 1.13 Free; Inkling 2 Small Free, Crouton Alpha Free, GLM 5.3 Flash Free, and the Nemotron 3 Ultra free row are gone, and the docs now state that free-tier chat models require OpenCode, with paid models or Go working from other clients.
Credit purchases carry a processing fee of 4.6% + $0.31 per the docs callout (4.4% + $0.30 before), stated as the only charge beyond token rates, and OpenCode itself uses low-cost models to generate session titles on your bill.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-26 | Pay-per-use catalog | Baseline: per-model rates as published (GLM-5.3 $1.40/$4.40, Kimi K3 $3/$15, Jev 1.13 $0.042 in) | https://opencode.ai/docs/zen/ |
| 2026-10-29 (observed) | Processing fee | Credit-purchase processing fee rose from 4.4% + $0.30 to 4.6% + $0.31 per transaction, still stated as the only charge beyond token rates; token rates unchanged | https://opencode.ai/docs/zen/ |

## Compared to

[OpenCode Go](../opencode-go/index.md) is the sibling subscription: $10/month for capped open-model usage, no frontier models, same balance; choose it when you want a ceiling.
[OpenRouter](../openrouter/index.md) is the breadth play: hundreds of models, passthrough pricing, 5.5% credit fee; choose it when price per token on open models matters more than curation.
Holding your own provider keys is cheapest for a single provider, and Zen's BYOK only covers OpenAI and Anthropic.

## Bottom line

Recommended for OpenCode-centric developers who want vetted endpoints, free models to fall back on, and US-hosted zero-retention.
Not for price-sensitive, high-volume runs on open models, where OpenRouter wins on raw per-token cost.
My disagreeable claim: the curation premium is worth paying only when a mis-served provider would silently degrade your agent, and most coding work is not that sensitive.

## Changes

- 2026-09-26 - Created.
- 2026-09-29 - Catalog check: the free roster grew from nine to ten models (LongCat 2.5 Preview Free joined), Claude Fable 5.1 and the GPT 6 line appeared on the price table, and the docs republished 2026-09-28; every previously listed per-token rate is unchanged.
- 2026-10-04 - Free roster moved from ten to twelve models on the live price table (Fledge Alpha Free newly listed as limited-time); every per-token rate re-verified unchanged.
- 2026-10-06 - Converted the Compared-to cross-references from plain-text paths into working links.
- 2026-10-07 - Catalog check: the price table's free rows count thirteen (from twelve recorded 2026-10-04, with Nemotron 3.5 Lightning Free and Muse Spark 1.3 Contributor Free now on the table), Mistral Large 4 gained a 50%-off promo row, and the docs now state US and EU hosting where the note said US-hosted; every per-token rate re-verified unchanged.
- 2026-10-14 - Catalog check: the free roster moved to fourteen rows with Cat Jam Free joining as a third stealth free model, and Gemini 4 Argon gained a 50%-off promo row (through November 30, 2026) beside Mistral Large 4's; every previously listed per-token rate re-verified unchanged.
- 2026-10-29 - Rotation re-verification with a product rename and a fee rise: the docs now brand the gateway OpenCode Console (endpoints moved to opencode.ai/inference/... with the zen/ legacy URLs still serving per the Docker integration doc), the credit-purchase processing fee rose from 4.4% + $0.30 to 4.6% + $0.31, the free roster fell from fourteen rows to ten (Space Bunny and Cat Jam gone, GLM-5.3-Flash and DeepSeek V4.1 Flash newly free, Flint 40B and a third Nemotron row in), the GLM-5.3-Flash and GLM-5.3 price-gap caution re-based onto today's OpenRouter catalog reads (the gap widened on GLM while MiniMax M2.7 converged), and DeepSeek V4 Flash's October 26 deprecation joined the table; every cited URL re-fetched live this run except the Reddit thread (documented 403), price history row appended.
- 2026-11-08 - Rotation re-verification with catalog churn: the free roster grew from ten rows to thirteen (Iceman Free, Inkling 2 Small Free, and Crouton Alpha Free joined, Inkling's provider retaining data and may train on it and region-restricted), Qwen3.7 Plus left the price table with Qwen3.6 Plus ($0.50/$3.00) and Qwen3.5 Plus ($0.20/$1.20) replacing it, the deprecation table gained Pulse Alpha Free (November 6, 2026), and the price-gap caution re-based onto fresh OpenRouter catalog reads (GLM-5.3-Flash input gap widened to 4.5x, MiniMax M2.7 de-converged to 1.4x); the processing fee (4.6% + $0.31), every previously listed per-token rate, and the Console branding re-verified unchanged; every cited URL re-fetched live this run except the Reddit thread (403 again).
- 2026-11-27 - Rotation re-verification with catalog churn: the docs page moved to opencode.ai/docs/console/models/ (the /docs/zen/ URL resolving there, the Docker integration doc still titled OpenCode Zen), the free roster fell from thirteen rows to twelve (Inkling 2 Small Free, Crouton Alpha Free, GLM 5.3 Flash Free, and Nemotron 3 Ultra Free gone; Tidepool Alpha Free, Seaglass Alpha Free, and Hy4 flash Free in) and the docs now state that free-tier chat models require OpenCode, three promo rows were recorded (GLM 5.3 at 60% off, DeepSeek V4.1 Flash at 60% off, Gemini 3.8 Flash at 50% off, each against an unchanged list price), Kimi K3.1 Pro, Qwen3.8 Max, Qwen3.8 Flash, Claude Sonnet 5.5, Claude Fable 5.2, and GPT 6.2 Astra joined the table and the GPT rows gained a 272K-token tier boundary, the deprecation table gained GLM 5.1 and 5.2 (November 19, 2026) and LongCat-2.0 (November 22, 2026) and dropped Pulse Alpha Free, and the price-gap caution re-based onto fresh OpenRouter catalog reads (GLM 5.3 Flash now equal at $0.15/$0.50, MiniMax M2.7 cheaper on Zen, GLM 5.3 and Kimi K2.6 still dearer); the processing fee (4.6% + $0.31), every previously listed per-token rate, and the Mistral Large 4 and Gemini 4 Argon promo rows re-verified unchanged, so no price history row; every cited URL re-fetched live this run except the Reddit thread (403 again), with costgoat no longer carrying a GLM-5.3-Flash row and the Go docs no longer carrying the "Use balance" phrase.

## See also

- [OpenCode Go](../opencode-go/index.md) - the sibling subscription that overflows into this balance.
- [OpenRouter](../openrouter/index.md) - the broader, usually cheaper gateway this one is measured against.
- [OpenCode](../../harnesses/opencode/index.md) - the harness Zen is the default recommended provider for.
- [Model provider feature matrix](../../model-provider-feature-matrix/index.md) - where Zen sits among access providers.

## References

- https://opencode.ai/docs/zen/ - per-model price table, free models, auto-recharge, deprecations, privacy, now branded OpenCode Console (200, last updated 2026-10-10, re-fetched 2026-10-11 and 2026-10-14 with the Gemini 4 Argon promo row and Cat Jam Free present; re-fetched 2026-10-29 reading the Console rename, the 4.6% + $0.31 processing fee, the ten free rows, and the DeepSeek V4 Flash October 26 deprecation; re-fetched 2026-11-08 with thirteen free rows (Iceman Free, Inkling 2 Small Free, Crouton Alpha Free new), Qwen3.6 Plus and Qwen3.5 Plus replacing Qwen3.7 Plus, the Pulse Alpha Free November 6 deprecation, and the fee callout unchanged; re-fetched 2026-11-27 at its new address opencode.ai/docs/console/models/, the /docs/zen/ URL resolving there, reading twelve free rows, the free-tier-requires-OpenCode rule, the GLM 5.3, DeepSeek V4.1 Flash, and Gemini 3.8 Flash promo rows, the 272K-token GPT tiers, the re-based deprecation table, and the fee callout unchanged).
- https://docs.docker.com/ai/docker-agent/providers/opencode-zen/ - third-party integration doc, Zen vs Go billing table (200; re-fetched 2026-10-29, still titled OpenCode Zen with the opencode.ai/zen/v1 base URL and the legacy opencode-zen provider id accepted; re-fetched 2026-11-08 unchanged in the cited respects, now also documenting the x-opencode-session header Docker Agent sends; re-fetched 2026-11-27 unchanged, still titled OpenCode Zen with the opencode.ai/zen/v1 base URL and the x-opencode-session header present).
- https://www.reddit.com/r/opencodeCLI/comments/1syog9v/opencode_zen_is_astoundingly_more_expensive_than/ - critical 4x price claim vs OpenRouter (direct fetch 403 again 2026-11-08 and 2026-11-27; content read via search).
- https://openrouter.ai/api/v1/models - the OpenRouter catalog API grounding the caution's comparison reads (200, 2026-11-08: z-ai/glm-5.3-flash $0.0335/$0.083, z-ai/glm-5.3 $0.0699/$1.40, minimax/minimax-m2.7 $0.21/$0.84, moonshotai/kimi-k2.6 $0.65/$3.41 per 1M tokens; re-fetched 2026-11-27: z-ai/glm-5.3-flash $0.15/$0.50, z-ai/glm-5.3 $0.0699/$1.40, minimax/minimax-m2.7 $0.60/$1.80, moonshotai/kimi-k2.6 $0.65/$3.41).
- https://costgoat.com/pricing/openrouter/ - OpenRouter per-model prices used for cross-gateway comparison (200, as of 2026-09-25; re-fetched 2026-10-29, updated October 28, with GLM-5.3-Flash at $0.15/$0.50 against the catalog's current $0.0457/$0.0742, so the catalog API was used for the caution instead; re-fetched 2026-11-08, updated November 6, still reading GLM-5.3-Flash at $0.15/$0.50, so the catalog API remains the caution's source; re-fetched 2026-11-27 as a pricing calculator page with no GLM-5.3-Flash row in its text).
- https://opencode.ai/docs/go - shared balance and "Use balance" fallback mechanics (200; re-fetched 2026-10-29; re-fetched 2026-11-08; re-fetched 2026-11-27 with the workspace balance wording and the Go $10 and Go Plus $40 prices present and the "Use balance" phrase gone).
- https://www.truefoundry.com/blog/openrouter-pricing - OpenRouter fee structure used as the price counterpoint (200; re-fetched 2026-10-29, its BYOK rows still carrying the retired request-count framing; re-fetched 2026-11-08, updated October 15, the same framing; re-fetched 2026-11-27, still updated October 15, 2026, with the 5.5% credit purchase fee and the same framing).
