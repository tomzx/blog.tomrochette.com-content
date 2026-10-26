---
title: Code-Graph-RAG
created: 2026-10-07
updated: 2026-10-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, code-retrieval, knowledge-graph, rag]
readability: 3
audience_notes: >
  Engineers wiring codebase retrieval into an agent loop who want structural, graph-backed
  answers instead of embedding similarity.
  Assumes familiarity with tree-sitter, graph databases, and Cypher.
---

Code-Graph-RAG is an MIT-licensed Python system that parses a multi-language codebase with tree-sitter plus compiler-grade frontends into a Memgraph knowledge graph and answers natural-language questions and edit requests through an agent that writes Cypher.

**It pushes code retrieval past similarity search entirely: functions, classes, calls, and imports live in a graph, so the questions it answers well are structural ones (what calls this, what breaks if this changes) that embeddings index cannot address at all.**

## What it is

A `cgr` CLI (PyPI `code-graph-rag`) with two components.
The parser layer reads every source file with tree-sitter, sharpens facts with compiler frontends where a toolchain exists (libclang for C and C++, go/types for Go, opt-in Roslyn, javac, and Jedi for C#, Java, and Python), and can overlay runtime behavior by tracing a test run or pulling production eBPF profiles into the graph.
The RAG layer turns natural language into Cypher over Memgraph, retrieves the matching code, and drives AST-based surgical patching with a diff preview.
Python, TypeScript, JavaScript, Rust, Go, Java, C, C++, C#, PHP, Lua, and Dart are fully supported, with more languages on a pluggable ast-grep tier, under one language-agnostic schema across a monorepo.
Made by an independent developer, with an enterprise support and services badge on the README.

## Status

**Actively shipping and early: 5.2k stars in sixteen months with almost no independent discussion.**
5,252 stars and 702 forks as of 2026-10-14, pushed 2026-10-26, with 547 open issues (GitHub API, as of 2026-10-26).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=vitali87/code-graph-rag&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=vitali87/code-graph-rag&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=vitali87/code-graph-rag&type=date&legend=top-left" />
</picture>

PyPI shows version 0.3.13 released 2026-10-25 across 35 releases: 0.2.0 (2026-10-15) was the first release past the 0.1 line that carried all 27 of the preceding ones, ten point releases landed in the three days after it, the 0.2 line ran to 0.2.24 by 2026-10-23, and the 0.3 line opened the next day and reached 0.3.13 within two days.
Two Show HNs (February and March 2026) drew 1 point each, so the star count ran far ahead of any independent technical debate, the same pattern Knowhere and open-codebase-index in this section show.

## Strengths

- **Blast-radius questions are its home turf: call graphs, reference walks, and dead-code discovery from entry points are native graph queries, not retrieval approximations.**
- The layered parser is the right architecture: tree-sitter for coverage, compiler frontends for precision where available, runtime traces for the dispatch static analysis cannot see.
- One unified graph schema across a polyglot monorepo is the case where per-repo embeddings pipelines degrade worst.

## Cautions

- **Zero independent discussion and roughly 550 open issues against 5.2k stars means the only quality evidence is the project's own demos and CI.**
- It brings a graph database: Memgraph is a separate dependency with its own licensing and operational cost, which the one-line install pitch understates.
- The 0.2 line landed ten point releases in its first three days, after 27 releases on the 0.1 line, and ran to 0.2.24 before a 0.3 line opened on 2026-10-24, which means churn, and the Cypher-generation quality depends on the model you attach, which no benchmark here measures.
- Indexing is per-repo work (`cgr start --update-graph`), so freshness after agent edits needs the incremental update path to actually hold.

## Pricing

Free and open source under MIT, with enterprise support and services quoted by the developer.
Your costs are the Memgraph deployment and your own LLM bills for query answering, so no prices belong in this note and no price history table applies.

## Compared to

- [open-codebase-index](../open-codebase-index/index.md): the embeddings-plus-BM25 sibling over MCP, host-neutral and lighter; choose it for concept lookup, Code-Graph-RAG for structural and blast-radius questions.
- Aider's graph-ranked repo map ([Aider](../../harnesses/aider/index.md)): the no-store middle ground, ranking tree-sitter symbols by references without a database; choose it when a Memgraph deployment is too much.
- [Tree-sitter code chunking](../tree-sitter-chunking/index.md): the parsing layer alone, feeding a vector store; Code-Graph-RAG keeps the parse and ditches the store.

## Bottom line

**Recommended for monorepo teams whose retrieval questions are structural, who will operate Memgraph, and who will validate answer quality on their own repo before trusting it.**
Not for concept-level search, not as a dependency-free tool, and not for anyone needing independent evidence first, because none exists.
My disagreeable claim: this is the version of code retrieval the embeddings era skipped, and its near-zero discussion footprint says more about how few teams measure retrieval structurally than about the tool.

## Changes

- 2026-10-07 - Created in the daily refresh's retrieval entrant scan from the awesome-rag-production source.
- 2026-10-13 - Refreshed the volatile numbers (5,252 stars, pushed 2026-10-14) and recorded the open-issue count falling from 739 to 591 in two days, with the Cautions line aligned.
- 2026-10-16 - Recorded the PyPI train moving to 0.2.0 (2026-10-15, 29 releases total, the first release past the 0.1 line) and refreshed the repository activity (pushed 2026-10-15, 589 open issues).
- 2026-10-19 - Recorded the PyPI train reaching 0.2.10 (2026-10-18, 30 releases total, ten point releases in three days) and refreshed the repository activity (pushed 2026-10-19, 589 open issues).
- 2026-10-22 - Refreshed the repository activity (pushed 2026-10-22) and recorded the open-issue count falling from 590 to 543, with the Cautions line aligned; PyPI 0.2.10 remains latest.
- 2026-10-24 - Recorded the PyPI train reaching 0.3.2 (2026-10-24, 34 releases total; the 0.2 line ran to 0.2.24 by 2026-10-23 before the 0.3 line opened) and refreshed the repository activity (pushed 2026-10-24, 538 open issues), with the Cautions churn line extended.
- 2026-10-25 - Refreshed the repository activity (pushed 2026-10-25, 526 open issues); PyPI 0.3.2 remains latest.
- 2026-10-26 - Fixed the star-history chart markup (the light source carried theme=dark), refreshed the repository activity (pushed 2026-10-26, 547 open issues), and recorded the PyPI train reaching 0.3.13 (2026-10-25, 35 releases total).

## See also

- [open-codebase-index](../open-codebase-index/index.md) - the self-hosted embeddings-based code index it contrasts with
- [Tree-sitter code chunking](../tree-sitter-chunking/index.md) - the parser layer it builds on without the vector store
- [Aider](../../harnesses/aider/index.md) - the graph-ranked repo map, the no-database variant of the same idea
- [Semantic code search in coding tools](../semantic-code-search/index.md) - the shipped-tool pattern it replaces for structural questions

## References

- https://api.github.com/repos/vitali87/code-graph-rag - 5,252 stars (as of 2026-10-14), 702 forks, MIT, created 2025-06-16, pushed 2026-10-26, 547 open issues (GitHub API, as of 2026-10-26)
- https://raw.githubusercontent.com/vitali87/code-graph-rag/main/README.md - the two-component architecture, compiler frontends, runtime tracing, language support, Memgraph storage
- https://raw.githubusercontent.com/vitali87/code-graph-rag/main/NEWS.md - the feature-news ledger behind the active-maintenance claim
- https://pypi.org/pypi/code-graph-rag/json - version 0.3.13 (2026-10-25), 35 releases (re-verified 2026-10-26; the 0.2 line ended at 0.2.24, 2026-10-23)
- https://hn.algolia.com/api/v1/search?query=Code-Graph-RAG%20knowledge%20graph&tags=story - the footprint scan: two Show HNs at 1 point each (2026-02 and 2026-03)
