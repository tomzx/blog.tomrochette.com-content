---
title: "Control Planes Feature Matrix"
created: 2026-08-27
updated: 2026-09-02
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, control-planes, agent-operations]
readability: 3
audience_notes: >
  Engineers evaluating a control plane for running many agents as an organization.
  Assumes you run at least one agent that can receive a heartbeat and know what an org chart is for.
---

This matrix compares the agent control planes profiled in this section: the flagship and the first stall record, so the category's consolidation story sits in one table.
Everything below was verified against live sources on 2026-09-02.

**A control plane is not a dashboard with more panels, it is an org (budgets, approvals, chain of command) wrapped around a heartbeat scheduler, and the second column below is the stall record proving the category fits exactly one open-source flagship.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.

## The matrix

| Feature | [Paperclip](../paperclip/index.md) | [TinyAGI](../tinyagi/index.md) |
| --- | --- | --- |
| Kind | self-hosted Node.js server and React UI, embedded Postgres | self-hosted orchestrator, TinyOffice web portal and TUI |
| License | ✓ MIT | ✓ MIT |
| Runtime model | heartbeat wakes on schedules and events, ticket checkout with 409 conflicts | SQLite queue with atomic transactions, retries, dead-letter |
| Agent contract | anything that can receive a heartbeat (OpenClaw, Claude Code, Codex, Cursor, HTTP) | Claude, Codex, and OpenAI or Anthropic-compatible endpoints |
| Team structure | ✓ org chart, mixed human and agent roles | ✓ multi-team, chain execution and fan-out |
| Governance | ✓ org chart, approvals, chain of command, immutable audit log | ✗ none recorded |
| Budgets | ✓ per-agent monthly budgets with auto-pause | ✗ |
| Sandboxed execution | ✓ e2b, Cloudflare, Daytona, Modal, Novita, self-hosted Kubernetes | ~ isolated agent workspaces |
| Multi-company | ✓ unlimited per deployment, data isolation | ✗ one company per install |
| Channels | any heartbeat-capable agent surface | Discord, WhatsApp, Telegram |
| Pricing | free self-hosted, cloud in waitlist, unpublished | free |
| Current status | active, about 79k stars since 2026-03-02, 5,336 open issues | stalled March 2026, 3,612 stars, 75 open issues |

## Reading the matrix

**The rows that separate a control plane from the orchestration category are governance, budgets, and multi-company isolation; a tool with parallel agents but none of those rows belongs in Orchestration, not here.**
Paperclip fills all three, TinyAGI filled the team rows and none of the governance ones, and the gap plus the March 2026 stall is the consolidation story in two columns.

The un-profiled long tail stays in prose until something clears the bar: claw-empire (1,366 stars, also stalled since March), desplega-ai's agent-swarm (729 stars, active, self-described company agentic operating system), multigent (62 stars), Cabinet (a knowledge-base product compared to Paperclip in its launch thread, a different problem), and kastra (policy enforcement for harnesses, a governance slice rather than a plane).
The employee side has its own category, [Assistant runtimes](../assistant-runtimes-feature-matrix/index.md), anchored by OpenClaw, the -claw variants, and Hermes.

## Choosing from the matrix

- Multiple agents toward business goals with cost ceilings and audit needs: Paperclip, the only living column.
- Repo-scale parallel coding agents instead: the Orchestration matrix is the right shelf.
- One agent: a harness plus a task tracker, no control plane needed.
- Studying the category's consolidation: TinyAGI, accepting it is a stall record, not a tool.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the repo-scale counterpart category
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the ledger layer a control plane generalizes
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the supervision problem heartbeats answer
- [Read the Commits, Not the Manual](../../learnings-from-openclaw/index.md) - the employee-side complement, profiled by the corpus

## References

- https://github.com/paperclipai/paperclip - pillars, heartbeat model, sandbox providers, roadmap
- https://paperclip.ing - homepage, release cadence, testimonials
- https://docs.paperclip.ing - official documentation
- https://github.com/TinyAGI/tinyagi - team model, queue, TinyOffice for the TinyAGI column
- https://api.github.com/repos/TinyAGI/tinyagi - the stall dates grounding the status row
