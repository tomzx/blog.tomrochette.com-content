---
title: Chonkie
created: 2026-09-16
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, chunking, rag, retrieval]
readability: 3
audience_notes: >
  Engineers choosing a chunker for a RAG pipeline over documents or code.
  Assumes familiarity with embeddings, tokenizers, and what a text splitter does.

---

Chonkie is an MIT-licensed Python (with a TypeScript port) chunking library for RAG pipelines that packages token-based, sentence, recursive, semantic, late, code (AST), and neural chunkers behind one small, dependency-light interface.

**It won the chunking niche on install size and speed, survived the niche's commoditization, and outlived its own company's attention: the library keeps shipping while the startup behind it has moved on to a new venture.**

## What it is

The README's chunker table covers `TokenChunker`, `FastChunker` (SIMD-accelerated byte chunking, the memchunk engine), `SentenceChunker`, `RecursiveChunker`, `SemanticChunker` (embedding-similarity boundaries, in the Greg Kamradt lineage), `LateChunker` (embeds before splitting, per the late-chunking paper), `CodeChunker` (AST-based code splits), `NeuralChunker` (model-based segmentation), `SlumberChunker` (LLM-verified split points), `TableChunker` (markdown tables), and `TeraflopAIChunker` (a vendor segmentation API), with a `pip install chonkie` core the repo badges at 505KB and optional extras for semantic, code, and API dependencies.
It also ships refineries, pipelines stored in a local SQLite database, a self-hosted REST API server (`uvicorn chonkie.api.main:app`), works with transformers, tokenizers, and tiktoken tokenizers, and publishes its own agent skills (`npx skills add chonkie-inc/skills`).
**The project began as bhavnicksm/chonkie (Show HN, 199 points, November 2024), became a YC-backed company with a 151-point Launch HN in June 2025 (the YC directory lists Feyn, Spring 2025 batch, same founders), and the repository now lives under the Feyn Labs org as feyninc/chonkie, though the original author repository now 404s.**

## Status

The open source library is active and widely used; the company around it has visibly moved on.
The repository shows 4,790 stars (as of 2026-10-13) and a push on 2026-10-23 (GitHub API, as of 2026-10-24), and PyPI shows version 1.7.0 released 2026-07-07 across 62 releases, with 1,255,276 downloads in the last month (the same figure recorded 2026-10-06, re-verified 2026-10-24); the TypeScript port, renamed alongside the org to feyninc/chonkiejs, was last pushed 2026-10-03.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=feyninc/chonkie&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=feyninc/chonkie&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=feyninc/chonkie&type=date&legend=top-left" />
</picture>

**The caution is the corporate trail: chonkie.ai, the domain in the Launch HN, now redirects to Feyn Labs, a venture whose founder letter is signed by Chonkie's co-founder Shreyash Nigam, the repository itself moved under the Feyn org (feyninc/chonkie, with the old chonkie-inc URL redirecting), the hosted endpoints (cloud.chonkie.ai, hub.chonkie.ai, labs.chonkie.ai) are dead or 404, and the README still links Cloud to the dead labs domain.**
The community footprint earlier scans missed exists: two major HN threads (199 points in 2024, 151 in 2025) plus a 153-point technical post ("So, you want to chunk really fast?", December 2025) by co-founder Bhavnick Minhas on his delimiter-based memchunk approach.

## Strengths

- **The lightweight pitch held up: a small default install working with any tokenizer, which is exactly what bloated framework splitters made painful.**
- The chunker menu spans cheap to expensive strategies (token to neural) behind one interface, so upgrading a pipeline's splitter is a one-line change.
- Adoption is broad: over a million PyPI downloads a month and framework integration, with LlamaIndex's newer `Chunker` node parser delegating to Chonkie rather than reimplementing chunking.
- Still maintained: releases through July 2026 and pushes into October 2026, no deprecation notice.

## Cautions

- **The commercial layer is gone: the cloud API the 2025 launch sold is dead, so anything built on Chonkie Cloud needs migration to the self-hosted API server, and the docs' "via our API" wording is now stale.**
- The benchmark claims (15MB versus 80-170MB installs, up to 33x faster token chunking than LangChain and LlamaIndex) are vendor-run and unverified independently; the repo's BENCHMARKS.md is maintained by the vendor.
- The practitioners' ranking cuts against premium chunking: Continue's custom code RAG guide ranks truncation and fixed-length chunking above AST chunking because long-context embedding models fit most files whole.
- Dependency on a venture that has pivoted means roadmap risk: Feyn Labs is about training custom models, not chunking.

## Pricing

**The library is free and MIT-licensed; the paid hosted API it once sold is dead, and the replacement is running the bundled self-hosted REST API server yourself.**
Costs beyond integration time are the usual RAG bill: embedding API calls for semantic and late chunking, or GPU time for the neural chunker.

## Compared to

- [LangChain](../langchain/index.md) and [LlamaIndex](../llamaindex/index.md) splitters: the benchmark targets; LlamaIndex now wraps Chonkie for chunking, which concedes where the effort should live, while LangChain offers separator-based splitting only.
- [Tree-sitter code chunking](../tree-sitter-chunking/index.md): the code-specific alternative; Chonkie's `CodeChunker` competes in the same AST-aware niche with less per-language machinery.
- Fixed-length and truncation chunking: the practitioners' default; per Continue's guide they beat fancier chunking for most corpora with 16k-token embedding models.

## Bottom line

**Recommended as the default chunker library when a pipeline genuinely needs splitting beyond naive truncation, since it is small, maintained, and framework-accepted.**
Not for anyone wanting a hosted or supported product: that part of Chonkie no longer exists.
My disagreeable claim: Chonkie's actual innovation was packaging, not algorithms, and its founders' move to a new venture says as much about chunking's commoditization as any benchmark does.

## Changes

- 2026-09-16 - Created.
- 2026-09-18 - Refreshed volatile facts for the 2026-09-18 verification: 4,755 stars, a push on 2026-09-18, and 1,081,591 PyPI downloads in the last month (pypistats answered again after the 2026-09-16 blocking).
- 2026-09-20 - Recorded the repository's move under the Feyn Labs org (feyninc/chonkie, the chonkie-inc URL now redirects) and refreshed the star count to 4,760; PyPI, releases, and the stale Cloud link unchanged.
- 2026-09-20 - Recorded the TypeScript port's matching rename to feyninc/chonkiejs and refreshed the trailing-month PyPI figure to 1,046,347 as of 2026-09-20.
- 2026-09-25 - Refreshed the volatile facts: 4,770 stars and 1,138,639 trailing-month PyPI downloads as of 2026-09-25; version 1.7.0, the push date, and the JS port unchanged.
- 2026-10-07 - Added the feyninc/chonkie star history chart to the Status section.
- 2026-10-11 - Reworded banned-term words out of the prose and refreshed the volatile figures for the 2026-10-11 verification; meaning unchanged.
- 2026-10-19 - Rotation re-verification re-fetched every cited URL live (PyPI 1.7.0, downloads, and repo numbers all unchanged); corrected the chunker-table list to the README's full eleven chunkers (adding Slumber, Table, and TeraflopAI, present since before the last verification) and corrected the YC batch claim to the YC directory's Spring 2025 listing for Feyn, since the launch title's own label has read both X25 (Algolia crawl) and P25 (live page).
- 2026-10-22 - Refreshed the repository activity (pushed 2026-10-20) and re-verified the trailing-month downloads unchanged; PyPI 1.7.0 remains latest.
- 2026-10-24 - Refreshed the repository activity (pushed 2026-10-23) and re-verified the trailing-month downloads unchanged; PyPI 1.7.0 remains latest.

## See also

- [LlamaIndex](../llamaindex/index.md) - its `Chunker` node parser delegates to Chonkie
- [Tree-sitter code chunking](../tree-sitter-chunking/index.md) - the code-specific AST chunking approach the `CodeChunker` competes with
- [LangChain](../langchain/index.md) - the splitter benchmark target with no AST chunker of its own
- [Context Management Patterns](../../context-management-patterns/index.md) - the size-threshold essay asking whether bespoke chunking matters at all

## References

- https://github.com/feyninc/chonkie - repository: 4,790 stars (as of 2026-10-13), MIT, created 2025-03-29, pushed 2026-10-23 (GitHub API, as of 2026-10-24)
- https://raw.githubusercontent.com/feyninc/chonkie/main/README.md - chunker table (11 chunkers), 505KB core, self-hosted API server, stale Cloud link (re-verified unchanged 2026-10-19; the file last changed 2026-06-05)
- https://pypi.org/pypi/chonkie/json - version 1.7.0 (2026-07-07), 62 releases, Python >=3.10, MIT (re-verified unchanged 2026-10-19)
- https://pypistats.org/api/packages/chonkie/recent - 1,255,276 downloads last month, unchanged and re-verified 2026-10-24
- https://docs.chonkie.ai - official docs, Python and JavaScript support, agent skills distribution (re-verified 2026-10-19)
- https://news.ycombinator.com/item?id=44225930 - Launch HN, 151 points, 2025-06-09: founders, 15MB versus 80-170MB, 33x token chunking claims (vendor tests); the title's batch label has read both X25 (Algolia crawl) and P25 (live page)
- https://news.ycombinator.com/item?id=42100819 - original Show HN, 199 points, 2024-11-10, under the now-deleted bhavnicksm/chonkie
- https://news.ycombinator.com/item?id=46501665 - "So, you want to chunk really fast?", 153 points, 2026-01-05
- https://minha.sh/posts/so,-you-want-to-chunk-really-fast - co-founder's memchunk post (delimiter-based SIMD chunking), December 2025
- https://usefeyn.com - Feyn Labs founder letter signed by Shreyash Nigam, the redirect target of chonkie.ai
- https://www.ycombinator.com/companies/chonkie - the YC directory entry (redirects to /companies/feyn): Feyn, Spring 2025 batch, founders Shreyash Nigam and Bhavnick Minhas
- https://hn.algolia.com/api/v1/search?query=chonkie - the footprint scan: launch threads, JS port, Cloud, and code-chunking Show HNs
