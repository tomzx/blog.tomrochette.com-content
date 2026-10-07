---
title: PraisonAI
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, python, low-code]
readability: 3
audience_notes: >
  Engineers evaluating low-code multi-agent frameworks who know CrewAI and
  AutoGen by name and want to know what this third option adds and what its
  security record says. Assumes basic Python.
---

PraisonAI is a Python low-code framework that assembles multi-agent workforces with self-reflection loops, a dashboard UI, MCP support, and approval gates.

## What it is

PraisonAI, created 2024-03-19 and MIT-licensed, packages agents, tools, MCP servers, guardrails, and approval hooks behind a low-code surface with a dashboard, and ships both a Python package (`praisonaiagents`) and desktop builds.
Its own framing puts a harness around every agent ("Agent = Model + Harness"), with `run_on="docker"` for self-hosted isolation and `approval=True` for human gates before risky tools run.
It sits in this category's low-code family beside Dify and Sim, closer to the code-first end of that spectrum.

## Status

Active and shipping fast: 9,192 stars, a push on 2026-10-07, release v4.7.12 on 2026-10-02, and `praisonaiagents` 1.7.10 on PyPI as of 2026-10-07 (GitHub API, PyPI), on a repository created 2024-03-19.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=MervinPraison/PraisonAI&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=MervinPraison/PraisonAI&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=MervinPraison/PraisonAI&type=date&theme=dark&legend=top-left" />
</picture>

**The critical record matters more than the star count here: a 2026-08-03 GitHub advisory (GHSA-5r6c-gj4g-r697) reported that SecurityPolicy command, path, and import restrictions were completely unenforced by the default SubprocessSandbox backend, so the sandbox story deserves direct verification before you lean on it.**
Press traction is thin, two 2-point Hacker News threads in July 2024, while the README carries a "Highlighted by Elon Musk" badge linking an X post I could not fetch (X serves no machine-readable pages), so I record the badge as a claim and the HN record as the measurable footprint.

## Strengths

- Breadth under one roof: agents, MCP, tools, guardrails, approval gates, and Docker isolation with a dashboard on top.
- MIT license and an active release train across a v4 major line.
- The approval-gate and self-reflection abstractions map directly onto human-in-the-loop workflows.

## Cautions

- The 2026 sandbox-enforcement advisory is the reason to read the current sandbox documentation before trusting `sandbox=` in production.
- One dominant maintainer and a sprawling surface (Python package, desktop builds, dashboard, MCP servers, install script) concentrate bus risk.
- The v4 line and daily-level releases mean interfaces can move under a low-code promise of stability.

## Pricing

Free, open source under the MIT license; no paid tier found.

## Compared to

CrewAI is the role-and-crew framework with a funded enterprise platform; choose it for commercial support, PraisonAI for the wider built-in tool surface.
AutoGen and its AG2 fork are conversation-centric; PraisonAI is workflow-and-workforce-centric.
Dify and Sim are visual-first business-app builders; PraisonAI stays closer to the code.

## Bottom line

Recommended for Python teams that want a self-hosted, low-administration multi-agent stack with approval gates and MCP in one package, and that will verify the sandbox behavior against the advisory themselves.
Not for security-sensitive deployments that need a vendor's incident track record behind the isolation layer.

## Changes

- 2026-10-07 - Created.

## See also

- [CrewAI](../crewai/index.md) - the closest funded alternative in the Python multi-agent family.
- [AutoGen](../autogen/index.md) - the conversation-centric framework whose frozen state reshaped this whole family.
- [Dify](../dify/index.md) - the visual-first member of the low-code family this note sits in.
- [Sim](../sim/index.md) - the Apache-2.0 visual builder alternative.

## References

- https://github.com/MervinPraison/PraisonAI - the repository, README harness framing, stars, and license.
- https://docs.praison.ai/ - the documentation site.
- https://pypi.org/project/praisonaiagents/ - the Python package and its current 1.7.10 version.
- https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-5r6c-gj4g-r697 - the 2026-08-03 advisory on unenforced SecurityPolicy restrictions in the default SubprocessSandbox backend.
- https://praison.ai - the install entry point the README's curl line uses.
- https://news.ycombinator.com/item?id=40885570 - the 2-point July 2024 launch thread, the measurable press footprint.
