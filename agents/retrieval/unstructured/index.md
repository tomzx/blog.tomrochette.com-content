---
title: Unstructured
created: 2026-10-06
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, document-parsing, rag, mcp]
readability: 3
audience_notes: >
  Engineers choosing a document parser for an LLM or RAG pipeline who have met Unstructured
  as the older default and need to know where it stands now.
  Assumes familiarity with partitioning, chunking, and hosted-versus-self-hosted trade-offs.
---

Unstructured is an Apache-2.0 Python document-parsing library whose `partition` functions turn PDFs, HTML, Word files, emails, images, and more into typed elements for LLM pipelines, and the front door of a company whose pitch has moved to hosted processing.

**Unstructured is the parsing incumbent that Docling displaced, and the displacement is now the company's own positioning: the open-source library still ships weekly, but its docs call it a prototyping starting point and the README leads with a login-walled hosted MCP service and a quote-priced platform.**

## What it is

A `pip install unstructured` toolkit of per-format `partition` functions that return typed elements (titles, narrative text, tables) with metadata, plus `chunk_by_title` splitting, cleaning, and staging utilities, installable directly, from Docker images for x86_64 and Apple silicon, or via conda on Windows.
The company around it sells two hosted products the README now headlines: Unstructured Transform, an MCP server that parses, enriches, chunks, and embeds 60-plus file types inside an agent session, and Unstructured Pipelines, the enterprise platform with a low-code UI or API for chunking, embedding, and image and table enrichment.
The open-source docs are one of three product tabs on the documentation site, beside Transform and Pipelines, and describe the library as "designed as a starting point for quick prototyping" with production scenarios pointed at Pipelines.

## Status

Active and still shipping: 15,529 stars, 1,350 forks since 2022-09-26, pushed 2026-10-05 (GitHub API, as of 2026-10-06), with PyPI at 0.27.16 released 2026-10-05 and five releases between 2026-09-14 and 2026-10-05.
Adoption remains large: about 2M downloads a month (pepy badge, as of 2026-10-06).
The displacement is the story: Docling, this category's current default, has 4.4x the stars (68.4k versus 15.5k) and roughly 1.5x the monthly downloads, and the largest dedicated Hacker News thread for Unstructured is 141 points from July 2023, with nothing comparable since.

## Strengths

- **Breadth with granularity: one API over dozens of formats, returning typed elements rather than raw text, which is what made it the default loader backend of the early framework-era RAG stack.**
- The hosted Transform MCP server is a genuine agent-era adaptation: an agent parses, enriches, chunks, and embeds in-session with no pipeline to build.
- The library runs anywhere its users already are: plain pip, Docker images for both major architectures, conda on Windows.

## Cautions

- **The vendor itself demoted the library: its own overview page calls it a prototyping starting point with limits and routes production to the paid Pipelines platform, so the free thing is positioned as the funnel, not the product.**
- Parsing quality on hard documents was contested from the start: top comments on the 141-point thread preferred PDFMiner's output and reached for Camelot for tables, the same hard-document tier where practitioners now report Docling's layout models winning.
- The Transform product page serves a Keycloak login (fetched 2026-10-06), so evaluating the hosted MCP service means creating an account before seeing a price or a document.
- Platform pricing is quote-only, a demo-request form with no public numbers.

## Pricing

The library is free under Apache-2.0.
Transform advertises a "Get Started for Free" entry but its product page sits behind sign-in, so no tier prices are publicly fetchable (as of 2026-10-06).
Pipelines is quoted through a demo request, with no published prices.

## Compared to

- [Docling](../docling/index.md): the current default, built on purpose-made layout and table models where Unstructured wraps per-format libraries; benchmark both on your worst scans before committing either way.
- [Knowhere](../knowhere/index.md): the other commercial parsing bet, hosted per page with structure-preserving chunks over MCP.
- Specialized parsers (PDFMiner, Camelot, pandoc): the per-format quality tax the 2023 thread's critics accepted, and still the safer choice when one hard format dominates your corpus.

## Bottom line

**Recommended when you need one API over many messy formats and accept library-grade rather than model-grade parsing, or as the on-ramp to its hosted pipeline if account-gated evaluation does not bother you.**
Not for hard-scan quality, where the field has moved to layout-model parsers, and not for teams that require public pricing before adopting a hosted layer.
My disagreeable claim: leading your README with the hosted MCP server is the unsentimental response to parsing commoditization, and Unstructured deserves more credit than its critics give it for reading that market correctly, because the alternative was pretending the library could still win on quality.

## Changes

- 2026-10-06 - Created in the daily refresh's retrieval entrant scan.

## See also

- [Docling](../docling/index.md) - the parser that displaced it as the open default
- [Knowhere](../knowhere/index.md) - the other hosted parsing pipeline in this category
- [Chonkie](../chonkie/index.md) - the chunking library its `chunk_by_title` competes with
- [LlamaIndex](../llamaindex/index.md) - the framework whose early loaders made this library the default

## References

- https://api.github.com/repos/Unstructured-IO/unstructured - 15,529 stars, 1,350 forks, Apache-2.0, created 2022-09-26, pushed 2026-10-05 (GitHub API, as of 2026-10-06)
- https://raw.githubusercontent.com/Unstructured-IO/unstructured/main/README.md - library scope, the Transform MCP and Pipelines leads, container and conda install paths
- https://docs.unstructured.io/open-source/introduction/overview - the vendor's own prototyping-grade framing of the library and the three-product docs split
- https://api.github.com/repos/Unstructured-IO/unstructured/releases?per_page=5 - 0.27.16 (2026-10-05) and the September release cadence
- https://pypi.org/pypi/unstructured/json - latest version 0.27.16
- https://static.pepy.tech/badge/unstructured/month - about 2M downloads a month (as of 2026-10-06)
- https://unstructured.io/enterprise - the Pipelines platform pitch and the demo-request pricing model
- https://transform.unstructured.io/ - the Transform MCP entry, serving a Keycloak login wall (fetched 2026-10-06)
- https://hn.algolia.com/api/v1/items/36616799 - the 141-point thread (2023-07-06) with the PDFMiner and Camelot quality critique
