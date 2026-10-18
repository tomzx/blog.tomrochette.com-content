---
title: IBM ContextForge
created: 2026-10-11
updated: 2026-10-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, gateway, mcp, governance, open-source, ibm]
readability: 3
audience_notes: >
  Platform engineers who want one governed, authenticated door in front of the MCP servers, A2A agents, and REST APIs their agents call, and who can run the supporting infrastructure themselves.
  Assumes you know what an API gateway and RBAC are.
---

IBM ContextForge (IBM/mcp-context-forge) is an Apache-2.0 gateway, registry, and proxy from IBM that federates MCP servers, A2A agents, and REST/gRPC APIs behind one authenticated endpoint, with RBAC, rate limits, SSO, audit trails, and a plugin framework.

**Its governance is traffic governance, not verdict governance: identity, rate limiting, and audit land at the wire, content guardrails are delegated to plugins, and at 4,597 stars it is the most-adopted self-hosted gateway in this category, evidence that teams adopt the door before they adopt the verdicts.**

## What it is

A Python and FastAPI application you deploy from PyPI (`mcp-contextforge-gateway`), a GHCR container, Docker Compose, or Helm, over SQLite in development and PostgreSQL plus Redis in production, with Redis-backed federation scaling to multi-cluster Kubernetes.
It runs as a fully compliant MCP server: MCP servers, A2A agents, and legacy REST or gRPC services (translated to MCP on the fly) register through an admin UI, and clients see one unified endpoint with auth, retries, and rate limiting in front of everything.
The governance surfaces are enterprise identity ones: RBAC roles and teams, multi-tenant workspaces, SSO through Keycloak, Okta, Microsoft Entra ID, IBM Security Verify, GitHub, or Google, OAuth 2.0 with user-scoped tokens, and metadata tracking with audit trails.
Security defaults are strict for the category: the gateway fails fast at startup without configured secrets, requires JTI and expiry claims on tokens, keeps public registration off, and applies fail-closed SSRF allowlists to cross-gateway routing.
IBM announced it as the ContextForge MCP Gateway 1.0.0 Beta on December 15, 2025, and the same post named IBM Elite Support (24x7x365 with a 2-hour SLA) as the paid support path; the project is maintained by IBM, led by Mihai Criveti, a Distinguished Engineer.

## Status

Active and heavily adopted: 4,623 stars, 924 forks, and 943 open issues as of 2026-10-18, created 2025-05-08, pushed 2026-10-17, with v1.0.11 published 2026-09-28 on GitHub and PyPI in step.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ibm/mcp-context-forge&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ibm/mcp-context-forge&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ibm/mcp-context-forge&type=date&legend=top-left" />
</picture>

**The adoption is unusually organic for this category: 4,623 stars and 924 forks put it third here behind Paperclip and the Microsoft toolkit, and fetched third-party comparisons already treat it as the standing self-hosted MCP gateway rather than a curiosity.**
The open-issue backlog is the largest of any gateway in this category by an order of magnitude (943, against a next-largest in the dozens), which reads as day-to-day use at scale colliding with limited maintainer triage, not as abandonment.

## Strengths

- Fleet-scale plumbing with the adoption to match: multi-cluster federation, Helm, air-gapped deployment, OpenTelemetry, and 7,000-plus tests, at a scale no other self-hosted gateway here matches.
- Secure by default in the ways that bite: mandatory startup secrets, required token expiry and revocation claims, public registration off, and fail-closed SSRF allowlists for cross-gateway routing.
- Protocol breadth is the point: one door in front of MCP, A2A agents, and REST/gRPC services, with legacy APIs virtualized as MCP tools instead of rewritten.
- Enterprise identity comes built in: RBAC, teams, multi-tenant workspaces, and SSO against the providers enterprises already run.

## Cautions

- Guardrails are plugins, not built-in policy verdicts: the launch blog counts 35-plus security plugins, and a third-party comparison states plainly that guardrails are not built in, so out of the box this is an authenticated door, not a policy engine.
- It governs tools and agent traffic, not models: there is no LLM routing, cost attribution, or model policy, unlike the managed Unity Gateway, so most deployments still need a second gateway for model traffic.
- The 943-open-issue backlog and self-hosted everything (Kubernetes, Redis, and your own Phoenix or Jaeger) add up to a platform-team commitment, not an install.
- Container images do not support arm64 in production, an Apple Silicon footnote that matters more every year.
- Competitor comparisons (TrueFoundry's is the most detailed) frame it as operationally heavy and under-supported; IBM's own Elite Support announcement contradicts the support half, but read every comparison in this space as positioning.

## Pricing

Apache-2.0 and free, self-hosted; your infrastructure is the cost.
IBM sells Elite Support for it (24x7x365 global support with a 2-hour SLA) by contact, with no public price.
No dollar prices are published, so there is no price history to track.

## Compared to

- [Databricks Unity Gateway](../databricks-unity-gateway/index.md): the managed counterpart, bundled into a platform and governing model plus MCP traffic with dollar-cost audit; choose it if you are on Databricks, ContextForge if you want the self-hosted door without buying a lakehouse.
- [LiteLLM](../../model-access/litellm/index.md): the model-traffic sibling one shelf over; ContextForge governs tool and agent traffic, LiteLLM governs provider calls, and teams that need both run both.
- [Cordum](../cordum/index.md): dispatch-time governance that holds a job until a human approves, where ContextForge authenticates and rate-limits whatever passes through; choose Cordum for approval workflows, ContextForge for access control at scale.

## Bottom line

**Recommended for platform teams that want one governed, authenticated endpoint in front of many MCP servers, A2A agents, and REST APIs, and can run PostgreSQL, Redis, and their own observability stack behind it.**
Not for model-cost governance, not for built-in policy verdicts without plugin work, and not for teams without the operations capacity to own a distributed gateway.

## Changes

- 2026-10-11 - Created from the awesome-ai-governance entrant scan, profiling IBM's gateway as the category's most-adopted request-boundary member.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [Databricks Unity Gateway](../databricks-unity-gateway/index.md) - the managed platform counterpart at the same request boundary
- [LiteLLM](../../model-access/litellm/index.md) - the model-traffic gateway this deliberately is not
- [Model Context Protocol (MCP)](../../protocols/mcp/index.md) - the protocol whose traffic this gateway governs
- [Cordum](../cordum/index.md) - the approval-first dispatch gate at a different enforcement point

## References

- https://github.com/IBM/mcp-context-forge - README: federation scope, deployment paths, security defaults, arm64 note, maintainers
- https://ibm.github.io/mcp-context-forge/latest/ - official documentation: RBAC, teams, SSO providers, OAuth, audit trails, plugins, multitenancy
- https://developer.ibm.com/blogs/context-forge-mcp-gateway-now-available/ - the December 15, 2025 launch post: 1.0.0 beta, 35-plus guardrail plugins, multi-tenant workspaces, IBM Elite Support with a 2-hour SLA
- https://api.github.com/repos/IBM/mcp-context-forge - stars, forks, issues, creation and push dates as of 2026-10-17
- https://api.github.com/repos/IBM/mcp-context-forge/releases - v1.0.11, published 2026-09-28
- https://pypi.org/pypi/mcp-contextforge-gateway/json - mcp-contextforge-gateway 1.0.11, uploaded 2026-09-28
- https://www.truefoundry.com/blog/ibm-contextforge-vs-truefoundry - the critical third-party comparison: guardrails not built in, no LLM routing, operational weight (a competitor's framing, read as positioning)
