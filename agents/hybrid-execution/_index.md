---
showArticleList: false
title: Hybrid execution
created: 2026-09-24
visible: true
status: in progress
tags: [agents, hybrid-execution]
readability: 3
---

Small fast models handling typed decisions beside the large model: constrained decoding, validate-and-retry libraries, the decision-model wave, and the three benchmarks that measure them.

- [Anthropic structured outputs](anthropic-structured-outputs/index.md) - schema-constrained decoding for Claude responses and tool inputs.
- [AnyJev](anyjev/index.md) - Nokia Applied Research's training-free readout turning any instruction-tuned LLM into a calibrated decision model with rotation-averaged logits and verified early-exit bounds, with an arXiv report and third-party benchmark coverage, 1,092 stars.
- [Atomic Agents](atomic-agents/index.md) - the MIT Python framework assembling agents, tools, and context providers as schema-validated components on Instructor and Pydantic, the validate-and-retry family's framework layer, 6.3k stars.
- [CUA-S1](cua-s1/index.md) - Cua's open-weights 706k-parameter System One checkpoint that scores form actions without generating text, the verifiable counterpart to Jev's closed contract.
- [Decision Index](decision-index/index.md) - the second independent scoreboard for Jev-class models, 110,201 public requests over 42 benchmarks plus private tests, where two 27B-class systems sit above Jev (third) and the boards disagree by tens of points.
- [Instructor](instructor/index.md) - Pydantic in, validated objects out, with a re-ask when validation fails.
- [Jeeves](jeeves/index.md) - PostHog's 9B reasoning decision model that thinks before it answers typed questions, beating Jev's published numbers on its own tests at ten times the latency.
- [Jeff](jeff/index.md) - the AutoJev-fork fine-tune family (0.8B and 2B Qwen3.5, Gemma 4 E2B) speaking Jev's request format at 22 ms locally, with the frankest self-run benchmark table in the wave.
- [Jev](jev/index.md) - TypeSafe's System One model that skips text generation entirely, typed decisions with calibrated confidence at 70-500ms, early access since September 2026.
- [JevBench](jevbench/index.md) - Benchmark Heaven's MIT scoreboard for Jev-class decision models, scored on intelligence, calibration, speed, and cost, whose boards keep getting rebuilt under the wave (Jev first through v1.4.2, the unranked reference on the October v1.6.1 redesign, with H2O-Lightning-4B now the open leader above it).
- [Jevlike](jevlike/index.md) - the community's one-day reverse-engineering of the Jev contract, an MIT option-attention starter, dormant since launch day, its head lifted by CUA-S1.
- [Kev](kev/index.md) - Jared Palmer's Apache-2.0 decision-model family (0.8B to a full-weights 27B, versioned together as Kev 1.0) speaking the Jev API locally, with the wave's strongest pre-registered eval discipline.
- [Laya](laya/index.md) - the Apache-2.0 open-weights decision-model family answering typed questions in a single pass, the open rival to Jev's contract with its limits stated on its own model card.
- [NanoJev](nanojev/index.md) - the 0.6B game-task replica with the most complete pipeline and the least verification, every benchmark unreplicated.
- [Nimble](nimble/index.md) - Bespoke Labs' one-day open Jev with the category's only human-labeled head-to-head (Jev wins by 1.2 macro points) and an unlicensed repo.
- [Ollaya](ollaya/index.md) - the Apache-2.0 local runtime serving nineteen open decision-model families behind a wire-identical Jev API, with parity checks against each author's own code.
- [OpenAI Structured Outputs](openai-structured-outputs/index.md) - schema-guaranteed responses via constrained decoding.
- [Outlines](outlines/index.md) - logit-masked generation following types, schemas, regexes, or grammars.
- [SemIf](semif/index.md) - frozen open models reading typed option probabilities straight from the logits, with a client-side WebGPU demo, called OpenJev until 2026-09-18.
- [tool-eval-bench](tool-eval-bench/index.md) - the MIT auditor for tool-calling quality on self-hosted serving stacks, 69 deterministic multi-turn scenarios with full traces plus a decision-model track over the same `/v1/systemone` surface.

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
- 2026-09-29 - Added Jeff.
- 2026-10-06 - Added Jeeves.
- 2026-10-06 - Added Ollaya.
- 2026-10-07 - Added Decision Index.
- 2026-10-07 - Added AnyJev.
- 2026-10-07 - Added Atomic Agents.
- 2026-10-08 - Added tool-eval-bench.
