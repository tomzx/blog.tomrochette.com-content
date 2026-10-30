---
title: Basic Memory
created: 2026-10-06
updated: 2026-10-30
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

A Python MCP server from Basic Machines (PyPI basic-memory 0.24.1, Python 3.12+), usable from any MCP client: Claude, Codex, Cursor, ChatGPT.
Notes are Obsidian-compatible markdown with observations and wikilinks that compound into a knowledge graph.
Search is semantic with optional cross-encoder reranking for hybrid and vector results.
Every tool is tagged with behavior hints (read-only, destructive, idempotent) for progressive tool discovery, so agents pick the right tool without probing.
The cloud adds cross-device sync, browser and mobile access, and a shared Teams workspace; the local server stays free and air-gapped.

## Status

**Active and mid-scale, with a thin public-discussion footprint.**
4,237 stars with the repository pushed 2026-10-20, created 2024-12-02, as of 2026-10-20 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=basicmachines-co/basic-memory&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=basicmachines-co/basic-memory&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=basicmachines-co/basic-memory&type=date&legend=top-left" />
</picture>

The registry-lag record ended: PyPI moved to 0.24.1 on 2026-10-23, in sync with the repository's tagged releases, after two months pinned at 0.23.2.
**The 1.0 line shipped as v1.0.0 on 2026-10-29, with PyPI in sync**: the MCP server's tools are replaced one for one by bm_* tools (bm_read, bm_write, bm_edit, bm_move, bm_delete, bm_search, bm_find, bm_list, bm_context, bm_project, bm_project_delete, bm_schema) with changed arguments, shared parameter types, and typed error refusals, note and search tools require an explicit project in multi-project setups, and the line adds bm doctor, a read-only self-test that reports real-project problems with the fixing command, plus a memory-doctor skill that teaches an agent to run it; the release also refuses note creates and updates whose path leaves the project.
The Hacker News record is a 4-point Show HN in March 2025 (0 comments) and a 2-point third-party story in February 2026, so the 4.1k stars came through the MCP-ecosystem channels (registry listings, Discord) rather than public debate.

## Strengths

- **Plain markdown on your disk is the canonical store**, so exit is git and the human side already has a mature editor in Obsidian.
- The agent and the human write to the same files with sync keeping them in step, which most agent-memory products only pretend to offer.
- Semantic search with optional reranking is a step past the FTS-only local stores in this category.
- Behavior-tagged tools (read-only, destructive, idempotent) cut the wasted context of agents probing what tools do.

## Cautions

- **AGPL-3.0 is the only non-permissive local license in this category**: fine to use, restrictive if you embed the server in a product.
- **The beta's locked-for-life cloud rate was retired within a day of this note's creation**: the ladder is now per-seat Team and Business tiers, which is exactly the repricing the beta language invited, so treat early rates here as non-binding.
- PyPI lags the repository by weeks, so current fixes mean installing from source.
- The knowledge graph is only as good as the agent's linking discipline, the same statistical-adherence problem the file conventions have, with a graph view added.
- Public scrutiny is thin: two threads totaling 6 points, no independent reviews found.

## Pricing

Local server: free, AGPL-3.0, all data on your disk.
Team: $15/seat/month (volume pricing $13/seat at 10 or more, $12 at 20 or more), 7-day trial, shared workspaces with roles and member management.
Business: $30/seat/month, adding SSO, audit logs, admin controls, HIPAA-compliant hosting, and priority support.
Agent Infrastructure: custom, credit-based pricing for agent fleets with on-premises options, as of 2026-10-11.
The $15/month locked-for-life beta is gone.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-06 | Cloud, Teams | Baseline: local free (AGPL-3.0), Cloud $15/mo beta locked ($12.50/mo yearly), 7-day trial, Teams same per-user price. | [basicmemory.com](https://basicmemory.com) |
| 2026-10-07 | Team, Business, Agent Infrastructure | The locked-for-life beta retired: Team $15/seat/mo (volume $13/seat at 10+, $12 at 20+), Business $30/seat/mo (SSO, audit, HIPAA hosting), Agent Infrastructure custom credits. | [basicmemory.com/pricing](https://basicmemory.com/pricing) |

## Compared to

- [Cabinet](../cabinet/index.md): both are markdown knowledge bases; Cabinet brings its own onboarded agent team and scheduler, Basic Memory is a server your existing agent talks to through MCP.
- [File-based agent memory](../file-based-agent-memory/index.md): the raw convention costs nothing and lives in the repo; Basic Memory adds the graph, semantic search, and cross-machine sync on top.
- [Memoryfields](../memoryfields/index.md): a portable format spec with minimal tooling, where Basic Memory is a working server; Memoryfields for transport between parties, Basic Memory for daily use on one disk.

## Bottom line

**Recommended for solo Claude or Codex users who want durable, Obsidian-editable agent memory without running a graph stack.**
Not for products embedding a memory engine (AGPL); teams get live shared workspaces with roles, though governance tooling (SSO, audit logs) starts at the $30 Business seat.

## Changes

- 2026-10-06 - Created from the 2026-10-06 entrant scan, with six fetched sources and the thin-discussion footprint plus the beta-pricing terms recorded as the critical angles.
- 2026-10-07 - Added the basicmachines-co/basic-memory star history chart to the Status section.
- 2026-10-07 - The cloud pricing restructured: the $15/mo locked-for-life beta retired in favor of Team $15/seat/mo with volume tiers, a new Business $30/seat/mo tier, and a custom credit-based Agent Infrastructure tier (Price history row); Teams moved from early to live with roles; the beta-repricing caution rewritten.
- 2026-10-17 - Rotation re-verification: every cited URL re-fetched live, no facts changed (the pricing page's schema.org data still lists Local $0, Team $15/seat, Business $30/seat; PyPI still 0.23.2 from 2026-08-25; the repository pushed 2026-10-16 as recorded).
- 2026-10-24 - Correction: the registry-lag record ended, PyPI moved to 0.24.1 on 2026-10-23 in sync with the repository's v0.24.1 tag, after two months pinned at 0.23.2.
- 2026-10-27 - Recorded the unreleased 1.0 line accumulating on main: the bm_* MCP tool replacement with typed refusals, explicit project arguments in multi-project setups, and the bm doctor self-test with its memory-doctor skill, published in the changelog's Unreleased section with a working migration guide and not yet in a release.
- 2026-10-30 - Recorded the v1.0.0 release (October 29, PyPI in sync): the bm_* tool line shipped as prepared, with shared parameter types and refusals for the bm_* tools and a fix refusing note writes whose path leaves the project.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [Cabinet](../cabinet/index.md) - the markdown knowledge base with its own agent team
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention this productizes with a server
- [Memoryfields](../memoryfields/index.md) - the portable-format sibling

## References

- https://github.com/basicmachines-co/basic-memory - repository, 4,132 stars, activity, AGPL-3.0, as of 2026-10-11
- https://raw.githubusercontent.com/basicmachines-co/basic-memory/main/README.md - architecture, features, the cloud pricing banner, and the Teams announcement
- https://basicmemory.com - product site and cloud offering
- https://basicmemory.com/pricing - the Team, Business, and Agent Infrastructure ladder, re-verified unchanged 2026-10-11
- https://pypi.org/pypi/basic-memory/json - basic-memory 1.0.0 (2026-10-29), in sync with the tagged releases; the two-month lag at 0.23.2 ended with 0.24.1 on 2026-10-23
- https://hn.algolia.com/api/v1/items/43374258 - the March 2025 Show HN (4 points, 0 comments)
- https://hn.algolia.com/api/v1/items/47091810 - the February 2026 third-party story (2 points), the thin-discussion record
