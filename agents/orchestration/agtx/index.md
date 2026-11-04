---
title: agtx
created: 2026-11-01
updated: 2026-11-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, terminal, worktree, blackboard]
readability: 3
audience_notes: >
  Terminal-first engineers who want several coding CLIs working on one task list in parallel, each in its own worktree.
  Assumes you know what git worktrees and tmux are.
---

agtx is a terminal-native agentic development environment that runs eight coding CLIs as specialists around one shared blackboard: tasks on a kanban, each executed by an agent in its own git worktree and tmux window.

**The bet is the blackboard architecture from AI research: specialists that never see each other's context, exchanging only what lands on the board.**

## What it is

A Rust TUI installed by script or built with cargo, driving Claude Code, Codex, Cursor, Grok, OpenCode, Gemini CLI, and more (eight CLIs) against a task lifecycle of backlog, planning, running, review, and done with a dependency graph.
Each phase can run a different agent with automatic switching and context handover, e.g. Grok researching, Claude implementing, Codex reviewing, with the conversation history persisted across the phases.
When a review task goes idle, agtx checks merge conflicts against the default branch with a non-destructive virtual merge (`git merge-tree`) and hands the agent its own `/agtx:merge-conflicts` skill to resolve and re-commit.
A QR-paired installable web app puts the board, task details, diffs, and the live terminal (keyboard included, for permission prompts) on your phone over Wi-Fi or a Tailscale tailnet, and an `/agtx:oneshot` skill runs the whole board unattended, planning milestone waves, unblocking workers, judging review, and merging.
By Fynn Fluegge, repository created 2026-02-08, Apache-2.0 licensed.

## Status

Active but slowing: 1,728 stars, 144 forks, and 28 open issues and pull requests as of 2026-11-01 (GitHub API), last push 2026-11-03 (no release since v1.0.6 on 2026-09-16).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=fynnfluegge/agtx&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=fynnfluegge/agtx&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=fynnfluegge/agtx&type=date&legend=top-left" />
</picture>

Zero Hacker News stories found as of 2026-11-01; the footprint is the repository, a Trendshift listing, and the README feature set.

## Strengths

- **One worktree and tmux window per task, with agent-driven conflict resolution, is workflow depth most board tools fake with a checkbox.**
- The per-phase agent assignment (research, implement, review) makes multi-model collaboration concrete instead of aspirational.
- The oneshot skill turns the board into an unattended runner with merge judgment, a full loop rather than a launcher.

## Cautions

- The release train stopped at v1.0.6 in mid-September 2026 and the last push is nine days old at this writing, so momentum is worth watching before you depend on it.
- Solo-maintained, with no third-party reviews or benchmarks found.
- The mobile web app needs the same network or a tailnet, so it is a companion, not a hosted control plane.

## Pricing

Free and open source under Apache-2.0.
No paid tier, account, or hosted service as of 2026-11-01.

## Compared to

- [dmux](../dmux/index.md): the tmux TUI pairing one task pane with one worktree; agtx adds the phase lifecycle and cross-model handover.
- [LoopTroop](../looptroop/index.md): the local GUI orchestrator with council planning over OpenCode; agtx stays terminal-native and drives eight CLIs.
- [Vibe Kanban](../vibe-kanban/index.md): the board-first web app; agtx is the terminal counterpart with per-task worktrees as the core mechanism.

## Bottom line

**Recommended for terminal people who want per-task worktree parallelism with different models owning different phases of one task.**
Not for GUI-first users, and not for remote or VPS workflows, which it does not target.

## Changes

- 2026-11-01 - Created.
- 2026-11-04 - Status refresh: the push date refreshed to 2026-11-03; the release line still ends at v1.0.6 (2026-09-16).

## See also

- [dmux](../dmux/index.md) - the one-pane-one-worktree precedent this note extends
- [LoopTroop](../looptroop/index.md) - the GUI-and-council counterpart
- [Vibe Kanban](../vibe-kanban/index.md) - the web board alternative
- [CLI Agent Orchestrator](../cli-agent-orchestrator/index.md) - AWS's tmux-session supervisor over twelve CLIs

## References

- https://api.github.com/repos/fynnfluegge/agtx - stars, license, and activity as of 2026-11-01
- https://raw.githubusercontent.com/fynnfluegge/agtx/HEAD/README.md - the blackboard model, phases, worktrees, mobile app, and oneshot skill
- https://api.github.com/repos/fynnfluegge/agtx/releases?per_page=100 - the 27-release train through v1.0.6 (2026-09-16)
- https://hn.algolia.com/api/v1/search?query=agtx&tags=story&hitsPerPage=5 - the zero-story Hacker News footprint as of 2026-11-01
- https://trendshift.io/repositories/23889 - the Trendshift listing linked from the README
