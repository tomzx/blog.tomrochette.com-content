---
title: OpenCode Zen
created: 2026-09-26
updated: 2026-10-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, ai-gateway, pay-per-use]
readability: 3
audience_notes: >
  For engineers comparing pay-per-use model gateways for coding agents.
  Assumes familiarity with per-token API pricing.
---

OpenCode Zen is the OpenCode (Anomaly) team's curated pay-per-use AI gateway, one API key over a tested catalog that spans open models and the Claude, GPT, Gemini, and Grok lines, renamed OpenCode Console on the docs by the 2026-10-29 read while the /docs/zen/ URL and the zen/ legacy endpoints still serve.

## What it is

Zen (now branded Console) is a billing and routing gateway, not a model: you add credits, get a key, and call OpenAI-compatible, Anthropic-compatible, Google, or Responses endpoints, served under `opencode.ai/inference/...` on the current docs with the older `opencode.ai/zen/v1` base URL still accepted by third-party integrations.
The team benchmarks each model/provider pair and serves what passes, their answer to getting a degraded version of a model through a generic router.
It also sells to teams (workspaces, roles, member spending caps, model toggles, BYOK for OpenAI and Anthropic keys), and free stealth and promo models rotate through the catalog.

## Status

Active, with heavy catalog churn managed through a public deprecation table, workspaces free during the beta with team pricing unannounced, and a product rename in flight: the docs page now titles itself "OpenCode Console" and calls the gateway Console throughout (read 2026-10-29), while the /docs/zen/ URL, the Docker Agent integration doc, and the zen/ base URLs still carry the Zen name.
The Reddit thread "Opencode Zen is astoundingly more expensive than OpenRouter" (July 2026) is the sharpest public criticism and remains the note's key stress test.
**Zen sells curation and reliability, and community measurements plus today's catalog reads say that premium can exceed 3x the cheapest gateway on identical models.**

## Strengths

- Every endpoint is benchmarked for coding-agent use, so you avoid badly served providers.
- A stable of free models (ten free rows as of 2026-10-29: the Big Pickle stealth model, GLM-5.3-Flash Free, DeepSeek V4.1 Flash Free, Beam Free, Flint 40B Free, MiMo-V2.6-Flash Free, Nemotron 3 Ultra Free, Nemotron 3.5 Lightning Free, Nemotron 3.5 Super VL Free, and Jev 1.13 Free) with documented data caveats.
- Markups are claimed to be zero beyond the processing fee on credit purchases (4.6% + $0.31 per transaction as of 2026-10-29, up from 4.4% + $0.30).
- US- and EU-hosted per the docs as of 2026-10-11, with zero-retention on most models and exceptions listed per model.
- Same balance backs the Go subscription's overflow, and the key works from any agent.

## Cautions

- The July 2026 community test measured Zen at more than 4x OpenRouter on Kimi K2.6 and MiniMax M2.7; the gap has since narrowed on some models and widened on others, per model as of 2026-10-29: Zen lists GLM-5.3-Flash at $0.15/$0.50 where OpenRouter's catalog reads $0.0457/$0.0742 (3.3x input, 6.7x output), GLM-5.3 at $1.40/$4.40 against OpenRouter's $0.0699/$1.40, while MiniMax M2.7 has converged to identical $0.30/$1.20 and Kimi K2.6 sits at $0.95/$4.00 against $0.65/$3.41.
- Auto-recharge buys credits when the balance runs low, last verified at $20 per top-up below a $5 floor; the current console billing page renders client-side and no longer states the amounts in fetchable text.
- Deprecated models vanish on published dates (DeepSeek V4 Flash deprecated October 26, 2026, per the current table), so configs need migrations, and free stealth models may use your data to improve the model during their free window.

## Pricing

Pay-as-you-go per 1M tokens, as of 2026-10-29: GLM-5.3 $1.40/$4.40, GLM-5.3-Flash $0.15/$0.50, Kimi K3 $3/$15, Qwen3.7 Plus $0.40/$1.60, DeepSeek V4.1 Flash $0.30/$1.20, MiniMax M3 $0.30/$1.20.
Frontier lines: Claude Sonnet 5 $2/$10, Claude Opus 5.5 $4/$20, Claude Fable 5.1 $10/$50, GPT 5.5 $5/$30, GPT 6 Astra $10/$50, GPT 6 Sol $2/$10, GPT 6.1 Sol $2/$10, Gemini 3.8 Flash $1.50/$7.50, Grok 4.7 $2/$6, with long-context surcharge tiers documented per model.
Mistral Large 4 carries a 50%-off promo row ($0.68/$2.09, struck from $1.36/$4.18), Gemini 4 Argon a second one ($2.00/$10.00, struck from $4.00/$20.00, through November 30, 2026), and Jev 1.13 charges $0.042 per input with free output.
Ten models are free as of 2026-10-29, down from fourteen at the 2026-10-14 read: the Big Pickle stealth model, GLM-5.3-Flash Free and DeepSeek V4.1 Flash Free (both newly free, zero-retention providers), Beam Free, Flint 40B Free, MiMo-V2.6-Flash Free, three Nemotron free rows, and Jev 1.13 Free; Space Bunny and Cat Jam are gone from the catalog.
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

## See also

- [OpenCode Go](../opencode-go/index.md) - the sibling subscription that overflows into this balance.
- [OpenRouter](../openrouter/index.md) - the broader, usually cheaper gateway this one is measured against.
- [OpenCode](../../harnesses/opencode/index.md) - the harness Zen is the default recommended provider for.
- [Model provider feature matrix](../../model-provider-feature-matrix/index.md) - where Zen sits among access providers.

## References

- https://opencode.ai/docs/zen/ - per-model price table, free models, auto-recharge, deprecations, privacy, now branded OpenCode Console (200, last updated 2026-10-10, re-fetched 2026-10-11 and 2026-10-14 with the Gemini 4 Argon promo row and Cat Jam Free present; re-fetched 2026-10-29 reading the Console rename, the 4.6% + $0.31 processing fee, the ten free rows, and the DeepSeek V4 Flash October 26 deprecation).
- https://docs.docker.com/ai/docker-agent/providers/opencode-zen/ - third-party integration doc, Zen vs Go billing table (200; re-fetched 2026-10-29, still titled OpenCode Zen with the opencode.ai/zen/v1 base URL and the legacy opencode-zen provider id accepted).
- https://www.reddit.com/r/opencodeCLI/comments/1syog9v/opencode_zen_is_astoundingly_more_expensive_than/ - critical 4x price claim vs OpenRouter (direct fetch 403; content read via search).
- https://costgoat.com/pricing/openrouter/ - OpenRouter per-model prices used for cross-gateway comparison (200, as of 2026-09-25; re-fetched 2026-10-29, updated October 28, with GLM-5.3-Flash at $0.15/$0.50 against the catalog's current $0.0457/$0.0742, so the catalog API was used for the caution instead).
- https://opencode.ai/docs/go - shared balance and "Use balance" fallback mechanics (200; re-fetched 2026-10-29).
- https://www.truefoundry.com/blog/openrouter-pricing - OpenRouter fee structure used as the price counterpoint (200; re-fetched 2026-10-29, its BYOK rows still carrying the retired request-count framing).
