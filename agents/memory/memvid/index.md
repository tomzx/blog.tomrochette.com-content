---
title: Memvid
created: 2026-10-08
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, file-format, single-file, rust]
readability: 3
audience_notes: >
  Engineers who want agent memory as one portable artifact they own, and who remember (or
  have heard of) the QR-code-in-video version of Memvid. Assumes you know what BM25 and
  vector indexes are.
---

Memvid is a portable single-file memory engine: a Rust core packs documents, embeddings, and indexes into one `.mv2` file that agents reach through SDKs, a CLI, and (per the site) MCP, with no server or database behind it.

**Its bet is that memory should ship as one portable artifact you own, not a service you run; the twist is that the viral version of that bet, QR codes in video files, is now the deprecated history.**

## What it is

An Apache-2.0 repository under Memvid, Inc., with a Rust crate (`memvid-core` 2.0), an npm SDK and CLI, and a PyPI SDK.
The v2 model is "Smart Frames": append-only immutable frames carrying content, timestamps, and checksums, grouped for compression and parallel reads inside a single `.mv2` file whose layout is a 4KB header, an embedded write-ahead log, compressed data segments, a Tantivy BM25 index, an optional HNSW vector index, a time index, and a table of contents.
Capsules (`.mv2`) add shareable units with rules and expiry, and an optional password-encrypted variant exists.
The marketing site now sells an enterprise "knowledge layer" engagement around the same file format, with demo-call pricing and no published numbers.

## Status

**Large stars, young rewrite, paused shipping.**
16,583 stars with the repository pushed 2026-07-14, created 2025-05-27, as of 2026-10-08 (GitHub API), nearly three months without a push.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=memvid/memvid&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=memvid/memvid&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=memvid/memvid&type=date&theme=dark&legend=top-left" />
</picture>

The registry trains last moved before the quiet stretch: npm memvid-cli at 2.0.160 (May 27, 2026) and PyPI memvid-sdk 2.0.160.
The history matters: the v1 approach (text as QR codes in MP4 frames) went viral with a 61-point Show HN in May 2025 and a 9-point follow-up, and the README now marks v1 deprecated, pointing QR references to a deprecation page.
The benchmark claims (+35 percent over the field on LoCoMo, sub-5ms P50 search) are the vendor's own, with no independent run I could find.

## Strengths

- **The single-artifact model is genuinely portable**: data, indexes, WAL, and TOC in one file with no sidecars, deployable on-prem or air-gapped.
- Append-only immutable frames with checksums make the store crash-safe and support timeline queries over past memory states.
- The index binds to its embedding model and fails fast on mismatch, closing the model-mixing footgun most local stores leave open.
- No server, no account, no network required after setup.

## Cautions

- **The mechanism that made it famous is deprecated, and the v2 rewrite is quiet**: no push since mid-July and registry releases frozen since late May.
- Every performance number is self-published, and the site's testimonial wall and comparison table against Pinecone, Chroma, Weaviate, and Qdrant are marketing.
- No contradiction or decay handling: an append-only timeline accrues, which is the exact problem the temporal members here exist to solve.
- The agent-facing surface is thin: no harness adapters in the repo, and MCP appears in marketing copy rather than the README.

## Pricing

Free and open: the engine and all SDKs are Apache-2.0.
The enterprise engagement is sold through demo calls with no published price, as of 2026-10-08.

## Compared to

- [Memoryfields](../memoryfields/index.md): both make memory a portable file; Memoryfields is a plain-markdown spec with minimal tooling, Memvid is a compiled binary format with working indexes.
- [Zep](../zep/index.md): temporal validity windows versus Memvid's timeline index; Zep for facts that change, Memvid for archive-like recall of what was said.
- [claude-mem](../claude-mem/index.md): harness-bound session compression in SQLite; Memvid's file is deliberately harness-free and session-free.

## Bottom line

**Recommended for developers who want one portable, offline memory artifact and will verify the benchmark claims on their own corpus first.**
Not for teams needing a maintained dependency today, multi-user memory, or any contradiction handling at all.

## Changes

- 2026-10-08 - Created from the 2026-10-08 awesome-list entrant scan, with seven fetched sources; the v1-QR-to-v2-frames pivot and the self-published-benchmark caution recorded as the critical angles.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [Memoryfields](../memoryfields/index.md) - the plain-markdown portable-format sibling
- [claude-mem](../claude-mem/index.md) - the harness-bound SQLite alternative
- [Zep](../zep/index.md) - the temporal-service alternative for facts that change

## References

- https://github.com/memvid/memvid - repository, 16,583 stars, activity, Apache-2.0, as of 2026-10-08
- https://raw.githubusercontent.com/memvid/memvid/master/README.md - the Smart Frames architecture, file layout, SDK table, feature flags, and the v1 deprecation notice
- https://www.memvid.com - the enterprise positioning, MCP mention, and the <5ms and +35 percent claims, as of 2026-10-08
- https://news.ycombinator.com/item?id=44125598 - the v1 viral Show HN (61 points, 23 comments, 2025-05-29)
- https://news.ycombinator.com/item?id=44134122 - the v1 follow-up thread (9 points, 2025-05-30)
- https://pypi.org/pypi/memvid-sdk/json - memvid-sdk 2.0.160, the frozen-train record
- https://registry.npmjs.org/memvid-cli - memvid-cli 2.0.160 (2026-05-27)
