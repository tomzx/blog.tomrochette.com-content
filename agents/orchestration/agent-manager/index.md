---
title: Agent Manager
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, tmux, tui, multi-cli, worktrees]
readability: 3
audience_notes: >
  Terminal-first engineers choosing between the many tmux TUIs for coding agents, who want to know whether one more is worth installing.
  Assumes you live in tmux and run at least two coding CLIs.
---

Agent Manager is a free, Apache-2.0 Go TUI over tmux that runs nine coding CLIs side by side with per-CLI status detection, worktree spawning, and a review mode that delivers line comments back to the agent.

**Agent Manager is the best-executed member of the most crowded, least differentiated genre in this category, and the debate in its own launch thread named the genre's problem: dozens of tools, barely distinguishable.**

## What it is

A single Go binary that attaches to a private tmux server named `agentmgr` and lays out sessions for Claude Code, OpenCode, Codex, Grok Build, Gemini CLI, Pi, Command Code, Hermes Agent, and Muse Code.
Status detection is per-CLI: the TUI reads each pane the way a person would and reports the agent's state.
You can send a prompt without attaching, spawn an agent into a worktree, open full-file diffs, leave review comments that go back into the agent's conversation, and kill or revive a session on its own conversation.
It is distributed as brew, an install script, an AUR package, mise, go install, and release binaries; Apache-2.0 since v0.19.0 (2026-08-04), MIT before, which is why older write-ups state the wrong license.

## Status

Active and young: 573 stars and 58 forks as of 2026-10-07, created 2026-07-15, with 29 contributors.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=YoanWai/agent-manager&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=YoanWai/agent-manager&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=YoanWai/agent-manager&type=date&legend=top-left" />
</picture>

Releases run roughly weekly: v0.40.0 shipped 2026-10-06, ten days after v0.39.0 capped a September with five releases.
The Show HN thread from 2026-07-30 reached 98 points and about 80 comments, dominated by the genre question: one commenter argued submissions like it should be filtered automatically "since there are dozen of these and they are barely distinguishable except for couple of opinioned choices".

## Strengths

- Nine CLIs with per-CLI state detection is the deepest pane-reading integration among the tmux columns here.
- The review loop closes: comments travel back into the agent's conversation instead of stopping at a diff view.
- Kill and revive on the same conversation answers the lost-context fear that stops people from restarting agents.
- Sessions live on a private tmux server, so the tool's panes never mix with your own, and distribution breadth (brew, AUR, mise, go install, binaries) makes trying it a two-minute decision.

## Cautions

- The genre is saturated: the launch thread's own verdict was that these tools are barely distinguishable, and picking this one over Claude Squad or dmux is a preference, not a derivation.
- The site's own feature list ends with "Not here yet: cost tracking", so teams that bill per agent need another tool.
- The mid-stream license change (MIT through v0.18.0, Apache-2.0 from v0.19.0 on 2026-08-04) means older coverage misstates the license.
- 0.x versioning with weekly releases: expect churn, and 570 stars is the smallest maintained footprint among the tmux columns besides The Perfect Orchestrator.

## Pricing

Free, in the site FAQ's own word: "Nothing", under Apache-2.0, with no account.
No paid tier exists; sessions run on the CLIs and subscriptions you already have.

## Compared to

- [Claude Squad](../claude-squad/index.md): the minimal tmux-and-worktrees manager; choose Claude Squad for the smallest footprint, Agent Manager for status detection and the comment-back review loop.
- [dmux](../dmux/index.md): the TUI that gives every task pane its own worktree and branch; choose dmux for per-task isolation by default, Agent Manager for nine-CLI breadth.
- [cmux](../cmux/index.md): the macOS terminal built around attention routing; choose cmux on a Mac for notification rings and cloud tasks, Agent Manager anywhere tmux runs.

## Bottom line

**Recommended for terminal-first engineers who run three or more different coding CLIs and want one pane of glass with review comments that reach the agent.**
Not for teams that need cost tracking, per-task worktree defaults, or a GUI.

## Changes

- 2026-10-06 - Created.
- 2026-10-07 - Added the YoanWai/agent-manager star history chart to the Status section.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Claude Squad](../claude-squad/index.md) - the minimal tmux incumbent
- [dmux](../dmux/index.md) - the worktree-per-task tmux TUI
- [cmux](../cmux/index.md) - the macOS terminal rival
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this category extends

## References

- https://api.github.com/repos/YoanWai/agent-manager - stars, forks, Apache-2.0 license, creation date, and push date as of 2026-10-05
- https://agent-manager.dev - the FAQ: license history, the "Nothing" pricing answer, distribution, the nine-CLI list, and the cost-tracking gap
- https://raw.githubusercontent.com/YoanWai/agent-manager/main/README.md - status detection, review mode, kill and revive, worktree spawning, and the private tmux server
- https://api.github.com/repos/YoanWai/agent-manager/releases - v0.39.0 (2026-09-26) and the weekly cadence
- https://news.ycombinator.com/item?id=49107749 - the Show HN thread (98 points, about 80 comments) and the distinguishability debate
