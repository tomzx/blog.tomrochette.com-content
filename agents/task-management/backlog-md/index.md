---
title: Backlog.md
created: 2026-08-27
updated: 2026-10-17
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, task-management, kanban, markdown, open-source, byok]
readability: 3
audience_notes: >
  Engineers who want agent work structured as reviewable markdown before it becomes code, without a database or a vendor.
  Assumes you already run at least one CLI or MCP-compatible agent and keep your projects in git.
---

Backlog.md is an MIT-licensed, markdown-native task manager and kanban visualizer for any git repository: a zero-config CLI where every task is a plain `.md` file and agents are steered through three human review checkpoints.

**The tracker's real product is the review gates, spec, plan, then code, each a screenful a human can actually read, which makes it the first line of code review rather than a to-do list.**

## What it is

Install with `npm i -g backlog.md` and any folder becomes a project board: tasks live as markdown files with acceptance criteria and a reusable Definition of Done, `backlog board` paints a live kanban in the terminal, and `backlog browser` serves a local drag-and-drop web UI.
The pitch is aimed squarely at the agent era: agents produce more code than you can read, so you review the task spec and the implementation plan before the code exists, one task equals one context window equals one PR.
It works with Claude Code, Codex, Gemini CLI, Kiro, Cursor, and anything MCP-compatible, auto-configuring them on demand, and the project dogfoods hard: nearly all of its own code is written by agents working through its own backlog.
It is maintained under the MrLesk identity, with conference talks ([Devoxx Belgium 2025](https://mrlesk.com/talks)) carrying the method.

## Status

Active and healthy at mid-scale.
As of 2026-10-17: 7,024 stars (as of 2026-10-14), 80 open issues and pull requests, pushed 2026-10-16, MIT-licensed, latest release v1.54.0 on 2026-10-16, 87,203 npm downloads last month.
v1.54.0 is a breaking release: `backlog task complete` and its MCP `task_complete` tool are removed in favor of marking work Done and archiving it, and archive now preserves the task's ID, record, dependencies, and references, with restore and delete alongside; it also changed the default task ordering and made previously accepted malformed edits fail.
The repo's quiet stretch since 2026-09-28 ended on 2026-10-07 with README commits adding a Backlog.md + Groma.md integration section, Groma.md being the same author's separate MIT architecture-map tool (188 stars as of 2026-10-10).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=MrLesk/Backlog.md&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=MrLesk/Backlog.md&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=MrLesk/Backlog.md&type=date&legend=top-left" />
</picture>

The July 2025 [launch thread](https://news.ycombinator.com/item?id=44483530) reached 254 points, the largest HN footprint of the task trackers profiled in this section.

## Strengths

- Everything is markdown in git: diffable, greppable, portable, and readable by humans and agents with no adapter.
- The three-checkpoint model (spec, plan, code) is the most explicit human-oversight design in this category.
- Terminal kanban plus local web UI covers both tastes without accounts or hosting.
- Dogfooding through its own backlog is verifiable in the repo, not a marketing claim.

## Cautions

- Markdown files have no atomic claims or dependency graph, so several agents sharing one board will race where [beads](../beads/index.md) serializes them.
- A board of thousands of flat files strains both the kanban view and the human reviewer it exists to protect.
- The review gates depend on agent discipline to seek approval; a yolo-configured agent can steamroll them.
- Bus factor looks small for a tool you might standardize a team on.

## Pricing

Free and open source under MIT.
No paid tier, hosting, or account exists.

## Compared to

- [beads](../beads/index.md): graph database with atomic claims; choose beads for multi-agent concurrency, Backlog.md for human reviewability.
- [Task Master](../task-master/index.md): PRD-driven pipeline with a company behind it; choose it when you want structure imposed, Backlog.md when you want to impose your own.
- GitHub Issues: hosted and agent-assignable, but the plan lives outside the repo and outside your diffs.

## Bottom line

**Recommended as the default first task tracker for agent-heavy repos, solo or small team, where reading the plan beats racing the agents.**
Not for multi-agent shared queues (no claims) or organizations needing a vendor to blame.
My disagreeable claim: its three checkpoints are what spec-driven development actually needed, a enforced review cadence rather than more templates, and [spec-kit](../../spec-driven-development/spec-kit/index.md)'s constitution files are weaker oversight than one gate a human actually attends.

## Changes

- 2026-08-27 - Created in the Task management category seed with the three-checkpoint review model, dogfooding claim, and terminal kanban recorded.
- 2026-09-27 - Refreshed scale numbers (6,862 stars, 73 open issues, 64,043 npm downloads) and recorded v1.53.0 (2026-09-24).
- 2026-10-07 - Added the MrLesk/Backlog.md star history chart to the Status section.
- 2026-10-10 - Recorded the README's Backlog.md + Groma.md integration section (2026-10-07, the same author's separate architecture-map tool) and refreshed counts (6,986 stars, 89 open issues, 84,452 npm downloads, pushed 2026-10-07).
- 2026-10-17 - Rotation re-verification with every cited URL re-fetched live; recorded the v1.54.0 release (2026-10-16: task complete and its MCP tool removed in favor of Done plus archive, archive keeping the task's ID, record, dependencies, and references with restore and delete added, new default ordering, malformed edits rejected) and refreshed counts (80 open issues and pull requests, pushed 2026-10-16).

## See also

- [beads](../beads/index.md) - the graph-database counterpoint from the same era
- [Task Master](../task-master/index.md) - the productized pipeline
- [GitHub Spec Kit](../../spec-driven-development/spec-kit/index.md) - the spec-first process layer it complements
- [Vibe Kanban](../../orchestration/vibe-kanban/index.md) - the kanban pattern applied to agents themselves

## References

- https://github.com/MrLesk/Backlog.md - README: checkpoints, commands, agent integrations, dogfooding claim
- https://api.github.com/repos/MrLesk/Backlog.md - stars, issues, push date, MIT license as of 2026-10-17
- https://raw.githubusercontent.com/MrLesk/Backlog.md/main/README.md - the Backlog.md + Groma.md integration section
- https://github.com/MrLesk/Backlog.md/releases/tag/v1.54.0 - the v1.54.0 notes: archive replaces complete, restore and delete, the breaking ordering and validation changes
- https://groma.md - the companion product the integration names (resolves to its GitHub repository)
- https://api.github.com/repos/MrLesk/groma.md - the companion repo: 188 stars, MIT, as of 2026-10-10
- https://news.ycombinator.com/item?id=44483530 - the 254-point launch thread
- https://api.npmjs.org/downloads/point/last-month/backlog.md - 87,203 downloads last month
- https://mrlesk.com/talks - conference talks demonstrating the method
