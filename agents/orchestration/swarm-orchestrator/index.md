---
title: Swarm Orchestrator
created: 2026-10-24
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, coding-agent, evidence, git-worktrees]
readability: 3
audience_notes: >
  Engineers who want an autonomous coding agent whose success claims carry tamper-evident
  receipts rather than model narration, and who accept solo-maintainer tooling and a
  command-line surface. Assumes you know what a git worktree and a test gate are.
---

Swarm Orchestrator is a free, ISC-licensed npm CLI (Node 24+) that runs coding-agent loops whose every claim must resolve to machine-captured evidence: edits stay inside a declared file set behind one recording chokepoint, the project's own checks run as sealed gates, retries face a numeric ratchet that forbids trading away tests, and each run exports a signed, hash-chained bundle whose dependency-free verifier anyone can execute offline.

**Its thesis is that a green verdict belongs to the harness, not the model: narrative always renders as unverified prose, and a passing check that cannot be shown able to fail is caught, not counted.**

## What it is

A TypeScript CLI from a solo author, distributed as swarm-orchestrator on npm, that takes a task and a git workspace, plans, declares the files it intends to touch, edits through the chokepoint, and runs your gates.
It drives Anthropic, OpenAI, Google, or local models through Ollama and other OpenAI-compatible servers, with on-machine probing and calibration (swarm select, swarm calibrate) that measures candidate models and a router that picks from the results.
swarm parallel gives each task its own worktree and a merge queue, tries tasks several ways under --redundancy with the winner chosen from measured numbers, and can decompose a --goal into a dependency-checked task graph; workers coordinate by reading each other's ledgers, never by message passing or model text.
The evidence machinery is the product: an append-only, hash-chained ledger under ~/.swarm/sessions, gates whose criteria are sealed before the first model call, bonds that hand each passing gate a file it must refuse, and bundles signed from the OS keychain (the fallback recorded in the manifest) that carry verify.mjs and rederive.mjs so verdicts recompute anywhere.
The verification half now also ships standalone as swarm-verify, with its own release train beside the agent's, reusable against changes from other sources.
The package name has carried four products: Copilot CLI session orchestration, the v11 and v12 pull-request cheat auditor, the v13 coding agent, and now the agent plus verifier split, and the README itself warns that anything below 13 is a different program.

## Status

Active and fast-moving under one maintainer: the repository was created 2026-01-22, held 112 stars, 5 forks, and 5 open issues as of 2026-10-24, was pushed 2026-10-25, and its 1,586 commits all belong to one contributor (GitHub API, as of 2026-10-27).
npm serves 14.4.0 (2026-10-10) as latest while the README still says 13.1.9, and the package drew 672 downloads in the month to 2026-10-22 (npm registry and downloads API, as of 2026-10-24).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=moonrunnerkc/swarm-orchestrator&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=moonrunnerkc/swarm-orchestrator&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=moonrunnerkc/swarm-orchestrator&type=date&legend=top-left" />
</picture>

No independent coverage exists: the only HN sighting is the author's own 1-point Show HN from 2026-03-12 for the pull-request-auditor era, and nothing third-party discusses the current agent.

## Strengths

- The claims discipline is unusual and inspectable: docs/claims.md maps every public claim to a committed artifact and maintains a forbidden-claims list that bans borrowed benchmarks, compliance dates, and unbounded security wording.
- The ratchet and the bonds attack the failure modes this category actually sees: a retry cannot delete tests to go green, and a gate that passes a planted failure is recorded vacuous and blocks the run.
- Bundles verify offline in a clean container, and the repository's nightly CI re-proves the committed evidence bundle alongside the suite.
- Parallel mode is genuine orchestration: per-task worktrees, a merge queue, redundancy ranked by measurement, and planner output checked for cycles and file conflicts before anything runs.
- Local-model choice is measured rather than assumed, with per-machine calibration reports committed under a dated protocol.

## Cautions

- Zero independent coverage and small adoption: 672 npm downloads a month, 112 stars, one contributor.
- Four products have shared the package name, so tutorials, issues, and habits from below v13 describe a different program.
- The README lags the registry (13.1.9 versus 14.4.0), which makes the documentation trail harder to follow than the code.
- Its own Limits section draws the boundary: gates prove mechanical quality, not design quality, and a signed bundle is not correctness.
- Solo-maintainer risk on a fast-churning surface, with breaking majors as the release habit.

## Pricing

Free and open source under ISC; you bring your own model keys or run local models.
No hosted tier and no paid plan found (as of 2026-10-24).

## Compared to

- [YYLO](../yylo/index.md): both trade in bounded tasks and receipts, but YYLO delegates to the CLIs you already run while Swarm Orchestrator brings its own agent loop and models.
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md): both refuse to trust worker self-reports, through adversarial worker-versus-worker refutation there and through harness-computed predicates and bonds here.
- [Bernstein](../bernstein/index.md): both sell replayable, offline-auditable runs; Bernstein removes the LLM from coordination entirely, while Swarm Orchestrator keeps the model in the loop but fences its verdicts.

## Bottom line

Recommended for engineers who want an unattended agent whose green claims arrive with tamper-evident receipts, especially over local models, and who accept solo-maintainer churn.
Not for teams wanting a GUI or supervision of Claude Code and friends, and not for anyone who needs a tool with outside scrutiny.

## Changes

- 2026-10-24 - Created.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [YYLO](../yylo/index.md) - the delegate-to-CLIs counterpart with the same receipts instinct
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md) - the adversarial alternative to evidence gating
- [Bernstein](../bernstein/index.md) - the no-LLM deterministic-scheduler sibling

## References

- https://api.github.com/repos/moonrunnerkc/swarm-orchestrator - repository, license, counts, and dates (as of 2026-10-24)
- https://raw.githubusercontent.com/moonrunnerkc/swarm-orchestrator/main/README.md - the task loop, parallel mode, evidence model, and the v12 boundary
- https://raw.githubusercontent.com/moonrunnerkc/swarm-orchestrator/v13-main/docs/claims.md - the claim-to-artifact table and the forbidden-claims list
- https://registry.npmjs.org/swarm-orchestrator - the version train, dist-tags, and dates
- https://api.npmjs.org/downloads/point/last-month/swarm-orchestrator - the 672-download month to 2026-10-22
- https://api.github.com/repos/moonrunnerkc/swarm-orchestrator/releases - the 14.4.0 train and the swarm-verify split
- https://api.github.com/repos/moonrunnerkc/swarm-orchestrator/contributors - the single-contributor record
- https://hn.algolia.com/api/v1/search?query=swarm-orchestrator&tags=story - the absent footprint and the 1-point Show HN
