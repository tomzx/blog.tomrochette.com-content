---
title: Ordewell
created: 2026-09-16
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, planner, multi-agent, open-source]
readability: 3
audience_notes: >
  Engineers who want one goal decomposed into coding-agent tasks with per-task model choices they can edit before any token is spent.
  Assumes you run at least one coding agent CLI and know what a dependency graph is.
---

Ordewell is an Apache-2.0 TypeScript CLI, terminal UI, and VS Code extension that turns one goal into an ordered plan of coding-agent tasks, each with its own runner, model, thinking effort and mode, then executes the plan and completes a task only when that task's marker appears in the runner output.

**The plan as a typed artifact you can rewrite before a token is spent, plus completion decided by markers rather than the model's own verdict, is the design worth stealing, and the launch thread's AI-written-replies episode is the caution this section exists to record.**

## What it is

An npm package (`ordewell`, also published scoped as `@ordewell/cli`, Node 20+, tmux for the TUI) with three surfaces over one core: a CLI, a chat-left-plan-right terminal UI, and a VS Code extension that bundles its own core.
A planner researches the repo read-only, interrogates a vague goal in conversation instead of guessing, and commits the plan as JSON; planning is one continuous message loop (ADR-0002) with no approve buttons.
Every task then runs as a real coding-agent session in a fresh context, handed its predecessors' results, with independent tasks running in parallel and the dependency graph always respected.
Runners are pluggable: Claude Code, Codex, and OpenCode ship built in, anything else is a plugin manifest, the planner can itself be one of those agents on a subscription you already hold, and 25 API-key providers are recognized for standalone use.
The planner's permissions are unusually explicit (ADR-0008): commands classify into auto, ask, and refuse tiers, refuse is not promptable, paths are confined to the workspace, and its docs concede this is a denylist over a real shell rather than an OS sandbox.

## Status

Active, young, and small.
As of 2026-10-08: 187 stars, 15 forks, 29 open issues (most of them a single-day roadmap filing on 2026-09-26), created 2026-07-31, pushed 2026-10-07, latest release v0.7.2 on 2026-10-07, and roughly 6,200 npm downloads last month across the `ordewell` and `@ordewell/cli` package names (the npm window still ends 2026-10-04).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ordewell/ordewell&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ordewell/ordewell&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ordewell/ordewell&type=date&legend=top-left" />
</picture>

v0.7.0 moved completion and planning onto Ordewell's own tools: a task reports done with `task_complete` and asks with `checkpoint` instead of printing markers, the planner reads the live runner catalog and submits the plan through tools, and the printed marker stays as the fallback for the terminal transport, plugin runners, and sessions where the server did not attach; it landed a day after the three 0.6.x fix releases of 2026-10-04, which completed a five-release v0.6.x line begun by the 2026-10-02 pair that made the structured transport the default with Codex and OpenCode connectors and added ops tasks and merge gates (ADR-0020), so a task that acts on the world runs once the work it depends on is merged.
v0.7.1 (2026-10-06) made messages reach a running task between tool calls instead of at the turn's end (ADR-0023), added force send (ctrl-s in the TUI, Send now in VS Code), and let checkpoints be answered from the TUI and the CLI.
v0.7.2 (2026-10-07) is a security release: whole classes of planner shell commands that should have been refused were slipping past the refusal tier (shell negation prefixes, substitutions past the first 32, interpreters fed through stdin, every spelling of an inline-code flag, quoting and escaping that hid a command inside a substitution, re-cased command names, and Windows cmd forms), and each is now refused, continuing the security pairs of the 0.6.x line.
The Show HN launch thread reached 56 points and 30 comments on 2026-09-15.

## Strengths

- The plan is editable structured data: change a task's runner, model, effort, or mode without losing completed work or round-tripping the AI.
- Marker-based completion is a verification primitive this category mostly lacks; a task completes on evidence, exit codes are kept as diagnostics, and manual marks can be reversed.
- Per-task model assignment is a portfolio decision made in the open, so a security refactor and a README update do not get the same model.
- The exploration envelope (ADR-0008) is the most explicit read-only planner discipline profiled in this section, including the admission of its own limits.

## Cautions

- **The launch thread's defining exchange is the transparency record: a commenter observed that everything about the project, including author replies in the comments, is AI-written, and the maintainer confirmed heavy AI use for the docs and code while standing behind the design.**
- Replying to people with AI-generated text drew a specific objection in the same thread, so treat the repo's discourse hygiene as part of the adoption decision.
- The same thread carried the standing structural objection to meta-frameworks: any advance gets absorbed into Claude and Codex within months, and this tool's planner-plus-runners surface is exactly the kind that absorption targets.
- The v0.7.x line and a star count under 200 mean churn is likely; ADR-0002 records saved sessions being wiped without migration on that rewrite.
- The planner's shell control is a denylist classifier over a real shell, not a sandbox (ADR-0011 tracks that gap), and v0.7.2's release notes read like an inventory of the bypasses that classification invites, after the 0.6.x security pairs; treat the refusal tiers as hardening in progress, not a settled defense.

## Pricing

Free and open source under Apache-2.0.
No paid tier exists; token costs follow your runner subscriptions or API keys.

## Compared to

- [Task Master](../task-master/index.md): both decompose an input into dependency-chained tasks, but Task Master's pipeline starts from a written PRD and is now a Commons-Clause commercial engine, while Ordewell's planner interrogates a vague goal and is Apache-2.0.
- [beads](../beads/index.md): beads is the shared-queue state layer with atomic claims; Ordewell is the planning layer above it, so they compose more than compete.
- [Backlog.md](../backlog-md/index.md): both keep the human in charge before code exists; Backlog.md gates on reviewing agent-written files, Ordewell gates on the editable plan artifact itself.

## Bottom line

**Recommended for engineers running mixed-model agent fleets who want per-task model assignment and evidence-based completion, and who accept a two-month-old project.**
Not for shared multi-agent queues (that is beads) or for teams that need maturity signals a project this small cannot give.
The disagreeable claim I will defend: the AI-written launch thread is not disqualifying here, but it is the exact failure mode this section's transparency rules exist to catch, and a tool that cannot surface its own authorship plainly should not be trusted to surface task completion either.

## Changes

- 2026-09-16 - Created.
- 2026-09-25 - Recorded the v0.4.23 release (2026-09-23, four ships since v0.4.19) and refreshed counts.
- 2026-09-27 - Recorded the v0.5.x line (v0.5.0 on 2026-09-25 through v0.5.4 on 2026-09-26, five ships in two days) and refreshed counts (162 stars, 42 open issues, about 3,500 npm downloads).
- 2026-09-29 - Recorded v0.5.5 (2026-09-28, streaming planner replies and run-robustness fixes), refreshed counts (179 stars, 33 open issues, about 4,400 npm downloads), and updated the launch thread to 56 points and 35 comments.
- 2026-10-02 - Recorded v0.5.6 (2026-09-30, the seventh v0.5.x release in five days) and refreshed counts (183 stars, pushed 2026-10-01, about 4,700 npm downloads across both package names).
- 2026-10-03 - Recorded the v0.6.0 and v0.6.1 releases (both 2026-10-02: structured transport as the default with Codex and OpenCode connectors, then ops tasks and merge gates per ADR-0020), refreshed counts (32 open issues, pushed 2026-10-02), and updated the launch thread to 30 comments.
- 2026-10-06 - Recorded the v0.7.0 release (2026-10-05, the MCP server for task and planner tools) and refreshed counts; corrected the launch-thread comment count in References to 30.
- 2026-10-06 - Corrected the v0.7.0 characterization against the changelog (Ordewell's own task and planner tools over the structured transport, not an MCP server, with the printed marker as the documented fallback for the terminal transport, plugin runners, and unattached sessions) and fixed the release-chain arithmetic (five v0.6.x releases including the three fixes of 2026-10-04); refreshed counts (184 stars) and added the changelog reference.
- 2026-10-07 - Added the ordewell/ordewell star history chart to the Status section.
- 2026-10-07 - Recorded the v0.7.1 release (2026-10-06, mid-turn message delivery per ADR-0023, force send, checkpoint answering from the TUI and CLI) and refreshed counts (187 stars, 15 forks).
- 2026-10-08 - Recorded the v0.7.2 security release (2026-10-07, refusal-tier bypass classes closed after the 0.6.x security pairs) and refreshed counts (pushed 2026-10-07).

## See also

- [beads](../beads/index.md) - the shared-queue state layer Ordewell assigns work into
- [Task Master](../task-master/index.md) - the PRD-first pipeline and the commercialized counterpart
- [Backlog.md](../backlog-md/index.md) - the review-gate sibling for oversight before code exists
- [Claude Code](../../harnesses/claude-code/index.md) - one of the three built-in runner agents
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/ordewell/ordewell - README: plan artifact, runners, marker verification, plugin manifests
- https://api.github.com/repos/ordewell/ordewell - stars, forks, dates, Apache-2.0 as of 2026-10-07
- https://github.com/ordewell/ordewell/blob/main/CHANGELOG.md - the v0.7.0 entry: `task_complete` and `checkpoint` tools, tool-based planning, the marker fallback scope
- https://ordewell.ai - the product site: surfaces, the plan-execute-verify loop, marker wording
- https://ordewell.ai/docs.html - install, requirements, headless usage
- https://github.com/ordewell/ordewell/blob/main/docs/adr/0002-planner-as-conversation-loop.md - the conversation-loop decision and the session wipe
- https://github.com/ordewell/ordewell/blob/main/docs/adr/0008-planner-exploration-envelope.md - the auto/ask/refuse tiers and path confinement
- https://news.ycombinator.com/item?id=49712276 - the launch thread: the AI-written exchange, the absorption objection, 56 points and 30 comments
- https://api.npmjs.org/downloads/point/last-month/@ordewell/cli - 3,220 downloads last month for the scoped package
