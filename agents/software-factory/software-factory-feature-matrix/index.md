---
title: "Software Factory Feature Matrix"
created: 2026-08-29
updated: 2026-10-07
status: finished
tags: [agent-curated, fully-ai-generated, llm=big-pickle, llm=glm-5.3-flash, comparison, software-factory, agentic-workflows]
readability: 3
audience_notes: >
  Engineers comparing repeatable, code-owned agent pipelines against each other.
  Assumes you know what a phase, an envelope, a gate, a worktree, and a skill are.
---

This matrix compares the members of the Software factory category: repeatable agents-plus-code production pipelines, where deterministic code owns the loop and agents are bounded nodes inside it.

**The deciding question for this category is who owns the loop: a factory puts phase sequencing, retries, and acceptance in code, and an agent owns only the work inside one bounded phase.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Fluent](../fluent/index.md) | [HAR](../har/index.md) | [Loki Mode](../loki-mode/index.md) | [Machinist](../machinist/index.md) | [Ouroboros](../ouroboros/index.md) | [Super Simple Software Factory](../super-simple-software-factory/index.md) | [SuperPlane](../superplane/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Delivery | Rust binary + skill for Codex/Claude Code/Pi, macOS only | CLI + MCP server, npm package | CLI (npm, Bun, Homebrew, Docker) + MCP server, by Autonomi | Go binary, machinist.sh docs | PyPI package + MCP server + Claude Code plugin | one skill (.claude/skills/sssf), stamped into any repo | self-hosted platform (Go engine, React surface), cloud or on-prem |
| Loop owner | Rust binary owns scheduler, reviewer, tester, learner | deterministic verify stages; agents own their edits | the Loki engine owns contract-to-receipt; agents build and review inside it | Go controller owns invocation and recording; agents own the work | Python orchestrator owns interview, spec, execute, evaluate, evolve | Python ADW scripts (code owns sequencing, retries, acceptance) | the platform owns the work-order line: intake, automation stages, retries, outcome |
| Agent boundary | Work Items in isolated worktrees, human attention queue, v0.3.0 Slack planning and approvals | one isolated slot per agent | briefs in; review council of specialist reviewers; blocked runs ask one question | named commands over named repositories, never arbitrary shell | worker never sees the grading command or expected result | one agent, one named phase at a time | work orders under workflow-level guardrails; ambiguous work and approvals stay with humans |
| Context across seams | Brief, Behavior Specs (EARS), Technical Approach, Plan | .har contract, shared by all agents | delivery contract (the acceptance criteria) derived before any build | prompts on stdin, optional prompt files | immutable Seed spec frozen before any code | typed JSON envelopes, parsed against a schema | work-order record from intake to outcome, with event history and artifacts |
| Acceptance | deterministic final Tester bound to the reviewed commit | deterministic verify with per-commit evidence trail | signed Evidence Receipt, states what was proven and what was not; loki verify re-checks offline | hands back a pull request, human gate, never ships | 3-stage gate: mechanical (70% coverage default), semantic LLM (0.8), consensus on triggers | gates that verify artifacts and tests after the fact | result checked, failures sent back with actionable context; humans review the PR |
| Failure handling | resumable Writer correction, fail-closed evidence, v0.3.0 recovery for long-running scheduler-owned work | per-slot teardown, evidence kept | outcomes and exit codes; an underivable contract blocks and asks one question | exit code decides; a killed script restarts from the beginning | budgeted evolution, 30-generation cap, stagnation detection | same-session correction, no cold restart | durable runs survive retries with event history, state, and artifacts |
| Self-improvement | ✓ Learner writes reusable Expertise after each change | ~ plugins and templates reduce drift, no learner | ✗ none (a static scored specialist pool, no learner) | ✗ none | ✓ refines specs and accumulates reusable assets across generations | ✗ none | ~ continuously re-evaluates which issues agents can handle; no learner |
| Isolation | ✓ isolated worktree, remote via AWS Fargate | ✓ worktree, ports, and database per slot | ? not verified (runs locally with your keys) | ✗ none built in, executor-dependent | ~ delegated to the host runtime | ✗ runs on current branch, no sandbox or merge step | ? not verified in the fetched docs |
| Coding agent | Codex, Claude Code, or Pi | Claude Code, Cursor, Codex, or any MCP agent | Claude, Codex, OpenCode (your keys) | any executable reading a prompt on stdin | 14 runtimes, Claude Code through Antigravity | pi only (claude_code stubbed) | Claude, Cursor, OpenAI, OpenRouter, Perplexity via integrations |
| Trace | Work Item / Attempt record with bound evidence | Mission Control dashboard per run and artifact | Evidence Receipt plus verdict and cost; live control plane on the site | durable events, artifacts, outcome, duration, reported tokens | event sourcing with full replay and lineage | SQLite, tool calls visible mid-run | Run records per step: inputs, outputs, retries, cost |
| License | Apache-2.0 | Apache-2.0 | BUSL-1.1 (source-available) | MIT | MIT | MIT | Apache-2.0 core, Enterprise Edition license for /ee |
| Pricing | free, no paid tier, no hosted cloud | core free; HAR HQ Team $400 per month up to 50 users with $100 monthly cloud credits, Enterprise custom (self-hosted or VPC, SSO/SAML/SCIM) | free source-available CLI, your keys; no published hosted prices as of 2026-10-07 | free, early access | free, GitHub Sponsors funded, enterprise offerings conditional | free, self-hosted | free open-source engine to self-host; cloud and on-prem without published prices as of 2026-10-07 |
| Born | 2026-07-10 | 2026-06-28 | 2025-12-26 | 2026-07-16 | 2026-01-14 | 2026-08-02 | 2025-05-07 |
| Stars | about 110 | about 100 | about 1.1k | about 490 | about 6.2k | about 950 | about 7.7k |

## Reading the matrix

**The loop-owner row is the whole category in one glance**: SSSF and Fluent move the loop into code (Python ADWs, a Rust scheduler), SuperPlane's platform and Loki Mode's engine own it as a product, while HAR coordinates a fleet but leaves each agent free to edit, which is why its acceptance is verify-focused rather than loop-owned.
A factory is defined by determinism, and HAR earns its place through deterministic verification rather than deterministic sequencing.

**The isolation row is where the category separates from a single long agent call**: Fluent and HAR isolate every candidate in its own worktree, SSSF deliberately runs on the current branch with no sandbox or merge step, the gap its own note names first, and the two newest columns leave isolation undocumented or unverified.

**The self-improvement row is still a two-horse race: Fluent writes reusable Expertise after accepted changes, and Ouroboros refines specs and accumulates assets across a budgeted evolution loop, while SSSF, HAR, Machinist, and Loki Mode stay static and SuperPlane only re-scores its intake.**
The difference is what compounds: Fluent compounds lessons about the code, Ouroboros compounds the specification itself.

**The hidden-grading row is Ouroboros' claim to a distinct cell: it is the only member that structurally withholds the grading command and expected result from the worker agent, an anti-reward-hacking design none of the others attempt.**

**The narrow columns are candid**: SSSF's pi-only dependency versus the open agent matrix of Fluent and HAR is the single biggest reason to look past the founding member's headline ease.
Ouroboros runs the other direction with 14 runtimes, the widest agent boundary in the category, paid for in evaluation tokens and beta churn.
**Machinist narrows the boundary in the other direction: its named-command entrypoint is the category's strictest agent interface, paid for with no built-in isolation and restart-from-zero failure semantics.**

**The pattern has independent practitioner validation beyond this category's tools.**
Will Larson's Imprint runs a Linear-project factory loop in production and finds it compounds only when the surrounding pieces exist: one source of task state, metric access, and a harness that works without a laptop.
The term's AI-era origin traces, by Larson's own attribution, to Justin McCarthy's February 2026 StrongDM essay, which describes the same bet from the inside: specs and scenarios drive agents, and no human writes or reviews the code.

**The rejected long tail**: agentic-software-factory (1 star, inflated agent counts), ai-factory (4 stars, no license), and Takk8IS/software-factory (0 stars, no license) did not clear the citation or credibility bar and are named here so no future run re-adds them silently.
The 2026-10-07 entrant scan resolved the topic's previously untracked candidates too: the AgentField family (SWE-AF at 1,030 stars and CodeAF at 296 stars, one in public beta and one in early preview on the AgentField platform) stays out on a scope call for the owner, whether a platform family gets a column, mirroring retrieval's Haystack precedent; Finn-loop (319 stars, dormant since 2026-07-23) is a three-skill Linear recipe rather than a loop-owning factory, addyosmani/factory (222 stars) is a dormant reference demo, mitkox/esf (187 stars) is an 18-day-old fork of this category's own Machinist, and lago-morph/software-factory (1 star, no license, dormant since 2026-06-08) closes the tail.

## Choosing from the matrix

- Want the easiest code-owned loop on a single agent and will wire your own gates: Super Simple Software Factory.
- Want a self-improving factory with a real final Tester and worktree isolation, pre-1.0 accepted: Fluent.
- Want a fleet of coding agents on one repo with deterministic verification and evidence, keeping your agents: HAR.
- Want a local, auditable runner with a strict named-command boundary around any agent CLI, early-access accepted: Machinist.
- Want vague briefs turned into verified code with the grading hidden from the worker, 14 runtimes and beta churn accepted: Ouroboros.
- Want an autonomous local issue-to-PR loop with an offline-checkable receipt, source-available licensing accepted: Loki Mode.
- Want the whole intake-to-PR line owned by a platform with durable runs and confidence-gated backlog intake: SuperPlane.

## Changes

- 2026-08-29 - Created as a single-column scaffold for SSSF when the Software factory category was seeded.
- 2026-08-29 - Rebuilt to three columns (SSSF, Fluent, HAR) with the who-owns-the-loop thesis.
- 2026-08-30 - Extended to four columns with Ouroboros, self-improvement and hidden-grading prose updated.
- 2026-08-30 - Re-sorted columns alphabetically with Fluent first, dropping the founding-member-first convention.
- 2026-09-05 - Extended from four to five columns with Machinist.
- 2026-09-13 - Added the Pricing row, recording HAR HQ's first published pricing (Team $400 per month up to 50 users with $100 monthly cloud credits, Enterprise custom) alongside the free open-source core.
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-25 - Refreshed the HAR (about 95, after v1.14.3) and Machinist (about 460) star cells.
- 2026-09-27 - Refreshed the SSSF star cell (about 900).
- 2026-09-29 - Refreshed the Machinist star cell (about 470); all other cells re-verified unchanged.
- 2026-10-02 - Refreshed the star cells (Fluent about 110, Machinist about 480, Ouroboros about 6.2k, SSSF about 920); HAR and all other cells re-verified unchanged.
- 2026-10-06 - Added the independent-practitioner paragraph grounding the loop-owner thesis (Will Larson's production factory loop, Justin McCarthy's term-origin essay) with two references; refreshed the Machinist and SSSF star cells.
- 2026-10-07 - Extended from five to seven columns with SuperPlane and Loki Mode, re-sorted alphabetically; recorded the 2026-10-07 entrant-scan resolutions in the long-tail paragraph; all previous cells re-verified unchanged.

## See also

- [Code Factories: Factorio](../../../code-factories-factorio/index.md) - the corpus metaphor this category turns into a tool taxonomy
- [Hybrid Execution Feature Matrix](../../hybrid-execution/hybrid-execution-feature-matrix/index.md) - the deterministic-orchestrates-LLM principle at the structured-output layer
- [Spec-driven Development Feature Matrix](../../spec-driven-development/spec-driven-development-feature-matrix/index.md) - the spec-first competitor to a full pipeline
- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the single coding agents these factories coordinate
- [Executions Feature Matrix](../../executions/executions-feature-matrix/index.md) - scheduled and event-triggered runs versus an invoked factory

## References

- https://github.com/disler/super-simple-software-factory - the founding column: architecture, envelopes, gates, and trace
- https://github.com/disler/super-simple-software-factory/tree/example - the stamped demo repo with real traces
- https://github.com/mrinalwadhwa/fluent - the Fluent column: scheduler, Tester, and Expertise loop
- https://github.com/os-factory/har - the HAR column: the .har contract, worktree isolation, and verify stage
- https://github.com/os-factory/har/releases - the release cadence grounding HAR's row
- https://github.com/owainlewis/machinist - the Machinist column: named commands, executors, recording, license
- https://github.com/Q00/ouroboros - the Ouroboros column: the loop, the three-stage gate, and the hidden-grading design
- https://github.com/asklokesh/loki-mode - the Loki Mode column: the delivery contract, review council, and Evidence Receipt
- https://github.com/superplanehq/superplane - the SuperPlane column: work orders, automation lines, and durable runs
- https://ouroboros.page/learn/en/evaluate/ - the gate stages and consensus triggers grounding the acceptance row
- https://lethain.com/software-factory-experiment/ - Will Larson's production factory loop, the independent practitioner validation of the compounding claim
- https://factory.strongdm.ai/ - Justin McCarthy's February 2026 essay, the term's origin and the spec-plus-scenario loop grounding the thesis
