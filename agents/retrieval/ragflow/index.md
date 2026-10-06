---
title: RAGFlow
created: 2026-10-06
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, retrieval, rag, document-parsing, agents]
readability: 3
audience_notes: >
  Engineers choosing a RAG engine or a knowledge base their agents can query with citations.
  Assumes familiarity with chunking, embeddings, and self-hosting trade-offs.
---

RAGFlow is an Apache-2.0 open-source RAG engine from InfiniFlow that turns documents into a cited, agent-usable knowledge base through layout-aware parsing, template-based chunking, and an agentic retrieval workflow, deployable self-hosted over Docker or through its cloud.

**RAGFlow is the largest bet that the retrieval engine itself is the product, and its 91.7k stars measure how badly DIY RAG teams wanted a deployable stack with inspectable chunks and grounded citations, but a disruptive 1.0 rewrite and an unpatched-RCE disclosure are the costs of adopting it.**

## What it is

A full engine, not a library: DeepDoc handles layout analysis, OCR, and table recognition, chunking is template-based per document kind (Word, slides, Excel, images, scanned copies, structured data, web pages, and more), and every answer ships with traceable citations plus a chunk view you can correct by hand.
Since August 2026 it compiles datasets into agent-usable knowledge artifacts (wikis, graphs, trees, page indexes, mind maps, timelines, skills) and runs agentic retrieval with Low, Medium, High, and Ultra thinking modes.
Surfaces: a web UI, REST API and Python SDK, an optional MCP server and sandbox executor, Docker deployment, and a hosted cloud.
Made by InfiniFlow, with v1.0.0-rc1 (2026-09-29) rewriting the service layer in Go: API, Admin, Ingestor, and Syncer as one Go service, NATS for messaging, Kvrocks for cache and checkpoints.

## Status

Very active and very large: 91,710 stars, 10,893 forks since 2023-12-12, pushed 2026-10-05 (GitHub API, as of 2026-10-06), with 3.9M Docker pulls (ragflow-stats badge, as of 2026-10-06).
The latest release is v1.0.0-rc1 (2026-09-29), a preview of the comprehensive Go rewrite, and its release notes warn that the data upgrade from v0.27.2 is irreversible.
The discussion footprint is front-loaded: a 230-point launch thread in April 2024 with 53 comments, 294 comment mentions on Hacker News since the start of 2025 (as of 2026-10-06), and only 2 of those in 2026 itself, a quieting worth weighing against the star count.

## Strengths

- **Template-based chunking with a human-in-the-loop chunk view makes the parsing story inspectable, which is the claim most DIY RAG stacks cannot make about their own pipeline.**
- Grounded citations and chunk-level traceability ship in the box, the feature teams most often build badly themselves.
- The agent surface is substantial: agentic retrieval modes, knowledge compilation into artifacts agents can read, and an MCP server so coding agents consume the knowledge base directly.
- Scale buys support: 3.9M Docker pulls and a repository this size mean the bug you hit is probably already filed.

## Cautions

- **ZeroPath disclosed a post-auth RCE in RAGFlow 0.24 (April 2026) affecting instances that use Infinity for chunk storage, reported to the project on 2026-03-03 as GHSA-vw46-rrp3-c99v and unpatched as of the article, with about 1,918 instances exposed on the public internet; GitHub's global advisory database has no such advisory (checked 2026-10-06), so the disclosure was never formally published.**
- The 1.0 rewrite is disruptive by its own release notes: a one-way data migration from v0.27.2, the local sandbox dropped, DeepDoc CPU-only, and the Team/Me permission model not yet supported.
- Self-hosting is a stack, not a binary: the README recommends 4 CPU cores, 16 GB RAM, and 50 GB disk, and the compose file carries MySQL plus a document engine (Elasticsearch, with kernel tuning, or Infinity) alongside the new NATS and Kvrocks services.
- The cloud free tier is deliberately tiny (0.1 GB storage, 500 credits a month, no API key), and the cloud app itself is a login-walled client-side application, so the tiers are only readable on the marketing page.

## Pricing

Self-hosted is free under Apache-2.0.
Cloud, as of 2026-10-06: Free at $0 a month (5 apps, 1 member, 0.1 GB storage, 500 credits/month, no API key), Starter at $29 a month (shown struck through from $59; 50 apps, 5 members, 5 GB, 5,000 credits, API key), Pro at $129 a month (struck through from $259; unlimited apps, 20 members, 50 GB, 20,000 credits), Enterprise custom with BYOC, on-premises, and custom SLA.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-06 | Cloud | Baseline: Free $0/mo (500 credits, 0.1 GB, no API key), Starter $29/mo (marked down from $59), Pro $129/mo (marked down from $259), Enterprise custom; self-hosted free (Apache-2.0). | [ragflow.io/#pricing-plan](https://ragflow.io/#pricing-plan) |

## Compared to

- [Docling](../docling/index.md): the parser layer RAGFlow bundles as DeepDoc; if you already run a parser and a vector store, RAGFlow replaces that whole pipeline rather than slotting into it.
- [Knowhere](../knowhere/index.md): the other parse-then-serve bet; Knowhere is hosted per-page parsing with structure-preserving chunks over MCP, RAGFlow is the full engine you deploy.
- [LlamaIndex](../llamaindex/index.md): the framework where you assemble this yourself; RAGFlow sells the assembled, cited, UI-bearing result.

## Bottom line

**Recommended for teams that want a deployable, citation-grounded knowledge base for agents and will operate the stack it needs, starting on their hardest documents exactly because the parsing claims are inspectable.**
Not for embedding search inside an application process (that is Orama's slot) or for code repositories (that is open-codebase-index's slot).
My disagreeable claim: what RAGFlow actually sells is trust, and the star count says the market's scarcest RAG ingredient was never layout accuracy, it was being able to see and fix what the retriever read.

## Changes

- 2026-10-06 - Created in the daily refresh's retrieval entrant scan.

## See also

- [Docling](../docling/index.md) - the open parser whose layout-and-table niche RAGFlow internalizes as DeepDoc
- [Knowhere](../knowhere/index.md) - the hosted counterpart selling document parsing as a per-page service
- [Chonkie](../chonkie/index.md) - the chunking-library approach to the splitting step RAGFlow templates
- [AnythingLLM](../../assistant-runtimes/anything-llm/index.md) - the assistant-runtime neighbor where the document-chat application pattern lives

## References

- https://api.github.com/repos/infiniflow/ragflow - 91,710 stars, 10,893 forks, Apache-2.0, Go, created 2023-12-12, pushed 2026-10-05 (GitHub API, as of 2026-10-06)
- https://raw.githubusercontent.com/infiniflow/ragflow/main/README.md - DeepDoc, template-based chunking, knowledge compilation, agentic retrieval modes, Go-native architecture, deployment requirements
- https://raw.githubusercontent.com/infiniflow/ragflow/main/docs/release_notes.md - the v1.0.0-rc1 Go rewrite, NATS and Kvrocks migration, irreversible v0.27.2 upgrade, known issues
- https://api.github.com/repos/infiniflow/ragflow/releases/latest - v1.0.0-rc1 published 2026-09-29
- https://ragflow.io/ - the pricing section: Free $0, Starter $29 (from $59), Pro $129 (from $259), Enterprise custom (as of 2026-10-06)
- https://ragflow.io/docs/ - official docs root (server-rendered; the /docs/dev/ path meta-refreshes here)
- https://zeropath.com/blog/ragflow-rce-unpatched-vulnerability - the April 2026 post-auth RCE disclosure (GHSA-vw46-rrp3-c99v, Shodan-exposed instances), the critical source
- https://api.github.com/advisories/GHSA-vw46-rrp3-c99v - 404 on 2026-10-06: the advisory was never published to GitHub's global database
- https://hn.algolia.com/api/v1/items/39896923 - the 230-point launch thread, 2024-04-01
- https://hn.algolia.com/api/v1/search?query=ragflow&tags=story - the story-footprint scan behind the launch-thread claims
- https://hn.algolia.com/api/v1/search?query=ragflow&tags=comment - the comment-footprint scans behind the 294-since-2025 and 2-in-2026 claims
- https://raw.githubusercontent.com/infiniflow/ragflow-stats/main/badges/docker-pulls.json - 3.9M Docker pulls (as of 2026-10-06)
- https://cloud.ragflow.io/ - the cloud app (a client-rendered JS shell; tiers read from the marketing page instead)
