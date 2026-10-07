---
title: hcom
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, cli, messaging, multi-agent, terminals]
readability: 3
audience_notes: >
  Engineers running several coding-agent CLIs in terminals who want the agents to
  coordinate directly instead of through a dashboard, and who will judge a
  shared-token security model. Assumes familiarity with tmux-style workflows.
---

hcom is an MIT-licensed CLI that lets coding agents message, watch, and spawn each other across terminal windows, turning separate CLI sessions into one ad-hoc team.

## What it is

hcom, created 2025-07-21 and written in Rust with a Python distribution, puts a thin coordination fabric in front of any terminal: start an agent with `hcom` in front, then prompt normally, and the agents gain the ability to message, watch, and spawn each other.
It works with thirteen CLIs (claude, codex, opencode, copilot, qoder, grok, pi, omp, agy, cursor, kimi, kilo, gemini), supports spawn, fork, resume, and kill in any terminal emulator or headless, and pane-aware terminals (kitty, wezterm, tmux, zellij, waveterm, cmux, herdr) can even close panes from `hcom kill`.
It occupies a niche none of this category's boards and platforms fill: coordination as a message bus over the terminals you already run, with no dashboard, database, or worktree model of its own.

## Status

Active and early: 559 stars, a push on 2026-10-06, release v0.7.28 on 2026-10-06, and `hcom` 0.7.28 on PyPI as of 2026-10-07 (GitHub API, PyPI), installable with uv or Homebrew, on a repository created 2025-07-21.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=aannoo/hcom&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=aannoo/hcom&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=aannoo/hcom&type=date&theme=dark&legend=top-left" />
</picture>

**The independent footprint is one 2-point Hacker News thread from 2026-02-14, so every adoption signal beyond the star count is self-reported, and the README's own examples ("spawn 3x opencode, split work, collect results") are the best available evidence of the intended use.**
Every agent runs in a terminal you can see, scroll, and interrupt, which is the design answer to the trust question the bigger platforms answer with audit logs.

## Strengths

- The mechanism is small enough to adopt per-session: no daemon to deploy, no database to run, no dashboard to learn.
- Cross-CLI breadth (thirteen CLIs) is the widest harness list in this category relative to the project's size.
- Live coordination primitives (message, watch, events with idle waits) compose with shell scripting instead of replacing it.

## Cautions

- The security boundary is a shared auth token the README itself says to treat like an API or SSH key, with SECURITY.md carrying the model; any agent in the fabric can message and spawn the others.
- No worktree, branch, or review model: coordination happens, but code safety stays the agent's and your problem.
- The fabric only exists while terminals run, and a 0.x version line means the protocol between agents can change.

## Pricing

Free, open source under the MIT license; no paid tier found.

## Compared to

Buzz is the heavyweight version of the same idea, a self-hosted Nostr relay carrying a whole team's communication, git hosting, and workflows; choose Buzz for a durable team fabric, hcom for today's terminal sessions.
Agent Manager drives nine CLIs from one tmux TUI; hcom is the inverse, agents staying in their own terminals while they coordinate.
Claude Squad bundles the same terminal-plus-worktree world with git worktrees and a diff tab; choose it when review matters more than messaging.

## Bottom line

Recommended for terminal-first engineers who want their existing coding CLIs to talk to each other without adopting a platform, and who will manage the shared token like any credential.
Not for teams that need audit trails, review gates, or anything that survives the terminal closing.

## Changes

- 2026-10-07 - Created.

## See also

- [Buzz](../buzz/index.md) - the self-hosted communication-fabric alternative at platform scale.
- [Agent Manager](../agent-manager/index.md) - the tmux TUI that drives multiple CLIs from one pane instead of messaging between panes.
- [Claude Squad](../claude-squad/index.md) - the terminal worktree manager next to which hcom's no-worktree stance is clearest.
- [dmux](../dmux/index.md) - the worktree-per-pane tmux alternative hcom deliberately does not compete with.

## References

- https://github.com/aannoo/hcom - the repository, README's CLI list and mechanism, stars, and license.
- https://pypi.org/project/hcom/ - the PyPI package and its current 0.7.28 version.
- https://github.com/aannoo/hcom/blob/main/SECURITY.md - the security model behind the shared auth token.
- https://github.com/aannoo/hcom/releases - the release list, v0.7.28 (2026-10-06) latest at verification.
- https://news.ycombinator.com/item?id=47011053 - the 2-point February 2026 thread, the project's whole independent footprint.
