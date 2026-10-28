---
title: Evo
created: 2026-10-28
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, autoresearch, tree-search, gates, open-source]
readability: 3
audience_notes: >
  Engineers who want the keep-or-revert loop pointed at their own codebase, and researchers comparing gate designs across self-improving harnesses.
  Assumes you know what a git worktree and a benchmark score floor are.
---

Evo is evo-hq's Apache-2.0 autoresearch orchestrator that turns a codebase into a tree-searched experiment loop: a discover pass figures out what to measure, and an optimize pass runs parallel coding-agent subagents in git worktrees toward that benchmark, keeping gains and discarding gate failures.

**Evo is the member whose judge is built before the loop starts: the discover pass instruments the benchmark and attaches a held-out score-floor gate by default, so the tree search optimizes against a measurement and a correctness bar it did not choose mid-run.**

## What it is

A Python package (evo-hq-cli on PyPI, v0.8.0) installed as a plugin for Claude Code, Codex, Cursor, Kimi, OpenClaw, Hermes, OpenCode, or Pi, authored by Alok Kumar Bishoyi under the evo-hq organization, with a Zenodo DOI and a named debt to Karpathy's autoresearch, which the README calls a pure hill climb that evo extends.
Two commands run the loop: `/evo:discover` explores the repository, asks what to optimize, and creates the benchmark plus gates against unintended changes, and `/evo:optimize` starts the loop, sizing each round to the benchmark's resource profile.
The search is a tree, not a single branch: subagents fork from any committed node in their own worktrees, read shared state (failure traces, annotations, discarded hypotheses), and frontier strategies (argmax, top_k, epsilon_greedy, softmax, and a GEPA-inspired pareto_per_task) pick which branch extends next.
Gates are pass-fail commands that run on every experiment and discard failures even when the score beats the current best, and RLM-inspired scan subagents read trace batches between rounds, surfacing compound failure patterns into shared state.
Experiments run in local worktrees or on SSH hosts, Modal, E2B, Daytona, AWS, or Azure backends, watched from a local dashboard on 127.0.0.1.

## Status

Young and shipping: 1,487 stars, 115 forks, 38 open issues and pull requests, created 2026-04-05, last pushed 2026-10-05, v0.8.0 the latest tag and PyPI release, as of 2026-10-28.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=evo-hq/evo&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=evo-hq/evo&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=evo-hq/evo&type=date&legend=top-left" />
</picture>

The footprint is thin: a single Hacker News thread from April 15, 2026, at 2 points with zero comments, and this run's searches found no independent evaluation or third-party coverage of any kind.
The company surface has already moved: evo-hq.com and its beta funnel now front EVO Router (RouterPlus), an LLM-inference-routing product, so the platform access the README advertises leads to the router business today.

## Strengths

- The discovered gate is the design point: discover builds the benchmark and attaches a held-out score-floor gate automatically, answering the return-a-constant and trade-correctness-for-speed failures the README names itself.
- Tree search with declared frontier strategies makes the exploration policy inspectable and tunable instead of emergent.
- Shared state across worktree subagents (traces, annotations, discarded hypotheses) attacks the repeat-failure problem parallel searches have.
- The surface is broad and legible: eight host harnesses, seven execution backends, a dashboard, and an update train with lockstep version pins between CLI, skills, and hooks.

## Cautions

- Every number is the project's own: no independent replication, benchmark table, or third-party measurement surfaced in this run's searches, and the launch footprint is one zero-comment thread.
- The judge is written by the same system that optimizes against it: discover decides what to measure, so a mis-specified benchmark or a leaky held-out slice is exactly what the loop will exploit.
- Gates are opt-in when the benchmark already exists in the repository, so ungated runs keep the failure mode the gates exist to block.
- The vendor's attention has moved to EVO Router, the inference-routing product its site and beta funnel now front, leaving the loop's own commercial continuation unclear as of 2026-10-28.
- One named author and seven months of history is a bus factor of one beside the institutional columns in this category.

## Pricing

Free and open source under Apache-2.0; there is no paid tier, so pricing does not apply.
Costs are your own model subscriptions (the loop drives eight host harnesses) and your compute, local or on the cloud backends.
The company's beta funnel prices EVO Router, the LLM-routing product, not evo.

## Compared to

- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the cited ancestor, a pure hill climb on one branch against a fixed metric; evo adds forking tree search, parallel subagents, and a benchmark the tool discovers itself.
- [AutoKernel](../autokernel/index.md): the domain-bound sibling whose bench.py is fixed and supplied; evo generalizes to any codebase at the cost of trusting the discovery pass.
- [Arbor](../arbor/index.md): the held-out merge gate on a persistent hypothesis tree; evo's gates discard inside the loop and its tree lives per target rather than across campaigns.

## Bottom line

**Recommended for engineers with a codebase, a measurable target, and the discipline to review what discover chose to measure before trusting what optimize found.**
Not for anyone needing an independently validated loop or a vendor committed to it: the footprint is one zero-comment thread and the company fronts a router now, as of 2026-10-28.

## Changes

- 2026-10-28 - Created.

## See also

- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the ancestor evo cites and extends
- [AutoKernel](../autokernel/index.md) - the fixed-benchmark sibling in the same family
- [Arbor](../arbor/index.md) - the held-out-gate cousin for hypothesis trees
- [AutoContext](../autocontext/index.md) - the promotion-gated sibling with declared policies
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/evo-hq/evo - repository and README: the two commands, tree search, frontier strategies, gates, backends, hosts, telemetry, and the CITATION.cff attribution (fetched via the API, 2026-10-28)
- https://api.github.com/repos/evo-hq/evo - repository metadata: Apache-2.0, 1,487 stars, 115 forks, created 2026-04-05, last push 2026-10-05, v0.8.0 the newest tag (fetched 200, 2026-10-28)
- https://pypi.org/pypi/evo-hq-cli/json - package version 0.8.0, Apache-2.0 license, Python 3.10-plus requirement (fetched 200, 2026-10-28)
- https://news.ycombinator.com/item?id=47780457 - the lone launch thread: 2 points, zero comments, April 15, 2026 (fetched via the Algolia API, 2026-10-28)
- https://evo-hq.com - the company site, now fronting RouterPlus, an LLM-inference-routing product (fetched 200, 2026-10-28)
- https://evo-hq.com/beta - the beta funnel, now titled Request access to EVO Router (fetched 200, 2026-10-28)
- https://doi.org/10.5281/zenodo.20447923 - the Zenodo citation record (fetched 200, 2026-10-28)
