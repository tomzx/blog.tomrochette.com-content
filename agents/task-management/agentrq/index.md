---
title: AgentRQ
created: 2026-10-13
updated: 2026-10-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, mcp, human-in-the-loop, self-hosted]
readability: 3
audience_notes: >
  People who delegate work to coding agents and want a realtime human-in-the-loop task board they self-host and reach from phone, web, or desktop.
  Assumes you know what MCP and ACP are.
---

AgentRQ is an AGPL-3.0, self-hosted human-in-the-loop task platform where agents pull assigned tasks and update statuses over MCP while the human watches, approves sensitive actions, and steers from a realtime board on mobile, web, or desktop.

**Its bet is supervision as conversation: the task board is the shared workspace, agents see its state over MCP and act autonomously inside it, and every permission request lands in the same thread the human is already reading.**

## What it is

A self-hosted platform (web, desktop, and a Chrome extension) that exposes a task management workspace to AI models over MCP and accepts work from any harness with ACP support, designed around the Claude subscription you already have.
Humans break goals into tasks and delegate; agents pull assignments, update statuses, and request permissions for sensitive actions in realtime; the board renders captures of the running app rather than mockups, per its own README.
A companion Chrome extension carries the board into the browser; the README carried a Discord link until v0.12.0 removed it, so the community channel is currently undocumented.

## Status

Active and modest: 1,152 stars as of 2026-10-14, 85 forks, and 2 open issues and pull requests as of 2026-10-18, created 2026-03-24, pushed 2026-10-18, AGPL-3.0 throughout, on a three-release train in two days (v0.11.1 to v0.11.3, 2026-10-15 and 2026-10-16) that added a native-ACP reasoning-level picker and refactored the ACP link layer into a protocol-neutral agentlink package, then v0.12.0 (2026-10-17), a security-and-ops minor that fixed SQL-injection and tool-spoofing holes in the ACP tool-call path, made the acp-gateway speak only native ACP v1, and added health and readiness probes with S3-shared TLS certificates.
Post-release commits keep landing on the main branch: per-task plan rows pinned above the chat, native-ACP resource links and notice toasts, and Claude plugin manifest fixes.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=agentrq/agentrq&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=agentrq/agentrq&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=agentrq/agentrq&type=date&theme=dark&legend=top-left" />
</picture>

**The independent record exists but is small: a 6-point Show HN from April 2026, a 2-point follow-up discussion, and little third-party coverage since, so the realtime claim rests on the README's own captures rather than field reports.**
Two open issues and pull requests against an active branch suggests either a quiet user base or fast triage; the README does not say which.

## Strengths

- The MCP-native task surface means any MCP client can see and act on the workspace, no per-harness plugin required.
- Permission requests for sensitive actions land in the approval flow, which is the human-in-the-loop mechanic done at the right layer.
- Self-hosted with your existing Claude subscription, so the task layer adds no per-seat bill and no vendor custody of your task history.
- Realtime sync across mobile, web, desktop, and the Chrome extension covers the where-am-I-when-the-agent-asks case.
- AGPL-3.0 keeps the server code copyleft, so improvements cannot close.

## Cautions

- AGPL-3.0 is a binding constraint for internal tooling teams with distribution concerns; read it before wiring it into a product.
- The traction record is one 6-point Show HN; the realtime and capture claims are the vendor's own.
- Task structure depth (dependencies, PRD ingestion) is undocumented in the README head, so plan-level rigor looks lighter than this category's dedicated trackers.
- Self-hosting a realtime collaboration server is an operational commitment the one-maintainer project does not document an ops story for.
- The ACP and MCP surfaces move fast upstream; version pinning discipline is on you.

## Pricing

Free and open source under AGPL-3.0, self-hosted.
No hosted tier and no paid plan; agents run on your existing subscriptions.

## Compared to

- [beads](../beads/index.md): the issue-tracker-native tracker with the largest adoption in the category; beads lives in your repo, AgentRQ puts the board in your pocket.
- [PlanDB](../plandb/index.md): the SQLite compound-graph planner with atomic claims; PlanDB is agent-first structure, AgentRQ is human-first supervision.
- [Backlog.md](../backlog-md/index.md): the file-based board that keeps tasks in the repository; choose it when the board must version with the code.

## Bottom line

**Recommended for solo operators and small teams who want self-hosted, phone-reachable supervision of MCP-capable agents under their own subscriptions.**
Not for AGPL-constrained teams, or anyone needing repository-native task storage or deep dependency planning.

## Changes

- 2026-10-13 - Created.
- 2026-10-16 - Recorded the v0.11.1 to v0.11.3 release train (2026-10-15 and 2026-10-16: the native-ACP reasoning-level picker, the protocol-neutral agentlink package, and task-save and publish fixes) and refreshed counts (2 open issues, pushed 2026-10-16).
- 2026-10-17 - Recorded v0.12.0 (2026-10-17: SQL-injection and tool-spoofing fixes in the ACP tool-call path, the acp-gateway speaking only native ACP v1, health and readiness probes, S3-shared TLS certificates, and the README's Discord link removed) and refreshed counts (pushed 2026-10-17).

## See also

- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins
- [beads](../beads/index.md) - the category's repo-native heavyweight
- [PlanDB](../plandb/index.md) - the agent-first structured planner
- [Backlog.md](../backlog-md/index.md) - the file-based board alternative
- [Model Context Protocol (MCP)](../../protocols/mcp/index.md) - the protocol AgentRQ exposes its workspace over

## References

- https://github.com/agentrq/agentrq - repository, AGPL-3.0 license, stars, push activity, and the MCP workspace model as of 2026-10-13
- https://agentrq.com/ - the product site and self-hosted positioning
- https://github.com/agentrq/agentrq/blob/main/README.md - the feature set, realtime capture claims, and harness support statement
- https://chromewebstore.google.com/detail/agentrq/iadkenmjgjoilnioldgchgjpdnbaghbj - the published Chrome extension backing the browser surface
- https://api.github.com/repos/agentrq/agentrq/releases - v0.11.1 to v0.11.3 (2026-10-15 and 2026-10-16) and v0.12.0 (2026-10-17): the release train and the security fixes
- https://news.ycombinator.com/item?id=47958608 - the April 2026 Show HN (6 points), the project's main independent footprint
