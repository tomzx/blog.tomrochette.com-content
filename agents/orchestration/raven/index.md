---
title: Raven
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, dag-planning, host-agent, self-hosted, benchmarking]
readability: 3
audience_notes: >
  Engineers evaluating self-hosted multi-agent platforms, who need both an architecture read and a provenance read.
  Assumes you know what a DAG, a coding harness, and a benchmark leaderboard are.
---

Raven is EverMind-AI's Apache-2.0 "harness of harnesses": a self-hosted host agent that plans work as a DAG and orchestrates its own Research, Code, Design, and Oncall agents alongside Claude Code and Codex.

**Raven pairs one of the more interesting architectures in this category with its most instructive launch failure: the authors posted AI-generated comments to their own Hacker News thread, and the pitch's "recursive self-improvement" is, as one commenter put it, loops.**

## What it is

A self-hosted platform where a Host Agent decomposes a task into a DAG and dispatches the nodes to built-in agents (Raven-Research for deep research, Raven-Code for software development, Raven-Design for visual design, Raven-Oncall for unattended automation) or to external harnesses such as Claude Code and Codex.
It ships sandboxing, sub-agents, channels, Docker deployment, and trajectory replay, plus Evolver, a separate tool that consumes Raven as a library and evaluates candidate harness changes.
The README claims its agents beat Claude Code on both quality and cost in its own ArtifactsBench benchmarks, which are self-published.
Apache-2.0, self-hosted, by EverMind-AI, with a technical report released as its own GitHub release on 2026-09-27.

## Status

Active and very early: 5,213 stars and 149 forks as of 2026-10-05, created 2026-05-21, with 35 contributors and v0.2.4 out on 2026-10-03 after five releases in September.

[![Star History Chart](https://api.star-history.com/chart?repos=EverMind-AI/Raven&type=date&legend=top-left)](https://www.star-history.com/?repos=EverMind-AI%2FRaven&type=date&legend=top-left)

The Show HN thread from 2026-09-29 drew 55 points and about 51 comments, and it is where the launch went wrong: dang, Hacker News's moderator, asked the authors to stop posting AI-generated or AI-edited comments, which site rules prohibit.
The same thread produced the sharpest one-line critique of the positioning: "it is loops", with no weight updates anywhere in the system.

## Strengths

- The DAG-planning host over heterogeneous agents (its own four plus Claude Code and Codex) is a design most columns approximate with a lead agent and optimism.
- Trajectory replay provides run-level audit, the feature Atlas built an entire product around, included here.
- Evolver, which treats the harness itself as the thing under test, is the most original idea in this batch of entrants.
- Shipping velocity: five releases in September 2026 plus a technical report.

## Cautions

- The launch carried a moderation warning about AI-generated comments, which is exactly the trust failure an agent company cannot afford.
- The recursive-self-improvement framing oversells: the self-evolution mechanism the README describes is generate-and-test over candidate changes, which is loops, and I found no training-loop evidence anywhere in the sources.
- The benchmark claims (beating Claude Code on quality and cost on ArtifactsBench) come from the project's own dashboards and should be treated as marketing until someone reproduces them.
- 0.2.x versioning with 92 open issues as of 2026-10-05: expect API churn.

## Pricing

Free and open source under Apache-2.0, self-hosted on your own hardware or Docker host.
No hosted tier recorded and no Raven bill.

## Compared to

- [Agent Swarm](../agent-swarm/index.md): the other self-hosted platform that turns orchestration into Docker-isolated workers and pull requests; choose Agent Swarm for intake-to-PR pipelines, Raven for DAG-planned heterogeneous teams with its own agents.
- [oh-my-codex](../oh-my-codex/index.md): the single-CLI enhancement path; choose it for Codex-only depth, Raven for multi-agent breadth.
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md): lead-and-worker tmux with adversarial verification; choose it for minimal infrastructure, Raven for sandboxing, replay, and a platform.

## Bottom line

**Recommended for self-hosting teams who want DAG-planned heterogeneous agents and will independently verify both the benchmarks and the comments.**
Not for anyone who needs a clean provenance story today or stable APIs before 1.0.

## Changes

- 2026-10-06 - Created.
- 2026-10-07 - Added the EverMind-AI/Raven star history chart to the Status section.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Agent Swarm](../agent-swarm/index.md) - the Docker-worker platform rival
- [oh-my-codex](../oh-my-codex/index.md) - the single-CLI contrast
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md) - the adversarial-verification lead/worker harness
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this category extends

## References

- https://api.github.com/repos/EverMind-AI/Raven - stars, forks, Apache-2.0 license, creation date, and push date as of 2026-10-05
- https://raw.githubusercontent.com/EverMind-AI/Raven/main/README.md - the DAG host agent, built-in agents, Evolver, and the benchmark claims
- https://evermind-ai.github.io/Raven/ - the documentation site
- https://api.github.com/repos/EverMind-AI/Raven/releases - v0.2.4 (2026-10-03), the September cadence, and tech-report-v1 (2026-09-27)
- https://raven.evermind.ai - the "harness of harnesses, built for RSI" positioning
- https://news.ycombinator.com/item?id=49890647 - the Show HN thread, dang's AI-comments warning, and the loops critique
