---
title: herdr
created: 2026-10-10
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.4, llm=glm-5.3-flash, orchestration, terminal-multiplexer, rust, agent-automation, session-persistence]
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

Active and heavily adopted: 44,094 stars and 3,485 forks as of 2026-10-15 on a repository created 2026-03-27 under the herdrdev org after public life as ogulcancelik/herdr, with the default branch's latest commit on 2026-10-29 (GitHub API, as of 2026-11-08; the repository-level pushes on 2026-11-03 and 2026-11-07 landed on side branches).
Latest stable release v0.9.5 (2026-10-14) with a daily preview train.
The ecosystem around it is small but real: the vendor's separate engine repository herdr-core ("terminals for coding agents", 193 stars as of 2026-10-31, Apache-2.0) carries the runtime beside the main repo, and herduck, a 10-star terminal app self-describing as derived from Herdr, appeared 2026-10-29 as the first third-party port attempt.
The record above stops at the TUI repository, and the product has since become two: the Herdr TUI (this note's subject, its releases ending at v0.9.5 of 2026-10-14 with the default branch's latest commit on 2026-11-19) and the Herdr desktop app, a separate program built on the herdr-core runtime (`hc`) that shares no agents with the TUI (herdr.dev, fetched 2026-11-27).
The app's changelog runs 0.1.12 (2026-11-02, agents on macOS running fully apart from the app), 0.1.16 (2026-11-14, a warning when a remote Linux machine would stop agents on disconnect, needing herdr-core 0.1.21), 0.1.17 (2026-11-22), and 0.1.18 (2026-11-24, closing a tab no longer ending agents started with `--outlive-parent`), with SSH machines, Tailscale included, joined through `hc machine add` and their agents kept running while the laptop sleeps; herdrdev/herdr-app shows 3,567 stars as of 2026-11-27 and herdr-core was pushed 2026-11-26 (GitHub API).
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

- Sheprd (sheprd-labs/sheprd, 2,385 stars and 219 forks as of 2026-11-27, Apache-2.0, created 2026-09-20): an unaffiliated native Rust and GPUI desktop client that runs Herdr 1, Herdr 2 (herdr-core), or tmux beneath workspaces, worktrees, review, and SSH and cloud machines on macOS, Linux, and Windows; choose it when you want herdr's daemon under a desktop app instead of a terminal client, with zero independent coverage recorded so far.

## Bottom line

**Recommended for terminal-first engineers running many agents across local and SSH machines who want agents to automate each other rather than click through another dashboard.**
Not for review-centric workflows, where no diff or PR surface exists, or for Windows users outside the beta.
My disagreeable claim: **herdr is the first column in this category whose product is the layer under the agents rather than a client above them, and if the runtime bet pays off, half the dashboards in the matrix become its plugins rather than its competitors.**

## Changes

- 2026-10-10 - Created from the orchestration category's entrant resolution, where the scanner recommended admission as a differentiated mechanism past the mission-control family.
- 2026-10-27 - Re-verified in rotation: all cited sources re-fetched and live (repo API, README, releases, both docs pages, both blog posts, HN); the push date refreshed to 2026-10-26, v0.9.5 still the latest stable with the daily preview train running.
- 2026-10-31 - Recorded the ecosystem pair from the broad-source scan: the vendor's herdr-core engine repository (193 stars as of 2026-10-31) and the derived 10-star herduck terminal app.
- 2026-11-04 - Status refresh: the default-branch record corrected (latest commit 2026-10-29, the 2026-11-03 repository push side-branch only) per the pushed-at divergence rule; v0.9.5 still the latest stable.
- 2026-11-12 - Rotation re-verification (every cited URL re-fetched live: repo API, README, releases, both docs pages, both blog posts, HN search, herdr-core, herduck); no factual drift, the default branch's latest commit still 2026-10-29 with later repository pushes on side branches, v0.9.5 still the latest stable.
- 2026-11-19 - Rotation re-verification: every cited URL re-fetched live (repo API, README, releases, both docs pages, both blog posts, the HN search and thread, herdr-core, herduck); no drift, v0.9.5 (2026-10-14) still the latest release and the default branch quiet since 2026-10-29.
- 2026-11-27 - Recorded the two-product split the note was missing (the Herdr desktop app on herdr-core, its changelog at 0.1.18 of 2026-11-24 with agents outliving the app since 0.1.12 and remote machines through `hc machine add`; herdr-app at 3,567 stars as of 2026-11-27) beside the TUI's v0.9.5 release record, and folded Sheprd (sheprd-labs/sheprd, 2,385 stars as of 2026-11-27), the unaffiliated Rust and GPUI desktop client, into Compared to on the derivatives-and-clients ruling.

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
- https://github.com/herdrdev/herdr-core - the vendor's engine repository beside the main repo
- https://github.com/wenhanweime/herduck - the derived third-party terminal app
- https://api.github.com/repos/herdrdev/herdr-app - the vendor's desktop app repository, description and push date, as of 2026-11-27
- https://api.github.com/repos/herdrdev/herdr-core - the engine repository's push date, as of 2026-11-27
- https://github.com/herdrdev/herdr-app/blob/master/CHANGELOG.md - the desktop app's changelog: 0.1.12 (2026-11-02) through 0.1.18 (2026-11-24), fetched 2026-11-27
- https://herdr.dev/core/ - the herdr-core runtime page: terminals that outlive the window, agents starting agents, and every machine over SSH, fetched 2026-11-27
- https://herdr.dev/ - the homepage naming the TUI and the desktop app as separate programs that share no agents, fetched 2026-11-27
- https://github.com/sheprd-labs/sheprd - the unaffiliated desktop client: backends, platforms, and the unaffiliated notice, as of 2026-11-27
- https://news.ycombinator.com/item?id=48756578 - the 404-point thread, the "exactly like tmux" critique, and the zmx counterpoint
