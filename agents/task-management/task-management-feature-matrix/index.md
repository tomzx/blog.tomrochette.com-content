---
title: "Task Management Feature Matrix"
created: 2026-08-27
updated: 2026-10-16
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, task-management, task-tracking]
readability: 3
audience_notes: >
  Engineers choosing how agents get their work queue, from a markdown file to a graph database to a PRD pipeline.
  Assumes you run at least one coding agent and know what a dependency graph is; each column links to a full note.
---

This matrix compares the fifteen task systems profiled in this section, feature by feature, so choosing between them does not require reading fifteen notes.

**Files versus database is the row that decides everything else: it determines whether your board survives multiple agents racing on it, and the planner layer Ordewell adds sits above that choice rather than replacing it.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Agent Kanban](../agent-kanban/index.md) | [AgentRQ](../agentrq/index.md) | [AI Dev Tasks](../ai-dev-tasks/index.md) | [Backlog.md](../backlog-md/index.md) | [beads](../beads/index.md) | [Epiq](../epiq/index.md) | [It's a Plan](../its-a-plan/index.md) | [kanban-md](../kanban-md/index.md) | [Kata](../kata/index.md) | [Operon](../operon/index.md) | [Ordewell](../ordewell/index.md) | [Pad](../pad/index.md) | [PlanDB](../plandb/index.md) | [Task Master](../task-master/index.md) | [Veritas Kanban](../veritas-kanban/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | Cloudflare Worker task board (React SPA, Hono API, D1), the Realmroot ecosystem's review product | self-hosted realtime human-in-the-loop task board exposed to agents over MCP | two markdown prompt files applied in any AI IDE or CLI | CLI, terminal and web kanban | Go CLI plus Dolt database | Git-native event-sourced issue tracker (TUI, browser GUI, MCP server) | self-hosted team tracker platform (web, REST, MCP) | single-binary Go CLI and TUI over a file kanban board | local-first Go daemon ledger (CLI, TUI, browser UI, MCP server, HTTP API) | Obsidian plugin plus operon-cli agent runtime | planner-plus-runners CLI, TUI, and VS Code extension | single-binary Go tracker (CLI, REST API, embedded web UI, MCP server) | single-binary Rust issue tracker (CLI, MCP server, HTTP API) over one SQLite file, no daemon | CLI plus MCP server | local-first board-first tracker (React UI, Node server, packaged Mac app) whose agent layer mounts in verified layers (CLI, MCP, webhooks, workflows, governance) |
| Storage | Cloudflare D1 behind the Worker; claims copy runtime and session provenance from verified Realmroot bindings | self-hosted server workspace, synced to web, desktop, and a Chrome extension | generated `tasks/<feature>.md` checklists in the repo, no runtime state | markdown task files in the repo | Dolt SQL in `.beads/`, JSONL export | append-only per-user event logs in a managed Git worktree, replayed deterministically; metadata in `.epiq/project.json` | PostgreSQL via Drizzle plus an S3-compatible object store | markdown task files with YAML frontmatter under `kanban/`, bounded activity log | SQLite under `KATA_HOME` (PostgreSQL option), the repo carries only `.kata.toml` | markdown tasks in the Obsidian vault, indexed by `operonId` | typed plan JSON per session, conversation persisted | SQLite with FTS5 (Postgres plus Redis option), workspace per project via `.pad.toml` | one SQLite file (`.plandb.db`) holding the whole coordination layer: task graph, dependency engine, work queue, audit log | files under `.taskmaster/` (tasks, config, state) | markdown task files with YAML frontmatter under `tasks/`, with file and SQLite repositories carrying a lease-safe worker foundation |
| License | ~ FSL-1.1 (source-available, Apache-2.0 per release after two years) | ✓ AGPL-3.0 | ✓ Apache-2.0 | ✓ MIT | ✓ MIT | ✓ MIT | ~ AGPL-3.0 (runner package Apache-2.0) | ✓ MIT | ✓ MIT | ~ GPL-3.0 (plugin and CLI) | ✓ Apache-2.0 | ✓ Apache-2.0 | ✓ Apache-2.0 | ~ MIT with Commons Clause | ✓ MIT |
| Task structure | tasks with assigned agent actors, notes, dependencies, review submissions, public board views | ~ goals broken into delegated tasks with statuses and permission gates, no documented dependency graph | numbered parent tasks and sub-tasks with checkboxes, Relevant Files sections, mandatory task 0.0 create-feature-branch | tasks with acceptance criteria, DoD, milestones | hash IDs, epics, sub-tasks, message type | tickets with refs, boards, tags, comments; commit-subject ref linking into inline code diffs | issues with projects, teams, cycles, custom fields, initiatives, dashboards | numbered task files with priority, tags, assignee, due dates, classes of service, WIP limits | issues with short refs, parent and child links, blocks and blocked-by ordering, labels, typed close evidence | durable `operonId` identity, inline and file tasks, subtasks, dependencies, recurrence, reminders, time tracking | ordered tasks, each with runner, model, thinking effort, mode, dependencies | typed collections (tasks, ideas, plans, docs, conventions, playbooks), custom fields, item refs, dependencies | compound graph: tasks containing subtasks to any depth, dependency edges crossing subtrees, pre and post conditions, task kinds, composite auto-completion | tasks with subtasks and dependency chains | kanban tasks with subtasks, sprints, templates, comments, workspaces with RBAC and agent tokens, bidirectional depends_on and blocks dependencies |
| Dependency graph | ✓ dependency relationships, cycles and cross-tenant links rejected | ✗ not recorded | ~ linear order only, the list is worked top to bottom | ~ milestones, no claim graph | ✓ graph plus auto-ready queue | ✗ none documented | ~ subtasks and links, no dependency scheduler | ✓ depends_on links with cycle rejection and unblocked pick filtering | ✓ blocks and blocked-by ordering, ready reads the graph | ~ dependency links between tasks, no auto-ready scheduler | ✓ ordered plan, dependencies respected | ~ item blocking with a ready query, no auto-ready scheduler | ✓ dependency DAG across containment boundaries, unblocked-ready reads, critical-path and bottleneck analysis, soft dependencies | ✓ dependency chains, move with them | ✓ bidirectional depends_on and blocks with DFS cycle detection and a recursive dependency API |
| Multi-agent concurrency | ~ claims on verified Realmroot session bindings, CAS task patches answer 409, the assignee cannot accept its own review | ✓ agents pull assigned tasks and update statuses in realtime | ✗ a generated checklist, no claims or locking | ✗ no atomic claims | ✓ atomic claim, hash IDs | ✓ per-agent identities write separate append-only logs merged by replay; conflicting text blocks resolve last-event-wins | ~ agents hold assignee slots, runs start on mention, assignment, or schedule, no claims | ✓ cooperative claim leases with expiry, require_claim statuses, claimed files made read-only | ✓ atomic claims with TTL leases, revision-guarded writes, actor attribution | ~ writes go through receipted sealed plans against one running Obsidian, no shared claims | ~ independent tasks run in parallel, no shared claims | ✓ atomic claim with TTL lease (a conflict names the live holder), named-agent attribution | ✓ atomic claiming through `plandb go`, two agents cannot hold one task; BM25 surfaces prior context to the next claimer | ? not verified | ~ no shared task claims; authority moves through durable compare-and-set phase transitions, and run-scoped tool catalogs with immutable digests bind every approval to exact arguments |
| PRD ingestion | ✗ none documented | ? not recorded | ✓ the pipeline is the PRD (`create-prd.md`, then `generate-tasks.md`) | ✗ manual task creation | ✗ manual task creation | ✗ none documented | ✗ none documented, docs and notes are human-authored | ✗ none documented | ✗ none documented | ✗ none documented | ~ opt-in PRD artifact inside the planner conversation | ~ agents decompose plans into tasks through playbooks, no parse-prd pipeline | ✗ none documented | ✓ `parse-prd` pipeline | ✓ PRD to user stories to quality-gated autonomous execution (4x10 review-gate scoring, fresh context per story, progress files) |
| Agent integrations | Realmroot Toolbox commands over OpenAPI, four installable skills, GitHub App; requires Realmroot identity and Enbor runtime services | MCP for any client, ACP for harness runs, Claude subscription oriented | any assistant that reads a file (Cursor, Claude Code, Windsurf, Amp documented) | Claude Code, Codex, Gemini CLI, Kiro, Cursor, MCP | `bd init` for Codex, Claude, Factory, Cursor, plus AGENTS.md and MCP | MCP server (`epiq-mcp`, thirty-odd tools), installable SKILL.md, per-agent identities, Claude Code documented | internal agents on any keyed model (Mastra runtime), external agents via @itsaplan/runner (Claude Code, Codex, OpenCode, Antigravity, Copilot, custom), plus MCP and REST | bundled installable skills (CLI use and a worktree development loop), context export to AGENTS.md and CLAUDE.md, no MCP server | contract hooks for 18 harnesses, AGENTS.md and CLAUDE.md briefings, native MCP server, teammate inbox and attention requests | operon-cli (typed requests, JSONL sessions), in-process Developer API, direct Markdown edits supported | runners Claude Code, Codex, and OpenCode over structured protocols (plugins removed in v0.8.0); planner can be a coding agent or one of 25 API providers | `/pad` skill for Claude Code (plugin with side panel), Cursor, Windsurf, Codex, OpenCode, Copilot, Amazon Q, Junie; versioned MCP server; consent-gated session pushes | installer auto-configures Claude Code, Cursor, Codex, Gemini CLI, OpenCode, Windsurf, and Aider; `/plandb` skill; CLI, MCP server, and HTTP API | MCP server and CLI, documented for Cursor, Claude Code, Windsurf, VS Code, Q CLI | MCP server (42 tools), CLI, Squad Chat webhooks, OpenClaw wake, runners for Buzz, Grok Build, Codex (SDK, app-server, cloud), Claude Code, Copilot CLI, Hermes, and OpenClaw; an AGENTS.md template |
| Pricing | free to self-deploy on your Cloudflare account, no documented paid tier | free self-host, no paid tier | free | free | free | free | free self-hosted, no per-seat fees; commercial license unlisted | free | free | free, GPL-3.0 | free | free self-hosted; Pad Cloud free tier (10 workspaces, 1,000 items, 3 collaborators), paid tier unlisted | free, Apache-2.0, no paid tier | CLI free, Hamster $40 per creator per month | free, MIT, self-hosted; packaged Mac app via Homebrew cask; no documented paid tier |
| Current status | active, 492 stars, pushed 2026-10-02, no tagged release since v1.13.4 (2026-05-19) | active, 1,152 stars as of 2026-10-14, pushed 2026-10-16, v0.11.3 (2026-10-16) | dormant, last push 2025-11-05, about 7.8k stars | active, 7,024 stars, v1.53.0 (2026-09-24), pushed 2026-10-15 | active, about 27.9k stars, 1,475 open issues as of 2026-10-16, v1.3.2-rc.2 prerelease 2026-10-10 after v1.3.1 stable 2026-09-30 | active, 542 stars, v1.13.0 (2026-10-13) | active, 963 stars, v1.5.0 (2026-10-13) | active, 224 stars, v0.39.0 (2026-10-05) | active, 464 stars, v0.18.0 (2026-09-17) | active, 255 stars, 4.0.1 (2026-10-14) | active, 202 stars, v0.10.2 (2026-10-14) | active, 193 stars, v0.18.0-rc.11 (2026-10-15) | stalled, 106 stars, v0.2.1 (2026-05-05), one commit since May | repo quiet since April 2026, product alive at Hamster | active, 840 stars, pushed 2026-10-14, v6.2.1 (2026-09-10) |

## Reading the matrix

**The storage row is the architecture decision: markdown files are diffable and agent-readable but race under concurrency, while Dolt gives beads cell-level merge and atomic claims at the cost of a database in your repo.**
Task Master's file storage sits between the two but its concurrency story is unverified, which is the cell I would resolve first before adopting it for shared queues.

**Ordewell is the category's planner layer: where the others track work, it decomposes a goal into an editable plan with per-task model assignment and refuses to take the agent's word for done, completing tasks on an explicit tool call since v0.8.0 removed the printed marker.**
Its 202 stars and v0.10.x release line make it one of the least proven columns, and its note records the launch thread's AI-written-replies episode as a transparency caution; v0.9.1 (2026-10-11) added the rule that planners never run a repository's own config until approved (ADR-0028), and v0.10.0 (2026-10-14) stopped the planner raising its own consent settings and supervisors widening a runner's permissions (ADR-0029 and ADR-0030).

**It's a Plan is the platform column: a full team tracker where agents hold assignee slots, and the only member whose storage lives on a server outside your files.**
Its 963 stars in thirteen weeks keep it the fastest-climbing young entrant here, and its note records the near-zero HN footprint as the open question.

**Operon is the knowledge-vault column: tasks live in the notes the human already keeps, and its sealed preview-and-apply runtime with receipts is the strongest agent-write contract in this category, though the runtime needs a running Obsidian and nothing works headless.**
Its 255 stars and a 4.x release train opened on 2026-10-14 make it young but steady, and its note records the zero-HN footprint as the open question.

**Epiq is the audit column: an event-sourced log kept in Git, replayed to reconstruct what unattended agents did, with per-agent identities and ref-linked code diffs, and its storage row is the only one that is append-only by design.**
Its 542 stars and 91-point launch thread make it mid-scale here, and its note records the last-event-wins text-conflict limitation the maintainer confirmed.

**The five October entrants fill the category's gaps: Agent Kanban enforces the review gate in the product model, kanban-md adds claim leases to markdown storage, Kata moves the ledger off the repo for loop speed and hook coverage, Pad tracks the rules the agents follow as items in the same database as the work, and Veritas Kanban gates what an agent may do by execution phase with digest-pinned, approval-bound tool catalogs.**
They are also the four least proven columns at 193 to 492 stars, and three of them (kanban-md, Kata, Pad) record a missing HN footprint as the open question.
PlanDB, the 2026-10-13 entrant, is now the least proven column of all at 106 stars, a compound graph in one SQLite file whose release train has been stalled since May inside a busy parent org.

**AI Dev Tasks is the ancestor column: the two-file prompt pack that ran the PRD-to-checklist loop before any of these tools existed, dormant since November 2025 with 7.8k stars and 1.7k forks.**
It is the reminder that the stateful rows above are the whole product: a generated checklist has none of them.

**PRD ingestion is the pipeline feature, and its provenance now splits four ways: the original pipeline (AI Dev Tasks) is dormant Apache-2.0 prompt files, the productized one (Task Master) went quiet inside a Commons-Clause commercial product, Ordewell treats the PRD as an optional conversational artifact, and Veritas Kanban runs PRD stories as fresh-context autonomous work scored by its review gate.**

**Every active column converges on meeting agents where they already are, a readable file, MCP, or an editor config, so the integration row is nearly a tie and should not drive the choice.**

## Choosing from the matrix

- Multiple agents sharing one queue: beads, for the atomic claims.
- Human review as the bottleneck: Backlog.md, for the three review gates.
- Auditing what unattended agents did while you were away: Epiq, replay the event log.
- Want a self-hosted team board where agents hold assignee slots: It's a Plan, the platform-style entrant, AGPL-3.0.
- Want the tracker inside your Obsidian vault: Operon, the knowledge-base column with receipted agent writes, GPL-3.0.
- Want the PRD pipeline and accept the vendor: Task Master, pinned to a version you control.
- Want the pipeline's zero-install ancestor: AI Dev Tasks, two prompt files, dormant since November 2025.
- Want a planner that assigns the model per task and verifies by tool call: Ordewell, Apache-2.0.
- Want review enforced by the product, not the prompt: Agent Kanban, the assignee cannot accept its own work, FSL-1.1 in the Realmroot ecosystem.
- Want a markdown board shared by parallel agents: kanban-md, expiring claim leases, MIT.
- Want the tracker in the agent's decision loop without touching the repo: Kata, the 4-millisecond local daemon, MIT.
- Want a task graph in one SQLite file with no daemon, no server, and no sync: PlanDB, compound graph with atomic claims, Apache-2.0, stalled since May.
- Want the rules agents follow tracked as items: Pad, conventions and playbooks beside the tasks, Apache-2.0.
- Want agent authority checkable after the fact, phase by phase, and will read the architecture docs first: Veritas Kanban, run-scoped tool catalogs with digest-pinned approvals, MIT, macOS-first packaging.

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
- 2026-10-08 - Extended from five to seven columns with AI Dev Tasks (the dormant prompt-file ancestor of the PRD pipeline) and Operon (the knowledge-vault entrant with the sealed-plan write path), inserted alphabetically, every row gaining cells traced to the new notes; refreshed the status cells (Backlog.md pushed 2026-10-07, beads 1,389 open issues, It's a Plan 905 stars, Ordewell v0.7.2 of 2026-10-07) and the reading and choosing prose.
- 2026-10-09 - Refreshed the It's a Plan status cell (913 stars, v1.4.0 of 2026-10-08, which added state-change agent schedules and Linear import) and the matching prose figure; all other cells re-verified unchanged against their notes and live sources.
- 2026-10-10 - Extended from seven to eight columns with Epiq (the Git-native event-sourced tracker whose replayable log audits unattended agent sprints), inserted alphabetically, every row gaining a cell traced to the new note; refreshed the beads status cell (about 27.8k stars, 1,415 open issues, v1.3.2-rc.2 prerelease of 2026-10-10), the It's a Plan, Operon, and Ordewell counts, and the reading and choosing prose.
- 2026-10-11 - Extended from eight to twelve columns with Agent Kanban (the FSL-licensed Cloudflare board whose assignee cannot accept its own review), kanban-md (the markdown kanban with expiring claim leases), Kata (the local-first daemon ledger), and Pad (the conventions-as-items tracker), inserted alphabetically, every row gaining cells traced to the new notes; refreshed the status cells (Backlog.md 6,997 stars, beads 1,424 open issues, Epiq 539 stars, It's a Plan 926 stars, Ordewell v0.9.0 of 2026-10-10 with tool-call-only completion) and the reading and choosing prose.
- 2026-10-11 - Extended from twelve to thirteen columns with Veritas Kanban (the MIT local-first board whose v6 runtime gates agent authority by execution phase with digest-pinned run-scoped tool catalogs), inserted alphabetically after Pad, every row gaining a cell traced to the new note; the intro, the October-entrants and PRD-provenance readings, and the choosing section updated, and its references added.
- 2026-10-13 - Extended from thirteen to fourteen columns with PlanDB (the stalled Apache-2.0 SQLite task graph whose compound graph separates containment from dependency, with atomic claims and no daemon), inserted alphabetically after Pad, every row gaining a cell traced to the new note; refreshed the Ordewell status cell (202 stars, v0.9.1 of 2026-10-11, the security release that stops planners running a repository's own config) and the reading and choosing prose.
- 2026-10-13 - Extended from thirteen to fourteen columns with AgentRQ (the AGPL self-hosted realtime human-in-the-loop task board), inserted in sorted position after AI Dev Tasks, all ten cells traced to the new note.
- 2026-10-13 - Recorded a correction to the AgentRQ extension bullet's from-count under the append-only rule: it reads thirteen to fourteen, but the correct count is fourteen to fifteen, PlanDB having taken the column count to fourteen earlier the same day.
- 2026-10-13 - Refreshed the status cells (Agent Kanban 492 stars, AgentRQ pushed 2026-10-14 at 1,152 stars, Backlog.md 7,024 stars, beads about 27.9k stars and 1,453 open issues, Epiq v1.13.0 of 2026-10-13 at 542 stars, It's a Plan v1.5.0 of 2026-10-13 at 963 stars, Kata 464 stars, Operon 255 stars, Pad 193 stars, Veritas Kanban 840 stars) and the matching prose figures.
- 2026-10-16 - Corrected the AgentRQ and AI Dev Tasks columns: every cell of the two columns had sat swapped since the 2026-10-13 AgentRQ insertion (the prompt pack's cells under AgentRQ and the realtime board's cells under AI Dev Tasks, including the Current status row), and returned the misplaced 2026-10-11 Veritas Kanban extension bullet above to date order; refreshed the release and activity cells (AgentRQ v0.11.3 of 2026-10-16 pushed, Backlog.md pushed 2026-10-15, beads 1,475 open issues as of 2026-10-16, Operon 4.0.1 of 2026-10-14, Ordewell v0.10.2 of 2026-10-14, Pad v0.18.0-rc.11 of 2026-10-15, Veritas Kanban pushed 2026-10-14) and moved the reading prose to the v0.10.x and 4.x release lines.

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
- https://github.com/snarktank/ai-dev-tasks - the prompt-pack workflow and scale for the AI Dev Tasks column
- https://raw.githubusercontent.com/snarktank/ai-dev-tasks/main/generate-tasks.md - task-list structure for the AI Dev Tasks column
- https://github.com/hasanyilmaz/operon - vault tasks and the agent runtime for the Operon column
- https://operon.cc/docs/docs-118-operon-agent-runtime-overview/ - the sealed-plan write path for the Operon column
- https://github.com/ljtn/epiq - the event-sourced model and MCP setup for the Epiq column
- https://raw.githubusercontent.com/ljtn/epiq/main/readme.md - storage, conflict handling, and agent identities for the Epiq column
- https://ljtn.github.io/epiq/ - the teams-and-agents positioning for the Epiq column
- https://news.ycombinator.com/item?id=48155570 - the launch thread grounding the Epiq caution cell
- https://github.com/kenn-io/kata - the daemon ledger, hooks, and beads import path for the Kata column
- https://github.com/antopolskiy/kanban-md - the file storage, claim leases, and bundled skills for the kanban-md column
- https://github.com/saltbo/agent-kanban - the Realmroot-bound architecture, task lifecycle, and FSL license for the Agent Kanban column
- https://github.com/PerpetualSoftware/pad - the collections, conventions, and MCP catalog for the Pad column
- https://github.com/BradGroux/veritas-kanban - the Veritas Kanban column: repository, MIT license, stars, and activity (GitHub API, as of 2026-10-14)
- https://raw.githubusercontent.com/BradGroux/veritas-kanban/main/docs/FEATURES.md - the Veritas Kanban column: markdown storage, dependencies, run-scoped tools v6, rosters, and PRD-driven development
- https://raw.githubusercontent.com/BradGroux/veritas-kanban/main/docs/SETUP-PATHS.md - the Veritas Kanban column: the layered readiness ladder behind its kind and concurrency cells
- https://github.com/Agent-Field/plandb - the PlanDB column: repository, README, installer behavior, and interfaces (fetched 2026-10-13)
- https://raw.githubusercontent.com/Agent-Field/plandb/main/docs/ARCHITECTURE.md - the PlanDB column: the compound graph model behind its storage, task structure, and dependency cells
- https://api.github.com/repos/Agent-Field/plandb - stars, dates, Apache-2.0, and the stalled release train as of 2026-10-13
