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

- [Augment Code](augment-code/index.md) - the coding platform whose core is a real-time semantic Context Engine feeding Auggie and Cosmos.
- [Graft](graft/index.md) - Trail's MIT context layer feeding agents a code graph instead of grep, 9.2k stars in twelve weeks with every benchmark still the vendor's own.
- [Graphify](graphify/index.md) - the local AST knowledge graph exposed as a `/graphify` skill and MCP server, structure over similarity, no vectors.
- [qmd](qmd/index.md) - Tobias Lütke's local hybrid search engine for notes, docs, and knowledge bases, BM25 plus vectors plus reranking.
- [Repomix](repomix/index.md) - the MIT CLI that packs a whole repo into one AI-friendly file, retrieval-free by design.
- [rtk](rtk/index.md) - the Rust CLI proxy that filters agent command output before it enters the context window.
- [Semble](semble/index.md) - the local static-embedding-plus-BM25 code search index that indexes in under a second on any CPU, snippets instead of grep-and-read.
- [Sourcegraph code context platform](sourcegraph-code-context/index.md) - code search repositioned as the retrieval layer for agents, with value showing up above roughly 400K lines.

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
