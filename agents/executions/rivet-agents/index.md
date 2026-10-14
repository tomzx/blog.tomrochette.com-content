---
title: Rivet Agents
created: 2026-10-13
updated: 2026-10-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, executions, durable-execution, scheduling, actor-model]
readability: 3
audience_notes: >
  Product engineers who want long-lived coding agents embedded in an application, deciding between a durable process runtime and the task-run platforms this category already holds.
  Assumes you know what an actor model, SQLite, and cron are.
---

Rivet Agents is the Apache-2.0 runtime from Rivet that runs a coding agent as one durable process per key, with its conversation and files in an Actor's SQLite database, woken by cron schedules, one-shot timed calls, HTTP and WebSocket requests, or app connectors.

**It is the durable-execution member of this category whose unit is a process, not a run: the agent sleeps between scheduled prompts and wakes with its conversation intact, and the catch is that the platform is young, on a v0.x line, and its headline durability numbers are the vendor's own.**

## What it is

You define the agent once in your backend with rivetkit, and every key you call it with gets its own Actor, conversations, and files.
File tools work on the Actor's SQLite database with no sandbox; add one (E2B or Daytona through the sandbox adapter) and shell tools run there, with provider keys staying in your backend and never entering the sandbox.
The agent harness is Pi (Earendil's Pi Durable package, beta), with your own model, your own keys, or your users' own subscriptions.
It is built by Rivet Gaming, Inc. (YC, a16z Speedrun), the company behind the rivet-dev/rivet control plane, and the repository is a monorepo renamed from sandbox-agent that carries Rivet Agents plus the Sandbox Agent HTTP control layer on one version line, v0.5.2 newest (2026-10-08).

## Status

**Active, young, and moving fast.**
1,604 stars, 134 forks, and 87 open issues and pull requests as of 2026-10-13 (GitHub API), created 2026-01-25 and pushed 2026-10-14 UTC.
The release train reached a stable v0.5.0 only on 2026-10-07 after release candidates that began in March, with v0.5.1 and v0.5.2 following within two days, and the company changelog shipped agentOS 0.4 with Hosted VMs on 2026-10-12.
The community footprint sits under the prior names: the Sandbox Agent SDK Show HN drew 41 points in January 2026, the Gigacode OpenCode-UI experiment 27 points in February, and SQLite for Rivet Actors 45 points, but no dedicated launch thread exists for the Agents product itself as of 2026-10-13, and a product line that has already carried the Sandbox Agent SDK and agentOS names beside the Actors platform carries identity churn a reader should price in.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=rivet-dev/agents&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=rivet-dev/agents&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=rivet-dev/agents&type=date&legend=top-left" />
</picture>

## Strengths

- **Durability with a different unit**: one Actor per key keeps the conversation and files across sleep, crash, and upgrade mid-run, so a nightly cron run continues one thread instead of starting a fresh session, the only scheduler in this category whose output accumulates.
- Schedules are first-class: cron expressions with time zones set in the Actor's `onCreate`, one-shot wakes with `schedule.after` and `schedule.at`, and the sandbox suspends while the agent sleeps.
- Self-hosting is complete: Apache-2.0 with a single-binary control plane, bring-your-own-cloud, or Rivet Cloud, and no cloud-only feature gap of the kind Trigger.dev documents for its checkpoints.
- Keys, credentials, and user subscriptions stay in your backend code, and the harness slot is stated as any-harness with Pi first.

## Cautions

- **The Pi Durable harness underneath is beta, and the docs' own limitations list is long**: no built-in approval flow, no automatic AGENTS.md or skill discovery, plain tool calls not rerun after a crash (only phased tasks are), waits capped at ten minutes, and roll-forward-only upgrades.
- The 12 ms wake and 72 KB per-Actor figures are the vendor's measurements; no independent benchmark or third-party evaluation exists as of 2026-10-13.
- The rename from sandbox-agent and the one-version-line monorepo covering Agents, Sandbox Agent, agentOS, and Dynamic Apps mean the surface you adopt can move under you.
- Agent state lives in the Actor's SQLite database and the rivetkit model, so adopting it is a commitment deeper than a workflow file, and no export story is documented.

## Pricing

The repository is free under Apache-2.0, and full self-hosting is free.
Rivet Cloud bills a monthly base plus usage: Free at $0 with 100,000 awake Actor hours, a $5 compute cap, 1 vCPU, and 5 GB storage; Hobby from $20/month plus usage; Team from $200/month plus usage; Enterprise BYOC by quote (as of 2026-10-13).
Usage meters include $0.05 per 1,000 awake Actor hours, $0.40 per GB-month of state storage, and compute from $0.0000330 per vCPU-second plus $0.0000029 per GiB-second, with sleeping Actors billed nothing.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-13 | Cloud plans | Baseline: Free $0 (100k awake Actor hours, $5 compute cap, 1 vCPU, 5 GB), Hobby from $20/mo plus usage, Team from $200/mo plus usage, Enterprise BYOC by quote; usage $0.05 per 1k awake Actor hours, storage $0.40 per GB-month, compute from $0.0000330 per vCPU-second plus $0.0000029 per GiB-second. | [rivet.dev/pricing](https://rivet.dev/pricing/) |

## Compared to

- [Trigger.dev](../trigger-dev/index.md): the same application-side durable-execution slot with a different unit, task runs with cloud-only CRIU checkpoints versus one process per agent whose state is SQLite you can self-host entirely.
- [Aeon](../aeon/index.md): scheduled agent runs as repo-native Actions workflows on your minutes; Rivet Agents embeds the agent in your application code and bills for awake time.
- [n8n](../n8n/index.md): the webhook-first canvas outside the codebase; Rivet Agents is code-first with no canvas and the agent loop in your backend.

## Bottom line

**Recommended for product engineers embedding long-lived coding agents in an application, who want cron-driven work that accumulates in one durable conversation and can accept a v0.x platform with a beta harness underneath.**
Not for repository chores (GitHub Agentic Workflows is the fit), one-shot scheduled tasks on the harness you already run (Aeon, Claude Code routines), or anyone who needs an independent track record before adopting.
My disagreeable claim: for the durable-agent use case this is a better fit than Trigger.dev's task runs, but I would not yet give either vendor's youngest layer unattended write access.

## Changes

- 2026-10-13 - Created from the cross-category scan, resolved to the durable-execution slot beside Trigger.dev after the kind call (durable execution for agent runs, not a general workflow engine under the kestra precedent).

## See also

- [Trigger.dev](../trigger-dev/index.md) - the task-run durable platform sharing the application-side slot
- [Aeon](../aeon/index.md) - repo-native scheduled agent runs on Actions
- [n8n](../n8n/index.md) - the webhook-first automation canvas
- [Pi](../../harnesses/pi/index.md) - the harness Rivet Agents runs as a durable Actor

## References

- https://github.com/rivet-dev/agents - repository, 1,604 stars, Apache-2.0, monorepo layout, one version line, as of 2026-10-13
- https://api.github.com/repos/rivet-dev/agents - exact counters (1,604 stars, 134 forks, 87 open issues and pull requests, pushed 2026-10-14 UTC, created 2026-01-25)
- https://rivet.dev/agents/docs - the actor-per-agent model, SQLite files, sandbox adapters, harness and model choice, and the company backing
- https://rivet.dev/agents/docs/schedules/ - cron and one-shot scheduling that continues one conversation
- https://rivet.dev/agents/docs/pi/ - Pi Durable beta status and the documented limitations list (critical source)
- https://rivet.dev/pricing/ - plan tiers, usage meters, and the sleeping-Actor billing rule, as of 2026-10-13
- https://rivet.dev - the company pitch, the agentOS 0.4 changelog line (2026-10-12), and the self-measured performance figures (critical source)
- https://hn.algolia.com/api/v1/search?query=rivet%20agents&tags=story - the footprint record: coverage under the Sandbox Agent SDK, Gigacode, and SQLite-for-Actors names, none for Agents itself, as of 2026-10-13
- https://news.ycombinator.com/item?id=46795584 - the January 2026 Sandbox Agent SDK Show HN (41 points), the predecessor's launch under the old name
