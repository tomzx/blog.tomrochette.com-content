---
title: Ollama
created: 2026-09-27
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, local-inference, model-registry]
readability: 3
audience_notes: >
  For engineers weighing local model runs against cloud subscriptions for coding agents.
  Assumes you know what quantization costs in quality and what an OpenAI-compatible endpoint is.
---

Ollama is the most popular local model runtime, a free open-source app that runs open models on your own hardware, with a model registry, a CLI, a desktop app, and a local OpenAI-compatible API, now paired with a paid cloud service.

**Ollama is no longer just the local runtime: its homepage now leads with cloud models for coding agents, and the local app has become the on-ramp to a $20-per-month subscription.**

## What it is

A Go server (MIT) that downloads and runs open models such as Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, and Gemma on laptop and desktop hardware, fronted by a CLI, a desktop app, and a local API that speaks Ollama, OpenAI, and Anthropic formats.
It launched in 2023 as "Docker for LLMs" out of a Y Combinator W21 team, and ollama.com now claims 9M+ monthly installs, 1B+ model downloads, and 200T+ tokens served (re-verified unchanged 2026-10-23).
The registry curates quantizations of each model, and `ollama run <model>` is the one-command experience that agent integrations (Claude Code, Codex, OpenCode) build on.

## Status

Very active: 183,371 stars as of 2026-10-16, repo pushed 2026-10-23 (as of 2026-10-24), among the largest repositories in the AI ecosystem.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ollama/ollama&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ollama/ollama&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ollama/ollama&type=date&legend=top-left" />
</picture>

The surface is expanding fast: MLX acceleration on Apple silicon arrived in preview with 0.19 in March 2026, and NVFP4 quantization is now supported alongside the GGUF classics.
Cloud models launched as Ollama Turbo in August 2025, and the plans were rebuilt into Free, Pro, Max, and Team tiers by late September 2026.
The 0.40 line keeps shipping: v0.40.9 (2026-10-22, after v0.40.7 and v0.40.8) added speech generation with Phonon on Apple Silicon behind an OpenAI-compatible /v1/audio/speech endpoint and brought vLLM Semantic Router's d3 decision models (2B to 27B) into the registry, a second decision-model surface after LocalAI's own.
v0.40.10 (2026-10-23) added NVIDIA's Nemotron 3.5 Bolt E4B, a Gemma 4-based vision-language model with a 128K context window and a DFlash drafter for speculative decoding, and v0.40.11-rc0 was cut 2026-10-24.
**The pivot is genuine: a tool whose brand was local and private now sells US, Europe, and Singapore-hosted cloud inference through NVIDIA cloud partners, with the local runtime free underneath.**

## Strengths

- The easiest on-ramp to local models: one command pulls and runs a model on macOS, Windows, and Linux, with GPU acceleration.
- Local inference is genuinely free and unlimited, and nothing leaves the machine, which matters for private codebases.
- The local API accepts OpenAI and Anthropic clients, so coding agents can point at it with a base URL change.
- MLX on Apple silicon (0.19 preview) roughly doubled prefill and decode throughput in the project's own March 2026 tests.
- Cloud pricing is legible: included dollar credits, half-price off-peak rates, and no rate limits beyond concurrency caps.

## Cautions

- Local hardware caps quality: laptop-class quantizations (Q4-style) of 30B models lose to cloud frontier models on hard coding work, so the free tier buys privacy and tinkering more than capability.
- The project has a long attribution fight with llama.cpp, its original engine, and mid-2025 it forked onto a custom ggml backend that reintroduced fixed bugs and trails upstream throughput in community benchmarks.
- Registry naming can mislead: `deepseek-r1` long pointed at a small distilled model, not the 671B original.
- Curated quantizations are limited (mostly Q4_K_M and Q8_0), so power users still leave for llama.cpp or LM Studio.
- CVE-2025-51471 let a malicious registry server exfiltrate auth tokens during pulls, and the fix landed slowly.
- Cloud prompts route to third-party NVIDIA cloud partners; Ollama promises no logging and no training, but the data does leave your machine.

## Pricing

Local runtime: free and unlimited, MIT licensed, no account needed.
Cloud plans (re-verified unchanged 2026-10-23): Free $0 with starter credits, Pro $20/month ($200/year, $16.67 per month billed annually) including $60 of usage credits, Max $100/month including $300, Team $500/month including $1,000 shared, Enterprise custom.
Cloud models bill per million tokens (glm-5.3 $1.40 in / $4.40 out, deepseek-v4.1-flash $0.30/$1.20, kimi-k3 $3/$15), with roughly half-price off-peak rates outside 12:00-18:00 UTC on weekdays and all weekend.
Concurrency caps: Free 1 request, Pro 3, Max and Team 10, and unused included credits do not roll over.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2025-08-05 | Cloud | Cloud models launch as Ollama Turbo, a subscription for hosted open models (430-point HN thread) | https://hn.algolia.com/api/v1/search?query=Ollama&tags=story&hitsPerPage=8 |
| 2026-09-27 | Tiers | Baseline as published: Free $0, Pro $20/mo ($60 credits), Max $100/mo ($300), Team $500/mo ($1,000 shared), per-token model table with off-peak discounts | https://ollama.com/pricing |

## Compared to

Hosted gateways like [OpenRouter](../openrouter/index.md) give frontier quality with zero hardware; choose Ollama local when privacy or offline use dominates, and Ollama cloud when you want one bill for open models.
llama.cpp and LM Studio cover the same local niche with more quantization choice and (per community benchmarks) higher throughput, at the cost of more setup.
As a gateway, Ollama is narrow: it fronts its own registry and cloud, not 100+ providers.

## Bottom line

Recommended for developers who want open models running privately on their own machine, and for agents whose data cannot leave the device.
Not for maximum quality per dollar on hard coding tasks, where cloud frontier models win and the local free tier mainly buys privacy.
My disagreeable claim: for coding agents on 16GB laptops, local quantized models are a toy, and Ollama's own pivot to selling cloud credits quietly admits it.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars scan surfaced it.
- 2026-10-04 - Homepage claim corrected from more than 9 million developers to 9M+ monthly installs (with 1B+ model downloads and 200T+ tokens served); stars refreshed.
- 2026-10-06 - Converted the Compared-to cross-references from plain-text paths into working links.
- 2026-10-07 - Added the ollama/ollama star history chart to the Status section.
- 2026-10-23 - Rotation re-verification with the release train: v0.40.7 (2026-10-18), v0.40.8 (2026-10-21), and v0.40.9 (2026-10-22) shipped, the last adding Phonon speech generation behind the OpenAI-compatible /v1/audio/speech endpoint and the d3 decision-model family (2B to 27B); every cited source re-fetched live with the pricing tiers, site counters, and model-table rows unchanged.
- 2026-10-24 - Release train refresh: v0.40.10 (2026-10-23) added NVIDIA's Nemotron 3.5 Bolt E4B, a Gemma 4-based vision-language model with a 128K context window and a DFlash drafter, and v0.40.11-rc0 followed on 2026-10-24.

## See also

- [OpenRouter](../openrouter/index.md) - the hosted multi-provider alternative when local hardware is the bottleneck.
- [Assistant runtimes](../../assistant-runtimes/_index.md) - local assistant products that ride on runtimes like this one.
- [OpenCode](../../harnesses/opencode/index.md) - a coding harness that runs against local Ollama endpoints.
- [Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - choosing models once the access path is settled.
- [Model provider feature matrix](../../model-provider-feature-matrix/index.md) - where Ollama sits among access providers.

## References

- https://api.github.com/repos/ollama/ollama - 182,429 stars, Go, MIT, pushed 2026-10-07 (fetched via the GitHub API, 2026-10-07; re-fetched 2026-10-14 at 183,051 stars; re-fetched 2026-10-18, pushed 2026-10-18; re-fetched 2026-10-19, pushed 2026-10-18 unchanged; re-fetched 2026-10-21, pushed 2026-10-20, v0.40.6 still the latest stable; re-fetched 2026-10-23, pushed 2026-10-23, v0.40.9 latest; re-fetched 2026-10-24, pushed 2026-10-23, v0.40.10 latest).
- https://api.github.com/repos/ollama/ollama/releases - the 0.40.x train (fetched 2026-10-23: v0.40.7 of 2026-10-18, v0.40.8 of 2026-10-21, v0.40.9 of 2026-10-22, whose notes carry the Phonon speech feature and the d3 decision models; re-fetched 2026-10-24: v0.40.10 of 2026-10-23 with the Nemotron 3.5 Bolt notes, and v0.40.11-rc0 of 2026-10-24).
- https://ollama.com/ - current positioning: 9M developers, coding-agent integrations, Pro/Max teaser, cloud regions (200, re-fetched 2026-10-21 with the 9M+/1B+/200T+ counters unchanged; re-fetched 2026-10-23 unchanged).
- https://ollama.com/pricing - all tiers, included credits, per-token model table, off-peak terms, concurrency caps, FAQ (200, re-fetched unchanged 2026-10-06, 2026-10-14, and 2026-10-21; re-fetched 2026-10-23 with tiers, credits, caps, and the cited model rows unchanged).
- https://docs.ollama.com/ - local API surface: Ollama, OpenAI, and Anthropic-compatible clients, cloud vs local split (200, re-fetched 2026-10-21; re-fetched 2026-10-23 unchanged).
- https://ollama.com/blog/mlx - MLX preview in 0.19, M5 benchmarks, NVFP4 support, 32GB+ memory requirement (200, re-fetched 2026-10-21; re-fetched 2026-10-23 unchanged).
- https://sleepingrobots.com/dreams/stop-using-ollama/ - critical history: llama.cpp attribution, ggml fork, model naming, registry limits, CVE-2025-51471 (200, re-fetched 2026-10-21; re-fetched 2026-10-23 unchanged).
- https://hn.algolia.com/api/v1/search?query=Ollama&tags=story&hitsPerPage=8 - MLX and Turbo launch dates, plus the 648-point "ecosystem doesn't need Ollama" thread (200, re-fetched 2026-10-21; re-fetched 2026-10-23 unchanged).
