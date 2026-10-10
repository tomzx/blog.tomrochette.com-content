---
showArticleList: false
title: Control planes
created: 2026-09-24
visible: true
status: in progress
tags: [agents, control-planes]
readability: 3
---

Governance above the harness: policy, permissions, approvals, budgets, trust, settlement, and audit between agent intent and execution.

- [Agent Control](agent-control/index.md) - Galileo's Apache-2.0 control plane that turns any Python or TypeScript function into a governed decision point with a @control() decorator and remotely managed policy.
- [CC Safety Net](cc-safety-net/index.md) - the MIT pre-execution guard that parses commands across sixteen coding-agent CLIs and blocks destructive git and filesystem operations plus secret reads before they run.
- [Code Atelier Governance SDK](code-atelier-governance-sdk/index.md) - the MIT Python SDK that puts scope, budget, approval, and loop gates in front of LLM calls and writes an HMAC audit chain to your existing Postgres.
- [Cordum](cordum/index.md) - the BUSL-1.1 source-available control plane whose Go safety kernel returns ALLOW, DENY, or REQUIRE_APPROVAL before a worker runs, with a Claude Code hook firewall on the endpoint.
- [CrowdStrike Falcon Guardian](crowdstrike-falcon-guardian/index.md) - the commercial AIDR layer that discovers shadow AI agents and turns AI usage policy into endpoint-enforced controls at agent execution time.
- [Databricks Unity Gateway](databricks-unity-gateway/index.md) - the managed governance gateway inside Unity Catalog that routes every model and MCP request through permissions, guardrails, rate limits, and dollar-cost audit tables.
- [HOL Guard](hol-guard/index.md) - the Apache-2.0 consortium-built runtime guard whose published per-harness coverage contract names what it can and cannot see, with approvals, local receipts, supply-chain inspection, and a freemium cloud.
- [Jamf AI Governance](jamf-ai-governance/index.md) - the Mac-native capability that turns AI usage policy into enforced vendor configurations for Claude Code, Codex, and their neighbors through Apple device management.
- [Microsoft Agent Governance Toolkit](microsoft-agent-governance-toolkit/index.md) - the MIT multi-language toolkit for deterministic policy, identity, sandboxing, SRE, and compliance, with a critical authentication writeup to read first.
- [Okto Pulse](okto-pulse/index.md) - the Elastic-2.0 local-first SDLC workbench that blocks coding-agent status transitions until spec coverage and delivery evidence are met.
- [OpenAPPA](openappa/index.md) - the MIT Rust engine that labels everything an agent reads with an audience and trust level and checks every tool call against TOML information-flow policy before it runs.
- [Paperclip](paperclip/index.md) - the MIT self-hosted control plane for a company of agents, heartbeats, budgets, and governance, about 98.2k stars in seven months.
- [SettleBridge](settlebridge/index.md) - the trust and policy gateway for agent-to-agent settlement, with escrow, reputation, and Merkle audit trails, and unresolved license metadata.
- [SIDJUA](sidjua/index.md) - the governance-first orchestrator with a five-stage pre-action pipeline, frozen since April 2026 with its announced reopening date missed.
- [TinyAGI](tinyagi/index.md) - the one-person-company orchestrator that stalled in March 2026, kept as the category's first consolidation record.
- [Veto](veto/index.md) - the Apache-2.0 authorization kernel that holds or blocks risky agent tool calls before execution and records offline-verifiable receipts.

Its members are compared on shared rows in the [Control Planes Feature Matrix](control-planes-feature-matrix/index.md).

## Changes

- 2026-08-27 - Added Paperclip.
- 2026-08-27 - Added TinyAGI.
- 2026-09-27 - Added Code Atelier Governance SDK.
- 2026-09-27 - Added Microsoft Agent Governance Toolkit.
- 2026-09-27 - Added Okto Pulse.
- 2026-09-27 - Added SettleBridge.
- 2026-09-27 - Added SIDJUA.
- 2026-09-27 - Added Veto.
- 2026-10-02 - Added Databricks Unity Gateway.
- 2026-10-04 - Added CrowdStrike Falcon Guardian.
- 2026-10-05 - Added Agent Control.
- 2026-10-05 - Added Jamf AI Governance.
- 2026-10-07 - Added Cordum.
- 2026-10-07 - Added OpenAPPA.
- 2026-10-07 - Added CC Safety Net.
- 2026-10-09 - Added HOL Guard.
