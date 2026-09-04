---
title: Worktrunk
created: 2026-08-30
updated: 2026-09-03
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, git-worktrees, cli, open-source]
readability: 3
audience_notes: >
  Engineers who run parallel coding agents in git worktrees and want the worktree lifecycle automated from the shell they already use.
  Assumes you know git worktrees and basic shell hooks.
---

Worktrunk (`wt`) is a Rust CLI that makes git worktrees as easy as branches so you can run many coding agents in parallel, with lifecycle hooks, LLM commit messages, and a one-command merge pipeline.
Facts below verified as of 2026-09-04.

**Worktrunk wins by staying out of the way: no TUI to learn, no daemon to run, just worktrees addressed by branch name plus hooks that automate the boring 80 percent of the parallel-agent workflow.**

## What it is

A single native binary around five verbs: `wt switch` (create a branch, worktree, and launch an agent in one command, `-x claude -c feature-a -- 'prompt'`), `wt list` (a status table with staged files, ahead/behind, CI status, and LLM summaries), `wt merge` (squash, rebase, fast-forward, and clean up in one pipeline), `wt remove`, and `wt config`.
Ten hook types (pre/post across switch, start, commit, merge, remove) are defined in a project `.config/wt.toml` or your user config, with pre-hooks blocking on failure and post-hooks running in background; a first-run approval prompt guards project hooks.
Extras include `pr:123` checkout, an interactive picker with diff previews, cache sharing between worktrees for `node_modules`-style directories, and LLM-generated commit messages.
Dual MIT or Apache-2.0 license, Homebrew, cargo, winget, and Arch (pacman) distribution, by Maximilian Roos as the dominant maintainer.

## Status

The leading worktree manager of the agent wave: 6,817 stars, 241 forks, 42 open issues and PRs as of 2026-09-03, created 2025-10-17, 4,982 commits, pushed the day of verification, latest release v0.76.0 on 2026-09-01.
Roughly 76 releases in ten and a half months; still pre-1.0 with breaking changes per release, and effectively a single-maintainer project.

## Strengths

- Purpose-built loop for parallel agents: the `-x` flag plus hooks covers dev servers, dependency installs, and per-worktree databases, not just worktree creation.
- Exceptional documentation, including agent-integration guides, and a status surface (`wt list`) that answers what all my agents are doing at a glance.
- Polished cross-platform distribution with signed Windows binaries and an answer to the Windows Terminal `wt` collision (`git-wt`).
- Fast cadence with community bug reports fixed within days.

## Cautions

- Bus factor approximately one: nearly all human commits are from the maintainer.
- Pre-1.0 churn is real; v0.75 raised the git minimum and broke both the list JSON schema and the library API, and v0.76 changed `-x` from a shell string to a single program name.
- Hooks execute arbitrary shell from project config; the approval system mitigates it, but review `.config/wt.toml` in unfamiliar repos.
- No independent critical review exists yet, and the tool assumes you are comfortable in your own shell and editor.

## Pricing

Free and open source, dual MIT or Apache-2.0, no paid tiers and no hosted component.

## Compared to

- [Claude Squad](../claude-squad/index.md): a TUI that hosts agents inside tmux with a review surface; choose it for one app that supervises agents, Worktrunk to keep your own shell and editor with hooks automating the lifecycle.
- [dmux](../dmux/index.md): a tmux pane per task with AI-named worktrees; choose it for an opinionated tmux flow, Worktrunk for a lighter native binary and deeper git plumbing.
- Plain `git worktree`: zero dependencies and fully standard; fine for occasional use, Worktrunk pays off once you juggle several agents and branches at once.

## Bottom line

**Recommended for terminal-first engineers running two or more parallel agents in one repo who want the worktree lifecycle automated without adopting a dashboard.**
Not for GUI-first workflows, and not for anyone who needs a project to promise stability before 1.0.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Claude Squad](../claude-squad/index.md) - the TUI-supervisor alternative
- [dmux](../dmux/index.md) - the tmux-centric alternative
- [OpenChamber](../openchamber/index.md) - the session-cockpit layer above the same worktrees

## References

- https://github.com/max-sixty/worktrunk - repository, README, commands, license
- https://worktrunk.dev - documentation and agent-integration guides
- https://worktrunk.dev/hook/ - hook types, blocking semantics, and the approval security model
- https://github.com/max-sixty/worktrunk/releases/tag/v0.76.0 - latest release, cadence, and breaking changes
- https://raw.githubusercontent.com/max-sixty/worktrunk/HEAD/README.md - quick start and the maintainer's own positioning
- https://github.com/smtg-ai/claude-squad - comparison data for the TUI alternative
