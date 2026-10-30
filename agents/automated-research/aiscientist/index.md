---
title: AiScientist
created: 2026-10-11
updated: 2026-10-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, machine-learning-engineering, paper-reproduction, multi-agent, open-source]
readability: 3
audience_notes: >
  Engineers comparing long-horizon ML research agents and coordination protocols, and anyone confused by the name's collision with Sakana's AI Scientist.
  Assumes you know what PaperBench-style paper reproduction asks of a system.
---

AiScientist is AweAI's artifact-mediated research lab for long-horizon ML engineering: a hierarchical agent team that coordinates through File-as-Bus, treating the workspace's files rather than chat messages as the system of record, with a paper track that reproduces published work and an MLE track that pushes a metric across 24-hour runs.

**It is the only member here whose unit of work is the reproduction, and its coordination claim (thin control over thick state) attacks the failure the other multi-agent columns leave implicit, context loss across long runs, while its name guarantees it will be mistaken for Sakana's AI Scientist in every search.**

## What it is

A Python system (github.com/AweAI-Team/AiScientist, MIT, initial public release 2026-04-13) described in the April 2026 paper "Toward Autonomous Long-Horizon Engineering for ML Research" (arXiv 2604.13018) by Guoxin Chen, Jie Chen, Lei Chen, and coauthors including Renmin University's Wayne Xin Zhao and Ji-Rong Wen.
The `paper` workflow takes a paper's markdown or bundle plus a GPU and time budget and drives the full reproduction loop: reading, planning, implementing, experimenting, debugging, and final self-check.
The `mle` workflow takes an ML task and runs repeated implementation-and-experiment cycles that improve the target metric, with the README's example trajectory showing 78 experiment cycles in a 24-hour autonomous run.
Benchmark integrations sit in the repository under MLE-bench and frontier-evals (PaperBench).

## Status

Dormant after a short public life: 146 stars, 12 forks, created 2026-03-30, last pushed 2026-07-21, as of 2026-10-28.
A search for the name surfaces Sakana's AI Scientist and unrelated name-alikes; this project has no visible Hacker News footprint as of 2026-10-28.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=AweAI-Team/AiScientist&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=AweAI-Team/AiScientist&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=AweAI-Team/AiScientist&type=date&legend=top-left" />
</picture>

## Strengths

- File-as-Bus is a testable coordination thesis: agents preserve decision-relevant state in workspace files across roles and invocations instead of compressing progress into conversation.
- The paper track targets reproduction, the deliverable the rest of the idea-to-paper sub-family skips in favor of new papers.
- The paper claims improvement over the strongest matched baselines on PaperBench, with the benchmark integration public in the repository.
- MIT license and a documented disk layout (what lands on the workspace) keep runs inspectable.

## Cautions

- Dormant since July 2026 after roughly four months of public development, with 146 stars and no independent coverage this run's searches could find.
- The benchmark claims are the project's own runs, self-scored on PaperBench and MLE-Bench configurations it integrated itself.
- The name collides with Sakana's far better-known AI Scientist, which buries discoverability for any query an autocomplete renders as "AI scientist".
- The 78-cycle, 24-hour headline is a single trajectory the README presents without an ablation.

## Pricing

Free and open source under MIT; there is no paid tier, so pricing does not apply.
Costs are your own GPUs (the workflows take explicit GPU and time budgets) and LLM API calls.

## Compared to

- [Sakana AI Scientist](../sakana-ai-scientist/index.md): the name it will be confused with; Sakana's system writes new papers while AiScientist reproduces existing ones, and only AiScientist is MIT-licensed.
- [AIDE ML](../aide-ml/index.md): the metric-judged tree search; AiScientist's MLE track is the long-horizon, hierarchically orchestrated variant of the same objective.
- [CORAL](../coral/index.md): the other coordination-first member; CORAL isolates the judge from the agents while AiScientist makes the filesystem the coordination medium.

## Bottom line

**Recommended reading for the File-as-Bus coordination argument and as the sub-family's reproduction-track data point, both preserved in the arXiv paper despite the repository's dormancy.**
Not for production use: the repository has been dormant since July 2026 and the benchmark claims have no independent check.

## Changes

- 2026-10-11 - Created.
- 2026-10-29 - Rotation re-verification: all five references re-fetched, no drift; the repository stands dormant since July 2026 with the name collision unchanged.

## See also

- [Sakana AI Scientist](../sakana-ai-scientist/index.md) - the name collision and the new-papers-versus-reproductions contrast
- [CORAL](../coral/index.md) - the other coordination-first system in the category
- [AIDE ML](../aide-ml/index.md) - the metric-judged ancestor of the MLE track
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/AweAI-Team/AiScientist - repository, MIT license, 146 stars, last push 2026-07-21 (as of 2026-10-28)
- https://raw.githubusercontent.com/AweAI-Team/AiScientist/main/README.md - File-as-Bus, the paper and MLE tracks, the 24-hour 78-cycle trajectory, and the release dates (fetched 200, 2026-10-28)
- https://arxiv.org/abs/2604.13018 - the paper: authors, thin control over thick state, and the PaperBench improvement claim (fetched 200 via the arXiv API, 2026-10-28)
- https://api.github.com/repos/AweAI-Team/AiScientist/contents/benchmark - the MLE-bench and frontier-evals (PaperBench) integration directories (fetched 200, 2026-10-28)
- https://hn.algolia.com/api/v1/search?query=AiScientist - the search surfacing Sakana collision results and name-alikes, no footprint for this project (fetched 200, 2026-10-28)
