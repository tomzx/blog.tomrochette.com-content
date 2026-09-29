---
title: "Control Planes Feature Matrix"
created: 2026-08-27
updated: 2026-09-29
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, llm=deepseek-v4.1-flash, comparison, control-planes, agent-operations]
readability: 3
audience_notes: >
  Engineers evaluating a control plane or a governance gate for running agents as an organization.
  Assumes you run at least one agent and know the difference between an orchestrator and a policy layer.
---

This matrix compares the eight governance tools profiled in this section, from self-hosted agent companies to in-process enforcement gates, so the category's full range and its consolidation story sit in one table.

**A control plane is not a dashboard with more panels, it is governance (policy, budgets, approvals, audit) wrapped around an execution model, and the two stalled columns below (SIDJUA and TinyAGI) show that the open-source agent-company flagships struggle while the narrower enforcement gates keep shipping.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.

## The matrix

| Feature | [Code Atelier Governance SDK](../code-atelier-governance-sdk/index.md) | [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md) | [Okto Pulse](../okto-pulse/index.md) | [Paperclip](../paperclip/index.md) | [SettleBridge](../settlebridge/index.md) | [SIDJUA](../sidjua/index.md) | [TinyAGI](../tinyagi/index.md) | [Veto](../veto/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | Python SDK with in-process gates | multi-language toolkit (Python, TypeScript, .NET, Rust, Go) | local-first SDLC workbench, web UI plus MCP server | self-hosted Node.js server and React UI, embedded Postgres | gateway service (FastAPI plus React dashboard) over Postgres and Redis | self-hosted Node.js platform, web console and SQLite | self-hosted orchestrator, TinyOffice web portal and TUI | framework-agnostic authorization kernel, TypeScript and Python SDKs |
| License | ✓ MIT | ✓ MIT | ~ Elastic-2.0, source-available | ✓ MIT | ? metadata inconsistent: site says Apache-2.0 or MIT, GitHub API reports none | ~ AGPL-3.0 plus commercial | ✓ MIT | ✓ Apache-2.0 |
| Runtime model | in-process gates around wrapped LLM clients, Postgres as the only dependency | interception middleware in app code, fail-closed Rust policy runtime | local FastAPI process, SQLite plus embedded graph, agents over MCP | heartbeat wakes on schedules and events, ticket checkout with 409 conflicts | always-on gateway with hot-reloading policy engine and Redis reputation cache | always-on daemons, governed cron, five-stage pre-action pipeline | SQLite queue with atomic transactions, retries, dead-letter | local deterministic evaluation wrapping tool calls, optional self-hosted or cloud policy server |
| Enforcement point | before the LLM call, in-process; tool calls inside a response are not inspected | before the action reaches the wire, in application middleware | at status transitions on the SDLC board (spec, task, test, done) | approvals and budgets gate agent actions in the company runtime | before a settlement proceeds, at the boundary gateway | before any action executes, outside the agent | ✗ none recorded beyond queue dispatch | before the tool handler runs, outside the model |
| Agent contract | Python code routed through wrap_openai, wrap_anthropic, or the LangChain handler | SDK or framework adapter, with plugins for Claude Code, Copilot CLI, Codex CLI, OpenCode | any MCP-capable coding agent (Claude Code, Codex, Cursor, Windsurf, Cline) | anything that can receive a heartbeat (OpenClaw, Claude Code, Codex, Cursor, HTTP) | agents on LangGraph, CrewAI, or ADK that settle over A2A-SE | any LLM provider (Anthropic, OpenAI, Google, Groq, Ollama, OpenAI-compatible) | Claude, Codex, and OpenAI or Anthropic-compatible endpoints | provider-agnostic tools plus LangChain, LangGraph, Vercel AI SDK, OpenAI Agents, MCP |
| Team structure | ✗ per-agent scopes, no org model | ~ trust tiers and delegation, no org chart | ✗ workflow roles, no org chart | ✓ org chart, mixed human and agent roles | ✗ | ✓ divisions and three trust tiers | ✓ multi-team, chain execution and fan-out | ✗ |
| Governance | ✓ scope, budget, HITL, loop, and presence gates, fail-closed | ✓ YAML, OPA Rego, or Cedar policy engine plus identity and compliance | ✓ 17 named gates on coverage, validation, and evidence | ✓ org chart, approvals, chain of command, immutable audit log | ✓ reputation floor, spend caps, and provenance requirements | ✓ five-stage pipeline plus ten non-removable baseline rules | ✗ none recorded | ✓ YAML rules with allow, block, warn, log, require_approval |
| Budgets | ✓ token and USD caps per session and per agent-day, fail-closed | ~ SLO error budgets, not spend caps | ✗ | ✓ per-agent monthly budgets with auto-pause | ✓ daily spend caps in policy | ✓ per-task and per-agent budgets, fail-closed cancellation | ✗ | ~ budget and cost constraints in policy |
| Sandboxed execution | ✗ in-process only | ✓ execution rings and four privilege levels | ✗ | ✓ e2b, Cloudflare, Daytona, Modal, Novita, self-hosted Kubernetes | ✗ | ~ bubblewrap on Linux, none on macOS and native Windows | ~ isolated agent workspaces | ✗ authorization only |
| Multi-company | ✗ | ~ multi-agent fleet, not multi-company | ✗ boards per install, with authorized global discovery | ✓ unlimited per deployment, data isolation | ✓ cross-organization trust through gateways and the exchange | ✗ one company per install | ✗ one company per install | ✗ |
| Channels | ✗ API and CLI only | ✗ framework adapters, not messaging | ✗ web UI and MCP | any heartbeat-capable agent surface | ✗ | Discord, Email, Telegram, CLI, REST, WebSocket, Slack and WhatsApp in beta | Discord, WhatsApp, Telegram | ✗ |
| Audit and evidence | ✓ HMAC-chained append-only Postgres, Ed25519 signatures, Article 12 report | ✓ tamper-evident Merkle audit and decision records | ✓ evidence gates and knowledge graph provenance | ✓ immutable activity log, run ids, artifacts on issues | ✓ Merkle-linked append-only audit, CSV and JSON export | ✓ integrity-verified write-ahead log with SHA-256 checks | ✗ none recorded | ✓ offline-verifiable decision receipts |
| Pricing | free MIT, hosted bridge unpriced | free MIT | free local, SaaS planned and unpriced | free self-hosted, cloud in waitlist, unpublished | Community free, Enterprise $2,500/month per gateway, Exchange 0.25% per settlement | free AGPL-3.0, commercial and enterprise by contact, unpriced | free | Developer $0, Hosted $299/month for 100K checks, Enterprise custom |
| Current status | active, 0 stars, v0.7.3, last push 2026-07-23 | active, 6,349 stars, 91 open issues, v4.1.0 (2026-06-09), public preview | active, 99 stars, v0.3.3, last push 2026-09-24 | active, about 93.5k stars since 2026-03-02, 6,019 open issues, v2026.916.1 (2026-09-21) | early, 1 star, 76 commits, last push 2026-09-25 | dormant, 26 stars, downloads frozen since April 2026, reopen date missed | stalled March 2026, 3,621 stars, 75 open issues | active product, 14 stars, veto-sdk@2.9.3 (2026-05-07) |

## Reading the matrix

**The rows that separate a control plane from the orchestration category are governance, budgets, and multi-company isolation; the new enforcement rows (enforcement point and audit and evidence) are what separate the governance gates from the planes, and the tables show two live planes at most.**
Paperclip fills governance, budgets, and multi-company isolation; SIDJUA and TinyAGI filled some team rows and none of the surviving ones, so both are stall records; the four gates (Code Atelier, the Microsoft toolkit, Veto, Okto Pulse) fill enforcement and audit while leaving team structure and multi-company empty.
**The category now has two centers of gravity: one open-source agent company (Paperclip) and a cluster of narrower enforcement gates, which is the more durable half because a gate can be adopted without replatforming.**
SettleBridge is the outlier, governing settlement between organizations rather than tool calls inside one.

The un-profiled long tail stays in prose until something clears the bar: claw-empire (1,378 stars, also stalled since March), desplega-ai's agent-swarm (781 stars, active, self-described company agentic operating system), multigent (66 stars), Cabinet (a knowledge-base product compared to Paperclip in its launch thread, a different problem), and OtoDock (scanned 2026-09-10: a 44-point Show HN on 2026-09-09 for its self-hosted company OS, but 111 stars, one maintainer, and a non-OSI license keep it below the bar for now).
Two governance slices surfaced earlier and now resolve as rejections: kastra (the kastra-labs organization holds a 1-star Claude plugin and no framework repository of substance, re-checked 2026-09-29, with the name also shared by two unrelated sub-1-star agent projects) and Blue (rejected 2026-09-18 for want of adoption evidence).
The employee side has its own category, [Assistant runtimes](../../assistant-runtimes/assistant-runtimes-feature-matrix/index.md), anchored by OpenClaw, the -claw variants, and Hermes.

## Choosing from the matrix

- Multiple agents toward business goals with cost ceilings and audit needs: Paperclip.
- Stopping or holding a risky tool call before it runs: Veto, the Microsoft Agent Governance Toolkit, or Code Atelier Governance SDK.
- Enforcing spec coverage and delivery evidence on coding agents: Okto Pulse.
- Settling value between independent agents: SettleBridge.
- Repo-scale parallel coding agents instead: the Orchestration matrix is the right shelf.
- Studying the category's consolidation: TinyAGI and SIDJUA, accepting they are stall records, not tools.

## Changes

- 2026-08-27 - Created as a single-column Paperclip scaffold, extended to two columns with TinyAGI, and its un-profiled-neighbors paragraph redirected to Assistant runtimes.
- 2026-09-07 - Paperclip issues cell and long-tail prose updated.
- 2026-09-10 - OtoDock added to the long tail on rejection.
- 2026-09-18 - Paperclip status cell refreshed (about 81k stars, 5,497 open issues) and Blue added to the long tail on rejection.
- 2026-09-21 - Paperclip and TinyAGI status cells refreshed (5,566 open issues; stall record unchanged).
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-25 - Refreshed the Paperclip status cell (about 82.7k stars, 5,643 open issues, v2026.916.1 of 2026-09-21).
- 2026-09-27 - Refreshed the Paperclip status cell (about 87.9k stars, 5,776 open issues) and the TinyAGI star count (3,621).
- 2026-09-27 - Added columns for Code Atelier Governance SDK, Microsoft Agent Governance Toolkit, Okto Pulse, SettleBridge, SIDJUA, and Veto; re-sorted all columns alphabetically; added enforcement-point and audit-and-evidence rows; rewrote the intro and reading-the-matrix prose for eight members.
- 2026-09-29 - Refreshed the Paperclip status cell (about 93.5k stars, 6,019 open issues) and resolved the kastra and Blue candidates as explicit rejections.

## See also

- [Orchestration Feature Matrix](../../orchestration/orchestration-feature-matrix/index.md) - the repo-scale counterpart category
- [Task Management Feature Matrix](../../task-management/task-management-feature-matrix/index.md) - the ledger layer a control plane generalizes
- [Sandboxing Feature Matrix](../../sandboxing/sandboxing-feature-matrix/index.md) - the isolation layer several of these gates deliberately leave out
- [Managing Many Concurrent LLM Agent Sessions](../../../managing-many-llm-agent-sessions/index.md) - the supervision problem heartbeats answer
- [Read the Commits, Not the Manual](../../../learnings-from-openclaw/index.md) - the employee-side complement, profiled by the corpus

## References

- https://github.com/paperclipai/paperclip - pillars, heartbeat model, sandbox providers, roadmap
- https://paperclip.ing - homepage, release cadence, testimonials
- https://docs.paperclip.ing - official documentation
- https://github.com/TinyAGI/tinyagi - team model, queue, TinyOffice for the TinyAGI column
- https://api.github.com/repos/TinyAGI/tinyagi - the stall dates grounding the status row
- https://github.com/microsoft/agent-governance-toolkit - the Microsoft toolkit column's packages, policy, and audit rows
- https://github.com/PlawIO/veto - Veto's rules, adapter matrix, and receipts
- https://github.com/imleopereira/agentic-governance - Code Atelier gates, threat model, and Postgres audit chain
- https://github.com/OktoLabsAI/okto-pulse - Okto Pulse gates, MCP surface, and local-first runtime
- https://github.com/a2a-settlement/settlebridge-ai - SettleBridge gateway components and settlement boundary
- https://github.com/GoetzKohlberg/sidjua - SIDJUA five-stage pipeline, divisions, and audit log
