---
title: LocalAI
created: 2026-10-10
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, local-inference, self-hosted]
readability: 3
audience_notes: >
  Engineers choosing self-hosted software to serve model access to a team from their own hardware.
  Assumes you know what an OpenAI-compatible endpoint is and what quantization costs in quality.
---

LocalAI is a free, self-hosted inference server that puts locally served open models behind OpenAI, Anthropic, Ollama, and ElevenLabs-compatible APIs, so existing clients keep working with only a base URL change.

## What it is

An MIT-licensed Go server created 2023-03-18 by Ettore Di Giacinto (mudler), originally under the go-skynet org and now at mudler/LocalAI (49,513 stars as of 2026-10-14, pushed 2026-10-28, as of 2026-10-28).
A small core pulls each engine in as a separate on-demand OCI backend image, wrapping llama.cpp, vLLM, SGLang, MLX, whisper.cpp, diffusers, and some sixty backends in total, so one install serves text, voice, vision, image, video, and 3D without becoming a giant download.
The same endpoint carries API key auth, per-user quotas, and role-based access in the free core, plus built-in agents with tool use, MCP, and skills, a 1,255-model gallery, native decision routing behind a /v1/decisions adapter since v4.12.0, and a distributed mode that routes across machines with VRAM-aware placement and failover.
The team also publishes its own native C/C++ engines (parakeet.cpp, vllm.cpp, moss-tts.cpp and more) and the APEX per-layer quantization recipes for mixture-of-experts models.

## Status

Active and shipping monthly: v4.9.0 (2026-08-20), v4.10.0 (2026-09-17), v4.11.0 (2026-10-02), v4.12.0 (2026-10-22), and security-only patch v4.12.1 (2026-10-23), pushed 2026-10-28 (as of 2026-10-28).
v4.12.0 redesigned the web UI and added streaming voice responses, native decision routing, image upscaling, and persistent Qdrant stores; its release notes count top-level gallery entries at 1,896 while the site's own gallery counter still reads 1,255 (checked 2026-10-23).
v4.12.1 hardens the external URL policy for user-supplied URLs against SSRF, validating redirect targets on every hop and treating non-public address ranges as blocked.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=mudler/LocalAI&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=mudler/LocalAI&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=mudler/LocalAI&type=date&legend=top-left" />
</picture>

The site reports 256 code contributors, a 3,187-member Discord, and eight translated README languages (as of 2026-10-23, per the project's own counts; the contributor count was 252 at the 2026-10-10 creation read).
Hacker News knows local AI the concept far more than LocalAI the product: title and URL searches surface concept essays in the thousands of points while the project's own thread there is its July 2026 engine-writing post at 134 points.

## Strengths

- The broadest drop-in compatibility surface in the family: OpenAI, Anthropic, Ollama, and ElevenLabs APIs over one endpoint, so most tools need a URL change and nothing else.
- Multi-user controls (API keys, per-user quotas, usage attribution, RBAC) ship in the free MIT core, the part hosted gateways and LiteLLM gate behind paid tiers.
- One engine per model means a client never notices a swap, and the composable backend images keep the base install small.
- Every feature carries a tested CPU-first path across NVIDIA, AMD, Intel, Apple Silicon, and Vulkan, not a degraded GPU-only story.

## Cautions

- Serving locally does not change what local quantized models are: the strongest critical field report I found documents looping, hallucinated tool calls, and code-review failures on long-horizon agent work even on a rig near $15,000 of GPU, so the ceiling is the weights, not the server.
- The APEX speed and size claims are self-published benchmarks on self-chosen workloads, though the project does print the perplexity trade alongside them.
- The surface is enormous (sixty-plus backends, video, 3D, agents, distributed clustering), which multiplies the maintenance and security perimeter well beyond what serving tokens requires.
- There is no hosted path and no published support offering beyond a contact email, so productionizing it is entirely on you.

## Pricing

Pricing does not apply: the core is free and open source under MIT with no paid tier, no hosted plan, and no token costs, and the only commercial paths are sponsorship (Spectro Cloud is the visible backer) and a contact email for business inquiries, as of 2026-10-10.

## Compared to

- [Ollama](../ollama/index.md): the one-command runtime with the registry and now paid cloud tiers; choose it for simplicity, LocalAI for multi-user controls, engine choice per model, and modalities beyond text.
- [Magnitude](../magnitude/index.md): the self-optimizing engine tuning kernels on your device; LocalAI chooses between engines instead of writing a faster one.
- [LiteLLM](../litellm/index.md): the self-hosted gateway over cloud provider APIs; the two are adjacent slots, and a stack can run both, LocalAI serving weights and LiteLLM routing the cloud fallback.

## Bottom line

**Recommended for teams that must serve open models from their own hardware to more than one user, with quotas and access control, on mixed or GPU-less hardware.**
Not for a single developer who wants one command and a registry (Ollama's slot), and not for anyone who needs frontier-model quality per token, where the hosted gateways and vendor plans in this category remain the answer.

## Changes

- 2026-10-10 - Created when this run's rafska/awesome-local-llm scan surfaced the family gap next to Ollama.
- 2026-10-23 - v4.12.0 released 2026-10-22 (redesigned web UI, streaming voice, native decision routing via /v1/decisions, image upscaling, persistent Qdrant stores); the release notes count top-level gallery entries at 1,896 against the site counter's 1,255, and the site's contributor count moved from 252 to 256.
- 2026-10-24 - Release refresh: security-only patch v4.12.1 (2026-10-23) hardened the external URL policy for user-supplied URLs against SSRF, with the repo pushed 2026-10-24.

## See also

- [Ollama](../ollama/index.md) - the registry-and-daemon incumbent this note sits beside in the local-serving family
- [Magnitude](../magnitude/index.md) - the kernel-tuning engine betting on speed where LocalAI bets on coverage
- [llamafile](../llamafile/index.md) - the distribute-instead-of-serve answer for the same open weights
- [LiteLLM](../litellm/index.md) - the self-hosted gateway for the cloud providers LocalAI does not serve
- [Model Access Feature Matrix](../model-access-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/mudler/LocalAI - 49,453 stars, 4,491 forks, MIT, created 2023-03-18, pushed 2026-10-10, homepage localai.io (fetched via the GitHub API, 2026-10-10; re-fetched 2026-10-14 at 49,513 stars, pushed 2026-10-14; re-fetched 2026-10-18, pushed 2026-10-17; re-fetched 2026-10-19, pushed 2026-10-19, v4.11.0 still latest; re-fetched 2026-10-21, pushed 2026-10-21, v4.11.0 still latest; re-fetched 2026-10-23, pushed 2026-10-23, v4.12.0 latest; re-fetched 2026-10-24, pushed 2026-10-24, v4.12.1 latest; re-fetched 2026-10-26, pushed 2026-10-26, v4.12.1 still latest; re-fetched 2026-10-28, pushed 2026-10-28, v4.12.1 still latest).
- https://raw.githubusercontent.com/mudler/LocalAI/master/README.md - backend architecture, the 4.11.0 release news, the native engine list, MIT license, and team (fetched 200, 2026-10-10)
- https://localai.io/ - the OpenAI, Anthropic, Ollama, and ElevenLabs compatibility claim, the 1,255-model gallery, APEX quantization tables with the perplexity trade, and the 252-contributor and Discord counts (fetched 200, 2026-10-10; re-fetched 2026-10-23 with the gallery counter still at 1,255 and the contributor count now 256).
- https://api.github.com/repos/mudler/LocalAI/releases - v4.9.0 (2026-08-20), v4.10.0 (2026-09-17), v4.11.0 (2026-10-02), the monthly cadence (fetched 200, 2026-10-10; re-fetched 2026-10-23 reading v4.12.0 of 2026-10-22; re-fetched 2026-10-24 reading v4.12.1 of 2026-10-23; re-fetched 2026-10-26, nothing new past v4.12.1; re-fetched 2026-10-28, still nothing new past v4.12.1).
- https://api.github.com/repos/mudler/LocalAI/releases/tags/v4.12.0 - the v4.12.0 release notes: web UI redesign, streaming voice, native decision routing, image upscaling, Qdrant stores, and the 1,660-to-1,896 top-level gallery-entry count (fetched 2026-10-23).
- https://hn.algolia.com/api/v1/search?query=LocalAI&tags=story&hitsPerPage=8 - the HN footprint: concept essays dominate while the product itself barely appears (fetched 200, 2026-10-10)
- https://hn.algolia.com/api/v1/search?query=localai&restrictSearchableAttributes=url&tags=story&hitsPerPage=6 - the project's own engine post at 134 points and 51 comments (July 2026), the largest direct HN presence found (fetched 200, 2026-10-10)
- https://blog.alexellis.io/local-ai-is-not-opus/ - the critical source: looping, hallucination, and quantization ceilings on long-horizon agent work even on high-end hardware, with the local-versus-plan cost framing (fetched 200, 2026-10-10)
