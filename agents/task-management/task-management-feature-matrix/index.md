---
title: "Task Management Feature Matrix"
created: 2026-08-27
updated: 2026-10-07
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, task-management, task-tracking]
readability: 3
audience_notes: >
  Engineers choosing how agents get their work queue, from a markdown file to a graph database to a PRD pipeline.
  Assumes you run at least one coding agent and know what a dependency graph is; each column links to a full note.
---

This matrix compares the five task managers profiled in this section, feature by feature, so choosing between them does not require reading five notes.

**Files versus database is the row that decides everything else: it determines whether your board survives multiple agents racing on it, and the planner layer Ordewell adds sits above that choice rather than replacing it.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Backlog.md](../backlog-md/index.md) | [beads](../beads/index.md) | [It's a Plan](../its-a-plan/index.md) | [Ordewell](../ordewell/index.md) | [Task Master](../task-master/index.md) |
| --- | --- | --- | --- | --- | --- |
| Kind | CLI, terminal and web kanban | Go CLI plus Dolt database | self-hosted team tracker platform (web, REST, MCP) | planner-plus-runners CLI, TUI, and VS Code extension | CLI plus MCP server |
| Storage | markdown task files in the repo | Dolt SQL in `.beads/`, JSONL export | PostgreSQL via Drizzle plus an S3-compatible object store | typed plan JSON per session, conversation persisted | files under `.taskmaster/` (tasks, config, state) |
| License | ✓ MIT | ✓ MIT | ~ AGPL-3.0 (runner package Apache-2.0) | ✓ Apache-2.0 | ~ MIT with Commons Clause |
| Task structure | tasks with acceptance criteria, DoD, milestones | hash IDs, epics, sub-tasks, message type | issues with projects, teams, cycles, custom fields, initiatives, dashboards | ordered tasks, each with runner, model, thinking effort, mode, dependencies | tasks with subtasks and dependency chains |
| Dependency graph | ~ milestones, no claim graph | ✓ graph plus auto-ready queue | ~ subtasks and links, no dependency scheduler | ✓ ordered plan, dependencies respected | ✓ dependency chains, move with them |
| Multi-agent concurrency | ✗ no atomic claims | ✓ atomic claim, hash IDs | ~ agents hold assignee slots, runs start on mention, assignment, or schedule, no claims | ~ independent tasks run in parallel, no shared claims | ? not verified |
| PRD ingestion | ✗ manual task creation | ✗ manual task creation | ✗ none documented, docs and notes are human-authored | ~ opt-in PRD artifact inside the planner conversation | ✓ `parse-prd` pipeline |
| Agent integrations | Claude Code, Codex, Gemini CLI, Kiro, Cursor, MCP | `bd init` for Codex, Claude, Factory, Cursor, plus AGENTS.md and MCP | internal agents on any keyed model (Mastra runtime), external agents via @itsaplan/runner (Claude Code, Codex, OpenCode, Antigravity, Copilot, custom), plus MCP and REST | runners Claude Code, Codex, OpenCode built in, plugins beyond; planner can be a coding agent or one of 25 API providers | MCP server and CLI, documented for Cursor, Claude Code, Windsurf, VS Code, Q CLI |
| Pricing | free | free | free self-hosted, no per-seat fees; commercial license unlisted | free | CLI free, Hamster $40 per creator per month |
| Current status | active, about 6.9k stars | active, about 27.7k stars, 1,388 open issues, v1.3.2-rc.1 prerelease 2026-10-05 after v1.3.1 stable 2026-09-30 | active, 896 stars, v1.3.0 (2026-10-04) | active, 187 stars, v0.7.1 (2026-10-06) | repo quiet since April 2026, product alive at Hamster |

## Reading the matrix

**The storage row is the architecture decision: markdown files are diffable and agent-readable but race under concurrency, while Dolt gives beads cell-level merge and atomic claims at the cost of a database in your repo.**
Task Master's file storage sits between the two but its concurrency story is unverified, which is the cell I would resolve first before adopting it for shared queues.

**Ordewell is the category's planner layer: where the other three track work, it decomposes a goal into an editable plan with per-task model assignment and refuses to take the agent's word for done, completing tasks on markers instead.**
Its 187 stars and v0.7.x release line make it the least proven column, and its note records the launch thread's AI-written-replies episode as a transparency caution.

**It's a Plan is the platform column: a full team tracker where agents hold assignee slots, and the only member whose storage and review live outside your git repository.**
Its 896 stars twelve weeks in make it the fastest-climbing young entrant here, and its note records the near-zero HN footprint as the open question.

**PRD ingestion is the pipeline feature, and its provenance is the warning: the only tool with a full PRD pipeline is the one whose license stopped being OSI open source and whose repo went quiet as the method moved into a paid product, while Ordewell treats the PRD as an optional conversational artifact instead.**

**All five converge on meeting agents where they already are, MCP or AGENTS.md or editor config, so the integration row is nearly a tie and should not drive the choice.**

## Choosing from the matrix

- Multiple agents sharing one queue: beads, for the atomic claims.
- Human review as the bottleneck: Backlog.md, for the three review gates.
- Want a self-hosted team board where agents hold assignee slots: It's a Plan, the platform-style entrant, AGPL-3.0.
- Want the PRD pipeline and accept the vendor: Task Master, pinned to a version you control.
- Want a planner that assigns the model per task and verifies by marker: Ordewell, newest and least proven, Apache-2.0.

## Changes

- 2026-08-27 - Created with three columns (Backlog.md, beads, Task Master) and ten rows, tracing every cell to the member notes.
- 2026-09-16 - Extended from three to four columns with Ordewell (inserted alphabetically), every row gaining a cell traced to the new note, and the reading and choosing prose extended to the planner layer.
- 2026-09-21 - Refreshed the beads status cell (new v1.3.1-rc.1 prerelease and issue count).
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-25 - Refreshed the Ordewell status cell (144 stars, v0.4.23 of 2026-09-23).
- 2026-09-27 - Refreshed the Backlog.md, beads, and Ordewell status cells (about 6.9k stars; about 27.5k stars and 1,270 open issues; 162 stars and v0.5.4 of 2026-09-26).
- 2026-09-29 - Refreshed the Ordewell status cell (179 stars, v0.5.5 of 2026-09-28); all other cells re-verified unchanged.
- 2026-10-02 - Refreshed the beads status cell (v1.3.1 stable of 2026-09-30, about 27.6k stars, 1,266 open issues) and the Ordewell status cell (183 stars, v0.5.6 of 2026-09-30), plus the matching prose figure.
- 2026-10-03 - Refreshed the beads status cell (1,299 open issues) and the Ordewell status cell (v0.6.1 of 2026-10-02), plus the matching prose release-line figure.
- 2026-10-06 - Refreshed the beads status cell (about 27.7k stars, 1,358 open issues) and the Ordewell status cell (185 stars, v0.7.0 of 2026-10-05), plus the matching prose release-line figure; all other cells re-verified unchanged.
- 2026-10-06 - Refreshed the beads status cell (1,373 open issues, v1.3.2-rc.1 prerelease of 2026-10-05) and the Ordewell status cell (184 stars), plus the matching prose figure; all other cells re-verified unchanged.
- 2026-10-07 - Extended from four to five columns with It's a Plan (inserted alphabetically), every row gaining a cell traced to the new note; refreshed the beads status cell (1,388 open issues) and the Ordewell status cell (187 stars, v0.7.1 of 2026-10-06), plus the matching prose figure.

## See also

- [Spec Driven Development Feature Matrix](../../spec-driven-development/spec-driven-development-feature-matrix/index.md) - the process layer that fills these boards
- [Control Planes Feature Matrix](../../control-planes/control-planes-feature-matrix/index.md) - what runs the agents once the queue exists
- [Orchestration Feature Matrix](../../orchestration/orchestration-feature-matrix/index.md) - the parallel-session layer these trackers feed
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map these categories sit in

## References

- https://github.com/MrLesk/Backlog.md - storage model, integrations, milestones for the Backlog.md column
- https://github.com/gastownhall/beads - Dolt modes, claims, hash IDs for the beads column
- https://github.com/eyaltoledano/claude-task-master - MCP tools, parse-prd, dependency moves for the Task Master column
- https://tryhamster.com/pricing - the commercial tier behind the Task Master method
- https://github.com/ordewell/ordewell - plan artifact, runners, marker verification for the Ordewell column
- https://api.github.com/repos/ordewell/ordewell - stars, dates, Apache-2.0 as of 2026-10-06
- https://ordewell.ai - surfaces and the plan-execute-verify loop for the Ordewell column
- https://news.ycombinator.com/item?id=49712276 - the launch thread grounding the Ordewell caution cell
- https://github.com/croffasia/itsaplan - agents as project members, stack, and license split for the It's a Plan column
- https://api.github.com/repos/croffasia/itsaplan - stars, dates, AGPL-3.0 as of 2026-10-07
- https://itsaplan.dev - surfaces and deployment paths for the It's a Plan column
