---
title: Open Swarm
created: 2026-09-27
updated: 2026-09-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, orchestration, mission-control, human-in-the-loop, worktrees]
readability: 3
audience_notes: >
  Engineers who want to launch and approve several agents from one local dashboard.
  Assumes you run Claude or plan to, and understand git worktrees and MCP servers.
---

Open Swarm is an AGPL-3.0, local-first mission-control desktop app for launching, monitoring, approving, and coordinating multiple AI coding agents in parallel on a spatial canvas.

**Open Swarm's bet is that the bottleneck is supervision, not spawning: it puts every agent on one pan-and-zoom canvas, funnels every tool-use request into a single approval workflow, and keeps the whole thing on your machine with no cloud relay or telemetry.**

## What it is

A desktop app (Electron shell over a React frontend and a FastAPI backend on port 8324) from openswarm-ai that runs Claude-powered agents through the Claude Agent SDK.
The spatial dashboard is an infinite canvas of drag-and-drop agent cards, view cards, and embedded browser cards; agent chat streams over WebSockets with per-session cost tracking and persistent history.
Its differentiators are a unified human-in-the-loop approval workflow (per-tool permissions of always-allow, ask, or deny, with batch approval from the dashboard), message branching that forks a conversation by editing a prior message, prompt templates, a skills library that syncs to `~/.claude/skills/`, and an MCP tools library with registry browsing.
Each agent gets its own git worktree and branch, with a diff viewer for uncommitted changes, and there are five built-in agent modes plus custom modes, interactive HTML/JS/CSS output views, dark and light themes, and keyboard shortcuts.
It currently targets macOS; Windows and Linux builds are documented as planned.

## Status

Active but small: about 820 stars and 171 forks as of 2026-09-27, created 2026-03-13, with development through 2026-09-23.
The current release line is explicitly experimental (v1.8.0-exp.2 on 2026-09-23), with a stable v1.7.11 before it.
**The signal is a license inconsistency: the README and the curated directory call it MIT, but the repository's LICENSE file is AGPL-3.0 and GitHub's API reports AGPL-3.0, so the permissive badge is the one piece of documentation not to trust.**

## Strengths

- The unified approval workflow is the strongest part of the design: one place to approve or deny tool calls across every agent.
- Cost tracking per session and per agent, which the parallel-agent category mostly leaves to the provider dashboard.
- Git worktree isolation per agent plus a diff viewer, so parallel work is contained and reviewable locally.
- Skills, MCP tools, prompt templates, and message branching give it real depth beyond a chat multiplexer.
- Fully local by design: no cloud relay, no telemetry, and the backend can be run directly for self-hosting.

## Cautions

- The README's MIT badge contradicts the AGPL-3.0 LICENSE, so confirm the actual terms before commercial or embedded use.
- macOS only as of 2026-09-27; Windows and Linux are planned but not shipped.
- Built on the Claude Agent SDK and Anthropic models; README says other models are coming, so it is effectively single-provider today.
- The advertised release line is experimental (v1.8.0-exp), so expect churn.
- The name collides with an unrelated `Intrect-io/OpenSwarm` Show HN project, which confuses search and comparisons.

## Pricing

Free and open source (AGPL-3.0 per the repository's LICENSE).
No hosted tier and no token markup; agents run on your own Anthropic API key.

## Compared to

- [Lanes](../lanes/index.md): macOS board-first with real PTY sessions and an access-governance endpoint; choose Open Swarm for the approval-centric canvas and cost tracking.
- [Conductor](../conductor/index.md): the polished closed Mac worktree dashboard; choose Open Swarm for a free, local, approval-gated alternative.
- [OpenChamber](../../surfaces/openchamber/index.md): a scheduled and interactive session surface; choose Open Swarm when you need many agents coordinated on one visible canvas.

## Bottom line

**Recommended for macOS engineers who run several Claude agents and want one local canvas with unified tool approvals and per-session cost tracking.**
Not for cross-platform teams, multi-provider fleets, or anyone who needs the README's MIT terms.

## Changes

- 2026-09-27 - Created.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Lanes](../lanes/index.md) - the board-first macOS workspace
- [Conductor](../conductor/index.md) - the closed Mac incumbent
- [Claude Squad](../claude-squad/index.md) - the free terminal alternative
- [OpenChamber](../../surfaces/openchamber/index.md) - the session-centric surface

## References

- https://github.com/openswarm-ai/openswarm - repository, architecture, features, stars, and the AGPL-3.0 LICENSE
- https://raw.githubusercontent.com/openswarm-ai/openswarm/HEAD/README.md - features, approval workflow, skills and MCP libraries, and the MIT badge
- https://news.ycombinator.com/item?id=47593100 - the author's Show HN post and the cost and approval rationale
- https://openorchestrators.org/ - the curated directory's Open Swarm entry
- https://openswarm.com/privacy - the no-cloud-relay and no-telemetry positioning
