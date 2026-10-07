---
title: LiteLLM
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, llm-gateway, self-hosted]
readability: 3
audience_notes: >
  For engineers deciding whether to self-host a gateway in front of their model providers.
  Assumes you know OpenAI-compatible APIs and per-token billing.
---

LiteLLM is the dominant self-hosted AI gateway, a Python SDK plus proxy server that exposes one OpenAI-compatible endpoint over 100+ provider APIs with routing, budgets, and spend tracking.

**Self-hosting the gateway means you own its availability, its config surface, and (since March 2026) its supply-chain risk, and that ownership is the entire trade.**

## What it is

BerriAI's gateway ships in two pieces: a Python SDK, a drop-in OpenAI-format client for 100+ providers, and a self-hosted proxy server with virtual keys, per-key budgets, rate limits, an admin UI, and spend tracking.
The Router adds retries, fallbacks, and load balancing across deployments, so an agent survives a single provider's outage or rate limit.
The proxy now also fronts MCP servers and A2A agents, making one deployment the gateway for models, tools, and agents at once.
A Rust core is in beta, and the repo description now reads "Rust core with Python SDK".
The core is MIT licensed; the `enterprise/` directory ships under a separate commercial license.

## Status

Very active: 60,198 stars as of 2026-10-06, repo pushed the same day, publicly released July 2023.

[![Star History Chart](https://api.star-history.com/chart?repos=BerriAI/litellm&type=date&legend=top-left)](https://www.star-history.com/?repos=BerriAI%2Flitellm&type=date&legend=top-left)

The cadence is extreme: a new minor line roughly every week, with v1.98.1, v1.99.4, v1.100.3, v1.101.2, v1.102.1, and v1.103/1.104 pre-releases all published between September 16 and 25, 2026, and PyPI latest at 1.104.0 (2026-10-04).
Since 2026-06-29 only the four most recent stable minor lines receive patches, a policy the company states is a direct cost of that cadence.
**In March 2026 the project's PyPI publishing credentials were compromised: poisoned 1.82.7 and 1.82.8 wheels shipped a credential stealer and were quarantined within about a day (PYSEC-2026-2).**

## Strengths

- One OpenAI-compatible surface over 100+ providers, with the Router handling retries, fallbacks, and load balancing.
- Virtual keys, per-key and per-team budgets, rate limits, and spend tracking are in the free self-hosted tier, not gated.
- The MCP and A2A gateways converge into the same endpoint, so one deployment fronts models, tools, and agents.
- The observability surface is broad, with callbacks for Langfuse, MLflow, Helicone, and OpenTelemetry.
- Day-0 support for new providers is effectively weekly, which matters when an agent stack adopts a fresh model fast.

## Cautions

- **March 2026: compromised 1.82.7/1.82.8 PyPI wheels stole SSH keys, cloud credentials, and Kubernetes tokens, exfiltrating to a lookalike domain; TechCrunch later tied the Mercor breach to the same compromise.**
- A gateway aggregates every provider credential you own, so it is a single high-value theft target; pin versions and verify tags before pulling.
- The config surface moves fast: minor lines ship weekly and older lines lose support within four releases, so an unpinned deployment drifts.
- Community pushback exists: a September 2026 "LiteLLM without the bloat" fork hit 177 points on Hacker News, with commenters arguing the SDK has outgrown its size and dependency budget.
- SSO above 5 users, audit logs, and most built-in moderation guardrails require the enterprise license.
- No public enterprise pricing; everything beyond OSS is quote-based, with no published floor.

## Pricing

Self-hosted OSS: free, MIT licensed (excluding the `enterprise/` directory).
Enterprise: quote-based license scoped to deployment size, adding SSO/SCIM, audit logs, organization RBAC, IP allowlists, multi-region deployment, and secret-manager integration; SSO is free for up to 5 users.
Standard enterprise support is included with the license, and 24/7 SLAs (Sev 0 in 1 hour) cost extra.
No model-access fees: providers bill tokens directly and LiteLLM takes no cut, as of 2026-10-02.

## Compared to

[OpenRouter](../openrouter/index.md) is the hosted counterpart: the same multi-provider idea, but someone else runs it and takes a 5.5% credit fee; choose LiteLLM when data residency or key custody rules out a third party.
[OpenCode Zen](../opencode-zen/index.md) sells curation of benchmarked endpoints; LiteLLM sells control, with no curation guarantee.
[Requesty](../requesty/index.md) is the category's other hosted gateway, lighter to adopt; LiteLLM wins on self-hosting and enterprise controls.

## Bottom line

Recommended for platform teams that must keep provider keys and logs inside their own perimeter, or that need per-team budgets across many providers.
Not for a single-provider setup or a small project, where the gateway is operational overhead without a payoff.
My disagreeable claim: below three providers, self-hosting LiteLLM is negative value, because you are running a stateful service to avoid editing a base URL.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars scan surfaced it.
- 2026-10-06 - Converted the Compared-to cross-references from plain-text paths into working links.
- 2026-10-07 - Added the BerriAI/litellm star history chart to the Status section.

## See also

- [OpenRouter](../openrouter/index.md) - the hosted gateway most teams compare against this one.
- [OpenCode Zen](../opencode-zen/index.md) - the curated-endpoint counterpoint to uncurated self-hosting.
- [Requesty](../requesty/index.md) - the category's other hosted gateway.
- [OpenCode](../../harnesses/opencode/index.md) - a coding harness that consumes gateways like this one.
- [Model provider feature matrix](../../model-provider-feature-matrix/index.md) - where LiteLLM sits among access providers.

## References

- https://api.github.com/repos/BerriAI/litellm - 60,198 stars, Python, license metadata, pushed 2026-10-06 (fetched via the GitHub API, 2026-10-06).
- https://docs.litellm.ai/docs/ - SDK and proxy feature claims, 100+ providers, MCP/A2A gateway, Rust beta (200).
- https://docs.litellm.ai/docs/enterprise - enterprise feature gates, SSO free to 5 users, four-line support window effective 2026-06-29 (200).
- https://raw.githubusercontent.com/BerriAI/litellm/main/LICENSE - MIT text with the enterprise/ directory carve-out (200).
- https://futuresearch.ai/blog/litellm-attack-transcript/ - minute-by-minute discovery of the March 2026 PyPI compromise, payload behavior, PYSEC-2026-2 (200).
- https://hn.algolia.com/api/v1/search?query=LiteLLM&tags=story&hitsPerPage=8 - the 938-point compromise thread, the Mercor/TechCrunch story, the litelm bloat fork (200).
- https://hn.algolia.com/api/v1/items/49662767 - litelm discussion, bloat criticism and rebuttals, 177 points (200).
- https://api.github.com/repos/BerriAI/litellm/releases?per_page=15 - release cadence, four stable lines patched the same day in September 2026 (200).
- https://pypi.org/pypi/litellm/json - PyPI latest at 1.104.0 (200, re-checked 2026-10-06).
