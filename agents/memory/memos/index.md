---
title: MemOS
created: 2026-10-06
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, agent-memory, knowledge-graphs, open-source]
readability: 3
audience_notes: >
  Engineers choosing a memory layer for agents, particularly those running OpenClaw-family
  assistants or DeepSeek Harness, who want the graph-backed platform option profiled.
  Assumes you know what vector and graph stores involve.
---

MemOS is MemTensor's Apache-2.0 memory operating system for LLMs and agents: a graph-backed memory engine with one API to add, retrieve, edit, and delete memory, shipped as a Python SDK, a self-hosted Docker stack, local plugins for agent harnesses, and a hosted cloud.

**Its bet is that memory should meet the agent where it already runs: official plugins for OpenClaw, Hermes, and DeepSeek Harness carry the same core from fully-local SQLite up to a shared graph platform.**

## What it is

MemOS 2.0 ("Stardust") from MemTensor, with the arXiv paper (2507.03724) behind the architecture.
The engine unifies store, retrieve, and manage for long-term memory: a graph you can inspect and edit rather than a black-box embedding store, multi-modal memory (text, images, tool traces, personas), MemCube knowledge bases with isolation and controlled sharing, asynchronous ingestion through MemScheduler, and natural-language memory feedback for correcting or replacing existing memories.
Four entry points: a hosted cloud API, self-hosting via docker compose against Neo4j plus Qdrant, and cloud or fully-local plugins.
The plugin line is the distribution strategy: official OpenClaw plugins (cloud and local, March 2026), Hermes Agent local plugins (April and May 2026), and a DeepSeek Harness connection (August 2026) that adds automatic recall and background capture to dsh without modifying its core.

## Status

**Active and mid-scale.**
11,755 stars with the repository pushed 2026-09-29, created 2025-07-06, as of 2026-10-08 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=MemTensor/MemOS&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=MemTensor/MemOS&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=MemTensor/MemOS&type=date&legend=top-left" />
</picture>

Latest engine release v2.0.34 (2026-09-23) and local-plugin release v2.0.20 (2026-09-21) per the GitHub releases API; the PyPI package is at 0.37.0, Apache-2.0.
The benchmark table is the vendor's own: LoCoMo 88.83 and LongMemEval 89.20 via OmniMemEval, the company's self-published evaluation framework spanning 14 commercial memory products.
The Hacker News footprint is nearly absent: a 2-point story in August 2025, no discussion since.

## Strengths

- **The plugin strategy is the best harness coverage in the category**: OpenClaw, Hermes, and DeepSeek Harness each have official local or cloud plugins, so one memory core follows agents that rarely share memory conventions.
- The local plugins are SQLite-based and 100 percent on-device, a real offline path, with the graph platform as the upgrade rather than the requirement.
- MemCube knowledge bases give multi-user and multi-project isolation with controlled sharing, which most local options skip entirely.
- Memory feedback through natural language (correct, supplement, replace) is a usable correction story without a bi-temporal model.

## Cautions

- **Every benchmark number is the vendor's own run of its own framework**, the same self-published pattern this section flags on Supermemory and Mem0, with no independent replication found.
- The hosted cloud API's endpoints sit on MemTensor's own infrastructure (memtensor.cn), a data-residency question for teams outside its jurisdiction, and the newly published Starter and Pro tiers are launch-promo-free, so their real prices are the $19 and $286 list figures.
- Self-hosting the full platform means operating Neo4j plus Qdrant, a heavier stack than the SQLite-only plugins suggest.
- Independent discussion is thin (a 2-point HN thread), so failure reports and fixes skew toward the vendor's channels.

## Pricing

Free and open: the engine, the PyPI package, and the local plugins are Apache-2.0.
The hosted cloud now publishes plans as of 2026-10-08: Free $0/month (50k add and 20k search calls, 3M input and 1M output chat tokens, up to 10 knowledge bases), Starter and Pro listed at $19 and $286/month and both currently flagged "Free Now" on an apply-to-join basis, and Enterprise custom.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-07 | Free, Starter, Pro, Enterprise | Baseline: Free $0/mo; Starter $19/mo and Pro $286/mo both temporarily free ("Free Now", apply now); Enterprise custom; OSS engine and local plugins free (Apache-2.0). | [memos.openmem.net](https://memos.openmem.net/) |

## Compared to

- [Mem0](../mem0/index.md): the hosted adoption leader; MemOS bets on harness plugins and self-hosting where Mem0 bets on the widest API adoption.
- [Cognee](../cognee/index.md): both graph-backed and self-hostable; Cognee is a pipeline you embed in applications, MemOS ships more product (plugins, scheduler, viewer) around the graph.
- [Zep](../zep/index.md): bi-temporal invalidation versus MemOS's feedback-based correction; Zep for audit-grade change over time, MemOS for local-first agent coverage.

## Bottom line

**Recommended for OpenClaw, Hermes, or DeepSeek Harness users who want local-first memory with a shared-platform upgrade path, and for teams already operating Neo4j and Qdrant.**
Not for anyone needing published hosted pricing, independent benchmark evidence, or cloud residency outside MemTensor's infrastructure.

## Changes

- 2026-10-06 - Created from the 2026-10-06 entrant scan, with seven fetched sources and the vendor-run-benchmark caveat recorded as the critical angle.
- 2026-10-07 - Added the MemTensor/MemOS star history chart to the Status section.
- 2026-10-07 - The hosted cloud began publishing plans: Free $0/mo, Starter $19/mo and Pro $286/mo both flagged "Free Now" on apply-to-join, Enterprise custom (new Price history section with the baseline row); the no-public-price caution rewritten and the landing-page reference updated.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [Mem0](../mem0/index.md) - the hosted-API rival with the wider adoption
- [Cognee](../cognee/index.md) - the other self-hostable graph-memory platform
- [OpenClaw](../../assistant-runtimes/openclaw/index.md) - the assistant harness with official MemOS plugins
- [DeepSeek Harness](../../harnesses/deepseek-harness/index.md) - the harness whose dsh plugin connection shipped August 2026

## References

- https://github.com/MemTensor/MemOS - repository, 11,713 stars, push record, description, as of 2026-10-06
- https://raw.githubusercontent.com/MemTensor/MemOS/main/README.md - features, the four entry points, plugin news timeline, and the OmniMemEval benchmark table
- https://memos-docs.openmem.net/ - documentation root (the README's home/overview deep link returned 404 at fetch time, recorded here)
- https://arxiv.org/abs/2507.03724 - the MemOS paper: a memory OS for AI systems
- https://pypi.org/pypi/MemOS/json - the memos package at 0.37.0, Apache-2.0
- https://memos.openmem.net/ - the hosted platform's landing page, now carrying the Free/Starter/Pro/Enterprise price table, re-verified unchanged as of 2026-10-08 (client-rendered on the 2026-10-06 fetch)
- https://hn.algolia.com/api/v1/items/44945613 - the August 2025 story (2 points, 0 comments), the thin-discussion record
