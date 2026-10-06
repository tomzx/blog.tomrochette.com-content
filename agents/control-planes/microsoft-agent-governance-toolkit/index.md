---
title: Microsoft Agent Governance Toolkit
created: 2026-09-27
updated: 2026-10-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, agent-governance, policy-enforcement, zero-trust, compliance, microsoft]
readability: 3
audience_notes: >
  Engineers deciding how to put deterministic guardrails around autonomous agents, and who need to separate what this toolkit actually enforces from what its README lists.
  Assumes you know what a policy engine is and that prompt-level instructions are not a security control.
---

The Microsoft Agent Governance Toolkit (microsoft/agent-governance-toolkit) is an MIT-licensed, multi-language toolkit that intercepts each agent tool call, message send, and delegation in application code and evaluates it against policy before the action reaches the wire.

**Its thesis is that prompt-level safety is a polite request to a stochastic system, so governance belongs in deterministic code outside the model, and this is the most complete shipping expression of that idea: policy, identity, sandboxing, SRE, and compliance in one repository.**

## What it is

`pip install "agent-governance-toolkit[full]"` installs a policy engine with YAML, OPA Rego, and Cedar support, plus a `govern()` wrapper that checks, logs, and enforces every tool call.
The packages are Agent OS (policy), Agent Mesh (DID identity and trust scoring), Agent Runtime (execution rings and sandboxing), Agent SRE (SLOs, circuit breakers, kill switch), Agent Compliance (OWASP and EU AI Act mapping), Agent Marketplace, Agent Lightning, and Agent Hypervisor.
SDKs exist for Python, TypeScript, .NET, Rust, and Go, with first-party plugins for Claude Code, Copilot CLI, Codex CLI, and OpenCode, and adapters for LangGraph, CrewAI, the OpenAI Agents SDK, Semantic Kernel, and Microsoft Agent Framework.
It is published under the Microsoft organization, but the team states an intent to move it to a foundation, and the README calls it a public preview that may break before GA.

## Status

Active, wide, and fast-moving: 6,392 stars, 1,131 forks, and 74 open issues as of 2026-10-05, created 2026-03-02, last pushed 2026-10-04, latest release v4.1.0 on 2026-06-09.
**The community footprint is thin relative to the star count: the Hacker News submissions I found top out at 6 points, and the most substantive third-party writeup is a security critique rather than a tutorial.**
That critique (April 26, 2026) found a caller-controlled `X-Agent-ID` header flowing into audit, policy, and rate-limit consumers with no verification, six exported security primitives with zero production callers, and an in-memory audit log that breaks its own integrity check on overflow.
The project has since shipped several breaking refactors, but I could not confirm from primary sources that the specific wiring gaps are closed, so treat the critique as a pre-adoption checklist rather than a resolved incident.

## Strengths

- The only toolkit in this category that ships policy, identity, sandboxing, SRE, and compliance as one spec-backed product, with formal RFC 2119 specifications and hundreds of conformance tests.
- Genuinely polyglot: five language SDKs and framework adapters, so governance does not dictate your stack.
- Deterministic and fail-closed at the interception point, which is the correct place to enforce anything that must not happen.
- Vendor-backed with the open-source fundamentals most tools here lack (CodeQL, continuous fuzzing, OpenSSF Scorecard, a published security policy).

## Cautions

- The April 2026 critique is the strongest published skeptical source in this whole category; confirm that identity is authenticated on your request path and that audit storage is durable before trusting the landing page.
- Public preview with breaking changes between minor versions; pin deliberately and read BREAKING_CHANGES before upgrading.
- Governance runs in application middleware, not at the OS kernel, and the README recommends one container per agent for real isolation.
- Breadth is a cost: seven packages and ten specifications is a large surface to evaluate for a small team.

## Pricing

MIT licensed and free, self-hosted, no paid tier.
Deployment guides cover Azure, AWS, GCP, and Docker Compose.

## Compared to

- [Veto](../veto/index.md): a narrower, single-purpose authorization kernel with a commercial cloud; choose Veto for one gate in front of risky tool calls, and this toolkit for a governance program across languages and frameworks.
- [SIDJUA](../sidjua/index.md): a self-hosted orchestrator with pre-action enforcement baked into the runtime; choose SIDJUA for a small always-on agent company, and this toolkit when the agents and frameworks already exist.
- [Code Atelier Governance SDK](../code-atelier-governance-sdk/index.md): a Python and Postgres-only enforcement SDK; choose it for a minimal footprint, and this toolkit for multi-language coverage and identity.

## Bottom line

**Recommended for platform teams standardizing deterministic agent governance across multiple languages and frameworks, who can independently verify the enforcement wiring. Not for single-agent projects or teams that want a thin, drop-in gate, since the surface is large and the preview churn is real.**

## Changes

- 2026-09-27 - Created.
- 2026-10-02 - Added the missing llm=glm-5.3-flash tag from this maintenance run; volatile numbers refreshed in place.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category compared on shared rows
- [Veto](../veto/index.md) - the narrower authorization-kernel alternative
- [SIDJUA](../sidjua/index.md) - the orchestration-plus-governance alternative, now frozen
- [An Agent Is Only as Safe as Its Worst Tool Call](../../../an-agent-is-only-as-safe-as-its-worst-tool-call/index.md) - the corpus argument this toolkit operationalizes
- [Sandboxing Feature Matrix](../../sandboxing/sandboxing-feature-matrix/index.md) - the isolation layer the execution rings overlap with

## References

- https://github.com/microsoft/agent-governance-toolkit - README: packages, quickstart, specs, preview notice, security boundaries
- https://api.github.com/repos/microsoft/agent-governance-toolkit - stars, forks, issues, push date as of 2026-10-05
- https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/ - launch post: seven packages, OWASP mapping, foundation intent
- https://www.flyingpenguin.com/authentication-bypass-in-microsoft-agent-governance-toolkit-at-573f989/ - critical security review of identity wiring and audit durability
- https://api.github.com/repos/microsoft/agent-governance-toolkit/releases - v4.1.0, 2026-06-09
- https://pypi.org/pypi/agent-governance-toolkit/json - distribution and version 4.1.0
