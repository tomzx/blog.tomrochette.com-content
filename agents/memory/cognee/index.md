---
title: Cognee
created: 2026-08-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, memory, agent-memory, knowledge-graphs, open-source]
readability: 3
audience_notes: >
  Engineers choosing a memory layer for agents who want the self-hostable graph option profiled.
  Assumes you know what a knowledge graph is and what running vector, graph, and relational backends involves.
---

Cognee is Topoteretes' open-source AI memory platform: a pipeline that turns documents and interactions into graph-plus-vector memory you can run entirely yourself, with an optional flat-priced cloud.

**Cognee is the self-hoster's memory platform: the entire engine, including the parts Mem0 and Zep keep behind the paid tier, is Apache-2.0, and the trade is that you operate the graph, vector, and relational backends yourself.**

## What it is

**An Apache-2.0 Python library plus TypeScript and Rust SDKs, a CLI, an HTTP server, and an MCP integration, all built around one pipeline: data in, knowledge graph plus vector and relational stores out.**
Multi-user mode is documented, and the vendor lists agentic integrations with Claude Code, Codex, and MCP.
Cognee Cloud runs the same engine managed, on gpt-oss-120b, OpenAI's open-weight model.

## Status

**Active and fast-moving.**
About 31k GitHub stars as of 2026-09-26, repository pushed 2026-09-26 UTC, and v1.6.1 (September 24, 2026) the latest release per the PyPI JSON API.
v1.6.0 is the keyless-first release: many flows now run with no LLM key, pipelines stamp runs at start and recover after crashes, a cognee-mcp client/server package lands for integrations, and the default Docker image drops GLiNER, a breaking change self-hosters must patch around.
v1.6.1 (September 24) adds Google Drive and Gmail ingestion with the Google connectors bundled into the SDK, chunked graph-visualization streaming for large subgraphs, and a GLiNER installer that defers the CPU Torch download to first use, and it promotes dlt to a core dependency, which breaks source installs that manage dependencies manually.
The company is part of the Berkeley Xcelerator and claims 5M+ SDK runs per month (vendor figure).
The community discussion footprint is thin for the star count: its two Show HN threads drew 9 and 6 points, so third-party scrutiny lags the repository's popularity.

## Strengths

- **The whole engine is open**: no Mem0-style split between an OSS SDK and a paid brain, and no Zep-style discontinued community edition.
- Flat, legible cloud pricing, a per-token rate instead of seats or credits, with unlimited users on every tier.
- Broad integration surface for one product: Python, TypeScript, and Rust SDKs, MCP, HTTP API, and CLI.
- Cloud defaults to an open-weight model (gpt-oss-120b) rather than steering you into a frontier vendor.

## Cautions

- **You are the operations department**: self-hosting means running graph, vector, and relational backends, the heaviest footprint of the memory options profiled here.
- The vendor publishes its own "Cognee vs Zep" and "Cognee vs mem0" comparisons, which are marketing, not benchmarks.
- Thin third-party discussion means fewer independent failure reports, and fewer independent fixes.
- The 1.x line is young and releasing almost weekly; expect churn between minor versions.

## Pricing

Open source: free, Apache-2.0.
Cloud: Free $0 (one workspace, 1M tokens included, unlimited users), Standard $1.00 per 1M tokens processed plus $5 per additional workspace per month, Enterprise custom with BYO cloud and SLAs, as of 2026-09-22.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-09 | Cloud Standard | Standard rate cut to $1.00 per 1M tokens processed. | [cognee.ai/pricing](https://www.cognee.ai/pricing) |
| 2026-09-18 | All tiers | Re-verified: Cloud Free $0 (one workspace, 1M tokens), Standard $1.00 per 1M plus $5 per additional workspace/mo, Enterprise custom; OSS free (Apache-2.0). | [cognee.ai/pricing](https://www.cognee.ai/pricing) |

## Compared to

- [mem0](../mem0/index.md): both are memory APIs with an OSS story; cognee's openness is complete where Mem0's benchmarked brain is the paid platform.
- [Zep](../zep/index.md): Zep's bi-temporal invalidation directly addresses contradiction over time; Cognee's pricing page now lists bi-temporal memory and conflict resolution too, but only as an Enterprise BYOC engagement feature rather than something I could verify in the open engine.
- [File-based agent memory](../file-based-agent-memory/index.md): for a coding agent in one repository, files remain the zero-operations default.

## Bottom line

**Recommended for teams that need multi-user graph memory and will run the stack themselves, or want flat per-token cloud billing.**
Not for solo coding-agent work, where plain files win, or for anyone without the appetite to operate three storage backends.

## Changes

- 2026-08-26 - Created as a Memory note after an entrant scan, citing seven verified sources.
- 2026-09-06 - Recorded that contradiction handling is now documented on the pricing page as an Enterprise BYOC feature.
- 2026-09-09 - Standard cloud price cut from $2.50 to $1.00 per 1M tokens; note, matrix cell, and choosing bullet updated.
- 2026-09-20 - Recorded v1.6.0 (September 18): keyless-first flows, crash-recovering pipelines, a cognee-mcp client/server package, and GLiNER removed from the default Docker image.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-25 - Recorded v1.6.1 (September 24): Google Drive and Gmail sync with bundled connectors, chunked visualization streaming, a deferred-install GLiNER setup, and dlt promoted to a core dependency; refreshed stars to about 31k.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - this note's column against the other four approaches
- [mem0](../mem0/index.md) - the hosted-first counterpart
- [Zep](../zep/index.md) - the temporal-graph counterpart
- [Context Management Patterns](../../context-management-patterns/index.md) - where memory sits among the other context techniques

## References

- https://github.com/topoteretes/cognee - source, Apache-2.0, about 31k stars, as of 2026-09-26
- https://www.cognee.ai/ - v1 announcement, integration list, Berkeley Xcelerator, 5M+ SDK runs claim
- https://www.cognee.ai/pricing - cloud tiers, per-token rate, workspace fee, gpt-oss-120b default, Enterprise bi-temporal memory listing, as of 2026-09-25 (the $1.00 Standard rate held since the 2026-09-09 cut)
- https://docs.cognee.ai/ - architecture, multi-user mode, SDK and integration surfaces
- https://pypi.org/pypi/cognee/json - v1.6.1 released September 24, 2026
- https://news.ycombinator.com/item?id=44169594 - Show HN, June 2025, the 9-point thread
- https://news.ycombinator.com/item?id=43031915 - Show HN, February 2025, the 6-point thread
