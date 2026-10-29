---
title: OpenCode Go
created: 2026-09-26
updated: 2026-10-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, coding-subscription, open-models]
readability: 3
audience_notes: >
  For engineers choosing how to pay for coding models.
  Assumes you know what an LLM API provider is and how coding agents consume one.
---

OpenCode Go is a subscription from the OpenCode (Anomaly) team that bundles access to a curated set of open coding models at $10/month, with a $40/month Go Plus tier and a $20-per-member Go Teams tier above it, usable from OpenCode or any compatible coding agent.

## What it is

Go sells model access, not an editor or a harness.
You subscribe, copy an API key, and point any agent at OpenAI-compatible, Anthropic-compatible, or Responses endpoints under `opencode.ai/zen/go/v1`.
The lineup is 30 curated coding models on the docs page as of 2026-10-29 (Grok 4.7, the GLM-5.3 and 5.2 lines, Kimi K3.1 Pro/K3/K2.7, Claude Haiku 5.5, Gemini 4 Argon at a 50% launch discount through November 30, the GPT 6 and 5.6 Luna pair, Qwen3.8, the DeepSeek V4 family, MiniMax M3 and M3.1, MiMo, LongCat-2.0, Hy3, Hy4 preview, and Step 5 Preview now paid), matching the product page's "View all 30 models" for the first time since September, with Beam Free and Iceman Contributor Free the current limited-time free models and only one member per workspace holding a personal subscription.

## Status

Active and changing fast.
The OpenCode repo shows about 208K GitHub stars on the product page footer as of 2026-10-11, and the plan has grown from a three-model Beta in March 2026 to 30 docs-listed models across three plans: Go $10, Go Plus $40, and Go Teams at $20 per member (added by the 2026-10-29 docs read, each member getting their own limits plus $5 more per model, and starting with Extra Usage on).
Churn is constant: GPT 6 Luna arrived 2026-09-22, Kimi K3.1 Pro and Gemini 4 Argon joined by 2026-10-29, Space Bunny Free and Cat Jam Free have left, and the docs-versus-product-page model-count mismatch that ran since September closed at 30 on 30.
**Go converts $10 into up to $60 of metered usage per month, Go Plus converts $40 into up to $180, and that ratio is the entire value proposition.**

## Strengths

- The $60 monthly usage value costs $10, up to 6x leverage if you max it.
- Models are benchmarked for agentic coding before inclusion, per the team.
- Works with any agent; Claude Code, Codex, Hermes, Pi, jcode, ZCode, and Kilo Code CLI are validated clients.
- Dollar-denominated windows make the bill predictable, free models stay available after limits, and "Use balance" falls back to your Zen balance instead of hard-stopping requests.
- Most models run with zero retention and no training on your data.

## Cautions

- **This is no longer general API access.**
- Since September 2026, clients must send coding-agent traffic, a genuine user agent, and an `x-opencode-session` header, which the community reads as whitelisting non-agent use.
- Limits are dollar-value, so flagship tiers (Grok, Kimi K3, GLM-5.3, GPT 6 Luna) include only $15/month, with a $3 5-hour window.
- The catalog and limits change monthly, the $5 first-month promo is gone, and usage estimates assume heavy prompt caching, so your actual request counts will not match.
- Muse Spark Contributor models train on your prompts and are region-limited.

## Pricing

Go: $10/month, cancel any time, re-verified 2026-10-29.
Go Plus: $40/month, same models with 2x to 4x the per-model monthly dollar limits (Kimi K3 and K3.1 Pro and GPT 6 Luna $15 to $60, GLM-5.3-Flash and Kimi K2.7 Code $60 to $180, DeepSeek V4.1 Flash $80 to $160).
Go Teams: $20 per member per month, every member carrying Go's 5-hour and weekly windows with a monthly limit $5 higher per model (Kimi K3 $20 versus Go's $15), and Extra Usage (overflow into the Zen balance) on by default.
The catalog moved hard between the 2026-10-14 and 2026-10-29 reads: Kimi K3.1 Pro joined at $2/$10 per 1M tokens under the $15 monthly limit, Gemini 4 Argon joined at a 50% launch discount ($2/$10, struck from $4/$20, through November 30, 2026) with a $30 monthly limit, MiniMax M3.1 Flash, MiMo-V2.6 lines, and Qwen3.7 Plus appeared, Step 5 Preview turned paid at $1.00/$2.70 under a $15 limit, LongCat-2.0 replaced the LongCat 2.5 free preview at $0.30/$1.20, and Space Bunny Free and Cat Jam Free left the roster, taking the docs list from 33 entries to 30 and matching the product page's count for the first time since September.
The docs also state DeepSeek's zero-retention agreement renews monthly and currently runs through October 31, 2026.
Each model carries a monthly dollar limit on Go ($15 to $80, mostly $60, $15 for flagships), with windows at 20% per rolling 5 hours (so $12 on a $60 model), 50% weekly ($30), and 100% monthly.
Exceeded limits fall back to free models, or to your Zen balance if you enable it.
Top-ups draw on the shared Zen balance, where card fees are passed at cost.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-03-12 | Go (Beta) | Baseline: $10/month, three models (GLM-5, Kimi K2.5, MiniMax M2.5), $60 usage value | https://help.apiyi.com/en/opencode-go-subscription-worth-it-review-en.html |
| 2026-08-24 | Go | First-month $5 promo removed, flat $10/month | https://codingplan.org/en/plans/opencode-go |
| 2026-09-02 | Go | $15 monthly limit became the standard for several flagship models (community-reported) | https://www.reddit.com/r/opencode/comments/1vo9j8l/opencode_go_15_is_now_the_standard/ |
| 2026-09-24 | GLM-5.3-Flash | Monthly limit doubled to $60 (docs confirm $60 by 2026-09-25) | https://www.reddit.com/r/opencode/comments/1wc1cwe/glm_53_flash_now_gets_twice_the_limits_on/ |
| 2026-09-29 | Go Plus | New $40/month plan added above the $10 Go plan, with 2x to 4x the per-model monthly dollar limits; docs republished 2026-09-28 | https://opencode.ai/docs/go |
| 2026-10-07 | Catalog | Space Bunny added as a priced model at $0.15/$0.60 per 1M tokens with a $30 monthly limit on Go, taking the docs list to 30 entries while the product page still says "View all 29 models" | https://opencode.ai/docs/go |
| 2026-10-10 | Catalog | Claude Haiku 5.5 added at $0.10/$0.50 per 1M tokens under 100K context with the $15 monthly limit, and Step 5 Preview Free added as a limited-time free model; docs list at 32 entries while the product page says 31 | https://opencode.ai/docs/go |
| 2026-10-14 | Catalog | Cat Jam Free, a stealth model, joined as a third limited-time free model (free-period training disclosed per the privacy table); docs list at 33 entries while the product page says 32; $10/$40 tiers and every per-model dollar limit re-verified unchanged | https://opencode.ai/docs/go |
| 2026-10-29 | Go Teams | Third plan added: $20 per member per month, each member carrying Go's 5-hour and weekly windows with a monthly limit $5 higher per model and Extra Usage on by default; Go and Go Plus prices unchanged | https://opencode.ai/docs/go |

## Compared to

[OpenCode Zen](../opencode-zen/index.md) is the sibling pay-per-use gateway: no subscription, huge catalog including Claude and GPT, but per-token prices that can exceed OpenRouter's.
Choose Go when you want a capped, predictable bill for open models.
[OpenRouter](../openrouter/index.md) has hundreds of models with routing and fallback at passthrough prices plus a 5.5% credit fee; choose it when you need frontier or long-tail models Go does not carry.
Direct DeepSeek API beats Go unless you fully use the $60 cap, per a community breakdown that pegs Go at 33% cheaper only at full usage.

## Bottom line

Recommended for heavy users of open coding models who will actually burn the $60 monthly value.
Not for anyone needing general-purpose API access, closed frontier models, or light usage.
My disagreeable claim: at roughly 50% usage Go is about break-even with direct API pricing, so most subscribers are partly paying for slack they never consume.

## Changes

- 2026-09-26 - Created.
- 2026-09-29 - Go Plus added at $40/month with 2x to 4x the per-model monthly dollar limits, the catalog moved from 32 to 29 models (LongCat, Hy3, Hy4 preview, Qwen3.8, and GPT 5.6 Luna joined the roster), and the docs republished 2026-09-28; price history row appended.
- 2026-10-03 - Corrected the model-count claim from 30 to 29, matching the product page's own count and the 2026-09-29 catalog bullet, with the $10/$40 tiers re-verified unchanged.
- 2026-10-06 - Converted the Compared-to cross-references from plain-text paths into working links.
- 2026-10-06 - Docs check (republished 2026-10-06): the DeepSeek V4 family gained peak and off-peak token pricing (off-peak half price, peak 01:00-04:00 and 06:00-10:00 UTC Mon-Fri), while the $10/$40 tiers, the 29-model product-page count, and the per-model dollar limits re-verified unchanged.
- 2026-10-07 - Catalog check: the docs model list moved to 30 entries with Space Bunny newly priced ($0.15/$0.60 per 1M tokens, $30 monthly limit on Go), while the product page still says "View all 29 models"; the $10/$40 tiers and the per-model dollar windows re-verified unchanged, and the repo star figure moved to about 208K on the product page footer.
- 2026-10-10 - Catalog check: Claude Haiku 5.5 joined as the first Anthropic model on Go ($0.10/$0.50 per 1M under 100K context, $15 monthly limit) and Step 5 Preview Free joined the limited-time free roster, taking the docs list to 32 while the product page says 31; the $10/$40 tiers and all per-model dollar windows re-verified unchanged.
- 2026-10-11 - Docs re-check (last updated 2026-10-10): the 32-docs-versus-31-product-page mismatch and the $10/$40 tiers hold, Hermes and ZCode joined the validated-clients table, and the docs state DeepSeek's zero-retention agreement renews monthly (currently through October 31, 2026).
- 2026-10-14 - Catalog check: Cat Jam Free joined as a third limited-time free model, moving the docs list to 33 entries against the product page's 32, with the free-period training disclosure added to the privacy table; the $10/$40 tiers and all per-model dollar windows re-verified unchanged; price history row appended.
- 2026-10-29 - Rotation re-verification with a plan addition and heavy catalog churn: Go Teams joined at $20 per member per month (own limits plus $5 more per model, Extra Usage on by default), Kimi K3.1 Pro and Gemini 4 Argon (50% off through November 30) joined the catalog while Space Bunny Free and Cat Jam Free left and Step 5 Preview turned paid, the docs list settled at 30 entries matching the product page, and the DeepSeek zero-retention renewal statement still runs through October 31; every cited URL re-fetched live this run (the two Reddit threads stay search-read), price history row appended.

## See also

- [OpenCode Zen](../opencode-zen/index.md) - the sibling pay-per-use gateway sharing the same balance and free models.
- [OpenRouter](../openrouter/index.md) - the largest general gateway and the main price competitor for the same open models.
- [OpenCode](../../harnesses/opencode/index.md) - the harness Go is bundled with and defaults to.
- [Model provider feature matrix](../../model-provider-feature-matrix/index.md) - cross-provider comparison of access features.

## References

- https://opencode.ai/go - product page, two-tier $10/$40 framing, model snapshot, GitHub star count (200, 2026-09-29; re-fetched 2026-10-29 with "View all 30 models", the Kimi K3.1 Pro/Gemini 4 Argon/Claude Haiku 5.5/Beam/Iceman New badges, and the Go $10/Go Plus $40 cards, the FAQ carrying the 20%/50%/100% windows and the DeepSeek October 31 renewal statement).
- https://opencode.ai/docs/go - full model/limit table for all three tiers, 20%/50%/100% windows, validated clients, header requirements (200, 2026-09-29, last updated 2026-10-10, re-fetched 2026-10-11 and 2026-10-14 with the Cat Jam Free row present; re-fetched 2026-10-29 with the Go Teams plan, the 30-model list, Kimi K3.1 Pro and Gemini 4 Argon rows, and Beam Free/Iceman Contributor Free as the limited-time free models).
- https://codingplan.org/en/plans/opencode-go - $5 first-month promo removal on 2026-08-24, catalog churn timeline (200; re-fetched 2026-10-29, still showing its 2026-09-24 snapshot of 32 models with Space Bunny Free and no Go Plus, so it lags the official pages by a month).
- https://help.apiyi.com/en/opencode-go-subscription-worth-it-review-en.html - March 2026 Beta state, dollar-window mechanics, critical take (200; re-fetched 2026-10-29, unchanged Beta-era content, cited as the historical baseline).
- https://www.reddit.com/r/opencode/comments/1w9pyvq/opencode_go_is_no_longer_general_api_access/ - community reaction to session-header requirement (direct fetch 403; content read via search).
- https://www.reddit.com/r/opencodeCLI/comments/1tqx9u1/why_opencode_gos_deepseek_v4_pro_is_33_cheaper/ - full-usage price math vs DeepSeek API (content read via search).
