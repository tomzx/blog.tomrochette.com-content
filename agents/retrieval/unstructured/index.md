---
title: Unstructured
created: 2026-10-06
updated: 2026-11-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, document-parsing, rag, mcp, llm=glm-5.4]
readability: 3
audience_notes: >
  Engineers choosing a document parser for an LLM or RAG pipeline who have met Unstructured
  as the older default and need to know where it stands now.
  Assumes familiarity with partitioning, chunking, and hosted-versus-self-hosted trade-offs.
---

Unstructured is an Apache-2.0 Python document-parsing library whose `partition` functions turn PDFs, HTML, Word files, emails, images, and more into typed elements for LLM pipelines, and the front door of a company whose pitch has moved to hosted processing.

**Unstructured is the parsing incumbent that Docling displaced, and the displacement is now the company's own positioning: the open-source library still ships, but its docs call it a prototyping starting point and the README's only pitch is a note steering readers to the hosted Transform v2 API for better output.**

## What it is

A `pip install unstructured` toolkit of per-format `partition` functions that return typed elements (titles, narrative text, tables) with metadata, plus chunking, cleaning, and staging utilities, installable directly, from Docker images for x86_64 and Apple silicon, or via conda on Windows.
The company around it sells hosted products the documentation site lists beside the library: Unstructured Transform, an MCP server and API that parses, enriches, chunks, and embeds documents inside an agent session, and Unstructured Pipelines, the enterprise platform for chunking, embedding, and image and table enrichment.
The README no longer headlines the hosted products: a note under the library description promises the open-source library stays completely free, then points readers to the Transform v2 API for higher-quality output, with a vendor table claiming 2x table content accuracy, 58 percent less invented content, and 0.878 text accuracy against the library's 0.715 (re-read 2026-11-25).
The open-source docs are one of three product tabs on the documentation site, beside Transform and Pipelines, and describe the library as "designed as a starting point for quick prototyping" with production scenarios pointed at Pipelines.

## Status

Active and still shipping: 15,563 stars and 1,349 forks as of 2026-10-13, pushed 2026-11-24 with the default branch's latest commit the 0.27.38 release commit and 490 open issues (GitHub API, as of 2026-11-25), with PyPI at 0.27.38 released 2026-11-24 across 250 releases, following 0.27.37 (2026-11-06) and 0.27.36 (2026-10-30).
The 0.27.38 release notes list one enhancement, rendering the PDF once in hi_res instead of once per pipeline stage, and carry fixes for CSV and TSV inputs, chunk overlap, and Word tables dropping rows in `text_as_html`.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Unstructured-IO/unstructured&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Unstructured-IO/unstructured&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Unstructured-IO/unstructured&type=date&legend=top-left" />
</picture>

Adoption remains large: the pepy badge reads 3M downloads a month (re-verified 2026-11-25, up from the about 2M recorded 2026-10-11).
The displacement is the story: Docling, this category's current default, has 4.4x the stars (68.7k versus 15.6k) and roughly 1.4x the monthly downloads (about 4.3M against 3M), and the largest dedicated Hacker News thread for Unstructured is 141 points from July 2023, with nothing comparable since.

## Strengths

- **Breadth with granularity: one API over dozens of formats, returning typed elements rather than raw text, which is what made it the default loader backend of the early framework-era RAG stack.**
- The hosted Transform MCP server is a genuine agent-era adaptation: an agent parses, enriches, chunks, and embeds in-session with no pipeline to build.
- The library runs anywhere its users already are: plain pip, Docker images for both major architectures, conda on Windows.

## Cautions

- **The vendor itself demoted the library: its own overview page calls it a prototyping starting point with limits and routes production to the paid Pipelines platform, so the free thing is positioned as the funnel, not the product.**
- Parsing quality on hard documents was contested from the start: top comments on the 141-point thread preferred PDFMiner's output and reached for Camelot for tables, the same hard-document tier where practitioners now report Docling's layout models winning.
- The Transform product page serves a Keycloak login (re-verified 2026-11-25), so evaluating the hosted MCP service means creating an account before seeing a document (its prices sit on the public pricing page).
- The published prices are pay-as-you-go only and drawn from a prepaid balance (Personal starts with a one-time $150 credit, Team adds a card and gets no free credit), and the Business plan stays custom-quoted.

## Pricing

The library is free under Apache-2.0.
The hosted service moved from sign-in-only and quote-only pricing to a public pricing page (read 2026-11-25): Personal with a one-time $150 free credit and top-ups from $50, Team at $0.01 a page with a shared workspace and API keys and no free credit, and Business custom-quoted, with processing drawn from a prepaid balance.
The published per-page rates for documents and images are $0.010 (Balanced, the default), $0.015 (Best), $0.002 (Fast), $0.020 (Hi-Res), and $0.030 (VLM), with audio at $0.015 a minute and video at $0.045 a minute (a video with sound draws the audio line too, $0.060 a minute).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-11-25 | Hosted service | Baseline: first published prices recorded; Personal with a one-time $150 free credit (top-ups from $50), Team $0.01/page (no free credit), Business custom; document and image rates Balanced $0.010/page (default), Best $0.015, Fast $0.002, Hi-Res $0.020, VLM $0.030, audio $0.015/min, video $0.045/min ($0.060/min with sound); before this reading Transform sat behind sign-in and Pipelines was quote-only (as of 2026-10-06). | [unstructured.io/pricing](https://unstructured.io/pricing) |

## Compared to

- [Docling](../docling/index.md): the current default, built on purpose-made layout and table models where Unstructured wraps per-format libraries; benchmark both on your worst scans before committing either way.
- [Knowhere](../knowhere/index.md): the other commercial parsing bet, hosted per page with structure-preserving chunks over MCP.
- Specialized parsers (PDFMiner, Camelot, pandoc): the per-format quality tax the 2023 thread's critics accepted, and still the safer choice when one hard format dominates your corpus.

## Bottom line

**Recommended when you need one API over many messy formats and accept library-grade rather than model-grade parsing, or as the on-ramp to its hosted pipeline if account-gated evaluation does not bother you.**
Not for hard-scan quality, where the field has moved to layout-model parsers, or for teams that need posted Business-level prices, which stay custom-quoted.
My disagreeable claim: cutting the README's hosted pitch down to one note that points readers at the paid API is the unsentimental response to parsing commoditization, and Unstructured deserves more credit than its critics give it for reading that market correctly, because the alternative was pretending the library could still win on quality.

## Changes

- 2026-10-06 - Created in the daily refresh's retrieval entrant scan.
- 2026-10-07 - Added the Unstructured-IO/unstructured star history chart to the Status section.
- 2026-10-09 - Recorded the PyPI train moving to 0.27.22 (2026-10-08, six releases in three days after 0.27.16) and refreshed the repository numbers (15,550 stars, pushed 2026-10-09); downloads and the displacement figures are unchanged.
- 2026-10-10 - Recorded PyPI 0.27.25 (2026-10-10, the first tagged release since 0.27.22) and refreshed the repository numbers (15,557 stars, pushed 2026-10-10); downloads unchanged and the Docling displacement ratio holds at 4.4x (68.6k versus 15.6k).
- 2026-10-16 - Recorded PyPI 0.27.27 (2026-10-15, 240 releases total, the first tagged release since 0.27.25) and refreshed the repository activity (pushed 2026-10-15).
- 2026-10-20 - Recorded the PyPI train moving to 0.27.30 (2026-10-19, 243 releases total, three tagged releases since 0.27.27) and refreshed the repository activity (pushed 2026-10-19).
- 2026-10-22 - Recorded the PyPI train moving to 0.27.33 (2026-10-22, 245 releases total, via 0.27.32 of 2026-10-20 with 0.27.31 skipped) and refreshed the repository activity (pushed 2026-10-22).
- 2026-10-24 - Recorded the PyPI train moving to 0.27.34 (2026-10-22, 246 releases total) and refreshed the repository activity (pushed 2026-10-24).
- 2026-10-26 - Refreshed the repository activity (pushed 2026-10-25); the PyPI train paused at 0.27.34.
- 2026-10-27 - Recorded PyPI 0.27.35 (2026-10-27, 247 releases total) and refreshed the repository activity (pushed 2026-10-27).
- 2026-10-31 - Recorded PyPI 0.27.36 (2026-10-30, 248 releases total) and refreshed the repository activity (pushed 2026-10-30).
- 2026-11-03 - Refreshed the repository activity (pushed 2026-11-02); PyPI 0.27.36 remains latest.
- 2026-11-07 - Recorded PyPI 0.27.37 (2026-11-06, 249 releases total) and refreshed the repository activity (pushed 2026-11-06).
- 2026-11-13 - Refreshed the repository activity (pushed 2026-11-13, 371 open issues); PyPI 0.27.37 remains latest.
- 2026-11-14 - Refreshed the repository activity (pushed 2026-11-14, 409 open issues); PyPI 0.27.37 remains latest.
- 2026-11-17 - Refreshed the repository activity (pushed 2026-11-17, 456 open issues); PyPI 0.27.37 remains latest.
- 2026-11-21 - Refreshed the repository activity (pushed 2026-11-19, 474 open issues); PyPI 0.27.37 remains latest across 249 releases.
- 2026-11-25 - Rotation re-verification re-fetched every cited URL live (the repository API, README, overview page, PyPI, pepy badge, enterprise page, Transform entry, and the 2023 thread all up) and recorded three moves: PyPI 0.27.38 (2026-11-24, 250 releases) with its release-note facts, the pepy badge reading 3M downloads a month against the about 2M recorded 2026-10-11 (the Docling download ratio re-read at roughly 1.4x), and the vendor's first published hosted prices (Personal one-time $150 credit, Team $0.01 a page, Business custom, with per-page rates from $0.002 to $0.030), which adds the Price history table; corrected the README description, which no longer headlines Transform and Pipelines but carries one note steering readers to the Transform v2 API, with the thesis, What-it-is, Cautions, Pricing, and Bottom-line lines aligned, and dropped the `chunk_by_title` name, which neither the README nor the overview page carries; refreshed the repository activity (pushed 2026-11-24 with the default branch's latest commit the 0.27.38 release commit, 490 open issues).

## See also

- [Docling](../docling/index.md) - the parser that displaced it as the open default
- [Knowhere](../knowhere/index.md) - the other hosted parsing pipeline in this category
- [Chonkie](../chonkie/index.md) - the chunking library its title-based chunking competes with
- [LlamaIndex](../llamaindex/index.md) - the framework whose early loaders made this library the default

## References

- https://api.github.com/repos/Unstructured-IO/unstructured - 15,563 stars and 1,349 forks (as of 2026-10-13), Apache-2.0, created 2022-09-26, pushed 2026-11-24 with the default branch's latest commit dated 2026-11-24 (the 0.27.38 release commit), 490 open issues (GitHub API, as of 2026-11-25)
- https://raw.githubusercontent.com/Unstructured-IO/unstructured/main/README.md - library scope, the stay-free note steering readers to the Transform v2 API with its benchmark table, container and conda install paths (re-fetched 2026-11-25)
- https://docs.unstructured.io/open-source/introduction/overview - the vendor's own prototyping-grade framing of the library and the three-product docs split (re-fetched 2026-11-25)
- https://pypi.org/pypi/unstructured/json - latest version 0.27.38 (2026-11-24), 250 releases, following 0.27.37 (2026-11-06) and 0.27.36 (2026-10-30), the release list grounding the train 0.27.28 (2026-10-16) through 0.27.38 with 0.27.31 skipped (fetched 2026-11-25)
- https://api.github.com/repos/Unstructured-IO/unstructured/releases/latest - 0.27.38 published 2026-11-24 and its release notes (fetched 2026-11-25)
- https://static.pepy.tech/badge/unstructured/month - 3M downloads a month (re-verified 2026-11-25; about 2M on 2026-10-11)
- https://unstructured.io/enterprise - the Pipelines platform pitch, carrying the Book A Demo and Get Started for Free entries (re-fetched 2026-11-25)
- https://unstructured.io/pricing - the published Personal, Team, and Business plans and the per-page rates behind the Pricing section and the Price history table (fetched 2026-11-25)
- https://transform.unstructured.io/ - the Transform MCP entry, serving a Keycloak login wall (re-verified 2026-11-25)
- https://hn.algolia.com/api/v1/items/36616799 - the 141-point thread (2023-07-06) with the PDFMiner and Camelot quality critique (re-fetched 2026-11-25, 141 points)
