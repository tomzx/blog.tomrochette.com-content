---
title: Happy Coder
created: 2026-09-06
updated: 2026-09-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, mobile, claude-code, codex]
readability: 3
audience_notes: >
  Engineers who run Claude Code or Codex and want to start and supervise sessions from their phone.
  Assumes you know what a coding-agent harness is and what an encrypted relay does; no mobile development knowledge assumed.
---

Happy Coder is an MIT-licensed open-source client that wraps Claude Code and Codex sessions on your machine and syncs them end-to-end encrypted to native iOS, Android, macOS, and web apps.
**It out-stars every tool in the orchestration category while staying a thin wrapper around two harnesses, which says the phone screen, not the orchestrator, is what people install.**
Facts below verified as of 2026-09-06.

## What it is

The `happy` npm package replaces the plain `claude` or `codex` command, so agents run locally with your existing subscriptions and credentials while the session mirrors to the remote clients.
The monorepo under the slopus GitHub organization ships the CLI, an encrypted sync server, and a remote-control agent CLI, all under MIT.
Native apps exist for iOS, Android, macOS, and the web, with realtime voice and end-to-end encryption between your machine and every client.
The README describes the makers as a community of engineers building for themselves, not a funded company.

## Status

Active and the category's traction leader: 23,657 GitHub stars as of 2026-09-06, created July 2025, last pushed the day of verification.
The latest CLI release, cli-1.2.3, shipped 2026-09-05.
Its August 2025 Show HN drew only 30 points, so the star count is bottom-up adoption rather than press traction.
For scale, Paseo, the category's other mobile-first entrant, reports 16.2k stars against Happy's 23.7k.

## Strengths

- Installs as a drop-in: `npm install -g happy`, then run `happy claude` or `happy codex` instead of the plain command.
- End-to-end encryption with a self-hostable relay server (the happy-server package), so nobody in between can read your sessions.
- Native iOS and Android apps with realtime voice, the exact surface mobile-first users ask for.
- Wrapping the official CLIs keeps provider subscriptions and terms of service intact.

## Cautions

- Two harnesses only, Claude Code and Codex, against Paseo's four native plus roughly thirty-six via ACP.
- No worktree lifecycle: an agent starts in a path you pick, and creating or managing worktrees stays on you.
- The desktop app is macOS only and lives in a separate 72-star repo, so the mobile apps carry the product.
- The iOS in-app purchase labeled "Plus Plus Monthly" at $19.99 is a donation, which confused early users enough to surface in the launch thread.
- Sustainability rests on a self-described community team with no funding announced.

## Pricing

Free and open source under MIT, with no paid tier.
The mobile in-app purchase is a donation, not a feature gate, and the sync server is self-hostable.

## Compared to

Paseo is the direct rival and the bigger system: a daemon that owns agent lifecycle, four native harnesses plus an ACP catalog, managed worktrees, and plugins, where Happy is a two-harness session mirror with a comparable encryption story.
Omnara is the other phone-first option, but it is a control plane that owns execution and state, while Happy deliberately owns neither.
Conductor is the closed macOS session manager for people who want polish and accept lock-in.

## Bottom line

Recommended for Claude Code or Codex users who want their existing sessions on a phone, encrypted, with self-hosting as an option.
Not for multi-provider orchestration, worktree isolation, or Windows and Linux desktops; pick Paseo, Omnara, or Conductor instead.

## See also

- [Paseo](../paseo/index.md) - the daemon-based rival that actually contests the mobile slot
- [Omnara](../omnara/index.md) - the control-plane take on phone-first supervision
- [Conductor](../conductor/index.md) - the closed macOS session manager
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - where this note's column lives
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map that places mobile clients in the stack

## References

- https://github.com/slopus/happy - repository, 23,657 stars, MIT license, monorepo components, team description (GitHub API, 2026-09-06)
- https://happy.engineering/ - official site and product framing
- https://github.com/slopus/happy/releases - cli-1.2.3 published 2026-09-05 (GitHub API)
- https://news.ycombinator.com/item?id=44904039 - August 2025 Show HN, 30 points, the donation-IAP question and Windows sync bugs (Algolia-verified)
- https://news.ycombinator.com/item?id=46994716 - February 2026 Show HN for the happy.engineering launch (Algolia-verified)
- https://paseo.sh/alternatives/happy-coder - independent comparison grounding the architecture, provider, and worktree-limit claims
