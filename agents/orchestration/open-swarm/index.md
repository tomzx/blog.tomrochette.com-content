---
title: Open Swarm
created: 2026-09-27
updated: 2026-10-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, orchestration, mission-control, human-in-the-loop, worktrees]
readability: 3
audience_notes: >
  Engineers who want to launch and approve several agents from one local dashboard.
  Assumes you run Claude or plan to, and understand git worktrees and MCP servers.
---

Open Swarm was an AGPL-3.0, local-first mission-control desktop app for launching, monitoring, approving, and coordinating multiple AI coding agents in parallel on a spatial canvas.

**Open Swarm's bet was that the bottleneck is supervision, not spawning: it put every agent on one pan-and-zoom canvas, funneled every tool-use request into a single approval workflow, and kept the whole thing on your machine with no cloud relay or telemetry. The bet ended in October 2026, when the project pivoted into a proprietary company product and the open-source repository became a signed-builds shell.**

## What it is

A desktop app (Electron shell over a React frontend and a FastAPI backend on port 8324) from openswarm-ai that runs Claude-powered agents through the Claude Agent SDK.
The spatial dashboard is an infinite canvas of drag-and-drop agent cards, view cards, and embedded browser cards; agent chat streams over WebSockets with per-session cost tracking and persistent history.
Its differentiators are a unified human-in-the-loop approval workflow (per-tool permissions of always-allow, ask, or deny, with batch approval from the dashboard), message branching that forks a conversation by editing a prior message, prompt templates, a skills library that syncs to `~/.claude/skills/`, and an MCP tools library with registry browsing.
Each agent gets its own git worktree and branch, with a diff viewer for uncommitted changes, and there are five built-in agent modes plus custom modes, interactive HTML/JS/CSS output views, dark and light themes, and keyboard shortcuts.
It targeted macOS; Windows and Linux builds were documented as planned.

## Status

**Pivoted to proprietary: the open-source mission-control canvas documented here is no longer being developed.**
The repository now states that OpenSwarm "has moved in a new direction, and its development no longer happens here", holds only the signed builds that installed copies check for updates, and declares the software proprietary (README fetched 2026-10-12).
The git history was replaced: the repo carries a single commit dated 2026-10-03 ("releases shell"), where the note's earlier verifications recorded an active source tree, and GitHub's license detection moved from AGPL-3.0 to NOASSERTION.
A v1.8.0 stable build was published on 2026-10-11 as a signed artifact, after the experimental line (exp.2 through exp.6, September 23 to October 6) this note tracked.
The company behind the new direction, Open Swarm Inc., runs a waitlist-gated consumer assistant whose agents act on Gmail, Calendar, and Drive, with a privacy policy effective October 3, 2026 that covers advertising pixels, session recordings, and hashed-email ad measurement, the opposite of the no-telemetry positioning this note originally recorded.
The last open-source state documented below is the AGPL-3.0 experimental line, about 826 stars and 171 forks as of 2026-10-12 (repository created 2026-03-13).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=openswarm-ai/openswarm&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=openswarm-ai/openswarm&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=openswarm-ai/openswarm&type=date&legend=top-left" />
</picture>

**The signal across the note's whole life is a license story in three acts: a README MIT badge over an AGPL-3.0 file (September 2026), then a proprietary declaration with the source history replaced by a build shell (October 2026). The badge was the first piece of documentation not to trust, and the pivot was the second.**

## Strengths

- The unified approval workflow is the strongest part of the design: one place to approve or deny tool calls across every agent.
- Cost tracking per session and per agent, which the parallel-agent category mostly leaves to the provider dashboard.
- Git worktree isolation per agent plus a diff viewer, so parallel work is contained and reviewable locally.
- Skills, MCP tools, prompt templates, and message branching give it real depth beyond a chat multiplexer.
- Fully local by design: no cloud relay, no telemetry, and the backend can be run directly for self-hosting.

## Cautions

- **The project is proprietary and closed-source as of October 2026**: the repository holds signed builds only, the source history is gone, and the AGPL-3.0 era is frozen at the last open release.
- The "fully local, no telemetry" design described below belonged to the pre-pivot app; the successor product's privacy policy describes advertising pixels, session recordings, and hashed-email ad measurement (effective 2026-10-03).
- macOS only as of 2026-09-27; Windows and Linux were planned but not shipped before the pivot.
- Built on the Claude Agent SDK and Anthropic models; the pre-pivot app was effectively single-provider.
- The name collides with an unrelated `Intrect-io/OpenSwarm` Show HN project, which confuses search and comparisons.

## Pricing

The pre-pivot app was free and open source (AGPL-3.0, last open line at v1.8.0-exp.6).
The current signed builds are proprietary with no published price; the successor Open Swarm Inc. product is waitlist-gated with no pricing page as of 2026-10-12.

## Compared to

- [Lanes](../lanes/index.md): macOS board-first with real PTY sessions and an access-governance endpoint; the approval-centric canvas Open Swarm pioneered has no maintained open-source successor.
- [Conductor](../conductor/index.md): the polished closed Mac worktree dashboard; it stayed closed but stayed alive, which the pivot proves was the harder half.
- [OpenRig](../openrig/index.md): the Apache-2.0 local control plane with YAML-defined seats and approvals, the closest maintained open-source substitute for the pre-pivot workflow.

## Bottom line

**Not recommendable: the documented open-source canvas is frozen, the repository is a proprietary build shell, and the successor is a different product for a different audience.**
The note stays as the category's second pivot record, after Flowise's archive, and as the reason to read a project's license file before its README.

## Changes

- 2026-09-27 - Created.
- 2026-09-30 - Recorded the experimental release line advancing to v1.8.0-exp.4 (September 29) and refreshed star counts.
- 2026-10-02 - Recorded the experimental release line advancing to v1.8.0-exp.5 (October 2) and refreshed star and fork counts.
- 2026-10-07 - Added the openswarm-ai/openswarm star history chart to the Status section.
- 2026-10-09 - Recorded the experimental release line advancing to v1.8.0-exp.6 (October 6).
- 2026-10-12 - Recorded the pivot: the repository is now a proprietary signed-builds shell (single commit dated 2026-10-03, v1.8.0 build 2026-10-11), development moved to Open Swarm Inc.'s waitlist-gated consumer assistant with a 2026-10-03 privacy policy, and the Status, Cautions, Pricing, Compared to, and Bottom line sections were rewritten around the pivot.
- 2026-10-29 - Re-verified in rotation: every cited URL re-fetched and live; the pivot state is unchanged (proprietary signed-builds shell, single 2026-10-03 commit, v1.8.0 the last build), no factual drift.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Lanes](../lanes/index.md) - the board-first macOS workspace
- [Conductor](../conductor/index.md) - the closed Mac incumbent
- [Claude Squad](../claude-squad/index.md) - the free terminal alternative
- [OpenChamber](../../surfaces/openchamber/index.md) - the session-centric surface

## References

- https://github.com/openswarm-ai/openswarm - repository, architecture, features, stars, and the AGPL-3.0 LICENSE (as recorded through 2026-10-09)
- https://raw.githubusercontent.com/openswarm-ai/openswarm/HEAD/README.md - features, approval workflow, skills and MCP libraries, and the MIT badge (as recorded 2026-09-27)
- https://api.github.com/repos/openswarm-ai/openswarm - the pivot-state repository: 826 stars, NOASSERTION license detection, 2026-10-03 update date (fetched 2026-10-12)
- https://api.github.com/repos/openswarm-ai/openswarm/readme - the pivot README: "moved in a new direction", signed builds only, proprietary declaration (fetched 2026-10-12)
- https://api.github.com/repos/openswarm-ai/openswarm/commits - the single-commit history dated 2026-10-03, the replaced git history (fetched 2026-10-12)
- https://api.github.com/repos/openswarm-ai/openswarm/releases - the release list ending at v1.8.0 (2026-10-11) after the exp.2-exp.6 line (fetched 2026-10-12)
- https://news.ycombinator.com/item?id=47593100 - the author's Show HN post and the cost and approval rationale
- https://openorchestrators.org/ - the curated directory's Open Swarm entry
- https://openswarm.com/privacy - now the Open Swarm Inc. consumer-assistant privacy policy effective 2026-10-03 (waitlist, ad pixels, session recordings), re-fetched 2026-10-12; the same URL grounded the old no-telemetry positioning when this note was created
