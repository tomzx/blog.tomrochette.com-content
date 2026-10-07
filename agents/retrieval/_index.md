---
showArticleList: false
title: Retrieval
created: 2026-09-24
visible: true
status: in progress
tags: [agents, retrieval]
readability: 3
---

Feeding agents the right slices of large corpora: chunking libraries, parsing pipelines, search-engine libraries, a full RAG engine, the two big frameworks, graph-RAG systems, a vectorless reasoning engine, code knowledge-graph retrieval, and the patterns built on them.

- [Chonkie](chonkie/index.md) - the MIT chunking library (token, semantic, and neural chunkers) for RAG pipelines, its commercial arm dead and its maker pivoted to Feyn Labs.
- [Code-Graph-RAG](code-graph-rag/index.md) - the MIT monorepo code-RAG system storing tree-sitter plus compiler facts in a Memgraph graph queried by an agent writing Cypher.
- [Docling](docling/index.md) - IBM-origin document parser turning PDF, Office, audio, and video into structured DoclingDocuments for RAG and agent pipelines.
- [GraphRAG](graphrag/index.md) - Microsoft Research's entity-graph RAG pipeline with community summaries, now declared largely in maintenance mode by its own README.
- [Knowhere](knowhere/index.md) - Ontos AI's structure-preserving document parsing and retrieval pipeline, hosted per page or self-hosted, its self-reported benchmark and near-empty HN footprint attached.
- [LangChain](langchain/index.md) - the largest LLM framework, repositioned in 2026 as an agent engineering platform.
- [LightRAG](lightrag/index.md) - the HKU lab's MIT graph-RAG framework (dual-level retrieval, pluggable graph storage), the maintained carrier of the pattern Microsoft parked.
- [LlamaIndex](llamaindex/index.md) - the MIT data framework for retrieval pipelines, now the open arm of LlamaParse.
- [open-codebase-index](open-codebase-index/index.md) - the MIT self-hosted semantic code index (embeddings, BM25, call graph) served to OpenCode, Claude Code, Codex, Pi, and MCP clients.
- [Orama](orama/index.md) - the Apache-2.0 embeddable search engine and RAG pipeline for JS/TS, 1.5M weekly installs on a stalled release train.
- [PageIndex](pageindex/index.md) - Vectify AI's vectorless reasoning-RAG engine (tree index per document, LLM tree search), the largest bet that the vector layer is skippable.
- [RAGFlow](ragflow/index.md) - InfiniFlow's Apache-2.0 RAG engine (DeepDoc parsing, template chunking, citations, agentic retrieval), 91.8k stars, self-hosted or clouded, with a disruptive 1.0 Go rewrite.
- [Semantic code search](semantic-code-search/index.md) - retrieval by meaning over embedded chunks, shipped as a workspace index.
- [Tree-sitter chunking](tree-sitter-chunking/index.md) - cutting files along syntax boundaries instead of fixed line counts.
- [Unstructured](unstructured/index.md) - the Apache-2.0 parsing incumbent Docling displaced, now funneling to a hosted Transform MCP server and quote-priced Pipelines.

Its members are compared on shared rows in the [Retrieval Feature Matrix](retrieval-feature-matrix/index.md).

## Changes

- 2026-08-24 - Added LangChain.
- 2026-08-24 - Added LlamaIndex.
- 2026-08-24 - Added Semantic code search.
- 2026-08-24 - Added Tree-sitter chunking.
- 2026-09-16 - Added Chonkie.
- 2026-09-20 - Added Knowhere.
- 2026-09-27 - Added Docling.
- 2026-10-05 - Added open-codebase-index.
- 2026-10-06 - Added Orama.
- 2026-10-06 - Added RAGFlow.
- 2026-10-06 - Added Unstructured.
- 2026-10-07 - Added Code-Graph-RAG.
- 2026-10-07 - Added GraphRAG.
- 2026-10-07 - Added LightRAG.
- 2026-10-07 - Added PageIndex.
