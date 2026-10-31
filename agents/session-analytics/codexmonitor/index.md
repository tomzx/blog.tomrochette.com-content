---
title: CodexMonitor
created: 2026-10-23
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, observability, codex, desktop]
readability: 3
audience_notes: >
  Engineers running OpenAI's Codex CLI who want one desktop surface for its threads, approvals, and account usage.
  Assumes you know what the Codex CLI and its app-server protocol are.
---

CodexMonitor is a free MIT Tauri desktop command center for OpenAI's Codex CLI: it manages workspaces and threads over the Codex app-server protocol, streams conversations and approvals as they run, meters your account's rate limits and credits, and pairs the agent with git, GitHub, and worktree tooling in one window.

**CodexMonitor watched Codex before OpenAI shipped its own desktop app, and it is now dormant: seven months without a commit while the vendor absorbed the same job.**

## What it is

A Tauri 2 + React app for macOS, Windows, and Linux (built from source with Node and a Rust toolchain; signed installers and an in-app updater ship through GitHub releases) that spawns one `codex app-server` per workspace and renders its threads.
The surface covers workspace and worktree management (agents can run in isolated worktrees under the app data directory), thread pin, rename, archive, and resume, a composer with skills, prompts, reviews, and file-path autocomplete, image attachments, Whisper dictation, model and reasoning-effort pickers, approval handling, and per-workspace settings synced into the Codex config.
Around the agent sit git diff and staging controls, branch management, GitHub Issues and Pull Requests through the `gh` CLI, a prompt library, a terminal dock, and a sidebar usage-and-credits meter beside a home usage snapshot.
An optional remote daemon mode runs Codex on another machine, with a Tailscale setup runbook and a headless daemon CLI, and an iOS remote-mode client is in progress.
Made by Thomas Ricouard (Dimillian), an independent developer, under MIT; the site states the app is not affiliated with OpenAI.

## Status

Dormant: 4,348 stars, 417 forks, 94 open issues, created 2026-01-11, last commit 2026-03-26, latest release v0.7.67 on 2026-03-24 (a 0.7.68 version bump landed in the repository the same day and was never released), as of 2026-10-31.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Dimillian/CodexMonitor&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Dimillian/CodexMonitor&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Dimillian/CodexMonitor&type=date&legend=top-left" />
</picture>

It launched in January 2026 as "an app to monitor the (Codex) situation" and became the main third-party Codex GUI within weeks, drawing a public retraction from Theo of t3.gg, who dropped plans to build his own after using it.
When OpenAI's own Codex desktop app appeared, Hacker News commenters called the two near-indistinguishable twins, with one crediting CodexMonitor's feature list first and another answering that every surface in this category looks alike; the repository's last commit landed days after that comparison.
**Its ending is the finding: a 4,000-star third-party command center went quiet within two months of the vendor shipping the same surface, and its 94 open issues are still waiting.**

## Strengths

- The most complete third-party Codex surface shipped to date: worktrees, approvals, plans, dictation, GitHub integration, and remote daemon mode in one MIT codebase.
- Genuine popularity for a single-maintainer desktop app: 4,348 stars, 415 forks, and public testimonials, including a retraction from a would-be competitor.
- It provably influenced the category: the vendor's own app arrived looking, by Hacker News commenters' account, like its twin.
- Local-first: it drives your own Codex CLI login and config, and remote mode rides your own Tailscale tailnet with a token you issue.

## Cautions

- Seven months dormant as of 2026-10-31, while the Codex CLI and the app-server protocol it drives keep moving, so expect drift between the app and the harness.
- OpenAI's desktop app now covers the same ground with vendor support, which weakens the case for adopting an unmaintained alternative.
- iOS support is unfinished (terminal and dictation unavailable on mobile builds), and building from source needs a Rust toolchain plus CMake and, on Windows, LLVM.
- It meters the account but does not analyze history: no transcript search, no cross-session archive, and no cost reports over past sessions.

## Pricing

Free and open source under MIT.
The site still carries its beta disclaimer (provided as is during the beta period), and no paid tier has ever been published.

## Compared to

- [Claude Code Agent Monitor](../claude-code-agent-monitor/index.md): the multi-harness live control room, still shipping; CodexMonitor is Codex-only and dormant, but adds worktree orchestration and GitHub panels the Monitor lacks.
- [Codex](../../harnesses/codex/index.md): the vendor's harness and, since 2026, its own desktop app, the default choice now that the independent alternative is quiet.
- [Tokscale](../tokscale/index.md) and [ccusage](../ccusage/index.md): usage reporting without agent control; CodexMonitor meters the account in its sidebar but cannot answer history questions the way they do.

## Bottom line

**Recommended only if you live in Codex, want every control in one native window, and accept an unmaintained codebase; otherwise the vendor's app or an active control room is the safer pick.**
Its dormancy is the data point: vendor surfaces absorb third-party command centers quickly.

## Changes

- 2026-10-23 - Created from the coordinator's entrant handoff, admitted as the category's first dormant member, the monitor kind beside ccusage and tokscale, with the official-app comparison from its Hacker News thread recorded.
- 2026-10-31 - Rotation re-verification: every cited URL re-fetched and live, and the Status corrected: the release line runs through v0.7.67 (2026-03-24), not v0.7.64 (2026-03-22) as recorded since creation, with the never-released 0.7.68 version bump landing the same day as v0.7.67 rather than three days later; dormancy unchanged (last commit 2026-03-26, the near-twin HN thread and beta disclaimer unchanged), and forks refreshed 415 to 417.

## See also

- [Claude Code Agent Monitor](../claude-code-agent-monitor/index.md) - the active multi-harness counterpart with launch-and-resume control
- [Codex](../../harnesses/codex/index.md) - the harness and vendor app CodexMonitor drives and competes with
- [Tokscale](../tokscale/index.md) - the ledger-style usage reporting CodexMonitor's sidebar meter only gestures at
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/dimillian/codexmonitor - the repository, 4,348 stars, MIT, created 2026-01-11, last pushed 2026-03-26 (as of 2026-10-31)
- https://raw.githubusercontent.com/Dimillian/CodexMonitor/main/README.md - the feature set: workspaces, threads, composer, git and GitHub panels, daemon and iOS paths
- https://www.codexmonitor.app - the positioning ("monitor your Codex situation"), the testimonials, and the beta disclaimer
- https://api.github.com/repos/Dimillian/CodexMonitor/releases - the release line through v0.7.67 (2026-03-24), the signed installers, and the updater feed (re-fetched 2026-10-31)
- https://api.github.com/repos/Dimillian/CodexMonitor/commits?per_page=5 - the last commits, ending 2026-03-26 (re-fetched 2026-10-31)
- https://news.ycombinator.com/item?id=46859808 - the thread calling CodexMonitor and the official Codex app near-indistinguishable twins (re-fetched live 2026-10-31)
