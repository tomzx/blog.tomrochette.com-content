---
title: Headroom
created: 2026-10-07
updated: 2026-10-09
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

A Python and TypeScript library, a zero-code-change proxy (`headroom proxy --port 8787`), a one-command wrapper around fourteen coding agents (`headroom wrap claude|codex|grok|copilot|cursor|aider|opencode|cline|continue|goose|openhands|openclaw|vibe|omp|zcode`), and an MCP server, from headroomlabs-ai (74,783 stars, pushed 2026-10-09, as of 2026-10-09).
Compression runs locally: statistical analysis keeps errors, anomalies, and boundaries in JSON arrays, a ModernBERT token classifier squeezes plain text, AST-aware compression (opt-in) collapses function bodies to signatures, an ML router resizes images, and everything removed lands in a Compress-Cache-Retrieve store the model can query through `headroom_retrieve`.
A shared cross-agent memory store deduplicates content across Claude, Codex, Gemini, and Grok sessions, and a `headroom learn` command tunes the compressor.
The docs' reproducible benchmarks (seeded, generated from MCP output formats, gpt-5.6 tokenizer) show 57 percent savings on an SRE incident dump (55,957 to 24,340 tokens), 42 percent on codebase exploration, and 21 percent on code search, with an explicit warning that savings depend on how repetitive your content is.

## Status

Active and compounding fast: created 2026-01-07, 74,783 stars and 5,797 forks in nine months, PyPI package at 0.40.0, 38,470 npm downloads in the week to 2026-10-07, as of 2026-10-09.

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
- 373 open issues and pull requests against nine months of explosive growth signals support strain.
- A compression layer in the hot path is one more thing that can be wrong subtly, and the correctness of what survives compression is exactly as good as the statistical heuristics.

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

## See also

- [rtk](../rtk/index.md) - the channel-specific output filter whose slot Headroom generalizes
- [Repomix](../repomix/index.md) - the one-shot packing alternative to continuous compression
- [Semble](../semble/index.md) - the retrieve-less-instead alternative to the same token bill
- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/headroomlabs-ai/headroom - repository, Apache-2.0 license, deployment surfaces, the agent wrap list, and the CCR store (fetched 200, 2026-10-07)
- https://api.github.com/repos/headroomlabs-ai/headroom - stars, forks, open issues, created date, and push date for the as-of status (fetched 200, 2026-10-07)
- https://docs.headroomlabs.ai/docs - the compression table by content type, the seeded benchmark table with its own caveats, and the framework integrations (fetched 200, 2026-10-07)
- https://pypi.org/pypi/headroom-ai/json - the published package version 0.40.0 (fetched 200, 2026-10-07)
- https://api.npmjs.org/downloads/point/last-week/headroom-ai - weekly npm download volume for the adoption claim (fetched 200, 2026-10-07)
- https://hn.algolia.com/api/v1/items/48999841 - the largest Headroom thread, 10 points, July 2026, grounding the modest-HN-footprint observation (fetched 200, 2026-10-07)
