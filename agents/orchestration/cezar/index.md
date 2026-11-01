---
title: Cezar
created: 2026-11-01
updated: 2026-11-01
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, worktree, vps, review-gate]
readability: 3
audience_notes: >
  Engineers who want coding agents working around the clock on a VPS, with worktree discipline and a review gate before anything lands.
  Assumes you know what Claude Code, Codex, and git worktrees are.
---

Cezar is an MIT control center that runs Claude Code, Codex, OpenCode, Pi, and other coding agents around the clock on your machine or a VPS, steered from a responsive web cockpit.

**The bet is that agents should keep working while you are away, and that worktree discipline, race-and-pick parallelism, and a review gate are what make unattended runs trustworthy.**

## What it is

A Node 20+ app installed from npm (`@open-mercato/cezar`) or a desktop-app track, using your existing CLI logins rather than API keys (claude, codex, copilot, cursor, agy, junie, opencode, pi).
Every task runs in its own full checkout, with a bounded worktree disk (retention default ten, per-row delete, a reclaim button) so a busy server stays clean.
Parallel agents can race the same task in separate worktrees: you compare diffs side by side and pick one, and the losers are archived with their worktrees cleaned up.
A finished run with changes waits at a review gate: read the diff, then push a draft PR; the cockpit carries a live event stream of agent text, tool calls, and screenshots, per-step token and cost usage, and scheduled starts keyed to a date, a time, or the account's observed usage-limit reset.
A GitHub panel reads issues and pull requests through your logged-in `gh` and hands an issue straight to an agent, GitHub Enterprise included; point a browser (laptop or phone) at the VPS and the team keeps working.
By open-mercato, the OpenMercato ERP team, repository created 2026-05-19.

## Status

Active: 904 stars, 169 forks, and 265 open issues and pull requests as of 2026-11-01 (GitHub API), pushed 2026-11-01, with 30 releases through v0.18.0 on 2026-10-31 plus a desktop track (desktop-v0.1.11, 2026-10-23).
The npm package shows 1,544 published versions since July 2026 (near-daily publishes) and 95,851 downloads in October 2026.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=open-mercato/cezar&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=open-mercato/cezar&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=open-mercato/cezar&type=date&legend=top-left" />
</picture>

Coverage is a launch echo: one 15-point Hacker News story (2026-10-01) and two small echo posts, then nothing, so the footprint is the repository, the npm numbers, and the cezar.run site.

## Strengths

- **The worktree lifecycle is the most complete in the category: bounded disk with retention, race-and-pick parallelism, and loser cleanup are all built in.**
- Usage-window-aware scheduled starts (waiting for the plan's limit reset) turn quota into a scheduling input no other member reads.
- The cockpit's event stream, cost accounting, and phone-first review make long unattended runs inspectable from anywhere.

## Cautions

- Coverage beyond the launch echo is absent as of 2026-11-01; adoption evidence is npm downloads, which a young project can inflate with CI publishes (1,544 versions since July).
- The vendor's cloud sandbox upsell sits beside the free product, and its price table is not public.
- Young (created May 2026) and pre-1.0, backed by an ERP vendor rather than an agent-tools specialist.

## Pricing

Free and open source under MIT, self-hosted.
The vendor sells hosted cloud sandboxes for 24/7 coding ("start for free"), with no public price table found as of 2026-11-01.

## Compared to

- [Omnara](../omnara/index.md): the YC control plane supervising agents from dashboard, phone, CLI, and Slack; Cezar adds the worktree lifecycle and race-and-pick execution.
- [Paseo](../paseo/index.md): the daemon with desktop, web, and mobile clients; Cezar is the VPS-always-on counterpart with review gates.
- [Emdash](../emdash/index.md): the desktop ADE for parallel worktree tasks; Cezar moves the same pattern to a browser-driven server.

## Bottom line

**Recommended for engineers who want an always-on agent box on a VPS with genuine worktree hygiene and a human review gate.**
Not for GUI-desktop-first users, and not for teams needing a hosted control plane with published pricing.

## Changes

- 2026-11-01 - Created.

## See also

- [Omnara](../omnara/index.md) - the control-plane sibling with phone supervision
- [Paseo](../paseo/index.md) - the daemon-plus-clients contrast
- [Emdash](../emdash/index.md) - the desktop ADE this moves server-side
- [Vibe Kanban](../vibe-kanban/index.md) - the board-first alternative without the worktree lifecycle

## References

- https://api.github.com/repos/open-mercato/cezar - stars, license, and activity as of 2026-11-01
- https://raw.githubusercontent.com/open-mercato/cezar/HEAD/README.md - the control-center model, supported CLIs, and install paths
- https://raw.githubusercontent.com/open-mercato/cezar/HEAD/docs/reference.md - the worktree lifecycle, review gate, races, cockpit, and GitHub panel
- https://api.github.com/repos/open-mercato/cezar/releases?per_page=100 - the 30-release train through v0.18.0 (2026-10-31)
- https://registry.npmjs.org/@open-mercato/cezar - the npm package, 1,544 versions since July 2026
- https://api.npmjs.org/downloads/point/2026-10-01:2026-10-31/@open-mercato/cezar - October 2026 downloads (95,851)
- https://cezar.run/ - the product site
- https://hn.algolia.com/api/v1/search?query=cezar.run&hitsPerPage=5 - the launch-echo coverage (15 points, 2026-10-01)
