---
title: Magnitude
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, local-inference, inference-engine]
readability: 3
audience_notes: >
  For engineers choosing a local runtime for coding agents.
  Assumes you know what tok/s, a KV cache, and quantization are.
---

Magnitude is a free open-source inference engine for agents that compiles and tunes its GPU kernels on your exact hardware, shipped as a desktop app that connects open models to the coding agent you already use.

**Its "up to 2x faster than llama.cpp" claim rests on one self-chosen benchmark, and launch-thread measurements show llama.cpp winning on other setups, so I treat Magnitude as a promising bet rather than a demonstrated win.**

## What it is

An Apache-2.0 inference engine written in Rust by magnitudedev, a two-person YC S25 team (Anders and Tom) whose previous project was an open-source browser agent that reached 4k+ stars and 100k+ downloads.
It installs as a desktop app on macOS, Windows, and Linux, serves open models from a curated catalog of 15 (as of 2026-10-06) over an OpenAI-compatible API, and tunes its kernels on your device in about one minute per downloaded model.
The kernels are hand-written with tunable parameters and then fitted to your chip: Metal on Apple silicon, CUDA on NVIDIA, Vulkan on AMD and Strix Halo, or plain CPU, and the KV cache is quantized to 8-bit keys and 4-bit values to cut long-context memory.
One-click connectors target Pi, OpenCode, Hermes, OpenClaw, Codex, Claude Code, Oh My Pi, and Cline.

## Status

Active and young: 6,474 stars, 442 forks, 36 open issues, repo pushed 2026-10-07 (as of 2026-10-07).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=magnitudedev/magnitude&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=magnitudedev/magnitude&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=magnitudedev/magnitude&type=date&legend=top-left" />
</picture>

The Launch HN post on 2026-09-30 drew 194 points and 99 comments.
The product pivoted: the same domain hosted "Magnitude: A coding agent that runs on open models" in June 2026 before the team turned the engine underneath it into the product.
The founders told the launch thread that a hybrid inference cloud with per-token billing is planned, with the free engine underneath.

## Strengths

- Kernel tuning happens on your machine in about a minute per model, so there is no manual benchmark fitting.
- Quantized KV cache cuts KV memory by more than half, and the site claims 27% less memory per agent with prefix caches shared across sessions.
- The catalog estimates what fits and how fast it runs before you download.
- Free, local, Apache-2.0, and private: nothing leaves the machine once a model is downloaded.
- The team uses coding agents to optimize kernels, a cheap way to keep pace with new model architectures.

## Cautions

- The speed claim is contested: the launch benchmark is a prose-repetition task, one launch user measured Magnitude 0.2.1 at roughly half of llama.cpp speed for both prefill and decode on an M5 Max (the founder acknowledged an unexploited M5 matmul path), and another measured llama.cpp 20-30% faster at decode on an RTX 5070ti.
- No multi-GPU support yet (issue #141), and one launch user's two NVIDIA GPUs were detected as four.
- The catalog is deliberately narrow: 15 curated families, nothing below 4-bit, because the founders say lower quantizations break thinking and tool calls.
- Launch users hit install friction, including a stuck "assessing models" step (issue #142) and model-fit estimates that were wrong on some machines.
- The planned cloud has no published prices, so the free engine is currently the whole product.

## Pricing

Pricing does not apply: the engine is free and open source under Apache-2.0 with no account and no token costs, and the founders' planned hybrid inference cloud had no published prices as of 2026-10-06.

## Compared to

[Ollama](../ollama/index.md) is the incumbent: broader model coverage, a far larger community, and its own paid cloud; choose it for breadth and ecosystem maturity, Magnitude for speed on the families it tunes for.
llama.cpp is the baseline engine with the widest hardware and model support, and launch-thread measurements show it still winning on some M5 and NVIDIA setups; choose Magnitude when its tuned kernels win on your chip and you want agent-oriented memory management in a desktop app.
vLLM serves batched multi-user inference on datacenter GPUs; choose it for shared servers, Magnitude for single-session local agent workloads.

## Bottom line

Recommended for engineers on Apple silicon running supported open model families in one or two agent sessions, who want the fastest setup with zero tuning effort.
Not for multi-GPU boxes, niche model families, or anyone who needs proven throughput today, where llama.cpp remains my default.
My disagreeable claim: on current evidence the 2x marketing is narrower than the headline, and a single-agent MacBook user loses little by waiting a quarter.

## Changes

- 2026-10-06 - Created.
- 2026-10-06 - Converted the Compared-to cross-references from plain-text paths into working links.
- 2026-10-07 - Added the magnitudedev/magnitude star history chart to the Status section.

## See also

- [Ollama](../ollama/index.md) - the incumbent free local runtime Magnitude races on speed.
- [Model Access Feature Matrix](../model-access-feature-matrix/index.md) - the category comparison holding this note's column.
- [OpenCode](../../harnesses/opencode/index.md) - a coding harness Magnitude connects to with one click.
- [OpenRouter](../openrouter/index.md) - the hosted alternative when local hardware is the constraint.
- [Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - choosing models once the runtime is settled.

## References

- https://api.github.com/repos/magnitudedev/magnitude - 6,474 stars, 442 forks, Rust, Apache-2.0, pushed 2026-10-07, homepage (fetched via the GitHub API, 2026-10-07).
- https://magnitude.dev/ - positioning, benchmark table (Metal 92% faster decode, CUDA 19%), memory and connector claims, FAQ (200, fetched 2026-10-06).
- https://hn.algolia.com/api/v1/items/49911995 - launch thread: founders, tuning time, benchmark methodology, critical speed measurements, planned per-token cloud (200, fetched 2026-10-06).
- https://hn.algolia.com/api/v1/search?query=magnitude&tags=story&numericFilters=created_at_i%3E1758900000 - launch points and date, plus the June 2026 coding-agent pivot story (200, fetched 2026-10-06).
- https://magnitude.dev/models - the 15-model catalog, quantizations Q4 to Q8, DFlash drafters (200, fetched 2026-10-06).
- https://github.com/magnitudedev/magnitude/issues/141 - dual-GPU configuration report, multi-GPU unsupported (200, fetched 2026-10-06).
