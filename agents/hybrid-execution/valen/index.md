---
title: Valen
created: 2026-10-13
updated: 2026-11-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, decision-model, open-weights, multimodal]
readability: 3
audience_notes: >
  Engineers routing cheap structured decisions off large models who want an open-weights, vision-capable option they can retrain themselves.
  Assumes you know what a Jev-family decision model is and what SFT means.
---

Valen is an Apache-2.0 open-weights multimodal decision model in the Jev family: text, images, and video in, candidate probabilities out, shipped as five sizes in the Valen-Decision-1.5 generation (0.8B, 2B, 4B, 9B, and 27B) after launching at 0.8B, 2B, and 4B, with the training recipe, general dataset, and evaluation sets published beside them.

**Its angle is reproducibility: it is the first Jev-family member that ships the whole pipeline, training code (SFT plus experimental RLCD), a 100k general dataset, the VisualDecisionBench evaluation, and ONNX and GGUF exports, so the decision layer is something you retrain rather than download and trust.**

## What it is

A training repository plus model family from an independent team, explicitly inspired by the Jev System One model lineage, with vision added: the models read screenshots, documents, and video frames, and emit decision probabilities for routing, gating, and classification calls.
The v0.4.0 release (2026-11-10) opened the second generation, Valen-Decision-1.5, in five sizes: the decision head on Qwen3.5 backends at 0.8B, 2B, 4B, and 9B plus a 27B on Qwen3.8-27B, each with block-bidirectional attention and a bbox grounding head, native weights storing the backbone in BF16 and the decision and grounding heads in FP32, per-size ONNX variants, and per-size F32/Q8_0-plus-vision GGUFs.
The Hugging Face org carries the model cards, the training and evaluation datasets, and a live demo Space; ONNX and GGUF exports landed 2026-10-13, a documentation site with a web chat and a free hosted decision API followed on 2026-10-21, and by 2026-10-25/26 the export story matured into refreshed modular ONNX variants per size with Python, JavaScript, and C++ SDKs over ONNX Runtime (CPU, CUDA, and a browser WebGPU path) plus qualified F32/Q8_0 GGUFs in all three launch sizes that run on Valen's own custom CPU runtime, with unmodified llama.cpp and Ollama support explicitly not claimed.
The README reports results on VisualDecisionBench and a game-evaluation set, with the Jev lineage anchor (the typesafe.ai System One post) cited directly.

## Status

Very young and actively shipping: 777 stars, 85 forks, and 1 open issue as of 2026-10-27, created 2026-09-23, pushed 2026-11-12 (README updates: a playground badge, the 1.5 release post, the Decision Index ranking, and community projects, plus SGLang launch commands pinning bfloat16 and hosted-API bbox documentation), with the repository now under the team's own org (it transferred from Liuziyu77/Valen to Valen-Team/Valen in early November) and the weights, datasets, demo, and export builds all public.
The project tagged its first release on 2026-10-28: v0.3.0 adds a CHANGELOG and a release process, records the valen-sdk 0.2.0 (PyPI) and @valen-team/sdk 0.2.0 (npm) publications, and packages the qualified F32/Q8_0 GGUFs behind the Valen-patched llama.cpp and Ollama builds of a pinned gguf-runtime-v0.1.0 download, with video input available from a source build; the README has since moved to valen-sdk 0.3.0 (2026-10-29) and announced a Valen.llm() LLM comparison and a Valen agent skill, and a Jev-ToM community evaluation joined the documentation on 2026-10-27.
On 2026-11-10 the v0.4.0 release shipped the Valen-Decision-1.5 generation in five sizes with the gguf-runtime-v0.2.0 prebuilt CPU runtime serving it: block attention, noul-rubric folding, text and image input, and bbox questions on image requests through `/v1/systemone` and `/v1/decisions`, with the 1.5 GGUFs (F32, Q8_0, and the vision file) in per-size `Valen-Decision-1.5-<size>-GGUF` repositories and the runtime 0.1.0 GGUFs of Valen-Decision-1.0 still loading.
On 2026-10-24 the serving story consolidated into dual inference protocols: the SGLang and vLLM images and plugins expose both `/v1/systemone` and `/v1/decisions` from the same decision head.
On 2026-10-25 and 10-26 the local-deployment story broadened: refreshed modular ONNX variants for all three sizes with Python (v0.2.0), JavaScript, and C++ SDKs over ONNX Runtime, and qualified F32/Q8_0 GGUFs running on Valen's custom CPU runtime with pinned, verified model downloads, where unmodified llama.cpp and Ollama support is explicitly not claimed.
On 2026-10-21 the project shipped a documentation site with a web chat and a free hosted decision API requiring no key (api.valen-team.workers.dev, predicate, choice, and score questions; higher quotas by email approval), and on 2026-10-18 it released JevalKit (github.com/Valen-Team/JevalKit, Apache-2.0), an evaluation toolkit for Jev-like decision models with a Hugging Face leaderboard Space.
On 2026-10-22 the repository added a validated vLLM serving plugin and deployment guides (a pinned candidate container for GPU validation, vLLM image startup commands in both READMEs), extending the serving story beyond the ONNX and GGUF exports.
On 2026-10-16 the repository added a public Decision Index adapter and reproduction guides: `evaluation/decision_index` wraps the official Decision Index reproduction kit (pinned to revision f5a6e4f, frozen suite 0.3, verified before any model loads), making Valen the first Jev-family member to ship a first-party adapter to that protocol; the board's 2026-11-12 regeneration (301 configurations) replaced the family's 1.0 rows with five Valen-Decision-1.5 rows, the 27B forty-seventh at 65.21, the 9B ninety-eighth at 55.85, the 4B 130th at 49.87, the 2B 181st at 37.97, and the 0.8B 227th at 27.60, so the 1.5 line's 27B now sits above the vendor's Jev 1.14 (sixty-seventh at 60.24) where the 1.0 rows sat far below it.
**The footprint is the thinnest in its family: a single 2-point Hacker News post and no third-party coverage found, so every quality claim is currently the team's own.**
The 0-open-issue count reflects age, not maturity.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Valen-Team/Valen&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Valen-Team/Valen&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Valen-Team/Valen&type=date&legend=top-left" />
</picture>

## Strengths

- Full-pipeline openness: training code, data, benchmarks, and exported weights are all published, which is the preconditions for actually verifying a decision model.
- The first-party JevalKit toolkit and its leaderboard give the family a reusable measurement harness instead of one-off benchmark scripts.
- Vision extends the Jev pattern to the cases that need it (screenshots, documents, video frames) at 0.8B to 27B scale.
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

Free to start in every mode: Apache-2.0 code and weights with no API dependency, a free hosted decision API requiring no key (api.valen-team.workers.dev, three question types, higher quotas by email approval), and local serving through vLLM or SGLang images and plugins at your own compute cost, which is small at 0.8B to 4B and grows with the 9B and 27B sizes.
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
- 2026-10-30 - Volatile re-verification after the 2026-10-28/29 pushes: the project tagged its first release, v0.3.0 (2026-10-28, a CHANGELOG and release process, the valen-sdk 0.2.0 PyPI and 0.2.0 npm publications recorded, the qualified GGUFs packaged behind the Valen-patched llama.cpp and Ollama builds of a pinned gguf-runtime-v0.1.0), the README moved to valen-sdk 0.3.0 and announced a Valen.llm() LLM comparison and a Valen agent skill, and a Jev-ToM community evaluation joined the documentation (2026-10-27); pushed date moved to 2026-10-29.
- 2026-10-31 - Out-of-rotation re-fetch at the drift signal: the Decision Index's 2026-10-29 regeneration (248 configurations) crowd-shifted the three Valen rows at unchanged scores (4B 132nd to 144th, 2B 177th to 193rd, 0.8B 194th to 212th); fetched and re-cited.
- 2026-11-05 - Volatile re-verification after the 2026-11-04 push: the repository transferred from Liuziyu77/Valen to Valen-Team/Valen, and the merged #41 added the Valen-Decision-1.5 architecture generation (block-structured full attention and a grounding head as additive configuration options on the existing qwen backend, FSDP2 training, compiler-robustness fixes that skip rejected records and avoid per-length kernel selection and FlexAttention recompiles) with the READMEs renaming the project Valen-Decision; no release past v0.3.0 (2026-10-28); pushed date moved to 2026-11-04 and the star-history chart and citations re-pointed at the new owner.
- 2026-11-11 - Volatile re-verification at the v0.4.0 release (2026-11-10): the Valen-Decision-1.5 generation shipped in five sizes (the decision head on Qwen3.5 at 0.8B, 2B, 4B, and 9B plus a 27B on Qwen3.8-27B, block-bidirectional attention and a bbox grounding head, native BF16-backbone/FP32-head weights, per-size ONNX variants, and per-size F32/Q8_0-plus-vision GGUFs), with the gguf-runtime-v0.2.0 prebuilt CPU runtime serving 1.5 over `/v1/systemone` and `/v1/decisions` (block attention, noul-rubric folding, text and image input, bbox questions) and the runtime-0.1.0 GGUFs of 1.0 still loading; pushed date moved to 2026-11-11.
- 2026-11-13 - Volatile re-verification after the pushed-date move to 2026-11-12 (README updates: a playground badge, the 1.5 release post, the Decision Index ranking, and community projects, plus SGLang launch commands pinning bfloat16 and hosted-API bbox documentation; no release past v0.4.0 and gguf-runtime-v0.2.0), and the Decision Index's 2026-11-12 regeneration (301 configurations) replaced the family's three 1.0 rows with five 1.5 rows (27B forty-seventh at 65.21, 9B ninety-eighth at 55.85, 4B 130th at 49.87, 2B 181st at 37.97, 0.8B 227th at 27.60), putting the 27B above the vendor's Jev 1.14 row.

## See also

- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins
- [H2O-Lightning-4B](../h2o-lightning-4b/index.md) - the established open-weights decision model
- [Strands Decider 2B](../strands-decider-2b/index.md) - the AWS decision model with published training discipline
- [Jev](../jev/index.md) - the lineage original
- [JevBench](../jevbench/index.md) - the board where decision models get scored

## References

- https://github.com/Valen-Team/Valen - repository (moved from Liuziyu77/Valen in early November 2026), Apache-2.0 license, stars, push activity, and the training-and-eval structure as of 2026-11-13 (pushed 2026-11-12; GitHub API re-fetched 2026-11-13)
- https://github.com/Valen-Team/Valen/releases - the v0.3.0 release notes (2026-10-28): the CHANGELOG and release process, the SDK publications, and the pinned gguf-runtime-v0.1.0 packaging (re-fetched 2026-11-05) and the v0.4.0 release notes (2026-11-10): the Valen-Decision-1.5 generation in five sizes with per-size ONNX and GGUF repositories (re-fetched 2026-11-11, now the latest release)
- https://github.com/Valen-Team/Valen/releases/tag/gguf-runtime-v0.2.0 - the prebuilt Valen-patched llama-server CPU runtime 0.2.0 (2026-11-10) serving Valen-Decision-1.5 over `/v1/systemone` and `/v1/decisions` with bbox questions and noul-rubric folding (fetched 2026-11-11)
- https://github.com/Valen-Team/JevalKit - the first-party evaluation toolkit: Apache-2.0, created 2026-10-16, unified model interfaces and prepared evaluation datasets (GitHub API, as of 2026-10-24)
- https://huggingface.co/spaces/Valen-Team/JevalKit-Leaderboard - the JevalKit leaderboard Space (fetched 2026-10-24)
- https://valen-team.github.io/ - the documentation site and web chat, with the free-API and quota statements (fetched 2026-10-24)
- https://github.com/Liuziyu77/Valen/blob/main/evaluation/decision_index/README.md - the Decision Index adapter guide: official kit pinned at f5a6e4f, frozen suite 0.3, suite verification before model load (fetched 2026-10-17)
- https://huggingface.co/Valen-Team - the Hugging Face org holding the model cards, datasets, and the per-size ONNX and GGUF repositories of the Valen-Decision-1.5 line (the fifteen 1.5 repositories fetched 2026-11-11)
- https://huggingface.co/Valen-Team/Valen-4B - the flagship model card with usage and reported results
- https://huggingface.co/datasets/Valen-Team/VisualDecisionBench - the published evaluation set behind the benchmark claims
- https://huggingface.co/spaces/yuhangzang/Valen-Preview-0923 - the live demo Space
- https://typesafe.ai/blog/introducing-system-one-models-and-jev - the System One and Jev lineage post the README cites
- https://news.ycombinator.com/item?id=49838068 - the single 2-point HN post, the recorded thin community footprint
