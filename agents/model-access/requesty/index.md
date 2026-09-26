---
title: Requesty
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, ai-gateway, llm-routing, eu-data-residency]
readability: 3
audience_notes: >
  For engineers deciding how to route and pay for LLM traffic in production.
  Assumes you know OpenAI-compatible APIs and per-token model pricing.
---

Requesty is an EU-hosted managed AI gateway that puts 600+ models behind one OpenAI-compatible endpoint and charges a flat 5% markup on upstream model spend.

**The 5% markup is the whole business model: keep your OpenAI SDK code, point the base URL at router.requesty.ai/v1, and pay model cost plus 5% for routing, caching, and governance.**

## What it is

I read it as pass-through billing with a gateway attached: hosted-only, no subscription tiers, no seat fees, no minimum spend.
You get routing policies, fallback chains, semantic caching, budget caps, PII detection, and an MCP gateway over one key.
Their own comparison post says the gateway is built in Rust, and EU residency in Frankfurt is central to their positioning.

## Status

- Alive and funded: a $3M seed led by 20VC was announced 2025-09-26, with Tapestry VC, Insiders Ventures, and Tiny Supercomputer, and Business Insider covered the pitch deck.
- The site footer reads © 2026 Requesty Ltd and their blog shipped multiple gateway comparisons through June and September 2026, yet an hn.algolia.com search for "requesty.ai" returns no story about the company, so their footprint is SEO and docs, not Hacker News.

## Strengths

- Pricing is one line long: a $10/1M token model costs $10.50 through them, and the free tier gives 200 requests/day on free models with no credit card.
- EU (Frankfurt) data residency is included on every plan.
- Enterprise adds SSO, RBAC, audit logs, guardrails, and service accounts for CI/CD.

## Cautions

- The 5% scales with your spend, so the fee grows exactly when your usage does, unlike flat-priced access.
- A competitor-authored guide (TrueFoundry, which sells a rival gateway) notes Requesty is hosted-only with no self-hosting, had SOC 2 Type II still in progress (expected Q3 2026), and keeps self-service prompt logging on for up to 30 days by default, with organization-wide zero retention available only on written request.
- Their own properties disagree on catalog size: 600+ on the pricing page versus 400+ in their June 2026 comparison.
- The "caching makes us net-negative on cost" claim (40-60% hit rates) is vendor math I could not verify independently.

## Pricing

- Free: $0, free models only, 200 requests/day, routing, caching, spend tracking, and EU residency included.
- Pay as you go: flat 5% markup on upstream model cost, all 600+ models, budget caps, and MCP gateway, with BYOK carrying 0% markup per their docs (as of 2026-09-26).
- Enterprise: custom, with SSO (Okta, Azure AD, Google Workspace, custom OIDC), RBAC, approved-model policies, and custom SLAs.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-26 | Pay as you go | Baseline: flat 5% markup on upstream spend, free tier at 200 requests/day | requesty.ai/pricing |

## Compared to

- OpenRouter: a 5.5% fee on credit purchases plus a $0.80 minimum and 365-day credit expiry per Requesty's own comparison; pick OpenRouter for catalog breadth and instant start, Requesty for governance and EU residency.
- LiteLLM: a free self-hosted proxy with zero markup; pick it if you have DevOps capacity and want no vendor in the billing path.
- Synthetic ([Synthetic](../synthetic/index.md)): a flat subscription for open-weight coding models, not a general gateway; pick it for agent coding at a fixed monthly cost.

## Bottom line

Recommended for teams routing production multi-provider traffic who want EU residency, budget governance, and a bill finance can read as a percentage.
Not for solo developers who only want cheap model access, or anyone who needs self-hosting.
My most contestable claim: without repetitive traffic that actually hits the cache, you are just paying 5% for a proxy.

## Changes

- 2026-09-26 - Created.

## See also

- [Synthetic](../synthetic/index.md) - the flat-subscription alternative for open-weight coding models.
- [OpenCode](../../harnesses/opencode/index.md) - an agent harness commonly pointed at gateways like this one.
- [Model provider feature matrix](../../model-provider-feature-matrix/index.md) - the cross-provider comparison this note feeds.

## References

- https://requesty.ai/pricing - 5% markup quote, tier table, 200 requests/day free tier, EU residency (as of 2026-09-26)
- https://www.requesty.ai/blog/requesty-raises-3m - $3M seed led by 20VC, investor list, EU positioning (published 2025-09-26)
- https://www.requesty.ai/blog/best-llm-routing-platforms-compared-2026-requesty-portkey-litellm-openrouter - their own marketing comparison; Rust, 8ms P50 claim, OpenRouter's 5.5% credit fee (published 2026-06-23)
- https://www.truefoundry.com/blog/requesty-ai-pricing - competitor-authored critical guide; BYOK 0%, 30-day prompt retention, SOC 2 in progress (published 2026-09-11)
- https://hn.algolia.com/api/v1/search?query=requesty.ai&tags=story - no meaningful Hacker News footprint found (queried 2026-09-26)
