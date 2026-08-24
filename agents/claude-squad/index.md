---
title: Claude Squad
created: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, orchestration, git-worktrees, terminal]
readability: 3
audience_notes: >
  Engineers who live in a terminal and want to run several coding agents at once without a GUI.
  Assumes you already use at least one CLI agent such as Claude Code or Codex and are comfortable with tmux.

---

Claude Squad is a free, AGPL-3.0 terminal app (command `cs`) that manages multiple coding agents in tmux sessions, each isolated in its own git worktree.
Facts below verified as of 2026-08-24.

**It is the minimal, single-binary version of the parallel-agent pattern, and at about 8.4k GitHub stars it became the default terminal recommendation despite almost no launch buzz.**

## What it is

A Go TUI from the smtg-ai organization, installed with `brew install claude-squad` (it is in homebrew-core, v1.0.20 as of 2026-08-24).
**The whole architecture is three primitives you already know: tmux for sessions, git worktrees for isolation, and a TUI for navigation.**
Each task runs in the background (an experimental auto-accept "yolo" mode included), you review diffs in a preview tab, and you commit, push, checkout, or resume from a keyboard menu.
Profiles let you launch any program per session, with Claude Code as the default and Codex, Aider, and Gemini as documented alternatives.
Prerequisites are just tmux and the GitHub CLI.

## Status

Active but slow-burning.
The repository was created in March 2025, was last pushed to on 2026-08-20, and shows 222 commits, about 8,358 stars, and 611 forks as of 2026-08-24.
Homebrew reports 5,611 installs over the last 365 days as of 2026-08-24, which is real but modest usage for its star count.
**Its Hacker News footprint is nearly empty (a 5-point launch thread in April 2025), so adoption spread through GitHub and word of mouth, not press.**

## Strengths

- Smallest dependency footprint in the category: one Go binary plus tmux and gh.
- Packaged in homebrew-core, so installation and updates are boring in the good way.
- Agent-agnostic through profiles despite the Claude-centric name.
- Background completion with a diff-review tab covers the core loop of dispatch, wait, review, merge.

## Cautions

- AGPL-3.0 is a hard no for many corporate environment policies.
- Development cadence is modest for such a popular repo, and the bus factor looks small.
- First-run reports in the ecosystem describe clunky onboarding, and there is no Windows story because tmux is a hard requirement.
- Worktree isolation does not copy untracked files like `.env`, a shared complaint across every tool in this category.

## Pricing

Free and open source under AGPL-3.0.
No paid tier, hosting, or subscription exists.

## Compared to

- dmux (../dmux/index.md): also tmux-based but multi-select fan-out and MIT; choose dmux for breadth, Claude Squad for a single static binary.
- Emdash (../emdash/index.md): a full desktop app with SSH remoting; choose it when you want a GUI and issue tracking.
- Plain tmux plus a worktree script: still viable, and what Claude Squad automates is only about 200 lines of shell away.

## Bottom line

**Recommended as the lowest-commitment way to try worktree-parallel agents in a terminal.**
Not for AGPL-averse companies or anyone who wants a supported product.
My disagreeable claim: for most engineers, Claude Squad plus a small setup script covers 90 percent of what the funded dashboards sell, because the dashboards' real product is review ergonomics, not parallelism.

## See also

- [dmux](../dmux/index.md) - the feature-rich MIT successor question to this same tmux-plus-worktrees design
- [Claude Code](../claude-code/index.md) - the harness most Claude Squad sessions drive
- [OpenCode](../opencode/index.md) - a lean harness that pairs well with terminal multiplexing
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where orchestration tools sit relative to harnesses and surfaces

## References

- https://github.com/smtg-ai/claude-squad - README, features, profiles, install options
- https://api.github.com/repos/smtg-ai/claude-squad - creation and push dates, stars, AGPL license
- https://smtg-ai.github.io/claude-squad/ - official site and prerequisites
- https://formulae.brew.sh/formula/claude-squad - homebrew-core packaging, version 1.0.20, install analytics
- https://news.ycombinator.com/item?id=43575127 - the small April 2025 launch thread
