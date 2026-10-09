---
title: Hindsight
created: 2026-10-07
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, agent-memory, benchmarks, open-source]
readability: 3
audience_notes: >
  Engineers choosing a memory layer for an agent product who want the benchmark-forward,
  Postgres-backed entrant profiled against Mem0, Zep, and the local peers.
  Assumes you know what vector search, rerankers, and MCP are.
---

Hindsight is Vectorize's MIT-licensed agent memory system: it retains conversations as four linked memory networks (world facts, experience facts, evidence-grounded observations, and self-written knowledge pages) in Postgres, recalls them through four parallel searches, and answers questions through an agentic reflect loop.

**Its bet is that memory should learn, not just remember: raw turns become consolidated beliefs with their evidence and history kept, and the hard claims come with a live benchmark site and named independent reproducers, which is more receipts than any rival in this category publishes.**

## What it is

A server (Docker, Helm, or pip with an embedded PostgreSQL) from Vectorize, Inc., exposing retain, recall, and reflect operations over REST, Python, TypeScript, and Go SDKs, and a built-in MCP server.
Recall runs semantic, keyword (BM25), graph, and temporal searches in parallel, fuses them by rank, reranks with a cross-encoder, and cuts to a token budget instead of a top-k.
A background worker consolidates overlapping facts into observations that cite their evidence with quotes and a proof count, refine instead of overwrite, and keep their history.
Banks carry a mission, directives, and a disposition (skepticism to empathy on a 1 to 5 scale) that apply only to the reflect loop.
Knowledge pages are living documents the bank writes about itself, mountable on disk as ordinary markdown with `hindsight fs mount`.
Documented surfaces cover 18 coding-agent CLIs (Claude Code, Codex, OpenCode, Cursor, Copilot, Hermes, OpenClaw, and more), LangGraph, CrewAI, Vercel AI SDK, and apps, with an embedded in-process mode for Python and Node.

## Status

**Active and suddenly large: 47,004 stars rank it third in this category behind claude-mem and mem0, on a repository that is barely a year old.**
47,004 stars with the repository pushed 2026-10-08, created 2025-10-30, as of 2026-10-08 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=vectorize-io/hindsight&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=vectorize-io/hindsight&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=vectorize-io/hindsight&type=date&legend=top-left" />
</picture>

Latest release v0.10.2 (2026-09-29) with PyPI (hindsight-api, hindsight-client) and npm in sync at 0.10.2 as of 2026-10-07, and 176,604 trailing-month npm client downloads (2026-09-05 to 2026-10-04).
The paper (arXiv 2512.12818, December 2025, with Virginia Tech's Naren Ramakrishnan among the authors) reports 91.4 percent on LongMemEval and 89.61 on LoCoMo; the live benchmark site claims 94.6 on LongMemEval-S, 92.0 on LoCoMo, and 64.1 on BEAM-10M as of 2026-10-07, and the README says Virginia Tech's Sanghani Center and The Washington Post independently reproduced the Hindsight numbers.
The discussion footprint is thin for the size: a 4-point Show HN (December 2025), a self-posted 3-point star-milestone thread (April 2026), and a 2-point story (October 2026), so the 46k stars came through benchmark attention and ecosystem listings rather than public debate.

## Strengths

- **The receipts are the differentiator**: per-dataset runs published as downloadable artifacts, a model leaderboard for retain, recall, rerank, and embed choices, and named outside reproducers, where every rival in this category still leads with self-run tables.
- Observation consolidation addresses the failure mode most extractors have: overlapping facts merge into one belief with evidence, history, and freshness-aware stale checks instead of piling up.
- Reflect returns answers with citations restricted to IDs it actually retrieved, shaped per bank by mission, directives, and disposition, which is an auditable reasoning loop rather than a top-k dump.
- Knowledge pages project onto disk as plain markdown, so grep, editors, and file-native agents work without the SDK.

## Cautions

- **The benchmark franchise is the vendor's own**: agentmemorybenchmark.ai is operated by Vectorize, the "industry standard" framing is its own, and the named independent reproductions are assertions on the README that I could not verify at arm's length in a public run.
- Self-hosting means running Postgres plus supplying LLM keys for extraction and reranking, a heavier footprint than the SQLite-local peers, and the 0.7 through 0.10 documentation lines run in parallel, so version churn is part of the deal.
- Cloud details (rates, quotas) sit behind a client-rendered console and a billing docs page, so the pay-as-you-go economics are not inspectable without an account.
- Public scrutiny is thin: three HN threads totaling 9 points, so the benchmark lead has no independent adversarial testing I could find.

## Pricing

Self-hosted: free, MIT, no restrictions.
Hindsight Cloud: pay as you go, billed on token usage with no fixed monthly fee and no seat pricing, $5 of signup credit with GitHub sign-in, 99.9 percent uptime target, as of 2026-10-07.
Enterprise: custom, with BYO-cloud, on-premises, SSO and RBAC, and up to a 99.95 percent SLA.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-07 | Self-hosted, Cloud, Enterprise | Baseline: self-host free (MIT), Cloud pay-as-you-go on token usage ($5 signup credit, no fixed fee), Enterprise custom. | [vectorize.io/pricing](https://vectorize.io/pricing) |

## Compared to

- [mem0](../mem0/index.md): the adoption leader of the same hosted-plus-OSS kind; Mem0 has the wider integration surface, Hindsight has the published receipts and the reflection loop.
- [Zep](../zep/index.md): temporal invalidation for facts that change; Hindsight keeps observation history instead, so choose Zep for audit-grade validity windows and Hindsight for learned beliefs.
- [claude-mem](../claude-mem/index.md): session compression for one user's coding agents on local SQLite; Hindsight is a product-grade service you operate for many users.

## Bottom line

**Recommended for teams building product agents who want the benchmark-forward engine and will verify the lead on their own workload, which its own artifact exports make practical.**
Not for solo coding-agent use, where local files or claude-mem cost nothing, or for buyers who need independently audited benchmarks before signing.

## Changes

- 2026-10-07 - Created from the 2026-10-07 awesome-list entrant scan, with nine fetched sources and the vendor-operated-benchmark caveat recorded as the critical angle.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [mem0](../mem0/index.md) - the adoption leader whose benchmark claims sit on the same contested ground
- [Zep](../zep/index.md) - the temporal-graph alternative for facts that invalidate
- [claude-mem](../claude-mem/index.md) - the local session-compression alternative for single users

## References

- https://github.com/vectorize-io/hindsight - repository, MIT license, 47,004 stars, activity, as of 2026-10-08
- https://raw.githubusercontent.com/vectorize-io/hindsight/main/README.md - architecture, memory types, benchmark claims, the independent-reproduction statement, and install paths
- https://hindsight.vectorize.io/ - product documentation: retain/recall/reflect, multi-strategy retrieval, observation consolidation, knowledge pages, 18 coding-agent integrations
- https://benchmarks.hindsight.vectorize.io/ - the live benchmark site and its downloadable run artifacts (LongMemEval-S 94.6, LoCoMo 92.0, BEAM-10M 64.1), as of 2026-10-07
- https://arxiv.org/abs/2512.12818 - the paper (91.4 percent LongMemEval, 89.61 LoCoMo, December 2025) and the author list
- https://vectorize.io/pricing - the self-host/Cloud/Enterprise ladder and the pay-as-you-go terms, as of 2026-10-07
- https://pypi.org/pypi/hindsight-api/json - hindsight-api 0.10.2 (2026-09-29), the release-sync record
- https://api.npmjs.org/downloads/point/last-month/@vectorize-io/hindsight-client - 176,604 trailing-month client downloads (2026-09-05 to 2026-10-04)
- https://hn.algolia.com/api/v1/search?query=%22hindsight%22%20agent%20memory&tags=story - the thin-discussion record (4-point Show HN 2025-12-16, 3-point milestone thread 2026-04-22, 2-point story 2026-10-05)
