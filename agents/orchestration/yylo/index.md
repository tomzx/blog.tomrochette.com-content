---
title: YYLO
created: 2026-10-21
updated: 2026-10-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, workflows, git-worktrees, evidence]
readability: 3
audience_notes: >
  Engineers who want coding-agent work delegated as bounded tasks with proof: evidence receipts,
  validation at finish, and protected merges, all state kept in Git. Assumes you already run
  at least one agent CLI and read changelogs before upgrading.
---

YYLO is an MIT, npm-distributed CLI that coordinates coding agents through a typed task lifecycle: each task records one bounded outcome, runs in its own worktree with session provenance preserved, passes delivery verification at finish, and lands through a merge under Git expected-old-ref protection, with task and kanban state kept in a separate Git-native ledger.

**YYLO's bet is that agent work needs receipts: a task is not done because the agent said so, but because tests, evidence, and a protected merge say so.**

## What it is

A three-layer, open-source system from JUNO AI INC.
The control plane is the YYLO CLI (`@yylo/cli` 0.2.12 on npm, with equivalent `yylo` and `yy` launchers), which delegates bounded work to agents such as Pi and Codex, preserves each attempt's worktree, model, and session provenance, and validates candidates before integration.
The engineering memory is YYLO Ledger (`yylo-ledger` 0.4.0 on PyPI), a Git-native store of tasks, records, receipts, and archives with a shell-friendly CLI, so task truth lives in the repository instead of a database.
The evaluation layer is YYLO Benchmark, which retains cases, delegates independent attempts, and reports separate check results and judge assessments against frozen checklist criteria.
The lifecycle is deliberately strict: `yy task finish` enforces admission and validation, the merge keeps ownership and conflict protection under expected-ref semantics, historical attempts are preserved and never auto-replayed, and the watch/status commands are read-only observers, because, in the changelog's own words, missing evidence is not success.
Eight independently versioned Skills teach agents the procedures for ledger records, planning, bounded delivery, and benchmark checklists.

## Status

Alive, tiny, and version-young: 65 stars and 11 forks as of 2026-10-21, repository created 2026-01-06 with default-branch pushes through 2026-10-17; npm serves `@yylo/cli` 0.2.12 while the GitHub releases page stops at 0.2.1-rc.14, so the train moved to npm, and the CLI pins the Ledger exactly (0.2.9 requires Ledger 0.4.0) (GitHub API, npm, and the Ledger README, as of 2026-10-21).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=yylo-dev/yylo&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=yylo-dev/yylo&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=yylo-dev/yylo&type=date&legend=top-left" />
</picture>

No independent coverage exists: no HN thread and no third-party write-up found as of 2026-10-21.
**The README carries 55-plus awesome-list badges, mostly from small lists, which is curated reach without engagement, and the nine months of history are the only evidence there is.**

## Strengths

- The bounded-task contract (one outcome, constraints, dependencies) plus evidence receipts makes agent work inspectable and stoppable at defined gates.
- Merge land under expected-old-ref protection is a genuine concurrency guard, rare at this layer of the category.
- The Ledger is Git-native, so task truth, dependencies, and receipts survive in the repository and review like code.
- The Benchmark layer turns attempts into comparable, retained evaluation evidence, with judge assessments separated from deterministic checks.
- Multi-agent by design: work routes to Pi, Codex, and other agents while session provenance stays attached.

## Cautions

- 65 stars and zero independent coverage; the badge wall is self-curated, not adoption.
- Exact-version pins across layers (the CLI admits exactly one Ledger version) make upgrades an all-or-nothing dance.
- The ecosystem is three repositories at 65, 1, and 2 stars: every layer is one maintainer's bet.
- 0.2.x with breaking changelog entries (autonomous run/resume refused without dispatch, watch demoted to read-only).
- The company behind it (JUNO AI INC.) has no public funding record this note could find.

## Pricing

Free and open source: the CLI is MIT, and the Ledger and Benchmark are MIT as well.
No hosted tier and no paid plan found (as of 2026-10-21).

## Compared to

- [Crewplane](../crewplane/index.md): both make the workflow the durable artifact; Crewplane renders each stage to disk as Markdown, while YYLO enforces a task lifecycle with validation and merge protection.
- [Worktrunk](../worktrunk/index.md): owns the worktree lifecycle with hooks; YYLO adds task state, evidence, and protected merges on top of the worktree it creates per task.
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md): the adversarial answer to worker overconfidence; YYLO's verification is checklist- and evidence-based rather than worker-versus-worker.

## Bottom line

Recommended for solo engineers who want bounded, receipt-backed agent tasks with protected merges and a Git-native paper trail.
Not for teams wanting a GUI, and not without tolerance for 0.2.x churn and exact-pin upgrades.

## Changes

- 2026-10-21 - Created.

- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart markup (the light source carried the dark-theme parameter; the theme parameter now sits only on the dark source).

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Crewplane](../crewplane/index.md) - the Markdown-workflow runner in the same process-as-artifact seat
- [Worktrunk](../worktrunk/index.md) - the worktree lifecycle YYLO builds its task isolation on
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md) - the adversarial alternative to evidence-based verification
- [Bernstein](../bernstein/index.md) - the deterministic-scheduler governance layer with the same trust-the-artifact instinct

## References

- https://api.github.com/repos/yylo-dev/yylo - repository, license, counts, and dates (as of 2026-10-21)
- https://yylo.dev/ - the three-layer system, per-layer versions, and the product-direction disclaimers
- https://yylo.dev/docs/ - the documentation index and the ecosystem procedures
- https://raw.githubusercontent.com/yylo-dev/yylo/main/CHANGELOG.md - the breaking 0.2.x boundary and the read-only watch rule
- https://registry.npmjs.org/@yylo/cli/latest - npm 0.2.12, the launchers, and the MIT license
- https://api.github.com/repos/yylo-dev/yylo/releases - the GitHub release train stopping at 0.2.1-rc.14
- https://raw.githubusercontent.com/yylo-dev/yylo-ledger/main/README.md - the Git-native Ledger contract and the exact-version pin
