---
title: OpenCode Go
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, coding-subscription, open-models]
readability: 3
audience_notes: >
  For engineers choosing how to pay for coding models.
  Assumes you know what an LLM API provider is and how coding agents consume one.
---

OpenCode Go is a $10/month subscription from the OpenCode (Anomaly) team that bundles access to a curated set of open coding models, usable from OpenCode or any compatible coding agent.

## What it is

Go sells model access, not an editor or a harness.
You subscribe, copy an API key, and point any agent at OpenAI-compatible, Anthropic-compatible, or Responses endpoints under `opencode.ai/zen/go/v1`.
The lineup is 32 open-weight coding models as of 2026-09-26 (Grok 4.7/4.6, GLM-5.3 family, Kimi K3, Qwen3.x, DeepSeek V4, MiniMax M3, MiMo, GPT 6 Luna), and only one member per workspace can hold a subscription.

## Status

Active and changing fast.
The OpenCode repo shows about 208K GitHub stars as of 2026-09-26, the Go docs were last updated 2026-09-25, and the plan has grown from a three-model Beta in March 2026 to 32 models.
Churn is constant: GPT 6 Luna arrived 2026-09-22 and Space Bunny Free appeared as a limited-time unlimited model.
**Go converts $10 into up to $60 of metered usage per month, and that 6x ratio is the entire value proposition.**

## Strengths

- The $60 monthly usage value costs $10, up to 6x leverage if you max it.
- Models are benchmarked for agentic coding before inclusion, per the team.
- Works with any agent; Claude Code, Codex, Pi, jcode, and Kilo Code CLI are validated clients.
- Dollar-denominated windows make the bill predictable, free models stay available after limits, and "Use balance" falls back to your Zen balance instead of hard-stopping requests.
- Most models run with zero retention and no training on your data.

## Cautions

- **This is no longer general API access.**
- Since September 2026, clients must send coding-agent traffic, a real user agent, and an `x-opencode-session` header, which the community reads as whitelisting non-agent use.
- Limits are dollar-value, so flagship tiers (Grok, Kimi K3, GLM-5.3, GPT 6 Luna) include only $15/month, with a $3 5-hour window.
- The catalog and limits change monthly, the $5 first-month promo is gone, and usage estimates assume heavy prompt caching, so your real request counts will not match.
- Muse Spark Contributor models train on your prompts and are region-limited.

## Pricing

$10/month, cancel any time, as of 2026-09-26.
Each model carries a monthly dollar limit (mostly $60, some $30, $15 for flagships), with windows at 20% per rolling 5 hours (so $12 on a $60 model) and 50% weekly ($30).
Exceeded limits fall back to free models, or to your Zen balance if you enable it.
Top-ups draw on the shared Zen balance, where card fees are passed at cost (4.4% + $0.30).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-03-12 | Go (Beta) | Baseline: $10/month, three models (GLM-5, Kimi K2.5, MiniMax M2.5), $60 usage value | https://help.apiyi.com/en/opencode-go-subscription-worth-it-review-en.html |
| 2026-08-24 | Go | First-month $5 promo removed, flat $10/month | https://codingplan.org/en/plans/opencode-go |
| 2026-09-02 | Go | $15 monthly limit became the standard for several flagship models (community-reported) | https://www.reddit.com/r/opencode/comments/1vo9j8l/opencode_go_15_is_now_the_standard/ |
| 2026-09-24 | GLM-5.3-Flash | Monthly limit doubled to $60 (docs confirm $60 by 2026-09-25) | https://www.reddit.com/r/opencode/comments/1wc1cwe/glm_53_flash_now_gets_twice_the_limits_on/ |

## Compared to

OpenCode Zen (../opencode-zen/index.md) is the sibling pay-per-use gateway: no subscription, huge catalog including Claude and GPT, but per-token prices that can exceed OpenRouter's.
Choose Go when you want a capped, predictable bill for open models.
OpenRouter (../openrouter/index.md) has hundreds of models with routing and fallback at passthrough prices plus a 5.5% credit fee; choose it when you need frontier or long-tail models Go does not carry.
Direct DeepSeek API beats Go unless you fully use the $60 cap, per a community breakdown that pegs Go at 33% cheaper only at full usage.

## Bottom line

Recommended for heavy users of open coding models who will actually burn the $60 monthly value.
Not for anyone needing general-purpose API access, closed frontier models, or light usage.
My disagreeable claim: at roughly 50% usage Go is about break-even with direct API pricing, so most subscribers are partly paying for slack they never consume.

## Changes

- 2026-09-26 - Created.

## See also

- [OpenCode Zen](../opencode-zen/index.md) - the sibling pay-per-use gateway sharing the same balance and free models.
- [OpenRouter](../openrouter/index.md) - the largest general gateway and the main price competitor for the same open models.
- [OpenCode](../../harnesses/opencode/index.md) - the harness Go is bundled with and defaults to.
- [Model provider feature matrix](../../model-provider-feature-matrix/index.md) - cross-provider comparison of access features.

## References

- https://opencode.ai/go - product page, $10/month framing, model snapshot, GitHub star count (200).
- https://opencode.ai/docs/go - full model/limit table, 20%/50%/100% windows, validated clients, header requirements (200).
- https://codingplan.org/en/plans/opencode-go - $5 first-month promo removal on 2026-08-24, catalog churn timeline (200).
- https://help.apiyi.com/en/opencode-go-subscription-worth-it-review-en.html - March 2026 Beta state, dollar-window mechanics, critical take (200).
- https://www.reddit.com/r/opencode/comments/1w9pyvq/opencode_go_is_no_longer_general_api_access/ - community reaction to session-header requirement (direct fetch 403; content read via search).
- https://www.reddit.com/r/opencodeCLI/comments/1tqx9u1/why_opencode_gos_deepseek_v4_pro_is_33_cheaper/ - full-usage price math vs DeepSeek API (content read via search).
