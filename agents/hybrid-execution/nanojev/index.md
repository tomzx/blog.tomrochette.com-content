---
title: NanoJev
created: 2026-09-21
updated: 2026-09-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights, game-agents]
readability: 3
audience_notes: >
  Engineers who followed the Jev wave and want to know how far a hobby-scale replica of the decision-model contract gets, especially on game and RL tasks.
  Assumes you know what a classification head and an SFT recipe are.
---

NanoJev is an individual developer's MIT-licensed nano replica of Jev: a 0.6B parallel decision model on a Qwen3-0.6B backbone that returns probability distributions over supplied candidates with zero output-token decoding, published end to end with weights, an 18,760-question dataset, and a replayable training pipeline.

**A 0.6B model claims to beat hosted Jev at three of four ViZDoom-family games, and not one of its numbers has been checked by anyone other than the author.**

## What it is

A complete training pipeline in the Jev pattern: a state, a question, and candidates go in, complete probability distributions come out, with Choice running set attention over 2 to 255 candidates, Boolean a sigmoid, and ordered Score a distribution over 2 to 10 levels.
One shared checkpoint handles four game tasks (a 50x50 maze, Snake, ViZDoom Basic aiming, and ViZDoom Predict Position moving-target shots), served by a script exposing `POST /api/evaluate` after loading the model once.
Weights live at C-Tianyu/NanoJev and the mixed-task dataset at C-Tianyu/NanoJev-Data, both downloadable without signing in, pinned to the `unified-games-v1` revision.
The code is MIT, by an individual developer signing as Tianyu (43 GitHub followers), and RLCD post-training sits on the public roadmap rather than in the shipped model, which is plain cross-entropy SFT.

## Status

**Active, six days old, mid-pack among the open replicas by stars, with the smallest community footprint.**
The repository was created 2026-09-17, pushed 2026-09-21, and shows about 2,200 stars and 235 forks as of 2026-09-25.
The weights show about 6,900 downloads and 83 likes, the dataset about 3,900 downloads, as of 2026-09-25.
The author published a follow-up project, JevHarness, for letting an LLM build task-specific decision harnesses with rewards and execution traces.
The Hacker News submission (2026-09-18) sits at 2 points and zero comments, the third-party JevBench board ranks no NanoJev checkpoint, and I found no independent discussion, evaluation, or runtime anywhere; **that silence is itself a signal, and it is why I weight every number below as unreplicated.**

## Strengths

- **The most complete public pipeline of the replica wave: data, checkpoints, replayable evaluation trajectories, and a per-decision simulator replay check, all downloadable without gating.**
- The results document is more rigorous than the README: OOD splits, Wilson intervals, and McNemar tests (Predict Position 27/128 against Jev's 11/128, unadjusted p = 0.009), and it publishes the games where Jev wins (Maze 7/10 against 4/10).
- Zero output-token decoding at 0.6B is the cheapest existence proof in this category that the decision-head trick is not a frontier-lab artifact.

## Cautions

- Every benchmark is self-run on tasks the author chose, against a Jev API whose version and sampling setup only he can confirm, and no independent party has re-run any of it.
- The most-shared evidence, the browser replays, is access-gated (the development site returned 401 when I fetched it), so the flashiest demos are unverifiable.
- The Hugging Face weights carry no license tag as of 2026-09-22 (the code repo is MIT), so the licensing of the weights themselves is ambiguous.
- The headline tables lead with the widest gaps (Basic 128/128 against 56/128) while the weighted totals are nearly level (66.85% against Jev's 65.39%), which is marketing by selection.

## Pricing

Free and open as code (MIT) with public weights and data, no hosted service and no paid tier.
The cost is a CUDA machine and the time to replay the pipeline.

## Compared to

- [Jev](../jev/index.md): the closed original NanoJev benchmarks against on game tasks; Jev has independent calibration work behind it and NanoJev has none.
- [Kev](../kev/index.md): the other trainable replica; kev is API-compatible with TypeSafe's SDK and ships third-party test sets, NanoJev ships games and a bigger star count.
- [CUA-S1](../cua-s1/index.md): the other tiny open checkpoint; both are research artifacts, and CUA-S1 at least publishes calibration metrics on its model card.

## Bottom line

**Recommended for researchers who want a complete, replayable decision-model training pipeline at toy scale, and for nobody shipping anything.**
Not for production decisions, for threshold logic, or for anyone who needs a number a second party has confirmed.
The disagreeable claim I will defend: NanoJev beating hosted Jev at three of four games is exactly the result this category needs someone other than the author to verify, and until that happens the repository is best read as a training-pipeline reference rather than a benchmark result.

## Changes

- 2026-09-21 - Created from the owner-prompted open-alternative scan; accepted on star and download traction with the missing community footprint stated explicitly.
- 2026-09-22 - Refreshed traction counts (about 2,000 stars, about 6,000 weight downloads), recorded the JevHarness follow-up project and the absence of any NanoJev row on the JevBench board, which leaves the benchmark claims unreplicated.
- 2026-09-25 - Refreshed traction counts (about 2,200 stars, about 6,900 weight downloads, the dataset at about 3,900) and corrected the star-ranking claim as Kev and Laya pulled far ahead.

## See also

- [Jev](../jev/index.md) - the closed model NanoJev replicates and benchmarks against
- [Kev](../kev/index.md) - the better-verified trainable replica from the same wave
- [CUA-S1](../cua-s1/index.md) - the other small open checkpoint scoped to one decision class
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/TianyuCodings/NanoJev - repository: MIT, created 2026-09-17, about 2,200 stars, 235 forks (GitHub API, as of 2026-09-25)
- https://raw.githubusercontent.com/TianyuCodings/NanoJev/main/README.md - the four-game claims, dataset scale, and the roadmap with RLCD pending
- https://raw.githubusercontent.com/TianyuCodings/NanoJev/main/docs/SONIC_PREDICT_POSITION_RESULTS.md - the detailed test and OOD tables, including the Maze losses and McNemar p-values
- https://huggingface.co/C-Tianyu/NanoJev - weights: created 2026-09-17, about 6,900 downloads, 83 likes, no license tag (as of 2026-09-25)
- https://huggingface.co/datasets/C-Tianyu/NanoJev-Data - the 18,760-question mixed-task dataset, about 3,900 downloads (as of 2026-09-25)
- https://news.ycombinator.com/item?id=49757421 - the 2-point, zero-comment submission grounding the missing-footprint claim
