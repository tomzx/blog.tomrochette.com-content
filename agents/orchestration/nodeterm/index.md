---
title: nodeterm
created: 2026-11-01
updated: 2026-11-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, terminal, canvas, kanban]
readability: 3
audience_notes: >
  Engineers juggling many terminals and agent sessions across projects who lose track of stacked tabs.
  Assumes you know what tmux and Claude Code sessions are.
---

nodeterm is a source-available terminal manager that turns terminals and agent sessions into draggable nodes on an infinite canvas, with every project doubling as a Trello-style board of live Claude Code sessions.

**The bet is spatial memory: sessions you can see, place, and zoom into survive restarts and scattered workflows better than a stack of hidden tabs.**

## What it is

An Electron app for macOS (arm64, x64), Linux (x64), and Windows (x64, beta) where a right-click adds a terminal or an agent node, each running in its own persistent tmux session (the app ships its own tmux, so sessions resume with `claude --resume`).
Node kinds cover terminals, agents (Claude Code, Codex, Antigravity, Gemini, GitHub Copilot, opencode, Grok, Cursor, or custom), sticky notes linked to agents as context, a Monaco editor, and diffs; groups bind to git worktrees for agent-per-branch layouts.
Agent nodes carry live transcripts, subagent cards, a per-node context meter, and a "needs you" state that lights the MacBook notch and posts notifications.
The same canvas runs three ways: the desktop app, a self-hosted browser app (Server Edition) with zero open ports, and an iOS companion that attaches to the same live sessions.
By Enes Kirca as an indie project, repository created 2026-06-15, BUSL-1.1 licensed with each release converting to MIT four years after publication.

## Status

Active: 2,287 stars, 264 forks, and 55 open issues and pull requests as of 2026-11-01 (GitHub API), pushed 2026-11-12, with releases through v0.5.1 (2026-11-06) and a Trendshift listing on the README.
The installer download badge reads 16.7k across all releases as of 2026-11-01.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=eneskirca/nodeterm&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=eneskirca/nodeterm&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=eneskirca/nodeterm&type=date&legend=top-left" />
</picture>

Zero Hacker News stories found as of 2026-11-01; the footprint is the repository, the download badge, and the nodeterm.dev docs.

## Strengths

- **The canvas is a genuinely different organizing model: terminals, agents, notes, and diffs as one spatial map beats window management for scattered multi-project work.**
- Session durability is engineered in: shipped tmux, restart restoration, power-and-sleep guards during agent runs.
- The zero-open-port Server Edition and iOS companion extend the same canvas to browser and phone without exposing your machine.

## Cautions

- BUSL-1.1 is source-available, not open source: a competing-product restriction applies until each release ages into MIT.
- The README admits the project costs about $2,000 a month to run and leans on a ten-spot sponsor tier, a funding-risk signal for an indie single-maintainer app.
- Claude Code is the first-class board citizen; other CLIs are agent nodes without the board-and-comments integration.

## Pricing

The desktop app is free.
A Founding Sponsor tier costs $200 per month with ten spots (one taken as of 2026-11-01), buying a logo placement and priority feature requests.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-11-01 | Founding Sponsor | recorded at $200/month, 10 spots, 1 taken (baseline) | https://raw.githubusercontent.com/eneskirca/nodeterm/HEAD/README.md |

## Compared to

- [tuios](../tuios/index.md): the Go terminal window manager with per-pane agent state and an Inbox; nodeterm is the canvas-and-iOS counterpart with a visual map.
- [herdr](../herdr/index.md): the Rust daemon multiplexer owning terminals and restoring layouts; nodeterm adds the spatial layer and the self-hosted browser mode.
- [cmux](../cmux/index.md): Manaflow's macOS terminal for parallel agents; nodeterm crosses to Linux and Windows beta and adds the Server Edition.

## Bottom line

**Recommended for engineers whose scattered, multi-project workflows defeat tab stacks and who want to see every session at once.**
Not for teams needing PR-centric review surfaces, and not for anyone requiring an OSI-approved license today.

## Changes

- 2026-11-01 - Created.
- 2026-11-04 - Status refresh: the push date refreshed to 2026-11-02; v0.4.5 still the latest release.
- 2026-11-06 - Volatile refresh: Recorded v0.5.0 (2026-11-04) as the new latest release.

## See also

- [tuios](../tuios/index.md) - the per-pane agent-state TUI sibling
- [herdr](../herdr/index.md) - the daemon multiplexer contrast
- [cmux](../cmux/index.md) - the macOS terminal-for-agents peer
- [Vibe Kanban](../vibe-kanban/index.md) - the board-first web alternative

## References

- https://api.github.com/repos/eneskirca/nodeterm - stars, license, and activity as of 2026-11-01
- https://raw.githubusercontent.com/eneskirca/nodeterm/HEAD/README.md - the canvas model, node kinds, Server Edition, sponsor tier, and license terms
- https://raw.githubusercontent.com/eneskirca/nodeterm/HEAD/LICENSE - the BUSL-1.1 terms and the four-year MIT conversion
- https://api.github.com/repos/eneskirca/nodeterm/releases?per_page=100 - the 70-release train through v0.4.5 (2026-10-24)
- https://raw.githubusercontent.com/eneskirca/nodeterm/badges/downloads.json - the 16.7k installer-download badge as of 2026-11-01
- https://nodeterm.dev/ - the product site
- https://nodeterm.dev/docs - the documentation home
- https://hn.algolia.com/api/v1/search?query=%22nodeterm%22&tags=(story,show_hn)&hitsPerPage=5 - the zero-story Hacker News footprint as of 2026-11-01
