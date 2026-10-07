---
title: Supermemory
created: 2026-10-04
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, agent-memory, context-engine, open-source]
readability: 3
audience_notes: >
  Engineers choosing a memory layer for an AI product or coding agent who want the
  benchmark-heavy entrant profiled against Mem0, Zep, and the file convention.
  Assumes you know what extraction pipelines, embeddings, and MCP are.
---

Supermemory is a hosted memory-and-context engine for AI applications that extracts facts from conversations, maintains user profiles, and serves hybrid retrieval, with an MIT-licensed one-binary local mode and an open-source MCP server.

**Supermemory is the most benchmark-aggressive product in agent memory: it claims first place on all three major memory benchmarks at once, which is either the field's best evidence or its best marketing, and no independent run I could find settles which.**

## What it is

A memory API (TypeScript and Python SDKs, REST) whose engine extracts facts from conversations, tracks updates, resolves contradictions, and expires stale information, layered with user profiles served in about 50ms, hybrid RAG-plus-memory search, connectors (Google Drive, Gmail, Notion, OneDrive, GitHub), and multimodal extractors for PDFs, images, video, and code.
Surfaces for agents include a hosted MCP server (the server code is open source) and installable plugins for Claude Code, Cursor, Codex, and OpenCode, plus coding-agent skills.
**Supermemory local** ships the same engine as a single self-hosted binary (embeddings default to a local model, any LLM works via your own key, data lives in one `./.supermemory` directory, fully offline against Ollama).
The company describes itself as a research lab; the repository began under founder Dhravya Shah's personal account and now lives in the supermemoryai organization.

## Status

**Active and large, with adoption that outruns its discussion footprint.**
About 31.1k stars, 2,739 forks, and 94 open issues and pull requests as of 2026-10-07, created 2024-02-27, pushed 2026-10-06 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=supermemoryai/supermemory&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=supermemoryai/supermemory&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=supermemoryai/supermemory&type=date&legend=top-left" />
</picture>

The npm SDK pulled 487,187 downloads in the trailing month (2026-09-05 to 2026-10-04) and the SDK lines moved to a 5.x major in one day: npm at 5.0.1 and PyPI at 5.0.0 (uploaded 2026-10-06, after three release candidates), up from 3.62.0.
The hosted platform claims 1T+ tokens processed per month and tens of millions of end users (vendor figures).
The community record is thin for the star count: its largest Hacker News story threads sit at 5 points or fewer, and the README's three first-place benchmark claims have not been independently replicated in any source I could verify, though a competing project's preliminary run (below) tested it and published a worse-than-claimed number.

## Strengths

- **The local mode is unusually complete for a hosted-first memory vendor**: one binary, local embeddings by default, offline-capable against Ollama, and the same API surface as the cloud, which makes the lock-in conversation different from Mem0's.
- Scope spans the whole context stack: memory, user profiles, RAG, connectors, and file processing in one system, so teams do not assemble the pipeline from parts.
- It publishes its evaluation harness (MemoryBench) as an open-source framework for comparing memory providers head to head, including its rivals.
- Agent-facing surfaces are first-class: hosted MCP, plugins for the major coding CLIs, and skills, not just an HTTP API.

## Cautions

- **Every performance claim traces to the vendor**: "#1 on LongMemEval, LoCoMo, and ConvoMem" is the README's own table, with methodology on the vendor's research page.
- The one independent datapoint I found cuts against the claims: the CodeAlmanac team's preliminary LoCoMo run at a 2,000-token budget scored Supermemory at 47.6 percent, below plain BM25 at 51.8 and Mem0 at 60.6 (their disclaimer: LoCoMo tests conversational memory, not their use case, and they published the numbers anyway).
- The Hacker News footprint is nearly absent for a 31k-star repository, the same stars-ahead-of-discussion pattern this section flagged on Graft, Graphify, and Knowhere.
- "Memory is not RAG" is the marketing frame, but the product sells both together, and the metering (below) charges separately for each layer.

## Pricing

Hosted plans as of 2026-10-04: Free $0 per month with $5 of credits renewed monthly; Pro $19 per month with $20 of credits; Max $100 per month with $130 of credits; Scale $399 per month with $600 of credits, unlimited team seats, SOC 2 and HIPAA BAA, and a self-hosted option.
Metering is in "SM tokens": plain text $5 per 1M, rich content $10 per 1M, SuperRAG retrieval $1 per 1M text tokens, queries $5 per 1M, and operations $100 per 1M.
Supermemory local is free (MIT).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-04 | Free, Pro, Max, Scale | Baseline: Free $0 ($5 monthly credits), Pro $19/mo ($20 credits), Max $100/mo ($130 credits), Scale $399/mo ($600 credits), SM-token metering $1-$10 per 1M; local mode free (MIT). | [supermemory.ai/pricing](https://supermemory.ai/pricing) |

## Compared to

- [Mem0](../mem0/index.md): the adoption leader of the same hosted-API kind; Mem0's OSS SDK is the more embedded default, Supermemory's local binary is the more complete self-host, and their benchmark claims directly collide.
- [Zep](../zep/index.md): temporal graphs with audit-grade provenance; choose Zep when invalidation over time and governance outrank raw recall scores, Supermemory when you want the benchmark-forward engine.
- [File-based agent memory](../file-based-agent-memory/index.md): still the zero-cost default for a coding agent in one repo; Supermemory earns its keep for cross-user, cross-app product memory.

## Bottom line

**Recommended for product teams that want memory plus RAG plus connectors from one vendor and will run MemoryBench on their own workload before believing the #1 claims.**
Not for teams that need an independent benchmark record first (it does not exist yet), or for solo coding-agent use, where files remain the right answer.
My disagreeable claim: Supermemory's local binary is strategically more interesting than its benchmark table, because "the hosted memory vendor that lets you leave" is the position Mem0 left open.

## Changes

- 2026-10-04 - Created from the 2026-10-04 entrant scan, after Graphify's own benchmark table surfaced it as the QA-accuracy rival and the citation bar was met with eight fetched sources.
- 2026-10-07 - Added the supermemoryai/supermemory star history chart to the Status section.
- 2026-10-07 - Recorded the SDK's 3.62.0 to 5.0.0 major jump (PyPI, after three release candidates on October 5 and 6; npm in sync at 5.0.1), six weeks after 3.62.0.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [Mem0](../mem0/index.md) - the adoption leader whose benchmark claims Supermemory directly contests
- [Zep](../zep/index.md) - the temporal-graph alternative for facts that invalidate
- [Graphify](../../context-engines/graphify/index.md) - the context-engine whose self-published benchmarks treat Supermemory as the accuracy bar
- [File-based agent memory](../file-based-agent-memory/index.md) - the free convention that covers the single-agent case

## References

- https://github.com/supermemoryai/supermemory - repository, MIT license, 31.1k stars and activity as of 2026-10-05 (the Dhravya/supermemory URL redirects here)
- https://raw.githubusercontent.com/supermemoryai/supermemory/main/README.md - engine architecture, local mode, benchmark claims, MemoryBench, plugin and MCP surfaces
- https://supermemory.ai/pricing - the four hosted plans, SM-token metering rates, and the Scale-tier compliance stack, as of 2026-10-04
- https://supermemory.ai - platform claims (1T+ tokens per month, 187ms median recall) and the benchmark figure positioning
- https://api.npmjs.org/downloads/point/last-month/supermemory - 487,187 trailing-month SDK downloads (2026-09-05 to 2026-10-04), fetched 2026-10-06
- https://pypi.org/pypi/supermemory/json - Python SDK 5.0.0 (2026-10-06), the record of the 3.62-to-5.0 jump
- https://news.ycombinator.com/item?id=48995181 - the CodeAlmanac thread carrying the one independent LoCoMo datapoint (Supermemory 47.6 percent at a 2k budget)
- https://hn.algolia.com/api/v1/search?query=supermemory&tags=story - the footprint scan grounding the thin-HN observation (top tool-related thread 5 points, 2024)
