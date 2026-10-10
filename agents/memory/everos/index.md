---
title: EverOS
created: 2026-10-09
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, agent-memory, markdown, local-first]
readability: 3
audience_notes: >
  Engineers choosing where agent memory should live who want the markdown-canonical
  runtime entrant from EverMind profiled against the file conventions, the portable-format
  spec, and the plugin-carrying memory OS.
  Assumes you know what vector indexes are.
---

EverOS is EverMind's Apache-2.0 local-first memory runtime for agents: conversations, files, and agent trajectories are stored as editable Markdown files that remain the source of truth, with SQLite and LanceDB indexes built beside them for retrieval, and a managed cloud offered above the same stack.

**Its bet is that memory should be files you can open and edit, with the indexes as rebuildable views, and that user memory and agent memory are two different products worth separate tracks.**

## What it is

A Python library and local server (pip install everos, Python 3.12+), startable keyless for the demo and with a single OpenRouter key for the full loop; the local stack is Markdown plus SQLite plus LanceDB with no external database.
Memory is organized on two first-class tracks: user episodes and profiles, and agent cases and skills distilled from trajectories, retrieved through ids scoped by user, agent, app, project, and session.
A reflection pass merges episode clusters and refines profiles and skills between sessions, and a knowledge-wiki surface exposes editable, source-backed Markdown pages.
Ingestion is multimodal through the vendor's mRAG layer (PDFs, images, documents, URLs).
Distribution leans on harness plugins: DeepSeek Harness, Hermes, and OpenClaw carry official EverOS plugins, Dify is supported, and EverOS is built into the vendor's own Raven agent.
EverMind also sells EverOS Cloud, a managed deployment of the same engine, and publishes a research line (EverCore, with the EverMemOS and HyperMem papers) behind the architecture.

## Status

**Young, fast-moving, and vendor-led, with the section's familiar thin public footprint.**
13,371 stars and 927 forks, created 2025-10-28, pushed 2026-10-06, as of 2026-10-09 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=EverMind-AI/EverOS&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=EverMind-AI/EverOS&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=EverMind-AI/EverOS&type=date&legend=top-left" />
</picture>

Latest release v1.4.1 (2026-09-24) with PyPI in sync at 1.4.1, a 1.x line that reached 1.4 within a year of creation.
The vendor's site claims SOTA numbers (LoCoMo 93.05, LongMemEval 83.00, HaluMem 93.04) from its own reproducible benchmark harness, and the system does not appear among the published commercial leaders of the independent Agent Memory Leaderboard's first cycle (August 2026).
I found no Hacker News thread through 2026-10-09 searches, so the 13k stars rest on the vendor's channels and plugin ecosystems, the same stars-ahead-of-discussion pattern this section has flagged on Supermemory, Cabinet, and memU.

## Strengths

- **The markdown-canonical local stack works as described**: files are the store, the SQLite and LanceDB indexes are rebuildable views, and editing a file syncs back through the watcher.
- Separate user and agent tracks (episodes and profiles versus cases and skills) match how personal assistants and coding agents actually differ.
- The official plugin line covers OpenClaw, Hermes, and DeepSeek Harness from one core, the same distribution bet MemOS makes with a different storage model.
- A visible release train with PyPI in sync, against a category where several members ship through separate channels.

## Cautions

- **Every benchmark number is the vendor's own run of its own harness**, the self-published pattern this section flags on Mem0, MemOS, and Supermemory, and the one independent common-framework evaluation in the field lists no EverOS result among its published leaders.
- The README's checkmark-and-cross competitor table and the site's "SOTA" framing are marketing, not evaluation.
- The 1.4.x line is young, and the hosted cloud's pricing is unpublished: the site's pricing page returned 404 at fetch time on 2026-10-09, so the managed tier is a contact-sales path today.
- The public footprint is thin (no HN record), so failure reports and fixes skew toward the vendor's Discord and Reddit channels.
- The quick start assumes an OpenRouter key for anything beyond the demo, a soft funnel toward one provider.

## Pricing

The open-source runtime is free, Apache-2.0, self-hosted on your own infrastructure.
EverOS Cloud exists as a managed tier with no published price found as of 2026-10-09 (the pricing page returned 404 and the console sits behind sign-in), so it is an engagement, not a plan ladder.

## Compared to

- [Memoryfields](../memoryfields/index.md): both make Markdown canonical; Memoryfields is a portable format spec with minimal tooling, EverOS is a working runtime with indexes, reflection, and plugins attached.
- [MemOS](../memos/index.md): the other plugin-carrying vendor memory OS; MemOS upgrades to Neo4j and Qdrant graphs, EverOS keeps everything in local files and indexes.
- [memU](../memu/index.md): both bet on markdown the agent can read and edit; memU lets the agent curate the wiki, EverOS runs vendor-written extraction and reflection.

## Bottom line

**Recommended for OpenClaw, Hermes, or DeepSeek Harness users who want a files-first memory runtime with user and agent tracks, and who will accept a young, vendor-led dependency.**
Not for teams needing published hosted pricing, independent benchmark evidence, or a proven multi-year release history.

## Changes

- 2026-10-09 - Created from the 2026-10-09 awesome-list entrant scan, with nine fetched sources and the self-published-benchmark-plus-thin-footprint combination recorded as the critical angle.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [MemOS](../memos/index.md) - the graph-upgrading rival for the same harness-plugin audience
- [Memoryfields](../memoryfields/index.md) - the format-spec sibling of the markdown-canonical position
- [memU](../memu/index.md) - the agent-curated markdown wiki alternative
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention EverOS productizes with indexes and plugins

## References

- https://github.com/EverMind-AI/EverOS - repository, 13,371 stars, forks, activity, description, as of 2026-10-09
- https://raw.githubusercontent.com/EverMind-AI/EverOS/main/README.md - the markdown-plus-SQLite-plus-LanceDB stack, the two tracks, scoping ids, reflection, and the integration table
- https://api.github.com/repos/EverMind-AI/EverOS/license - the Apache-2.0 license file, verified through the GitHub API
- https://api.github.com/repos/EverMind-AI/EverOS/releases - the v1.4.x release train, as of 2026-10-09
- https://pypi.org/pypi/everos/json - everos 1.4.1 (2026-09-24), in sync with the GitHub tag
- https://docs.evermind.ai - the documentation root: EverOS Cloud, open-source, and API reference surfaces
- https://evermind.ai - the vendor site: SOTA claims, the EverCore research line, the product family, and the missing published pricing
- https://hn.algolia.com/api/v1/search?query=everos&tags=story - the footprint scan finding no thread (2026-10-09), the thin-discussion record
- https://agentmemoryleaderboard.ai/ - the independent academic-consortium leaderboard whose published first-cycle commercial leaders do not include this system
