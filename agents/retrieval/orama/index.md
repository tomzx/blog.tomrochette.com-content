---
title: Orama
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, search-engine, rag, typescript]
readability: 3
audience_notes: >
  Engineers choosing an embeddable search engine for a JavaScript or TypeScript app, or for a RAG
  prototype that must live inside the process.
  Assumes you know what inverted indexes, embeddings, and hybrid search are.
---

Orama is an Apache-2.0 search engine and RAG pipeline library that runs in-process in the browser, on a server, or at the edge, with full-text, vector, and hybrid search in a ~2kb-core TypeScript package.

## What it is

**A dependency, not a deployment: you install `@orama/orama` and the index lives inside your process.**
You declare a schema (ten data types, including `vector[<size>]`), insert documents, and search with BM25 full-text, vector, or hybrid mode; typo tolerance, stemming and tokenization in 30 languages, facets, filters, geosearch, and merchandising rules ship in the box.
Since v3.0.0 it also sells the RAG loop itself: Answer Engine chat sessions over your index, with plugins for embeddings, a secure client-side proxy for OpenAI keys, persistence, and analytics.
It is made by OramaSearch Inc., written in TypeScript, and runs in Node, browsers, Deno, and edge runtimes; official guides cover Chinese and Japanese tokenization.

## Status

**Actively installed, slowly maintained: the npm firehose keeps flowing while the repository has gone quiet.**
10,570 stars and 405 forks as of 2026-10-06; the latest release is v3.1.18, published 2025-12-19, the most recent main-branch commit landed 2026-07-03 (a community CJK plugin fix), and the default branch was last pushed 2026-10-03.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=oramasearch/orama&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=oramasearch/orama&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=oramasearch/orama&type=date&legend=top-left" />
</picture>

npm reports 1,505,745 downloads/week for `@orama/orama` (window 2026-09-28 to 2026-10-04).
The discussion footprint is nearly empty for that scale: the only HN story dedicated to Orama is a 1-point 2023 post, with demos and integration posts at 2 to 5 points.

## Strengths

- One schema-driven package covers full-text, vector, and hybrid search plus an Answer Engine, deployable anywhere JavaScript runs, with no server to operate.
- The plugin system (embeddings, secure proxy, persistence, analytics, framework integrations) extends it without forking.
- Apache-2.0 with no hosted dependency, so the data never leaves your process.

## Cautions

- **The release train has stalled**: nothing since v3.1.18 in December 2025, and 2026 main-branch commits are sparse, so budget for owning its maintenance.
- GitHub detects the license as NOASSERTION even though LICENSE.md is the standard Apache-2.0 text, a detection quirk that will mislead any tool keying off the license field.
- Searching npm for "orama" surfaces an unrelated 2018 "Plug and play React charts" package (latest 2.0.6, 521 downloads/week as of 2026-10-06) that traps searches for the name.
- Nothing code-specific: no AST-aware chunking or repo structure awareness, it indexes whatever text you hand it.

## Pricing

Apache-2.0 open source; no paid tiers or hosted plans surfaced in this run's fetches (the docs root documents only the open-source library and its plugins), so pricing does not apply.

## Compared to

- [LlamaIndex](../llamaindex/index.md): the framework that orchestrates retrieval pipelines over external stores; choose Orama when the index itself must live in your JS/TS process.
- [open-codebase-index](../open-codebase-index/index.md): the code-aware self-hosted index served over MCP; choose it for repositories, Orama for application content.
- [Chonkie](../chonkie/index.md): the chunking layer that would feed an Orama index in a larger pipeline.

## Bottom line

Recommended for JS/TS teams that want search or RAG to live inside their app or edge function with zero infrastructure, accepting that they may inherit its maintenance.
Not for code-aware retrieval (grep-first loops or a code index serve better) or for anyone who needs a vendor to call.

## Changes

- 2026-10-06 - Created.
- 2026-10-07 - Added the oramasearch/orama star history chart to the Status section.

## See also

- [open-codebase-index](../open-codebase-index/index.md) - the code-specific self-hosted counterpart in this category
- [Chonkie](../chonkie/index.md) - the chunking library that would feed it in a pipeline
- [Retrieval Feature Matrix](../retrieval-feature-matrix/index.md) - the nine-column comparison this note joins
- [Context Management Patterns](../../context-management-patterns/index.md) - the size-threshold argument that demotes local indexes

## References

- https://api.github.com/repos/oramasearch/orama - repository facts (10,570 stars, 405 forks, TypeScript, ~2kb core description, pushed 2026-10-03, as of 2026-10-06)
- https://raw.githubusercontent.com/oramasearch/orama/main/README.md - features, ten data types, plugin list, Answer Engine, install targets
- https://raw.githubusercontent.com/oramasearch/orama/main/LICENSE.md - the standard Apache-2.0 text, Copyright 2023 OramaSearch Inc.
- https://api.npmjs.org/downloads/point/last-week/@orama/orama - 1,505,745 downloads/week, window 2026-09-28 to 2026-10-04
- https://api.github.com/repos/oramasearch/orama/releases/latest - v3.1.18 published 2025-12-19
- https://api.github.com/repos/oramasearch/orama/commits?per_page=1 - latest main-branch commit 2026-07-03 (CJK plugin fix by a community contributor)
- https://hn.algolia.com/api/v1/search?query=orama - the near-empty HN footprint (1-point 2023 story; demos at 2 to 5 points)
- https://registry.npmjs.org/orama - the unrelated stale "Plug and play React charts" package (latest 2.0.6)
- https://api.npmjs.org/downloads/point/last-week/orama - 521 downloads/week for the stale package, window 2026-09-28 to 2026-10-04
- https://docs.orama.com/open-source - official docs root, including the Chinese and Japanese guides
