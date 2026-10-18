---
title: Strands Decider 2B
created: 2026-10-12
updated: 2026-10-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights]
readability: 3
audience_notes: >
  Engineers tracking who ships the decision-model contract as a vendor product, and whether a hyperscaler-backed open checkpoint is worth a slot beside the community fine-tunes.
  Assumes you know what a LoRA adapter and a Brier score are, and have read this category's Jev note.
---

Strands Decider 2B is the Strands Agents team's Apache-2.0 decision model, a 2B LoRA-plus-pointer readout on Qwen3.5 that answers choice, score, and yes/no questions with calibrated confidence in one pass, shipped with a pip CLI and positioned as the decision component for agentic workflows built on the Strands Agents SDK.

**This is the wave's second company-built open checkpoint, and the first from a hyperscaler's agent team, and it arrives with the strongest self-run evaluation culture in the category and the weakest third-party result: the seed tables and calibration contract are published to a standard nobody else matches, while the one independent board that has measured it ranks it 135th of 174.**

## What it is

A small decision model in this category's standard pattern: a state and typed questions go in, one probability per option comes out, no generated text.
The released checkpoint, `strands-decider-2B-qwen3.5-v1-2610` on Hugging Face, is a rank-48 adapter plus a readout head trained on a 246,678-row mix whose builders describe every source family, drop the 20,000 rows whose terms restrict commercial use, and use an Apache-2.0 Gemma 4 teacher with Claude only as an independent row filter whose text never enters the data.
The v1 line is not one model: the same 2026-10-09 release shipped four Gemma 4 siblings (E2B, E4B, 12B, and a 26B-A4B, each the same pointer head on `google/gemma-4-*-it` bases, every one a three-run soup), with per-model self-run tables reading 180 to 207 right of the 231 JevBench public items and 29.78 to 48.69 against the Decision Index's public suite, and the training configs of all five v1 releases were published under `configs/v1` on 2026-10-16.
The v1 checkpoint is a soup of three training runs (the per-layer mean of three seeds' LoRA updates with stacked heads), anchored to the previous release with a KL term so answers do not drift.
Serving is a pip CLI (`pip install strands-decider`, PyPI 0.1.0) with CPU, CUDA, MPS, and MLX extras, MLX running 1.4 to 1.6x faster than MPS on Apple silicon per the README.
It comes from strands-labs, the org behind the Strands Agents SDK, an AWS-backed agent framework, and the README positions the model as a natural fit for decisions inside workflows built on that SDK.

## Status

Active and fresh: the repository was created 2026-09-29 and pushed 2026-10-16, with 636 stars as of 2026-10-15 and 89 forks as of 2026-10-18, and the Hugging Face checkpoint was published 2026-10-09 with 7 likes, its download counter still not tracking (GitHub and Hugging Face APIs).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=strands-labs/strands-decider&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=strands-labs/strands-decider&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=strands-labs/strands-decider&type=date&legend=top-left" />
</picture>

The launch post (2026-10-07) drew a 285-point Show HN thread, above the bar most of this wave cleared, and the tone was warmer than most decision-model threads: early commenters reported on-device deployments rather than methodology fights, one running it in a browser extension to filter email.
The self-run evidence is unusually disciplined: evaluation/results.md publishes per-seed tables next to the soup's numbers (JevBench public items 180 of 231 tasks right, Brier 0.280, ECE 0.072, HotpotQA 0.832 never trained on), states that the training-data builders are not yet on `main` so the data cannot be rebuilt from the repository, and dates every measurement.
The headline reliability claim is a confidence contract: on short classification tasks it has never seen, answers at confidence 0.9 or higher are right about 95 percent of the time, with "confirm or ask a person" below that, which is the deployment logic the calibrated-probability columns all promise.
The one independent reading so far is adverse: the Decision Index 0.3.2 board (regenerated 2026-10-16, 174 configurations) scores strands-decider-2b at 21.34, rank 135, against hosted Jev's 61.53 at thirteenth, while the project's own balanced-skill self-run reads 30.82, and JevBench carries no row for any Strands checkpoint yet.

## Strengths

- **The evaluation culture is the strongest in the category: per-seed results beside the released soup, a KL anchor to the previous release, held-out sets named with their train-split relationships disclosed, and a calibration contract stated as a number you can act on.**
- Vendor standing is concrete: the Strands Agents SDK is one of the major agent frameworks, and a decision model shipped as its native component is the distribution path the H2O note predicted would crowd the individuals.
- The data mix is documented past what most of the wave publishes, including the commercially restricted rows it removed and the teacher-versus-filter roles of the two LLMs.
- Small enough for CPU and Apple-silicon serving with a pip one-liner, which keeps the deployment story inside processes no GPU touches.

## Cautions

- **The only third-party reading is near the bottom of the board: 21.34 against Jev's 60.11 on the Decision Index, with no JevBench row yet, so the calibration contract is self-run until a second board confirms it.**
- 600 stars, a checkpoint too new for download counts, and an adverse board row make this the weakest traction of any admitted entry in this wave; the thread's warmth has not yet become deployments at scale.
- The training configs of all five v1 releases landed under `configs/v1` on 2026-10-16, but the data builders themselves are still not on `main`, so the one thing the results tables imply you could check, the data, cannot be rebuilt from the repository yet.
- The project is tied to the Strands SDK's roadmap, and the README's own framing ("an experimental typed classifier" on PyPI) keeps expectations deliberately low.

## Pricing

Pricing does not apply: Apache-2.0 code and weights, a free PyPI package, and no hosted service.
The cost is your own hardware, and the 2B size keeps that small.

## Compared to

- [Jev](../jev/index.md): the closed original whose published numbers this model's self-run tables use as yardsticks; Jev keeps the latency and the SLA, Strands Decider ships inspectable weights with a calibration contract.
- [Decider](../decider/index.md): the open family with the widest checkpoint range, whose 31B ranks fifth on the Decision Index where Strands' 2B ranks 135th; choose Decider for measured accuracy across budgets, Strands Decider for the eval discipline and the SDK tie-in.
- [H2O-Lightning-4B](../h2o-lightning-4b/index.md): the other company-built open checkpoint, measured first on the board that has not measured this one; the two are the test case for whether vendors or individuals populate this category.

## Bottom line

**Recommended for engineers inside the Strands ecosystem who want a local, calibrated decision component with published per-seed evidence, and for anyone studying how a vendor should disclose a training run.**
Not as a measured engine today: one adverse third-party reading and no second board row.
The disagreeable claim I will defend: the fair comparison is not with the community fine-tunes but with the vendor APIs, and Strands Decider is the first open artifact whose confidence contract is stated precisely enough to be falsifiable, which is worth more than the 60 points of Decision Index score separating it from Jev.

## Changes

- 2026-10-12 - Created from the entrant scan (HN and release-feed sweep), accepted on the 285-point thread, AWS Strands team standing, and the published seed-level evaluation culture, with the adverse Decision Index reading recorded as the governing caution.
- 2026-10-13 - The Decision Index 0.3.2 relabel and second same-day regeneration (149 configurations) moved the adverse reading from 21.75, rank 107, to 21.34, rank 111; refreshed stars to 600 and the pushed date to 2026-10-12.
- 2026-10-15 - The Decision Index's 2026-10-14 regeneration (166 configurations) held the score at 21.34 while moving the rank from 111 to 127; refreshed stars to 636, forks to 85, and the pushed date to 2026-10-14.
- 2026-10-18 - Volatile re-verification surfaced the release's full extent and recorded it: the v1 line shipped five checkpoints on 2026-10-09, the 2B Qwen3.5 measured here plus four Gemma 4 siblings (E2B, E4B, 12B, 26B-A4B on `google/gemma-4-*-it` bases) carrying self-run tables the note had not mentioned, and the training configs of all five were published under `configs/v1` on 2026-10-16 (the data builders remain off `main`); the Decision Index's 2026-10-16 regeneration (174 configurations) moved the unchanged 21.34 from rank 127 to 135 and Jev's reading to the 1.14 row at 61.53, the pushed date moved to 2026-10-16 (an evaluate/serving consistency fix and the config publication), and the checkpoint's likes refreshed to 7.

## See also

- [Jev](../jev/index.md) - the closed contract this model reimplements openly and self-measures against
- [Decider](../decider/index.md) - the open family measured beside it on the Decision Index, 64.62 versus 21.34
- [H2O-Lightning-4B](../h2o-lightning-4b/index.md) - the other vendor-built open checkpoint in the wave
- [Kev](../kev/index.md) - the pre-registered-eval precedent this project's seed tables most resemble
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/strands-labs/strands-decider - repository: Apache-2.0, created 2026-09-29, 636 stars as of 2026-10-15, 89 forks, pushed 2026-10-16, the CLI surfaces and device extras (GitHub API and README, as of 2026-10-18)
- https://github.com/strands-labs/strands-decider/tree/main/configs/v1 - the training configs of the five v1 releases, published 2026-10-16 (fetched 2026-10-18)
- https://strandsagents.com/blog/introducing-strands-decider/ - the launch post: the decision-model positioning, the confidence contract, and the SDK tie-in (fetched 2026-10-12)
- https://raw.githubusercontent.com/strands-labs/strands-decider/main/evaluation/results.md - the seed tables, the soup design, the KL anchor, the data-mix disclosure, the Gemma 4 v1 section, and the not-yet-rebuilt-data statement (re-fetched 2026-10-18)
- https://huggingface.co/StrandsAgents/strands-decider-2B-qwen3.5-v1-2610 - the checkpoint: Apache-2.0, published 2026-10-09, 7 likes, downloads not yet tracked, one of five v1 checkpoints in the org (Hugging Face API, as of 2026-10-18)
- https://news.ycombinator.com/item?id=49987076 - the 285-point launch thread (2026-10-07, fetched via the Algolia items API), its on-device deployment reports the early traction evidence
- https://huggingface.co/spaces/multimodalart/jev-decision-index/resolve/main/data/v03.json - the Decision Index 0.3.2 board scoring strands-decider-2b at 21.34, rank 135 of 174 (generated 2026-10-16, fetched 2026-10-18)
- https://pypi.org/project/strands-decider/ - the package, 0.1.0, self-described as an experimental typed classifier (re-fetched 2026-10-18)
