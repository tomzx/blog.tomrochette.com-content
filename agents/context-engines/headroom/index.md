---
title: Headroom
created: 2026-10-07
updated: 2026-11-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, compression, token-optimization]
readability: 3
audience_notes: >
  Engineers whose agents burn tokens on tool output, logs, and RAG chunks, and anyone comparing context compression layers.
  Assumes you know what a context window costs per token.
---

Headroom is the Apache-2.0 context compression layer that rewrites everything an agent reads, tool outputs, logs, files, RAG chunks, and conversation history, before it reaches the LLM, keeping the signal and discarding the repetition, with the full originals retrievable on demand.

**Headroom is the generalization of rtk's idea into a product surface: where rtk filters one channel, command output, Headroom compresses every input channel, ships as a library, proxy, agent wrapper, and MCP server at once, and makes the loss reversible through a retrieve tool the model can call back.**

## What it is

A Python and TypeScript library, a zero-code-change proxy (`headroom proxy --port 8787`), a one-command wrapper around fifteen coding agents (`headroom wrap claude|codex|grok|copilot|cursor|aider|opencode|cline|continue|goose|openhands|openclaw|vibe|omp|zcode`), an MCP server, and an opt-in output shaper that trims what the model writes back (verbosity steering at the system-prompt tail, off by default), from headroomlabs-ai (75,468 stars as of 2026-10-18, pushed 2026-11-07).
Compression runs locally: statistical analysis keeps errors, anomalies, and boundaries in JSON arrays, a ModernBERT token classifier squeezes plain text, AST-aware compression (opt-in) collapses function bodies to signatures, an ML router resizes images, and everything removed lands in a Compress-Cache-Retrieve store the model can query through `headroom_retrieve`.
A shared cross-agent memory store deduplicates content across Claude, Codex, Gemini, and Grok sessions, and a `headroom learn` command tunes the compressor.
The docs' reproducible benchmarks (seeded, generated from MCP output formats, gpt-5.6 tokenizer) show 57 percent savings on an SRE incident dump (55,957 to 24,340 tokens), 42 percent on codebase exploration, and 21 percent on code search, with an explicit warning that savings depend on how repetitive your content is.

## Status

Active and compounding fast: created 2026-01-07, 75,468 stars as of 2026-10-18 and 6,184 forks as of 2026-11-08, PyPI package at 0.43.1 (2026-11-05) across 206 releases, 171,340 npm downloads summed for 2026-10-08 to 2026-11-08 (six zero days in the window).
Release v0.41.0 (2026-10-14) added a native Google Antigravity IDE integration, OpenCode 2.x plugin-API support, and the headroom-snip Claude Code mod, the proxy gained turn hooks that rewrite OpenAI Responses requests on HTTP and WebSocket (2026-10-17), release v0.42.0 (2026-10-26) shipped those hooks plus per-request saved-token counts on OutcomeSnapshot and the same tool-savings reporting on the gateway /v1/compress endpoint as the proxy path, and the v0.43 pair (both 2026-11-05) ported the MCP servers to SDK 2.x as a breaking change, answered `headroom_retrieve` on streaming chat completions, added a headroom skill plugin for Claude Code, Codex, Copilot and skills.sh, and put model-routing savings into `headroom savings`, with v0.43.1 fixing a CCR order-queue eviction and a memory-schema key.
Main's unreleased 2026-11-08 batch follows: `headroom wrap droid` adding Factory Droid as a sixteenth wrapped agent, a model-router shadow mode (`HEADROOM_MODEL_ROUTER_LOG_ONLY`) and unified multi-upstream routing for Anthropic Cloud and local oMLX, per-request `cost_usd` in `/stats` recent requests, shared Redis store availability in `/health` and `/metrics`, DeepSeek reported as its own provider, cumulative output tokens carried in savings history checkpoints, Bedrock AWS credentials refreshed before expiry, and `max_body_bytes` applied to the chat completions and responses routes, on top of the 2026-11-06 to 11-07 fix batch (Vertex onboarding failures explained in-band, doctor IPv6 and loopback matching, the Hugging Face tokenizer fix that had silently reverted compression on HF-tokenized models, and Connection-named response-header dropping).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=headroomlabs-ai/headroom&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=headroomlabs-ai/headroom&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=headroomlabs-ai/headroom&type=date&legend=top-left" />
</picture>

Trendshift ranked it the number-one repository of the day during its surge.
The HN footprint is modest for the star count (three submissions, the largest at 10 points in July 2026), a gap worth noticing either as marketing-driven adoption or as a signal that star velocity outran practitioner debate.

## Strengths

- One mechanism (compress, then retrieve on demand) covers every input channel, where channel-specific filters leave logs, RAG, and history uncompressed.
- The retrieve path changes the risk calculus of aggressive compression, since the model can pull back any discarded original instead of hallucinating it.
- Local-only compression with a stated no-content-sent policy keeps the layer palatable for private repos.
- Deployment breadth: the same compressor reaches apps (library), existing agents (wrap), arbitrary HTTP clients (proxy), and MCP clients without code changes.

## Cautions

- The benchmark corpus is generated and seeded rather than production telemetry, and the docs say so; treat the percentages as reproducible upper references, not guarantees for your workload.
- AST-aware code compression is opt-in and off by default, so the default code path is less aggressive than the headline suggests.
- 445 open issues and pull requests as of 2026-10-18 had shrunk to 262 by 2026-11-08, but ten months of explosive growth still signals support strain.
- A compression layer in the hot path is one more thing that can be wrong subtly, and the correctness of what survives compression is exactly as good as the statistical heuristics.
- An anonymous telemetry beacon is on by default; it reports compression ratios, counters, and provider and model IDs, never prompts or code, and turns off with `HEADROOM_BEACON=off`, `HEADROOM_TELEMETRY=off`, `DO_NOT_TRACK=1`, or `HEADROOM_OFFLINE=1`, but default-on phoning home is a fact to weigh before adopting.

## Pricing

Free and open source under Apache-2.0; there is no paid tier, so pricing does not apply.
Costs are your own hardware for the compression pass.

## Compared to

- [rtk](../rtk/index.md): the category's established output filter, Rust, per-command; Headroom is the broader, multi-channel sibling with a retrieve path, rtk the leaner proxy with a longer track record in this section.
- [Repomix](../repomix/index.md): the packer that solves token cost by shrinking what you send once; Headroom solves it by shrinking everything the agent reads continuously.
- [Semble](../semble/index.md): attacks the same bill by retrieving less from an index; Headroom compresses whatever the agent retrieves anyway.

## Bottom line

**Recommended for teams with measurable token spend dominated by tool output, logs, and RAG noise, starting with the proxy on one noisy workflow and auditing what survives compression before trusting it broadly.**
Not as a substitute for retrieval quality (compressing bad context makes bad context cheaper), and not where an unaudited transformation in the agent loop is unacceptable.

## Changes

- 2026-10-07 - Created.
- 2026-10-18 - Recorded release v0.41.0 (native Antigravity IDE integration, OpenCode 2.x plugin support, the headroom-snip Claude Code mod) and the proxy turn-hook work, corrected the wrap count from fourteen to fifteen agents per the README, and refreshed the activity figures.
- 2026-10-25 - Replaced the weekly npm-window adoption claim with the trailing-month figure (159,697 to 2026-10-22) per the trailing-month ruling on npm weekly windows; the 2026-10-24 main-branch fixes carried no release or material change; the stars figure keeps its 2026-10-18 as-of date.
- 2026-10-27 - Recorded release v0.42.0 (2026-10-26: the OpenAI Responses turn hooks released, per-request saved tokens on OutcomeSnapshot, and the gateway /v1/compress endpoint reporting the same tool savings as the proxy path), with the PyPI package at 0.42.0; the stars figure keeps its 2026-10-18 as-of date.
- 2026-11-06 - Full rotation re-verification: every cited URL re-fetched (repository page and README, docs, PyPI, npm range, the HN thread, and the GitHub API all intact, the compression table and seeded benchmark rows unchanged); recorded the v0.43 pair (both 2026-11-05: the breaking MCP SDK 2.x port, `headroom_retrieve` answered on streaming chat completions, a headroom skill plugin for Claude Code, Codex, Copilot and skills.sh, model-routing savings in `headroom savings`, and two CCR and memory fixes in v0.43.1) with PyPI at 0.43.1 across 206 releases; recorded the README's new output-shaper surface (opt-in verbosity steering on what the model writes back, with counterfactual estimated savings and a holdout-measured mode) and its default-on anonymous telemetry beacon with documented opt-outs; refreshed the volatile numbers (6,173 forks, 318 open issues and pull requests, pushed 2026-11-06, 147,968 npm downloads summed for 2026-10-07 to 2026-11-06, eight zero days in the window); the stars figure keeps its 2026-10-18 as-of date.
- 2026-11-07 - Recorded main's unreleased 2026-11-06 to 11-07 fix batch (in-band Vertex failure diagnostics plus a `[vertex]` backend extra, doctor IPv6 and case-variant loopback matching, the HF BatchEncoding token-count fix for silently reverted compression on HF-tokenized models, chatgpt-4o tokenizer aliases, learn-analyzer JSON hardening, Connection-named response-header dropping); no release since v0.43.1.
- 2026-11-08 - Recorded main's unreleased 2026-11-08 batch (`headroom wrap droid` adding Factory Droid as a sixteenth wrapped agent, the model-router shadow mode and unified Anthropic Cloud plus local oMLX routing, per-request `cost_usd` in `/stats`, Redis store health and metrics, DeepSeek as its own provider, cumulative output tokens in savings checkpoints, Bedrock credential refresh, `max_body_bytes` on chat routes) and refreshed the volatile numbers (6,184 forks, 262 open issues and pull requests, pushed 2026-11-08, 171,340 npm downloads summed for 2026-10-08 to 2026-11-08); no release since v0.43.1, so the sixteenth wrap target is unreleased.

## See also

- [rtk](../rtk/index.md) - the channel-specific output filter whose slot Headroom generalizes
- [Repomix](../repomix/index.md) - the one-shot packing alternative to continuous compression
- [Semble](../semble/index.md) - the retrieve-less-instead alternative to the same token bill
- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/headroomlabs-ai/headroom - repository, Apache-2.0 license, deployment surfaces, the agent wrap list, and the CCR store (fetched 200, 2026-10-18)
- https://api.github.com/repos/headroomlabs-ai/headroom - stars, forks, open issues, created date, and push date for the as-of status (fetched 200, 2026-10-18)
- https://docs.headroomlabs.ai/docs - the compression table by content type, the seeded benchmark table with its own caveats, and the framework integrations (fetched 200, 2026-10-18)
- https://pypi.org/pypi/headroom-ai/json - the published package version 0.43.1 across 206 releases (fetched 200, re-fetched 2026-11-08)
- https://api.npmjs.org/downloads/range/2026-10-08:2026-11-08/headroom-ai - 171,340 downloads summed for 2026-10-08 to 2026-11-08, six zero days in the window (fetched 2026-11-08)
- https://api.github.com/repos/headroomlabs-ai/headroom/releases?per_page=6 - the release train: v0.43.0 and v0.43.1 both published 2026-11-05 (fetched 2026-11-06)
- https://hn.algolia.com/api/v1/items/48999841 - the largest Headroom thread, 10 points, July 2026, grounding the modest-HN-footprint observation (fetched 200, 2026-10-18)
