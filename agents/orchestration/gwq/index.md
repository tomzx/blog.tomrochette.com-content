---
title: gwq
created: 2026-10-21
updated: 2026-10-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, git-worktrees, cli, tmux]
readability: 3
audience_notes: >
  Terminal-first engineers who run parallel coding agents across several repositories and want
  worktree creation, discovery, and status without a dashboard app. Assumes you already use
  git worktrees and at least one agent CLI.
---

gwq is an Apache-2.0 Go CLI that manages Git worktrees the way ghq manages clones: fuzzy-finder creation, switching, and deletion, a global view across every repository, a status dashboard, and tmux sessions for long-running commands, positioned explicitly for parallel AI coding agents.

**gwq's bet is that worktree management is a discovery problem, not a Git problem: point it at a base directory, and every worktree in every repository is one fuzzy search away.**

## What it is

A single-binary Go tool by d-kuro (Masayuki Ishii, a Kubernetes engineer), installed from his Homebrew tap, `go install`, or source, with the repository created 2025-05-26.
Commands cover the lifecycle: `add` (new or existing branch, interactive pick), `list` with a global `-g` flag and JSON output, `get` for shell substitution, `cd` through shell integration, `exec` to run a command inside a worktree, `remove` with dry-run and branch cleanup, `status --watch` with filters, sorting, and CSV, `tmux run/attach/kill` for long-lived processes, and TOML `config` with global and per-project files.
Discovery is filesystem scanning under `worktree.basedir` (default `~/worktrees`) with no registry, and a naming template of `{{.Host}}/{{.Owner}}/{{.Repository}}/{{.Branch}}`.
Per-repository `repository_settings` copy untracked files (recursive since v0.1.2, with `.git` never copied) and run setup commands, so a new worktree arrives ready.
The README's workflow section is blunt about the audience: create three worktrees, run `claude` in each, and watch them with `gwq status --watch`.

## Status

Active with a slow release train: 475 stars and 23 forks as of 2026-10-21, repository created 2025-05-26, default-branch push 2026-10-02, latest release v0.1.2 on 2026-10-02 after v0.1.1 in May (GitHub API and releases, as of 2026-10-21).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=d-kuro/gwq&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=d-kuro/gwq&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=d-kuro/gwq&type=date&legend=top-left" />
</picture>

The independent footprint exists but is small: a two-point HN submission from May 2026 with no comments, and a September 2026 post on shunk031.me building a ghq × gwq × fzf workflow around it.
**Seventeen months of existence, a year of it before the agent boom, gives gwq the oldest creation date of any tool in its seat; the quiet release train is the trade.**

## Strengths

- Global discovery without a registry: `-g` works from anywhere, and v0.1.2 made it fast (parallel git calls took a six-second scan with a large `node_modules` down to 0.2 seconds).
- `copy_files` solves the untracked-files problem per repository, with rules for symlinks, nested repositories, and self-copying when the worktree base lives inside the repo.
- `status --watch` is a terminal dashboard for parallel agent runs, with JSON and CSV output for scripting.
- tmux integration keeps dev servers and watchers alive per worktree while the agent works.
- One Go binary, shell completion for bash, zsh, and fish, and a Homebrew tap.

## Cautions

- No PR, diff, or review surface: it manages checkouts, not change delivery, so pair it with a review tool.
- v0.1.x means the command set and config format can still move.
- Two releases in 2026: fixes land on the default branch well before they land in the tap.
- One maintainer whose public attention is mostly Kubernetes tooling.
- Shell integration does not support PowerShell.

## Pricing

Free and open source under Apache-2.0.
No hosted tier and no paid plan; you pay only for the agents you run inside the worktrees.

## Compared to

- [Worktrunk](../worktrunk/index.md): the other worktree-lifecycle CLI here; Worktrunk is Rust with hooks and a one-command merge, while gwq's edge is the global cross-repository view and the fuzzy finder.
- [Claude Squad](../claude-squad/index.md): runs agents inside tmux sessions with worktrees; gwq manages the worktrees and leaves session management to you.
- Plain `git worktree` plus a shell function: zero dependencies; gwq earns its keep once worktrees span several repositories and you want one status view.

## Bottom line

Recommended for terminal-first engineers running parallel agents across many repositories who want discovery and status without an app.
Not for anyone expecting review, PR, or session management from the same tool.

## Changes

- 2026-10-21 - Created.

- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart markup (the light source carried the dark-theme parameter; the theme parameter now sits only on the dark source).

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Worktrunk](../worktrunk/index.md) - the other worktree-lifecycle CLI in the category
- [Claude Squad](../claude-squad/index.md) - the tmux-and-worktree runner one level up
- [dmux](../dmux/index.md) - the tmux TUI that gives every task pane a worktree
- [herdr](../herdr/index.md) - the terminal runtime that owns agents' panes outright

## References

- https://api.github.com/repos/d-kuro/gwq - repository, license, counts, and dates (as of 2026-10-21)
- https://raw.githubusercontent.com/d-kuro/gwq/main/README.md - commands, the parallel-agent workflow section, install, and configuration
- https://api.github.com/repos/d-kuro/gwq/releases - the v0.1.x release train and dates
- https://raw.githubusercontent.com/d-kuro/gwq/main/docs/release-notes/v0.1.2.md - recursive copy_files rules and the global-discovery speedup
- https://shunk031.me/post/ghq-gwq-fzf-worktree/ - the third-party ghq × gwq × fzf workflow write-up
- https://hn.algolia.com/api/v1/items/48034159 - the two-point, no-comment May 2026 HN footprint
