---
title: "HAR"
created: 2026-08-29
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=big-pickle, llm=glm-5.3-flash, software-factory, harness, multi-agent, worktrees]
readability: 3
audience_notes: >
  Engineers who run fleets of coding agents on one repo and want deterministic verification and proof of what ran.
  Assumes you know what a worktree, a harness, and an MCP server are.
---

HAR, the open agent harness from os-factory, is a CLI and MCP server that turns a repository into isolated per-agent worktrees with deterministic launch, verify, and teardown stages, so a fleet of coding agents can work concurrently and reviewers trust the output.
Facts below verified as of 2026-09-02.

## What it is

An Apache-2.0 TypeScript tool, installed via `npm install -g @osfactory/har`, that scaffolds a machine-readable `.har/` contract into any repo naming its stack, scripts, and checks.
Each task gets an isolated slot: its own worktree, branch, ports, and database.
A deterministic verify stage runs the project's real checks and records evidence, logs, artifacts, and a validated tree hash per commit, and Mission Control is the bundled local dashboard.
It is harness-agnostic and works with Claude Code, Cursor, Codex, or any MCP-capable agent.

## Status

Active and shipping fast: 84 stars and 10 forks since creation on 2026-06-28, 374 commits, and v1.7.0 released 2026-09-01 (v1.0.0 landed 2026-08-28), with releases landing almost daily and the last main push on 2026-09-01 per the GitHub API as of 2026-09-02.
It carries a code of conduct, security policy, and a sponsor (Kerno, a runtime code tester for coding agents), which is a steadier footprint than the category's usual single-commit repo.

## Strengths

- **One repo contract replaces the scattered run knowledge**: a README, CLAUDE.md, Cursor rules, and CI yaml become one `.har/` that any agent reads the same way.
- **Real concurrency**: each slot gets its own worktree, ports, and database, so agents no longer collide on shared dev servers or git state.
- **Proof, not self-report**: every task runs the same deterministic verify and leaves an evidence trail, because verification passes are tied to the exact code that was checked.
- **Portable away from vendor lock-in**: because the contract lives in the repo as an open standard, switching coding agents does not mean rebuilding the verification setup.

## Cautions

- **It runs alongside a coding agent rather than replacing it**: HAR coordinates and verifies a fleet, but the agents themselves are the harnesses you already pay for, so it is a layer, not a factory that owns the whole loop like Fluent.
- **Young at 84 stars**, though daily releases through v1.7.0 signal momentum, not abandonment.
- **The deterministic verify is only as strong as your contract**: a `.har/` that ships placeholder checks is theater, the same trap as the placeholder gates elsewhere in this category.
- **It depends on the ecosystem staying open**: its value rests on a portable contract and MCP support holding across vendors in a landscape that keeps consolidating.

## Pricing

Apache-2.0, free, installable from npm with no license cost.
You bring the coding agents and their subscriptions, and Mission Control runs locally on your machine.
There is no paid tier and no hosted cloud.

## Compared to

- [Super Simple Software Factory](../super-simple-software-factory/index.md) stamps a Python loop into the repo and owns phases and gates in code; HAR is harness-side, isolating and verifying a fleet around a repo contract rather than stamping a single loop.
- [Fluent](../fluent/index.md) adds a deterministic final Tester and a self-improvement learning loop on top of worktree isolation; HAR provides the isolation and verification but delegates the reviewing and learning to its agents.
- [Harnesses](../harness-feature-matrix/index.md) are the single coding agents (Claude Code, Codex) that HAR coordinates; this category is the fleet-and-factory layer above them.

## Bottom line

Recommended for teams running several coding agents on one repository who want concurrent work, deterministic verification, and an evidence trail without rewriting their agent setup.
Not for a solo developer doing one agent at a time, where the harness alone is simpler than the fleet machinery.

## See also

- [Super Simple Software Factory](../super-simple-software-factory/index.md) - the founding member this harness-style factory is read against
- [Fluent](../fluent/index.md) - the self-improving factory that also owns the full loop
- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - the category matrix HAR now fills a column in
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the single coding agents a HAR fleet coordinates
- [Code Factories: Wow](../../code-factories-wow/index.md) - the corpus metaphor this category scales toward

## References

- https://github.com/os-factory/har - the repo, the `.har/` contract, and the verify-and-evidence model
- https://harproject.dev - the documentation covering concepts, verification, MCP tools, and Mission Control
- https://youtu.be/XKl4ZzWy7mQ - the introductory demo of the harness
- https://github.com/os-factory/har/releases - the release cadence, v1.0.0 through v1.4.0
- https://kerno.io - the sponsor that tests runtime code for coding agents, grounding the verification emphasis
