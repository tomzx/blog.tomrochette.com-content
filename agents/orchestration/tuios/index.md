---
title: tuios
created: 2026-10-28
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, terminal, go, worktrees]
readability: 3
audience_notes: >
  Engineers who live in the terminal and run several coding-agent CLIs, deciding whether a terminal multiplexer can replace their agent dashboard.
  Assumes you know tmux and git worktrees.
---

tuios is a MIT-licensed Go terminal window manager that knows what the coding agents in its panes are doing, with per-pane agent state, one Inbox for everything the agents wait on, agent-to-agent mail, and worktree fan-out.

## What it is

A terminal multiplexer and window manager built on Charm's Bubble Tea v2: BSP tiling, workspaces, a command palette, kitty graphics, a daemon that keeps sessions alive across restarts, SSH server and web terminal modes, and phone pairing with push notifications.
The agent layer is the differentiator: `tuios integration install` wires 19 harnesses (Claude Code, Codex, Gemini CLI, opencode, Crush, Cursor Agent, and more) to report state, 24 agent CLIs are detected by process and screen, and any program can report through the OSC 7501 protocol.
`tuios fan` starts one prompt in several agents, each in its own git worktree, with keep, compare, verify, and diff commands over the attempts; agents message each other through a fenced mailbox; turn checkpoints make each agent turn reviewable and undoable; and `tuios ship` takes an agent's worktree to a commit, merge, or pull request.
It also speaks herdr's socket protocol and ships a tmux shim, so tools built for either multiplexer keep working, and it runs across machines over SSH and Tailscale.
Gaurav Gosain maintains it as a solo project with 5,500-plus commits.

## Status

Active and fast: 6,175 stars on a repository created 2025-09-06, pushed 2026-10-28, with v0.11.1 (2026-10-26) fixing three reported security advisories and adding worktree keys and a new theme (GitHub API, releases, as of 2026-10-28).
Install paths cover Homebrew, AUR, Nix (including nixpkgs), an install script, and Docker, and the docs site ships an in-browser WebAssembly tour.
**The adoption-scrutiny gap is the caution: the only HN thread is 5 points from 2025-10-20, so 6.2k stars arrived without a public debate record, and the only third-party echo is a directory's Tool of the Week badge.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Gaurav-Gosain/tuios&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Gaurav-Gosain/tuios&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Gaurav-Gosain/tuios&type=date&legend=top-left" />
</picture>

## Strengths

- The deepest agent-state integration in the terminal family: five detection tiers (hook, OSC 7501, herdr protocol, screen rules, process) and an `unknown` state that refuses to call a silent pane idle.
- Worktree fleets with side-by-side attempts, per-pane grants that bound what an agent's pane may do, and per-turn checkpoints that make agent work reviewable and reversible.

## Cautions

- Solo-maintained and pre-1.0; the release log is a steady stream of self-found terminal-emulation bugs, which shows diligence but also churn.
- Zero independent coverage: no HN thread above 5 points and no press beyond a directory badge.
- Isolation is per-pane grants, not sandboxing; agents still run as full terminal programs on your machine.

## Pricing

Does not apply: MIT, free, supported by a Ko-fi link.

## Compared to

dmux gives each task pane its own worktree but has no agent state or Inbox; tuios is that idea with the agent layer built in.
herdr owns terminals and reports agent state for 18 CLIs, and tuios deliberately answers herdr's socket protocol instead of fighting it; pick herdr for the daemon-first design and tuios for tiling, graphics, and fleets.
Claude Squad runs agents in tmux sessions with worktrees but without the state detection, mail, review, and ship surfaces.

## Bottom line

Recommended for terminal-first engineers running several agent CLIs who want one screen, one inbox, and worktree fan-out with review built in.
Not for GUI-first teams, and not for anyone whose threat model needs sandboxed isolation rather than grants.

## Changes

- 2026-10-28 - Created.

## See also

- [herdr](../herdr/index.md) - the terminal-runtime member whose socket protocol tuios answers.
- [dmux](../dmux/index.md) - the worktree-per-pane tmux TUI that tuios extends with the agent layer.
- [Claude Squad](../claude-squad/index.md) - the minimal tmux-and-worktree seat in the same family.
- [hcom](../hcom/index.md) - the pure messaging fabric behind tuios's built-in agent mail.

## References

- https://github.com/Gaurav-Gosain/tuios - repository, README feature tables, license, and the star count (as of 2026-10-28).
- https://tuios.dev/ - the documentation site grounding the agents, worktrees, ship, and release-history claims.
- https://raw.githubusercontent.com/Gaurav-Gosain/tuios/main/docs/AGENT_STATE.md - the agent-state guide grounding the detection tiers and mail verbs.
- https://api.github.com/repos/Gaurav-Gosain/tuios - repository metadata, counts, and dates (as of 2026-10-28).
- https://hn.algolia.com/api/v1/search?query=tuios&tags=story - the 5-point 2025 thread grounding the missing-footprint signal.
