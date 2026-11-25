---
title: Backlog.md
created: 2026-08-27
updated: 2026-11-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, llm=glm-5.4, task-management, kanban, markdown, open-source, byok]
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
As of 2026-11-25: 7,024 stars (as of 2026-10-14), 104 open issues and pull requests, pushed 2026-11-24, MIT-licensed, latest release v1.57.4 on 2026-11-22, 157,147 npm downloads over the trailing month to 2026-11-25.
v1.54.0 is a breaking release: `backlog task complete` and its MCP `task_complete` tool are removed in favor of marking work Done and archiving it, and archive now preserves the task's ID, record, dependencies, and references, with restore and delete alongside; it also changed the default task ordering and made previously accepted malformed edits fail.
v1.55.0 (2026-10-20) followed as a repair release: versioned JSON output for draft lists, signal forwarding so stopping the npm and Bun launcher stops its native process, unknown YAML frontmatter preserved when unrelated fields are edited, explicit UTC timestamps, and duplicate task IDs repaired through `backlog doctor --fix`.
v1.55.1 (2026-10-21) and v1.55.2 (2026-10-22) are security hardening releases patching dependencies and native certificate handling; v1.55.2's caveat was that native Git HTTPS proxies were temporarily unsupported while direct HTTPS and HTTP CONNECT proxies kept working.
v1.55.3 (2026-10-23) closed that caveat by restoring native Git certificate and proxy settings, including private HTTPS proxies, fixed task reads and writes in Nix packages, and rebuilt the native executables and Nix packages with Bun 1.4.4 for the upstream Brotli decoder and certificate trust fixes.
Four releases then landed in one day, 2026-11-21: v1.56.0 made task filenames follow title edits (a rename keeps the task's ID and links, with branches reconciled by creation time to the second) and made decisions first-class records the CLI writes and reads (--context, --decision, --alternatives, --consequences, supersession links, `backlog decision view`), required YAML-only markdown metadata with second-precision UTC timestamps, and applied a custom workflow's final column consistently across statistics, milestones, and board completion marks; v1.57.0 added a read-only static browser export (`backlog browser export`) publishing the board, task list, documents, decisions, and milestones to any static host with search and links working; v1.57.1 rejected document and decision IDs carrying folder separators before any write, a path-traversal guard, stopped standalone builds auto-loading bunfig.toml and .env, and added a security policy; and v1.57.2 locked document and decision IDs before lookup so an edit racing a rename reports record-busy instead of document-not-found, across edits, archive, restore, delete, and MCP document updates.
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
- 2026-10-21 - Recorded the v1.55.0 release (2026-10-20: versioned JSON output for draft lists, launcher signal forwarding, unknown YAML frontmatter preserved on unrelated edits, explicit UTC timestamps, and duplicate task IDs repaired through backlog doctor) and refreshed counts (73 open issues and pull requests, pushed 2026-10-20, 88,640 npm downloads).
- 2026-10-23 - Recorded the v1.55.1 and v1.55.2 security hardening releases (2026-10-21 and 2026-10-22: dependency and certificate-authority patching, with native Git HTTPS proxies temporarily unsupported in v1.55.2) and refreshed counts (77 open issues and pull requests, pushed 2026-10-23).
- 2026-10-25 - Recorded v1.55.3 (2026-10-23: native Git certificate and private HTTPS proxy support restored, closing the v1.55.2 caveat, Nix package task fixes, and a Bun 1.4.4 rebuild of the native executables) and refreshed counts (82 open issues and pull requests, 85,015 npm downloads).
- 2026-10-28 - Refreshed counts (85 open issues and pull requests, pushed 2026-10-28, 90,282 npm downloads over the trailing month to 2026-10-28); v1.55.3 still the newest release.
- 2026-10-31 - Refreshed counts (84 open issues and pull requests, pushed 2026-10-29, 95,771 npm downloads over the trailing month to 2026-10-31); v1.55.3 still the newest release.
- 2026-11-12 - Rotation re-verification with every cited URL re-fetched live (repository, API, README, the v1.54.0 through v1.55.3 release tags, groma.md resolving to its repository, the companion repo, the 254-point launch thread, npm, the talks page) and refreshed counts (94 open issues and pull requests, pushed 2026-11-11, 124,586 npm downloads over the trailing month to 2026-11-12); v1.55.3 still the newest release.
- 2026-11-15 - Rotation re-verification with every cited URL re-fetched live (repository, API, README, the v1.54.0 through v1.55.3 release tags, groma.md still resolving to its repository, the companion repo, the 254-point launch thread, npm, the talks page) and refreshed counts (102 open issues and pull requests, 143,042 npm downloads over the trailing month to 2026-11-15); v1.55.3 still the newest release.
- 2026-11-21 - Refreshed counts (109 open issues and pull requests, pushed 2026-11-21, 161,829 npm downloads over the trailing month to 2026-11-21); v1.55.3 still the newest release, with main carrying unreleased work since (task-file renames when a title changes, custom workflow statuses in milestones and board views, and a memory bound for the terminal board).
- 2026-11-22 - Recorded the four releases of 2026-11-21 (v1.56.0: task filenames follow title edits, decisions as first-class CLI records, YAML-only metadata with second-precision UTC times, final-column consistency for custom workflows; v1.57.0: the read-only static browser export; v1.57.1: the folder-separator ID guard, standalone bunfig and .env loading skipped, a security policy; v1.57.2: the rename race closed with ID locking and record-busy retries across edits, archive, restore, delete, and MCP document updates) and refreshed counts (107 open issues and pull requests, 160,990 npm downloads over the trailing month to 2026-11-22); v1.57.2 now the newest release.
- 2026-11-25 - Recorded v1.57.3 and v1.57.4 (both 2026-11-22: the phone-friendlier Backlog browser with swipe navigation across the Kanban board and a navigation drawer for documents and decisions, then the fix for 403 responses when the browser opens on a custom hostname) and main's unreleased work since (the BACK-828 web redesign page shell with shared colors and type, BACK-829's one-page Tasks view with List and Board layouts, BACK-836's restored mouse-wheel scrolling in the terminal board, and BACK-838's live updates surviving a reconnect), and refreshed counts (104 open issues and pull requests, pushed 2026-11-24, 157,147 npm downloads over the trailing month to 2026-11-25); v1.57.4 now the newest release.

## See also

- [beads](../beads/index.md) - the graph-database counterpoint from the same era
- [Task Master](../task-master/index.md) - the productized pipeline
- [GitHub Spec Kit](../../spec-driven-development/spec-kit/index.md) - the spec-first process layer it complements
- [Vibe Kanban](../../orchestration/vibe-kanban/index.md) - the kanban pattern applied to agents themselves

## References

- https://github.com/MrLesk/Backlog.md - README: checkpoints, commands, agent integrations, dogfooding claim
- https://api.github.com/repos/MrLesk/Backlog.md - stars, issues, push date, MIT license as of 2026-11-15
- https://raw.githubusercontent.com/MrLesk/Backlog.md/main/README.md - the Backlog.md + Groma.md integration section
- https://github.com/MrLesk/Backlog.md/releases/tag/v1.54.0 - the v1.54.0 notes: archive replaces complete, restore and delete, the breaking ordering and validation changes
- https://api.github.com/repos/MrLesk/Backlog.md/releases/tags/v1.55.0 - the v1.55.0 notes: JSON draft lists, launcher signal forwarding, frontmatter preservation, doctor repair
- https://api.github.com/repos/MrLesk/Backlog.md/releases/tags/v1.55.2 - the v1.55.2 notes: certificate-authority hardening and the native Git HTTPS proxy caveat
- https://api.github.com/repos/MrLesk/Backlog.md/releases/tags/v1.55.3 - the v1.55.3 notes: native Git certificate and private HTTPS proxy support restored, Nix fixes, the Bun 1.4.4 rebuild
- https://api.github.com/repos/MrLesk/Backlog.md/releases - the 2026-11-21 and 2026-11-22 releases v1.56.0 through v1.57.4: filenames following renames, decision records, the static export, the ID guards, the rename-race locking, the phone-friendly browser, and the custom-hostname fix
- https://groma.md - the companion product the integration names (resolves to its GitHub repository)
- https://api.github.com/repos/MrLesk/groma.md - the companion repo: 188 stars, MIT, as of 2026-10-10
- https://news.ycombinator.com/item?id=44483530 - the 254-point launch thread
- https://api.npmjs.org/downloads/point/2026-10-26:2026-11-25/backlog.md - 157,147 downloads over the trailing month to 2026-11-25
- https://mrlesk.com/talks - conference talks demonstrating the method
