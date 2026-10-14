---
title: herdr
created: 2026-10-10
updated: 2026-10-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, terminal-multiplexer, rust, agent-automation, session-persistence]
readability: 3
audience_notes: >
  Engineers deciding where coding agents physically run, who already live in tmux or a terminal and know the harness CLIs.
  Assumes you know what detach and reattach mean and what an agent lifecycle state is.
---

herdr is a Rust terminal-multiplexer daemon that owns coding agents' terminals: panes, persistence across detach and restart, saved SSH machines, and a CLI and socket API that lets agents drive each other.

**Its bet is that the missing orchestration layer sits beneath the harnesses, not above them: one daemon owns the terminals, so detachment, reboot recovery, remote machines, and agent-to-agent prompting become properties of the runtime instead of features every dashboard in this category reimplements.**

## What it is

A tmux-lineage multiplexer rebuilt for agents: workspaces, tabs, and panes where every agent pane is marked working, blocked, or idle, and the daemon keeps everything running when you close the client or lose SSH, then restores the saved layout on reattach or restart.
Agents drive it through `herdr agent start`, `agent prompt --wait`, `agent wait`, and `agent read` over 24 supported agent kinds (Claude Code, Codex, OpenCode, Gemini, Cursor, Devin, Amp, Grok, Kimi, Kilo, Pi, and more), so a script or one agent can spawn panes, prompt other agents, and wait until another agent is genuinely blocked, with alternate-screen transcript reads for full-screen harnesses.
One Rust binary, no Electron, with a plugin marketplace the YC announcement credits at more than 500 plugins one month after launch.
It is made by Can Celik, who built it solo, joined Y Combinator's F26 batch in August 2026, and raised a $6M seed led by Bessemer Venture Partners in September 2026; the runtime switched from AGPL to Apache-2.0 at the YC announcement.

## Status

Active and heavily adopted: 43,703 stars and 3,447 forks as of 2026-10-13 on a repository created 2026-03-27 under the herdrdev org after public life as ogulcancelik/herdr, pushed the day of this check.
Latest stable release v0.9.3 (2026-09-29) with a daily preview train.
The Hacker News footprint is the category's largest: a 404-point, 178-comment thread in July 2026, a 281-point YC announcement thread in August, and a 166-point launch thread in June.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=herdrdev/herdr&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=herdrdev/herdr&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=herdrdev/herdr&type=date&legend=top-left" />
</picture>

**The persistence story needs the docs' own precision: a detach keeps every process alive, but a server restart does not, and what returns is the saved layout plus resumed agent conversations for the 18 CLIs with native session restore, which is a different promise than the one the marketing implies.**

## Strengths

- The automation API is the deepest in this category: agent start, prompt with waits, lifecycle states (working, blocked, done, idle), send-keys into an agent's UI, and reads that page an alternate-screen transcript, all over CLI or socket.
- Native session restore covers 18 CLIs with documented exact resume commands, from `claude --resume <id>` to `pi --session <id>`, so a rebooted machine comes back with conversations intact.
- Multi-machine in one window: saved SSH machines with independent reconnects, and `herdr --remote user@host` installs the server on the host by itself.
- Distribution and momentum: Homebrew, mise, and install-script paths, a daily preview train, YC F26 backing, and the seed round to hire a team.

## Cautions

- "Sessions survive reboot" oversells: the docs are explicit that original processes do not survive a restart, layout returns, and only supported agent conversations resume; live handoff of running processes across server replacement is experimental and opt-in.
- Pane screen history replay is off by default because pane output can contain secrets and tokens, and the docs tell you to treat the session directory like terminal history.
- The category's oldest objection applies: the top summary of the 404-point thread is that this is tmux with agent status and nicer defaults, and commenters running zmx or Orca saw no reason to switch.
- A solo-founder project becoming a company mid-flight: the marketplace's 500-plus third-party plugins are a trust surface the core does not vet.

## Pricing

Free and open source under Apache-2.0, with the founder's public pledge at the YC announcement that the runtime stays free.
No paid tier as of 2026-10-10; the company is seed-funded and hiring, with no published paid plans.

## Compared to

- [cmux](../cmux/index.md): the other agent-first terminal, macOS-only and built around attention routing; choose cmux on a Mac for notification rings, herdr for cross-platform daemons, SSH machines, and the automation API.
- [hcom](../hcom/index.md): pure message fabric over the terminals you already run, herdr included; choose hcom to keep your multiplexer, herdr to replace it.
- [Conductor](../conductor/index.md): the macOS session manager whose product is the diff review flow; choose Conductor for PR ergonomics, herdr when terminal-native scale and remote machines matter more.

## Bottom line

**Recommended for terminal-first engineers running many agents across local and SSH machines who want agents to automate each other rather than click through another dashboard.**
Not for review-centric workflows, where no diff or PR surface exists, or for Windows users outside the beta.
My disagreeable claim: **herdr is the first column in this category whose product is the layer under the agents rather than a client above them, and if the runtime bet pays off, half the dashboards in the matrix become its plugins rather than its competitors.**

## Changes

- 2026-10-10 - Created from the orchestration category's entrant resolution, where the scanner recommended admission as a differentiated mechanism past the mission-control family.

## See also

- [cmux](../cmux/index.md) - the other agent-first terminal, and the closest existing column
- [hcom](../hcom/index.md) - the messaging fabric that already treats herdr as a pane-aware terminal
- [Omnara](../omnara/index.md) - the control plane that owns execution and state instead of the terminal
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this category extends

## References

- https://api.github.com/repos/herdrdev/herdr - stars, forks, Apache-2.0 license, creation and push dates, and topics, as of 2026-10-10
- https://raw.githubusercontent.com/herdrdev/herdr/master/README.md - the runtime positioning, persistence summary, agent-native claims, and install surfaces
- https://api.github.com/repos/herdrdev/herdr/releases?per_page=5 - v0.9.3 (2026-09-29), v0.9.2, and the daily preview train
- https://herdr.dev/docs/session-state/ - what survives detach, restart, update, and handoff, plus the 18-CLI native session restore table
- https://herdr.dev/docs/agent-automation/ - the automation primitives, the 24 supported agent kinds, and the lifecycle states
- https://herdr.dev/blog/herdr-is-joining-y-combinator/ - the solo-founder story, YC F26, the AGPL-to-Apache switch, 25k stars and 340k downloads at announcement, and the 500-plus plugin count
- https://herdr.dev/blog/herdr-raised-a-seed/ - the $6M seed led by Bessemer with Y Combinator, e2vc, and the angel list
- https://hn.algolia.com/api/v1/search?query=herdr&tags=story&hitsPerPage=10 - the HN footprint, queried 2026-10-10
- https://news.ycombinator.com/item?id=48756578 - the 404-point thread, the "exactly like tmux" critique, and the zmx counterpoint
