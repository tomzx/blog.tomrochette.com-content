---
title: Valen
created: 2026-10-13
updated: 2026-10-27
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
The Hugging Face org carries the three model cards, the training and evaluation datasets, and a live demo Space; ONNX and GGUF exports landed 2026-10-13, a documentation site with a web chat and a free hosted decision API followed on 2026-10-21, and by 2026-10-25/26 the export story matured into refreshed modular ONNX variants per size with Python, JavaScript, and C++ SDKs over ONNX Runtime (CPU, CUDA, and a browser WebGPU path) plus qualified F32/Q8_0 GGUFs in all three sizes that run on Valen's own custom CPU runtime, with unmodified llama.cpp and Ollama support explicitly not claimed.
The README reports results on VisualDecisionBench and a game-evaluation set, with the Jev lineage anchor (the typesafe.ai System One post) cited directly.

## Status

Very young and actively shipping: 777 stars, 85 forks, and 1 open issue as of 2026-10-27, created 2026-09-23, pushed 2026-10-27 (docs-only commits since the 10-26 GGUF qualification), with the weights, datasets, demo, and export builds all public.
On 2026-10-24 the serving story consolidated into dual inference protocols: the SGLang and vLLM images and plugins expose both `/v1/systemone` and `/v1/decisions` from the same decision head.
On 2026-10-25 and 10-26 the local-deployment story broadened: refreshed modular ONNX variants for all three sizes with Python (v0.2.0), JavaScript, and C++ SDKs over ONNX Runtime, and qualified F32/Q8_0 GGUFs running on Valen's custom CPU runtime with pinned, verified model downloads, where unmodified llama.cpp and Ollama support is explicitly not claimed.
On 2026-10-21 the project shipped a documentation site with a web chat and a free hosted decision API requiring no key (api.valen-team.workers.dev, predicate, choice, and score questions; higher quotas by email approval), and on 2026-10-18 it released JevalKit (github.com/Valen-Team/JevalKit, Apache-2.0), an evaluation toolkit for Jev-like decision models with a Hugging Face leaderboard Space.
On 2026-10-22 the repository added a validated vLLM serving plugin and deployment guides (a pinned candidate container for GPU validation, vLLM image startup commands in both READMEs), extending the serving story beyond the ONNX and GGUF exports.
On 2026-10-16 the repository added a public Decision Index adapter and reproduction guides: `evaluation/decision_index` wraps the official Decision Index reproduction kit (pinned to revision f5a6e4f, frozen suite 0.3, verified before any model loads), making Valen the first Jev-family member to ship a first-party adapter to that protocol; the board's 0.4.1 edition now carries three Valen rows, Valen-4B 132nd at 37.57, Valen-2B 177th at 22.20, and Valen-0.8B 194th at 16.55 (230 configurations after the 2026-10-26 regeneration).
**The footprint is the thinnest in its family: a single 2-point Hacker News post and no third-party coverage found, so every quality claim is currently the team's own.**
The 0-open-issue count reflects age, not maturity.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Liuziyu77/Valen&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Liuziyu77/Valen&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Liuziyu77/Valen&type=date&legend=top-left" />
</picture>

## Strengths

- Full-pipeline openness: training code, data, benchmarks, and exported weights are all published, which is the preconditions for actually verifying a decision model.
- The first-party JevalKit toolkit and its leaderboard give the family a reusable measurement harness instead of one-off benchmark scripts.
- Vision extends the Jev pattern to the cases that need it (screenshots, documents, video frames) at 0.8B to 4B scale.
- The experimental RLCD stage beyond SFT is published rather than hidden, warts included.
- Export builds (ONNX, GGUF) make deployment boring at the small end: modular ONNX variants run through the Python, JavaScript, and C++ SDKs (CPU, CUDA, browser WebGPU), and the GGUFs run through the project's own CPU runtime, though the GGUF path is not stock llama.cpp.
- The first-party Decision Index adapter means its scores on that board's protocol can be reproduced from the repository itself, not just asserted.
- Apache-2.0 with no API dependency, so the decision layer cannot be revoked by a vendor.

## Cautions

- Every benchmark number is self-reported on self-built benchmarks (VisualDecisionBench, Valen-Eval-Game), with no independent evaluation found.
- Three weeks old at verification with one maintainer team and a single 2-point HN post; treat the project as a pre-adoption artifact.
- RLCD is labeled experimental by the authors themselves, so the training recipe's stability is unproven.
- The Jev family's known weakness (calibration drift outside the training distribution) applies with no published out-of-distribution numbers.
- Probabilities out means no schema enforcement: the caller owns validation, the opposite of this category's structured-output columns.

## Pricing

Free to start in every mode: Apache-2.0 code and weights with no API dependency, a free hosted decision API requiring no key (api.valen-team.workers.dev, three question types, higher quotas by email approval), and local serving through vLLM or SGLang images and plugins at your own compute cost, which at 0.8B to 4B is small.
No paid tier exists as of 2026-10-24; the hosted endpoint's terms beyond the email-approval quota are unpublished.

## Compared to

- [H2O-Lightning-4B](../h2o-lightning-4b/index.md): the family's established open-weights member with a longer track record; Valen adds vision and the full training pipeline.
- [Strands Decider 2B](../strands-decider-2b/index.md): AWS's decision model with the better-published training discipline; Valen matches the openness and adds multimodality at a smaller scale.
- [Jev](../jev/index.md): the original closed System One model whose pattern Valen replicates openly.

## Bottom line

**Recommended for engineers who want a small multimodal decision model they can audit, retrain, and run locally, and who will validate it on their own data.**
Not for production routing without independent evaluation, or for anyone needing schema-enforced tool calls from the decision layer itself.

## Changes

- 2026-10-13 - Created.
- 2026-10-17 - Volatile re-verification after the 2026-10-16 push: recorded the public Decision Index adapter and reproduction guides (evaluation/decision_index, the official kit pinned at f5a6e4f, frozen suite 0.3), the first first-party adapter to that protocol in the Jev family; strengths updated.
- 2026-10-22 - Volatile re-verification after the 2026-10-22 pushes: recorded the validated vLLM serving plugin and deployment guides (a pinned candidate container for GPU validation, vLLM image startup commands in both READMEs); pushed date moved to 2026-10-22.
- 2026-10-24 - Volatile re-verification after the 2026-10-23/24 pushes: recorded the serving surface consolidating into dual inference protocols (`/v1/systemone` and `/v1/decisions` from the same decision head on the SGLang and vLLM images and plugins), the 2026-10-21 documentation site with web chat and a free no-key hosted decision API (the Pricing section rewritten, the "no hosted tier" statement retired), the 2026-10-18 JevalKit evaluation toolkit and leaderboard, and the 0.4.1 Decision Index board now carrying three Valen rows (4B 131st at 37.57, 2B 176th, 0.8B 193rd); pushed date moved to 2026-10-24.
- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Volatile re-verification after the 2026-10-25/26 pushes: recorded the refreshed modular ONNX variants per size with Python (v0.2.0), JavaScript, and C++ SDKs over ONNX Runtime (CPU, CUDA, browser WebGPU), and the qualified F32/Q8_0 GGUFs in all three sizes running on Valen's custom CPU runtime with pinned, verified downloads, where unmodified llama.cpp and Ollama support is explicitly not claimed; the export-build strength reworded; the star-history chart's light source corrected (it wrongly carried the dark-theme parameter); pushed date moved to 2026-10-26.
- 2026-10-27 - Out-of-rotation re-fetch at the drift signal: the Decision Index's 2026-10-26 regeneration (230 configurations) crowd-shifted the three Valen rows one place each at unchanged scores (4B 131st to 132nd, 2B 176th to 177th, 0.8B 193rd to 194th), and the repository's pushed date moved to 2026-10-27 on docs-only commits; forks refreshed to 85; fetched and re-cited.

## See also

- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins
- [H2O-Lightning-4B](../h2o-lightning-4b/index.md) - the established open-weights decision model
- [Strands Decider 2B](../strands-decider-2b/index.md) - the AWS decision model with published training discipline
- [Jev](../jev/index.md) - the lineage original
- [JevBench](../jevbench/index.md) - the board where decision models get scored

## References

- https://github.com/Liuziyu77/Valen - repository, Apache-2.0 license, stars, push activity, and the training-and-eval structure as of 2026-10-27 (pushed 2026-10-27 on docs-only commits; README re-fetched 2026-10-27 with its news list)
- https://github.com/Valen-Team/JevalKit - the first-party evaluation toolkit: Apache-2.0, created 2026-10-16, unified model interfaces and prepared evaluation datasets (GitHub API, as of 2026-10-24)
- https://huggingface.co/spaces/Valen-Team/JevalKit-Leaderboard - the JevalKit leaderboard Space (fetched 2026-10-24)
- https://valen-team.github.io/ - the documentation site and web chat, with the free-API and quota statements (fetched 2026-10-24)
- https://github.com/Liuziyu77/Valen/blob/main/evaluation/decision_index/README.md - the Decision Index adapter guide: official kit pinned at f5a6e4f, frozen suite 0.3, suite verification before model load (fetched 2026-10-17)
- https://huggingface.co/Valen-Team - the Hugging Face org holding the three model cards and datasets
- https://huggingface.co/Valen-Team/Valen-4B - the flagship model card with usage and reported results
- https://huggingface.co/datasets/Valen-Team/VisualDecisionBench - the published evaluation set behind the benchmark claims
- https://huggingface.co/spaces/yuhangzang/Valen-Preview-0923 - the live demo Space
- https://typesafe.ai/blog/introducing-system-one-models-and-jev - the System One and Jev lineage post the README cites
- https://news.ycombinator.com/item?id=49838068 - the single 2-point HN post, the recorded thin community footprint
