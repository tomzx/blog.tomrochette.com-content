---
title: Rivet Agents
created: 2026-10-13
updated: 2026-10-27
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
File tools work on the Actor's SQLite database with no sandbox; add one (E2B, Daytona, or Freestyle through the sandbox adapter) and shell tools run there, with provider keys staying in your backend and never entering the sandbox.
The agent harness is Pi (Earendil's Pi Durable package, beta), with your own model, your own keys, or your users' own subscriptions.
It is built by Rivet Gaming, Inc. (YC, a16z Speedrun), the company behind the rivet-dev/rivet control plane, and the repository is a monorepo renamed from sandbox-agent that carries Rivet Agents plus the Sandbox Agent HTTP control layer on one version line, v0.5.4 newest (2026-10-27).

## Status

**Active, young, and moving fast.**
1,604 stars as of 2026-10-13, 134 forks and 85 open issues and pull requests as of 2026-10-27 (GitHub API), created 2026-01-25 and pushed 2026-10-27 UTC.
The release train reached a stable v0.5.0 only on 2026-10-07 after release candidates that began in March, with v0.5.1 through v0.5.3 following within a week (v0.5.3 on 2026-10-14) and v0.5.4 landing 2026-10-27, while the company homepage now leads with Introducing Rivet 3.0 Preview and pitches the whole platform as the orchestrator for agentic workloads (as of 2026-10-27).
The community footprint sits under the prior names: the Sandbox Agent SDK Show HN drew 41 points in January 2026, the Gigacode OpenCode-UI experiment 27 points in February, and SQLite for Rivet Actors 45 points, but no dedicated launch thread exists for the Agents product itself as of 2026-10-27, and a product line that has already carried the Sandbox Agent SDK, agentOS, and Actors names, and now a 3.0 banner, carries identity churn a reader should price in.

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
- The 6.9 ms cold-start and 72.4 KB per-Actor figures on the homepage are the vendor's own measurements (as of 2026-10-27); no independent benchmark or third-party evaluation exists as of 2026-10-13.
- The rename from sandbox-agent, the one-version-line monorepo covering Agents, Sandbox Agent, agentOS, and Dynamic Apps, and the new Rivet 3.0 Preview platform banner mean the surface you adopt can move under you.
- Agent state lives in the Actor's SQLite database and the rivetkit model, so adopting it is a commitment deeper than a workflow file, and no export story is documented.

## Pricing

The repository is free under Apache-2.0, and full self-hosting is free with no usage limits.
Rivet Cloud rebuilt its billing around control-plane plans plus per-node Actor pricing (as of 2026-10-27): Free at $0/month with one control-plane node and one included Actor Node, Hobby at $10/month with up to 3 Actor Nodes, Team at $120/month across three availability zones with up to 10, and Enterprise at $900/month with up to 50 and dedicated support.
Actor Nodes bill per month by size, from $4.20 (R-5) to $94.50 (R-160), with the larger sizes gated by plan, clusters run on Google Cloud in the region you pick, and bring-your-own nodes cost nothing beyond the control plane.
The awake-hour, storage, and per-second usage meters the plans carried until this month are gone.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-13 | Cloud plans | Baseline: Free $0 (100k awake Actor hours, $5 compute cap, 1 vCPU, 5 GB), Hobby from $20/mo plus usage, Team from $200/mo plus usage, Enterprise BYOC by quote; usage $0.05 per 1k awake Actor hours, storage $0.40 per GB-month, compute from $0.0000330 per vCPU-second plus $0.0000029 per GiB-second. | [rivet.dev/pricing](https://rivet.dev/pricing/) |
| 2026-10-27 | Cloud plans | Billing rebuilt from usage meters to control-plane plans (Free $0, Hobby $10, Team $120, Enterprise $900 per month) plus per-month Actor Nodes ($4.20 R-5 to $94.50 R-160, sizes plan-gated); awake-hour, storage, and per-second meters removed; bring-your-own nodes free beyond the control plane. | [rivet.dev/pricing](https://rivet.dev/pricing/) |

## Compared to

- [Trigger.dev](../trigger-dev/index.md): the same application-side durable-execution slot with a different unit, task runs with cloud-only CRIU checkpoints versus one process per agent whose state is SQLite you can self-host entirely.
- [Aeon](../aeon/index.md): scheduled agent runs as repo-native Actions workflows on your minutes; Rivet Agents embeds the agent in your application code and bills per Actor Node on its cloud.
- [n8n](../n8n/index.md): the webhook-first canvas outside the codebase; Rivet Agents is code-first with no canvas and the agent loop in your backend.

## Bottom line

**Recommended for product engineers embedding long-lived coding agents in an application, who want cron-driven work that accumulates in one durable conversation and can accept a v0.x platform with a beta harness underneath.**
Not for repository chores (GitHub Agentic Workflows is the fit), one-shot scheduled tasks on the harness you already run (Aeon, Claude Code routines), or anyone who needs an independent track record before adopting.
My disagreeable claim: for the durable-agent use case this is a better fit than Trigger.dev's task runs, but I would not yet give either vendor's youngest layer unattended write access.

## Changes

- 2026-10-13 - Created from the cross-category scan, resolved to the durable-execution slot beside Trigger.dev after the kind call (durable execution for agent runs, not a general workflow engine under the kestra precedent).
- 2026-10-16 - Recorded the v0.5.3 release (2026-10-14); the pricing page re-verified unchanged and all other claims held.
- 2026-10-22 - Fully re-verified in rotation with every cited URL re-fetched: the docs overview (actor-per-agent model, SQLite files, the sandbox adapter docs now listing Freestyle beside E2B and Daytona, prose updated to match), the schedules page (cron in onCreate, one-shot wakes, sandbox suspension while sleeping), the Pi Durable beta page (the limitations list holds, including the missing approval flow and the ten-minute wait cap), the pricing tiers (all unchanged), the agentOS 0.4 and Hosted VMs changelog line, the monorepo layout on one version line, and the no-dedicated-thread footprint record; v0.5.3 (2026-10-14) remains the newest release, and the repository counters refreshed (134 forks, 85 open issues and pull requests, pushed 2026-10-21 UTC).
- 2026-10-27 - Fully re-verified in rotation with every cited URL re-fetched: recorded the v0.5.4 release (2026-10-27), the homepage's Rivet 3.0 Preview repositioning with new vendor figures (6.92 ms cold start, 72.4 KB per Actor), and the rebuilt Cloud pricing (control-plane plans plus per-month Actor Nodes replacing the awake-hour and per-second meters), with a price-history row; the docs, Pi beta limitations, schedules page, and the under-prior-names HN footprint all re-confirmed, and the counters refreshed (85 open issues and pull requests, pushed 2026-10-27 UTC).

## See also

- [Trigger.dev](../trigger-dev/index.md) - the task-run durable platform sharing the application-side slot
- [Aeon](../aeon/index.md) - repo-native scheduled agent runs on Actions
- [n8n](../n8n/index.md) - the webhook-first automation canvas
- [Pi](../../harnesses/pi/index.md) - the harness Rivet Agents runs as a durable Actor

## References

- https://github.com/rivet-dev/agents - repository, 1,604 stars, Apache-2.0, monorepo layout, one version line, as of 2026-10-13
- https://api.github.com/repos/rivet-dev/agents - exact counters (1,604 stars pinned at their 2026-10-13 fetch, 134 forks, 85 open issues and pull requests, pushed 2026-10-27 UTC, created 2026-01-25; re-verified 2026-10-27)
- https://rivet.dev/agents/docs - the actor-per-agent model, SQLite files, sandbox adapters, harness and model choice, and the company backing (re-fetched 2026-10-27)
- https://rivet.dev/agents/docs/schedules/ - cron and one-shot scheduling that continues one conversation (re-fetched 2026-10-27)
- https://rivet.dev/agents/docs/pi/ - Pi Durable beta status and the documented limitations list (critical source, re-fetched 2026-10-27)
- https://rivet.dev/pricing/ - the rebuilt control-plane plans and per-month Actor Node pricing, as of 2026-10-27
- https://rivet.dev - the company pitch, the Rivet 3.0 Preview banner, and the self-measured performance figures (6.92 ms cold start, 72.4 KB per Actor; critical source, re-fetched 2026-10-27)
- https://hn.algolia.com/api/v1/search?query=rivet%20agents&tags=story - the footprint record: coverage under the Sandbox Agent SDK, Gigacode, and SQLite-for-Actors names, none for Agents itself, as of 2026-10-27
- https://news.ycombinator.com/item?id=46795584 - the January 2026 Sandbox Agent SDK Show HN (41 points), the predecessor's launch under the old name
