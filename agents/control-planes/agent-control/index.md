---
title: Agent Control
created: 2026-10-05
updated: 2026-11-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, policy-enforcement, runtime-governance, open-source]
readability: 3
audience_notes: >
  Engineers who want agent decisions governed by policy held outside the agent's code, and platform teams comparing centralized enforcement gates.
  Assumes you know what a decorator, a policy server, and an evaluator are.
---

Agent Control (agentcontrol/agent-control) is Galileo Technologies' Apache-2.0 control plane, carried into Cisco and Splunk by Cisco's completed 2026-05-22 acquisition of Galileo, that turns any Python or TypeScript function into a governed decision point with a `@control()` decorator, evaluating the call against centrally managed policy on a server and returning deny, steer, warn, log, or allow before the action runs.

**Its thesis is that guardrails hardcoded in agent code rot one repository at a time, so the decorators mark where decisions happen while the policy lives on a server, letting a compliance team change what every agent enforces without a single redeploy.**

## What it is

A Docker Compose deployment of a policy server, a PostgreSQL store, and a web UI; developers install a Python (3.12+) or TypeScript SDK and mark functions with `@control()`, and each decorated call ships its inputs and outputs to the server (or a local cache when configured) for evaluation.
A deny raises a `ControlViolationError` before the unsafe action proceeds.
Built-in evaluators cover regex, list, JSON, and SQL checks, and the architecture is deliberately pluggable: one policy can mix Galileo's Luna, NVIDIA NeMo guardrails, AWS Bedrock checks, Cisco AI Defense guardrails, and custom evaluators.
Framework support covers LangChain, CrewAI, Google ADK, and AWS Strands, with an OpenClaw plugin in the same organization.
The launch blog (March 11, 2026) frames the product against Forrester's agent control plane market evaluation, with launch partners including Cisco, CrewAI, AWS Strands, Glean, Rubrik, and ServiceNow.
The vendor changed hands mid-train: Cisco announced its intent to acquire Galileo on April 9, 2026 and completed it on May 22, 2026, folding Galileo's commercial platform into Splunk Agent Observability, and one of the launch partners ended up the owner; the open-source control plane kept shipping under the agentcontrol organization after the acquisition, and the project site still names Galileo Technologies, Inc.

## Status

Active and young: 327 stars, 55 forks, and 20 contributors as of 2026-10-14, with 50 open issues as of 2026-11-22, created 2026-01-30, and a fast release train (v8.12.0 on 2026-10-09, v8.13.0 on 2026-10-13, v8.14.0 on 2026-10-19, v8.15.0 on 2026-10-23, v8.16.0 on 2026-11-20, v8.17.0 on 2026-11-20, mirrored by agent-control-sdk 8.15.0 on PyPI and the npm agent-control package moving to 3.6.0); the default branch's latest push is the 2026-11-20 v8.17.0 release commit, with the 2026-11-05 pre-release fixes behind it and the 2026-11-09 and 11-21 repo-level pushes side branches. The ownership moved to Cisco and Splunk after the May 2026 Galileo acquisition, and the launch post's galileo.ai URL now redirects to the Splunk Agent Observability product page (a 403 to a browser user agent this run, 200 to a plain fetch).

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
- Cisco and Splunk maintain the project while selling the commercial Agent Observability platform upstream (Galileo folded in), so the open-source roadmap will always answer to the acquirer's funnel; the HN silence means nobody independent has stress-tested the enforcement claims yet.

## Pricing

The control plane is Apache-2.0 and free, self-hosted via Docker Compose with PostgreSQL.
Galileo's commercial evaluation and observability platform, now Splunk Agent Observability under Cisco, integrates with it and is priced separately; no dollar prices are published on the pages cited here, so there is nothing to track.

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
- 2026-10-10 - Release train moved to v8.12.0 (2026-10-09) with agent-control-sdk 8.12.0 on PyPI and the npm package holding at 3.3.0; scale refreshed (324 stars, 20 contributors).
- 2026-10-21 - Full rotation re-verification: every cited URL re-fetched and live, and the release train moved to v8.14.0 (2026-10-19) with agent-control-sdk 8.14.0 on PyPI and the npm package moving to 3.4.0 the same day, ending the 3.3.0 hold.
- 2026-10-25 - Release train moved to v8.15.0 (2026-10-23) with agent-control-sdk 8.15.0 on PyPI and the npm package holding at 3.4.0; the release adds a Galileo Decision Models evaluator.
- 2026-10-31 - Rotation re-verification: every cited URL re-fetched and live, the release train holding at v8.15.0 with agent-control-sdk at 8.15.0 on PyPI and npm holding at 3.4.0, and the status counters refreshed (49 open issues, pushed 2026-10-29); no drift beyond the counters.
- 2026-11-08 - Rotation re-verification: every cited URL re-fetched and live, the release train holding at v8.15.0 with agent-control-sdk at 8.15.0 on PyPI and npm holding at 3.4.0, the default branch's latest push still 2026-11-05 with the repo-level 2026-11-07 push a side branch, and the launch thread still 2 points with zero comments; no drift beyond the counters.
- 2026-11-15 - Rotation re-verification with drift: Cisco completed its acquisition of Galileo Technologies on 2026-05-22 (announced 2026-04-09), folding the commercial platform into Splunk Agent Observability, and the launch post's galileo.ai URL now redirects to the Splunk Agent Observability product page, so the vendor framing moved from Galileo to Cisco and Splunk while the Apache-2.0 project continues under the agentcontrol organization; the launch-post citation stands through the redirect (403 to a browser user agent, 200 plain) and the The New Stack coverage stands behind a site-wide bot wall (its domain root 403s a browser user agent too); the release train holding at v8.15.0 with agent-control-sdk at 8.15.0 on PyPI and npm holding at 3.4.0, the default branch's latest push still 2026-11-05 with the 2026-11-09 repo-level push a side branch, and the launch thread still 2 points with zero comments.
- 2026-11-20 - Release train moved to v8.16.0 (2026-11-20): Orbit binding-list targets are validated locally and before binding authorization (SAO-20817), plus evaluator runtime URL updates; the npm agent-control package moved from 3.4.0 to 3.5.0 alongside the ts-sdk-v3.5.0 tag, ending the 3.4.0 hold; the counters refreshed (50 open issues).
- 2026-11-22 - Release train moved to v8.17.0 (published 2026-11-20): an evaluator runtime-URL revert (#306) beside the release chore that moves the npm agent-control package from 3.5.0 to 3.6.0 with the ts-sdk-v3.6.0 tag; the counters holding (50 open issues).

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [Veto](../veto/index.md) - the local-first authorization kernel this complements
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md) - the broader vendor-backed governance program
- [CrowdStrike Falcon Guardian](../crowdstrike-falcon-guardian/index.md) - the endpoint-anchored commercial counterpart
- [An Agent Is Only as Safe as Its Worst Tool Call](../../../an-agent-is-only-as-safe-as-its-worst-tool-call/index.md) - the corpus argument for gating the call

## References

- https://github.com/agentcontrol/agent-control - README: quickstart, SDKs, evaluator model, framework support, and the insecure-defaults warning
- https://galileo.ai/blog/announcing-agent-control - launch post: the @control() design, deny/steer/warn/log/allow decisions, launch partners, and the Forrester framing (the domain now redirects to Splunk's Agent Observability page after Cisco's 2026-05-22 Galileo acquisition; fetched this run through the redirect)
- https://www.cisco.com/site/us/en/about/corporate-development/acquisitions/galileo/index.html - the acquisition completion page: May 22, 2026, Splunk Observability Cloud integration
- https://www.splunk.com/en_us/about-splunk/acquisitions/galileo.html - the Splunk acquisition page: Galileo now Splunk Agent Observability
- https://www.splunk.com/en_us/products/agent-observability.html - the Agent Observability product page the galileo.ai domain now serves
- https://agentcontrol.dev/ - project site: Control Store, audit logs, and the Galileo maintenance commitment
- https://api.github.com/repos/agentcontrol/agent-control - stars, forks, issues, contributors, creation and push dates as of 2026-10-10
- https://api.github.com/repos/agentcontrol/agent-control/releases - the v8.8.0 through v8.12.0 release train
- https://pypi.org/pypi/agent-control-sdk/json - agent-control-sdk 8.12.0, Apache-2.0
- https://thenewstack.io/galileo-agent-control-open-source/ - independent coverage of the launch
- https://news.ycombinator.com/item?id=47355862 - the 2-point, zero-comment launch thread, the thin community footprint this note records
