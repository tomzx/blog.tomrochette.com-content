---
title: Agent Swarm
created: 2026-10-02
updated: 2026-10-03
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, lead-worker, docker, slack, multi-agent]
readability: 3
audience_notes: >
  Engineers who want task intake from chat and issue trackers to land as pull requests through a self-hosted lead/worker agent system.
  Assumes you know Docker Compose and already run at least one CLI coding harness.
---

Agent Swarm is an MIT-licensed, self-hosted lead/worker orchestration platform where a lead agent takes tasks from Slack, GitHub, GitLab, Linear, email, or an API and delegates them to worker agents running in isolated Docker containers.

**Its bet is that delegation should start where work already arrives, in chat and issue trackers, and end where work is judged, in pull requests, with memory and identity persisting across every session in between.**

## What it is

A Docker Compose (or Helm on Kubernetes) deployment built by Desplega Labs, the company behind desplega.sh.
A lead agent plans and assigns subtasks through an MCP API server over SQLite, workers execute inside their own containers with full dev environments, and results ship as PRs, Slack replies, or email.
It drives Claude Code (recommended), Codex, pi, Devin, Claude Managed Agents, an experimental in-process opencode server, and any ACP-speaking agent.
Around that core it layers a dashboard UI, DAG workflows with human-in-the-loop gates, scheduled tasks, a skills system, vector-searchable shared memory, persistent per-agent identity, and an E2B-backed eval harness.

## Status

Active and shipping fast: 851 stars, 106 forks, 25 contributors, and 14 open issues and pull requests as of 2026-10-03, created 2025-12-19, with the default branch pushed the same day and docs updated October 2, 2026 at v1.161.0.
**The adoption evidence is real but early: a 63-point Show HN thread in February 2026 and a live public demo, with the production claims (a customer with 80% of its team onboarded and over 800 human-initiated tasks weekly) self-reported by the vendor.**
The README's own tip that the repo "evolves every single day" is the plain read of the risk: this is a high-velocity single-vendor product, not a community project.

## Strengths

- Intake where work already lives: Slack DMs, repo @mentions, Linear tickets, and email all become tasks without a dashboard visit.
- Real isolation, one container per worker, with git, Node.js, and Python preinstalled, so a runaway task cannot trash your machine.
- Memory and identity that compound: learnings are extracted after each session and recalled later, with citation ratings on by default.
- Schema-validated task results and deferred tasks (wake when watched tasks finish or a deadline hits) make it scriptable from outside the dashboard.
- Harness-agnostic workers, so a swarm can mix Claude Code and Codex under one lead.

## Cautions

- Every production number on the site is vendor-reported; the public demo is a shared workspace where submitted tasks are visible to everyone.
- The stack expects you to run Docker Compose or Kubernetes and bring your own model keys, so the operational floor is higher than a desktop app in this category.
- Single SQLite database as the coordination store keeps small swarms simple and sets the ceiling for larger ones.
- The velocity is churn: the docs tell you to watch the repo because it changes daily, which is a poor fit for teams that pin versions.
- Desplega Labs sells setup calls and services around the open-source core, so some documentation reads as a funnel.

## Pricing

Free and open source under MIT, self-hosted on infrastructure you control.
There is no paid tier; you pay your infrastructure and inference providers directly, and the vendor sells optional human setup calls rather than software licenses.

## Compared to

- [OpenRig](../openrig/index.md): OpenRig defines a team of persistent tmux seats in YAML on your own machine; Agent Swarm is heavier (Docker, a database, a dashboard) but adds chat intake, workflows, and scheduled work.
- [Omnara](../omnara/index.md): Omnara supervises agents from a hosted control plane with mobile reach; Agent Swarm keeps execution inside your own containers.
- [Gas Town](../gastown/index.md): Gas Town is a tmux-town for supervising many agents on one box; choose it for local supervision, Agent Swarm for company-scale task routing with isolation.

## Bottom line

**Recommended for teams that want chat-and-issue-tracker intake to turn into reviewed pull requests through isolated worker agents they host themselves.**
Not for solo local parallelism (a worktree manager is lighter) or for anyone who needs a slow-moving, community-governed dependency.

## Changes

- 2026-10-02 - Created.
- 2026-10-03 - Reworded a banned-term word out of the prose and refreshed the volatile counts; meaning unchanged.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [OpenRig](../openrig/index.md) - the lighter YAML-defined control plane over real terminal sessions
- [Omnara](../omnara/index.md) - the hosted control-plane counterpart
- [Gas Town](../gastown/index.md) - the local tmux supervision town
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this category extends

## References

- https://github.com/desplega-ai/agent-swarm - repository, MIT license, stars, forks, contributors, and push activity as of 2026-10-02
- https://docs.agent-swarm.dev - feature list, architecture (MCP API server, SQLite, Docker workers), and harness support, docs at v1.161.0 updated 2026-10-02
- https://docs.agent-swarm.dev/docs/guides/harness-configuration - the Claude Code, Codex, pi, Devin, Claude Managed Agents, opencode, and ACP harness setup
- https://raw.githubusercontent.com/desplega-ai/agent-swarm/main/MCP.md - schema-validated send-task results and deferred-task semantics
- https://www.agent-swarm.dev - self-hosting positioning, public demo, and the vendor-reported Capchase adoption claims
- https://www.agent-swarm.dev/case-studies/capchase - the customer case study behind the self-reported numbers
- https://news.ycombinator.com/item?id=47165046 - the February 2026 Show HN thread (63 points, 46 comments), the main independent community footprint
