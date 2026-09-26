---
title: Laya
created: 2026-09-21
updated: 2026-09-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights, multilingual]
readability: 3
audience_notes: >
  Engineers who followed the Jev launch and want to know whether an open, self-hostable decision model already exists, and what the trade-offs are.
  Assumes you know what a classification head and calibrated probabilities are, and ideally have read this category's Jev note.
---

Laya is an Apache-2.0 family of open-weights "System 1" decision models from ConvAI Innovations that answers typed questions (choice, score, noul) over any state in a single forward pass, no text generation, 33 milliseconds per question on a T4, with a router that picks between an English, a multilingual, and a typed-decisions checkpoint.

**Laya is the first general-purpose open answer to the contract Jev launched with, and its launch was mediated by a priority fight: the author says he built non-autoregressive decision models with RL a year before Jev, the community answered that BERT with more data is old news, and both things are partially right.**

## What it is

Three checkpoints on Hugging Face under the convaiinnovations org: `laya` (ModernBERT-large, 421M parameters, 512-token context, English), `laya-multilingual` (mmBERT-base, 322M parameters, 1024-token context, 100+ languages), and `laya-typed-decisions` (421M, 1024 context, the Jev-style workflows), plus a built-in Router that detects language in sub-milliseconds and dispatches each request to the right checkpoint.
The question vocabulary mirrors Jev's primitives: `choice` over enumerated criteria, `score` against a rubric, and `noul`, a 0-1 truth value, all answered with calibrated probabilities in one non-autoregressive pass.
Training uses reinforcement learning against strictly proper scoring rules, the method both this lab and TypeSafe call RLCD, and the models ship as a `pip install laya` package (0.3.20 as of 2026-09-25) rather than a hosted API.
Community runtimes extend it past PyTorch: laya-mlx reports 7-14 ms decisions on an M3 Max, and a CoreML port runs offline on Apple Neural Engine.

## Status

Days old and compounding fast, as of 2026-09-25.
The main repository was created 2026-09-18 and shows about 23,000 stars, laya-mlx about 6,200 since 2026-09-19, with a CoreML port, third-party demo endpoints, and roughly ten community quantizations appearing within days.
The author's launch story, "I built non-autoregressive decision models with RL a year ago" (2026-09-19), drew a 1,350-point Hacker News thread as of 2026-09-25, the largest community footprint of any Jev follow-up, and a follow-up gist thread on running Laya offline on an M4 Mac reached 176 points as of 2026-09-25.
The first independent deployment account landed 2026-09-22: an engineer chose Laya over hosted Jev for local agent routing on a Mac Studio and measured 37 of 40 acceptable decisions on a frozen replay against 33 of 40 for his previous deterministic router, while stating plainly that it was not a Laya-versus-Jev head-to-head.
On the third-party JevBench board Laya's 421M checkpoint ranks low on both readings (54.4 on v1.2, 30.3 on the sealed v1.4 revision) but posts the cheapest cost per 1,000 decisions of any ranked system (about $0.0029), which is the trade its model card already advertised.
The headline comparisons remain self-run, but unusually self-critical: the model card carries an "Honest Limits" section conceding that the base checkpoints score near chance on typed-decisions zero-shot (0.362 against a 0.461 majority-class baseline), that the 0.766 headline belongs to a checkpoint fine-tuned on that benchmark's own training split, and that the models ship over-confident until you fit a temperature on your own data.

## Strengths

- **The no-generation guarantee is inspectable end to end: Apache-2.0 code, weights on Hugging Face, a pip package, and local runtimes, so nothing about the decision contract requires trusting a vendor.**
- Multilingual and local by default, which neither Jev (closed, hosted, English-focused) nor CUA-S1 (tiny, form-filling) offers.
- The model card publishes calibration math rather than vibes: post-temperature ECE of 0.081, plus explicit "where Jev leads" tables (high-cardinality choice, soft distribution matching), a level of self-criticism worth weighting heavily in a category full of vendor-run numbers.
- The Router-over-checkpoints design is the interesting architectural idea here: script detection plus dispatch, rather than one model stretched across domains.
- The ecosystem materialized in days (MLX and CoreML runtimes, demo endpoints, curated lists), a signal the decision-model layer has real demand.

## Cautions

- **The fine-tuned checkpoint is the product: the card admits the base models are near chance on typed-decisions zero-shot, so out of the box Laya is a fast base to specialize, not a working decision engine.**
- **Context and cardinality are the hard limits: 512 to 1024 default tokens per checkpoint against Jev's advertised 32k-plus budget, and on a 77-option question Jev scores 0.870 while Laya scores 0.425 at default settings, both flagged in the HN thread and on the card itself.**
- Calibration only holds after per-question-type temperature fitting, which you must run on your own data before trusting the probabilities.
- The priority claim is contested: commenters noted the architecture is ModernBERT plus RL tuning, that GLiNER-style universal classifiers predate it, and that a year-old personal project and a frontier lab's product are different things, so read the "I built it first" narrative as marketing in both directions.
- Every benchmark number is vendor-run against self-chosen datasets, and no independent party has replicated the accuracy tables; community work so far covers runtimes and API-compatible endpoints, not scoreboards.

## Pricing

Free and open: Apache-2.0 code and weights, no hosted service and no paid tier as of 2026-09-21.
The cost is your own hardware and the engineering to keep three checkpoints plus a router warm.

## Compared to

- [Jev](../jev/index.md): the closed, hosted original with 32k-plus context, parallel evaluation, and unproven subsidy economics; choose Jev for long states and zero ops, Laya for self-hosting, privacy, and languages.
- [CUA-S1](../cua-s1/index.md): the tiny open checkpoint scoped to form filling; CUA-S1 publishes calibration metrics, Laya publishes generality, and both are open brackets on the same closed claim.
- [Outlines](../outlines/index.md): constrained decoding over a general model you serve, the right choice when the decision still needs generated text or grammar coverage Laya's single-pass scorer cannot express.

## Bottom line

**Recommended for engineers who want the Jev-style decision layer running on their own hardware, especially across languages, and who can live inside a 1k-token state.**
Not for long-context states, for audited calibration requirements, or for anyone who needs a vendor SLA today.
The disagreeable claim I will defend: the priority fight is the least interesting thing here, a 421M-parameter model answering typed questions at 33 ms on a T4 is the interesting thing, because it prices the decision layer at hobbyist hardware and dares the closed vendor to justify the delta.

## Changes

- 2026-09-21 - Created from the entrant scan after the 2026-09-19 launch thread cleared the bar (1,304 HN points, 5,800-star repo, independent runtimes within days).
- 2026-09-22 - Recorded the star surge (about 17,800), the 0.3.6 package, the first independent deployment account (astgl.com, chose Laya for local routing with explicit limits), the JevBench third-party reading (54.4 overall, cheapest cost per 1,000 decisions), and refreshed thread counts (1,338 and 173 points).
- 2026-09-25 - Refreshed traction (about 23,000 stars, laya-mlx about 6,200, PyPI 0.3.20, threads 1,350 and 176 points) and recorded the JevBench v1.4 sealed re-scoring (Laya 30.3, from 54.4, still cheapest per 1,000 decisions).

## See also

- [Jev](../jev/index.md) - the closed System One model whose contract Laya open-sources a rival answer to
- [CUA-S1](../cua-s1/index.md) - the other open-weights decision checkpoint, scoped to form filling
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where the planner above a decision layer gets chosen

## References

- https://github.com/NandhaKishorM/laya - repository: Apache-2.0, created 2026-09-18, about 23,000 stars, checkpoint table and Router docs (GitHub API, as of 2026-09-25)
- https://laya.convaiinnovations.com/ - the launch site: 33 ms single-pass and 7.2 ms batched claims, benchmark framing
- https://news.ycombinator.com/item?id=49765348 - the launch thread (1,350 points as of 2026-09-25, 2026-09-19): context-limit, novelty, and GLiNER criticisms
- https://pypi.org/project/laya/ - the package: 0.3.20 as of 2026-09-25 (0.3.6 on 09-22, 0.3.5 on 09-21, 0.3.4 on 09-20)
- https://huggingface.co/convaiinnovations/laya - the primary checkpoint (ModernBERT-large, 421M parameters, 3,396 likes as of 2026-09-25)
- https://github.com/mizorewww/laya-mlx - the MLX runtime: 7-14 ms on M3 Max, about 6,200 stars as of 2026-09-25
- https://news.ycombinator.com/item?id=49777106 - the 176-point offline-Mac thread (2026-09-20) grounding the local-runtimes claim
- https://astgl.com/p/local-laya-vs-hosted-jev-typed-decisions - the independent deployment account: chose Laya for local routing on a Mac Studio, 37/40 versus 33/40 on a frozen replay, explicitly not a Jev head-to-head
