---
title: Knowhere
created: 2026-09-20
updated: 2026-09-20
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, rag, chunking, document-parsing, mcp, open-source]
readability: 3
audience_notes: >
  Engineers building RAG over messy real-world documents (PDFs, decks, spreadsheets) who are
  choosing a parser and chunker, and weighing a hosted per-page API against self-hosting.
  Assumes familiarity with chunks, embeddings, and MCP.
---

Knowhere is a document parsing and retrieval system from Ontos AI that turns messy files (PDFs, decks, spreadsheets, images) into a persistent, navigable memory structure for agents, shipped as an Apache-2.0 open-source engine, a hosted per-page API, and an MCP server.
Facts below verified as of 2026-09-20.

**Knowhere's bet is that chunking should preserve document structure (hierarchy, tables, cross-references) instead of throwing it away, and that agents should traverse that structure like a map rather than re-parse files every session.**
The bet is real and shipping, but the public discussion footprint is nearly invisible for the star count.

## What it is

**One pipeline, two parsing tracks, three delivery surfaces.**
The Text track preserves native structure where extraction is reliable, while the Vision track sends complex PDF and PowerPoint pages to frontier vision models, and both converge into one hierarchy-native chunk schema with source-page citations.
The 2.0 release (September 8, 2026) reframed the output as corpus-native agent memory: a unified schema, hierarchy-aware tools, and resolvable evidence references that external agents consume through MCP (`@ontos-ai/knowhere-mcp`, a local stdio server) as well as through the built-in retrieval.
Surfaces: a hosted API with Python and Node SDKs plus a CLI, the open-source engine, and a separate self-hosted stack repository.
Made by Ontos AI, which open-sourced the full stack on May 7, 2026.

## Status

**Active and shipping weekly, with a striking mismatch between stars and discussion.**
3,391 stars since 2026-04-30, latest release v1.2.13 on 2026-09-17, pushed 2026-09-17 (GitHub API, as of 2026-09-20).
Two Show HNs drew a combined 2 points and 1 comment (March and September 2026), so like graft and graphify, the star count ran far ahead of any independent technical discussion.
The self-hosted stack repo has 12 stars and was last pushed 2026-08-11, so the self-hosting path looks far less trafficked than the hosted funnel.

## Strengths

- **Structure preservation is the differentiator**: hierarchy, merged-cell tables, and source-page traceability survive into the chunks, which flat chunkers discard.
- The Vision track handles dirty scans and slide decks that text-only OCR pipelines garble, and both tracks emit the same schema.
- The MCP server gives agents parse, list, outline, grep, and retrieval tools with read-only or full-access permission modes.
- Failed jobs are automatically refunded before you notice, which is the right billing posture for a per-page API.

## Cautions

- **The benchmark comparison on the marketing site is entirely self-reported**: "50 retrieval tasks across 500+ curated documents" with no published methodology and no third-party replication I could find.
- The Vision track sends your pages to frontier vision models, so the local-and-offline pitch only holds for the Text track and the self-hosted deployment.
- The PyPI name `knowhere` is an unrelated 2017 package (the real SDK is `knowhere-python-sdk`), the same name-collision trap graphify documented.
- Two Show HNs with almost no comments is a missing-community-footprint signal: nobody independent has argued about this tool in public yet.

## Pricing

**The hosted API bills per page: $0.015 per billable page ($1.50 per 100 pages), with rate-limit tiers unlocked by lifetime spend and a $5 free credit on signup (as of 2026-09-20).**
Billable pages count physical PDF pages, slide counts, one page per image, and size-derived units for text and spreadsheets; jobs that fail after billing are refunded.
The open-source engine and the self-hosted stack are free under Apache-2.0.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-20 | Cloud API | Baseline: $0.015 per billable page ($1.50 per 100 pages), $5 free signup credit, rate-limit tiers by lifetime spend; open-source engine free (Apache-2.0). | [docs.knowhereto.ai/pricing](https://docs.knowhereto.ai/pricing) |

## Compared to

- [Chonkie](../chonkie/index.md): the library approach, chunkers you embed in your own pipeline; Knowhere is the hosted-pipeline approach, where parsing, structuring, and retrieval are a service.
- [LlamaIndex](../llamaindex/index.md): the framework whose node parsers (including its Chonkie-wrapping `Chunker`) you assemble yourself; Knowhere sells the assembled pipeline.
- Plain OCR plus a vector store: cheaper and fully under your control, but you own every layout failure, which is exactly the failure mode Knowhere sells against.

## Bottom line

**Recommended for teams whose RAG corpus is dirty PDFs and decks and who would rather pay per page than maintain a parsing pipeline; spend the $5 credit on your worst documents first.**
Not for privacy-sensitive corpora on the Vision track, and not for anyone who needs independent benchmark evidence before adopting, because none exists yet.
My disagreeable claim: the near-total absence of public discussion around a 3,391-star tool is evidence against the star count, not against the tool; judge it on your own documents or not at all.

## Changes

- 2026-09-20 - Created from the 2026-09-20 entrant scan after the September 17 Show HN resurfaced the project.

## See also

- [Chonkie](../chonkie/index.md) - the chunker-library counterpart to Knowhere's hosted pipeline
- [Tree-sitter code chunking](../tree-sitter-chunking/index.md) - the code-side analogue of the structure-preserving chunking argument
- [LlamaIndex](../llamaindex/index.md) - the assemble-it-yourself framework alternative
- [Semantic code search in coding tools](../semantic-code-search/index.md) - where workspace indexing retreated, the inverse of Knowhere's bet

## References

- https://github.com/Ontos-AI/knowhere - repository, README (architecture, tracks, news timeline), stars and activity as of 2026-09-20
- https://github.com/Ontos-AI/knowhere/releases - release cadence, v1.2.13 on 2026-09-17
- https://knowhereto.ai - hosted product surface, $5 free credit, and the self-reported comparison table
- https://docs.knowhereto.ai/ - product docs: SDKs, CLI, retrieval query surface
- https://docs.knowhereto.ai/pricing - per-page pricing, billable-page counting, refund policy, rate-limit tiers
- https://docs.knowhereto.ai/mcp - MCP server tools, permission modes, host configuration
- https://github.com/Ontos-AI/knowhere-self-hosted - the self-hosted stack, 12 stars as of 2026-09-20
- https://hn.algolia.com/api/v1/items/49738595 - the September 17, 2026 Show HN, 1 point, 0 comments
- https://hn.algolia.com/api/v1/items/47505117 - the March 24, 2026 Show HN, 1 point, 1 comment
- https://pypi.org/pypi/knowhere/json - the unrelated PyPI name-squat grounding the caution
