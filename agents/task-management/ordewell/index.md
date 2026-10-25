---
title: Ordewell
created: 2026-09-16
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, planner, multi-agent, open-source]
readability: 3
audience_notes: >
  Engineers who want one goal decomposed into coding-agent tasks with per-task model choices they can edit before any token is spent.
  Assumes you run at least one coding agent CLI and know what a dependency graph is.
---

Ordewell is an Apache-2.0 TypeScript CLI, terminal UI, and VS Code extension that turns one goal into an ordered plan of coding-agent tasks, each with its own runner, model, thinking effort and mode, then executes the plan and completes a task only on that task's explicit `task_complete` tool call, evidence a runner cannot produce by accident.

**The plan as a typed artifact you can rewrite before a token is spent, plus completion decided by an explicit tool call rather than the model's own verdict, is the design worth stealing, and the launch thread's AI-written-replies episode is the caution this section exists to record.**

## What it is

An npm package (`ordewell`, also published scoped as `@ordewell/cli`, Node 20+) with three surfaces over one core: a CLI, a chat-left-plan-right terminal UI, and a VS Code extension that bundles its own core.
A planner researches the repo read-only, interrogates a vague goal in conversation instead of guessing, and commits the plan as JSON; planning is one continuous message loop (ADR-0002) with no approve buttons.
Every task then runs as a real coding-agent session in a fresh context, handed its predecessors' results, with independent tasks running in parallel and the dependency graph always respected.
Runners are the three built-in coding agents, Claude Code, Codex, and OpenCode, driven only through their structured protocols since v0.8.0 removed the terminal transport and plugin runners; the planner can itself be one of those agents on a subscription you already hold, and 25 API-key providers are recognized for standalone use.
The planner's permissions are unusually explicit (ADR-0008): commands classify into auto, ask, and refuse tiers, refuse is not promptable, paths are confined to the workspace, and its docs concede this is a denylist over a real shell rather than an OS sandbox.

## Status

Active, young, and small.
As of 2026-10-25: 202 stars (as of 2026-10-14), 19 forks, 47 open issues and pull requests, created 2026-07-31, pushed 2026-10-24, latest release v0.10.12 on 2026-10-22, and about 10,600 npm downloads last month across the `ordewell` and `@ordewell/cli` package names.
v0.10.11 and v0.10.12 (both 2026-10-22) consolidated run and planner settings into one /settings surface with the one-value slash commands gone from the TUI and VS Code (the headless CLI keeps them), held a task_complete report until its turn closes so the tool reply reaches the runner before the verdict stops it, and kept a completion through a forced message and a message_undelivered exit so the runner's success is not discarded.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ordewell/ordewell&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ordewell/ordewell&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ordewell/ordewell&type=date&legend=top-left" />
</picture>

The 0.6.x line (2026-10-02 to 2026-10-04) made the structured transport the default with Codex and OpenCode connectors, added ops tasks and merge gates (ADR-0020), and shipped two security releases, and v0.7.x continued the pattern: v0.7.0 moved completion and planning onto Ordewell's own tools with the printed marker as a fallback, v0.7.1 delivered messages between tool calls (ADR-0023), and v0.7.2 (2026-10-07) closed refusal-tier bypass classes (shell negation, hidden substitutions, interpreter spellings, Windows cmd forms).
Three releases landed on 2026-10-10: v0.8.0 removed the terminal transport, plugin runners, and the printed completion marker, making an attempt-bound `task_complete` call the only completion path and the `checkpoint` tool the only question path (ADR-0025), unified planner and task skills as Agent-Skills-format folders that can live committed in the workspace, and closed two escapes, a Claude Code planner writing through its native plan file and a runner inheriting another Ordewell's MCP credentials; v0.8.1 raised the default parallel task count from three to five; v0.9.0 put harness planners under the same research envelope as the API planner (ADR-0026), with a shared read-only allowlist for commands and MCP tools, repository-supplied approval settings refused, and path-named programs always asking.
The Show HN launch thread reached 56 points and 30 comments on 2026-09-15.
v0.9.1 (2026-10-11) closed the next class: planners no longer run a repository's own config, so project hooks, env blocks, plugins, and project MCP servers start only after explicit approval, and a Codex planner treats the repository it researches as untrusted (ADR-0028).
v0.10.0 (2026-10-14) extended the security line to consent itself: global run settings can only be changed by your chat commands, with no planner-reachable tool or route able to raise them (ADR-0030), and a supervisor's answer_approval can deny or hand off a runner's request but can never widen its permissions (ADR-0029); v0.10.1 moved checkpoint answering into the task view's message box and v0.10.2 shipped the same day.
v0.10.3 (2026-10-16) worked the same trust line into onboarding: the first screen states that nothing runs until you approve the plan, a first run with no API key plans with an installed coding agent instead of failing on a missing OpenRouter key, API-key setup offers every supported provider, and task cards show their runner, model, and effort.
The v0.10.4 to v0.10.10 run (2026-10-17 to 2026-10-19) then turned to session and cost discipline: loading a saved session stays idle until you explicitly continue it, with no wake-ups or resume timers firing just because a session opened (v0.10.7), a planner whose process died between turns restarts on your next message, and v0.10.10 unified one context-and-cost usage line across the TUI, the status command, and the VS Code panel, with a task's runner stopped as soon as it reports completion.

## Strengths

- The plan is editable structured data: change a task's runner, model, effort, or mode without losing completed work or round-tripping the AI.
- Tool-call completion is a verification primitive this category mostly lacks; a task completes on an explicit `task_complete` call from its own attempt, not on the model's prose, and exit codes are kept as diagnostics.
- Per-task model assignment is a portfolio decision made in the open, so a security refactor and a README update do not get the same model.
- The exploration envelope (ADR-0008) is the most explicit read-only planner discipline profiled in this section, including the admission of its own limits.

## Cautions

- **The launch thread's defining exchange is the transparency record: a commenter observed that everything about the project, including author replies in the comments, is AI-written, and the maintainer confirmed heavy AI use for the docs and code while standing behind the design.**
- Replying to people with AI-generated text drew a specific objection in the same thread, so treat the repo's discourse hygiene as part of the adoption decision.
- The same thread carried the standing structural objection to meta-frameworks: any advance gets absorbed into Claude and Codex within months, and this tool's planner-plus-runners surface is exactly the kind that absorption targets.
- The v0.8.0 boundary release removed transports, plugins, and the completion marker outright, and a star count under 200 means churn is likely; ADR-0002 records saved sessions being wiped without migration on an earlier rewrite.
- The planner's shell control is a denylist classifier over a real shell, not a sandbox (ADR-0011 tracks that gap), v0.7.2's release notes read like an inventory of the bypasses that classification invites, and v0.9.0's one-envelope rewrite shows the harness planners needed their own pass; treat the refusal tiers as hardening in progress, not a settled defense.

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
- 2026-10-11 - Recorded the 2026-10-10 release triple: v0.8.0's removals (terminal transport, plugin runners, the completion marker; tool-call-only completion per ADR-0025, unified skills, the Claude Code plan-file and MCP-credential escapes closed), v0.8.1's parallel default of five, and v0.9.0's one-envelope planner research (ADR-0026); refreshed counts (196 stars, 17 forks, 45 open issues).
- 2026-10-13 - Recorded the v0.9.1 security release (2026-10-11: planners no longer run a repository's own config per ADR-0028, project MCP servers gated on approval, Codex planners treat the repository as untrusted) and refreshed counts (202 stars, 19 forks, 44 open issues, roughly 8,200 npm downloads).
- 2026-10-16 - Recorded the v0.10.x line (all three 2026-10-14: v0.10.0's consent-integrity security release, the planner unable to raise its own run settings per ADR-0030 and supervisors able to narrow but never widen runner permissions per ADR-0029, v0.10.1's in-task checkpoint answering, and v0.10.2) and refreshed counts (50 open issues and pull requests, pushed 2026-10-15).
- 2026-10-17 - Recorded the v0.10.3 release (2026-10-16: the nothing-runs-until-approval first screen, no-key first runs planning with an installed coding agent, provider-wide API-key setup, task cards showing runner, model, and effort, and approval and ops-task scheduling fixes) and refreshed counts (pushed 2026-10-16).
- 2026-10-21 - Recorded the v0.10.4 to v0.10.10 line (2026-10-17 to 2026-10-19: saved sessions load idle until explicitly continued, a dead planner process restarts between turns, and the unified context-and-cost usage line across TUI, status, and VS Code with the runner stopped at its task_complete report) and refreshed counts (18 forks, 52 open issues and pull requests, pushed 2026-10-20, about 10,300 npm downloads).
- 2026-10-23 - Recorded v0.10.11 and v0.10.12 (both 2026-10-22: the one /settings surface with the one-value slash commands gone from TUI and VS Code, task_complete held until the turn closes, and completions surviving forced messages and exits) and refreshed counts (44 open issues and pull requests, pushed 2026-10-22).
- 2026-10-25 - Refreshed counts (19 forks, 47 open issues and pull requests, pushed 2026-10-24, about 10,600 npm downloads); v0.10.12 still the newest release.

## See also

- [beads](../beads/index.md) - the shared-queue state layer Ordewell assigns work into
- [Task Master](../task-master/index.md) - the PRD-first pipeline and the commercialized counterpart
- [Backlog.md](../backlog-md/index.md) - the review-gate sibling for oversight before code exists
- [Claude Code](../../harnesses/claude-code/index.md) - one of the three built-in runner agents
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/ordewell/ordewell - README: plan artifact, runners, marker verification, plugin manifests
- https://api.github.com/repos/ordewell/ordewell - stars, forks, dates, Apache-2.0 as of 2026-10-25
- https://api.github.com/repos/ordewell/ordewell/releases - the v0.10.0 through v0.10.10 release notes (2026-10-14 to 2026-10-19): the consent-integrity rules, checkpoint answering, the onboarding changes, saved-session idle loading, and the unified usage line
- https://github.com/ordewell/ordewell/blob/main/CHANGELOG.md - the v0.7.0 entry: `task_complete` and `checkpoint` tools, tool-based planning, the marker fallback scope
- https://raw.githubusercontent.com/ordewell/ordewell/main/CHANGELOG.md - the v0.8.0, v0.8.1, v0.9.0, and v0.9.1 entries: the removals, unified skills, the escape closures, the one-envelope planner research, and the repository-config security release
- https://ordewell.ai - the product site: surfaces, the plan-execute-verify loop, marker wording
- https://ordewell.ai/docs.html - install, requirements, headless usage
- https://github.com/ordewell/ordewell/blob/main/docs/adr/0002-planner-as-conversation-loop.md - the conversation-loop decision and the session wipe
- https://github.com/ordewell/ordewell/blob/main/docs/adr/0008-planner-exploration-envelope.md - the auto/ask/refuse tiers and path confinement
- https://news.ycombinator.com/item?id=49712276 - the launch thread: the AI-written exchange, the absorption objection, 56 points and 30 comments
- https://api.npmjs.org/downloads/point/last-month/@ordewell/cli - 5,446 downloads last month for the scoped package
- https://api.npmjs.org/downloads/point/last-month/ordewell - 5,122 downloads last month for the unscoped package
