---
title: Ollaya
created: 2026-10-06
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, local-inference, model-hub]
readability: 3
audience_notes: >
  Engineers who want the Jev-style decision contract running locally across many open model families instead of one vendor's server.
  Assumes you have read this category's Jev note and know what a fitted temperature is.
---

Ollaya is an Apache-2.0 local runtime and model hub, built in the image of Ollama, that serves nineteen open decision-model families behind a wire-identical replica of TypeSafe's Jev API.

**The decision-model wave just got its Ollama, and its verification discipline is the strongest the open side of this category has shown: 41,352 answers checked one by one against each author's own code, with the raw data published.**

## What it is

One binary (a desktop app, a CLI, and a Docker image) for macOS, Windows, and Linux that exposes `/v1/systemone`, `/v1/decisions`, and `/v1/models` with TypeSafe's request and response formats, so the official TypeSafe Python SDK 0.7.1 runs unchanged against localhost.
The library spans nineteen families as of 2026-10-08: encoder-based ones (laya, nli, gliclass, von, decima) that answer in 10 to 20 milliseconds on a CPU, and decoder-based ones (winnow, clef, kev, decider, nimble, jeb, jeeves, cygnet, snap, arbiter) up to 12B.
Weights are pulled from each author's Hugging Face repository pinned to a commit and checked against sha256, never re-hosted.
It runs on ONNX Runtime over the CPU or an NVIDIA GPU (CUDA 13 or 12, Vulkan), with MLX on Apple silicon for laya and nli, and it is an independent project by Mert Cobanov, not affiliated with Ollama or TypeSafe.

## Status

**Fifteen days old, beta, and already the wave's default front door.**
The repository was created 2026-09-23 and shows 1,239 stars and 72 forks as of 2026-10-08, pushed 2026-10-06.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ollaya-dev/ollaya&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ollaya-dev/ollaya&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ollaya-dev/ollaya&type=date&legend=top-left" />
</picture>

The launch Show HN thread (2026-09-25) reached 618 points, the third-largest of the whole Jev wave.
The results page reports 31 models measured, 73,720 benchmark answers scored against human labels, 41,352 parity checks against the authors' own code, and 2,184 timed requests, with the newest measurement dated 2026-10-06 on three disclosed machines (RTX 5090 and RTX 4090 desktops and an M4 Pro Mac mini) plus contributor-run community benches, under Ollaya 0.8.0.
Its head-to-head numbers are self-run but use Bespoke Labs' public benchmark with Ollama on the same GPU: winnow:12b scores 0.773 against Ollama 0.35's best 0.749, and on the same Nimble weights Ollaya reports 5.5x lower calibration error (ECE 0.022 against 0.122) while conceding speed to Ollama's GGUF path (310 ms against 210 ms).

## Strengths

- **Parity checking against the authors' code is the discipline this category needed: answers compared one by one against what each model's author ships, raw data included, rather than another self-graded accuracy table.**
- Weights pinned by commit and sha256 from the authors' own repositories, so the runtime cannot silently drift from what an author measured.
- Calibration is first-class: each model ships its author's fitted temperature, and a Modelfile refits it on your labelled data.
- The encoder families (nli, gliclass, laya) cover the millisecond, CPU-friendly slice that Ollama's decoder-only decision support ignores, and the TypeSafe-compatible surface means code written against the closed API moves without edits.

## Cautions

- **The accuracy and latency comparisons are self-run on two disclosed consumer machines, and the hosted-Jev comparison imports third-party benchmark numbers measured elsewhere, which the site itself says to read only as orders of magnitude.**
- Beta software with one named developer carrying it, so bus factor is one.
- The library mixes strong and weak models by design (its own table scores laya:en at 0.361 on typed decisions), so the runtime does not save you from model choice.
- API compatibility is to the published formats, not to the closed model: point the TypeSafe SDK at Ollaya and you get open-model quality, not Jev's.

## Pricing

Free and open: Apache-2.0 runtime, authors' weights under their own licenses, no metering and no hosted tier.
The cost is your hardware and the model downloads.

## Compared to

- [Jev](../jev/index.md): the closed, hosted original Ollaya's API copies; choose Jev for frontier accuracy behind an SLA, Ollaya for local, private, unmetered decisions across sixteen families.
- [Kev](../kev/index.md): a single-family server for the same contract; Ollaya is the multi-family hub that ships kev:9b among its models.
- Ollama 0.35: the incumbent runtime, which serves two decision-model families (Nimble and Tev1) as raw-softmax GGUF conversions; Ollaya covers more families with author calibration but loses the same-weights latency race.

## Bottom line

**Recommended for engineers who want the open decision-model wave behind one local API with its calibration intact, and for anyone auditing a checkpoint against its author's code.**
Not for anyone who needs a vendor SLA, hosted-Jev-class accuracy today, or a project with more than one maintainer.
The disagreeable claim I will defend: runtimes, not models, decide which open ecosystems survive, and Ollama proved it for LLMs, so every model author in this wave should treat Ollaya's defaults as their distribution channel whether they like it or not.

## Changes

- 2026-10-06 - Created from the entrant scan after the 2026-09-25 Show HN thread cleared the bar (618 points, 1.2k stars in ten days, and a parity-checked results page).
- 2026-10-06 - Corrected the age claim (created 2026-09-23, thirteen days old, not three weeks) and refreshed stars to 1,209.
- 2026-10-07 - Added the ollaya-dev/ollaya star history chart to the Status section.
- 2026-10-07 - Reworded two pre-existing "shapes" compounds to "formats" (the TypeSafe request and response formats, the published formats) to keep the banned-terms rule.
- 2026-10-08 - The library grew to nineteen families (decima, snap, and arbiter joining) and the results page moved to 31 models measured, 2,184 timed requests, a newest measurement of 2026-10-06, a third disclosed machine (M4 Pro Mac mini) beside the two desktops, and Ollaya 0.8.0; refreshed stars to 1,239.

## See also

- [Jev](../jev/index.md) - the closed model whose API Ollaya replicates wire for wire
- [Kev](../kev/index.md) - the single-family server whose checkpoints Ollaya also packages
- [Laya](../laya/index.md) - the encoder family that gives Ollaya its CPU-speed slice
- [Nimble](../nimble/index.md) - whose public human-labeled benchmark is the yardstick in Ollaya's Ollama comparison
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://ollaya.dev/ - product surface: endpoints, model families, platforms, the Ollama comparison table, Apache-2.0 licensing
- https://github.com/ollaya-dev/ollaya - repository: Apache-2.0, created 2026-09-23, 1,226 stars, 71 forks, pushed 2026-10-06 (GitHub API, as of 2026-10-07)
- https://ollaya.dev/results - the measurement page: 26 models, 73,720 benchmark answers, 41,352 parity checks, disclosed machines, newest measurement 2026-10-02
- https://ollaya.dev/docs/typesafe-compatibility - the wire-identical TypeSafe API documentation, including SDK 0.7.1 compatibility
- https://news.ycombinator.com/item?id=49848269 - the 618-point launch thread (2026-09-25)
- https://huggingface.co/ollaya-dev - the pinned model mirrors (15 repositories listed via the Hugging Face API, as of 2026-10-06)
