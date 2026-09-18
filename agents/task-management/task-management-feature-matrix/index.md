---
title: "Task Management Feature Matrix"
created: 2026-08-27
updated: 2026-09-16
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, task-management, task-tracking]
readability: 3
audience_notes: >
  Engineers choosing how agents get their work queue, from a markdown file to a graph database to a PRD pipeline.
  Assumes you run at least one coding agent and know what a dependency graph is; each column links to a full note.
---

This matrix compares the four task managers profiled in this section, feature by feature, so choosing between them does not require reading four notes.
Everything below was verified against live sources on 2026-09-18.

**Files versus database is the row that decides everything else: it determines whether your board survives multiple agents racing on it, and the planning layer the newest column adds sits above that choice rather than replacing it.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Backlog.md](../backlog-md/index.md) | [beads](../beads/index.md) | [Ordewell](../ordewell/index.md) | [Task Master](../task-master/index.md) |
| --- | --- | --- | --- | --- |
| Kind | CLI, terminal and web kanban | Go CLI plus Dolt database | planner-plus-runners CLI, TUI, and VS Code extension | CLI plus MCP server |
| Storage | markdown task files in the repo | Dolt SQL in `.beads/`, JSONL export | typed plan JSON per session, conversation persisted | files under `.taskmaster/` (tasks, config, state) |
| License | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ~ MIT with Commons Clause |
| Task structure | tasks with acceptance criteria, DoD, milestones | hash IDs, epics, sub-tasks, message type | ordered tasks, each with runner, model, thinking effort, mode, dependencies | tasks with subtasks and dependency chains |
| Dependency graph | ~ milestones, no claim graph | ✓ graph plus auto-ready queue | ✓ ordered plan, dependencies respected | ✓ dependency chains, move with them |
| Multi-agent concurrency | ✗ no atomic claims | ✓ atomic claim, hash IDs | ~ independent tasks run in parallel, no shared claims | ? not verified |
| PRD ingestion | ✗ manual task creation | ✗ manual task creation | ~ opt-in PRD artifact inside the planner conversation | ✓ `parse-prd` pipeline |
| Agent integrations | Claude Code, Codex, Gemini CLI, Kiro, Cursor, MCP | `bd setup` for Codex, Claude, Factory, Cursor, plus AGENTS.md and MCP | runners Claude Code, Codex, OpenCode built in, plugins beyond; planner can be a coding agent or one of 25 API providers | MCP server and CLI, documented for Cursor, Claude Code, Windsurf, VS Code, Q CLI |
| Pricing | free | free | free | CLI free, Hamster $40 per creator per month |
| Current status | active, about 6.8k stars | active, about 27k stars | active, 129 stars, v0.4.19 (2026-09-10) | repo quiet since April 2026, product alive at Hamster |

## Reading the matrix

**The storage row is the architecture decision: markdown files are diffable and agent-readable but race under concurrency, while Dolt gives beads cell-level merge and atomic claims at the cost of a database in your repo.**
Task Master's file storage sits between the two but its concurrency story is unverified, which is the cell I would resolve first before adopting it for shared queues.

**Ordewell is the category's planner layer: where the other three track work, it decomposes a goal into an editable plan with per-task model assignment and refuses to take the agent's word for done, completing tasks on markers instead.**
Its 129 stars and v0.4.x release line make it the least proven column, and its note records the launch thread's AI-written-replies episode as a transparency caution.

**PRD ingestion is the pipeline feature, and its provenance is the warning: the only tool with a full PRD pipeline is the one whose license stopped being OSI open source and whose repo went quiet as the method moved into a paid product, while Ordewell treats the PRD as an optional conversational artifact instead.**

**All three converge on meeting agents where they already are, MCP or AGENTS.md or editor config, so the integration row is nearly a tie and should not drive the choice.**

## Choosing from the matrix

- Multiple agents sharing one queue: beads, for the atomic claims.
- Human review as the bottleneck: Backlog.md, for the three review gates.
- Want the PRD pipeline and accept the vendor: Task Master, pinned to a version you control.
- Want a planner that assigns the model per task and verifies by marker: Ordewell, newest and least proven, Apache-2.0.

## Changes

- 2026-08-27 - Created with three columns (Backlog.md, beads, Task Master) and ten rows, tracing every cell to the member notes.
- 2026-09-16 - Extended from three to four columns with Ordewell (inserted alphabetically), every row gaining a cell traced to the new note, and the reading and choosing prose extended to the planner layer.

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
- https://api.github.com/repos/ordewell/ordewell - stars, dates, Apache-2.0 as of 2026-09-18
- https://ordewell.ai - surfaces and the plan-execute-verify loop for the Ordewell column
- https://news.ycombinator.com/item?id=49712276 - the launch thread grounding the Ordewell caution cell
