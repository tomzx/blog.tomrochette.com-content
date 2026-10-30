---
title: InternAgent
created: 2026-10-29
updated: 2026-10-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, multi-agent, scientific-discovery, open-source]
readability: 3
audience_notes: >
  Engineers comparing lab-built autonomous science frameworks and researchers tracking how benchmark-anchored the claims behind them are.
  Assumes you know what an agentic experiment loop and a leaderboard submission are.
---

InternAgent is Shanghai AI Laboratory's unified agentic framework for long-horizon autonomous scientific discovery: a closed loop that generates hypotheses, plans and executes experiments (computational or wet-lab), verifies the results, and evolves its own approach across scientific domains.

**InternAgent is this category's broadest single loop, twelve research task types from algorithm discovery to paper reproduction in one framework, and its most benchmark-anchored subsystem, but its headline numbers are the lab's own while the one third-party table it appears on ranks it fourth overall.**

## What it is

A Python framework (github.com/InternScience/InternAgent, Apache-2.0, created 2025-05-16 as the rename of NovelSeek) by the InternScience org, the AI for Science group of Shanghai AI Laboratory.
Version 1.0 open-sourced 2025-10-13 covers twelve autonomous research task types from hypothesis generation to automated experiment execution, described in the paper "InternAgent: When Agent Becomes the Scientist" (arXiv 2505.16938, May 2025).
Version 1.5 open-sourced 2026-05-07 adds three core subsystems (Generation, Validation, Evolution), a memory module, autonomous paper reproduction, enhanced algorithm discovery, and deep research, and claims leading scores on GAIA (86.06), GPQA (87.37), HLE, and FrontierScience, with validation in biology, earth science, and material science (technical report, February 2026).
Runs are config-driven and model-agnostic: an OpenRouter gateway, OpenAI-compatible endpoints, or Anthropic keys, with coding agents as experiment backends (`--exp_backend claudecode`) and a self-contained AutoDebug task as the first run.
The lab exposes InternAgent's deep-research pipeline as a public integration endpoint (scphub, since March 2026).

Its solution-optimization subsystem ships separately as [MLEvolve](https://github.com/InternScience/MLEvolve), a Monte Carlo Graph Search agent for Kaggle-style ML engineering built on AutoMLGen, described in its own paper (arXiv 2606.06473, June 2026); the line continued on 2026-10-15 with MLExpert, a trained 35B MoE agentic model reporting 72.7 percent on MLE-Bench Lite (arXiv 2610.22344).

## Status

Active at the lab, quiet at the repository: 1,459 stars, 136 forks, created 2025-05-16, last push 2026-07-29 on main, as of 2026-10-29.
The subsystem line carries the current momentum: MLEvolve pushed 2026-10-16 and MLExpert released 2026-10-15, both under the same org.
The subsystem's headline is leaderboard-anchored: MLEvolve's 2026-02-14 submission sits on OpenAI's official MLE-Bench leaderboard at 61.33 percent any-medal (All) over 75 tasks at a 12-hour budget, fourth overall and first among the submissions that publish source code, though the leaderboard has taken no new submissions since April 24, 2026 while its maintainers rework the fairness process.
**The community footprint is absent: a Hacker News search returns no stories for InternAgent, its former NovelSeek name, or MLEvolve as of 2026-10-29, so the 1,459 stars measure a Chinese-language and academic audience, the channel pattern DeepAnalyze and ARIS show.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=InternScience/InternAgent&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=InternScience/InternAgent&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=InternScience/InternAgent&type=date&legend=top-left" />
</picture>

## Strengths

- The breadth is unmatched in the category: one framework spanning hypothesis generation, algorithm discovery, paper reproduction, deep research, and wet-lab empirical discovery, with the 1.5 report claiming workflow compression from weeks to minutes in biology, earth science, and material science.
- The subsystem's claim is third-party anchored: MLEvolve's row sits on OpenAI's own leaderboard with grading reports attached, a stronger anchor than the self-run tables most members publish, and it did so at half the run time of the three proprietary systems above it.
- It runs on infrastructure you already have: config-driven model gateways and coding agents as experiment backends, under Apache-2.0.
- Institutional staying power: the loop survived a rename, two versions, a public deep-research endpoint, and a continued subsystem line even while the main repository went quiet.

## Cautions

- The "#1 on MLE-Bench" claim needs its qualifier: the official leaderboard ranks MLEvolve fourth overall (61.33) behind Famou-Agent 2.0 (64.44), AIBuildAI (63.11), and MARS+ (62.67), and the subsystem's own README reports 65.3 from its paper's runs, a figure that does not match the leaderboard row.
- The 1.5 headline scores (GAIA, GPQA, HLE, FrontierScience) are the lab's own runs, and the wet-lab claims are not reproducible by a reader.
- The main repository has been quiet since July 2026, so the framework's center of gravity has moved to subsystem repositories.
- Zero Hacker News footprint means no independent engineering read on any of the claims exists.
- The leaderboard itself is closed to new submissions while its maintainers rebuild the fairness process, so the ranking is a snapshot, not a live court.

## Pricing

Free and open source under Apache-2.0; there is no paid tier, so pricing does not apply.
Costs are your own model API keys (OpenRouter, OpenAI-compatible, or Anthropic) and your compute; the lab's scphub endpoint exposes the deep-research pipeline separately, with no published prices.

## Compared to

- [Sakana AI Scientist](../sakana-ai-scientist/index.md): the idea-to-paper ancestor; Sakana's loop ends at a manuscript, InternAgent claims the full cycle through executed and verified experiments, including wet labs.
- [AIDE ML](../aide-ml/index.md): the metric-judged tree search ancestor; MLEvolve is the same Kaggle-tier objective with Monte Carlo Graph Search, and the leaderboard row that beats AIDE's entries by decades of medal-rate points.
- [Kapso](../kapso/index.md): the campaign framework whose own leaderboard row (50.67) MLEvolve outranks on the same table; Kapso generalizes beyond benchmarks, MLEvolve specializes in them.

## Bottom line

**Recommended reading for anyone building long-horizon science agents, as the broadest public architecture in the category, and for ML-engineering teams choosing a loop by its only third-party-anchored leaderboard row.**
Not for anyone needing independently verified wet-lab or reasoning-benchmark claims, none of which have a third-party read as of 2026-10-29.

## Changes

- 2026-10-29 - Created as an entrant from the InternScience org scan, with the MLEvolve subsystem folded in and its leaderboard row verified against OpenAI's table.

## See also

- [Sakana AI Scientist](../sakana-ai-scientist/index.md) - the idea-to-paper ancestor InternAgent claims to complete
- [AIDE ML](../aide-ml/index.md) - the tree-search ancestor whose leaderboard rows MLEvolve displaced
- [Kapso](../kapso/index.md) - the rival subsystem on the same MLE-Bench table
- [DeepAnalyze](../deepanalyze/index.md) - the other thin-Western-footprint member, and the trained-model kind MLExpert moves toward
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/InternScience/InternAgent - repository, README, news timeline, and Apache-2.0 license (fetched 200, 2026-10-29)
- https://raw.githubusercontent.com/InternScience/InternAgent/main/README.md - the 1.0 and 1.5 feature sets, the NovelSeek rename, run instructions, and the scphub access note (fetched 200, 2026-10-29)
- https://api.github.com/repos/InternScience/InternAgent - stars, forks, created and pushed dates, and license metadata for the as-of status (fetched 200 via the API, 2026-10-29)
- https://arxiv.org/abs/2505.16938 - the 1.0 paper "InternAgent: When Agent Becomes the Scientist" (fetched 200 via the arXiv API, 2026-10-29)
- https://huggingface.co/papers/2602.08990 - the 1.5 technical report page: the three subsystems, the GAIA/GPQA/HLE/FrontierScience claims, and the wet-lab scope (fetched 200, 2026-10-29)
- https://discovery.intern-ai.org.cn - the project website (fetched 200, 2026-10-29)
- https://raw.githubusercontent.com/InternScience/MLEvolve/main/README.md - the subsystem's MCGS design, the AutoMLGen lineage, and its own 65.3 percent claim (fetched 200, 2026-10-29)
- https://arxiv.org/abs/2606.06473 - the MLEvolve paper "A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery" (fetched 200 via the arXiv API, 2026-10-29)
- https://raw.githubusercontent.com/openai/mle-bench/main/README.md - the official leaderboard rows for MLEvolve (61.33, fourth overall, first with source available), InternAgent's own 2025 submission, Kapso's row, and the closed-submissions notice (fetched 200, 2026-10-29)
- https://internscience.github.io/MLEvolve/ - the subsystem's project page (fetched 200, 2026-10-29)
- https://hn.algolia.com/api/v1/search?query=InternAgent - the zero-story Hacker News footprint, checked also for NovelSeek and MLEvolve (fetched 200, 2026-10-29)
