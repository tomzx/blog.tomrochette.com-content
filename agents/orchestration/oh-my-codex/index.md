---
title: oh-my-codex
created: 2026-09-27
updated: 2026-09-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, orchestration, codex, skills, workflows]
readability: 3
audience_notes: >
  Engineers using OpenAI Codex CLI who want stronger defaults, reusable workflows, and team-style parallel execution.
  Assumes you already run Codex CLI and are comfortable with npm global installs and project-level config.
---

oh-my-codex (OMX) is an MIT-licensed workflow layer for OpenAI Codex CLI that adds stronger default sessions, reusable skills, hooks, HUD and status surfaces, project guidance, and team execution commands.

**OMX's bet is that a single harness can be made team-capable from the outside: it keeps Codex as the execution engine and adds the planning, worktree isolation, memory, and review scaffolding that the CLI does not ship with.**

## What it is

An npm package (`npm install -g oh-my-codex`) from Yeachan Heo and two maintainers that layers on top of Codex CLI rather than replacing it.
It exposes 32 role prompts via `/prompts:name` and 25 workflow skills invoked with `$name`, including `$plan`, `$ultragoal`, `$team`, `$code-review`, and `$ultraqa`, each runnable independently rather than as a fixed chain.
Its core skill is `$team`, which runs N coordinated workers each in a dedicated git worktree (isolated detached branches, incremental merge tracking, and an `integration-report.md`), optionally mixed across providers via `OMX_TEAM_WORKER_CLI_MAP=codex,claude,gemini`.
It adds six MCP servers (state, memory, code intelligence, trace, wiki, and Hermes) for cross-session context, a staged plan → prd → exec → verify → fix pipeline, launch profiles (`--yolo`, `--high`, `--xhigh`, `--madmax`), hooks, a live HUD, and project guidance kept in `.omx/`.
Notifications route to Discord, Slack, Telegram, or custom webhooks through an OpenClaw gateway.

## Status

Actively shipped and very popular: about 33,395 stars and 2,542 forks as of 2026-09-27, created 2026-02-02, with the latest release v0.21.6 on 2026-09-21 and npm at the same version across 135 published versions.
The 0.21 line was a consolidation: it retired legacy keywords behind a sunset-stub resolver (`$ralph` to `$ultragoal`, `$ultrawork` to `$team`) and removed writable MCP state tools.
**The popularity is harness-specific: OMX is a Codex CLI layer, and the README itself warns that native Windows and the Codex App are not the default experience and may break, and that third-party "OMX v2" forks are not official.**

## Strengths

- Turns an individual Codex session into a coordinated team with automatic per-worker git worktrees and incremental merge tracking.
- A large, named surface of skills and prompts (`$plan`, `$team`, `$ultragoal`, `$code-review`, `$ultraqa`) that is independently invocable.
- Six MCP servers give persistent memory, state, code intelligence, and tracing across sessions.
- Mixed-provider teams let Codex, Claude, and Gemini workers run side by side in one team.
- MIT, with a README that is unusually explicit about install pitfalls and unsupported paths.

## Cautions

- Primarily tuned for macOS and Linux; native Windows and the Codex App "may break or behave inconsistently" per the README.
- It is a layer on Codex CLI only, so it inherits Codex's model, pricing, and platform constraints.
- Fast-moving with a retirement cadence: `$ralph`, `$ultrawork`, and `$pipeline` were retired in 0.21, so older docs and tutorials drift.
- npm global installs can collide with a Homebrew-owned `codex` binary (`EEXIST`), a documented footgun.
- The huge star count is not matched by independent field reporting during this run; the community channel is a shared Discord server.

## Pricing

Free and open source under MIT.
No hosted tier and no token markup; Codex API or subscription usage is billed by OpenAI.

## Compared to

- [Sandcastle](../sandcastle/index.md): a TypeScript library that sandboxes any CLI agent; choose OMX when you want workflows and team execution on top of Codex specifically.
- [Crewplane](../crewplane/index.md): a provider-agnostic Markdown workflow runner; choose OMX for Codex-native skills, hooks, and worktree teams.
- Plain Codex CLI plus scripts: the zero-dependency option; OMX earns its keep once you want planning skills, memory, and parallel worktree workers.

## Bottom line

**Recommended for Codex CLI users on macOS or Linux who want stronger defaults, reusable skills, persistent memory, and worktree-isolated team execution.**
Not for Windows-first users, non-Codex harnesses, or anyone who needs a stable, slow-moving interface.

## Changes

- 2026-09-27 - Created.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Codex](../../harnesses/codex/index.md) - the harness oh-my-codex layers on
- [Sandcastle](../sandcastle/index.md) - the scripted sandbox alternative
- [Crewplane](../crewplane/index.md) - the provider-agnostic workflow runner
- [Worktrunk](../worktrunk/index.md) - the worktree CLI the $team model parallels

## References

- https://github.com/Yeachan-Heo/oh-my-codex - repository, skills, team mode, MCP servers, license, stars, and release data
- https://raw.githubusercontent.com/Yeachan-Heo/oh-my-codex/HEAD/README.md - install paths, the platform caution, and the official-project warning
- https://www.npmjs.com/package/oh-my-codex - package page and version history
- https://registry.npmjs.org/oh-my-codex - npm metadata: 0.21.6 latest, 135 versions, MIT, and dates
- https://yeachan-heo.github.io/oh-my-codex-website/ - the 32 prompts, 25 skills, `$team` worktree model, and release notes
