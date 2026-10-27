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
- [AnyJev](anyjev/index.md) - Nokia Applied Research's training-free readout turning any instruction-tuned LLM into a calibrated decision model with rotation-averaged logits and verified early-exit bounds, with an arXiv report, third-party benchmark coverage, and three Decision Index rows (eighth, nineteenth, and thirtieth on the 0.4.1 board), 1,271 stars.
- [Atomic Agents](atomic-agents/index.md) - the MIT Python framework assembling agents, tools, and context providers as schema-validated components on Instructor and Pydantic, the validate-and-retry family's framework layer, 6.3k stars.
- [BAML](baml/index.md) - Boundary's Apache-2.0 typed language for agent code, where LLM calls are functions with schema return types and the error-correcting parser from its structured-output era, 9.4k stars.
- [CLM](clm/index.md) - the Apache-2.0 contrastive state-action encoder (a Qwen3-8B embedding model plus a 75 MB head) behind the wave's first architectural dissent, whose Jev-parity claims both independent boards answer with near-zero scores, 2.9k stars.
- [CUA-S1](cua-s1/index.md) - Cua's open-weights 706k-parameter System One checkpoint that scores form actions without generating text, the verifiable counterpart to Jev's closed contract.
- [Decider](decider/index.md) - Mapika's Apache-2.0 one-pass family from 2B to 35B-A3B on Qwen3.5 decoders, JevBench's first open number one and the category's clearest sealed-protocol collapse record.
- [Decision Index](decision-index/index.md) - the second independent scoreboard for Jev-class models, 110,201 public requests over 42 benchmarks shown but uncounted beside a fully private Full score, where forty-one systems sit above Jev 1.14 (forty-second) on the 0.4.1 board.
- [Guardrails](guardrails/index.md) - the Apache-2.0 validator-hub framework composing Input and Output Guards from 65 installable risk validators around 100-plus LiteLLM-reachable providers, with validate-and-reask structured generation, now under Harvey after its September acquisition.
- [H2O-Lightning-4B](h2o-lightning-4b/index.md) - H2O.ai's Apache-2.0 Qwen3.5-4B decision fine-tune with vision, the first open-weights system measured above hosted Jev on an independent composite.
- [Instructor](instructor/index.md) - Pydantic in, validated objects out, with a re-ask when validation fails.
- [Jeeves](jeeves/index.md) - PostHog's 9B reasoning decision model that thinks before it answers typed questions, beating Jev's published numbers on its own tests at ten times the latency.
- [Jeff](jeff/index.md) - the AutoJev-fork fine-tune family (0.8B and 2B Qwen3.5, Gemma 4 E2B) speaking Jev's request format at 22 ms locally, with the frankest self-run benchmark table in the wave.
- [Jev](jev/index.md) - TypeSafe's System One model that skips text generation entirely, typed decisions with calibrated confidence at 70-500ms, early access since September 2026.
- [JevBench](jevbench/index.md) - Benchmark Heaven's MIT scoreboard for Jev-class decision models, scored on intelligence, calibration, speed, and cost, whose boards keep getting rebuilt under the wave (Jev first through v1.4.2, the unranked reference on the October boards, H2O-Lightning-31B v1.0.7 the capability leader on the method-v1.7 board as of 2026-10-25).
- [Jevlike](jevlike/index.md) - the community's one-day reverse-engineering of the Jev contract, an MIT option-attention starter, dormant since launch day, its head lifted by CUA-S1.
- [Kev](kev/index.md) - Jared Palmer's Apache-2.0 decision-model family (0.8B to a full-weights 27B, versioned together as Kev 1.0) speaking the Jev API locally, with the wave's strongest pre-registered eval discipline.
- [Laya](laya/index.md) - the Apache-2.0 open-weights decision-model family answering typed questions in a single pass, the open rival to Jev's contract with its limits stated on its own model card.
- [Marvin](marvin/index.md) - Prefect's Apache-2.0 AI-functions toolkit, the validate-and-retry family's smallest API (extract, cast, classify, generate over Pydantic types) with a ControlFlow-derived task-agent-thread layer, twice rebuilt and quiet on releases since March 2026, 6.2k stars.
- [NanoJev](nanojev/index.md) - the 0.6B game-task replica with the most complete pipeline and the least verification, every benchmark unreplicated.
- [Nimble](nimble/index.md) - Bespoke Labs' one-day open Jev with the category's only human-labeled head-to-head (Jev wins by 1.2 macro points) and an unlicensed repo.
- [Ollaya](ollaya/index.md) - the Apache-2.0 local runtime serving twenty-nine open decision-model families behind a wire-identical Jev API, with parity checks against each author's own code.
- [OpenAI Structured Outputs](openai-structured-outputs/index.md) - schema-guaranteed responses via constrained decoding.
- [Outlines](outlines/index.md) - logit-masked generation following types, schemas, regexes, or grammars.
- [SemIf](semif/index.md) - frozen open models reading typed option probabilities straight from the logits, with a client-side WebGPU demo, called OpenJev until 2026-09-18.
- [Strands Decider 2B](strands-decider-2b/index.md) - the Strands Agents team's Apache-2.0 2B decision model with the wave's best-published training discipline (seed tables, a soup, a calibration contract) and the weakest third-party reading so far, 585 stars.
- [System1-Arena](system1-arena/index.md) - the Apache-2.0 academic benchmark handing decision models and generative LLMs identical typed decisions across 92k questions and 138 closed-loop environments, the fourth scoreboard and the first to measure both halves of the contract like for like.
- [tool-eval-bench](tool-eval-bench/index.md) - the MIT auditor for tool-calling quality on self-hosted serving stacks, 69 deterministic multi-turn scenarios with full traces plus a decision-model track over the same `/v1/systemone` surface.
- [Valen](valen/index.md) - the Apache-2.0 open-weights Jev-family decision model with vision (0.8B/2B/4B, ONNX and GGUF exports, training code and benchmarks published), a month old with a 2-point HN footprint and a free hosted decision API since 2026-10-21.
- [Von](von/index.md) - the Apache-2.0 395M ModernBERT encoder answering typed questions on CPUs through Python and TypeScript SDKs and a Docker image, the wave's smallest credible generalist, near the bottom of the accuracy tables by third-party reading, archived by its author on 2026-10-17.
- [Winnow](winnow/index.md) - EldanRing's Apache-2.0 Gemma 4 family (E2B to 12B, GGUF, vision) matching Jev answer-for-answer on public subsets, the community checkpoint that three independent readers rank at the top.

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
- 2026-10-11 - Added CLM.
- 2026-10-11 - Added Decider.
- 2026-10-11 - Added H2O-Lightning-4B.
- 2026-10-11 - Added Von.
- 2026-10-11 - Added Winnow.
- 2026-10-11 - Added BAML.
- 2026-10-12 - Added Strands Decider 2B.
- 2026-10-13 - Added Valen.
- 2026-10-13 - Added Guardrails.
- 2026-10-15 - Added Marvin.
- 2026-10-17 - Added System1-Arena.
