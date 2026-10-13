---
title: PlanDB
created: 2026-10-13
updated: 2026-10-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, issue-tracking, local-first, sqlite, open-source]
readability: 3
audience_notes: >
  Engineers choosing a local task graph for coding agents who want dependency-aware parallelism without a daemon, and anyone weighing a stalled tracker backed by a live ecosystem.
  Assumes you know what a dependency DAG and an MCP server are.
---

PlanDB is an Apache-2.0, single-binary Rust issue tracker for coding agents: one SQLite file holds a compound task graph, recursive containment plus a dependency DAG that crosses it, claimed atomically by agents over CLI, MCP, or HTTP with no daemon, no config, and no network.

**The compound graph is the differentiator: containment and dependency are two separate structures, so a subtask deep in one subtree can block a task in another, which is the structure mid-flight agent planning actually needs.**

## What it is

A Rust binary that creates a `.plandb.db` file and treats it as the entire coordination layer: the task graph, the dependency engine, the work queue, the handoff protocol, and the audit log.
Three surfaces share that one store: a CLI for shell agents, an MCP server (`plandb mcp`) for Claude Code, Cursor, and Windsurf, and an HTTP API (`plandb serve`) for custom agents and dashboards.
Planning is built to change mid-flight: `split` decomposes a stuck task into parallel subtasks, `insert` adds a step between two existing ones with dependencies rewired, `pivot` abandons a subtree, and `go` claims the next unblocked task through an atomic operation two agents cannot both win.
Conditions travel with tasks (`--pre`, `--post`), `context` records discoveries and blockers that BM25 search surfaces to whichever agent claims a related task later, and `critical-path` and `bottlenecks` read the graph instead of a flat list.
The installer (`curl agentfield.ai/plandb/install | bash`) auto-configures Claude Code, Cursor, Codex, Gemini CLI, OpenCode, Windsurf, and Aider with planning instructions and a `/plandb` skill, and the AgentField org maintains it under Apache-2.0 as the task-planning layer of its agent stack.

## Status

Stalled as a standalone release train, alive inside a busy ecosystem.
As of 2026-10-13: 106 stars, 10 forks, 6 open issues, created 2026-03-04, pushed 2026-09-24, and the newest tagged release is v0.2.1 from 2026-05-05, so five months have produced exactly one commit (an atomic task-split fix on 2026-09-24).
The parent org is active: AgentField (2,611 stars) was pushed 2026-10-05, and SWE-AF (1,033 stars), which uses PlanDB internally to coordinate parallel agent workstreams, was pushed 2026-10-08.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Agent-Field/plandb&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Agent-Field/plandb&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Agent-Field/plandb&type=date&legend=top-left" />
</picture>

An HN search for plandb returns no story about it as of 2026-10-13, so the adoption evidence is the repository curve and the parent stack's internal usage, not independent discussion.

## Strengths

- The compound graph expresses what flat lists and pure trees cannot: dependencies between tasks at any depth, crossing containment boundaries, with composites that auto-complete when their children finish.
- `plandb go` is the zero-infrastructure version of the atomic-claim primitive this category keeps reinventing: no daemon, no server, and two agents cannot hold one task.
- Pre and post conditions are visible at claim time, so the completion contract reaches the agent before it starts, not in a review comment afterward.
- Context entries compound across agents and sessions: what one agent learned surfaces automatically to the next one on a related task, with no handoff step to forget.

## Cautions

- **The release train stopped five months ago and one commit has landed since May, so the standalone tracker looks paused while the org's energy went to AgentField and SWE-AF; adopting it is a bet the org revives it.**
- The installer writes into agent configuration files (Claude Code rules and skills, Codex's AGENTS override, Gemini's GEMINI.md), a broad filesystem footprint for a tracker install.
- The README's strongest proof, a 3,769-line Rust transformer with seven RL experiments planned and tracked in PlanDB, is the maintainer's own unreviewed demo, not independent validation.
- State lives in a single SQLite file with no sync, no multi-machine story, and no UI beyond `plandb watch`, so it coordinates agents on one checkout, not a team across machines.

## Pricing

Free and open source under Apache-2.0.
No paid tier, hosting, or account exists; the parent AgentField site prices its whole stack at zero dollars with no paid tier.

## Compared to

- [beads](../beads/index.md): both give agents a dependency graph with atomic claims; beads carries a versioned Dolt database in the repository and syncs over git, PlanDB keeps a plain SQLite file with no sync story.
- [kata](../kata/index.md): both sit local-first beside the work; kata runs a daemon for millisecond queries, federation, and 18-harness hooks, PlanDB is a bare file with no daemon at all.
- [kanban-md](../kanban-md/index.md): the human-readable counterpoint; kanban-md keeps the board as markdown files in git, PlanDB keeps it in a database only its CLI reads.

## Bottom line

**Recommended for a solo engineer who wants dependency-aware parallel agent work with zero infrastructure and accepts a stalled release train.**
Not for teams that need sync across machines, a UI, or a project with visible momentum.
My disagreeable claim: the five-month gap matters less than it looks, because the artifact is a SQLite file whose graph outlives the CLI that wrote it, and a revived or forked client could read the same database tomorrow.

## Changes

- 2026-10-13 - Created after the GitHub entrant scan surfaced it, recording the compound graph, the atomic claims, and the five-month release gap.

## See also

- [beads](../beads/index.md) - the repo-carried graph-database counterpoint with the same claims primitive
- [kata](../kata/index.md) - the daemon-backed local-ledger counterpoint
- [kanban-md](../kanban-md/index.md) - the markdown-files counterpoint
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/Agent-Field/plandb - repository: README, install paths, interfaces, the AgentField relationship (fetched 2026-10-13)
- https://raw.githubusercontent.com/Agent-Field/plandb/main/README.md - the compound graph, atomic claiming, split/insert/pivot, pre and post conditions, the installer behavior, the benchmark demo
- https://raw.githubusercontent.com/Agent-Field/plandb/main/docs/ARCHITECTURE.md - the SQLite-file-as-coordination-layer thesis and the containment-plus-dependency model
- https://api.github.com/repos/Agent-Field/plandb - stars, forks, dates, license, push date as of 2026-10-13
- https://api.github.com/repos/Agent-Field/plandb/releases - v0.2.1 (2026-05-05) and the release gap
- https://agentfield.ai/ - the parent stack: the zero-dollar one-tier pricing statement, CodeAF and the control plane around PlanDB
- https://hn.algolia.com/api/v1/search?query=plandb&tags=story - no story about plandb as of 2026-10-13, the missing footprint signal
