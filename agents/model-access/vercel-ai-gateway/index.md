---
title: Vercel AI Gateway
created: 2026-10-06
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, ai-gateway, pay-per-token, byok]
readability: 3
audience_notes: >
  Engineers choosing a hosted gateway to route coding-agent traffic, and the bill that comes with it.
  Assumes you know per-token provider pricing and what a routing fallback does.
---

Vercel AI Gateway is Vercel's managed model gateway: one API key and one endpoint over 200+ provider models, billed per token at provider list prices with zero markup, plus budgets, fallback, and policy controls that coding agents route through.

**It sells the gateway at 0% and moves the monetization to the platform around it, credits, add-on metering, and the Vercel account, which makes it the cheapest token path here on paper and the least flat one.**

## What it is

A hosted gateway from Vercel, generally available August 21, 2025 after a May 2025 beta, speaking OpenAI Chat Completions, OpenAI Responses, and Anthropic Messages formats, with text, image, video, speech, embeddings, and reranking behind one balance.
You top up AI Gateway Credits and call `ai-gateway.vercel.sh/v1`, Vercel routes to a provider at list price with automatic provider and model fallback, or you bring your own provider keys (BYOK) and pay no fee at all.
The coding-agent surface is the sharpest part: `vercel ai-gateway setup` detects the agents on your machine and writes configs for 29 documented harnesses (Claude Code, Codex, Cursor, OpenCode, Cline, Aider, Crush, Goose, Pi, Zed, and more), stores the key in the macOS Keychain, and migrates desktop sessions.
Team budgets per team, project, key, or member, zero-data-retention routing, and provider allowlists are enforced at the gateway on every request.

## Status

Active and pushed hard into the coding-agent space: the one-command coding-agent setup shipped August 12, 2026 for nine agents, and by mid-September 2026 the docs table covered 29.
It is the same system that serves v0.app, built on the AI SDK (2M+ downloads per week as of the GA post), and changelog entries keep landing (Claude Sonnet 5.5 and Fable 5.1 availability, MiniMax H3 discounts, capacity expansions through September 2026).
Its Hacker News footprint is thin (only 2-to-5-point stories in an Algolia search as of 2026-10-06), so the adoption evidence is the changelog cadence and the integration count, not community debate.

## Strengths

- **On the token path the zero-markup claim checks out: list price on credits and BYOK at no fee, where every other hosted gateway here takes 5% to 5.5% somewhere.**
- One command configures nearly thirty coding agents at once, with budget flags in the same command.
- Team-wide ZDR and provider allowlists hold for every agent request without touching agent configs, which no consumer ladder in this category offers.
- The competitive effect is documented: OpenRouter cut its BYOK fees in October 2025 in response to this gateway.

## Cautions

- There is no flat tier at all: pay-per-token only, so the predictability half of this category sells does not exist here.
- The zero-fee headline excludes add-on metering: team-wide ZDR and provider allowlists bill $0.10 per 1,000 requests, custom reporting $0.075 per 1,000 writes plus $5 per 1,000 queries, and trace drains $0.05 per 1,000 traces plus $0.50 per GB.
- In December 2025 a $0 credit balance blocked every request including BYOK ones (issue 11280, since closed), and the docs now disclose that a failed BYOK request falls back to system credentials billed to your credits, so the balance gate still sits in front of everything.
- Free credits are $5 every 30 days per the GA post (the current pricing page no longer states the amount), the free tier covers a model subset, and the first payment ends free credits permanently.

## Pricing

Tokens bill at each provider's list price with no markup and no platform fee; payment-processing fees on top-ups are yours, as of 2026-10-06.
Free tier: $5 of credits every 30 days per the GA announcement, a free-tier model subset, and per-model rate limits.
Paid tier: AI Gateway Credits top-ups (manual or auto), BYOK free but paid-tier only, volume discounts on request, and Enterprise invoicing without processing fees.
Add-on surcharges, deducted from credits: team-wide provider allowlist $0.10 per 1,000 successful requests and team-wide ZDR $0.10 per 1,000 requests (per-request ZDR free, both Pro and up), custom reporting at $0.075 per 1,000 writes plus $5 per 1,000 queries, and trace drains at $0.05 per 1,000 traces plus $0.50 per GB billed on the plan rather than credits.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-06 | PAYG / BYOK / add-ons | Baseline: tokens at provider list price with 0% markup, BYOK free on the paid tier, free tier $5 of credits per 30 days per the GA post, add-on surcharges published (allowlist and team ZDR $0.10/1k requests, reporting $0.075/1k writes and $5/1k queries, traces $0.05/1k plus $0.50/GB) | https://vercel.com/docs/ai-gateway/pricing |

## Compared to

[OpenRouter](../openrouter/index.md) is the same breadth play with rankings and a community, but it takes 5.5% on credit purchases where Vercel takes 0% on tokens; choose Vercel for the fee, OpenRouter for the ecosystem data.
[LLM Gateway](../llm-gateway/index.md) is the other low-fee challenger at 5% on top-ups plus a flat DevPass; Vercel beats it on fee and agent setup tooling, loses on the flat-rate option.
[LiteLLM](../litellm/index.md) is the self-hosted zero-fee incumbent; pick it when keys and logs cannot sit inside a vendor at all.

## Bottom line

Recommended for teams running several coding agents who want one list-price bill, enforced ZDR and provider policy, and setup in one command.
Not for anyone who needs a predictable monthly ceiling (no flat tier exists) or who refuses a Vercel account around their inference.
My disagreeable claim: zero markup here prices the gateway, not the product, because the margin reappears as per-request surcharges, platform gravity, and the data of knowing what every agent spends.

## Changes

- 2026-10-06 - Created when this run's entrant scan surfaced the gateway's coding-agent setup documentation.

## See also

- [OpenRouter](../openrouter/index.md) - the incumbent gateway whose BYOK fees this one undercut.
- [LLM Gateway](../llm-gateway/index.md) - the other low-fee hosted gateway, with the flat DevPass plans.
- [Requesty](../requesty/index.md) - the governance gateway at a flat 5% with EU residency.
- [LiteLLM](../litellm/index.md) - the self-hosted zero-fee counterpoint.
- [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md) - the vendors billed at list price underneath.

## References

- https://vercel.com/docs/ai-gateway - gateway overview, zero-markup claim, BYOK, budgets, fallback (200, page last updated 2026-09-14)
- https://vercel.com/docs/ai-gateway/pricing - no markup, free and paid tiers, credits, add-on surcharge tables (200, page last updated 2026-09-08)
- https://vercel.com/docs/ai-gateway/coding-agents - the 29-agent setup table, the one-command CLI, per-agent endpoints (200, page last updated 2026-09-13)
- https://vercel.com/blog/ai-gateway-is-now-generally-available - GA announcement of August 21, 2025: $5 free credits per 30 days, hundreds of models, v0 pedigree, AI SDK at 2M weekly downloads (200)
- https://vercel.com/changelog/set-up-coding-agents-in-one-command-with-ai-gateway - the August 12, 2026 coding-agent setup launch, 200+ models, budgets on agent keys (200)
- https://www.coplay.dev/blog/openrouter-drops-fees-in-response-to-vercel-s-ai-gateway - competitive response: OpenRouter's October 2025 BYOK fee cut attributed to this gateway (200)
- https://github.com/vercel/ai/issues/11280 - critical: a $0 credit balance blocked BYOK requests in December 2025, closed with the system-credential fallback documented (fetched via the GitHub API)
