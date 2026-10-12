---
title: Karpathy Autoresearch
created: 2026-10-10
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, autoresearch, machine-learning, open-source]
readability: 3
audience_notes: >
  Engineers and researchers tracing where the autonomous research loop came from and what its simplest verified form looks like.
  Assumes you know what a training loss curve and a git branch are.
---

Karpathy Autoresearch is Andrej Karpathy's three-file open-source loop in which an AI coding agent edits a nanochat training script overnight, runs five-minute experiments on a single GPU, and keeps or discards each one on the measured validation loss.

**Autoresearch is the founding artifact of the loop family this category tracks, and its judging rule is the simplest here: the validation curve is the only oracle, so the loop cannot claim a win the measurement did not produce, and its failure mode is overfitting the metric rather than fabricating the result.**

## What it is

A GitHub repository whose working surface is deliberately three files: `prepare.py` (fixed data preparation and evaluation, not modifiable), `train.py` (the single file the agent edits, holding the GPT model, the Muon plus AdamW optimizers, and the training loop), and `program.md` (the instructions the human edits, which Karpathy calls the research-org code).
A run works like this: the agent agrees a run tag, branches `autoresearch/<tag>`, reads the repository, then experiments autonomously, each experiment training for a fixed five minutes on one GPU, with every result appended to a `results.tsv` ledger and kept or reverted on the numbers.
The training target is a simplified single-GPU implementation of Karpathy's nanochat (58,552 stars as of 2026-10-11).
Karpathy announced it in March 2026 with a deliberately mythologizing framing: the repo is "the story of how it all began" for a future where agent swarms run research.

## Status

Dormant as a repository, dominant as an influence: 97,661 stars, 13,566 forks, created 2026-03-06, last push 2026-03-26, no releases and no license file, as of 2026-10-11.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=karpathy/autoresearch&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=karpathy/autoresearch&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=karpathy/autoresearch&type=date&theme=dark&legend=top-left" />
</picture>

The community footprint is the largest in this category: the March 19, 2026 Hacker News thread on scaling it reached 237 points with 94 comments, and the project spawned a dedicated awesome list (created 2026-03-20) that catalogs dozens of descendant skills, ports, and domain adaptations.
The strongest independent test came from SkyPilot (March 18, 2026): pointed at the loop with 16 Kubernetes GPUs, Claude Code submitted about 910 experiments in 8 hours, taught itself to screen ideas on H100s and validate winners on H200s, and moved validation loss from 1.003 to 0.974, a 2.87 percent improvement over baseline.

## Strengths

- The judge cannot be argued with: every experiment's verdict is a measured loss number, the only oracle in this category that no model or vendor mediates.
- The programming surface is Markdown, so the research-org design is legible, diffable, and copyable in a way no harness codebase is.
- It is the smallest complete loop in the category: three files, one GPU, no framework, no API keys.
- The scaling test shows the loop's strategy changes with compute: with 16 GPUs the agent ran factorial waves of 10 to 13 experiments and caught interaction effects that sequential search misses.

## Cautions

- The practitioner critique cuts at ambition, not accuracy: the top scaling-thread replies read the loop as automated hyperparameter tuning at toy scale, "brute-force search, but guided", and note that a two-node cluster is the whole test bed.
- No license file ships with the repository, so reuse beyond reading it sits in unclear legal ground.
- Dormant since 2026-03-26: Karpathy moved on, and the descendants (skills, ports, benchmarks) carry the line rather than the original.
- The fixed five-minute budget bounds what an improvement can mean, and the 2.87 percent cluster result is the vendor's own run, not a replicated one.

## Pricing

Free; the loop costs your own GPU time and model API calls.
There is no paid tier and no license under which to sell it, so pricing does not apply.

## Compared to

- [Agon](../agon/index.md): the producer-critic factory that wraps the loop in adversarial review and aims at papers; Autoresearch is the one-agent keep-or-revert ancestor with the harder oracle.
- [OpenResearch](../openresearch/index.md): the workspace-grade descendant that industrializes the loop on your own agents with git lineage; Autoresearch is the three-file prototype.
- [DeepAnalyze](../deepanalyze/index.md): the trained-model descendant where the loop is learned in the weights rather than prompted in a Markdown file.

## Bottom line

**Recommended as the first loop to read in this category: everything else here descends from it or competes with its structure, and its judge is the one to steal.**
Not for anyone who needs a maintained tool, a license that permits reuse, or research beyond a toy training run.

## Changes

- 2026-10-10 - Created.

## See also

- [Agon](../agon/index.md) - the producer-critic elaboration of the keep-or-revert loop
- [OpenResearch](../openresearch/index.md) - the workspace descendant running the loop on your own agents
- [DeepAnalyze](../deepanalyze/index.md) - the trained-model descendant
- [Andrej Karpathy](../../people-and-publications/andrej-karpathy/index.md) - the author's profile note in this section
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/karpathy/autoresearch - the repository: three-file design, keep-or-revert loop, nanochat base, and the March 2026 framing (fetched 200, 2026-10-10)
- https://api.github.com/repos/karpathy/autoresearch - stars, forks, created and pushed dates, and the no-license status for the as-of line (fetched 200, 2026-10-11)
- https://raw.githubusercontent.com/karpathy/autoresearch/master/program.md - the agent-facing loop definition: branch per run, results.tsv ledger, fixed five-minute budget (fetched 200, 2026-10-10)
- https://blog.skypilot.co/scaling-autoresearch/ - the independent 16-GPU scaling test: about 910 experiments in 8 hours, the H100-screen and H200-validate strategy, 1.003 to 0.974 validation loss (fetched 200, 2026-10-10)
- https://hn.algolia.com/api/v1/items/47442435 - the 237-point, 94-comment scaling thread and its hyperparameter-tuning and brute-force critiques (fetched 200, 2026-10-10)
- https://raw.githubusercontent.com/webfuse-com/awesome-autoresearch/main/README.md - the dedicated descendant list the loop spawned (fetched 200, 2026-10-11)
- https://api.github.com/repos/karpathy/nanochat - the nanochat base and its star count (fetched 200, 2026-10-11)
