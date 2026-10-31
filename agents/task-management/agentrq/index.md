---
title: AgentRQ
created: 2026-10-13
updated: 2026-10-31
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

Active and modest: 1,152 stars as of 2026-10-14, 86 forks, and 4 open issues and pull requests as of 2026-10-31, created 2026-03-24, pushed 2026-10-31, with a dual licence since v0.13.0: the repository stays AGPL-3.0-only with a binary-only commercial licence from Contextual, Inc., while the agentrqd server daemon, its installers, and the agentrq-ws CLI are published under Apache-2.0.
The v0.11.1 to v0.11.3 train (2026-10-15 and 2026-10-16) added a native-ACP reasoning-level picker and refactored the ACP link layer into a protocol-neutral agentlink package, v0.12.0 (2026-10-17) fixed SQL-injection and tool-spoofing holes in the ACP tool-call path, made the acp-gateway speak only native ACP v1, and added health and readiness probes with S3-shared TLS certificates, v0.12.1 (2026-10-18) landed the per-task plan rows pinned above the chat plus native-ACP notices, resource-link file handoffs, and Claude plugin manifest fixes, and v0.13.0 (2026-10-18) shipped the server as one binary with the web app built in and made the supervisor workspace clear context by default.
v0.13.1 (2026-10-21) shipped the MCP text attachments and pointed the task tool at the agentrq-ws CLI for them alongside dependency security patches, and v0.13.2 (2026-10-23) added a per-user MCP connections and machines-online view for the operator and quieted native and web-push notifications for agent thoughts, plans, and usage.
v0.13.3 and v0.13.4 (both 2026-10-24) rebuilt the README around animated scenes in place of screenshots, added a Task Timeline feature row and Machine Info tiles with a CPU meter, made enrollment start serving so setup drops the serve step, fixed one-line task titles and the phone title model, and patched dependency advisories in dompurify, vitest, and electron.
v0.14.0 (2026-10-28) began moving the desktop app from Electron to Tauri: a pure Rust core landed behind the same UI (window state, deep links, notifications, updater, tray, protocol routing, CSP), with the SidePanel guest abstraction and an isolated-workspaces feature row added to the README.
v0.14.2 (2026-10-30) sealed desktop secrets with a key file instead of the OS keychain, and the v0.15 train followed within two days: v0.15.0 stopped the API throttles trusting client-sent addresses, believing a client-address header only from configured proxies, and opened the Links note's web links in the side panel, and v0.15.1 (2026-10-31) made the workspace MCP server advertise a title, description, and website, exposed each action tool's actions as a real schema enum, named the agent on each kanban task card with its icon, showed each workspace's active tasks and its forks, and landed a broad test-coverage expansion across the API, MCP, Slack, notification, and event handlers.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=agentrq/agentrq&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=agentrq/agentrq&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=agentrq/agentrq&type=date&legend=top-left" />
</picture>

**The independent record exists but is small: a 6-point Show HN from April 2026, a 2-point follow-up discussion, and little third-party coverage since, so the realtime claim rests on the README's own captures rather than field reports.**
Nine open issues and pull requests against an active branch suggests either a quiet user base or fast triage; the README does not say which.
The count stood at four as of 2026-10-31.

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

Self-hosted and free under AGPL-3.0-only, dual-licensed since v0.13.0 with a binary-only commercial licence from Contextual, Inc. for proprietary use without the AGPL's obligations.
The agentrqd daemon, its installers, and the agentrq-ws CLI keep their own Apache-2.0; agents run on your existing subscriptions.

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
- 2026-10-20 - Recorded v0.12.1 and v0.13.0 (both 2026-10-18: per-task plan rows pinned above the chat, native-ACP notices, resource-link file handoffs, and Claude plugin manifest fixes, then the server shipped as one binary with the web app built in and the supervisor workspace clearing context by default) and the v0.13.0 license split (agentrqd, its installers, and the agentrq-ws CLI published under Apache-2.0 while the repository stays AGPL-3.0-only with a binary-only commercial tier), with pushed refreshed to 2026-10-19.
- 2026-10-21 - Out-of-rotation correction: brought the Pricing section in line with the v0.13.0 licence split the previous run recorded, naming the dual licence (AGPL-3.0-only repository plus a binary-only commercial licence from Contextual, Inc.) and the Apache-2.0 daemon, installers, and CLI, re-verified against the README's licence section (fetched 2026-10-21).
- 2026-10-23 - Recorded v0.13.1 and v0.13.2 (2026-10-21 and 2026-10-23: the MCP text attachments shipped with the task tool pointed at agentrq-ws, dependency security patches, the per-user MCP connections and machines-online view, and the notification routing fixes) and refreshed counts (pushed 2026-10-23).
- 2026-10-25 - Recorded v0.13.3 and v0.13.4 (both 2026-10-24: the README rebuilt around animated scenes with a Task Timeline feature row, Machine Info CPU tiles, enrollment starting the server itself, and dependency security patches) and refreshed counts (87 forks, 9 open issues and pull requests, pushed 2026-10-25).
- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-27 - Corrected the star-history chart light source (it carried the dark-theme parameter; only the dark source may).
- 2026-10-27 - Restored the Changes order (the 2026-10-25 fallback-markup bullet sat below the 2026-10-27 light-source bullet; oldest first is the rule).
- 2026-10-28 - Recorded v0.14.0 (2026-10-28: the desktop app's Electron-to-Tauri migration with a pure Rust core, the SidePanel guest abstraction, and an isolated-workspaces feature row) and refreshed counts (86 forks, 6 open issues and pull requests, pushed 2026-10-28).
- 2026-10-31 - Recorded v0.14.2 through v0.15.1 (2026-10-30 and 2026-10-31: desktop secrets sealed with a key file instead of the OS keychain, throttle address-trust fixes believing client-address headers only from configured proxies, the workspace MCP server advertising title, description, and website, action-tool schema enums, agent-named kanban cards, and a broad test-coverage expansion) and refreshed counts (4 open issues and pull requests, pushed 2026-10-31).

## See also

- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the category comparison this note joins
- [beads](../beads/index.md) - the category's repo-native heavyweight
- [PlanDB](../plandb/index.md) - the agent-first structured planner
- [Backlog.md](../backlog-md/index.md) - the file-based board alternative
- [Model Context Protocol (MCP)](../../protocols/mcp/index.md) - the protocol AgentRQ exposes its workspace over

## References

- https://github.com/agentrq/agentrq - repository, AGPL-3.0 license, stars, push activity, and the MCP workspace model as of 2026-10-31
- https://agentrq.com/ - the product site and self-hosted positioning
- https://github.com/agentrq/agentrq/blob/main/README.md - the feature set, realtime capture claims, the harness support statement, and the dual-licence section (licence re-fetched 2026-10-21)
- https://chromewebstore.google.com/detail/agentrq/iadkenmjgjoilnioldgchgjpdnbaghbj - the published Chrome extension backing the browser surface
- https://api.github.com/repos/agentrq/agentrq/releases - the release train from v0.11.1 (2026-10-15) through v0.15.1 (2026-10-31): the security fixes, the feature releases, and the Tauri migration
- https://news.ycombinator.com/item?id=47958608 - the April 2026 Show HN (6 points), the project's main independent footprint
