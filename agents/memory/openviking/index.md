---
title: OpenViking
created: 2026-10-07
updated: 2026-10-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, context-database, file-based, open-source]
readability: 3
audience_notes: >
  Engineers choosing where an agent's knowledge, memory, and skills should live who want
  the filesystem-model entrant from ByteDance profiled against the graph pipelines and the
  file conventions. Assumes you know what MCP and vector search are.
---

OpenViking is Volcengine (ByteDance)'s AGPL-3.0 context database for AI agents: it stores knowledge, memory, and skills as one virtual filesystem browsable through `viking://` URIs with ordinary file operations, generated summary layers, and directory-scoped semantic search.

**Its bet is that memory should be a filesystem you can reason about: an agent lists, trees, reads, and greps its own context instead of querying a black-box embedding pool, and every directory carries a summary so it can decide what to load.**

## What it is

An open-source server under the volcengine GitHub organization, deployable self-hosted (Docker, a one-click Railway template) or as a documented enterprise private deployment, with an npm CLI (@openviking/cli), Python and Go SDKs, an MCP server for cross-session read and write, and a browser Studio demo.
Context is organized in three layers per directory: an L0 abstract, an L1 overview, and the L2 source, so agents scan cheap summaries before loading full content.
The three context types are resources (documents and code), memories (user preferences and experience), and agent skills, each addressable by `viking://` URI.
Documented agent integrations cover Claude Code, Codex, Cursor, Hermes, OpenCode, and DeepSeek Harness (Desktop support landed 2026-10-27).
The research lineage is real: the VikingMem paper (accepted at VLDB 26) defines the memory-base paradigm behind it, and a second paper's TrieHI directory-semantic index is integrated into OpenViking itself.

## Status

**Active and large, with adoption that outruns its discussion footprint even more than this category's usual pattern.**
40,037 stars with the repository pushed 2026-10-28, created 2026-01-05, as of 2026-10-28 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=volcengine/OpenViking&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=volcengine/OpenViking&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=volcengine/OpenViking&type=date&legend=top-left" />
</picture>

Latest release v0.5.2.1 (2026-10-27, a hotfix on v0.5.2 from 2026-10-23) alongside python-sdk 0.1.17 (2026-10-26, a release-pinning fix) and go sdk v0.0.5, per the GitHub releases API; the hotfix disables automatic detection of new sensitive values in sessions, which had misjudged ordinary content as private, replaced it with placeholders, and created invalid privacy records, while matching of registered privacy values and restoration of historical placeholders stay in place.
Main-branch work since the hotfix (2026-10-29 and 30, pending release) runs wide: native BM25 for openGauss, batched group-member administration (a breaking admin change), an opt-in Redis directory TTL, Studio terminal filesystem-mutation commands, session compression preserving retained previews, a Hermes recovery-lock handoff fix, and agent onboarding guides with a history import script, joining the rule service exposing `openviking_rule_search` to agents and the CodeBuddy Code CLI host adapter that were already pending, while the Rules (Beta) guides and API reference shipped in the docs (2026-10-26), DeepSeek Harness Desktop support landed (2026-10-27), and the standalone gateway can now run as a multi-replica service on Redis.
v0.5.0 adds the OpenViking Gateway (beta): a standalone proxy process on port 1935 that any model client with a configurable base URL can point at, injecting profile, memory, and skill context without plugins or prompt changes, supporting the Anthropic Messages, OpenAI Chat Completions, and OpenAI Responses protocols, and replaying injected content byte-for-byte so provider prompt caches and thinking signatures stay valid; v0.5.1 can run that gateway inside the OpenViking server itself and adds field-level privacy references, expanded batch-write options, and multimodal retrieval.
v0.5.2 turns working memory off by default (sessions still archive raw messages and extract long-term memory, but WM and checkpoint summaries now require an explicit `enable_working_memory=true`), moves the LangChain integration into a separate `langchain-openviking` package, adds session-privacy extraction with privacy-tree MCP tools, and renames the Pi extension's tools from `viking_*` to `openviking_*`.
Development and writing are both active: the 108-page documentation site and the project blog are current (the latest post, a three-minute evaluation test, dates to 2026-10-03).
The Hacker News record is a single 2-point thread from March 2026, so a 39k-star repository in nine months ran on trend cycles and ByteDance's ecosystem rather than public scrutiny.

## Strengths

- **Inspectability is built into the storage model, not bolted on**: every directory is browsable and editable with file tools, which is the most direct answer in this category to the black-box-memory critique.
- The L0/L1/L2 summary layers make context cost a first-class design decision, letting an agent scope retrieval to a subtree instead of scanning a flat index.
- One store covers knowledge, memory, and skills, so teams do not assemble a memory service, a RAG stack, and a skill registry separately.
- The academic grounding is unusually strong for a vendor repo: a VLDB-accepted memory-base paper and an integrated directory-semantic index from the same research line.

## Cautions

- **AGPL-3.0 is the restrictive license in this category's upper tier**: fine to run, viral if you embed the server in a hosted product, which is exactly what a "context database" invites.
- It is three products in one store (resources, memories, skills), so its memory behavior is one subtree of a larger system, and the product documentation describes no automated contradiction or decay pass for memory content.
- The headline retrieval gains (up to 30 percent over baselines) come from the vendor-aligned papers, and I found no independent benchmark of the product.
- Deployment outside the managed paths (self-host, Railway, enterprise contact) is on you, and the web marketing site failed to render for me this run, so the hosted story is docs-only as of 2026-10-07.

## Pricing

Pricing does not apply beyond the free open-source server (AGPL-3.0, self-hosted or via the Railway template) and an enterprise private-deployment engagement with no published price, as of 2026-10-07.

## Compared to

- [MemOS](../memos/index.md): the other graph-backed platform from a large lab; MemOS is Apache-2.0 with official harness plugins, OpenViking is AGPL with a filesystem model and stronger research receipts.
- [Memoryfields](../memoryfields/index.md): the portability bet as a spec'd format; OpenViking is a running database whose contents are file-organized but server-resident.
- [Cognee](../cognee/index.md): a pipeline you embed in applications; OpenViking is a database agents connect to and browse.

## Bottom line

**Recommended for teams that want one inspectable store for knowledge, memory, and skills, are comfortable with AGPL, and will evaluate retrieval on their own workloads with the project's own evaluation guide.**
Not for proprietary SaaS embedding, and not for buyers who need published hosted pricing or independent benchmarks today.

## Changes
- 2026-10-07 - Created from the 2026-10-07 awesome-list entrant scan, with seven fetched sources and the AGPL-plus-no-independent-benchmark combination recorded as the critical angle.
- 2026-10-10 - Recorded v0.5.0 (October 9) with the OpenViking Gateway beta (a base-URL proxy that injects memory without plugins while preserving provider prompt caches) and python-sdk 0.1.14; refreshed stars to 39,565.
- 2026-10-20 - Recorded v0.5.1 (October 19, 151 commits after v0.5.0): the gateway can now run inside the OpenViking server, with field-level privacy references, expanded batch-write options, and multimodal retrieval, and the release notes call out API deletions and storage-format changes.
- 2026-10-24 - Recorded v0.5.2 (October 23): working memory off by default (explicit `enable_working_memory=true` required), the LangChain integration split into the separate `langchain-openviking` package, session-privacy extraction with privacy-tree MCP tools, and the Pi extension's tools renamed from `viking_*` to `openviking_*`.
- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart markup: the light-theme source carried the dark-theme parameter; it now points at the default chart.
- 2026-10-26 - The main-branch train grew a rule service exposing `openviking_rule_search` to agents and a CodeBuddy Code CLI host adapter (both pending release), and python-sdk refreshed to 0.1.17.
- 2026-10-27 - Recorded the Rules (Beta) guides and API reference shipping in the docs (2026-10-26), DeepSeek Harness Desktop support landing on main (2026-10-27, added to the integration list), and the standalone gateway running as a multi-replica Redis service; the rule service and CodeBuddy adapter remain pending release.
- 2026-10-28 - Recorded the v0.5.2.1 hotfix (October 27): session privacy auto-detection disabled after it misjudged ordinary content as private and replaced it with placeholders, with registered-value matching and historical placeholder restore retained; the docs gained a RAG and memory evaluation guide and the push date refreshed to 2026-10-28.
- 2026-10-30 - Recorded the pending-release main-branch train (October 29-30): native BM25 for openGauss, breaking batched group-member administration, an opt-in Redis directory TTL, Studio terminal filesystem commands, compression preserving retained previews, a Hermes recovery-lock handoff fix, and agent onboarding guides with a history import script.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [MemOS](../memos/index.md) - the other big-lab memory platform, Apache-2.0 where this is AGPL
- [Memoryfields](../memoryfields/index.md) - the format-spec sibling of the files-over-black-box position
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention whose inspectability this productizes at service scale

## References

- https://github.com/volcengine/OpenViking - repository, AGPL-3.0, 39,625 stars, activity, as of 2026-10-11
- https://github.com/volcengine/OpenViking/releases/tag/v0.5.0 - the v0.5.0 release notes: the OpenViking Gateway beta, its three supported protocols, prompt-cache-preserving replay, and python-sdk 0.1.14
- https://github.com/volcengine/OpenViking/releases/tag/v0.5.2 - the v0.5.2 release notes: working memory defaulting off, the LangChain package split, privacy-tree MCP tools, and the Pi tool renames
- https://raw.githubusercontent.com/volcengine/OpenViking/main/README.md - the viking:// filesystem model, context types, Studio, and deployment paths
- https://docs.openviking.ai/ - the L0/L1/L2 context layers, agent integrations, CLI, and the 108-page documentation map
- https://blog.openviking.ai/ - the active project blog, latest post 2026-10-03
- https://arxiv.org/abs/2605.29640 - VikingMem (VLDB 26): the memory-base paradigm, temporal weighting, and the 30-percent retrieval claim
- https://arxiv.org/abs/2606.16903 - the directory-semantic query and maintenance paper whose TrieHI index is integrated into OpenViking
- https://hn.algolia.com/api/v1/items/47365646 - the single HN thread (2 points, 2026-03-13), the thin-discussion record
