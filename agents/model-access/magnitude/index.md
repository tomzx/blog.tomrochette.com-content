---
title: Magnitude
created: 2026-10-06
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.4, llm=glm-5.3-flash, model-access, local-inference, inference-engine]
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
One-click connectors target Pi, OpenCode, Hermes, OpenClaw, Codex, Claude Code, Oh My Pi, and Cline, and a `@magnitudedev/cli` package (0.2.17 as of 2026-11-12) installs the app and can connect Claude Code to the loaded local model without a Claude login; since 0.2.11 the CLI also runs any GGUF of a supported model family, including off-catalog quantizations, finetunes, and merges, 0.2.14 made the catalog sortable by each model's estimated speed on your machine or by its intelligence score, 0.2.15 stopped rejecting Claude-protocol clients over the `anthropic-version` header, 0.2.16 fixed concurrent chats sharing a prompt prefix unloading the model, with shared-prefix reuse across requests (the release's own numbers: 8 concurrent requests sharing a 15K-token prompt from 226 seconds each to 3.5 seconds on an NVIDIA A10G with a draft model), and 0.2.17 added dot-product CPU kernels for ARM (AWS Graviton and Ampere class), with runtime detection of those instructions on Linux ARM64 builds and the release's own numbers at 4-13x faster prompt processing and 1.4-5x faster generation on Q8_0 models versus 0.2.16, plus fixes for a catalog-version deletion removing an image file shared with another installed version, MTP-drafting batch failures, and dropped connections while a download starts.

## Status

Active and young: 6,886 stars, 464 forks (as of 2026-10-24), repo pushed 2026-11-27 (as of 2026-11-27), the default-branch work kernel- and program-store focused (shared program formation across processes, per-backend decode-gap tooling, and a NaN-propagation fix in the engine registry), then a 2026-11-17 batch compiling Metal attention and ordered GEMM kernels on macOS 27, giving CPU kernel code memory and symbol lookup a Windows implementation, fixing streamed MoE models crashing the Metal worker on their first request, reserving a request's memory as it writes instead of its whole context up front, and stopping a panicking CPU launch from failing every later device use; since then the releases feed carries only QA-build prereleases (the npm CLI tags 0.2.97, 0.2.98, and 0.2.99 on 2026-11-20 and 11-21 plus a cliqa-r3-r0-0.2.17 tag of 2026-11-20, each marked a temporary QA build), and since 2026-11-23 a 0.3.0 alpha prerelease train (0.3.0-alpha.0 and 0.3.0-alpha.1 on 2026-11-23, 0.3.0-alpha.2 on 2026-11-24, each flagged prerelease), with CLI 0.2.17 the latest stable at that point; the 0.3.0 line then went stable on 2026-11-24 evening (0.3.0 not flagged prerelease, its notes headlined by streaming MoE models larger than GPU memory or system RAM and a CLI-only install path) and patched daily to 0.3.5 (2026-11-26) and 0.3.6 (2026-11-27), so CLI 0.3.6 is the latest stable release (its notes headlined by faster streamed MoE inference on Apple Silicon and NVIDIA, up to 1.88x faster decode and 2.07x faster prefill with about 2.6 GB less host memory on large MoE models by the release's own numbers, a cap on prefill workspace for large resident MoE models that removes 16 to 57 GB of unused allocations on 64K to 256K context models, and Apache-2.0 declared in the Rust workspace and package manifests after license and SBOM tools had reported the engine as unlicensed); the 2026-11-23 and 11-24 default-branch batch enabled embedded MTP beside a projector for GLM-5.3 Flash, lowered the recommendations target speed to 10 tok/s, and carried CUDA graph, prefill pipeline, and Vulkan kernel work; the 2026-11-25 and 11-26 batch fixed Windows 10 startup by reading the NUMA nodes the build supports, sealed the decode stages streamed Gemma 4 blocks run in, stopped a catalog drafter serving as its own target, moved Vulkan inter-workgroup atomics onto the Vulkan Memory Model, bounded Windows CUDA VRAM by the WDDM local budget, and fixed non-finite NVFP4 verify outputs on Apple M5.
The 2026-11-27 default-branch batch, versioned on the branch as 0.3.7 and unpublished at this check, fixed a streamed MoE expert-watcher panic when lease extensions evict an expert already routed as a hit, a shadow-tracking panic on streamed MoE models run without speculative drafting, foreground `magnitude serve` printing systemd shutdown instructions when launched from a shell inheriting `INVOCATION_ID`, Vulkan device initialization on GPUs where memory type 0 cannot back storage buffers (Intel Arc Pro B70 on Mesa ANV), a Vulkan long-context prefill panic, and prefetches overwriting in-flight step slot retention.

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
- The catalog is deliberately narrow: 15 curated families with catalog quantizations nothing below 4-bit, because the founders say lower quantizations break thinking and tool calls (since CLI 0.2.11, 2026-10-26, any GGUF of a supported family can be run from the CLI, which widens what loads without changing what the catalog curates).
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
- 2026-10-17 - Recorded the `@magnitudedev/cli` package (0.2.9, published 2026-10-15), which installs the app and connects Claude Code to the loaded local model without a Claude login; the release listing re-fetched the same day.
- 2026-10-28 - CLI train refresh: `@magnitudedev/cli` advanced to 0.2.13 (0.2.11 of 2026-10-26 added custom-GGUF runs of any supported family beyond the curated catalog, 0.2.12 of 2026-10-27 was app polish, and 0.2.13 of 2026-10-28 fixed the Discover page flashing back to assessing), with the catalog caution amended for the custom-model path and the repo pushed 2026-10-28.
- 2026-10-29 - CLI train refresh: `@magnitudedev/cli` 0.2.14 (2026-10-29) made the model catalog sortable by Fastest, using each model's estimated speed on your machine at 50K context, or by Most intelligent, using the catalog's intelligence score, with unrated models last; the repo pushed 2026-10-29; stars stand at their 2026-10-24 verification.
- 2026-10-31 - CLI train refresh: `@magnitudedev/cli` 0.2.15 (2026-10-30) made the engine's Anthropic-compatible messages and token-counting endpoints accept any `anthropic-version` header value, or none, instead of rejecting clients that do not send `2023-06-01`; the repo pushed 2026-10-30; stars stand at their 2026-10-24 verification.
- 2026-11-04 - CLI train refresh: `@magnitudedev/cli` 0.2.16 (2026-11-03) fixed concurrent chats sharing a prompt prefix unloading the model with "target state capacity changed after availability check" and added shared-prefix reuse, requests joining an in-flight shared prefix instead of recomputing it; the repo pushed 2026-11-04; stars stand at their 2026-10-24 verification.
- 2026-11-12 - CLI train refresh: `@magnitudedev/cli` 0.2.17 (2026-11-08) added dot-product CPU kernels for ARM (AWS Graviton and Ampere class), with runtime detection of those instructions on Linux ARM64 builds and the release's own numbers at 4-13x faster prompt processing and 1.4-5x faster generation on Q8_0 versus 0.2.16, plus fixes for a catalog-version deletion removing an image file shared with another installed version, MTP-drafting batch failures, and dropped connections during downloads; the repo pushed 2026-11-12; stars stand at their 2026-10-24 verification.
- 2026-11-17 - Push refresh: the default branch carried a 2026-11-17 batch compiling Metal attention and ordered GEMM kernels on macOS 27, adding a Windows implementation for CPU kernel code memory and symbol lookup, and fixing streamed MoE models crashing the Metal worker on their first request, per-request memory reservation, grouped CPU projections, and a panicking CPU launch poisoning later device uses, with CLI 0.2.17 still the latest release; the repo pushed 2026-11-17; stars stand at their 2026-10-24 verification.
- 2026-11-21 - Push refresh: the releases feed carries only QA-build prereleases since the 11-17 state (npm CLI tags 0.2.97 through 0.2.99 on 2026-11-20 and 11-21 and a cliqa-r3-r0-0.2.17 tag of 2026-11-20, each marked a temporary QA build), with CLI 0.2.17 still the latest stable; the repo pushed 2026-11-21; stars stand at their 2026-10-24 verification.
- 2026-11-24 - Push refresh: a 0.3.0 alpha prerelease train opened on the releases feed (0.3.0-alpha.0 and 0.3.0-alpha.1 on 2026-11-23, 0.3.0-alpha.2 on 2026-11-24, each flagged prerelease, so CLI 0.2.17 stays the latest stable under the standing QA-build reading), and the 2026-11-23 and 11-24 default-branch batch enabled embedded MTP (as the commit titles it) for GLM-5.3 Flash, lowered the recommendations target speed to 10 tok/s, and carried CUDA graph, prefill pipeline, and Vulkan kernel work; the repo pushed 2026-11-24; stars stand at their 2026-10-24 verification.
- 2026-11-26 - Release train refresh with a latest-stable move: CLI 0.3.0 went stable on 2026-11-24 evening (not flagged prerelease, its notes headlined by streaming MoE models larger than GPU memory or system RAM and a CLI-only install path), so the QA-build reading no longer holds the stable fact, and the line patched to 0.3.1 (2026-11-24), 0.3.2, 0.3.3, and 0.3.4 (2026-11-25), and 0.3.5 (2026-11-26, multi-turn reasoning and KV prefix cache preserved across chat templates and tool loops, a non-finite NVFP4 fix on Apple M5); the 11-25 and 11-26 default-branch batch fixed Windows 10 startup, sealed the decode stages streamed Gemma 4 blocks run in, stopped a catalog drafter serving as its own target, moved Vulkan inter-workgroup atomics onto the Vulkan Memory Model, and bounded Windows CUDA VRAM by the WDDM local budget; the repo pushed 2026-11-26; stars stand at their 2026-10-24 verification.
- 2026-11-27 - Release train refresh and rotation re-verification: CLI 0.3.6 shipped 2026-11-27 (faster streamed MoE inference on Apple Silicon and NVIDIA, up to 1.88x faster decode and 2.07x faster prefill with about 2.6 GB less host memory by the release's own numbers, a cap on prefill workspace for large resident MoE models removing 16 to 57 GB of unused allocations on 64K to 256K context models, the sliding-window history limit applied when backing request memory, and Apache-2.0 declared in the Rust workspace and package manifests after license and SBOM tools reported the engine as unlicensed), so CLI 0.3.6 is the latest stable release, with a 0.3.7 patch of six fixes versioned on the default branch (two streamed MoE panics, a foreground serve systemd notice, two Vulkan initialization and prefill fixes, and prefetch holds) unpublished at this check; every cited URL re-fetched live (the repository API, the releases feed, the 0.2.16 release notes, the site, the models page, both Hacker News reads, and issue 141) with the site's benchmark figures and the models page's catalog rows no longer matching the creation reads, both recorded in References, and the launch thread's comment tree counting 96 against the 99 recorded at creation; the repo pushed 2026-11-27; stars stand at their 2026-10-24 verification.

## See also

- [Ollama](../ollama/index.md) - the incumbent free local runtime Magnitude races on speed.
- [Model Access Feature Matrix](../model-access-feature-matrix/index.md) - the category comparison holding this note's column.
- [OpenCode](../../harnesses/opencode/index.md) - a coding harness Magnitude connects to with one click.
- [OpenRouter](../openrouter/index.md) - the hosted alternative when local hardware is the constraint.
- [Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - choosing models once the runtime is settled.

## References

- https://api.github.com/repos/magnitudedev/magnitude - 6,474 stars, 442 forks, Rust, Apache-2.0, pushed 2026-10-07, homepage (fetched via the GitHub API, 2026-10-07; re-fetched 2026-10-14 at 6,717 stars, 464 forks, pushed 2026-10-13; re-fetched 2026-10-17, pushed 2026-10-17; re-fetched 2026-10-19, pushed 2026-10-19; re-fetched 2026-10-21, pushed 2026-10-21; re-fetched 2026-10-23, pushed 2026-10-23; re-fetched 2026-10-24, pushed 2026-10-24; re-fetched 2026-10-25, pushed 2026-10-25; re-fetched 2026-10-26, pushed 2026-10-26; re-fetched 2026-10-28, pushed 2026-10-28; re-fetched 2026-10-29, pushed 2026-10-29; re-fetched 2026-10-31, pushed 2026-10-30; re-fetched 2026-11-04, pushed 2026-11-04; re-fetched 2026-11-07, pushed 2026-11-07; re-fetched 2026-11-08, pushed 2026-11-08; re-fetched 2026-11-12, pushed 2026-11-12; re-fetched 2026-11-14, pushed 2026-11-13; re-fetched 2026-11-17, pushed 2026-11-17, 7,881 stars; re-fetched 2026-11-21, pushed 2026-11-21; re-fetched 2026-11-27, pushed 2026-11-27).
- https://api.github.com/repos/magnitudedev/magnitude/releases - the `@magnitudedev/cli` train (0.2.9 on 2026-10-15) and the desktop-update-acceptance pre-releases (fetched 200, 2026-10-17; re-fetched 2026-10-19, nothing new past the 2026-10-15 entries; re-fetched 2026-10-21 reading @magnitudedev/cli@0.2.10 of 2026-10-20, a memory-planning patch for unified-memory GPUs; re-fetched 2026-10-23 and again 2026-10-24, nothing new past 0.2.10; re-fetched 2026-10-25 and again 2026-10-26, still nothing new past 0.2.10; re-fetched 2026-10-28 reading @magnitudedev/cli@0.2.11 of 2026-10-26 (custom-GGUF runs), 0.2.12 of 2026-10-27, and 0.2.13 of 2026-10-28; re-fetched 2026-10-29 reading @magnitudedev/cli@0.2.14 of 2026-10-29, the catalog-sort release; re-fetched 2026-10-31 reading @magnitudedev/cli@0.2.15 of 2026-10-30, the Anthropic header-tolerance patch; re-fetched 2026-11-04 reading @magnitudedev/cli@0.2.16 of 2026-11-03, the shared-prefix concurrency fix; re-fetched 2026-11-07, still nothing past 0.2.16; re-fetched 2026-11-08, still nothing past 0.2.16; re-fetched 2026-11-12 reading @magnitudedev/cli@0.2.17 of 2026-11-08, the ARM CPU-kernel release; re-fetched 2026-11-21 with 0.2.17 still the newest stable and only QA-build prereleases past it (0.2.97-0.2.99 on 2026-11-20 and 11-21, cliqa-r3-r0-0.2.17 on 2026-11-20; re-fetched 2026-11-27 reading @magnitudedev/cli@0.3.6 of 2026-11-27 the newest stable, the 0.3.0 line's sixth patch past its 2026-11-24 stable release).
- https://api.github.com/repos/magnitudedev/magnitude/releases/tags/%40magnitudedev%2Fcli%400.2.16 - the 0.2.16 release notes: the concurrent-chats fix and the shared-prefix reuse numbers (fetched 200, 2026-11-04; re-fetched 2026-11-27 unchanged)
- https://magnitude.dev/ - positioning, benchmark table (Metal 92% faster decode, CUDA 19%), memory and connector claims, FAQ (200, fetched 2026-10-06; re-fetched 2026-11-27 with the connector list and the Apache-2.0 claim in the fetchable text while the 92% and 19% benchmark figures and the 27% memory claim are no longer in it, so they stand at the 2026-10-06 read).
- https://hn.algolia.com/api/v1/items/49911995 - launch thread: founders, tuning time, benchmark methodology, critical speed measurements, planned per-token cloud (200, fetched 2026-10-06; re-fetched 2026-11-27 at 194 points, the comment tree counting 96 at this fetch).
- https://hn.algolia.com/api/v1/search?query=magnitude&tags=story&numericFilters=created_at_i%3E1758900000 - launch points and date, plus the June 2026 coding-agent pivot story (200, fetched 2026-10-06; re-fetched 2026-11-27, the launch thread still at 194 points).
- https://magnitude.dev/models - the 15-model catalog, quantizations Q4 to Q8, DFlash drafters (200, fetched 2026-10-06; re-fetched 2026-11-27 with DeepSeek V4.1 Flash, Qwen3.8 Flash Next, GLM-5.3 Flash, Qwen3.8 27B, Muse Glimmer 30B, Qwen3.6 35B-A3B, Gemma 4 12B, and Qwen3.5 4B among the listed rows, so the 15-family count stands at the 2026-10-06 read).
- https://github.com/magnitudedev/magnitude/issues/141 - dual-GPU configuration report, multi-GPU unsupported (200, fetched 2026-10-06; re-fetched 2026-11-27, still open).
