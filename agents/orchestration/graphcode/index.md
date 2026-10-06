---
title: GraphCode
created: 2026-09-27
updated: 2026-10-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, orchestration, macos, graph, loops]
readability: 3
audience_notes: >
  macOS engineers who want unattended, connected, still-attachable agent loops rather than a one-shot dispatch.
  Assumes you run at least one agent CLI and understand shell exit codes and PTY sessions.
---

GraphCode is an FSL-1.1-MIT source-available native macOS workspace that arranges live coding-agent sessions into a graph, where every node is a real terminal and hand-off, message, or spawn edges fire on conditions including a shell predicate.

**GraphCode's bet is that a loop is an agent session on repeat, so it schedules nothing itself: recurrence lives inside the session's own prompt, which keeps each loop attachable and steerable mid-run instead of a headless job that already finished.**

## What it is

A native SwiftUI app for macOS 15 or later on Apple Silicon, from scgopi, installed with a Homebrew cask or a signed DMG.
The unit is a loop, an agent session that runs repeatedly in one of four modes: turn-based (pauses each turn for review), goal-based (runs until a goal is met, optionally proven by a shell command exiting 0), time-based (a cadence written into the prompt, like `/loop 1h triage`), or composite (a sub-graph that plans its own steps).
Each loop runs in a worktree and its terminal is a `zmx` PTY session that survives quitting the app, restarting the daemon, or rebooting, so reopening attaches to the same session with one scrollback rather than starting a duplicate.
Edges between nodes fire on conditions (always, on success, on failure) with a cycle guard, and loops message each other by name across graphs and repositories, staged into memory when the peer is asleep.
It bundles no agents and drives five backends (Claude Code, GitHub Copilot CLI, Codex, OpenCode, and Pi), exposes an app, a `graphcoded` daemon, a `graphcode` CLI, and a shared GraphcodeKit framework, keeps all state under `~/.graphcode/`, and writes nothing inside the project folders you open.

## Status

New and fast-moving: about 135 stars and 19 forks as of 2026-10-05, created 2026-07-26, with v0.1.78 (2026-10-04) the latest release, promoted from the October 3 beta line, following v0.1.77 (2026-09-29, loops come back after a codespace or remote-host restart) and the first stable v0.1.76 of 2026-09-28, still a pre-1.0 line.
It is maintained by one developer, scgopi, on top of Ghostty's terminal engine and the zmx session daemon.
**Two months old, one maintainer, and a 0.1.x version mean GraphCode is an idea to try, not infrastructure to depend on, and its FSL-1.1-MIT license is source-available rather than OSI open source until the future license converts.**

## Strengths

- The graph model is a genuinely different abstraction: edges are hand-off, message, or spawn, and the agents on either end can differ.
- Sessions outlive the app and reboots via zmx, so unattended loops remain attachable and correctable.
- The self-improving loop separates maker, critic, and a bounded guard, and reads a measured metric rather than the loop's self-report, which is the right structure for autonomous iteration.
- Goal-based loops use a shell predicate as the done check, and the UI can test that predicate as the daemon will.
- Nothing is written inside your project folders, and the integration surfaces (GraphcodeKit and the CLI) stay MIT.

## Cautions

- macOS 15 or later on Apple Silicon only.
- FSL-1.1-MIT is source-available, not OSI open source, for the app and daemon until the future license date.
- Pre-1.0 beta with one maintainer and a small community; no Hacker News or forum footprint during this run.
- Bundles no agent CLIs and requires at least one on PATH (the website says Claude Code specifically).
- Time-based loops on Codex, OpenCode, and Pi need an experimental daemon heartbeat because only some agents have a `/loop` skill.

## Pricing

Free to download and self-host under the Functional Source License (FSL-1.1-MIT), which becomes MIT after the license's delay.
No paid tier, no hosted service, and no token markup; agent access runs on your own subscriptions.

## Compared to

- [LoopTroop](../looptroop/index.md): a planning-first GUI for repo-scale tickets; choose GraphCode when you want connected, unattended, still-attachable loops instead of council planning.
- [Sandcastle](../sandcastle/index.md): a scripted library with sandbox isolation; choose GraphCode for a native visual graph and surviving PTY sessions.
- tmux plus a cron job: the zero-dependency option; GraphCode earns its keep when loops must message each other and be steered mid-run.

## Bottom line

**Recommended for macOS Apple Silicon engineers who want unattended, connected agent loops they can still attach to and correct.**
Not for Intel Macs, Linux, or Windows, and not for anyone who requires an OSI open source license or a multi-maintainer project.

## Changes

- 2026-09-27 - Created.
- 2026-09-29 - Recorded the first stable release, v0.1.76 (September 28), after the 0.1.76-beta2 prerelease, and refreshed star counts.
- 2026-09-30 - Recorded v0.1.77 (September 29, loops reopen their conversations after a codespace or remote-host restart) and refreshed star counts.
- 2026-10-04 - Added the 0.1.78 beta line (three prereleases on October 3) to the status, and refreshed star counts.
- 2026-10-05 - Recorded v0.1.78 (October 4) as the latest release, promoted from the October 3 beta line, and refreshed star counts.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [LoopTroop](../looptroop/index.md) - the planning-first GUI orchestrator
- [Sandcastle](../sandcastle/index.md) - the scripted sandbox library
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md) - the adversarial-verification tmux harness
- [Claude Code](../../harnesses/claude-code/index.md) - the default loop backend

## References

- https://github.com/scgopi/GraphCode - repository, loop types, daemon and CLI, license split, stars, and release data
- https://graphcode.app/ - the graph-engineering model, loop types, self-improving loop, and architecture
- https://raw.githubusercontent.com/scgopi/GraphCode/HEAD/README.md - install, five backends, zmx sessions, and the FSL-1.1-MIT license text
- https://github.com/scgopi/GraphCode/blob/main/LICENSE - the license split between FSL-1.1-MIT app and MIT integration surfaces
- https://openorchestrators.org/ - the curated directory's GraphCode entry
