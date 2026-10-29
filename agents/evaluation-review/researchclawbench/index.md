---
title: ResearchClawBench
created: 2026-10-28
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation, benchmark, automated-research, ai-for-science]
readability: 3
audience_notes: >
  Engineers tracking whether AI research agents can actually reproduce published science, and teams picking a yardstick for automated-research work.
  Assumes you know what an LLM-as-judge and a rubric are.
---

ResearchClawBench is a benchmark from the AI for Science center of Shanghai AI Laboratory that measures whether AI coding agents can conduct scientific research end to end, scoring their code, figures, and reports against the published paper each task re-discovers.

## What it is

A benchmark plus evaluation harness: 40 official tasks across 10 disciplines (astronomy through physics), each built from a published paper by domain experts who extract the task, write a weighted rubric of text and image items, curate the raw data and related work, and reproduce the result themselves to prove every rubric item is achievable.
Stage 1 hands the agent the workspace and requires code, figures, and a report; stage 2 has a multimodal LLM judge score each rubric item in one of two modes, target optimization for quantitative results (0 to 100 against the paper's own numbers) or diagnostic analysis for reasoning, under strict-by-design prompting that demands evidence for every claim.
The judge model is yours to configure (the README example sets gpt-5.1), the rcb-eval CLI batches runs with the agent model and judge model deliberately separated, and built-in presets cover Claude Code, Codex CLI, OpenClaw, ResearchClaw, Nanobot, EvoScientist, LingTai, ARIS Codex, and the ResearchHarness baseline.
Made by the InternScience organization, MIT licensed for code and dataset, mirrored on Hugging Face and ModelScope, and described in an arXiv paper at v5.

## Status

Active and research-backed: 276 stars, 27 forks, 2 open issues and pull requests as of 2026-10-28, created 2026-03-18, pushed 2026-10-23, 195 commits, with the paper at v5 (2026-07-03) and the newest leaderboard news dated 2026-09-17.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=InternScience/ResearchClawBench&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=InternScience/ResearchClawBench&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=InternScience/ResearchClawBench&type=date&legend=top-left" />
</picture>

The paper's headline (as of v5): the strongest auto-research agent, Claude Code, averages 21.5 and the strongest ResearchHarness LLM, Claude-Opus-4.7, 20.7, so every published entry still sits well below the 50 line that means matching the paper, with InnoClaw 2.0's 34.89 average (second among agents as of 2026-09-17) the best posted since.
**Adoption lives inside the AI-for-Science community, where seven-plus external teams hold leaderboard entries and the Hugging Face mirror carries an official-benchmark model leaderboard, while the broader developer footprint is absent: zero Hacker News stories and zero comments as of 2026-10-28.**

## Strengths

- Tasks grounded in published papers with raw data and human-validated rubrics: experts reproduced each result before any agent ran, so the checklists measure achievable science, not vibes.
- The 50/70 scale reads at a glance (50 means matching the paper, 70 and above surpassing it), and per-item scoring with reasoning shows exactly where a report fell short.
- Dual-mode judging separates quantitative comparison from reasoning quality instead of averaging them into one number.
- A working submission pipeline: community tasks flow through a Hugging Face Space into dataset pull requests (57 rows on the mirror as of 2026-10-28), and external agent results keep landing on the leaderboard.

## Cautions

- The judge is an unvalidated LLM: strict prompting and expert-built rubrics are the controls, but no study checks judge agreement against human reviewers, the exact check MLR-Bench ran and this benchmark has not.
- Leaderboard entries arrive through the maintainers' own pipeline, and the public site is a client-rendered shell a fetcher cannot read, so scores are hard to audit from outside.
- The community footprint is narrow beyond the AI-for-Science scene: no Hacker News presence at all as of 2026-10-28, and the built-in agent list skews toward the OpenClaw ecosystem the benchmark's name comes from.
- Maintenance pace is uneven: the repository last pushed 2026-10-23 and the last announced leaderboard refresh is 2026-09-17, so the site's live-update claim rests on unannounced rebuilds.
- Running it is not free in practice: ResearchHarness batches need search, fetch, and PDF-tool credentials on top of agent and judge tokens.

## Pricing

Not applicable; MIT code and dataset, and a run costs whatever your agent's and judge's tokens cost.

## Compared to

- [MLR-Bench](../mlr-bench/index.md): the other research-agent benchmark in this category; MLR-Bench scores the full arc from idea to paper over 201 workshop tasks with a two-model judge validated against expert reviewers, ResearchClawBench scores raw-data re-discovery of 40 published results with expert rubrics and an unvalidated judge, so choose MLR-Bench for breadth and judge validation, ResearchClawBench for reproduction depth.
- [FrontierHarness Eval](../frontierharness-eval/index.md): the vendor-run benchmark for coding-agent harnesses on engineering tasks; ResearchClawBench measures the same class of agents on science instead.
- [Sakana AI Scientist](../../automated-research/sakana-ai-scientist/index.md): an agent that does autonomous research; ResearchClawBench is the ruler you would measure it and its successors with.

## Bottom line

**Recommended as the yardstick when the question is whether an agent can reproduce published science from raw data, and as the research-agent complement to the engineering-task benchmarks in this category.**
Not for CI gating, and not as a leaderboard to quote at face value while the judge has no human-agreement study and the scores ride the maintainers' own pipeline.

## Changes

- 2026-10-28 - Created.

## See also

- [MLR-Bench](../mlr-bench/index.md) - the validated-judge counterpart scoring the full research arc
- [FrontierHarness Eval](../frontierharness-eval/index.md) - the engineering-task benchmark for the same harnesses
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [Sakana AI Scientist](../../automated-research/sakana-ai-scientist/index.md) - the autonomous-research agent class this benchmark measures

## References

- https://github.com/InternScience/ResearchClawBench - repository and README: task design, two-stage pipeline, rubric modes, agent presets, leaderboard news (as of 2026-10-28)
- https://arxiv.org/abs/2606.07591 - the paper (v5, 2026-07-03): 40 tasks, protocol, headline scores, failure-mode analysis
- https://huggingface.co/datasets/InternScience/ResearchClawBench - the MIT dataset mirror: 57 rows, task schema, official-benchmark model leaderboard
- https://internscience.github.io/ResearchClawBench-Home/ - the leaderboard site (a client-rendered shell to fetchers)
- https://raw.githubusercontent.com/InternScience/ResearchClawBench/main/LICENSE - the MIT license
- https://api.github.com/repos/InternScience/ResearchClawBench - stars, forks, license, created and pushed dates as of 2026-10-28
- https://api.github.com/orgs/InternScience/repos - the InternScience organization, Shanghai AI Laboratory's AI for Science center (InternAgent, SGI-Bench)
- https://hn.algolia.com/api/v1/search?query=ResearchClawBench - the zero-coverage check: no stories or comments as of 2026-10-28
