---
title: Atlas
created: 2026-09-29
updated: 2026-09-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, coding-agents, source-control, rust]
readability: 3
audience_notes: >
  Developers running several coding agents against one codebase who want audit-grade history of which agent did what.
  Assumes you use Claude Code or Codex and know what ACP is.
---

Atlas is the Apache-2.0 Rust desktop app, for macOS and Windows, that bills itself as source control for coding agents: every agent run becomes a checkpoint linking commits back to the session, prompts, tool calls, and reasoning that produced them.

**Atlas is the first entrant in this category whose product is the history rather than the harness: it treats agent sessions as first-class, queryable commits.**

## What it is

A desktop workspace where you run Claude Code, Codex, Atlas's own native agent, or anything from the ACP registry side by side against the same codebase, with shared memory so switching agents mid-task does not reset context (README, docs.tryatlas.cc).
Around the agents it adds an Explorer, a Spaces spatial board for notes and their connections, up to three resizable split-view columns, and a filterable activity log that survives restarts.
The repo sits at 8,320 stars with 338 forks, Apache-2.0, created 2026-05-14, built in Rust with a web-technology UI, built from source with Bun and Rust (GitHub API, README, as of 2026-09-29).
It surfaced as an entrant from the owner's GitHub stars.

## Status

Active and growing fast: 8,320 stars in roughly 4.5 months, last push 2026-09-28, latest release alpha-0.3.4 on 2026-09-27 (GitHub API, as of 2026-09-29).
Official installers ship as macOS .app/.dmg and Windows .msi; Linux is build-from-source with GTK and WebKitGTK dependencies.
The README carries Trendshift badges for Rust, and feature work targets version branches rather than main, a sign of release discipline inside alpha.
I found no HN launch thread and no third-party coverage: the community footprint so far is GitHub stars alone, which is itself a signal.

## Strengths

- **Agent-attributed source control is a genuinely new angle**: checkpoints that keep commit, prompt, tool calls, and reasoning together answer "which agent did exactly what and why" months later, which worktree managers and terminals in this category do not.
- Running Claude Code, Codex, and ACP agents side by side with shared memory makes agent switching cheap instead of a restart.
- The surrounding surface (Explorer, Spaces, split view, pinned activity log) treats the agent workspace as a durable place, not a terminal session.
- Traction is real for its age: 8.3k stars and Trendshift placement within five months of first commit.

## Cautions

- Alpha software (versioned alpha-0.3.x): expect breaking changes, and the branch-based contribution flow confirms churn.
- **The community footprint outside GitHub is missing**: no HN thread, no independent reviews I could find, so the 8.3k stars have no public scrutiny behind them yet.
- Solo-or-small-team scale with 338 forks and an alpha cadence; bus-factor risk is unquantified.
- Linux support is source-build only, and the Rust first compile is minutes, not seconds.

## Pricing

None: Atlas is free and open source under Apache-2.0, with no pricing page, paid tier, or hosted offering as of 2026-09-29.

## Compared to

- [Conductor](../conductor/index.md): the macOS app for parallel Claude Code and Codex sessions; Conductor is steadier, Atlas adds the per-session audit history.
- [cmux](../cmux/index.md): the terminal-first take on parallel agents; choose cmux for keyboard-driven work, Atlas for a GUI with queryable history.
- [Orca](../orca/index.md): the broader agent development environment across desktop, mobile, and remote; Orca covers more surfaces, Atlas goes deeper on source-control integration.

## Bottom line

Recommended for developers running several coding agents against one codebase who want per-agent, per-session audit history that survives the session.
Not for teams needing a stable 1.0, Linux desktop installers, or a tool with independent community validation.

## Changes

- 2026-09-29 - Created when the owner's GitHub-stars entrant resolved in the carried candidate pile.

## See also

- [Conductor](../conductor/index.md) - the established macOS parallel-agent app Atlas competes with
- [cmux](../cmux/index.md) - the terminal-first alternative for running agents side by side
- [Orca](../orca/index.md) - the broader agent development environment peer
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins

## References

- https://api.github.com/repos/pacifio/atlas - GitHub API (200): 8,320 stars, 338 forks, Apache-2.0, Rust, pushed 2026-09-28, created 2026-05-14 (as of 2026-09-29)
- https://raw.githubusercontent.com/pacifio/atlas/main/README.md - README (200): checkpoints, side-by-side agents, ACP registry, shared memory, installers, build requirements
- https://www.tryatlas.cc - official website, live (200)
- https://docs.tryatlas.cc/docs/product/explorer - official documentation, live (200)
- https://docs.tryatlas.cc/docs/product/chat - official documentation, chat and sessions, live (200)
- https://api.github.com/repos/pacifio/atlas/releases/latest - releases API (200): alpha-0.3.4, published 2026-09-27
