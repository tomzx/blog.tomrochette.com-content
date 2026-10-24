---
title: Waku
created: 2026-10-23
updated: 2026-10-23
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surfaces, desktop, open-source, multi-agent]
readability: 3
audience_notes: >
  Engineers who run several agent CLIs and want one native desktop window over them,
  profiled against bb, CodeNomad, and the other local session cockpits in this category.
  Assumes you know what Claude Code or OpenCode is and what BYOK means.
---

Waku is a GPL-3.0 native desktop app, written in Rust on GPUI, that drives the coding-agent CLIs you already run (Amp, Claude Code, Codex CLI, Cursor CLI, Fx, Grok Build, Kimi Code, OpenCode, Pi) from one local window.

**Its bet is that the cockpit should be as native as the editor, not another Electron shell, and that one provider-neutral session model over each CLI's own structured protocol beats one app per agent.**

## What it is

A desktop application for macOS (a signed, auto-updating `.dmg` via Sparkle), Linux (an install script into `~/.local`, no root), and Windows (a per-user installer plus a portable `.zip`), with a browser client that talks to the same daemon.
Each agent connects over its strongest native interface, stream-json, JSON-RPC, or live events, normalized into one provider-neutral model, so sessions, transcripts, tool activity, and checkpoints land in one timeline.
The architecture splits the desktop (an RPC client) from a standalone `waku-daemon` that owns task SQLite data, provider session forks, and all workspace filesystem and Git operations; every prompt checkpoints your working tree under a hidden git ref, so a rewind restores the code and the provider conversation together.
It is built by EGOIST, a long-standing open-source author (13,600+ GitHub followers, 800+ repositories, the CEO of ChatWise), and the site jokes "Not backed by Y Combinator".

## Status

**Active and young.**
1,586 stars and 159 open issues as of 2026-10-23 (GitHub API), repository created 2026-07-31, last pushed 2026-10-02, with v0.1.20 (2026-10-02) as the latest release in a steady 0.1.x train.
The self-submitted Show HN ("I built a native app for coding agents with Rust and GPUI", August 15, 2026) drew 39 points and 17 comments, a modest footprint for a tool this polished.
Everything runs on your machine: no account, no telemetry, no Waku cloud, and the daemon stays loopback-only unless you deliberately expose it.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=egoist/waku&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=egoist/waku&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=egoist/waku&type=date&legend=top-left" />
</picture>

## Strengths

- **Native is a feature here, not marketing**: Rust and GPUI (the GPU framework behind Zed) buy instant launch and smooth scrolling through years of transcript, the exact complaint that motivated the author.
- One normalized timeline across nine agent CLIs, each connected over its own structured protocol with session continuity, is the widest multi-harness coverage in this category.
- Checkpoints that restore code and conversation together (a hidden git ref per prompt) are a more honest rewind than chat-log-only undo.
- Local by architecture: projects, sessions, transcripts, and provider IDs stay on your disk, with no account to create and no telemetry to opt out of.

## Cautions

- **The license is GPL-3.0**, not the MIT or Apache-2.0 most of this category ships, which matters if you fork it into something you distribute.
- It is a v0.1.x product from one primary author, with 159 open issues and Windows support explicitly partial ("what is not available there yet", per the docs).
- MCP and AGENTS.md handling are not documented anywhere in the README or site, so the harness-level conventions this section tracks are unverified.
- Name collision: Waku is also the 6.5k-star minimal React framework (wakujs/waku); searches for one find mostly the other.

## Pricing

Pricing does not apply: the app is free and GPL-3.0, with no hosted tier and no account.
The costs are the CLI subscriptions or API keys of whichever agents you drive through it.

## Compared to

- [bb](../bb/index.md): the other multi-CLI native desktop bet; bb is Apple-Silicon-forward and self-building, Waku ships native Windows and Linux builds today and leans on provider CLIs it does not modify.
- [CodeNomad](../codenomad/index.md): the one-harness commitment; CodeNomad goes deep on OpenCode with phone remote control, Waku goes wide across nine CLIs with no remote story beyond the local daemon.
- [cc-haha](../cc-haha/index.md): the single-vendor workbench; cc-haha wraps Claude Code's whole control plane, Waku treats every CLI as a swappable peer.

## Bottom line

**Recommended for engineers who live in multiple agent CLIs and want one fast, local, keyboard-first window over all of them.**
Not for teams that need remote access, mobile surfaces, or a vendor to call, and not for anyone who cannot accept GPL-3.0 in their toolchain.

## Changes

- 2026-10-23 - Created from the coordinator handoff (owner-star signal, 2026-07-31), admitted as a surfaces-kind fit: a native multi-CLI session cockpit in the bb and CodeNomad family, with the GPL-3.0 license and the React-framework name collision recorded as cautions.

## See also

- [bb](../bb/index.md) - the closest native multi-harness peer and its main comparison
- [CodeNomad](../codenomad/index.md) - the deep-one-harness alternative this note's width contrasts with
- [cc-haha](../cc-haha/index.md) - the single-vendor workbench at the other end of the breadth axis
- [Surface Feature Matrix](../surface-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/egoist/waku - repository facts: 1,586 stars, GPL-3.0, Rust, created 2026-07-31, pushed 2026-10-02, 159 open issues (GitHub API, as of 2026-10-23)
- https://raw.githubusercontent.com/egoist/waku/main/README.md - the supported-agent list, the daemon architecture, checkpoints under a hidden git ref, and the install paths (fetched 2026-10-23)
- https://waku.sh - the product site: the native pitch, GPUI, keyboard-first controls, local-by-architecture, and the "Not backed by Y Combinator" line (fetched 2026-10-23)
- https://api.github.com/repos/egoist/waku/releases/latest - v0.1.20 (2026-10-02) as the latest release (fetched 2026-10-23)
- https://hn.algolia.com/api/v1/items/49315709 - the August 15, 2026 Show HN (39 points): the author's Electron-frustration motivation and the skeptical "wrapper over the existing agents" thread (fetched 2026-10-23)
- https://api.github.com/users/egoist - the author record: 13,638 followers, 833 public repositories, CEO of ChatWise (fetched 2026-10-23)
- https://github.com/wakujs/waku - the React framework of the same name (6,474 stars) behind the disambiguation caution (GitHub API, as of 2026-10-23)
