---
title: R2R
created: 2026-10-11
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, rag, knowledge-graph]
readability: 3
audience_notes: >
  Engineers choosing a deployable RAG engine and weighing the survivors against
  the bets that stalled.
  Assumes familiarity with ingestion pipelines, hybrid search, and REST services.
---

R2R is SciPhi's MIT-licensed Python RAG engine that serves multimodal ingestion, hybrid search, automatic knowledge graphs, and agentic retrieval behind a RESTful API with Python and JavaScript SDKs.

**It was the loudest early bet that the RAG engine, not a framework, should be the product, and its silence since late 2025 makes it the cautionary footnote to RAGFlow's survival in the same slot.**

## What it is

A `pip install r2r` server (default port 7272) with an `r2r-js` npm SDK and a Docker compose full mode over Postgres plus Neo4j.
The feature set covered the full engine checklist early: multimodal ingestion (text, PDF, JSON, images, audio), hybrid semantic and keyword search with reciprocal rank fusion, automatic entity and relationship extraction into a knowledge graph, user and collection management, and a Deep Research API for multi-step retrieval plus reasoning.
It launched on Show HN twice, first as a framework in February 2024 (167 points), then repositioned in June 2024 (251 points) with the V2 post explicitly citing the LangChain abstraction backlash and declaring the switch to "a RAG engine instead of a framework".
Made by SciPhi, a startup founded by Owen Colegrove, which pitched a hosted cloud at sciphi.ai in both launches.

## Status

**Dormant, with its commercial surfaces rotting: the repository's last push is 2025-11-07, and the docs and company site are gone.**
8,015 stars and 131 open issues since 2024-02-12, pushed 2025-11-07, with PyPI at 3.6.6 released 2025-08-17 across 225 releases (GitHub API and PyPI, as of 2026-10-24).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=SciPhi-AI/R2R&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=SciPhi-AI/R2R&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=SciPhi-AI/R2R&type=date&legend=top-left" />
</picture>

The docs domain serves 404s on its root and quickstart paths, and sciphi.ai fails to answer at all (both fetched 2026-10-11), so the cloud funnel the launches pitched no longer exists.
The awesome-rag-production list carries its own dormancy warning on the entry, "quiet since late 2025 with no release since v3.6.5 (2025-06)".
The launch-driven discussion stopped after 2024: the V3 announcement thread drew 1 point in December 2024.

## Strengths

- **The engine-not-framework positioning was the right call two years early, and the V2 launch text reads today as this category's thesis statement.**
- The feature list anticipated what full engines now ship: hybrid RRF, knowledge-graph construction, user management, and grounded answers in one deployable service.
- The fixed-API promise ("keep the API ~fixed while we iterate on the internal system logic") was the right production instinct.

## Cautions

- **Dormant means you own it entirely: no release in over a year, 131 open issues, docs gone, and a company site that no longer answers.**
- The stack is heavy for what you get: Postgres plus Neo4j plus the service, with the graph store's operational cost on you.
- Anyone starting a document-RAG engine today has actively maintained options in the same slot, so adopting a dormant one needs a migration story, not a leap of faith.

## Pricing

Free and open source under MIT.
The hosted cloud the 2024 launches pitched is unreachable as of 2026-10-11, so no prices exist to track and no price history table applies.

## Compared to

- [RAGFlow](../ragflow/index.md): the engine bet that kept shipping, now at 92k stars with a 1.0 rewrite in flight, and the default choice in this slot.
- [GraphRAG](../graphrag/index.md): the other stalled graph-flavored system, but parked by an explicit maintenance declaration with releases continuing, not by silence.
- [LlamaIndex](../llamaindex/index.md): the assemble-it-yourself framework path; more work, and the vendor is alive.

## Bottom line

**Recommended for studying what the engine-not-framework argument looked like in 2024, and for the minority already running it, who should treat the dead docs and silent upstream as a migration trigger.**
Not for new deployments: RAGFlow occupies the same slot with an active release train and a community that answers.
My disagreeable claim: R2R's silence is the market's verdict that a REST-wrapped RAG engine without a differentiated parsing story is a feature of a bigger product, not a company, and RAGFlow escaped that fate only by making parsing the product.

## Changes

- 2026-10-11 - Created in the daily refresh's retrieval entrant scan from the awesome-rag-production source.
- 2026-10-11 - Added the star history chart.
- 2026-10-24 - Rotation re-verification re-fetched every cited URL live: the docs domain still 404s on root and quickstart, sciphi.ai and www still unreachable, PyPI still at 3.6.6 (225 releases), the launch footprint unchanged (167, 251, and 1 points), the awesome-rag-production dormancy warning still on the entry, and the repository still pushed 2025-11-07 with open issues drifting from 129 to 131.

## See also

- [RAGFlow](../ragflow/index.md) - the active engine in the slot R2R pioneered
- [GraphRAG](../graphrag/index.md) - the declared-maintenance counterpart to R2R's silent stall
- [LangChain](../langchain/index.md) - the abstraction backlash R2R's V2 launch rode, told from the framework's own note
- [LlamaIndex](../llamaindex/index.md) - the framework path R2R argued against

## References

- https://api.github.com/repos/SciPhi-AI/R2R - 8,015 stars, MIT, created 2024-02-12, pushed 2025-11-07, 131 open issues (GitHub API, as of 2026-10-24)
- https://raw.githubusercontent.com/SciPhi-AI/R2R/main/py/README.md - the engine positioning, feature list, install paths, and SDKs (the root README is a one-line pointer to this file; re-verified unchanged 2026-10-24, still linking the dead docs domain)
- https://pypi.org/pypi/r2r/json - version 3.6.6 (2025-08-17), 225 releases (re-verified unchanged 2026-10-24)
- https://hn.algolia.com/api/v1/search?query=R2R%20SciPhi&tags=story - the launch footprint: V1 at 167 points (2024-02-26), V2 at 251 points (2024-06-26), V3 at 1 point (2024-12-04) (re-verified unchanged 2026-10-24)
- https://r2r-docs.sciphi.ai/ - 404 on the root and quickstart paths (fetched 2026-10-11, re-verified 2026-10-24)
- https://sciphi.ai - transport error, with www.sciphi.ai also unreachable (fetched 2026-10-11, re-verified 2026-10-24)
- https://raw.githubusercontent.com/Yigtwxx/awesome-rag-production/main/README.md - the entrant source, whose R2R entry carries the dormancy warning quoted in the Status section (re-verified 2026-10-24)
