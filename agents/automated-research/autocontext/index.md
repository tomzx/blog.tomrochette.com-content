---
title: AutoContext
created: 2026-10-14
updated: 2026-10-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, self-improvement, context-bundles, eval-gated-promotion, open-source]
readability: 3
audience_notes: >
  Engineers who run agents against measurable tasks and want the improvement loop itself governed, plus researchers comparing promotion gates across self-improving harnesses.
  Assumes you know what a dev and holdout split and an A/B trial are.
---

AutoContext is Grey Haven's Apache-2.0 recursive self-improvement harness that runs your task against an evaluator, keeps the lessons that measurably helped, and serves them back to the next run.

**AutoContext is the member that turns the keep-or-revert gate into an audited promotion pipeline: nothing its own agents write reaches the next run's prompt or model until matched trials, a held-out lane, and a replayed comparison say it helped.**

## What it is

A Python and TypeScript CLI (`autoctx`, PyPI `autocontext`, npm `autoctx`) from Grey Haven LLC, an applied AI venture studio, with a Pi extension, an MCP server, and a TUI.
Give it a goal or a saved scenario and it drives an agent from Anthropic, OpenAI-compatible, OpenRouter, Claude Code, Codex, Pi, or your own vLLM, Ollama, or MLX endpoint through generations scored by the scenario's evaluator, keeping the useful lessons and discarding the rest.
The kept lessons are context bundles, immutable manifests of playbook, hints, routing, and validation state whose components each carry a SHA-256 digest, promoted only through an outcome-gated pipeline under a campaign false-promotion budget.
The `train` surface closes the loop's second leg: it distills verifier-scored trajectories into a LoRA adapter that the next run auto-resolves and serves, and kernel-evolution studies extend the same evidence discipline to GPU-kernel work.

## Status

Active and early: 1,309 stars, 115 forks, five contributors, created 2026-02-11, repository last pushed 2026-10-21 off the main branch, whose newest commit remains 2026-09-29, as of 2026-10-21.
Jay Scambler wrote 2,144 of the repository's roughly 2,209 commits, and Grey Haven markets itself as an applied AI venture studio.
The train is live: 35 PyPI releases through 0.18.0 (2026-09-16) and 46 npm versions through 0.19.0 (2026-09-28), with the docs site's changelog last updated 2026-08-26.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=greyhaven-ai/autocontext&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=greyhaven-ai/autocontext&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=greyhaven-ai/autocontext&type=date&legend=top-left" />
</picture>

The community footprint is the thinnest in the category for the star count: this run's searches found one Hacker News story, from 2026-03-14, at 2 points with zero comments, and no substantive third-party coverage.

## Strengths

- The promotion gate is the category's most machined: eight requirements from matched screening through compare-and-swap, rejected and inconclusive results persisted as an immutable negative-result ledger, and every promotion recording candidate, incumbent, evaluator epoch, policy digest, and rollback target.
- The training leg closes end to end: the project's case study trains a LoRA on verifier-scored strategies and the next run auto-serves it without a hardcoded model path.
- The project grades its own ambition down: the same case study reports the multi-generation bootstrap gain at +7.4 percent, far below the curated-elite single step, and the README states its archived reuse studies do not authorize production promotion.
- It ships as installable surfaces (PyPI, npm, a Pi extension, MCP, a TUI) rather than a paper's companion repository.

## Cautions

- Every published number is the project's own, measured on its own scenarios such as grid_ctf with a 0.5-billion-parameter base model and its own verifier; this run's searches found no independent replication.
- The README pins PyPI `autocontext==0.19.1`, which does not resolve as of 2026-10-14 (PyPI's latest is 0.18.0), and the npm train runs a minor version ahead of Python's.
- One contributor accounts for nearly all of the code, a bus factor of one beside the institutional columns in this category.
- The gates trust the evaluator epoch, fixtures, and digests you configure; a weak or leaky evaluator gives the machinery noise to promote.
- 1,308 stars against two points of Hacker News discussion is a reach-to-engagement gap worth watching.

## Pricing

Free and open source under Apache-2.0; there is no paid tier, so pricing does not apply.
Costs are your own model API keys or your own GPU (vLLM, Ollama, or MLX for the training leg).

## Compared to

- [Arbor](../arbor/index.md): both gate changes on evidence the loop never optimized against; Arbor withholds held-out data for code merges on a hypothesis tree, AutoContext replays matched context trials under a reserved error budget.
- [Mole](../mole/index.md): both put enforcement inside the loop's contract; Mole's ledger stops a deep-research run at your budget ceiling, AutoContext's false-promotion budget bounds wrong promotions across a whole campaign.
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the keep-or-revert ancestor judged by the validation curve; AutoContext is the industrial descendant where the keep decision is an eight-step pipeline with receipts.

## Bottom line

**Recommended for engineers who already run agents against a measurable evaluator and want their loop's context and training promotions governed by trials that replay and receipts that persist.**
Not for anyone expecting independently verified performance claims, and not as a judged research-output system, since its published numbers are all self-measured as of 2026-10-14.

## Changes

- 2026-10-14 - Created.

## See also

- [Arbor](../arbor/index.md) - the held-out merge gate cousin for code changes
- [Mole](../mole/index.md) - the other enforcement-inside-the-loop column, budget instead of trials
- [Kapso](../kapso/index.md) - the campaign framework banking evaluator-priced lessons between runs
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the keep-or-revert ancestor
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/greyhaven-ai/autocontext - repository metadata: Apache-2.0, Python, 1,309 stars, 115 forks, created 2026-02-11, last push 2026-10-21 off main (fetched 200, 2026-10-21)
- https://raw.githubusercontent.com/greyhaven-ai/autocontext/main/README.md - the loop definition, surfaces table, provider matrix, install pins, and what's-new section (fetched 200, 2026-10-14)
- https://raw.githubusercontent.com/greyhaven-ai/autocontext/main/docs/context-bundles.md - the bundle lifecycle, the eight promotion requirements, the false-promotion budget, and the negative-result ledger (fetched 200, 2026-10-14)
- https://raw.githubusercontent.com/greyhaven-ai/autocontext/main/autocontext/docs/case-study-recursive-loop.md - the closed-loop case study and its self-reported +41.9 percent and +7.4 percent figures (fetched 200, 2026-10-14)
- https://autocontext.ai/docs - the documentation site (fetched 200, 2026-10-14)
- https://autocontext.ai/docs/changelog - the changelog with the August 26 registry-status table (fetched 200, 2026-10-14)
- https://pypi.org/pypi/autocontext/json - 35 releases, latest 0.18.0 on 2026-09-16; the README's 0.19.1 pin returned 404 (fetched 200 and 404, 2026-10-14)
- https://registry.npmjs.org/autoctx - 46 versions, latest 0.19.0, created 2026-03-12 (fetched 200, 2026-10-14)
- https://api.github.com/repos/greyhaven-ai/autocontext/contributors - five contributors with jayscambler at 2,144 commits (fetched 200, 2026-10-14)
- https://api.github.com/orgs/greyhaven-ai - the organization: Grey Haven, applied AI engineering, greyhaven.ai (fetched 200, 2026-10-14)
- https://hn.algolia.com/api/v1/items/47372119 - the lone Hacker News story, 2 points, zero comments, 2026-03-14 (fetched 200, 2026-10-14)
