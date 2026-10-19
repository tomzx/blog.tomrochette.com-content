---
title: Bifrost
created: 2026-10-07
updated: 2026-10-19
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, gateway, self-hosted]
readability: 3
audience_notes: >
  Teams self-hosting an LLM gateway for routing, failover, budgets, and governance across providers.
  Assumes you know what an OpenAI-compatible endpoint is.
---

Bifrost is Maxim's high-performance open-source AI gateway: one Go service unifying 20-plus providers behind an OpenAI-compatible API with automatic failover, load balancing, semantic caching, budgets, and an MCP gateway, self-hosted or clustered.

**Bifrost is the self-hosted-gateway family's performance challenger, the LiteLLM sibling built in Go instead of Python, and its governing claim is overhead: the vendor's sustained benchmark puts added latency at 11 microseconds per request at 5,000 requests per second.**

## What it is

An Apache-2.0 Go gateway by Maxim (the LLM-evaluation company), deployable with npx, Docker, or Kubernetes Helm charts, with a built-in web UI for configuration and monitoring (8,762 stars, pushed 2026-10-13, as of 2026-10-14).
The core routes across 20-plus providers (OpenAI, Anthropic, Bedrock, Vertex, Azure, and more) with weighted key distribution, automatic fallbacks, and semantic caching; governance layers virtual keys, budgets, and rate limits per consumer, team, or customer.
Around the core sit an MCP gateway that is both client and server (with OAuth, tool filtering, and an agent mode), a plugin system in Go or WASM, Prometheus and OpenTelemetry instrumentation, and SDK drop-in replacements for the OpenAI, Anthropic, Bedrock, and Google GenAI SDKs.
The enterprise tier adds clustering with gossip-based sync, RBAC with Okta and Entra identity providers, guardrails through Bedrock and Model Armor, in-VPC deployment, and audit logs aimed at SOC 2, GDPR, and HIPAA.

## Status

Active and fast-releasing: created 2025-03-19, 8,842 stars as of 2026-10-16, component-tagged releases shipping through 2026-10-13 (transports v2.3.0, telemetry v1.9.0, semanticcache v1.7.0, routing v1.2.0, prompts v1.1.10), repo pushed 2026-10-19, as of 2026-10-19.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=maximhq/bifrost&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=maximhq/bifrost&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=maximhq/bifrost&type=date&legend=top-left" />
</picture>

The repo description no longer carries the "50x faster than LiteLLM" comparison it had at creation: re-fetched 2026-10-18 it sells "10,000+ models", "under 200µs of overhead at 5k RPS", and MCP Code Mode, while the docs and README still carry the 11-microsecond vendor benchmark; its Show HN threads stayed small (3 points in December 2025), so the adoption case is stars, Docker pulls, and the Trendshift badge rather than independent load-testing.

## Strengths

- The Go core buys a latency and concurrency profile the Python gateways in this family cannot match on the same hardware, at least per the vendor's own numbers.
- Governance is first-class, with hierarchical budgets, per-consumer virtual keys, and MCP tool allow-lists, not bolted on.
- Drop-in SDK replacement means adoption is a base-URL change, and the LiteLLM compatibility layer offers a migration path from the incumbent.
- Plugin extensibility in Go or WASM covers the custom middleware cases that send teams toward building their own gateway.

## Cautions

- The performance claims are vendor-published with no independent replication (the docs' 11-microsecond benchmark, plus the description's looser under-200µs line), as of 2026-10-18; the 50x-faster-than-LiteLLM comparison left the description by this date.
- Smaller ecosystem than LiteLLM: fewer providers, fewer integrations, and a shorter community track record.
- Enterprise governance (clustering, RBAC, SSO) sits behind contact-sales, so the open core alone may not carry a large production deployment.
- A young project from a company whose main product is an evaluation platform, so the gateway's long-term priority is an inference about Maxim's roadmap, not a fact.

## Pricing

Free and open source under Apache-2.0; the gateway itself has no paid tier, so pricing does not apply.
Enterprise governance features are priced through contact-sales conversations with unpublished numbers.

## Compared to

- [LiteLLM](../litellm/index.md): the family incumbent at roughly 60k stars, Python, broadest provider and integration coverage; choose Bifrost for throughput-critical self-hosting, LiteLLM for ecosystem breadth.
- [Experiential](../experiential/index.md): the YC-backed zero-markup gateway that mines agent traces; Bifrost keeps your traces local instead of trading them for routers.
- [Plano](../plano/index.md): the Envoy-based gateway and agent data plane; Bifrost is the application-level gateway, Plano the infrastructure-level one.

## Bottom line

**Recommended for teams that need a self-hosted gateway fast enough to sit in the hot path and want budgets, failover, and MCP governance in one deployable.**
Not for the broadest provider matrix or the largest community, where LiteLLM still leads, and not for buyers who need independently benchmarked performance claims before committing.

## Changes

- 2026-10-07 - Created.
- 2026-10-16 - Release train refresh: five component releases landed 2026-10-13 (transports v2.3.0, telemetry v1.9.0, semanticcache v1.7.0, routing v1.2.0, prompts v1.1.10) after the previous set had held since 2026-10-06, and the API re-fetch moved stars to 8,842 with the repo pushed 2026-10-16.
- 2026-10-18 - Repo-description refresh: the 50x-faster-than-LiteLLM comparison left the repository description (now "10,000+ models", "under 200µs of overhead at 5k RPS", and MCP Code Mode), the docs and README still carry the 11-microsecond vendor benchmark, and the repo pushed 2026-10-18; the Status and Cautions prose moved with it.

## See also

- [LiteLLM](../litellm/index.md) - the Python incumbent Bifrost positions itself against
- [Experiential](../experiential/index.md) - the zero-markup hosted-gateway sibling in this family
- [Plano](../plano/index.md) - the Envoy-based self-hosted gateway with the router lineage
- [Model Access Feature Matrix](../model-access-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/maximhq/bifrost - repository, Apache-2.0 license, the 23-plus-provider README, and (at the 2026-10-07 fetch) the description's 50x-LiteLLM positioning, since removed (fetched 200, 2026-10-07)
- https://api.github.com/repos/maximhq/bifrost - stars, created date, push date, and license for the as-of status (fetched 200, 2026-10-07; re-fetched 2026-10-16 at 8,842 stars, pushed 2026-10-16; re-fetched 2026-10-18 with the description no longer carrying the 50x claim and pushed 2026-10-18; re-fetched 2026-10-19, pushed 2026-10-19, description unchanged).
- https://docs.getbifrost.ai - the feature surface: failover, virtual keys, budgets, semantic caching, the MCP gateway, plugins, the 11-microsecond benchmark claim, and the enterprise tier (fetched 200, 2026-10-07; re-fetched 2026-10-18 with the 11µs claim and the 20-plus-provider framing unchanged)
- https://api.github.com/repos/maximhq/bifrost/releases - the component-tagged release line through 2026-10-06 (fetched 200, 2026-10-07)
- https://hn.algolia.com/api/v1/items/46203228 - the December 2025 Show HN thread, 3 points, grounding the small-HN-footprint observation (fetched 200, 2026-10-07)
- https://raw.githubusercontent.com/maximhq/bifrost/HEAD/README.md - the quickstart surfaces (npx, Docker) and the provider list behind the gateway cells (fetched 200, 2026-10-07; re-fetched 2026-10-18 on the dev branch with the 23-plus-provider framing and the 11µs benchmark table unchanged)
