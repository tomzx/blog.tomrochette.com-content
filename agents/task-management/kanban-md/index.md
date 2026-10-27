---
title: kanban-md
created: 2026-10-11
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, kanban, markdown, multi-agent, open-source]
readability: 3
audience_notes: >
  Engineers running several coding agents over one repository who want the board to stay plain markdown files without losing coordination between agents.
  Assumes you know what a git worktree is and what a YAML frontmatter file looks like.
---

kanban-md is an MIT-licensed, single-binary Go kanban board stored entirely as markdown files: tasks are YAML-frontmatter files under `kanban/`, and cooperative claim leases let several agents share the board without a database.

**It is the missing middle of this category: Backlog.md's markdown-file storage plus the claim primitive only the database-backed members offered, which makes the file board safe to share between parallel agents.**

## What it is

A Go CLI (Homebrew, `go install`, release binaries, `kbmd` as a shorthand alias) with a full terminal TUI; `kanban-md init` creates `kanban/config.yml` and `kanban/tasks/`, where every task is a markdown file whose frontmatter carries id, status, priority, tags, assignee, and due date.
The command surface is built for agent loops: `pick --claim` finds and claims the next unblocked task in one call, `--compact` gives one line per task for cheap polling, JSON output everywhere, and `context` writes a board summary into AGENTS.md or CLAUDE.md.
Claims are cooperative leases: they expire (default one hour), `require_claim` statuses (in-progress, review) refuse anonymous moves, and claimed task files are made read-only on Unix as an accident guard, which the README states outright is not a security boundary.
The board model adds classes of service (expedite, fixed-date, standard, intangible), WIP limits, parent and dependency links with cycle rejection, flow metrics, and a bounded best-effort activity log.
The antopolskiy identity maintains it under MIT, and two installable skills ship with the CLI: command usage and a full kanban-based development loop (claim, worktree, implement, merge, done, with explicit defer-to-user rules).

## Status

Active and young.
As of 2026-10-27: 224 stars (as of 2026-10-11), 34 forks, created 2026-02-07, pushed 2026-10-05, latest release v0.39.0 on 2026-10-05.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=antopolskiy/kanban-md&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=antopolskiy/kanban-md&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=antopolskiy/kanban-md&type=date&legend=top-left" />
</picture>

The Show HN thread reached 19 points and 4 comments on 2026-02-10, and independent coverage has stayed thin since, so the adoption curve is the repository's own; the bundled development-loop skill has at least one downstream user, the Batty supervisor project, which wraps kanban-md as its board.

## Strengths

- Markdown files stay the source of truth, so git, grep, and any agent read the board with no adapter, and the board can travel inside the repository.
- The claim lease (single-command pick, expiry, require_claim statuses) is exactly the piece Backlog.md lacks for parallel agents on one board.
- The bundled skills carry the whole loop, including the board-home-versus-worktree discipline and handoff notes, not just command syntax.
- A single binary with no daemon and no database, plus a TUI with narrow-terminal and mouse modes for human supervision.

## Cautions

- The README says it directly: claims reduce duplicate work but are not a security or distributed-transaction boundary, so a misbehaving agent can still collide.
- 224 stars and a solo maintainer are a small bet, and the v0.x line means format churn (the config schema sits at version 12, and the standalone TUI binary was retired along the way).
- No MCP server: agents drive it through shell commands and skills only, so MCP-first harnesses get no native tools.
- The activity log is best-effort and bounded, so the audit story is weaker than the event-sourced members, Epiq and kata.

## Pricing

Free and open source under MIT.
No paid tier, hosting, or account exists.

## Compared to

- [Backlog.md](../backlog-md/index.md): the closest neighbor, also markdown files plus a board; choose Backlog.md for its three human review gates and local web UI, kanban-md for parallel-agent claims, WIP flow, and the bundled development-loop skill.
- [beads](../beads/index.md): choose beads when claims must be atomic against a database with merge-capable history, kanban-md when files must remain the store.
- [Kata](../kata/index.md): the daemon-ledger counterpoint, millisecond queries, event streams, and harness hooks versus plain files and a lease.

## Bottom line

**Recommended for solo engineers running two to five parallel agents over one repository who want the board in files and the coordination in expiring claims.**
Not for teams needing enforced review gates (Backlog.md), a system of record with a durable audit trail (Epiq, kata), or a hosted team board (It's a Plan).
My disagreeable claim: markdown files plus expiring leases cover the small-team multi-agent case better than a database, because a stale lease is visible in git while a stale database row is visible only through a query.

## Changes

- 2026-10-11 - Created after the topic search surfaced the claim-lease design this category's markdown members lacked.
- 2026-10-11 - Added the star history chart.
- 2026-10-21 - Rotation re-verification with every cited URL re-fetched live (repository page, the bundled development-loop skill, API, releases, HN search): nothing changed, with v0.39.0 still the newest tag and the last push still 2026-10-05.
- 2026-10-27 - Rotation re-verification with every cited URL re-fetched live (repository page, the bundled development-loop skill, API, releases, HN search): nothing changed, with v0.39.0 still the newest tag and the last push still 2026-10-05.

## See also

- [Backlog.md](../backlog-md/index.md) - the markdown-board sibling without claims
- [beads](../beads/index.md) - the database-backed claim counterpoint
- [Kata](../kata/index.md) - the local daemon ledger counterpoint
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/antopolskiy/kanban-md - README: storage, claims, classes of service, TUI, skills, design principles (fetched 2026-10-11)
- https://raw.githubusercontent.com/antopolskiy/kanban-md/main/.agents/skills/kanban-based-development/SKILL.md - the bundled development-loop skill: worktrees, board-home discipline, handoffs, defer-to-user rules
- https://api.github.com/repos/antopolskiy/kanban-md - stars, forks, dates, MIT license as of 2026-10-27
- https://api.github.com/repos/antopolskiy/kanban-md/releases - v0.39.0 (2026-10-05) still newest as of 2026-10-27, and the release history
- https://hn.algolia.com/api/v1/search?query=%22kanban-md%22&tags=story - the 19-point Show HN thread (2026-02-10), the main independent footprint
