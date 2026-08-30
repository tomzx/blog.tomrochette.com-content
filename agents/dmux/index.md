---
title: dmux
created: 2026-08-24
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, orchestration, git-worktrees, terminal, open-source]
readability: 3
audience_notes: >
  Terminal-first engineers juggling several coding-agent CLIs who want worktree and merge plumbing without a GUI.
  Assumes familiarity with tmux, npm global installs, and at least one supported agent CLI.

---

dmux is an MIT-licensed terminal multiplexer for coding agents: a tmux-based TUI where each task pane gets its own git worktree and branch, from the standardagents project led by Justin Schroeder (FormKit) and Boyd.
Facts below verified as of 2026-08-30.

**It is the terminal-native answer to the GUI worktree dashboards, with the widest agent fan-out in the category, and a community footprint that is still an order of magnitude smaller than its ambition.**

## What it is

Install with `npm install -g dmux`, run `dmux` in a repo, press `n`, type a prompt, and pick one or more agents.
**Each pane is a full working copy: dmux creates the worktree, names the branch with an AI-generated label, launches the chosen CLIs, and later merges or opens a GitHub PR from a pane menu.**
It supports Claude Code, Codex, OpenCode, Cline, Gemini, Qwen, Amp, pi, Cursor, Copilot, and Crush CLIs, plus plain terminal panes that restore their last directory and even resume interrupted agent conversations.
Requirements are Node 18+, tmux 3.0+, and git 2.20+.
Extras include lifecycle hooks (worktree create, pre-merge, post-merge), macOS notifications, a file browser, pane hiding, and multi-project sessions.

## Status

Active and shipping.
The repository was created 2025-08-20, was last pushed 2026-08-16, and shows 747 commits, about 1,758 stars, and 138 forks as of 2026-08-30.
npm recorded 2,008 downloads in the last month as of 2026-08-30.
**Community discussion is thin: the August 2025 launch thread got 3 points and the February 2026 thread got 9 points with zero comments on Hacker News.**
That gap between repo activity and discussion footprint is the main signal to watch.

## Strengths

- Multi-select launches run two or three different agents on the same prompt in isolated worktrees, which is the cheapest A/B evaluation of models I have seen in any tool here.
- Durable terminals that resume agent conversations after restart solve a real annoyance of raw tmux.
- Wrapping native CLIs means new harness features appear without waiting for dmux to reimplement them.
- MIT license, no subscription, no account.

## Cautions

- Effectively a small-maintainer project (two named authors), so bus factor is low.
- The docs site (dmux.ai) is JavaScript-heavy and rendered nearly empty for me, so the README is the real documentation.
- AI naming, summaries, and pane analysis require configuring an inference provider, which adds a setup dependency the core loop does not need.
- No cloud or remote execution mode; everything runs on your machine inside tmux.

## Pricing

Free and open source under MIT.
No paid tiers; the site credits FormKit, Inc. for sponsorship.

## Compared to

- [Claude Squad](../claude-squad/index.md): simpler, single Go binary, AGPL; choose it when you want less machinery.
- [Conductor](../conductor/index.md): the polished, funded Mac GUI covering the same workflow; choose it when you want review ergonomics over terminal control.
- Raw tmux plus worktree aliases: free forever, but you rebuild naming, merge, and PR plumbing yourself.

## Bottom line

**Recommended for terminal-first engineers who want merge plumbing and multi-agent fan-out without leaving the keyboard.**
Not for anyone who needs a supported product, documentation depth, or remote execution.
My disagreeable claim: multi-agent fan-out is mostly a gimmick, and dmux's genuinely durable idea is resumable agent terminals, which every GUI dashboard should copy.

## See also

- [Claude Squad](../claude-squad/index.md) - the leaner tmux alternative in the same niche
- [Claude Code](../claude-code/index.md) - the primary agent most dmux panes run
- [Crush](../crush/index.md) - one of the eleven supported agent CLIs
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the layer map this tool belongs to

## References

- https://github.com/standardagents/dmux - README, agent list, requirements, hooks
- https://api.github.com/repos/standardagents/dmux - stars, commits, push dates, MIT license
- https://dmux.ai - official site, authors, license and sponsorship credit
- https://news.ycombinator.com/item?id=47075312 - February 2026 thread (9 points) showing the small discussion footprint
- https://api.npmjs.org/downloads/point/last-month/dmux - 2,008 downloads in the last month
