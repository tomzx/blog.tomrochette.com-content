---
title: cmux
created: 2026-08-24
updated: 2026-09-20
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, orchestration, terminal, parallel-agents, macos]
readability: 3
audience_notes: >
  macOS engineers running several CLI coding agents who lose track of which terminal needs attention.
  Assumes you know what a terminal multiplexer is and what GPL-3.0 implies for your employer.
---

cmux is Manaflow's open-source macOS terminal built on libghostty for running many coding agents in parallel, with vertical tabs, workspaces, notification rings, and an open-core cloud tier.
Facts below verified as of 2026-09-24.

**cmux's real product is attention routing, not multiplexing, and its real business is cloud execution: the terminal is the free, GPL-3.0 funnel, and the subscription is where the company actually lives.**

## What it is

**A native macOS terminal (built on libghostty, not an Electron app and not a Ghostty fork) whose features target the many-agents-at-once workflow**: vertical and horizontal tabs, workspaces, split panes, notification rings around panes that need you, a notification panel that jumps to the most recent unread agent, and an in-app browser with a scriptable API ported from agent-browser.
It is programmable through a socket API and a `cmux notify` CLI, ships local session history, and runs Claude Code, Codex, Gemini, and any CLI agent on your own keys.
A paid subscription (Pro or Max) adds Cloud VM agents and the iOS app; the CodeRouter pitch that was on the pricing page in August has since disappeared from it.

## Status

**Active and remarkably fast.**
About 27.3k stars and 2.4k forks as of 2026-09-22, created January 28, 2026, with commits landing the day of verification.
The launch thread counted 18 releases in two days; the project is at v0.64.x (v0.64.25 on 2026-09-17) with a nightly channel.
Three contributors dominate the history (about 5.2k, 3.8k, and 1.2k contributions), so this is a small funded team (Manaflow, Inc.) moving very quickly, not a broad community.

## Strengths

- **Notification rings and the unread panel solve the actual pain of parallel agents**, knowing which terminal is waiting for you, better than any tmux setup.
- libghostty makes it a real native terminal with real performance, and the maintainer is responsive (launch-thread bugs fixed within releases).
- The scriptable socket API and notify CLI mean agents themselves can drive it, and third parties already teach Claude Code to do exactly that.
- The free tier is the full terminal: every CLI agent, BYOK, notifications, browser panels, no metering.

## Cautions

- **macOS only**, and the client is GPL-3.0-or-later (which GitHub labels "Other"), so copyleft-policy teams should check before adoption.
- Open-core: cloud execution sits behind Pro at $50/month (with a $200/month Max tier for bigger VMs), so the roadmap's center of gravity is the subscription, not the terminal.
- The pace is a risk profile: 0.x versions, a nightly channel, and a launch-era bug list mean churn.
- An August 2026 thread reports whole-app freezes of 2-10 seconds with SSH sessions open, so remote-heavy workflows should test first.
- **Name collisions are everywhere**: craigsc/cmux ("tmux for Claude Code", MIT, about 604 stars), a separate October 2025 Show HN "Cmux, Coding Agent Multiplexer" GUI, and an unrelated Go connection multiplexer; search carefully before citing.

## Pricing

Free $0: the full terminal, any CLI agent BYOK, notifications, browser panels, socket API, local history.
Pro $50/month: cloud agents on isolated VMs, capped at up to 50 Cloud VMs per user with 24 GB RAM and 6 vCPUs shared across all of them, plus unlimited workspaces, the iOS app, and email support; as of 2026-09-22 the page bills monthly only (the tiers verified unchanged from 2026-09-18), with the $40 billed-yearly rate it showed on 2026-09-16 gone (the shared-pool phrasing dates to 2026-09-10, after the per-VM resources with a 256 GB disk ceiling it showed on 2026-09-09, and different shared-pool totals through 2026-09-05).
Max $200/month adds up to 64 GB RAM per machine (32 or 64 GB Cloud VMs on 16 vCPUs), where Free, Pro, and Team machines top out at 24 GB.
Team $60/user/month adds centralized billing and priority support; Enterprise adds self-hosted, even air-gapped, cloud execution, SSO/SAML, audit logs, and SOC 2, as of 2026-09-22.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-05 | Pro | Shared-pool cloud VM resources, with totals differing from later descriptions. | [cmux.com/pricing](https://cmux.com/pricing) |
| 2026-09-09 | Pro | Listed per-VM resources with a 256 GB disk ceiling. | [cmux.com/pricing](https://cmux.com/pricing) |
| 2026-09-10 | Pro | Returned to shared-pool phrasing (up to 50 VMs sharing 24 GB RAM and 6 vCPUs). | [cmux.com/pricing](https://cmux.com/pricing) |
| 2026-09-16 | Pro | Priced $50/mo, or $40 billed yearly. | [cmux.com/pricing](https://cmux.com/pricing) |
| 2026-09-18 | All tiers | Yearly rate removed: Pro $50/mo monthly only; Max $200/mo adds 32 or 64 GB machines on 16 vCPUs; Team $60/user/mo; Free $0. | [cmux.com/pricing](https://cmux.com/pricing) |

## Compared to

- [dmux](../dmux/index.md): tmux-based and cross-platform; pick dmux off macOS, cmux for notifications.
- [Claude Squad](../claude-squad/index.md): free AGPL tmux manager; lighter, rougher, no cloud ambitions.
- [Vibe Kanban](../vibe-kanban/index.md): kanban abstraction over agents versus staying in the terminal metaphor.

## Bottom line

**Recommended for macOS engineers whose bottleneck is attention across many CLI agent sessions and who want that solved in a real terminal.**
Not for Linux or Windows users, copyleft-restricted shops, or anyone who needs a stable 1.0 interface.

## Changes

- 2026-08-24 - Created in the Orchestration category after an owner request, covering manaflow-ai/cmux and disambiguating two same-named products.
- 2026-09-02 - Pricing packaging changed, CodeRouter removed and unlimited active cloud VMs added.
- 2026-09-04 - Cloud VM disk cap cut from 200GB to 32GB.
- 2026-09-05 - Pricing restructured again to a shared pool (5 vCPU, 20 GB, 200 GB) with VMs starting at 8 GB/32 GB.
- 2026-09-06 - Pricing page dropped the shared-pool cloud spec for per-VM resources with a 256 GB disk ceiling.
- 2026-09-10 - Pricing page reverted to shared-pool phrasing (24 GB RAM, 6 vCPU shared).
- 2026-09-18 - Pricing page moved to monthly-only billing and added a $200/month Max tier with up to 64 GB RAM per Cloud VM.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the orchestration layer this note belongs to
- [Managing Many Concurrent LLM Agent Sessions](../../../managing-many-llm-agent-sessions/index.md) - the supervision problem the notification panel exists for
- [dmux](../dmux/index.md) - the terminal-native cross-platform alternative
- [Claude Squad](../claude-squad/index.md) - the free minimal neighbor

## References

- https://github.com/manaflow-ai/cmux - source, license statement, repository scale, as of 2026-09-22
- https://cmux.com/pricing - tiers, the Max tier, shared-pool cloud VM specs and their churn, CodeRouter removal, verified unchanged on 2026-09-22
- https://cmux.com/blog/zen-of-cmux - the project's own design philosophy
- https://news.ycombinator.com/item?id=47079718 - the February 2026 launch thread with author Q&A
- https://www.bounds.dev/posts/teaching-claude-code-to-drive-cmux/ - third-party account of agents driving cmux programmatically
- https://news.ycombinator.com/item?id=49285938 - the August 2026 SSH freeze report
- https://github.com/craigsc/cmux - the other cmux, for disambiguation
