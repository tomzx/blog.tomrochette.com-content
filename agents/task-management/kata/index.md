---
title: Kata
created: 2026-10-11
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, issue-tracking, local-first, cli, mcp, open-source]
readability: 3
audience_notes: >
  Engineers whose coding agents need a shared work ledger that answers in milliseconds and never touches the repository.
  Assumes you know what an MCP server and a session hook are.
---

Kata is an MIT-licensed, local-first issue ledger for coding agents: a single Go binary runs a daemon over SQLite that answers CLI, TUI, browser, MCP, and HTTP calls in single-digit milliseconds, so the tracker joins the agent's decision loop instead of sitting behind a hosted API.

**The 4-millisecond figure is the product thesis: kata's site argues that speed changes what a tracker is for, moving it from a place agents report to at the end of a task into working memory they query before every decision.**

## What it is

A Go daemon (auto-started on first use, idle-shutdown opt-in) holding issues in SQLite under `KATA_HOME`, with PostgreSQL as the production option, so the repository carries only a small `.kata.toml` binding file.
Surfaces: a CLI with `--agent` and `--json` modes, a terminal TUI, a daemon-served browser workspace, a native MCP server with seventeen on-demand section loaders, a versioned HTTP API, and a Go package for in-process embedding.
Issues carry short refs, parent and child links, blocks and blocked-by ordering, labels, durable cursor-addressable events, and closes that must cite evidence (`--commit`, `--test`, `--evidence`).
The coordination primitives are the draw: atomic claims (`kata claim --if-unowned`, with user-set TTL leases of one minute to 24 hours since v0.19.0), revision-guarded writes (`--if-match`), idempotent creates and closes, teammate identities with per-recipient inboxes, and `kata notify` attention requests.
Beyond one machine: a remote daemon, import and optional two-way status sync with GitHub, Notion, Plane, Linear, Twenty, Todoist, and TickTick plus a Forgejo connector, project sharing between federation hubs, and daemon-to-daemon federation, with a `kata import --source-format beads` path off beads.
Kenn Software LLC maintains it under MIT, with documentation at katatracker.com.

## Status

Active and on a steady release cadence.
As of 2026-10-27: 464 stars (as of 2026-10-14), 50 forks, 38 open issues and pull requests, created 2026-04-30, pushed 2026-10-27, latest release v0.20.0 on 2026-10-24, with backward compatibility promised since v0.14.0 (v0.19.0's command rename is the declared exception).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=kenn-io/kata&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=kenn-io/kata&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=kenn-io/kata&type=date&legend=top-left" />
</picture>

v0.19.0 shipped the changelog's long-standing unreleased block in one drop: the `agent-hook` rename covering the native harness targets (attention hooks now install on by default), new MCP coordination tools with paginated exhaustive issue discovery, `kata doctor`, and opt-out anonymous telemetry, alongside TickTick and Forgejo sync, federation project sharing, native cron, recurring child issues, comment replies, and TUI undo.
v0.20.0 (published 2026-10-24) added the terminal UI's Attention inbox for notification requests, `kata notify --re` reply requests with `kata wait --until reply` to block on an answer, `kata notify --broadcast` to an issue's participants (a 50-recipient cap with per-sender rate limits), and `issue.scheduled_reached` events that trigger date-driven work, while hardening SQLite upgrades against corruption after unclean daemon exits and rebuilding telemetry without the PostHog SDK (opt-outs preserved, daily count buckets and backoff in place of raw properties).

An HN search for the project returns zero story hits as of 2026-10-25 (the fuzzy hits are unrelated projects), so the adoption evidence is the repository curve and the changelog's external contributor roster (Wes McKinney, Marius van Niekerk), not independent discussion.

## Strengths

- Claims, leases, revision guards, and idempotency keys are concurrency primitives in the tracker, not conventions layered on a to-do list.
- Closing is an explicit completion claim with typed evidence, `kata audit closes` replays them, and the daemon refuses to close a parent over open children.
- The ledger lives beside the repo, not in it, which keeps the checkout clean and the same CLI working outside git; that is the deliberate contrast with beads carrying a database in `.beads/`.
- Harness coverage is the widest recorded in this section: contract and attention hooks for Claude Code, Codex, Cursor, Gemini, Copilot, Pi, Amp, OpenCode, OpenClaw, and more.

## Cautions

- State outside git means history does not ride commits the way beads, Epiq, or Backlog.md state does; federation and remote daemons are the sync paths, and both are more moving parts than a push.
- v0.19.0 ships anonymous telemetry (daily install events, session-duration buckets, screen views, daily agent activity from hooks and MCP), opt-out via `KATA_TELEMETRY_ENABLED=0`, a default worth checking before adopting a tool pitched as local-first.
- 459 stars in under six months, a company behind a free MIT product, and an unstated business model make the long-term bet unclear.
- The v0.19.0 upgrade carries real breaking changes: the `agent-hook` command rename (old spellings rejected, hooks must be reinstalled), attention hooks on by default, a PostgreSQL migration requiring schema-owner credentials, and federated hubs that must upgrade before their connected devices.

## Pricing

Free and open source under MIT.
No paid tier is listed; hosted mode is the same daemon deployed on your own account (Cloud Run, Fly.io, Render, Railway).

## Compared to

- [beads](../beads/index.md): both are local-first agent queues with atomic claims; beads carries a versioned Dolt database inside the repo and syncs over git, kata keeps the ledger beside the repo and syncs over daemons, and kata ships the import path between them.
- [kanban-md](../kanban-md/index.md): the markdown-board counterpoint; choose it when state must be readable files in git, kata when query speed, event history, and harness hooks matter more.
- [It's a Plan](../its-a-plan/index.md): the team-platform counterpoint, a self-hosted server board where agents hold assignee slots versus a machine-local ledger.

## Bottom line

**Recommended for multi-agent work on one machine or one team of machines where the tracker should sit inside the agent loop, with GitHub sync as the mirror rather than the queue.**
Not for teams whose task history must live in the repository, or anyone who needs a hosted product with a support contract.
My disagreeable claim: a tracker 250 milliseconds away is a different species from one 4 milliseconds away, and most "agents cannot track work" complaints are about that gap rather than about data models.

## Changes

- 2026-10-11 - Created after the entrant sweep surfaced its beads-alternative positioning and import path.
- 2026-10-11 - Added the star history chart.
- 2026-10-18 - Recorded the v0.19.0 release (2026-10-17: the agent-hook rename with attention hooks on by default, MCP coordination tools with paginated exhaustive issue discovery, kata doctor, TickTick and Forgejo sync, federation project sharing, native cron, recurring child issues, comment replies, TUI undo, and the telemetry line shipped) and refreshed counts (pushed 2026-10-18).
- 2026-10-25 - Rotation re-verification with every cited URL re-fetched live (repository, API, releases, the katatracker.com site still current through 0.20.0, the changelog, the agent workflows doc with its 18-harness hook table intact, the HN search still at zero story hits); recorded v0.20.0 (published 2026-10-24: the TUI Attention inbox, notify --re reply requests with wait --until reply, participant broadcasts with a 50-recipient cap, issue.scheduled_reached date events, SQLite upgrade corruption hardening, and the PostHog-free telemetry rework) and refreshed counts (41 open issues and pull requests, pushed 2026-10-25).

## See also

- [beads](../beads/index.md) - the repo-carried database counterpoint and the migration source
- [kanban-md](../kanban-md/index.md) - the markdown-board sibling with lease claims
- [AGENTS.md](../../protocols/agents-md/index.md) - the convention kata's briefings and hooks write into
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/kenn-io/kata - README: storage, surfaces, sharing models, the beads comparison and import path (fetched 2026-10-11)
- https://katatracker.com/ - the site: the 4-millisecond measurements, event stream, federation, evidence-based closes, the layer argument against SaaS trackers
- https://raw.githubusercontent.com/kenn-io/kata/main/docs/changelog.md - release history: v0.20.0 (2026-10-23) and v0.19.0 (2026-10-17) with their upgrade notes
- https://api.github.com/repos/kenn-io/kata/releases/tags/v0.19.0 - the v0.19.0 notes: sync targets, federation sharing, claims with TTL, MCP tools, upgrade requirements
- https://raw.githubusercontent.com/kenn-io/kata/main/docs/workflows/agents.md - the agent contract, the 18-harness hook coverage table, teammate and inbox workflows, MCP setup
- https://api.github.com/repos/kenn-io/kata - stars, forks, dates, MIT license as of 2026-10-27
- https://api.github.com/repos/kenn-io/kata/releases - v0.20.0 (published 2026-10-24) and the release cadence
- https://hn.algolia.com/api/v1/search?query=katatracker&tags=story - zero story hits as of 2026-10-25, the missing HN footprint
