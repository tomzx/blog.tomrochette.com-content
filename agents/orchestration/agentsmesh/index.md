---
title: AgentsMesh
created: 2026-10-02
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, agent-fleet, self-hosted, bsl]
readability: 3
audience_notes: >
  Team leads who want to run many AI coding agents across shared machines with tickets, channels, and automated loops in one console.
  Assumes you know Docker and at least one coding harness.
---

AgentsMesh is a BSL-1.1, self-hosted platform that turns remote machines into managed AgentPods and runs fleets of AI coding agents across them with tickets, channels, multi-agent collaboration, and automated loops from one console.

**Its bet is fleet operations as the product: not one agent with a nice worktree, but a hundred agents across your machines with a console that treats pods, tickets, and loops as first-class objects.**

## What it is

A Docker-deployed platform with a web console, built by a founder-led team and distributed through Docker Hub with a demo video and Discord support.
The unit of compute is the AgentPod, a remote AI workstation you register; work is tracked as tickets, coordinated in channels, and automated through loops with an AgentFile layer and MCP tools connecting agents to the platform.
It drives Claude Code, Codex CLI, Gemini CLI, Aider, and OpenCode, plus custom agents over MCP, and covers git repository connection and team management in the same console.
The license is Business Source License 1.1, source-available with a conversion date, not OSI open source.

## Status

Active but maturing slowly: 2,361 stars as of 2026-10-06, created 2026-02-28, pushed 2026-09-23, with the last tagged release v0.44.7 on 2026-07-25 and development continuing on the default branch since.

<a href="https://www.star-history.com/?repos=AgentsMesh%2FAgentsMesh&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=AgentsMesh/AgentsMesh&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=AgentsMesh/AgentsMesh&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=AgentsMesh/AgentsMesh&type=date&legend=top-left" />
 </picture>
</a>

**The adoption record is thin: a 3-point Show HN thread in March 2026 is the only independent footprint, so the hundred-agent story rests on the vendor's demo, not field reports.**
The docs are unusually complete for that traction (quick start through full API reference), which is the strongest credibility signal the project has.

## Strengths

- The pod model targets real fleet problems: register machines, distribute agents, and steer the whole set from one console instead of one terminal per agent.
- Tickets, channels, and loops in one place close the plan-track-automate loop that most orchestration tools split across three products.
- Multi-harness by design (Claude Code, Codex, Gemini CLI, Aider, OpenCode) with custom agents over MCP, so the console outlives any single vendor's CLI.
- Documentation depth (per-object API references, AgentFile layer) suggests an actual multi-tenant design rather than a wrapper script.
- Docker Hub distribution keeps self-hosting concrete: pull, configure, run.

## Cautions

- BSL 1.1 means you can use it but not offer it as a competing service, and the source-available window has a conversion date rather than being open now.
- Nine days without a push at verification time and no release since July 2026: the release cadence lags the branch, so pinning is guesswork.
- No independent usage evidence: the community footprint is one 3-point Show HN thread and a Discord.
- The hundred-agent claim is untested in public; pod scheduling behavior under real contention is not documented with numbers.
- Solo-console architecture concentrates state (tickets, channels, loop history) in one platform you must back up like any database.

## Pricing

Free to self-host under BSL 1.1 for internal use.
You pay your own machines and model subscriptions; the docs and site list no hosted tier and no license fees.

## Compared to

- [Agent Swarm](../agent-swarm/index.md): MIT and lead/worker with chat intake; AgentsMesh is BSL-licensed and built on a pod-and-ticket model, closer to an internal platform than a bot.
- [Gas Town](../gastown/index.md): tmux-town supervision for one powerful machine; AgentsMesh spreads the fleet across registered remote pods.
- [Omnara](../omnara/index.md): hosted control plane with mobile supervision; AgentsMesh keeps the fleet and the console on your own hardware.

## Bottom line

**Recommended for platform teams that want a self-hosted console treating agent fleets as pods, tickets, and loops, and can live with a BSL license.**
Not for open-source-license purists, solo users (a worktree manager is lighter), or anyone who needs proof of hundred-agent scale before adopting.

## Changes

- 2026-10-02 - Created.
- 2026-10-03 - Reworded a banned-term compound out of the Compared-to prose; meaning unchanged.
- 2026-10-07 - Added the AgentsMesh/AgentsMesh star history chart to the Status section.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Agent Swarm](../agent-swarm/index.md) - the MIT lead/worker alternative with chat intake
- [Gas Town](../gastown/index.md) - the single-machine tmux supervision town
- [Omnara](../omnara/index.md) - the hosted control-plane counterpart
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this category extends

## References

- https://github.com/AgentsMesh/AgentsMesh - repository, BSL-1.1 license, stars, pod and loop architecture, and the push record as of 2026-10-02
- https://agentsmesh.ai/docs - the AgentPod, ticket, channel, loop, AgentFile, and MCP-tools documentation with the supported-harness list
- https://github.com/AgentsMesh/AgentsMesh/releases - the v0.44.7 release (2026-07-25) anchoring the version and cadence claims
- https://hub.docker.com/u/agentsmesh - the Docker Hub distribution used by the self-hosting path
- https://news.ycombinator.com/item?id=47252334 - the March 2026 Show HN thread (3 points), the project's only independent community footprint
