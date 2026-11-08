---
title: Orama
created: 2026-10-06
updated: 2026-11-08
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
10,574 stars and 407 forks as of 2026-10-13; the latest release is still v3.1.18, published 2025-12-19, the most recent main-branch commit is still the 2026-07-03 community CJK plugin fix (re-verified 2026-11-08), and the repository shows push activity on 2026-10-18 without a main-branch commit since July.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=oramasearch/orama&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=oramasearch/orama&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=oramasearch/orama&type=date&legend=top-left" />
</picture>

npm reports 6,854,940 downloads in the trailing month for `@orama/orama` (range sum 2026-10-09 to 2026-11-08, six zero days inside the window), the window the section's npm-gaps ruling prefers for adoption claims, against prior readings of 6,008,962 (to 2026-11-04), 6,041,061 (to 2026-10-29), and 5,194,510 the month before, all while the release train sits still.
The discussion footprint is nearly empty for that scale: the only HN story dedicated to Orama is a 1-point 2023 post, demos and integration posts sit at 2 to 12 points (the largest a 12-point Show HN for a writing app that uses Orama as its local vector store), and the biggest mention overall is the 381-point OpenKnowledge Show HN of 2026-06-25, which lists Orama among its OSS stack dependencies.

## Strengths

- One schema-driven package covers full-text, vector, and hybrid search plus an Answer Engine, deployable anywhere JavaScript runs, with no server to operate.
- The plugin system (embeddings, secure proxy, persistence, analytics, framework integrations) extends it without forking.
- Apache-2.0 with no hosted dependency, so the data never leaves your process.

## Cautions

- **The release train has stalled**: nothing since v3.1.18 in December 2025, and 2026 main-branch commits are sparse, so budget for owning its maintenance.
- GitHub detects the license as NOASSERTION even though LICENSE.md is the standard Apache-2.0 text, a detection quirk that will mislead any tool keying off the license field.
- Searching npm for "orama" surfaces an unrelated 2018 "Plug and play React charts" package (latest 2.0.6, 513 downloads/week in the week to 2026-11-07) that traps searches for the name.
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
- 2026-10-18 - Corrected the matrix See-also line from fifteen to sixteen columns, stale since R2R joined on 2026-10-11; the rotation re-verification re-fetched every cited URL and found all claims unchanged.
- 2026-10-25 - Rotation re-verification re-fetched every cited URL live and moved the adoption figure to the trailing-month window per the npm-gaps ruling: 5,194,510 downloads (2026-09-23 to 2026-10-22), with the last complete weekly window at 1,044,238, down about 27 percent from the prior recorded week; the release stall, the quiet main branch, the license, the name collision, and the HN footprint all unchanged.
- 2026-10-31 - Rotation re-verification re-fetched every cited URL live: the release stall (v3.1.18), the quiet main branch (2026-07-03), the license detection, and the 1-point dedicated HN footprint all unchanged; the trailing-month range sum to 2026-10-29 reads 6,041,061 (seven zero days) and the last complete week (2026-10-23 to 2026-10-29) read 2,325,888, up from the prior recorded week, a swing the zero-day gaps make unreadable as a trend, and the name-squat package's weekly figure refreshed to 244.
- 2026-11-04 - Rotation re-verification re-fetched every cited URL live: the release stall (v3.1.18), the quiet main branch (2026-07-03), the push on 2026-10-18, the license file, the docs, and the near-empty HN footprint all unchanged; the trailing-month range sum to 2026-11-04 reads 6,008,962 (nine zero days), roughly flat against the prior readings, and the name-squat package's weekly figure refreshed to 436 (window 2026-10-27 to 2026-11-02).
- 2026-11-08 - Rotation re-verification re-fetched every cited URL live: the release stall (v3.1.18), the quiet main branch (2026-07-03), the push on 2026-10-18, the license file, and the docs all unchanged; the trailing-month range sum to 2026-11-08 reads 6,854,940 (six zero days), and the HN footprint gained its largest mention, the 381-point OpenKnowledge Show HN (2026-06-25) listing Orama in its OSS stack, while the dedicated-story record still holds; the name-squat package's weekly figure refreshed to 513 (window 2026-11-01 to 2026-11-07).

## See also

- [open-codebase-index](../open-codebase-index/index.md) - the code-specific self-hosted counterpart in this category
- [Chonkie](../chonkie/index.md) - the chunking library that would feed it in a pipeline
- [Retrieval Feature Matrix](../retrieval-feature-matrix/index.md) - the sixteen-column comparison this note joins
- [Context Management Patterns](../../context-management-patterns/index.md) - the size-threshold argument that demotes local indexes

## References

- https://api.github.com/repos/oramasearch/orama - repository facts (10,574 stars and 407 forks as of 2026-10-13, TypeScript, ~2kb core description, pushed 2026-10-18) (GitHub API, as of 2026-11-08)
- https://raw.githubusercontent.com/oramasearch/orama/main/README.md - features, ten data types, plugin list, Answer Engine, install targets (re-verified unchanged 2026-11-08)
- https://raw.githubusercontent.com/oramasearch/orama/main/LICENSE.md - the standard Apache-2.0 text, Copyright 2023 OramaSearch Inc. (re-verified 2026-11-08)
- https://api.npmjs.org/downloads/range/2026-10-09:2026-11-08/@orama/orama - 6,854,940 downloads across the trailing-month window, six zero days inside it (fetched 2026-11-08; summed per the npm-gaps ruling because npm's point endpoints can serve stale windows)
- https://api.github.com/repos/oramasearch/orama/releases/latest - v3.1.18 published 2025-12-19 (re-verified still latest 2026-11-08)
- https://api.github.com/repos/oramasearch/orama/commits?per_page=1 - latest main-branch commit 2026-07-03 (CJK plugin fix by a community contributor, re-verified 2026-11-08)
- https://hn.algolia.com/api/v1/search?query=orama - the near-empty dedicated HN footprint (1-point 2023 story; demos and integration mentions at 2 to 12 points; the 381-point OpenKnowledge Show HN of 2026-06-25 lists Orama in its OSS stack, re-verified 2026-11-08)
- https://registry.npmjs.org/orama - the unrelated stale "Plug and play React charts" package (latest 2.0.6, re-verified 2026-11-08)
- https://api.npmjs.org/downloads/point/last-week/orama - 513 downloads/week for the stale package, window 2026-11-01 to 2026-11-07 (fetched 2026-11-08)
- https://docs.orama.com/open-source - official docs root, including the Chinese and Japanese guides (fetched 2026-10-17, re-verified live 2026-11-08)
