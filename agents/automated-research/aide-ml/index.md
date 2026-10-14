---
title: AIDE ML
created: 2026-10-11
updated: 2026-10-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, machine-learning-engineering, tree-search, open-source]
readability: 3
audience_notes: >
  Engineers comparing metric-judged ML engineering agents and tracing the tree-search mechanism's published origin.
  Assumes you know what a validation metric and a Kaggle competition are.
---

AIDE ML is Weco AI's open-source reference build of the AIDE algorithm, an LLM agent that frames machine learning engineering as tree search over code, drafting, debugging, and benchmarking candidate solutions until a user-defined metric stops improving.

**It is the published ancestor of the metric-judged tree-search mechanism this category's campaign and evolution columns build on: where Karpathy's autoresearch keeps or reverts a single lineage, AIDE explores a tree of candidate solutions and reuses the promising branches, and that distinction is the category's main mechanism split.**

## What it is

A Python package (aideml on PyPI, v0.2.2, MIT) from the February 2025 paper "AIDE: AI-Driven Exploration in the Space of Code" (arXiv 2502.13138) by Zhengyao Jiang, Dominik Schmidt, Dhruv Srikanth, Dixing Xu, Ian Kaplan, Deniss Jacenko, and Yuxiang Wu.
You point it at a dataset and state a goal and a metric; the agent runs trial-and-error as tree search in the space of solutions, strategically reusing and refining promising nodes.
The README positions three layers: the AIDE algorithm (the paper), this repository (the lean research build), and the Weco product (weco.ai), the commercial platform the company built out from it.
The repository description notes AIDE is referenced in OpenAI's MLE-bench.

## Status

Active-adjacent and widely forked: 1,572 stars, 237 forks, created 2024-04-03, last pushed 2026-10-12 (a depth-limit fix in the search loop, its first commit since September 3), as of 2026-10-13.
The Hacker News footprint is nearly absent: the April 2024 launch thread drew 1 point and zero comments, as of 2026-10-11.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=WecoAI/aideml&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=WecoAI/aideml&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=WecoAI/aideml&type=date&legend=top-left" />
</picture>

## Strengths

- The mechanism is the point: greedy tree search with draft, debug, and improve nodes, the design later systems (Kapso's tree-searched campaigns, CORAL's evolution) extend or cite.
- It is the rare member here with an independent head-to-head: Agent Laboratory's site scored AIDE (o1-preview) at two MLE-Bench medals and above-median-human performance on 5 of 10 challenges, against mle-solver's four medals.
- Ships as an installable package with search-tree visualization, built for swapping search heuristics, evaluators, and LLM backends.
- The company behind it is the proof of the mechanism: Weco AI productized the algorithm rather than abandoning it.

## Cautions

- The repository is a reference build, not a product: the README routes production use to the Weco platform, so expect to outgrow the open package.
- One commit landed in the six weeks to October 12 and the package sits at 0.2.2, so development is slow while the MLE-agent space moves.
- Its headline evaluations are the paper's own runs; the independent medal count comes from a competitor's comparison on 10 challenges with o1-preview, a thin slice.
- Zero traction on Hacker News despite 1,568 stars, an unusually developer-silent footprint for a package this forked.

## Pricing

Free and open source under MIT; there is no paid tier in the package, so pricing does not apply.
Costs are your own LLM API calls and compute; the commercial Weco product is priced separately and its prices are not published in this repository.

## Compared to

- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the keep-or-revert single lineage; AIDE is the tree-search generalization where failed branches stay explored rather than reverted.
- [Kapso](../kapso/index.md): the campaign framework that tree-searches coding-agent experiments toward objectives and evaluators; AIDE is the lighter published ancestor with the algorithm paper.
- [Agent Laboratory](../agent-laboratory/index.md): the idea-to-paper system whose mle-solver was measured against AIDE on MLE-Bench medals.

## Bottom line

**Recommended for agent-architecture researchers who want the tree-search MLE mechanism in its published, hackable form, and as the citation anchor for where metric-judged code search began.**
Not for production ML engineering: the README itself routes that to the Weco product, and the open package moves slowly.

## Changes

- 2026-10-11 - Created.
- 2026-10-13 - Recorded the repository's October 12 return (a depth-limit debug-parent fix, its first commit since September 3) and refreshed the counts.

## See also

- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the keep-or-revert counterpart whose single lineage AIDE's tree generalizes
- [Kapso](../kapso/index.md) - the campaign framework extending metric-judged tree search across runs
- [Agent Laboratory](../agent-laboratory/index.md) - the system whose evaluation supplied AIDE's independent medal count
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/WecoAI/aideml - repository, MIT license, 1,568 stars, last push 2026-09-03, MLE-bench reference (as of 2026-10-11)
- https://raw.githubusercontent.com/WecoAI/aideml/main/README.md - the three-layer split (algorithm, reference build, Weco product) and the tree-search description (fetched 200, 2026-10-11)
- https://arxiv.org/abs/2502.13138 - the AIDE paper: authors and the tree-search formulation (fetched 200 via the arXiv API, 2026-10-11)
- https://pypi.org/pypi/aideml/json - the aideml package at version 0.2.2 (fetched 200, 2026-10-11)
- https://agentlaboratory.github.io/ - the independent MLE-Bench medal comparison scoring AIDE at two medals on ten challenges (fetched 200, 2026-10-11)
- https://hn.algolia.com/api/v1/search?query=aideml - the 1-point, zero-comment launch thread from April 2024 (fetched 200, 2026-10-11)
