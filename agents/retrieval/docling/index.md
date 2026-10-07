---
title: Docling
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, document-parsing, rag]
readability: 3
audience_notes: >
  Engineers choosing a document parser to feed a RAG or agent pipeline.
  Assumes you know what chunking, embeddings, OCR, and a layout model are.
---

Docling is an MIT-licensed Python document-parsing library, started by IBM's Deep Search team and now listed as an LF AI & Data project, that converts PDF, Office files, images, audio, and video into a unified DoclingDocument exportable to Markdown, JSON, HTML, and DocTags.

**Docling became the default open document parser on the strength of its layout and table model lineage, but its pipeline leans on PyTorch and specialized models by design, which makes it heavyweight for slim deployments and keeps a market open for lighter parsers and hosted pipelines.**

## What it is

A `pip install docling` library whose converter takes PDF, DOCX, PPTX, XLSX, HTML, EPUB, email, images, audio, video, and more, and produces one typed document representation with reading order, tables, figures, code, formulas, and chart structure.
The PDF path runs layout and table-structure models (DocLayNet and TableFormer in the project's technical report, arXiv 2408.09869) plus OCR engines, and an optional VLM pipeline fronted by granite-docling-258M, a 258M-parameter Apache-2.0 model built on Idefics3 with a siglip2 encoder and a Granite 165M language model.
It ships a CLI, a docling-serve REST API server for running it as a service, an MCP server for agent access, chunking utilities for RAG, and integrations with LangChain, LlamaIndex, Haystack, and CrewAI.
Local execution is a stated design goal for sensitive and air-gapped data.
The repository was created 2024-07-09 as IBM's ds4sd/docling and now lives under the docling-project organization with a Linux Foundation AI & Data listing.

## Status

Very active and very large: 68,429 stars, 5,003 forks, 1,007 open issues, and a push on 2026-10-06 as of 2026-10-06.

[![Star History Chart](https://api.star-history.com/chart?repos=docling-project/docling&type=date&legend=top-left)](https://www.star-history.com/?repos=docling-project%2Fdocling&type=date&legend=top-left)

PyPI shows version 2.134.0 released 2026-10-06 across 222 releases, with Python 3.9 support dropped at 2.70.0, and the pepy badge reports about 3M downloads in the last month as of 2026-10-06 (pypistats returned 429 this run; its last confirmed figure was 2,834,838 on 2026-10-05).
The HN footprint is thin for that scale: the largest story thread I found is 13 points from 2024-11-03, which says adoption flows through framework integrations and tutorials rather than launch-driven attention.
The project's docs now advertise a managed path, Docling for IBM watsonx, exposing the same REST API as the self-hosted server.

## Strengths

- **The structured-understanding lineage is the product: layout, reading order, and table structure from purpose-built models, wrapped in one typed document format you can ground citations against.**
- Format breadth is unusual, from PDF and Office to audio, video, XBRL, and email, behind one converter interface.
- The ecosystem surface is where its scale shows: first-party LangChain and LlamaIndex recipes, an MCP server, docling-serve, and in-package chunkers make it the default upstream of most DIY RAG stacks.
- granite-docling-258M gives it an open, small, purpose-built VLM option that no lighter parser has an equivalent of.

## Cautions

- **The default pipeline is heavyweight: the installation docs state the models depend on PyTorch, and three issues from 2026 (#3997, #4100, #3793) exist specifically to defer torch, pypdfium2, and other heavy imports so slim installs can work.**
- Quality on hard documents is contested: practitioners in a June 2026 HN thread report marker with forced OCR outperforming it on long or complex scans, with one reporting that docling gives them garbage on exactly those documents.
- A May 2026 HN comparison describes it as the heavier, GPU-leaning side of the local-parsing trade-off, which matters for CPU-only deployments.
- The managed path routes through IBM watsonx, so the zero-ops option is also a lock-in option.
- Roughly a thousand open issues is the cost of being the default: bugs across dozens of formats and platforms all land here.

## Pricing

Free and open source under MIT; the cost of running it is your own compute for the torch-based models.
Self-hosting the REST API is free via docling-serve, and the docs' managed path, Docling for IBM watsonx, is quoted through IBM rather than priced on the project pages I fetched, so no prices belong in this note and no price history table applies.

## Compared to

- [Chonkie](../chonkie/index.md): complementary, not competing; Docling produces the structured text, Chonkie splits it, and Docling's own chunking docs cover the handoff.
- Hosted parsing pipelines (Mistral OCR, watsonx managed): choose hosted for zero infrastructure and hard-scan quality, Docling for local execution, volume economics, and privacy.
- [LlamaIndex](../llamaindex/index.md) and [LangChain](../langchain/index.md) document readers: Docling's integrations effectively make it the parser layer those frameworks call, and its own recipes say as much.

## Bottom line

**Recommended as the default self-hosted document parser for RAG and agent pipelines that need real structure (tables, reading order, formulas) and can carry a PyTorch dependency.**
Not for slim or CPU-bound deployments without the slim-install work, and not to be trusted blind on damaged scans: benchmark it against your own corpus before committing.
My disagreeable claim: Docling's dominance owes as much to IBM's distribution and first-party framework integrations as to parsing quality, and its scale has made it the commodity layer that other tools now advertise themselves against.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars scan surfaced it.
- 2026-10-07 - Added the docling-project/docling star history chart to the Status section.

## See also

- [Chonkie](../chonkie/index.md) - the downstream chunker that typically consumes what Docling produces
- [LangChain](../langchain/index.md) - first-party integration recipes make Docling the parser layer behind many LangChain RAG stacks
- [LlamaIndex](../llamaindex/index.md) - the other first-party integration this category tracks, including the DoclingReader
- [Graphify](../../context-engines/graphify/index.md) - the context-engine sibling that also turns raw sources into agent-usable structure

## References

- https://api.github.com/repos/docling-project/docling - 68,429 stars, 5,003 forks, MIT, created 2024-07-09, pushed 2026-10-06, 1,007 open issues, as of 2026-10-06
- https://raw.githubusercontent.com/docling-project/docling/main/README.md - format list, DoclingDocument, exports, integrations, MCP server, docling-serve, LF AI & Data badge
- https://arxiv.org/abs/2408.09869 - the technical report grounding the DocLayNet layout and TableFormer table models and the MIT, commodity-hardware claims
- https://docling-project.github.io/docling/getting_started/installation/ - the PyTorch dependency, install extras, and the Python 3.9 cutoff at 2.70.0
- https://pypi.org/pypi/docling/json - version 2.134.0 (2026-10-06), 222 releases, Python >=3.10
- https://pypistats.org/api/packages/docling/recent - 2,834,838 downloads in the last month, as of 2026-10-05 (429 on 2026-10-06, kept dated)
- https://static.pepy.tech/badge/docling/month - about 3M downloads a month, corroborating the pypistats figure (as of 2026-10-06)
- https://api.github.com/search/issues?q=repo:docling-project/docling+install+size+OR+heavy+OR+torch+in:title - issues #3997, #4100, and #3793, the slim-install and lazy-import work
- https://hn.algolia.com/api/v1/search?query=docling&tags=comment - practitioner comments: the GPU-heavy comparison, the marker-plus-forced-OCR preference, and the wrapper question
- https://hn.algolia.com/api/v1/search?query=docling&tags=story - the story-footprint scan grounding the thin-HN observation (top thread 13 points, 2024-11-03)
- https://lfaidata.foundation/projects/ - the LF AI & Data project listing
- https://huggingface.co/ibm-granite/granite-docling-258M/raw/main/README.md - granite-docling-258M: Apache-2.0, Idefics3-based, siglip2 encoder, Granite 165M language model
- https://docling-project.github.io/docling/usage/api_server/ - the self-hosted REST API server
- https://docling-project.github.io/docling/usage/api_server/managed/ - the managed path: Docling for IBM watsonx, same REST API, no published prices
