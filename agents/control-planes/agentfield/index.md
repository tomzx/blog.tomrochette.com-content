---
title: AgentField
created: 2026-10-13
updated: 2026-10-17
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, governance, identity, policy-enforcement, receipts, open-source]
readability: 3
audience_notes: >
  Engineers who want to run fleets of agents as backend services with identity, policy, approvals, and audit built into the plane rather than bolted on, and who can accept a release train that has never left release candidates.
  Assumes you know what a DID, a policy gate, and a canary deployment are.
---

AgentField (Agent-Field/agentfield) is an Apache-2.0 open-source control plane from AgentField, the company founded by the Agnostiq and Covalent team, that turns Python, Go, or TypeScript agent functions into REST endpoints on a stateless Go plane and builds identity, access policy, human approvals, cost caps, and tamper-evident audit trails into the same service that routes the calls.

**Its pitch is that governance and the execution fabric should be one artifact: every agent gets a W3C DID, every cross-agent call is evaluated against tag-based ALLOW and DENY policy, every execution produces an offline-verifiable credential, and the same plane handles the queueing, retries, and fan-out.**

## What it is

A stateless Go control plane you run from Docker Compose or Kubernetes (or one binary beside your agents), scaling horizontally behind a load balancer, with a dashboard on localhost 8080 and an `af` CLI for scaffolding, serving, and verification.
Agents are plain functions in Python, Go, or TypeScript: `@app.reasoner()` marks AI judgment, `@app.skill()` marks deterministic code, and `app.run()` exposes each as a REST endpoint that auto-registers with the plane.
Beyond routing it owns the operational surface: durable async execution with webhooks and SSE (runs of hours or days, no timeout), bounded in-process admission with backpressure (429 and 503 plus Retry-After), canary and blue-green agent deployments, tag-based discovery across the mesh, memory scopes (global, actor, session, workflow) with KV plus vector search, and workflow DAG traces.
It also orchestrates coding agents: its own AForge harness ships beside the plane, and Claude Code, Codex, Gemini CLI, and OpenCode can be dispatched as providers through `app.harness()`.
The governance layer is the differentiator: tag-based access policies (function-level granularity, input constraints, priority ordering, first-match-wins), a tag approval workflow (auto, manual, or forbidden registration), cryptographically signed tag credentials, DID revocation lists, human approval pauses through `app.pause()`, per-run cost caps (`max_budget_usd`), and a verifiable credential per execution that verifies offline with `af vc verify audit.json`.

## Status

Active and funded: 2,611 stars, 430 forks, 36 open issues, and 62 contributors as of 2026-10-13, repository created 2025-11-05 (the company organization in March 2025), last push 2026-10-17.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Agent-Field/agentfield&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Agent-Field/agentfield&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Agent-Field/agentfield&type=date&legend=top-left" />
</picture>

The release train has never left release candidates: the latest tag is v0.1.142-rc.14 (2026-10-17) and PyPI holds agentfield 0.1.141 (2026-09-29).
The founders are Oktay Goktas and Santosh Kumar Radha, the team behind Agnostiq (acquired by DataRobot in 2025) and Covalent, with Panache Ventures, Brightspark Ventures, and Drive Capital listed as partners, so this is a funded company's open-source product rather than a weekend project.
**The community footprint is thin for the star count: a Hacker News search returns zero relevant threads, and the one independent writeup I found is a single Medium post, so the adoption evidence is the star count, the contributor count, and the vendor's own case studies (a 10,000-branch deep-research fan-out, a 250-agent security audit, both self-reported) rather than public technical debate.**

## Strengths

- Identity, policy, approvals, cost caps, and receipts ship inside the free build; the pricing page's own framing is that the capabilities usually reserved for an enterprise upsell are in the same artifact as the rest.
- The governance model is cryptographic rather than prompt-based: signed tag credentials prove authorization was legitimately assigned, revocations propagate, and execution receipts verify offline.
- The execution fabric is production plumbing: backpressure with explicit status codes, canary rollouts at traffic weights, webhooks with HMAC signing, and DAG traces over every fan-out.
- Three SDK languages plus harness orchestration mean coding agents become callable functions on the same governed plane instead of running outside it.

## Cautions

- Policy evaluation is fail-open by default: with no matching policy a cross-agent call is allowed, which the docs call backward compatibility and which inverts the default most gates in this category ship.
- The train is all release candidates (v0.1.x-rc), so pin deliberately, expect wire and config churn, and note PyPI trails the tags.
- Installation and lifecycle telemetry is on by default (the README says no prompts or payloads are sent; opt out with `AGENTFIELD_TELEMETRY_ENABLED=false`), a default worth knowing before any regulated deployment.
- Zero Hacker News threads and one third-party writeup mean the enforcement and scale claims are the vendor's own; the useful exception is the README's own routing-overhead admission (roughly 100 to 200 milliseconds per cross-agent hop), stated against interest.
- The marketing site splits the story ("the full governance story lives on the enterprise page") while the pricing page insists no paid tier exists, so read the docs and the repository rather than either surface.

## Pricing

Free: one tier at $0, everything included, no paid, premium, or enterprise tier, no account, no usage limits, Apache-2.0, self-hosted (the vendor's pricing page is explicit on every point).
The enterprise page describes audiences for the governance capabilities, not a tier, and the costs you actually carry are the infrastructure and model spend behind your agents.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-13 | Core | Recorded at $0, one tier, no paid plan, unlimited seats and usage | https://agentfield.ai/pricing.md |

## Compared to

- [Cordum](../cordum/index.md): both gate at the plane, but Cordum's safety kernel returns ALLOW, DENY, or REQUIRE_APPROVAL before a worker runs under a BUSL-1.1 license, while AgentField evaluates tag policy on cross-agent calls, fails open on no match, and is Apache-2.0 with the identity layer built in; choose Cordum for approval-held job dispatch, AgentField for an agent backend with identity and receipts.
- [Paperclip](../paperclip/index.md): the company control plane that manages agents as employees over a ticket board with org charts and budgets; AgentField runs the agents as services instead of managing them as staff.
- [IBM ContextForge](../ibm-contextforge/index.md): the gateway that federates existing MCP, A2A, and REST traffic behind one governed door; AgentField expects the agents to be written on it in the first place.

## Bottom line

**Recommended for teams building an agent backend from scratch who want identity, policy, approvals, and audit in the same artifact as the execution fabric, and who will configure deny-by-default policy on day one.**
Not for governing agents built on other frameworks (ContextForge or the Microsoft toolkit federate and wrap instead), and not for anyone who needs a stable 1.0 or independent validation of the enforcement claims.

## Changes

- 2026-10-13 - Created from the 2026-10-12 entrant resolution, profiling the Apache-2.0 agent-backend plane with DID identity, tag policy, approvals, and receipts built into the free build.
- 2026-10-16 - Release train moved to v0.1.142-rc.12 (2026-10-15) with PyPI holding at 0.1.141.
- 2026-10-17 - Release train moved to v0.1.142-rc.14 (2026-10-17) with PyPI still holding at 0.1.141.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [Cordum](../cordum/index.md) - the dispatch-time safety kernel and the closest enforcement-point neighbor
- [Paperclip](../paperclip/index.md) - the company-scale control plane for managing agents rather than running them
- [An Agent Is Only as Safe as Its Worst Tool Call](../../../an-agent-is-only-as-safe-as-its-worst-tool-call/index.md) - the corpus argument for gating the call

## References

- https://github.com/Agent-Field/agentfield - README: control-plane framing, governance pillars, scaling model, harness providers, telemetry default, self-reported case studies
- https://api.github.com/repos/Agent-Field/agentfield - stars, forks, issues, contributors, creation and push dates as of 2026-10-13
- https://api.github.com/repos/Agent-Field/agentfield/releases - the release-candidate-only train, v0.1.142-rc.9 on 2026-10-05
- https://pypi.org/pypi/agentfield/json - agentfield 0.1.141, Apache-2.0, uploaded 2026-09-29
- https://agentfield.ai/ - homepage: the build-like-APIs framing and the control-plane language
- https://agentfield.ai/docs/build/governance/policy - the access-policy documentation: tag ALLOW/DENY semantics, the fail-open no-match default, tag approval workflow, tag VCs, and DID revocations
- https://agentfield.ai/about - founders (Agnostiq, acquired by DataRobot 2025; Covalent) and the partner list
- https://agentfield.ai/pricing.md - one tier at $0, no paid plan, unlimited seats and usage
- https://hn.algolia.com/api/v1/search?query=agentfield&tags=story - the zero-relevant-thread footprint check as of 2026-10-13
- https://medium.com/open-intelligence/agentfield-the-control-plane-that-turns-ai-coding-agents-into-production-infrastructure-63de553e466c - the one independent writeup found (403 to fetchers; read via search excerpt this run)
