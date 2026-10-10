---
title: Agent Orchestrator
created: 2026-10-06
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, kanban, worktrees, multi-harness, desktop]
readability: 3
audience_notes: >
  Engineers shortlisting a free, open, cross-platform kanban workspace that supervises many coding CLIs from one desktop.
  Assumes you run at least one CLI coding agent and know what a git worktree is.
---

**Agent Orchestrator (AO) is the category's quiet volume leader: a free, Apache-2.0 desktop kanban workspace that supervises 26-plus coding CLIs from one daemon, and it reached 12.8k stars on a 15-point launch thread.**

## What it is

AO is a local desktop workspace (macOS Apple silicon and Intel, Windows, Linux AppImage/deb/rpm) built on a Go backend daemon with an Electron frontend and a SQLite change-data-capture layer that streams session state to the UI.
A worker is its unit of execution: one task, one coding agent, and one isolated workspace with its own branch and git worktree, with the conversation, terminal, changed files, browser preview, pull request, CI state, and review state attached to that session from start to finish.
A project-aware orchestrator plans and delegates larger outcomes, a live kanban groups workers by status, and CI or review feedback routes back to the same worker instead of a new session.
It drives Claude Code, Codex, and 25 more CLIs per the repo description (23 counted in Starlog's July review), runs web and mobile access plus account-gated cloud agent sessions, and ships under the Apache-2.0 license.

## Status

Active and shipping daily: 12,970 stars, 1,770 forks, 765 open issues and pull requests, and 30 contributors as of 2026-10-09, created 2026-02-13 (GitHub API, as of 2026-10-09).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=OrchestratorInc/agent-orchestrator&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=OrchestratorInc/agent-orchestrator&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=OrchestratorInc/agent-orchestrator&type=date&legend=top-left" />
</picture>

The stable line sits at v0.13.5 (2026-10-08), promoted from the nightly train after v0.13.4 (2026-10-07), with nightlies publishing most days (GitHub releases API).
**The identity record is the caution: the repository has lived under four organizations in eight months (ComposioHQ, AgentWrapper, Untrivial-ai, and now OrchestratorInc), each old URL a 301 today, which is the same rename churn this section flagged on Ruflo but repeated.**
The community footprint is thin for the star count: the Show HN launch drew only 15 points on 2026-03-29 (a text post with no external link, HN Algolia), so the 12.8k stars spread through GitHub, X, and Discord rather than press, and the only third-party coverage I found is a competitor's roundup (Tembo, June 2026) and one technical review (Starlog, July 2026, at 8.6k stars).

## Strengths

- Free and open source (Apache-2.0) across all three desktop OSes, with the daemon watching agent and git state so the kanban stays live.
- Per-worker branch and worktree isolation with PR, CI, and review state carried on the session and fed back to the same agent.
- Broad harness coverage (26+ CLIs) without waiting on the orchestrator to reimplement harness features.

## Cautions

- Four organization renames in eight months (ComposioHQ to AgentWrapper to Untrivial-ai to OrchestratorInc) make every badge, mirror, and historical reference a moving target.
- A 15-point launch thread, no field reports, and a self-issued "Top 6k repositories" badge, so the 12.8k stars are uncorroborated by independent discussion.
- Cloud agent sessions sit behind account access with no public price page (the docs pricing path 404s), and the repo's "pricing catalog" is a LiteLLM-derived model-price list for display, not product pricing.

## Pricing

Free and open source under Apache-2.0.
Cloud agent sessions exist behind account access, and no public price page exists as of 2026-10-06.

## Compared to

- [Multica](../multica/index.md): the board rival that casts agents as teammates; Multica carries a custom license and a caveated star count, AO carries Apache-2.0 and an uncorroborated one.
- [Orca](../orca/index.md): the bigger, better-funded ADE at 86k stars; choose Orca for polish and mobile depth, AO for the kanban-plus-review-loop design on a plain Apache-2.0.
- [Vibe Kanban](../vibe-kanban/index.md): the kanban design AO extends, now vendor-less; Vibe Kanban is the caution, AO the live iteration.

## Bottom line

Recommended for engineers who want a free, open, cross-desktop kanban that supervises many harnesses and routes CI and review feedback back into the same worker.
Not for anyone who needs a stable identity to standardize on (four renames and counting), vendor support, or independently corroborated adoption.

## Changes

- 2026-10-06 - Created after the entrant scan surfaced the OrchestratorInc repository at 12.8k stars with no note in the section.
- 2026-10-07 - Added the OrchestratorInc/agent-orchestrator star history chart to the Status section.
- 2026-10-08 - Recorded v0.13.4 promoted from the nightly train to the stable line (October 7) and 12.9k stars as of 2026-10-08.
- 2026-10-09 - Recorded v0.13.5 (October 8) as the stable release and refreshed the star count to 12,970 as of 2026-10-09.

## See also

- [Multica](../multica/index.md) - the other high-star board-style workspace, with the license caveat AO avoids
- [Orca](../orca/index.md) - the scale leader of the desktop ADE family AO competes with
- [Vibe Kanban](../vibe-kanban/index.md) - the kanban-for-agents design and its vendor-loss record
- [Conductor](../conductor/index.md) - the funded, closed Mac session manager at the polished end of the genre

## References

- https://github.com/OrchestratorInc/agent-orchestrator - repository, description, harness count, license, and stars (GitHub API, as of 2026-10-06)
- https://docs.orchestrator.inc/ - documentation index, daemon install model, and platform list
- https://docs.orchestrator.inc/guides/cloud - cloud sessions behind account access
- https://starlog.is/articles/ai-agents/untrivial-ai-agent-orchestrator - the July 2026 technical review grounding the architecture cells (SQLite CDC, Electron, worktree per agent)
- https://www.tembo.io/blog/ai-agent-orchestration-tools - the June 2026 roundup tracking it as Composio's coding-native open-source orchestrator
- https://news.ycombinator.com/item?id=47562440 - the 15-point Show HN launch (2026-03-29) grounding the community-footprint claim
- https://github.com/ComposioHQ/agent-orchestrator - the 301 redirect that grounds the rename chain
