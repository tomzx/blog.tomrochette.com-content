---
title: Parallel Code
created: 2026-10-23
updated: 2026-10-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, worktrees, desktop, multi-harness, electron]
readability: 3
audience_notes: >
  macOS or Linux engineers who run several CLI coding agents and want a desktop that
  isolates every task in its own worktree and helps them compare and merge the results.
  Assumes you already pay for at least one agent CLI subscription.
---

Parallel Code is Johannes Millan's MIT-licensed Electron desktop app that dispatches coding-agent tasks in parallel, each in its own git worktree and branch, with diff review, guided change tours, an AI Arena mode that races agents head-to-head, and phone monitoring over Wi-Fi or Tailscale.

**Parallel Code's bet is comparison: instead of one agent iterating, run several and merge the best diff, with the review aids to tell them apart.**

## What it is

An Electron and SolidJS desktop app for macOS and Linux (dmg, AppImage, and deb packages, or `npm run dev` from source on Node 18+), by johannesjo (Johannes Millan), the author of the 23k-star open-source task manager Super Productivity.
It drives Claude Code, Codex CLI, Gemini CLI, Copilot CLI, and Antigravity CLI natively, with no API wrapper between you and the CLI.
Creating a task automates the git structure the tool exists for: a branch from your configured base, a worktree for it, symlinks for `node_modules` and other gitignored directories, then the agent spawned inside that tree, with the branch merged back from the sidebar when you are satisfied.
Around that loop it piles on review aids: a built-in diff viewer with inline comments, guided change tours generated from a branch's diff, model-written task briefs that flag claims the diff does not show, confidence ratings, a board view across projects kept in Obsidian-compatible `KANBAN.md`, a browser preview inside the task canvas, per-task shell terminals, optional Docker sandboxing via a `.parallel-code/Dockerfile`, a PR CI watcher, and a Super Productivity integration that syncs the focused task both ways.

## Status

Active and solo-led: 1,060 stars, 144 forks, 23 contributors, and 48 open issues and pull requests on a repository created 2026-02-18, pushed 2026-10-25, with v5.0.0 (2026-10-25) the latest release, the first after the v4 line's v4.0.0 (2026-10-10), carrying task briefs with confidence ratings replacing Steps, a per-project Markdown Kanban board over live tasks and GitHub issues, background verify with a single readiness line, and Android quick replies back behind a button (GitHub API, releases, as of 2026-10-26).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=johannesjo/parallel-code&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=johannesjo/parallel-code&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=johannesjo/parallel-code&type=date&legend=top-left" />
</picture>

The independent footprint is thin: the Show HN launch on 2026-02-22 drew 2 points and no comments (HN Algolia), and I found no press coverage, so the 1.1k stars ride the author's Super Productivity audience and word of mouth.
Four major versions in eight months is the other side of that coin: the surface moves faster than any community scrutiny has formed around it.

## Strengths

- Worktree automation that covers the boring edges: gitignored-directory symlinking, existing-worktree import, non-git folders, and a direct mode that works on the main branch when isolation is not wanted.
- AI Arena races agents head-to-head on the same task, which turns the parallel-worktree design into an actual comparison protocol rather than just concurrent windows.
- The review stack (tours, briefs, confidence ratings) is generated from the diff itself, so review effort scales with the change rather than with your patience.
- Phone monitoring over Wi-Fi or Tailscale with no external service or account.
- MIT and free, with your agent subscriptions the only cost.

## Cautions

- v4.0 in eight months means the workflow surface (tours, briefs, ratings, board) churns between versions, and nothing here is an API to script against.
- macOS and Linux only; there is no Windows build.
- Antigravity tasks cannot run inside Docker isolation because its keyring-based sign-in has no container path, a limitation the README documents rather than solves.
- One author, and a 2-point launch thread, so the tool has never faced independent scrutiny at scale.

## Pricing

Free and open source under MIT, with no hosted tier and no paid plan.
You pay your existing agent subscriptions and nothing to the tool.

## Compared to

- [Claude Squad](../claude-squad/index.md): the terminal minimalist's version of the same worktree-per-agent loop; Claude Squad costs nothing but your tmux fluency, Parallel Code adds GUI review and arena comparison.
- [Agent Orchestrator](../agent-orchestrator/index.md): the kanban at 13.5k stars driving 26-plus CLIs; choose it for scale and CI-feedback loops, Parallel Code for tour-assisted review and head-to-head racing on a smaller surface.
- [Emdash](../emdash/index.md): the bigger ADE with 25-plus auto-detected CLIs, SSH-first execution, and YC backing; Parallel Code is narrower, keyboard-first, and independent.

## Bottom line

Recommended for keyboard-first macOS and Linux engineers who want to race or parallel-dispatch the major CLIs in per-task worktrees with real review aids, at zero cost.
Not for Windows users, not for teams that need multi-maintainer durability, and not for anyone scripting against a stable API.

## Changes

- 2026-10-23 - Created after the coordinator handoff flagged the unmatched repository, admitted on the worktree-CLI precedent (gwq, Worktrunk) with the worktree-per-task desktop kind.

- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Recorded the v5.0.0 major (2026-10-25), the first release after the v4 line, with task briefs replacing Steps and a per-project Markdown Kanban board.
- 2026-10-26 - Corrected the star-history chart markup (the light source carried the dark-theme parameter; the theme parameter now sits only on the dark source).

## See also

- [Claude Squad](../claude-squad/index.md) - the tmux minimalism this tool's GUI adds review and racing to
- [Agent Orchestrator](../agent-orchestrator/index.md) - the kanban scale counterpart at 13.5k stars
- [Emdash](../emdash/index.md) - the broader, SSH-first ADE in the same desktop genre
- [Worktrunk](../worktrunk/index.md) - the worktree-lifecycle CLI underneath this app's manual workflow
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this column joins

## References

- https://api.github.com/repos/johannesjo/parallel-code - repository, license, counts, and dates (as of 2026-10-23)
- https://raw.githubusercontent.com/johannesjo/parallel-code/main/README.md - the harness list, worktree automation, tours, briefs, arena, and platform support
- https://api.github.com/repos/johannesjo/parallel-code/releases - the release train through v5.0.0
- https://hn.algolia.com/api/v1/items/47115578 - the two-point, no-comment Show HN launch (2026-02-22)
- https://api.github.com/repos/super-productivity/super-productivity - the author's Super Productivity app and its 23k-star audience
- https://youtu.be/sLf0tsQA3pU - the intro video linked from the README
