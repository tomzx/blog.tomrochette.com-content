---
title: Von
created: 2026-10-11
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights, cpu-inference]
readability: 3
audience_notes: >
  Engineers who want typed decisions on hardware smaller than a GPU box, and want to know what a 395M encoder actually buys against the decoder-based wave.
  Assumes you know what a ModernBERT-class encoder is, and have read this category's Jev note.
---

Von is wfzyx's Apache-2.0 non-autoregressive decision model, a 395M ModernBERT encoder that answers Choice, Noul, and Score questions over JSON or text states in one forward pass with no generated tokens, shipped as a TypeSafe-wire server plus Python and TypeScript SDKs and runnable on CPU through OpenVINO.

**Von is the wave's smallest credible generalist, and its third-party benching says exactly what its size predicts: the cheapest, fastest CPU deployment in the category, English-only in practice, and near the bottom of the accuracy tables the decoder fine-tunes lead.**

## What it is

A ModernBERT encoder (about 3 GB of weights on Hugging Face) that reads option descriptions against a shared state and scores them in one pass: Choice over K described options with a probability over all of them, Noul as a probability, and Score as a calibrated position on an ordinal scale.
It ships as `von-sdk` for Python and TypeScript, a Docker image (`ghcr.io/wfzyx/von:cpu`), and runtimes for CPU (OpenVINO), CUDA, ROCm, and Apple MPS, speaking TypeSafe's `/v1/systemone` wire protocol so SDK code written against the hosted contract runs unchanged.
The README leads with a Doom demo whose every action is one forward pass scoring six option descriptions against a text-rendered depth buffer, on the same shipped weights that answer routing questions, and the model card carries the training data and the benchmark record.

## Status

Archived and concluded as of 2026-10-17: the repository now carries GitHub's archived flag and a README banner reading "Status: Archived / Concluded (2026-10-17)", with weights, SDKs, and benchmarks preserved for reference (final push 2026-10-17, then a 2026-10-19 README commit pointing the archived notice at LiquidAI's d1-omni-600M as the follow-on).
Before that it was active and community-scale: the repository was created 2026-09-18, 880 stars as of 2026-10-11, and the checkpoint shows 85,677 downloads and 64 likes as of 2026-10-27 (GitHub and Hugging Face APIs); `von-sdk` 1.3.7 has been on PyPI since 2026-10-02 and remains installable, and the weights on Hugging Face are untouched (not gated).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=wfzyx/von&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=wfzyx/von&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=wfzyx/von&type=date&legend=top-left" />
</picture>

The scoreboard readings are humbling: von-1.3 scores 11.65, rank 212 of 230 on the Decision Index 0.4.1 board as regenerated 2026-10-26, against Jev 1.14's 60.24, and Von does not carry a JevBench composite row.
The third-party local-jev-bench suite (measured 2026-10-05) states the model card's own boundary in its findings: English-only, 15 percent on a Korean set, near the bottom of its accuracy tables on every set but the small English one, at 32 to 411 ms first-call p50; Ollaya's table scores von at 0.447 on typed decisions with 8,192-token states at 19 ms.

## Strengths

- **CPU-first serving is the differentiator that matters: 20 to 30 ms decisions on commodity cores put this contract inside processes no GPU touches, and the Docker and dual-SDK packaging makes that a ten-minute install.**
- The six-figure rolling-month download count (85,677 as of 2026-10-27) on a 395M checkpoint says the size niche is genuine, and von is the only encoder-scale generalist in the wave besides Laya's family.
- TypeSafe-wire compatibility plus Python and TypeScript SDKs keep it drop-in for code written against the hosted contract.
- The model card publishes the training data and benchmark record rather than a claims table, which is more than most of the wave's launch posts offer.

## Cautions

- **Accuracy is the price of the size: near-bottom readings on every third-party table that includes it, and a Korean-language 15 percent that its own card's English-only note predicts.**
- No JevBench composite row exists, so its calibration has no independent reading beyond local-jev-bench's distribution-distance work.
- One maintainer, 880 stars, and an SDK versioned in the ones digit: the bus factor and API-stability cautions that apply to every one-person entry in this wave apply here.
- The 395M encoder's ceiling is architectural; fine-tuning recipes exist in the repo, but no published fine-tune has moved it into the top group.

## Pricing

Free and open: Apache-2.0 code and weights, no hosted service and no paid tier.
The cost is about 3 GB of weights and whatever CPU you already have.

## Compared to

- [Laya](../laya/index.md): the other encoder-scale family; Laya ships three checkpoints and a router with working multilingual coverage and its own fine-tuned typed-decisions specialist, Von ships one smaller model with a CPU-first runtime story.
- [Jev](../jev/index.md): the closed original; against hosted Jev, Von trades most of the accuracy for hardware the size of a laptop, which is the trade the contract's millisecond pitch implies but no decoder entrant actually delivers.
- [Ollaya](../ollaya/index.md): the runtime that packages von and its calibration, and whose own table is the fastest way to see what the 395M ceiling costs.

## Bottom line

**Recommended, with the archival attached, for embedded, on-prem, or per-process decision layers where a GPU is off the table and English-only, mid-accuracy decisions are acceptable: the weights and SDKs are preserved and runnable, but nothing here will be fixed.**
Not for accuracy-led rankings, multilingual states, or anyone who needs a calibrated threshold validated by a second party.
The disagreeable claim I will defend: Von's near-bottom accuracy and six-figure downloads are the same fact, the demand in this category is for the deployment model first and the scoreboard second, and every accuracy-led entrant that ignored that has grown slower than the CPU ones.

## Changes

- 2026-10-11 - Created from the entrant scan (awesome-jev cross-check), accepted on the CPU-first niche (880 stars, 103k checkpoint downloads) with the near-bottom third-party accuracy readings recorded as the governing caution.
- 2026-10-11 - Added the star history chart.
- 2026-10-15 - The Decision Index citation moved from the stale 0.3.1 label to the current 0.3.2 board at the unchanged 8.17, now rank 151 of 166.
- 2026-10-17 - Status moved to archived: the repository gained GitHub's archived flag and a README banner dated 2026-10-17 ("Archived / Concluded", weights, SDKs, and benchmarks preserved for reference); the recommendation now carries the archival, and the checkpoint's download and like counts were re-read (115,170 and 59) with the weights and PyPI package confirmed untouched.
- 2026-10-20 - Volatile re-verification after the 2026-10-19 post-archival push: the archived notice now points at LiquidAI's d1-omni-600M as the follow-on (the README's only change), and the checkpoint's download and like counts were re-read at 118,261 and 62 with the weights confirmed untouched.
- 2026-10-22 - The Decision Index's edition-0.4 rebuild (226 configurations, the Full score now entirely private) rescored the archived von-1.3 to 11.65, rank 208 of 226, against Jev 1.14's 60.24; the archive status is untouched.
- 2026-10-27 - Rotation re-verification, every cited URL re-fetched and live: the archive holds (the repository still carries GitHub's archived flag and the d1-omni-600M pointer), PyPI still serves von-sdk 1.3.7, the checkpoint's rolling-month counts re-read at 85,677 downloads and 64 likes, the Decision Index's 2026-10-26 regeneration (230 configurations) moved the unchanged 11.65 from rank 208 to 212, and Ollaya's 0.447 typed-decisions row holds; nothing else changed.

## See also

- [Laya](../laya/index.md) - the other encoder-scale family, multilingual and routed where Von is single and CPU-first
- [Jev](../jev/index.md) - the closed contract Von reproduces on CPU-class hardware
- [Ollaya](../ollaya/index.md) - the runtime that packages von and carries its typed-decisions row
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/wfzyx/von - repository: Apache-2.0, created 2026-09-18, 880 stars, archived 2026-10-17 with the "Archived / Concluded" README banner (its 2026-10-19 commit points at LiquidAI/d1-omni-600M), the 395M ModernBERT design, SDK and Docker surfaces, and the runtime matrix (GitHub API and README, as of 2026-10-20; archived flag and pushed date re-confirmed 2026-10-27)
- https://huggingface.co/wfzyx/von - the checkpoint: Apache-2.0, created 2026-09-19, 85,677 downloads and 64 likes as of 2026-10-27, training data and benchmark record on the card (Hugging Face API, as of 2026-10-27)
- https://pypi.org/project/von-sdk/ - the Python SDK, version 1.3.7 uploaded 2026-10-02 (fetched 2026-10-11, re-fetched unchanged 2026-10-27)
- https://huggingface.co/spaces/multimodalart/jev-decision-index/resolve/main/data/v03.json - the Decision Index 0.4.1 row scoring von-1.3 at 11.65, rank 212 of 230 after the 2026-10-26 regeneration, against Jev 1.14's 60.24 (fetched 2026-10-27)
- https://raw.githubusercontent.com/tak-bro/local-jev-bench/HEAD/README.md - the third-party Apple Silicon reading: English-only, 32 to 411 ms first-call p50, near the bottom of the accuracy tables (measured 2026-10-05, fetched 2026-10-11, re-fetched 200 2026-10-27)
- https://ollaya.dev/ - Ollaya's packaged von row: 0.447 on typed decisions with 8,192-token states (fetched 2026-10-11, re-fetched 2026-10-27, the row holds)
