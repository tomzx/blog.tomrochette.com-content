---
title: cmux
created: 2026-08-24
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, orchestration, terminal, parallel-agents, macos]
readability: 3
audience_notes: >
  macOS engineers running several CLI coding agents who lose track of which terminal needs attention.
  Assumes you know what a terminal multiplexer is and what GPL-3.0 implies for your employer.
---

cmux is Manaflow's open-source macOS terminal built on libghostty for running many coding agents in parallel, with vertical tabs, workspaces, notification rings, and an open-core cloud tier.
Facts below verified as of 2026-09-05.

**cmux's real product is attention routing, not multiplexing, and its real business is cloud execution: the terminal is the free, GPL-3.0 funnel, and the subscription is where the company actually lives.**

## What it is

**A native macOS terminal (built on libghostty, not an Electron app and not a Ghostty fork) whose features target the many-agents-at-once workflow**: vertical and horizontal tabs, workspaces, split panes, notification rings around panes that need you, a notification panel that jumps to the most recent unread agent, and an in-app browser with a scriptable API ported from agent-browser.
It is programmable through a socket API and a `cmux notify` CLI, ships local session history, and runs Claude Code, Codex, Gemini, and any CLI agent on your own keys.
A Pro subscription adds Cloud VM agents and the iOS app; the CodeRouter pitch that was on the pricing page in August has since disappeared from it.

## Status

**Active and remarkably fast.**
About 26.8k stars and 2.3k forks as of 2026-09-04, created January 28, 2026, with commits landing the day of verification.
The launch thread counted 18 releases in two days; the project is at v0.64.x with a nightly channel.
Three contributors dominate the history (about 5.2k, 3.8k, and 1.2k contributions), so this is a small funded team (Manaflow, Inc.) moving very quickly, not a broad community.

## Strengths

- **Notification rings and the unread panel solve the actual pain of parallel agents**, knowing which terminal is waiting for you, better than any tmux setup.
- libghostty makes it a real native terminal with real performance, and the maintainer is responsive (launch-thread bugs fixed within releases).
- The scriptable socket API and notify CLI mean agents themselves can drive it, and third parties already teach Claude Code to do exactly that.
- The free tier is the full terminal: every CLI agent, BYOK, notifications, browser panels, no metering.

## Cautions

- **macOS only**, and the client is GPL-3.0-or-later (which GitHub labels "Other"), so copyleft-policy teams should check before adoption.
- Open-core: cloud execution sits behind Pro at $40/month (billed yearly), so the roadmap's center of gravity is the subscription, not the terminal.
- The pace is a risk profile: 0.x versions, a nightly channel, and a launch-era bug list mean churn.
- An August 2026 thread reports whole-app freezes of 2-10 seconds with SSH sessions open, so remote-heavy workflows should test first.
- **Name collisions are everywhere**: craigsc/cmux ("tmux for Claude Code", MIT, about 601 stars), a separate October 2025 Show HN "Cmux, Coding Agent Multiplexer" GUI, and an unrelated Go connection multiplexer; search carefully before citing.

## Pricing

Free $0: the full terminal, any CLI agent BYOK, notifications, browser panels, socket API, local history.
Pro $40/month billed yearly ($50 month-to-month): cloud agents on isolated VMs, capped at up to 50 Cloud VMs per user sharing a pool of 5 vCPU, 20 GB RAM, and 200 GB disk total, each VM starting at 8 GB RAM and 32 GB disk, with sizes from 4 to 64 GB RAM available as capacity allows, as of 2026-09-05 (the page restored the 200 GB shared-pool total alongside the 32 GB per-VM default after showing 32 GB per VM with no pool total on 2026-09-04), plus unlimited workspaces, the iOS app, and email support.
Team $48/user/month billed yearly ($60 month-to-month) adds centralized billing and priority support; Enterprise adds self-hosted, even air-gapped, cloud execution, SSO/SAML, audit logs, and SOC 2, as of 2026-09-04.

## Compared to

- [dmux](../dmux/index.md): tmux-based and cross-platform; pick dmux off macOS, cmux for notifications.
- [Claude Squad](../claude-squad/index.md): free AGPL tmux manager; lighter, rougher, no cloud ambitions.
- [Vibe Kanban](../vibe-kanban/index.md): kanban abstraction over agents versus staying in the terminal metaphor.

## Bottom line

**Recommended for macOS engineers whose bottleneck is attention across many CLI agent sessions and who want that solved in a real terminal.**
Not for Linux or Windows users, copyleft-restricted shops, or anyone who needs a stable 1.0 interface.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the orchestration layer this note belongs to
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the supervision problem the notification panel exists for
- [dmux](../dmux/index.md) - the terminal-native cross-platform alternative
- [Claude Squad](../claude-squad/index.md) - the free minimal neighbor

## References

- https://github.com/manaflow-ai/cmux - source, license statement, repository scale, as of 2026-09-05
- https://cmux.com/pricing - tiers, cloud VM pool and disk specs, CodeRouter removal, as of 2026-09-05
- https://cmux.com/blog/zen-of-cmux - the project's own design philosophy
- https://news.ycombinator.com/item?id=47079718 - the February 2026 launch thread with author Q&A
- https://www.bounds.dev/posts/teaching-claude-code-to-drive-cmux/ - third-party account of agents driving cmux programmatically
- https://news.ycombinator.com/item?id=49285938 - the August 2026 SSH freeze report
- https://github.com/craigsc/cmux - the other cmux, for disambiguation
