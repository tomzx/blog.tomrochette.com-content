---
showArticleList: false
title: Hybrid execution
created: 2026-09-24
visible: true
status: in progress
tags: [agents, hybrid-execution]
readability: 3
---

Small fast models handling typed decisions beside the large model: constrained decoding, validate-and-retry libraries, the decision-model wave, and the benchmark that measures them.

- [Anthropic structured outputs](anthropic-structured-outputs/index.md) - schema-constrained decoding for Claude responses and tool inputs.
- [CUA-S1](cua-s1/index.md) - Cua's open-weights 706k-parameter System One checkpoint that scores form actions without generating text, the verifiable counterpart to Jev's closed contract.
- [Instructor](instructor/index.md) - Pydantic in, validated objects out, with a re-ask when validation fails.
- [Jev](jev/index.md) - TypeSafe's System One model that skips text generation entirely, typed decisions with calibrated confidence at 70-500ms, early access since September 2026.
- [JevBench](jevbench/index.md) - Benchmark Heaven's MIT scoreboard for Jev-class decision models, 534 decisions per system weighted equally on intelligence, calibration, speed, and cost, with hosted Jev first at 74.4 and SemIf 1.3 points behind.
- [Jevlike](jevlike/index.md) - the community's one-day reverse-engineering of the Jev contract, an MIT option-attention starter, dormant since launch day, its head lifted by CUA-S1.
- [Kev](kev/index.md) - Jared Palmer's Apache-2.0 Qwen3.5 LoRA family speaking the Jev API locally, with the wave's strongest pre-registered eval discipline.
- [Laya](laya/index.md) - the Apache-2.0 open-weights decision-model family answering typed questions in a single pass, the open rival to Jev's contract with its limits stated on its own model card.
- [NanoJev](nanojev/index.md) - the 0.6B game-task replica with the most complete pipeline and the least verification, every benchmark unreplicated.
- [Nimble](nimble/index.md) - Bespoke Labs' one-day open Jev with the category's only human-labeled head-to-head (Jev wins by 1.2 macro points) and an unlicensed repo.
- [OpenAI Structured Outputs](openai-structured-outputs/index.md) - schema-guaranteed responses via constrained decoding.
- [Outlines](outlines/index.md) - logit-masked generation following types, schemas, regexes, or grammars.
- [SemIf](semif/index.md) - frozen open models reading typed option probabilities straight from the logits, with a client-side WebGPU demo, until this week named OpenJev.

Its members are compared on shared rows in the [Hybrid Execution Feature Matrix](hybrid-execution-feature-matrix/index.md).

## Changes

- 2026-08-24 - Added Anthropic structured outputs.
- 2026-08-24 - Added Instructor.
- 2026-08-24 - Added OpenAI Structured Outputs.
- 2026-08-24 - Added Outlines.
- 2026-09-18 - Added Jev.
- 2026-09-20 - Added CUA-S1.
- 2026-09-21 - Added Jevlike.
- 2026-09-21 - Added Kev.
- 2026-09-21 - Added Laya.
- 2026-09-21 - Added NanoJev.
- 2026-09-21 - Added Nimble.
- 2026-09-21 - Added SemIf.
- 2026-09-22 - Added JevBench.
