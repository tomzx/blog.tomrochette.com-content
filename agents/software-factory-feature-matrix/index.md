---
title: "Software Factory Feature Matrix"
created: 2026-08-29
updated: 2026-08-30
status: finished
tags: [agent-curated, fully-ai-generated, llm=big-pickle, llm=glm-5.3-flash, comparison, software-factory, agentic-workflows]
readability: 3
audience_notes: >
  Engineers comparing repeatable, code-owned agent pipelines against each other.
  Assumes you know what a phase, an envelope, a gate, a worktree, and a skill are.
---

This matrix compares the members of the Software factory category: repeatable agents-plus-code production pipelines, where deterministic code owns the loop and agents are bounded nodes inside it.
Everything below was verified against live sources on 2026-08-29, with the Ouroboros column verified 2026-08-30.

**The deciding question for this category is who owns the loop: a factory puts phase sequencing, retries, and acceptance in code, and an agent owns only the work inside one bounded phase.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Fluent](../fluent/index.md) | [HAR](../har/index.md) | [Ouroboros](../ouroboros/index.md) | [Super Simple Software Factory](../super-simple-software-factory/index.md) |
| --- | --- | --- | --- | --- |
| Delivery | Rust binary + skill for Codex/Claude Code/Pi, macOS only | CLI + MCP server, npm package | PyPI package + MCP server + Claude Code plugin | one skill (.claude/skills/sssf), stamped into any repo |
| Loop owner | Rust binary owns scheduler, reviewer, tester, learner | deterministic verify stages; agents own their edits | Python orchestrator owns interview, spec, execute, evaluate, evolve | Python ADW scripts (code owns sequencing, retries, acceptance) |
| Agent boundary | Work Items in isolated worktrees, human attention queue | one isolated slot per agent | worker never sees the grading command or expected result | one agent, one named phase at a time |
| Context across seams | Brief, Behavior Specs (EARS), Technical Approach, Plan | .har contract, shared by all agents | immutable Seed spec frozen before any code | typed JSON envelopes, parsed against a schema |
| Acceptance | deterministic final Tester bound to the reviewed commit | deterministic verify with per-commit evidence trail | 3-stage gate: mechanical (70% coverage default), semantic LLM (0.8), consensus on triggers | gates that verify artifacts and tests after the fact |
| Failure handling | resumable Writer correction, fail-closed evidence | per-slot teardown, evidence kept | budgeted evolution, 30-generation cap, stagnation detection | same-session correction, no cold restart |
| Self-improvement | ✓ Learner writes reusable Expertise after each change | ~ plugins and templates reduce drift, no learner | ✓ refines specs and accumulates reusable assets across generations | ✗ none |
| Isolation | ✓ isolated worktree, remote via AWS Fargate | ✓ worktree, ports, and database per slot | ~ delegated to the host runtime | ✗ runs on current branch, no sandbox or merge step |
| Coding agent | Codex, Claude Code, or Pi | Claude Code, Cursor, Codex, or any MCP agent | 13 runtimes, Claude Code through Antigravity | pi only (claude_code stubbed) |
| Trace | Work Item / Attempt record with bound evidence | Mission Control dashboard per run and artifact | event sourcing with full replay and lineage | SQLite, tool calls visible mid-run |
| License | Apache-2.0 | Apache-2.0 | MIT | MIT |
| Born | 2026-07-10 | 2026-06-28 | 2026-01-14 | 2026-08-02 |
| Stars | about 84 | about 82 | about 5,729 | about 764 |

## Reading the matrix

**The loop-owner row is the whole category in one glance**: SSSF and Fluent move the loop into code (Python ADWs, a Rust scheduler) while HAR coordinates a fleet but leaves each agent free to edit, which is why its acceptance is verify-focused rather than loop-owned.
A factory is defined by determinism, and HAR earns its place through deterministic verification rather than deterministic sequencing.

**The isolation row is where the category separates from a single long agent call**: Fluent and HAR isolate every candidate in its own worktree, while SSSF deliberately runs on the current branch with no sandbox or merge step, the gap its own note names first.

**The self-improvement row is now a two-horse race: Fluent writes reusable Expertise after accepted changes, and Ouroboros refines specs and accumulates assets across a budgeted evolution loop, while SSSF and HAR stay deliberately static.**
The difference is what compounds: Fluent compounds lessons about the code, Ouroboros compounds the specification itself.

**The hidden-grading row is Ouroboros' claim to a distinct cell: it is the only member that structurally withholds the grading command and expected result from the worker agent, an anti-reward-hacking design none of the others attempt.**

**The narrow columns are candid**: SSSF's pi-only dependency versus the open agent matrix of Fluent and HAR is the single biggest reason to look past the founding member's headline ease.
Ouroboros runs the other direction with 13 runtimes, the widest agent boundary in the category, paid for in evaluation tokens and beta churn.

**The rejected long tail**: agentic-software-factory (1 star, inflated agent counts), ai-factory (4 stars, no license), and Takk8IS/software-factory (0 stars, no license) did not clear the citation or credibility bar and are named here so no future run re-adds them silently.

## Choosing from the matrix

- Want the easiest code-owned loop on a single agent and will wire your own gates: Super Simple Software Factory.
- Want a self-improving factory with a real final Tester and worktree isolation, pre-1.0 accepted: Fluent.
- Want to run a fleet of coding agents on one repo with deterministic verification and evidence, keeping your agents: HAR.
- Want vague briefs turned into verified code with the grading hidden from the worker, 13 runtimes and beta churn accepted: Ouroboros.

## See also

- [Code Factories: Factorio](../../code-factories-factorio/index.md) - the corpus metaphor this category turns into a tool taxonomy
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the deterministic-orchestrates-LLM principle at the structured-output layer
- [Spec-driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the spec-first competitor to a full pipeline
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the single coding agents these factories coordinate
- [Executions Feature Matrix](../executions-feature-matrix/index.md) - scheduled and event-triggered runs versus an invoked factory

## References

- https://github.com/disler/super-simple-software-factory - the founding column: architecture, envelopes, gates, and trace
- https://github.com/disler/super-simple-software-factory/tree/example - the stamped demo repo with real traces
- https://github.com/mrinalwadhwa/fluent - the Fluent column: scheduler, Tester, and Expertise loop
- https://github.com/os-factory/har - the HAR column: the .har contract, worktree isolation, and verify stage
- https://github.com/os-factory/har/releases - the v1.0.0 release grounding HAR's cadence
- https://github.com/Q00/ouroboros - the Ouroboros column: the loop, the three-stage gate, and the hidden-grading design
- https://ouroboros.page/learn/en/evaluate/ - the gate stages and consensus triggers grounding the acceptance row
