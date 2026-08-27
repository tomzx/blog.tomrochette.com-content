---
title: "Control Planes Feature Matrix"
created: 2026-08-27
updated: 2026-08-27
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, comparison, control-planes, agent-operations]
readability: 3
audience_notes: >
  Engineers evaluating a control plane for running many agents as an organization.
  Assumes you run at least one agent that can receive a heartbeat and know what an org chart is for.
---

This matrix compares the agent control planes profiled in this section.
The category has one profiled member as of 2026-08-27, so this is the single-column scaffold the next member extends, and the gap is named below.
Everything below was verified against live sources on 2026-08-27.

**With one column the matrix still makes the category's key comparison readable: a control plane is not a dashboard with more panels, it is an org (budgets, approvals, chain of command) wrapped around a heartbeat scheduler, and every future column will be judged on those rows.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.

## The matrix

| Feature | [Paperclip](../paperclip/index.md) |
| --- | --- |
| Kind | self-hosted Node.js server and React UI, embedded Postgres |
| License | ✓ MIT |
| Runtime model | heartbeat wakes on schedules and events, ticket checkout with 409 conflicts |
| Agent contract | anything that can receive a heartbeat (OpenClaw, Claude Code, Codex, Cursor, HTTP) |
| Governance | ✓ org chart, approvals, chain of command, immutable audit log |
| Budgets | ✓ per-agent monthly budgets with auto-pause |
| Sandboxed execution | ✓ e2b, Cloudflare, Daytona, Modal, Novita, self-hosted Kubernetes |
| Multi-company | ✓ unlimited per deployment, data isolation |
| Pricing | free self-hosted, cloud in waitlist, unpublished |
| Current status | active, about 79k stars since 2026-03-02, 5,417 open issues |

## Reading the matrix

**The rows that separate a control plane from the orchestration category are governance, budgets, and multi-company isolation; a tool with parallel agents but none of those rows belongs in Orchestration, not here.**
Paperclip fills all three today, which is why it anchors the category despite being six months old.

The un-profiled neighbors stay in prose until they earn notes: smaller ticket-orchestrator experiments have not cleared the credibility bar, while the employee side now has its own category, [Assistant runtimes](../assistant-runtimes-feature-matrix/index.md), anchored by [OpenClaw](../openclaw/index.md) and its shrinking variants.

## Choosing from the matrix

- Multiple agents toward business goals with cost ceilings and audit needs: Paperclip, the only profiled column, self-hosted.
- Repo-scale parallel coding agents instead: the Orchestration matrix is the right shelf.
- One agent: a harness plus a task tracker, no control plane needed.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the repo-scale counterpart category
- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the ledger layer a control plane generalizes
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the supervision problem heartbeats answer
- [Read the Commits, Not the Manual](../../learnings-from-openclaw/index.md) - the employee-side complement, profiled by the corpus

## References

- https://github.com/paperclipai/paperclip - pillars, heartbeat model, sandbox providers, roadmap
- https://paperclip.ing - homepage, release cadence, testimonials
- https://docs.paperclip.ing - official documentation
