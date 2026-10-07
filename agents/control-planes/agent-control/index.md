---
title: Agent Control
created: 2026-10-05
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, policy-enforcement, runtime-governance, open-source]
readability: 3
audience_notes: >
  Engineers who want agent decisions governed by policy held outside the agent's code, and platform teams comparing centralized enforcement gates.
  Assumes you know what a decorator, a policy server, and an evaluator are.
---

Agent Control (agentcontrol/agent-control) is Galileo Technologies' Apache-2.0 control plane that turns any Python or TypeScript function into a governed decision point with a `@control()` decorator, evaluating the call against centrally managed policy on a server and returning deny, steer, warn, log, or allow before the action runs.

**Its thesis is that guardrails hardcoded in agent code rot one repository at a time, so the decorators mark where decisions happen while the policy lives on a server, letting a compliance team change what every agent enforces without a single redeploy.**

## What it is

A Docker Compose deployment of a policy server, a PostgreSQL store, and a web UI; developers install a Python (3.12+) or TypeScript SDK and mark functions with `@control()`, and each decorated call ships its inputs and outputs to the server (or a local cache when configured) for evaluation.
A deny raises a `ControlViolationError` before the unsafe action proceeds.
Built-in evaluators cover regex, list, JSON, and SQL checks, and the architecture is deliberately pluggable: one policy can mix Galileo's Luna, NVIDIA NeMo guardrails, AWS Bedrock checks, Cisco AI Defense guardrails, and custom evaluators.
Framework support covers LangChain, CrewAI, Google ADK, and AWS Strands, with an OpenClaw plugin in the same organization.
The launch blog (March 11, 2026) frames the product against Forrester's agent control plane market evaluation, with launch partners including Cisco, CrewAI, AWS Strands, Glean, Rubrik, and ServiceNow.

## Status

Active and young: 322 stars, 55 forks, 45 open issues, and 19 contributors as of 2026-10-07, created 2026-01-30, pushed 2026-10-07, with a fast release train (v8.8.0 on 2026-09-22, v8.9.0 and v8.10.0 on 2026-10-01, v8.11.0 on 2026-10-02, mirrored by agent-control-sdk 8.11.0 on PyPI and agent-control 3.3.0 on npm).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=agentcontrol/agent-control&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=agentcontrol/agent-control&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=agentcontrol/agent-control&type=date&legend=top-left" />
</picture>

**The community footprint is thin for the backing it carries: the Hacker News launch thread drew 2 points and zero comments, so the adoption evidence is the release cadence, the contributor count, and the launch-partner list rather than organic discussion.**
A version line already at v8 eight months in says the API moves; the README's own quickstart warns that the default compose file starts without API keys configured, which it calls dangerous for any real-world usage.

## Strengths

- The decorator-plus-server split is the right factoring for fleet governance: developers own where the hooks sit, policy teams own what they enforce, and policy changes need no redeploy.
- Pluggable evaluators mean the gate is not married to one vendor's detection models, which is rare among the enforcement gates in this category.
- Decisions include steer and warn, not just allow and deny, so the plane can correct an agent instead of only stopping it.
- Real software hygiene: CI, Codecov, both SDK ecosystems published, and a UI dashboard included in the open-source deployment.

## Cautions

- Enforcement quality equals evaluator quality: a regex list blocks what it anticipates, exactly the failure mode the launch anecdote describes, and nothing here substitutes for tool-level design.
- Every governed call crosses a network hop to the policy server unless a local cache is configured, which adds latency and a new failure point to the agent's critical path.
- The quickstart's own insecure-by-default warning means the first-run experience trains the wrong habits; read the API key configuration before exposing anything.
- Galileo maintains the project while selling a commercial platform upstream, so the open-source roadmap will always answer to the funnel; the HN silence means nobody independent has stress-tested the enforcement claims yet.

## Pricing

The control plane is Apache-2.0 and free, self-hosted via Docker Compose with PostgreSQL.
Galileo's commercial evaluation and observability platform integrates with it and is priced separately; no dollar prices are published on the pages cited here, so there is nothing to track.

## Compared to

- [Veto](../veto/index.md): both gate calls before execution, but Veto evaluates deterministic YAML rules locally with portable receipts, while Agent Control centralizes policy on a server with pluggable vendor evaluators; choose Veto for a local-first gate, Agent Control for fleet-wide policy without redeploys.
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md): the toolkit ships identity, sandboxing, SRE, and compliance alongside policy; Agent Control is narrower and deeper on the step-level enforcement axis with the evaluator marketplace.
- [Code Atelier Governance SDK](../code-atelier-governance-sdk/index.md): both put a gate in front of LLM calls, but Code Atelier is an in-process Python and Postgres SDK with an HMAC audit chain, while Agent Control externalizes policy to a server with a UI and cross-language SDKs.

## Bottom line

**Recommended for platform teams standardizing runtime guardrails across many agents and frameworks who can run a policy server and want policy changes to land without redeploys.**
Not for local-first or latency-critical enforcement, and not for anyone who needs independent validation of the enforcement claims before adopting a gate.

## Changes

- 2026-10-05 - Created from the entrant-resolution run, profiling Galileo's open-source control plane as the category's centralized-policy-server entrant.
- 2026-10-07 - Added the agentcontrol/agent-control star history chart to the Status section.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [Veto](../veto/index.md) - the local-first authorization kernel this complements
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md) - the broader vendor-backed governance program
- [CrowdStrike Falcon Guardian](../crowdstrike-falcon-guardian/index.md) - the endpoint-anchored commercial counterpart
- [An Agent Is Only as Safe as Its Worst Tool Call](../../../an-agent-is-only-as-safe-as-its-worst-tool-call/index.md) - the corpus argument for gating the call

## References

- https://github.com/agentcontrol/agent-control - README: quickstart, SDKs, evaluator model, framework support, and the insecure-defaults warning
- https://galileo.ai/blog/announcing-agent-control - launch post: the @control() design, deny/steer/warn/log/allow decisions, launch partners, and the Forrester framing
- https://agentcontrol.dev/ - project site: Control Store, audit logs, and the Galileo maintenance commitment
- https://api.github.com/repos/agentcontrol/agent-control - stars, forks, issues, contributors, creation and push dates as of 2026-10-06
- https://api.github.com/repos/agentcontrol/agent-control/releases - the v8.8.0 through v8.11.0 release train
- https://pypi.org/pypi/agent-control-sdk/json - agent-control-sdk 8.11.0, Apache-2.0
- https://thenewstack.io/galileo-agent-control-open-source/ - independent coverage of the launch
- https://news.ycombinator.com/item?id=47355862 - the 2-point, zero-comment launch thread, the thin community footprint this note records
