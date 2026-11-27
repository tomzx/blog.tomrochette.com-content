---
title: oh-my-codex
created: 2026-09-27
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, llm=glm-5.4, orchestration, codex, skills, workflows]
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

Actively shipped and very popular: about 33,526 stars and 2,541 forks as of 2026-10-13, created 2026-02-02, with the default branch pushed 2026-11-25, with v0.22.25 (2026-11-25, Autopilot Deep Interview questions allowed in exact-session autopilot mode) the latest release after v0.22.24 (2026-11-24, native manifest hydration respecting explicit environment overrides on dev versions) after v0.22.23 (2026-11-24, native agents refreshed automatically after package updates and the notify fallback watcher on file-system events) after v0.22.22 (2026-11-24, setup refreshing stale model, provider, and reasoning pins without `--force`) after v0.22.21 (2026-11-24, repeated Stop hook invocations suppressed for blocked team workers) after v0.22.20 (2026-11-24, Homebrew Cellar node paths mapped to stable symlinks so managed Codex hooks and the MCP server configuration survive a node upgrade) after v0.22.19 (2026-11-24, the `OMX_DEFAULT_*_MODEL` environment tiers made the single source of truth for agent models with the per-agent `exactModel` pins removed, and the exit resume block printed for resume launches) after v0.22.18 (2026-11-23, spark and explore runtime resolution following the configured main model, the fix meant for v0.22.17) after v0.22.17 (2026-11-23, ralplan's Architect and Critic quality gates and lane reuse) after v0.22.16 (2026-11-23, a version bump only), the newest four of the v0.22 line that opened with v0.22.0 (2026-11-08, a minor bump that shipped the Herdr team runtime backend Phase 2, worker capacity management, task claim renewal, session execution comparisons, and regression gates, and made team operations fail closed on Git conflicts) and ran through v0.22.10 across 2026-11-08 to 2026-11-16 (v0.22.8 fixing team-lock recovery loops and Stop-hook stability, v0.22.9 giving the code-review skill source-bound continuation and repair receipts, v0.22.10 aligning ralplan skill guidance with the warn-and-skip policy for unavailable custom gates), then v0.22.11 (2026-11-18, preserving custom `developer_instructions` through legacy setup mode and canonicalizing `CODEX_HOME` for symlink handling) and a four-release burst across 2026-11-21 and 2026-11-22 (v0.22.12 recovering quarantined live-pin lock links from JSONL record streams in team state, v0.22.13 a safe resume of verified OMX session owners, v0.22.14 the first part of the exit-block improvements suggesting reattach commands while session owners are alive, and v0.22.15 vision-model guidance requiring reliable viewport evidence for CSS advice), after the v0.21 line closed at v0.21.48 (2026-11-07), seven releases in two days after v0.21.11 (2026-10-13) and a daily patch line running on through v0.21.46 (2026-11-02), after v0.21.44 (2026-10-31) and v0.21.39 (2026-10-28, recognizing GPT-6.1 Terra in the known Codex model catalog and fixing canonical state-root publication for detached session leaders), after v0.21.29 (2026-10-22) hardened team mailbox isolation further, after v0.21.19 (2026-10-19) added team-scoped mailbox delivery that isolates mailbox messages and recovery by team, and v0.21.10 (2026-10-13) hardened the astra-defaults evaluation infrastructure, fixed TOML configuration merges dropping multi-line `[tui]` arrays, and added npm registry-visibility diagnostics, and v0.21.9 (2026-10-12) added cumulative session token-usage reporting (`omx session usage`), native subagent completion evidence for doctor diagnostics, and an astra-defaults live evaluation collector.
As of 2026-11-27 the train stands at v0.22.29 (2026-11-26, Beads command support extended to every workflow phase) after v0.22.28 (2026-11-26, the per-second authority churn in attached HUDs stopped), v0.22.27 (2026-11-25, tmux HUDs kept independent and stacked), and v0.22.26 (2026-11-25, model fields refreshed for pristine agent TOMLs), per the GitHub releases feed.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Yeachan-Heo/oh-my-codex&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Yeachan-Heo/oh-my-codex&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Yeachan-Heo/oh-my-codex&type=date&legend=top-left" />
</picture>

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
- 2026-10-02 - Recorded v0.21.7 (October 1) as the new latest release and refreshed star, fork, and version counts.
- 2026-10-07 - Added the Yeachan-Heo/oh-my-codex star history chart to the Status section.
- 2026-10-12 - Recorded v0.21.9 (October 12, session token-usage reporting, native subagent completion evidence, and the astra-defaults evaluation collector) as the new latest release.
- 2026-10-13 - Recorded v0.21.10 and v0.21.11 (both October 13: the TOML merge fix and registry diagnostics, then the fresh provider-inheritance fix in native agent TOMLs) as the new latest release, and refreshed the star count to about 33,526.
- 2026-10-19 - Recorded v0.21.19 (2026-10-19), npm verified in sync at 148 published versions.
- 2026-10-20 - Recorded v0.21.25 (2026-10-20, team mailbox isolation hardening) and the v0.21.20 through v0.21.24 patch line, npm at 154 published versions.
- 2026-10-25 - Recorded v0.21.36 (2026-10-25) as the latest release, npm in sync.
- 2026-11-01 - Rotation re-verification (every cited URL re-fetched; the npmjs.com package page served a 403 bot wall this run while the registry endpoint stayed live); recorded v0.21.44 (2026-10-31) as the latest release, npm at 173 published versions.
- 2026-11-07 - Re-verified in rotation: every cited URL re-fetched live (repository, README, npm registry, docs site); the npmjs.com package page now serves a bot wall to plain fetches while the registry endpoint grounds the package facts, and no factual drift otherwise.
- 2026-11-15 - Volatile refresh: Recorded v0.22.7 (2026-11-15) as the latest release.
- 2026-11-17 - Recorded v0.22.10 (2026-11-16, team-lock recovery and Stop-hook fixes, source-bound review receipts, ralplan guidance matching unavailable-gate policy) as the latest release.
- 2026-11-19 - Volatile refresh: recorded v0.22.11 (2026-11-18, custom `developer_instructions` preserved through legacy setup, `CODEX_HOME` canonicalized) as the latest release.
- 2026-11-22 - Volatile refresh: recorded the four-release burst v0.22.12 through v0.22.15 across 2026-11-21 and 2026-11-22 (quarantined live-pin lock recovery, safe session-owner resume, exit-block part A, viewport-evidence vision guidance) as the latest releases.
- 2026-11-24 - Volatile refresh: recorded v0.22.16 (2026-11-23, a version bump only), v0.22.17 (2026-11-23, ralplan Architect and Critic quality gates and lane reuse), v0.22.18 (2026-11-23, spark and explore runtime resolution following the configured main model), v0.22.19 (2026-11-24, the `OMX_DEFAULT_*_MODEL` environment tiers as the single source of truth for agent models, the exit resume block for resume launches), and v0.22.20 (2026-11-24, Homebrew Cellar node paths mapped to stable symlinks so managed Codex hooks survive node upgrades) as the latest releases, the push date refreshed to 2026-11-24.
- 2026-11-25 - Rotation re-verified, every cited URL re-fetched and live (the npm package page behind its recorded bot wall, the registry read in full); recorded v0.22.21 (2026-11-24, repeated Stop hook invocations suppressed for blocked team workers), v0.22.22 (2026-11-24, setup refreshing stale model, provider, and reasoning pins without `--force`), v0.22.23 (2026-11-24, native agents refreshed after package updates, the notify fallback watcher on file-system events), v0.22.24 (2026-11-24, native manifest hydration respecting environment overrides on dev versions), and v0.22.25 (2026-11-25, Autopilot Deep Interview questions allowed in exact-session autopilot mode) as the latest releases, npm latest at 0.22.25, the push date recorded in Status as 2026-11-25, the 2026-11-24 bullet's push date having been absent from the prose.
- 2026-11-27 - Volatile refresh: recorded v0.22.26 and v0.22.27 (2026-11-25), v0.22.28 and v0.22.29 (2026-11-26, Beads commands in every workflow phase) on the release train.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Codex](../../harnesses/codex/index.md) - the harness oh-my-codex layers on
- [Sandcastle](../sandcastle/index.md) - the scripted sandbox alternative
- [Crewplane](../crewplane/index.md) - the provider-agnostic workflow runner
- [Worktrunk](../worktrunk/index.md) - the worktree CLI the $team model parallels

## References

- https://github.com/Yeachan-Heo/oh-my-codex - repository, skills, team mode, MCP servers, license, stars, and release data
- https://api.github.com/repos/Yeachan-Heo/oh-my-codex/releases?per_page=6 - the release feed, v0.22.25 (2026-11-25) back to v0.22.18 (2026-11-23) (as of 2026-11-25).
- https://raw.githubusercontent.com/Yeachan-Heo/oh-my-codex/HEAD/README.md - install paths, the platform caution, and the official-project warning
- https://www.npmjs.com/package/oh-my-codex - package page and version history
- https://registry.npmjs.org/oh-my-codex - npm metadata: 0.21.44 latest, 173 versions, MIT, and dates (as of 2026-11-01)
- https://yeachan-heo.github.io/oh-my-codex-website/ - the 32 prompts, 25 skills, `$team` worktree model, and release notes
- https://api.github.com/repos/Yeachan-Heo/oh-my-codex/releases/tags/v0.22.20 - the v0.22.20 release notes (2026-11-24): Homebrew Cellar node paths mapped to stable symlinks (fetched 2026-11-24)
- https://api.github.com/repos/Yeachan-Heo/oh-my-codex/releases/tags/v0.22.25 - the v0.22.25 release notes (2026-11-25): Autopilot Deep Interview questions allowed, with the v0.22.21 through v0.22.24 notes (fetched 2026-11-25)
