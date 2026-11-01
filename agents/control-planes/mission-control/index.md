---
title: Mission Control
created: 2026-11-01
updated: 2026-11-01
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-planes, agent-operations, task-dispatch, self-hosted, open-source]
readability: 3
audience_notes: >
  Operators running several AI agent runtimes (OpenClaw, Claude Code, Codex) who want one local plane for dispatch, review-gated completion, and spend visibility, and who are deciding whether an alpha-stage plane is worth the churn.
  Assumes you know what a task queue, a review gate, and RBAC are.
---

Mission Control (builderz-labs/mission-control) is an MIT-licensed, self-hosted operations plane for AI agents: a Next.js server over SQLite that dispatches tasks to OpenClaw, Claude Code, Codex, and framework-adapter runtimes, holds task completion until a review approval record exists, and tracks sessions, spend, and security events from one dashboard.

**Its bet is that the control plane sits above the runtimes' own loops rather than inside them: the runtimes keep their reasoning and tools, and the plane answers who owns the task, what executed, which result passed review, and where spend accumulated.**

## What it is

One Node.js (Next.js 16) process with SQLite in WAL mode, deployed from source (Node 22+ and pnpm), Docker Compose, a hardened Compose overlay, or a published image, with no account and no forced telemetry.
Agents register through an authenticated REST API, and the surfaces are a web UI, a CLI, an MCP server, an OpenAPI-described REST contract, WebSocket, and SSE.
Every task follows the lifecycle inbox, assigned, in_progress, review, done, with rejected, failed, and cancelled branches; dispatch runs through manual assignment, an atomic queue claim with per-agent capacity, auto-dispatch through the OpenClaw gateway with complexity-based model routing, cron task templates, agent-to-agent handoffs, and automatic stale-task recovery.
Aegis is the completion gate: a reviewer agent (configurable through `MC_COORDINATOR_AGENT`) whose VERDICT must approve before a task reaches done, up to three review cycles before the task fails with accumulated feedback.
The governance row ships roles (admin, operator, viewer), API keys, security events, trust signals, approvals, audits, and evals, beside workspaces that isolate as shared or strict and fail closed on unowned resources.
Host CLI dispatch carries opt-in sandbox flags: an `allowedTools` allowlist, a clamped `--max-budget-usd`, and a workspace-scoped working directory; the changelog states that absent config leaves dispatch byte-identical to before.
Adapters and observation surfaces cover OpenClaw, Claude Code, Codex, CrewAI, LangGraph, AutoGen, and Claude SDK workflows, with adapter depth varying by runtime.

## Status

Active alpha and adopted for its age: 6,424 stars, 125 forks, and 58 open issues as of 2026-11-01, created 2026-02-13, pushed 2026-10-28, with v2.3.0 (2026-07-25) the latest tagged release while main keeps moving past it.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=builderz-labs/mission-control&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=builderz-labs/mission-control&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=builderz-labs/mission-control&type=date&legend=top-left" />
</picture>

The maintainer is nyk (Builderz Labs), and the changelog shows a sustained security habit: hashed API keys at rest, a dependency-advisory patch release, prompt-injection guards, property-based fuzzing at trust boundaries, and strict-workspace enforcement.
**The community footprint is effectively absent: a Hacker News search returns no thread about this project, only same-name lookalikes (a 45-point Show HN for a different Mission Control task manager, pixel-art and terminal dashboards), so the adoption evidence is the star count and the release work, and the name makes coverage searches unreliable.**

## Strengths

- The dispatch loop is genuine orchestration plumbing: atomic queue claims, capacity limits, stale-task recovery, cron templates, and handoffs, with the linked execution session retained per task.
- Completion is gated: a task cannot reach done without an Aegis approval record, and a rejection requeues the task with feedback attached.
- Workspaces isolate as shared or strict and fail closed on ambiguous or unowned resources, which is the right default direction for multi-team deployments.
- Runtime-agnostic by contract, so an OpenClaw, Claude Code, or Codex fleet is governed from one REST, MCP, and CLI surface instead of one dashboard per vendor.

## Cautions

- The README's own warning applies to everything here: alpha software, and APIs, schemas, and configuration may change between releases.
- The changelog states plainly that no approval policy engine is included, so governance is task-level review plus RBAC, not tool-call policy; this plane does not gate what an agent does inside a task the way the enforcement gates in this category do.
- Aegis is an LLM reviewer agent, so gate quality tracks model quality, and the review prompt, verdict parsing, and retry limits are the vendor's own design with no independent measurement.
- The sandbox flags are opt-in and absent config leaves dispatch unchanged, so the safe path for host CLI execution is deliberate setup, not a default.
- The tagged release train went quiet after v2.3.0 (2026-07-25) while main kept moving (last push 2026-10-28), so release notes lag the code you clone.

## Pricing

Free and open source under MIT, self-hosted, no account.
The maintainer sells a fixed-scope Agent OS Setup package (installing the wider agent operating stack, with Mission Control where it fits) at $5,000 to $12,000, usually two to four weeks; it is a services motion beside the free product.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-11-01 | Agent OS Setup | First recorded: $5,000 to $12,000 fixed scope, the maintainer's consulting package beside the free product | https://mc.builderz.dev |

## Compared to

- [Paperclip](../paperclip/index.md): both run companies of agents over a task board, but Paperclip carries org charts, per-agent budgets that pause spend, and a cloud path, while Mission Control is the lighter local plane whose gate is a review record rather than a budget.
- [Cordum](../cordum/index.md): Cordum's safety kernel returns ALLOW, DENY, or REQUIRE_APPROVAL before a worker runs; Mission Control dispatches first and reviews the result after, so choose Cordum when the gate must precede execution.
- [AgentField](../agentfield/index.md): AgentField turns agent functions into governed backend services with cryptographic identity; Mission Control manages existing runtimes from above instead of hosting the agents itself.

## Bottom line

**Recommended for operators running several agent runtimes who want one local plane for dispatch, review-gated completion, and spend visibility, and who accept alpha churn, opt-in guardrails, and self-reported claims.**
Not for tool-call policy enforcement (there is no policy engine), for teams needing a managed multi-tenant SaaS, or for anyone who requires a stable API or independent validation of the review gate.

## Changes

- 2026-11-01 - Created from the task-management worker's routing handoff, profiling the self-hosted operations plane as the category's fourth live plane, with the changelog's no-policy-engine statement as the critical angle.

## See also

- [Paperclip](../paperclip/index.md) - the company-scale control plane this most closely parallels
- [Cordum](../cordum/index.md) - the dispatch-time gate that holds jobs before workers run
- [AgentField](../agentfield/index.md) - the agent-backend plane that hosts functions instead of managing runtimes
- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category compared on shared rows
- [An Agent Is Only as Safe as Its Worst Tool Call](../../../an-agent-is-only-as-safe-as-its-worst-tool-call/index.md) - the corpus argument for why a review gate alone is not the enforcement layer

## References

- https://github.com/builderz-labs/mission-control - README: the governance row, the dispatch loop, the adapters, the alpha warning, and the security boundary
- https://raw.githubusercontent.com/builderz-labs/mission-control/main/docs/orchestration.md - the task lifecycle, the seven dispatch patterns, and the Aegis review flow this note traces
- https://raw.githubusercontent.com/builderz-labs/mission-control/main/CHANGELOG.md - the release history, the opt-in sandbox flags, and the no-approval-policy-engine statement
- https://mc.builderz.dev - homepage: positioning, scale figures, and the Agent OS Setup package
- https://api.github.com/repos/builderz-labs/mission-control - stars, forks, issues, license, creation and push dates as of 2026-11-01
- https://hn.algolia.com/api/v1/search?query=mission-control%20agents&tags=story - the zero-thread footprint check and the same-name collisions, as of 2026-11-01
