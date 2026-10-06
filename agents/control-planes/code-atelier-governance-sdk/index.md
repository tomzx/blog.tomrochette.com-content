---
title: Code Atelier Governance SDK
created: 2026-09-27
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, agent-governance, policy-enforcement, audit-trail, postgres, human-in-the-loop]
readability: 3
audience_notes: >
  Python engineers who want enforcement gates in front of LLM calls without adding infrastructure, and who will read a threat model before trusting a security boundary.
  Assumes you know what an HMAC chain is and that observability is not enforcement.
---

The Code Atelier Governance SDK (code-atelier-governance) is an MIT-licensed Python SDK that wraps LLM clients and tool calls in pre-execution enforcement gates (scope, budget, approvals, loop detection, presence) and writes an HMAC-chained audit trail to the Postgres your application already runs.

**Its thesis is that tracing tools explain what an agent did after the damage, so the useful primitive is a gate that fires before the LLM call and denies it, backed by an audit chain a regulator can verify without a new data platform.**

## What it is

`pip install code-atelier-governance` exposes a `GovernanceSDK` with eight modules: Audit, Scope, Cost, Gates, Loop Detection, Presence, Contracts, and Compliance.
Scope is a per-agent allowlist with hidden tools removed from the LLM context and default deny; Cost enforces token and USD caps per session and per agent-day with built-in pricing for more than twenty models and a combined budget query; Gates issues single-use HMAC-bound approval tokens for high-risk actions.
The audit trail is an append-only HMAC chain with optional Ed25519 per-row signatures, on-demand chain verification, and EU AI Act Article 12 evidence reports.
Integrations are one-line wrappers for OpenAI, Anthropic, and LangChain, plus a sync wrapper for Flask and Django, and everything depends only on a Postgres connection string, with an optional read-only console.
The vendor is Code Atelier, and the source lives at imleopereira/agentic-governance.

## Status

Dormant since July 2026 and essentially unadopted.
The SDK is at version 0.7.3 with 11 PyPI releases, and the repository was created 2026-04-09 with its last source push on 2026-07-23, more than two months before this check (as of 2026-10-06).
The repository has 0 stars, 0 forks, and no description or topics, which is unusual for a project with a polished documentation site and a hosted platform bridge.
**The community footprint is absent: a Hacker News search for Code Atelier governance returns nothing, so every claim here rests on the vendor's own pages and the repository.**
**What earns the note despite the silence is the threat model, which states plainly what the SDK does not protect against instead of implying it is a complete security boundary.**
The vendor also publishes a scaffolder that wires a Microsoft Agent Governance Toolkit agent through these gates, which is a rare, concrete interoperability gesture in this category.

## Strengths

- Just Postgres: no Redis, Kafka, ClickHouse, sidecar, or background worker, so adoption cost is close to zero for a team already on Postgres.
- Fail-closed enforcement by default (cost, scope, and gates raise), while observation surfaces warn and continue, which is the right asymmetry.
- A written threat model that names the bypasses (direct client calls, subprocesses, tool calls inside LLM responses) rather than hiding them.
- EU AI Act Article 12 evidence export and a self-approval prevention design show the compliance audience is being taken seriously.

## Cautions

- 0 stars and no third-party usage evidence; the only assessment available is the vendor's own.
- In-process gates do not defend against a second process or any code path that calls OpenAI or Anthropic directly, and the README says so; network-level enforcement needs a proxy.
- Scope enforcement gates the LLM call, not the tool calls returned inside the response, so a determined agent can still execute a disallowed tool unless you enforce at the tool layer too.
- Tampering is detected only when verification runs; a database administrator with key control can still replace the chain, as the threat model admits.
- v0.6.2 flipped several defaults to fail-closed and broke callers, so read the upgrade notes before following an older tutorial.

## Pricing

MIT licensed and free.
A hosted platform exists through an opt-in bridge that dual-writes audit events while keeping local Postgres authoritative, plus a read-only console, but no prices are published.

## Compared to

- [Veto](../veto/index.md): a framework-agnostic authorization kernel with a commercial cloud and portable receipts; choose Veto for TypeScript or polyglot stacks and this SDK when you are Python and Postgres and want budget and loop gates too.
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md): broad, vendor-backed, and multi-language with identity and sandboxing; choose AGT for a governance program, and this SDK for the smallest viable gate.
- [Langfuse](../../evaluation-review/langfuse/index.md): observability that records what happened; choose Langfuse to understand agent behavior, and this SDK to block a call before it happens.

## Bottom line

**Recommended for Python teams already on Postgres that want a minimal pre-execution gate with budgets, approvals, and a tamper-evident audit trail. Not for polyglot stacks, teams needing process or network-level enforcement, or anyone who requires an adopted project with independent security review.**

## Changes

- 2026-09-27 - Created.
- 2026-10-02 - Moved the status to dormant (no source push since 2026-07-23) and added the missing llm=glm-5.3-flash tag; version 0.7.3 re-verified as current on PyPI.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category compared on shared rows
- [Veto](../veto/index.md) - the authorization-kernel alternative with a commercial cloud
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md) - the broad multi-language alternative
- [An Agent Is Only as Safe as Its Worst Tool Call](../../../an-agent-is-only-as-safe-as-its-worst-tool-call/index.md) - the corpus argument for gating the call
- [Evaluation Review Feature Matrix](../../evaluation-review/evaluation-review-feature-matrix/index.md) - the observability layer this deliberately is not

## References

- https://www.codeatelier.tech/governance - overview: modules, comparison table, Article 12 framing
- https://www.codeatelier.tech/governance/quickstart - quickstart: install, schema, gates, console, sync wrapper
- https://github.com/imleopereira/agentic-governance - README: modules, threat model, configuration, standards
- https://api.github.com/repos/imleopereira/agentic-governance - stars, forks, creation and push dates as of 2026-10-06
- https://pypi.org/pypi/code-atelier-governance/json - version 0.7.3, MIT license, 11 releases
- https://raw.githubusercontent.com/imleopereira/agentic-governance/production/CHANGELOG.md - release notes: fail-closed defaults and the AGT recipe scaffolder
