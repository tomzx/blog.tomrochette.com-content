---
title: Epiq
created: 2026-10-10
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, issue-tracking, event-sourcing, git, open-source]
readability: 3
audience_notes: >
  Engineers running unattended coding-agent sessions who need to reconstruct what the agents did to the board and the code.
  Assumes you know what an event log, an MCP server, and a git worktree are.
---

Epiq is an MIT-licensed, Git-native issue tracker that keeps the board as an append-only event log synced through Git and replays it on demand, built so unattended agent work becomes auditable history through an MCP server, a skill file, and per-agent identities.

**Workflow replay is the audit interface unattended agent sprints need, and storing the board as an event log in Git is a storage choice no other member of this category makes.**

## What it is

A self-hosted, local-first tracker running as a terminal UI (built with Ink) and a browser GUI over one event-sourced engine: every change is an append-only event in a per-user log file, and the board is materialized deterministically by replay, with ULIDs plus last-known-edge references ordering concurrent events across machines.
State lives in a managed Git worktree outside your checkout (`~/.epiq-global/worktrees/<id>`), project metadata in `.epiq/project.json`, so `:sync` over a git remote is the whole collaboration model, with no accounts, SaaS, or external services.
Agents get three doors: an MCP server (`epiq-mcp`, thirty-odd tools) for deterministic access, an installable `SKILL.md` that teaches the recommended workflow, and per-agent identities, so each agent authors its own events, assigns itself, and shows up in the contributor list.
Commits prefixed with a ticket's ref land in the ticket's inline code diff, where reviewers comment on lines, and the jolaflow identity maintains it under MIT.

## Status

Active and shipping fast.
As of 2026-10-25: 542 stars (as of 2026-10-14), 22 forks, 1 open issue and pull request, created 2025-06-22, pushed 2026-10-24, latest release v1.15.2 on 2026-10-23, and 1,746 npm downloads last month.
The v1.12.x line shipped four releases in twelve days, and v1.13.0 followed five days later with cross-repository commit linking: a board can connect other repos, commits in them land on the tickets they name and in the timeline, and read-only clones fetched on sync (capped at 2 GB each, self-recovering) make the linked diffs work outside the board's own checkout.
v1.13.1 and v1.13.2 (2026-10-19) fixed a slow TUI memory leak (releases had been shipping React's development build, which records a timing entry on every screen update), v1.14.0 (2026-10-20) let boards and lanes carry descriptions that hold the conventions agents follow, handed out by the MCP server on assume, get, create, and move, plus board flow stats over eight weeks, commit linking through an Epiq-Ref line in the commit body, and drafts that survive tab switches, and the v1.15 line landed three releases on 2026-10-23: v1.15.0 added dense cards (a Wide/Dense switch collapsing a card to title plus one ref line, a clock on stalled tickets, live dots on tickets touched in the last five minutes, and click-to-filter assignees and tags), v1.15.1 fixed an SSH repo connect failure, and v1.15.2 extended time travel so cards and the Code tab show each ticket's code as it was at the needle, with the needle's position kept in the URL.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ljtn/epiq&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ljtn/epiq&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ljtn/epiq&type=date&legend=top-left" />
</picture>

The Show HN launch thread reached 91 points and 48 comments on 2026-05-16, the second-largest HN footprint in this category after Backlog.md, followed by a 1-point video repost on 2026-08-30 and little independent coverage since, so current adoption rests on the repo's own curve.

## Strengths

- Workflow replay is the audit interface unattended agents need: scrub the timeline to see what moved, who moved it, and the linked diffs, during the run or after it.
- The event-sourced design gives multi-agent concurrency by construction: each agent writes its own log file, git merges stay trivial, and replays converge.
- Per-agent identities turn the board into an attribution record instead of one shared user.
- Ticket-to-commit ref linking with inline code diffs puts code review inside the ticket.

## Cautions

- Conflicting updates to the same text block resolve last-event-wins with no character-level merge, a limitation the maintainer confirmed in the launch thread, recoverable only through time-travel peeks.
- The launch thread's historical objection stands: distributed git issue trackers have repeatedly died on design problems of exactly this class, and Epiq is one maintainer's answer.
- Global npm install drew the thread's loudest resistance, and the npx-based MCP startup resolves against the registry on every start, which hangs in network-restricted agent sandboxes unless you install globally and point at the binary.
- The web UI arrived after launch and the project is single-maintainer at 539 stars, so bus risk and community footprint are both thin for a system of record.

## Pricing

Free and open source under MIT.
No paid tier, hosting, or account exists.

## Compared to

- [beads](../beads/index.md): both are repo-local state layers with concurrency designs, Dolt atomic claims versus event-log replay; choose beads when agents need a dependency-ready work queue, Epiq when the audit trail is the product.
- [Backlog.md](../backlog-md/index.md): both keep state in git, but Backlog.md's three review gates run before code exists while Epiq's replay runs after.
- [It's a Plan](../its-a-plan/index.md): the platform counterpoint, a server board where agents hold assignee slots, versus Epiq's repo-local logs.

## Bottom line

**Recommended for engineers running unattended agent sessions who need to reconstruct what happened, in the repo, without a server.**
Not for text-heavy collaborative editing under concurrency (last-event-wins) or teams that need a non-developer PM interface.
My disagreeable claim: the append-only event log is a better memory format for agent work than the markdown files this category keeps choosing, because replay answers "what happened" without inventing a schema for it.

## Changes

- 2026-10-10 - Created after the broad-list and GitHub search scan surfaced the 91-point launch thread the category had not resolved.
- 2026-10-13 - Recorded the v1.13.0 release (2026-10-13: cross-repository commit linking, so commits in connected repos land on the tickets they name and in the timeline, with read-only clones fetched on sync and capped at 2 GB) and refreshed counts (542 stars, 1 open issue, pushed 2026-10-13, 2,751 npm downloads).
- 2026-10-21 - Recorded the v1.13.1 and v1.13.2 fixes (2026-10-19, the TUI memory leak from releases shipping React's development build) and v1.14.0 (2026-10-20: board and lane descriptions that hold conventions agents follow and are handed out over MCP, board flow stats, commit linking through an Epiq-Ref line, unsent-text preservation); refreshed counts (zero open issues and pull requests, pushed 2026-10-20, 2,281 npm downloads).
- 2026-10-25 - Recorded the v1.15.0 to v1.15.2 releases (all 2026-10-23: dense cards with a Wide/Dense switch, stalled-ticket clocks and live dots, click-to-filter cards, an SSH repo-connect fix, and time travel showing each ticket's code as it was at the needle with the position kept in the URL) and refreshed counts (1 open issue and pull request, pushed 2026-10-24, 1,746 npm downloads).

## See also

- [beads](../beads/index.md) - the other repo-local state layer, graph database versus event log
- [Backlog.md](../backlog-md/index.md) - the markdown-native review-gate counterpoint
- [It's a Plan](../its-a-plan/index.md) - the platform-style counterpoint where agents hold assignee slots
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/ljtn/epiq - repository: README, MCP setup, agent identities, install paths (fetched 2026-10-10)
- https://api.github.com/repos/ljtn/epiq - stars, forks, dates, MIT license as of 2026-10-25
- https://raw.githubusercontent.com/ljtn/epiq/main/readme.md - the event-sourced model, conflict handling, MCP and skill setup, worktree sync
- https://ljtn.github.io/epiq/ - the site: teams-and-agents positioning, live monitoring and replay wording, the MCP tool count
- https://news.ycombinator.com/item?id=48155570 - the 91-point launch thread: the distributed-tracker history objection, the last-event-wins exchange, the MCP-versus-skill debate
- https://api.github.com/repos/ljtn/epiq/releases - v1.15.2 (2026-10-23), the v1.15.0 and v1.15.1 releases of the same day, v1.14.0 (2026-10-20), and the release train through v1.12.4
- https://api.npmjs.org/downloads/point/last-month/epiq - 1,746 downloads last month
