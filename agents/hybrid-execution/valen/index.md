---
title: Valen
created: 2026-10-13
updated: 2026-10-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, decision-model, open-weights, multimodal]
readability: 3
audience_notes: >
  Engineers routing cheap structured decisions off large models who want an open-weights, vision-capable option they can retrain themselves.
  Assumes you know what a Jev-family decision model is and what SFT means.
---

Valen is an Apache-2.0 open-weights multimodal decision model in the Jev family: text, images, and video in, candidate probabilities out, shipped as 0.8B, 2B, and 4B checkpoints with the training recipe, general dataset, and evaluation sets published beside them.

**Its angle is reproducibility: it is the first Jev-family member that ships the whole pipeline, training code (SFT plus experimental RLCD), a 100k general dataset, the VisualDecisionBench evaluation, and ONNX and GGUF exports, so the decision layer is something you retrain rather than download and trust.**

## What it is

A training repository plus model family from an independent team, explicitly inspired by the Jev System One model lineage, with vision added: the models read screenshots, documents, and video frames, and emit decision probabilities for routing, gating, and classification calls.
The Hugging Face org carries the three model cards, the training and evaluation datasets, and a live demo Space; ONNX and GGUF releases landed the week of this check, so the models run on modest local hardware and in runtimes beyond PyTorch.
The README reports results on VisualDecisionBench and a game-evaluation set, with the Jev lineage anchor (the typesafe.ai System One post) cited directly.

## Status

Very young and actively shipping: 777 stars, 70 forks, and 1 open issue as of 2026-10-13, created 2026-09-23 and pushed the day of this check, with the weights, datasets, demo, and export builds all public.
**The footprint is the thinnest in its family: a single 2-point Hacker News post and no third-party coverage found, so every quality claim is currently the team's own.**
The 0-open-issue count reflects age, not maturity.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Liuziyu77/Valen&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Liuziyu77/Valen&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Liuziyu77/Valen&type=date&theme=dark&legend=top-left" />
</picture>

## Strengths

- Full-pipeline openness: training code, data, benchmarks, and exported weights are all published, which is the preconditions for actually verifying a decision model.
- Vision extends the Jev pattern to the cases that need it (screenshots, documents, video frames) at 0.8B to 4B scale.
- The experimental RLCD stage beyond SFT is published rather than hidden, warts included.
- Export builds (ONNX, GGUF) make deployment boring: the models run in standard runtimes on small hardware.
- Apache-2.0 with no API dependency, so the decision layer cannot be revoked by a vendor.

## Cautions

- Every benchmark number is self-reported on self-built benchmarks (VisualDecisionBench, Valen-Eval-Game), with no independent evaluation found.
- Three weeks old at verification with one maintainer team and a single 2-point HN post; treat the project as a pre-adoption artifact.
- RLCD is labeled experimental by the authors themselves, so the training recipe's stability is unproven.
- The Jev family's known weakness (calibration drift outside the training distribution) applies with no published out-of-distribution numbers.
- Probabilities out means no schema enforcement: the caller owns validation, the opposite of this category's structured-output columns.

## Pricing

Free and open source under Apache-2.0, weights and all.
No hosted tier; the cost is your own inference compute, which at 0.8B to 4B is small.

## Compared to

- [H2O-Lightning-4B](../h2o-lightning-4b/index.md): the family's established open-weights member with a longer track record; Valen adds vision and the full training pipeline.
- [Strands Decider 2B](../strands-decider-2b/index.md): AWS's decision model with the better-published training discipline; Valen matches the openness and adds multimodality at a smaller scale.
- [Jev](../jev/index.md): the original closed System One model whose pattern Valen replicates openly.

## Bottom line

**Recommended for engineers who want a small multimodal decision model they can audit, retrain, and run locally, and who will validate it on their own data.**
Not for production routing without independent evaluation, or for anyone needing schema-enforced tool calls from the decision layer itself.

## Changes

- 2026-10-13 - Created.

## See also

- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins
- [H2O-Lightning-4B](../h2o-lightning-4b/index.md) - the established open-weights decision model
- [Strands Decider 2B](../strands-decider-2b/index.md) - the AWS decision model with published training discipline
- [Jev](../jev/index.md) - the lineage original
- [JevBench](../jevbench/index.md) - the board where decision models get scored

## References

- https://github.com/Liuziyu77/Valen - repository, Apache-2.0 license, stars, push activity, and the training-and-eval structure as of 2026-10-13
- https://huggingface.co/Valen-Team - the Hugging Face org holding the three model cards and datasets
- https://huggingface.co/Valen-Team/Valen-4B - the flagship model card with usage and reported results
- https://huggingface.co/datasets/Valen-Team/VisualDecisionBench - the published evaluation set behind the benchmark claims
- https://huggingface.co/spaces/yuhangzang/Valen-Preview-0923 - the live demo Space
- https://typesafe.ai/blog/introducing-system-one-models-and-jev - the System One and Jev lineage post the README cites
- https://news.ycombinator.com/item?id=49838068 - the single 2-point HN post, the recorded thin community footprint
