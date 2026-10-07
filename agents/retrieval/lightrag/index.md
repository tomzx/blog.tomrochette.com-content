---
title: LightRAG
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, rag, knowledge-graph]
readability: 3
audience_notes: >
  Engineers choosing a graph-based RAG implementation for a document corpus and weighing
  academic-lineage frameworks against maintenance-mode originals.
  Assumes familiarity with entity extraction, embeddings, and graph stores.
---

LightRAG is the HKU Data Intelligence Lab's MIT-licensed Python framework that extracts entities and relations into a knowledge graph and answers queries with dual-level retrieval, the EMNLP 2025 paper behind the most-starred graph-RAG implementation.

**It took the graph-RAG pattern Microsoft parked in maintenance mode and turned it into a maintained framework with pluggable storage and a growing multimodal stack, and that velocity is both its appeal and its risk.**

## What it is

A `pip install lightrag-hku` framework: an LLM pass extracts entities and relations into a graph, and queries run at two levels, low-level retrieval over specific entities and high-level retrieval over topics and themes.
Storage is pluggable across Neo4j, PostgreSQL, MongoDB, and OpenSearch (the unified backend added March 2026), with a WebUI that visualizes the graph, citation support, a default reranker for mixed queries, and four selectable chunking strategies (fixed, recursive, vector, paragraph).
RAG-Anything merged in May 2026 brought multimodal parsing and extraction through MinerU or Docling services, and role-specific LLM configuration (extraction, query, keywords, vision) landed the same month.
Made by HKUDS, the lab that also ships RAG-Anything, VideoRAG, and MiniRAG.

## Status

**Actively maintained with a large, fast-moving community.**
40,003 stars and 5,665 forks since 2024-10-02, pushed 2026-10-03, with 359 open issues (GitHub API, as of 2026-10-07).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=HKUDS/LightRAG&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=HKUDS/LightRAG&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=HKUDS/LightRAG&type=date&legend=top-left" />
</picture>

PyPI shows version 1.5.7 released 2026-09-02 across 94 releases, and the README's news line runs to July 2026 (Smart Heading recognition for Word documents).
The paper (arXiv 2410.05779) was published at EMNLP 2025.
The launch thread drew 82 points in July 2024 and little HN activity since, so the star count grew through tutorials and the lab's ecosystem rather than launch-driven debate.

## Strengths

- **The complete graph-RAG loop in one install: extraction, dual-level query, graph storage of your choice, visualization, and citations, where GraphRAG gives you the pipeline and stops.**
- Storage portability is unusual for the family: one framework over Neo4j, PostgreSQL, MongoDB, or OpenSearch keeps the graph out of a vendor.
- An academic paper plus a large community means the method is documented and the failure modes are discussed in public issues.

## Cautions

- **The lab's breadth is the roadmap risk: RAG-Anything, VideoRAG, and MiniRAG share one maintainership, and 359 open issues say the core absorbs more than it resolves.**
- The accuracy story is self-run; I found no independent benchmark replicating the paper's numbers on a different corpus.
- The feature surface churns (chunking strategies, merged multimodal parsing, role-specific models), so pin versions and re-test on upgrades.
- Setup is a stack: an embedding model, an LLM, a graph or unified store, and optionally parsing services.

## Pricing

Free and open source under MIT.
The costs are your own model bills for extraction and querying plus the storage you attach, so no prices belong in this note and no price history table applies.

## Compared to

- [GraphRAG](../graphrag/index.md): the origin in maintenance mode; LightRAG is where the pattern's active development lives.
- [RAGFlow](../ragflow/index.md): the deployable engine with a UI and cloud tiers; choose it when you want citations and chunk inspection without assembling storage yourself.
- [Graphify](../../context-engines/graphify/index.md): the context-engine angle, building graph structure an agent reads, rather than a queryable RAG framework.

## Bottom line

**Recommended as the default graph-RAG framework when the graph layer genuinely earns its indexing cost, which for most corpora means theme and multi-hop questions, not lookup.**
Not for teams that need a frozen dependency or independent accuracy evidence, because it offers neither.
My disagreeable claim: LightRAG's star count measures the graph-RAG idea's appeal, not adoption depth, and the 359 open issues are the truer count of how much work the pattern still demands.

## Changes

- 2026-10-07 - Created in the daily refresh's retrieval entrant scan from the awesome-rag-production source.

## See also

- [GraphRAG](../graphrag/index.md) - the maintenance-mode original whose pattern this framework maintains
- [RAGFlow](../ragflow/index.md) - the engine alternative that bundles parsing, citations, and agentic retrieval
- [Docling](../docling/index.md) - the parser LightRAG's multimodal mode calls through RAG-Anything
- [The Importance of Context When Interacting with LLMs](../../../the-importance-of-context-when-interacting-with-llms/index.md) - the retrieval-quality-over-model-choice argument

## References

- https://api.github.com/repos/HKUDS/LightRAG - 40,003 stars, 5,665 forks, MIT, created 2024-10-02, pushed 2026-10-03, 359 open issues (GitHub API, as of 2026-10-07)
- https://raw.githubusercontent.com/HKUDS/LightRAG/main/README.md - dual-level retrieval, storage backends, chunking strategies, the RAG-Anything merge, the news timeline
- https://arxiv.org/abs/2410.05779 - the EMNLP 2025 paper: LightRAG, simple and fast retrieval-augmented generation
- https://pypi.org/pypi/lightrag-hku/json - version 1.5.7 (2026-09-02), 94 releases, MIT
- https://learnopencv.com/lightrag/ - the widely-cited third-party guide grounding the tutorial-driven adoption pattern
- https://hn.algolia.com/api/v1/search?query=LightRAG&tags=story - the footprint scan: the 82-point 2024 launch thread and thin activity since
