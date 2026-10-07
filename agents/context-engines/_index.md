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
- [CodeAlive](codealive/index.md) - the hosted context-engine API serving a code graph and hybrid retrieval to any MCP agent on metered per-action pricing, from a small London company with no independent coverage yet.
- [Context7](context7/index.md) - Upstash's hosted docs-injection service pulling version-specific library documentation into the prompt at question time over MCP or a CLI skill, the category's only engine that indexes the world's libraries instead of your repo.
- [Graft](graft/index.md) - Trail's MIT context layer feeding agents a code graph instead of grep, 9.6k stars in fourteen weeks with every benchmark still the vendor's own.
- [Graphify](graphify/index.md) - the local AST knowledge graph exposed as a `/graphify` skill and MCP server, structure over similarity, no vectors.
- [Headroom](headroom/index.md) - the Apache-2.0 compression layer rewriting tool outputs, logs, files, and RAG chunks before they reach the LLM, reversible through a retrieve tool, 74.5k stars in nine months.
- [Jevgrep](jevgrep/index.md) - the MIT CLI that answers a question about a repo with files, leads, and excerpts, Jev judging relevance per query with no index at all, 2,355 stars in eleven days.
- [qmd](qmd/index.md) - Tobias Lütke's local hybrid search engine for notes, docs, and knowledge bases, BM25 plus vectors plus reranking.
- [Repomix](repomix/index.md) - the MIT CLI that packs a whole repo into one AI-friendly file, retrieval-free by design.
- [rtk](rtk/index.md) - the Rust CLI proxy that filters agent command output before it enters the context window.
- [Semble](semble/index.md) - the local static-embedding-plus-BM25 code search index that indexes in under a second on any CPU, snippets instead of grep-and-read.
- [Serena](serena/index.md) - the LSP-backed MCP toolkit giving agents IDE-grade symbol retrieval and editing for free, with a paid JetBrains backend, about 30k stars.
- [Sourcegraph code context platform](sourcegraph-code-context/index.md) - code search repositioned as the retrieval layer for agents, with value showing up above roughly 400K lines.
- [TOON](toon-format/index.md) - the MIT spec-backed Token-Oriented Object Notation that re-encodes JSON as indentation and table rows, about 1.9 million npm downloads a week, cutting the token cost of structured data in prompts.

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
