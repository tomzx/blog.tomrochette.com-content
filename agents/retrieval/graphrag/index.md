---
title: GraphRAG
created: 2026-10-07
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, rag, knowledge-graph, microsoft]
readability: 3
audience_notes: >
  Engineers deciding whether a knowledge-graph RAG layer earns its indexing cost over a
  document corpus, and what taking the reference implementation home means now.
  Assumes familiarity with RAG, entity extraction, and LLM indexing costs.
---

GraphRAG is Microsoft Research's MIT-licensed Python pipeline that builds an LLM-extracted entity knowledge graph over a text corpus and answers queries from community summaries, the reference implementation of the graph-based RAG pattern.

**It founded the graph-RAG family and answered the question vector RAG answers worst (what are the themes across this whole corpus), and its own README now declares the project largely in maintenance mode, which makes it a pattern to study rather than a dependency to adopt.**

## What it is

A `pip install graphrag` CLI and library that chunks a corpus, prompts an LLM to extract entities, relationships, and claims per chunk, detects communities over the graph, and pre-generates community summaries for global questions.
It answers two query styles: local search (entity-anchored neighborhood questions) and global search (map-reduce over community summaries).
The method paper (arXiv 2404.16130) frames it as moving from local to global sense-making on narrative private data.
Made by Microsoft Research, first released July 2024, optional Azure OpenAI or local model support.

## Status

**Active by the commit clock, retired by its own README.**
36,271 stars and 3,838 forks since 2024-03-27, pushed 2026-10-08, 52 open issues (GitHub API, as of 2026-10-09).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=microsoft/graphrag&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=microsoft/graphrag&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=microsoft/graphrag&type=date&legend=top-left" />
</picture>

PyPI shows version 3.3.0 released 2026-10-08 across 51 releases (a SQLite performance fix), so the bugfix train still runs under the maintenance declaration.
The README's warning is the status fact that matters: the project is largely in maintenance mode, it will not accept new PRs or implement new features, and it names the dramatic change in frontier-model capabilities and a diversified research portfolio as the cause.
The launch thread drew 282 points in July 2024, the largest graph-RAG footprint on Hacker News.

## Strengths

- **Global sense-making is its product: community summaries answer "what are the themes across this corpus" questions that similarity search structurally cannot.**
- It is the citation root of the pattern: LightRAG, nano-graphrag, and most graph-RAG work name it.
- MIT licensed with a CLI, a Python API, and docs deep enough to replicate the pipeline.

## Cautions

- **Maintenance mode means the feature freeze is explicit: budget to own whatever you build on it, because upstream has said it is done.**
- Indexing is expensive by the project's own warning, an LLM call set per chunk over your whole corpus.
- Version bumps carry breaking config changes, and the README tells you to re-init between minor versions.
- Nothing agent-facing: no MCP server, no retrieval tools for a coding harness, the consumer is your own application.

## Pricing

Free and open source under MIT.
The costs are your own LLM bills for indexing and querying, which the project's documentation warns can be large on big corpora, so no prices belong in this note and no price history table applies.

## Compared to

- [LightRAG](../lightrag/index.md): the actively maintained graph-RAG counterweight, dual-level retrieval instead of community summaries; pick it when you want graph RAG with a living release train.
- [RAGFlow](../ragflow/index.md): the deployable engine with citations and a UI; graph structure is one artifact kind among its outputs, not the core.
- [LlamaIndex](../llamaindex/index.md): property-graph indexes give you the graph option inside a general framework, at the cost of assembling the pipeline yourself.

## Bottom line

**Recommended for studying what graph RAG is and for one-shot theme extraction over a stable narrative corpus you can afford to index.**
Not for code, not for fast-changing corpora, and not as a dependency bet now that the maker has declared maintenance mode.
My disagreeable claim: the maintenance-mode declaration is graph RAG's candid status report, the frontier ate the gap it exploited, and the pattern's heirs now argue about which parts survive as plain long-context questions.

## Changes

- 2026-10-07 - Created in the daily refresh's retrieval entrant scan from the awesome-rag-production source.
- 2026-10-09 - Recorded PyPI 3.3.0 (2026-10-08, a SQLite performance fix, 51 releases) and refreshed the repository numbers (36,271 stars, pushed 2026-10-08); the README's maintenance-mode declaration is unchanged.

## See also

- [LightRAG](../lightrag/index.md) - the maintained graph-RAG implementation this project's pattern spawned
- [RAGFlow](../ragflow/index.md) - the full RAG engine that packages graph-shaped artifacts as one output among several
- [Graphify](../../context-engines/graphify/index.md) - the context-engine sibling building agent-usable graph structure
- [The Importance of Context When Interacting with LLMs](../../../the-importance-of-context-when-interacting-with-llms/index.md) - why retrieval structure beats raw model choice

## References

- https://api.github.com/repos/microsoft/graphrag - 36,271 stars, 3,838 forks, MIT, created 2024-03-27, pushed 2026-10-08, 52 open issues (GitHub API, as of 2026-10-09)
- https://api.github.com/repos/microsoft/graphrag/releases/latest - v3.3.0 published 2026-10-08, the SQLite performance-fix release
- https://raw.githubusercontent.com/microsoft/graphrag/main/README.md - the maintenance-mode warning, the expensive-indexing warning, the init-between-versions rule
- https://arxiv.org/abs/2404.16130 - the method paper: From Local to Global, graph RAG as query-focused summarization
- https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/ - the Microsoft Research announcement grounding community summaries and the local/global query split
- https://microsoft.github.io/graphrag/ - official docs root: local and global search, CLI quickstart
- https://pypi.org/pypi/graphrag/json - version 3.3.0 (2026-10-08), 51 releases, MIT
- https://hn.algolia.com/api/v1/search?query=GraphRAG%20is%20now%20on%20GitHub&tags=story - the July 2024 launch thread, 282 points, 49 comments
