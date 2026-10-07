---
title: PageIndex
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, rag, document-parsing]
readability: 3
audience_notes: >
  Engineers retrieving from long professional documents who wonder whether the vector-store
  layer can be skipped entirely, and what a reasoning-based index costs per query.
  Assumes familiarity with RAG, embeddings, and document structure.
---

PageIndex is Vectify AI's MIT-licensed Python engine that replaces the vector index with a hierarchical tree index per document and retrieves by LLM reasoning through the tree, the flagship of the vectorless RAG argument.

**Its bet is that similarity is not relevance: instead of embedding chunks and hoping the nearest neighbor answers the question, it builds a table-of-contents tree and lets an LLM read down it like a human expert, trading embedding bills for token bills.**

## What it is

A `pip install pageindex` SDK with two modes.
Local mode (added August 2026) builds the tree on your machine with your own LLM key, using PageIndex Flash, the fast tree-index generator that is now the default for text-based PDFs, and retrieval runs agentically through the tree with full conversation context and page-level citations.
Cloud mode moves parsing, OCR, image understanding, tree construction, and storage to the vendor, upgrades citations to block level, and exposes an MCP server plus an API, with PageIndex File System extending tree indexing across whole corpora.
The maker pitches it at financial reports, legal documents, filings, and technical manuals.

## Status

**Actively developed and heavily starred for a two-year-old research bet.**
38,836 stars and 3,363 forks since 2025-04-01, pushed 2026-10-06, 119 open issues (GitHub API, as of 2026-10-07).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=VectifyAI/PageIndex&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=VectifyAI/PageIndex&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=VectifyAI/PageIndex&type=date&legend=top-left" />
</picture>

The Show HN carried the thesis fight: 192 points and 128 comments in August 2025, the largest vectorless-RAG debate on the site, with follow-up posts since.
The vendor's headline benchmark claims 98.7 percent on FinanceBench against roughly 50 percent for vector RAG, and an open benchmark repo publishes the runner for its 62-question lookup suite, though that repo shows 4 stars, so independent replications have not followed.

## Strengths

- **The citations are the product: every answer traces to a page or block of the source document, which is the property teams building on financial and legal text actually buy.**
- No chunking and no vector store removes two whole pipeline stages that own most DIY RAG failures on structured documents.
- Local mode keeps documents on your machine with your own keys, and the tree index is reusable across questions, unlike raw long-context dumps.

## Cautions

- **Retrieval quality rides on a paid LLM call per query: the vendor's own cost curves show per-model accuracy ladders, so a cheaper model is a worse retriever, not just a slower one.**
- The benchmark evidence is vendor-run; the open runner helps, but a 4-star benchmark repo means nobody independent has published numbers.
- The cloud surface (MCP server, folders, metadata, OCR) is login-gated with no public prices, so the managed path is a sales conversation.
- Long documents only: for short pages or small corpora the tree build costs more than it saves.

## Pricing

Local mode is free and MIT-licensed, running on your own LLM keys; the maker estimates about $0.001 per page to build a tree index locally.
PageIndex Cloud requires an API key from a login-walled developer portal, and no tier prices are publicly fetchable (as of 2026-10-07); VPC and on-premises deployments are quoted by contact.
No public prices belong in this note, so no price history table applies.

## Compared to

- [RAGFlow](../ragflow/index.md): the deployable engine that keeps the vector pipeline but makes chunks inspectable; PageIndex removes the pipeline instead.
- Raw long-context input: the vendor's comparison shows native whole-PDF input costing 2.1x more at 52 pages and 16.6x at 420, and not fitting at all beyond, which frames when retrieval earns its keep better than any benchmark.
- [Orama](../orama/index.md): the opposite pole, an in-process index with zero LLM cost per query, for corpora where similarity search is good enough.

## Bottom line

**Recommended for long professional documents where citation traceability and multi-step reading beat lookup speed, starting on your own worst filings to test the accuracy claims.**
Not for code, not for latency-sensitive lookup, and not for anyone who needs independent benchmarks before committing, because they do not exist yet.
My disagreeable claim: PageIndex is less a retrieval system than a claim that retrieval was the wrong abstraction for documents a model can read, and the per-query LLM bill is the price of admitting that.

## Changes

- 2026-10-07 - Created in the daily refresh's retrieval entrant scan from the awesome-rag-production source.

## See also

- [RAGFlow](../ragflow/index.md) - the keep-the-pipeline-and-inspect-it alternative for document RAG
- [Chonkie](../chonkie/index.md) - the chunking layer PageIndex's no-chunking thesis argues against
- [Docling](../docling/index.md) - the parsing stage vectorless retrieval still needs for scanned inputs in cloud mode
- [Context Management Patterns](../../context-management-patterns/index.md) - the sibling argument that agent-native context beats bespoke indexes below a size threshold

## References

- https://api.github.com/repos/VectifyAI/PageIndex - 38,836 stars, 3,363 forks, MIT, created 2025-04-01, pushed 2026-10-06, 119 open issues (GitHub API, as of 2026-10-07)
- https://raw.githubusercontent.com/VectifyAI/PageIndex/main/README.md - the tree-index method, local and cloud modes, Flash indexing, benchmark tables and cost curves
- https://docs.pageindex.ai/ - developer docs: SDK client, documents, agent integrations, MCP tools
- https://vectify.ai/blog/Mafin2.5 - the vendor's FinanceBench claim (98.7 percent, February 2025 blog)
- https://api.github.com/repos/VectifyAI/PageIndex-OSS-Benchmark - the open benchmark runner, 4 stars, pushed 2026-08-17 (GitHub API, as of 2026-10-07)
- https://hn.algolia.com/api/v1/search?query=PageIndex%20Vectorless%20RAG&tags=story - the footprint scan: the 192-point Show HN (2025-08-27) and follow-ups
- https://developer.pageindex.ai/ - the cloud developer portal, serving a login wall (fetched 2026-10-07)
