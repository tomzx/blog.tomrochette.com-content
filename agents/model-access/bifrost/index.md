---
title: Bifrost
created: 2026-10-07
updated: 2026-10-07
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

An Apache-2.0 Go gateway by Maxim (the LLM-evaluation company), deployable with npx, Docker, or Kubernetes Helm charts, with a built-in web UI for configuration and monitoring (8,598 stars, pushed 2026-10-07, as of 2026-10-07).
The core routes across 20-plus providers (OpenAI, Anthropic, Bedrock, Vertex, Azure, and more) with weighted key distribution, automatic fallbacks, and semantic caching; governance layers virtual keys, budgets, and rate limits per consumer, team, or customer.
Around the core sit an MCP gateway that is both client and server (with OAuth, tool filtering, and an agent mode), a plugin system in Go or WASM, Prometheus and OpenTelemetry instrumentation, and SDK drop-in replacements for the OpenAI, Anthropic, Bedrock, and Google GenAI SDKs.
The enterprise tier adds clustering with gossip-based sync, RBAC with Okta and Entra identity providers, guardrails through Bedrock and Model Armor, in-VPC deployment, and audit logs aimed at SOC 2, GDPR, and HIPAA.

## Status

Active and fast-releasing: created 2025-03-19, 8,598 stars, component-tagged releases shipping through 2026-10-06 (transports v2.2.6, telemetry v1.8.5, semanticcache v1.6.9), as of 2026-10-07.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=maximhq/bifrost&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=maximhq/bifrost&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=maximhq/bifrost&type=date&legend=top-left" />
</picture>

The repo description positions it as "50x faster than LiteLLM", a vendor claim whose published support is the docs' own 11-microsecond overhead benchmark; its Show HN threads stayed small (3 points in December 2025), so the adoption case is stars, Docker pulls, and the Trendshift badge rather than independent load-testing.

## Strengths

- The Go core buys a latency and concurrency profile the Python gateways in this family cannot match on the same hardware, at least per the vendor's own numbers.
- Governance is first-class, with hierarchical budgets, per-consumer virtual keys, and MCP tool allow-lists, not bolted on.
- Drop-in SDK replacement means adoption is a base-URL change, and the LiteLLM compatibility layer offers a migration path from the incumbent.
- Plugin extensibility in Go or WASM covers the custom middleware cases that send teams toward building their own gateway.

## Cautions

- The performance and 50x claims are vendor-published; no independent replication exists, as of 2026-10-07.
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

## See also

- [LiteLLM](../litellm/index.md) - the Python incumbent Bifrost positions itself against
- [Experiential](../experiential/index.md) - the zero-markup hosted-gateway sibling in this family
- [Plano](../plano/index.md) - the Envoy-based self-hosted gateway with the router lineage
- [Model Access Feature Matrix](../model-access-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/maximhq/bifrost - repository, Apache-2.0 license, the 23-plus-provider README, and the 50x-LiteLLM positioning (fetched 200, 2026-10-07)
- https://api.github.com/repos/maximhq/bifrost - stars, created date, push date, and license for the as-of status (fetched 200, 2026-10-07)
- https://docs.getbifrost.ai - the feature surface: failover, virtual keys, budgets, semantic caching, the MCP gateway, plugins, the 11-microsecond benchmark claim, and the enterprise tier (fetched 200, 2026-10-07)
- https://api.github.com/repos/maximhq/bifrost/releases - the component-tagged release line through 2026-10-06 (fetched 200, 2026-10-07)
- https://hn.algolia.com/api/v1/items/46203228 - the December 2025 Show HN thread, 3 points, grounding the small-HN-footprint observation (fetched 200, 2026-10-07)
- https://raw.githubusercontent.com/maximhq/bifrost/HEAD/README.md - the quickstart surfaces (npx, Docker) and the provider list behind the gateway cells (fetched 200, 2026-10-07)
