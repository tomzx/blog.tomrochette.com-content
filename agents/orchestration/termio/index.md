---
title: termio
created: 2026-11-01
updated: 2026-11-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, terminal, tmux-alternative, ssh]
readability: 3
audience_notes: >
  macOS engineers who live in the terminal, run several coding CLIs, and want session state and attention routing without learning tmux.
  Assumes you know what Claude Code or Codex sessions look like.
---

termio is a terminal-first agentic development environment: a native macOS terminal built so coding agents run where they already live, and the app tells you which one needs you.

**The bet is that when agents write most of the code, the environment's job is session state and attention routing, and it should stay a terminal rather than become a dashboard.**

## What it is

A free macOS 14+ app (dmg or Homebrew cask, Sparkle auto-updates) that wires up each agent's own hooks on first launch, so every session reports working, idle, or needs-you as a sidebar dot, a menu-bar tray ring, and the same signal on your phone.
Every session's shell lives in `termiod`, a daemon, so quitting the app only detaches: close the laptop, reopen, and the session is where you left it, same process and scrollback, a tmux alternative without the tmux vocabulary.
Twelve CLIs are named (Claude Code, Codex, OpenCode, Pi, Amp, Cursor, Copilot, Kimi, Antigravity, Crush, Grok, and any other CLI agent).
The remote mode turns any SSH-reachable Linux VPS into an agent host: termio reads `~/.ssh/config`, copies one binary into `~/.local/bin`, and the session lives on the box, not in the connection, so dropping the link leaves the agent working and reattaching restores the exact screen.
An iPhone companion (TestFlight beta) pairs by QR code; project sessions pair with worktrees in the sidebar.
By the termio-sh org, repository created 2026-05-23, MIT licensed, site at termio.sh with docs and a changelog.

## Status

Active and fast: 751 stars, 63 forks, and 37 open issues and pull requests as of 2026-11-01 (GitHub API), pushed 2026-11-02, with 100-plus releases and v0.71.0 out on 2026-11-02 (v0.70.0 and v0.70.1 the same day) after v0.69.0 (2026-10-31), which had matched the Homebrew cask the same day.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=termio-sh/termio&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=termio-sh/termio&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=termio-sh/termio&type=date&legend=top-left" />
</picture>

Zero Hacker News coverage found as of 2026-11-01; the footprint is the repository, the download server, and the Homebrew tap.

## Strengths

- **Daemon-backed session persistence is the differentiator: the tmux benefit (detach, survive, reattach) without requiring you to learn tmux.**
- Hooks-first integration means no wrapper forks around the CLIs; the agents stay stock and termio reads their own state signals.
- The SSH remote mode is designed correctly: the session lives on the box, so connection drops never kill work.

## Cautions

- macOS only today, with no Windows or Linux desktop story; Linux appears only as a remote daemon host.
- Zero independent coverage as of 2026-11-01; adoption evidence is the star count and the release cadence.
- A 100-release pre-1.0 train in five months promises churn.

## Pricing

Free, no account, MIT licensed.
No paid tier found as of 2026-11-01.

## Compared to

- [tuios](../tuios/index.md): the Go terminal window manager with per-pane agent state and worktree fan-out; termio is the macOS-native, daemon-backed counterpart with a phone companion.
- [herdr](../herdr/index.md): the Rust daemon multiplexer restoring layouts for 18 CLIs; termio trades breadth for a polished native Mac shell.
- [cmux](../cmux/index.md): Manaflow's Ghostty-based macOS terminal; termio adds the SSH remote mode and the needs-you routing.

## Bottom line

**Recommended for macOS engineers who want tmux's session durability and agent attention routing without tmux's learning curve.**
Not for Windows or Linux desktop users, and not for anyone needing diff review surfaces, which it leaves to the CLIs.

## Changes

- 2026-11-01 - Created.
- 2026-11-07 - Re-verified in rotation: every cited URL re-fetched live (repository API, README, releases, Homebrew cask, download server, HN search); no factual drift, still quiet since the 2026-11-02 push, HN still returns nothing.

## See also

- [tuios](../tuios/index.md) - the per-pane agent-state TUI sibling
- [herdr](../herdr/index.md) - the cross-platform daemon multiplexer contrast
- [cmux](../cmux/index.md) - the other macOS terminal built for agents
- [Agent Manager](../agent-manager/index.md) - the Go TUI with per-CLI status detection

## References

- https://api.github.com/repos/termio-sh/termio - stars, license, and activity as of 2026-11-01
- https://raw.githubusercontent.com/termio-sh/termio/HEAD/README.md - the termiod daemon model, hooks integration, remote ADE, and mobile companion
- https://api.github.com/repos/termio-sh/termio/releases?per_page=100 - the 100-release train through v0.69.0 (2026-10-31)
- https://raw.githubusercontent.com/termio-sh/homebrew-tap/HEAD/Casks/termio.rb - the Homebrew cask at 0.69.0 with Sparkle livecheck
- https://downloads.termio.sh/termio.dmg - the macOS download endpoint (HTTP 200, 2026-11-01)
- https://hn.algolia.com/api/v1/search?query=termio.sh&hitsPerPage=5 - the zero-hit Hacker News footprint as of 2026-11-01
