---
showArticleList: false
title: Context engines
created: 2026-09-24
visible: true
status: in progress
tags: [agents, context-engines]
readability: 3
---

The tools that decide what enters the context window: semantic engines, code graphs, repo packers, output filters, and local search indexes.

- [Augment Code](augment-code/index.md) - the coding platform whose core is a real-time semantic Context Engine feeding Auggie and Cosmos, sold to Harness on 2026-10-08.
- [code-review-graph](code-review-graph/index.md) - the local Tree-sitter code graph served over MCP as review context, blast radius and risk scores with the category's most self-critical benchmarks, 32k stars in eight months and a review-first name on a context engine.
- [CodeAlive](codealive/index.md) - the hosted context-engine API serving a code graph and hybrid retrieval to any MCP agent on metered per-action pricing, from a small London company with no independent coverage yet.
- [Context7](context7/index.md) - Upstash's hosted docs-injection service pulling version-specific library documentation into the prompt at question time over MCP or a CLI skill, the category's only engine that indexes the world's libraries instead of your repo.
- [Entroly](entroly/index.md) - the Apache-2.0 receipt-backed compression layer that selects evidence within a token budget, records every omission, and recovers the exact original bytes on demand, the category's audit-first bet at 476 stars.
- [Graft](graft/index.md) - Trail's MIT context layer (renamed Trail-code) feeding agents a code map plus shared team learnings instead of grep, 10.1k stars with every benchmark still the vendor's own.
- [Graphify](graphify/index.md) - the local AST knowledge graph exposed as a `/graphify` skill and MCP server, structure over similarity, no vectors.
- [Headroom](headroom/index.md) - the Apache-2.0 compression layer rewriting tool outputs, logs, files, and RAG chunks before they reach the LLM, reversible through a retrieve tool, 75k stars in nine months.
- [Jevgrep](jevgrep/index.md) - the MIT CLI that answers a question about a repo with files, leads, and excerpts, Jev judging relevance per query with no index at all, about 2.7k stars in three weeks.
- [LLMLingua](llmlingua/index.md) - Microsoft Research's MIT prompt-compression library (perplexity token pruning plus a GPT-4-distilled BERT-class compressor), the peer-reviewed ancestor of this category's compression products, 6.7k stars.
- [qmd](qmd/index.md) - Tobias Lütke's local hybrid search engine for notes, docs, and knowledge bases, BM25 plus vectors plus reranking.
- [Repomix](repomix/index.md) - the MIT CLI that packs a whole repo into one AI-friendly file, retrieval-free by design.
- [Repowise](repowise/index.md) - the AGPL-3.0 local index of call graph, git history, tests, and decisions served to agents over ten task-shaped MCP tools, with code-health analytics and self-run context-tool benchmarks on the same index.
- [rtk](rtk/index.md) - the Rust CLI proxy that filters agent command output before it enters the context window.
- [Semble](semble/index.md) - the local static-embedding-plus-BM25 code search index that indexes in under a second on any CPU, snippets instead of grep-and-read.
- [Serena](serena/index.md) - the LSP-backed MCP toolkit giving agents IDE-grade symbol retrieval and editing for free, with a paid JetBrains backend, about 30k stars.
- [SoL-Pi](sol-pi/index.md) - NV Labs' MIT Pi-harness extension (Action Fusion, paged recall, verified reducer, online compaction) keeping long auto-research loops flat in token cost, about 3.4k stars with a three-post HN footprint.
- [Sourcegraph code context platform](sourcegraph-code-context/index.md) - code search repositioned as the retrieval layer for agents, with value showing up above roughly 400K lines.
- [TOON](toon-format/index.md) - the MIT spec-backed Token-Oriented Object Notation that re-encodes JSON as indentation and table rows, about 7.8 million npm downloads in the trailing month, cutting the token cost of structured data in prompts.
- [Vanna](vanna/index.md) - the archived MIT text-to-SQL RAG framework whose DDL-docs-past-queries retrieval founded the data-semantics half of this category, 23.8k stars, the open-source core read-only since 2026-03-29 while the company sells Cloud and Enterprise.
- [WrenAI](wrenai/index.md) - Canner's Apache-2.0 governed semantic layer and context engine for data, versioned MDL plus business definitions in your git serving agents governed SQL over MCP, the first column over business semantics instead of code, about 17.8k stars.

Its members are compared on shared rows in the [Context Engines Feature Matrix](context-engines-feature-matrix/index.md).

## Changes

- 2026-08-24 - Added Augment Code.
- 2026-08-24 - Added Repomix.
- 2026-08-24 - Added Sourcegraph code context platform.
- 2026-08-30 - Added Graphify.
- 2026-08-30 - Added qmd.
- 2026-08-30 - Added rtk.
- 2026-08-30 - Added Semble.
- 2026-09-12 - Added Graft.
- 2026-10-04 - Added Serena.
- 2026-10-05 - Added CodeAlive.
- 2026-10-07 - Added Jevgrep.
- 2026-10-07 - Added Context7.
- 2026-10-07 - Added Headroom.
- 2026-10-07 - Added TOON.
- 2026-10-10 - Added LLMLingua.
- 2026-10-10 - Added WrenAI.
- 2026-10-11 - Added code-review-graph.
- 2026-10-11 - Added Vanna.
- 2026-10-12 - Added Entroly.
- 2026-10-13 - Added SoL-Pi.
- 2026-10-13 - Added Repowise.
