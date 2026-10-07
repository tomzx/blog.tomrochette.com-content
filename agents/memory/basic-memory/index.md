---
title: Basic Memory
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, mcp, knowledge-base, markdown]
readability: 3
audience_notes: >
  Engineers using Claude, Codex, or Cursor who want their agent's knowledge to persist as
  markdown files they can also open and edit themselves.
  Assumes you know what an MCP server is.
---

Basic Memory is an AGPL-3.0 local-first knowledge base for AI agents: a Python MCP server that reads and writes markdown notes on your disk, links them into a knowledge graph through observations and wikilinks, and layers semantic search on top, with an optional paid cloud.

**Its bet is that the files remain the source of truth and everything else, the graph, the search, the sync, is a view over them, so the human and the agent edit the same notes.**

## What it is

A Python MCP server from Basic Machines (PyPI basic-memory 0.23.2, Python 3.12+), usable from any MCP client: Claude, Codex, Cursor, ChatGPT.
Notes are Obsidian-compatible markdown with observations and wikilinks that compound into a knowledge graph.
Search is semantic with optional cross-encoder reranking for hybrid and vector results.
Every tool is tagged with behavior hints (read-only, destructive, idempotent) for progressive tool discovery, so agents pick the right tool without probing.
The cloud adds cross-device sync, browser and mobile access, and a shared Teams workspace; the local server stays free and air-gapped.

## Status

**Active and mid-scale, with a thin public-discussion footprint.**
4,104 stars with the repository pushed 2026-10-06, created 2024-12-02, as of 2026-10-06 (GitHub API).

<a href="https://www.star-history.com/?repos=basicmachines-co%2Fbasic-memory&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=basicmachines-co/basic-memory&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=basicmachines-co/basic-memory&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=basicmachines-co/basic-memory&type=date&legend=top-left" />
 </picture>
</a>

The PyPI release (0.23.2) dates to 2026-08-25, so the registry lags the active repository.
The Hacker News record is a 4-point Show HN in March 2025 (0 comments) and a 2-point third-party story in February 2026, so the 4.1k stars came through the MCP-ecosystem channels (registry listings, Discord) rather than public debate.

## Strengths

- **Plain markdown on your disk is the canonical store**, so exit is git and the human side already has a mature editor in Obsidian.
- The agent and the human write to the same files with sync keeping them in step, which most agent-memory products only pretend to offer.
- Semantic search with optional reranking is a step past the FTS-only local stores in this category.
- Behavior-tagged tools (read-only, destructive, idempotent) cut the wasted context of agents probing what tools do.

## Cautions

- **AGPL-3.0 is the only non-permissive local license in this category**: fine to use, restrictive if you embed the server in a product.
- The $15/month cloud rate is a "locked for life" beta offer, a sign-up-now deal that invites later repricing for anyone joining after the beta.
- PyPI lags the repository by weeks, so current fixes mean installing from source.
- The knowledge graph is only as good as the agent's linking discipline, the same statistical-adherence problem the file conventions have, with a graph view added.
- Public scrutiny is thin: two threads totaling 6 points, no independent reviews found.

## Pricing

Local server: free, AGPL-3.0, all data on your disk.
Cloud: $15/month (beta rate locked for life; $12.50/month billed yearly), 7-day free trial; Teams at the same per-user price with a shared workspace.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-06 | Cloud, Teams | Baseline: local free (AGPL-3.0), Cloud $15/mo beta locked ($12.50/mo yearly), 7-day trial, Teams same per-user price. | [basicmemory.com](https://basicmemory.com) |

## Compared to

- [Cabinet](../cabinet/index.md): both are markdown knowledge bases; Cabinet brings its own onboarded agent team and scheduler, Basic Memory is a server your existing agent talks to through MCP.
- [File-based agent memory](../file-based-agent-memory/index.md): the raw convention costs nothing and lives in the repo; Basic Memory adds the graph, semantic search, and cross-machine sync on top.
- [Memoryfields](../memoryfields/index.md): a portable format spec with minimal tooling, where Basic Memory is a working server; Memoryfields for transport between parties, Basic Memory for daily use on one disk.

## Bottom line

**Recommended for solo Claude or Codex users who want durable, Obsidian-editable agent memory without running a graph stack.**
Not for products embedding a memory engine (AGPL), or teams needing multi-user governance today (Teams is early and thin).

## Changes

- 2026-10-06 - Created from the 2026-10-06 entrant scan, with six fetched sources and the thin-discussion footprint plus the beta-pricing terms recorded as the critical angles.
- 2026-10-07 - Added the basicmachines-co/basic-memory star history chart to the Status section.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [Cabinet](../cabinet/index.md) - the markdown knowledge base with its own agent team
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention this productizes with a server
- [Memoryfields](../memoryfields/index.md) - the portable-format sibling

## References

- https://github.com/basicmachines-co/basic-memory - repository, 4,104 stars, activity, AGPL-3.0, as of 2026-10-06
- https://raw.githubusercontent.com/basicmachines-co/basic-memory/main/README.md - architecture, features, the cloud pricing banner, and the Teams announcement
- https://basicmemory.com - product site and cloud offering
- https://pypi.org/pypi/basic-memory/json - basic-memory 0.23.2 (2026-08-25), the registry lag record
- https://hn.algolia.com/api/v1/items/43374258 - the March 2025 Show HN (4 points, 0 comments)
- https://hn.algolia.com/api/v1/items/47091810 - the February 2026 third-party story (2 points), the thin-discussion record
