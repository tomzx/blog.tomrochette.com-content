---
title: MemMachine
created: 2026-10-11
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, agent-memory, knowledge-graphs, open-source]
readability: 3
audience_notes: >
  Engineers adding persistent memory to an agent product who want the OSS graph-plus-SQL
  option profiled against the hosted APIs. Assumes you know what an episodic store is.
---

MemMachine is an Apache-2.0 memory layer for AI agents, incubated by MemVerge, that pairs graph-stored episodic memory with SQL-stored profile memory behind Python, TypeScript, REST, and MCP surfaces, self-hosted or on a free cloud account.

**Its bet is that episodic and profile memory want different databases, a graph for conversational context and SQL for durable user facts, with a model-agnostic server on top so no frontier lab owns the memory.**

## What it is

A server (Docker or pip, memmachine-client and memmachine-server on PyPI at 0.4.0) exposing add and search through a Python SDK, a TypeScript SDK, a REST API, and a native MCP server (stdio and HTTP) for Claude Desktop, Cursor, and other MCP clients.
Episodic memory lands in a graph database (Neo4j) as conversational context, profile memory lands in SQL as long-term user facts, and a short-term working set covers the live session.
Prebuilt integrations cover LangChain, LangGraph, CrewAI, LlamaIndex, AWS Strands, n8n, Dify, and FastGPT, plus an NVIDIA NeMo Agent Toolkit integration announced in April 2026.
The project was incubated inside MemVerge and is now described as community-driven, with MemVerge engineering still assigned and an enterprise version announced.

## Status

**Active and mid-scale, with a corporate backer and no benchmark record.**
3,072 stars and 220 forks, created 2025-08-15, pushed 2026-10-27, Apache-2.0, as of 2026-10-28 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=MemMachine/MemMachine&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=MemMachine/MemMachine&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=MemMachine/MemMachine&type=date&legend=top-left" />
</picture>

Both PyPI distributions moved to 0.4.0 on 2026-10-08.
The Hacker News record is thin: a 4-point Show HN in November 2025 and a 2-point story the month before, so adoption rests on registry and framework channels rather than public debate.
The site names Arista Networks, Hugging Face, and Duke University among trusted teams and publishes customer quotes, but no independent evaluation of the engine exists in either direction.

## Strengths

- **The two-store split matches the data**: episodic context in a graph, durable facts in SQL, and a session-scoped working set, instead of one embedding pool doing all three jobs badly.
- Model-agnostic and on-prem by design; the site's FAQ explicitly targets teams that cannot hand memory to a frontier lab's service.
- The integration list is the widest of any young entrant in this category, eight frameworks plus the NeMo toolkit, for an OSS-first memory layer.
- Working docs, examples, Discord, and a funded company behind it rather than a solo maintainer.

## Cautions

- **It publishes no benchmarks at all**, which is rare in a category where even self-run numbers are table stakes; the marketing leans on logos and testimonials instead.
- Self-hosting wants a Neo4j plus SQL stack, a heavier footprint than the SQLite-local peers here.
- The enterprise version is announced as available soon and the cloud console is free but unpriced, so the commercial model is not yet visible.
- The star push is explicit (README star requests, ambassador programs), which softens the adoption signal relative to the logo wall.

## Pricing

Open source is free under Apache-2.0.
The hosted MemMachine Platform offers a free account with no published price.
An enterprise version is announced without pricing, as of 2026-10-11.

## Compared to

- [mem0](../mem0/index.md): the hosted adoption leader; MemMachine's graph-plus-SQL split is the architectural counterpoint to Mem0's vector-first platform, and both have free OSS layers.
- [Hindsight](../hindsight/index.md): the other service-grade engine you can self-host; Hindsight publishes per-run benchmark artifacts, MemMachine publishes none yet.
- [claude-mem](../claude-mem/index.md): single-user session compression for coding agents; MemMachine is a product-grade layer for many users and frameworks.

## Bottom line

Recommended for teams standardizing agent memory across LangGraph or CrewAI stacks who want the OSS path on their own databases and will run their own evaluations.
Not for buyers who need published benchmarks, a visible commercial ladder, or a lightweight local footprint today.
My disagreeable claim: publishing zero numbers in a benchmark-obsessed category is either restraint or avoidance, and only time settles which.

## Changes
- 2026-10-11 - Created from the 2026-10-11 Awesome-Agent-Memory entrant scan, with seven fetched sources and the no-benchmark-plus-logo-wall profile recorded as the critical angle.
- 2026-10-24 - Rotation re-verification: every cited URL re-fetched live (repository API, README, docs, site, PyPI, Hacker News search), no facts changed; both PyPI distributions still 0.4.0, the thin-discussion record unchanged.
- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart markup: the light-theme source carried the dark-theme parameter; it now points at the default chart.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [mem0](../mem0/index.md) - the hosted adoption leader it structurally answers
- [Hindsight](../hindsight/index.md) - the self-hostable engine with the benchmark receipts this lacks
- [claude-mem](../claude-mem/index.md) - the single-user session-compression alternative

## References

- https://github.com/MemMachine/MemMachine - repository, Apache-2.0, 3,065 stars, 219 forks, created 2025-08-15, pushed 2026-10-10, verified through the GitHub API as of 2026-10-11
- https://raw.githubusercontent.com/MemMachine/MemMachine/main/README.md - the episodic-plus-profile architecture, the integration table, MCP server, and the MemVerge-incubated FAQ pointer
- https://docs.memmachine.ai - the documentation root: quickstart, install guide, and core concepts
- https://memmachine.ai - the MemVerge incubation FAQ, the trusted-teams wall, the NeMo integration post, and the enterprise announcement
- https://pypi.org/pypi/memmachine-client/json - memmachine-client 0.4.0 (2026-10-08), the release-sync record
- https://hn.algolia.com/api/v1/search?query=memmachine&tags=story - the thin-discussion record (4-point Show HN 2025-11-21, 2-point story 2025-10-23)
- https://github.com/TeleAI-UAGI/Awesome-Agent-Memory - the entrant source that surfaced it, as of 2026-10-11
