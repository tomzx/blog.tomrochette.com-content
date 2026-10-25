---
title: TencentDB Agent Memory
created: 2026-10-11
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, agent-memory, session-memory, openclaw, hermes, open-source]
readability: 3
audience_notes: >
  Engineers running OpenClaw or Hermes agents who want token-aware memory capture with an
  inspectable trail, profiled against the plugin-carriers and the keyless session server.
  Assumes you know what an agent harness plugin is.
---

TencentDB Agent Memory is Tencent's MIT-licensed memory plugin for OpenClaw and Hermes agents: short-term tool logs compress into drill-down Mermaid canvases while long-term memory layers into a persona pyramid over local SQLite, with a Tencent Cloud vector backend strictly optional.

**Its bet is that compression must stay reversible: every summary keeps a deterministic node_id path back to the raw log, so tokens are saved without losing the evidence trail.**

## What it is

An npm plugin (@tencentdb-agent-memory/memory-tencentdb 1.0.3, Node 22+) installed into OpenClaw with one command and zero config, or into Hermes as a Docker image or a wired provider with a local gateway on port 8420.
Short-term memory offloads full tool outputs to refs/*.md files and condenses task state into a Mermaid canvas the agent reads back via node_id when a detail matters.
Long-term memory layers L0 conversation, L1 atomic facts, L2 scenarios, and L3 persona as readable Markdown under ~/.openclaw/memory-tdai, with BM25 plus vector plus RRF hybrid recall over SQLite and sqlite-vec by default.
Defaults run keyless locally against your own model key; the Hermes Docker image defaults to Tencent Cloud's LKE endpoint with DeepSeek-V3.2.
Published by Tencent (the repository moved from the Tencent org to TencentCloud), with a 24-hour issue-response pledge and a public roadmap.

## Status

**Large and fast-rising, with a license detector footnote.**
29,264 stars and 2,852 forks, created 2026-04-07, pushed 2026-10-19, as of 2026-10-20 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=TencentCloud/TencentDB-Agent-Memory&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=TencentCloud/TencentDB-Agent-Memory&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=TencentCloud/TencentDB-Agent-Memory&type=date&legend=top-left" />
</picture>

The LICENSE wraps standard MIT terms in a Tencent notice, which is why GitHub's detector marks it unclassifiable; the 2026-10-07 entrant rejection (missing license) reversed once the file was read this run.
The Hacker News footprint is one 2-point thread (August 2026), so a 29.3k-star rise in six months ran on Trendshift placement and awesome-list channels, the category's familiar stars-ahead-of-discussion pattern at Tencent scale.

## Strengths

- **The drill-down chain is the differentiator**: persona to scenario to atom to raw conversation stays inspectable in plain files, the most direct answer in this category to the black-box-memory critique short of the file convention itself.
- Symbolic short-term memory (offload plus Mermaid canvas plus node_id recall) attacks the actual token bill, and the vendor publishes per-benchmark token deltas alongside accuracy.
- The local default (SQLite plus sqlite-vec, your own key) is genuinely zero-config, and the cloud vector database stays optional.
- Corporate maintenance cadence with a public roadmap (portable memory, skill generation, an observability dashboard next).

## Cautions

- **Every benchmark number is the vendor's own run of its own plugin**: the SWE-bench, WideSearch, and PersonaMem gains come from Tencent's continuous-session setup, with no independent replication.
- The stack funnels toward Tencent services: the Hermes image defaults to Tencent's LKE endpoint and the cloud backend is Tencent's, a data-residency question outside its jurisdiction.
- The short-term compression path requires applying a runtime patch script to the OpenClaw installation, a moving target against a fast-moving harness.
- GitHub cannot classify the license, so automated compliance tooling may flag a repository whose terms are actually MIT.

## Pricing

Free and open under the Tencent MIT license; the local backend needs only your own model key.
The optional Tencent Cloud Vector Database backend bills under Tencent Cloud's own pricing, not published in the fetched surfaces, as of 2026-10-11.

## Compared to

- [MemOS](../memos/index.md): the other big-org plugin carrier; MemOS is Apache-2.0 with a hosted graph platform, this is MIT and file-first with a local default.
- [agentmemory](../agentmemory/index.md): the keyless session-memory server; both capture and compress over local stores, and this adds the persona pyramid and the reversible-compression chain.
- [claude-mem](../claude-mem/index.md): the capture-and-compress adoption leader, bound to coding-agent hooks where this covers the OpenClaw and Hermes family.

## Bottom line

Recommended for OpenClaw or Hermes users who want token-aware capture with an inspectable trail and will rerun the vendor benchmarks on their own sessions.
Not for teams needing a license file standard tooling recognizes, independence from Tencent's cloud gravity, or OpenClaw installs that cannot take a patch script.
My disagreeable claim: reversible compression, not recall quality, is the feature that will decide this category's winners, and this is the first member to build its whole architecture around it.

## Changes

- 2026-10-11 - Created after the 2026-10-07 rejection's missing-license trigger fired (the repository now carries MIT terms under a Tencent notice), with six fetched sources and the self-run-benchmark-plus-Tencent-funnel profile recorded as the critical angle.
- 2026-10-16 - Recorded the v2.0.3-beta.1 pre-release (October 13: a pluggable decision service, on-demand skill selection, and session trajectory recording, all default-off with unchanged behavior on old configs); refreshed stars to 29,264.
- 2026-10-25 - Rotation re-verification: every cited URL re-fetched live, no facts changed (no release since the v2.0.3-beta.1 pre-release, the npm plugin still at 1.0.3, and the October 19-21 default-branch pushes are panel UI fixes and a README translation).

- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [MemOS](../memos/index.md) - the other big-org harness-plugin memory platform
- [agentmemory](../agentmemory/index.md) - the keyless cross-harness session server
- [claude-mem](../claude-mem/index.md) - the capture-and-compress leader this challenges on token economics

## References

- https://github.com/TencentCloud/TencentDB-Agent-Memory - repository, 27,909 stars, 2,713 forks, created 2026-04-07, pushed 2026-10-10, verified through the GitHub API as of 2026-10-11 (the Tencent/TencentDB-Agent-Memory URL redirects here)
- https://raw.githubusercontent.com/TencentCloud/TencentDB-Agent-Memory/main/README.md - the layering and symbolization architecture, the benchmark table, defaults, install paths, and the roadmap
- https://raw.githubusercontent.com/TencentCloud/TencentDB-Agent-Memory/main/LICENSE - the MIT terms under Tencent's own notice, the reason the GitHub detector returns no SPDX id
- https://registry.npmjs.org/@tencentdb-agent-memory/memory-tencentdb - the plugin package at 1.0.3 (2026-09-22)
- https://hn.algolia.com/api/v1/search?query=tencentdb%20agent%20memory&tags=story - the thin-discussion record (one 2-point thread, 2026-08-05)
- https://github.com/TeleAI-UAGI/Awesome-Agent-Memory - the entrant source that surfaced it, as of 2026-10-11
