---
title: Basic Memory
created: 2026-10-06
updated: 2026-11-13
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

A Python MCP server from Basic Machines (PyPI basic-memory 1.0.0, Python 3.12+), usable from any MCP client: Claude, Codex, Cursor, ChatGPT, with a Hermes Agent memory-provider plugin in the repository's integrations directory.
Notes are Obsidian-compatible markdown with observations and wikilinks that compound into a knowledge graph.
Search is semantic with optional cross-encoder reranking for hybrid and vector results.
Every tool is tagged with behavior hints (read-only, destructive, idempotent) for progressive tool discovery, so agents pick the right tool without probing.
The cloud adds cross-device sync, browser and mobile access, and shared workspaces; the local server stays free and air-gapped.

## Status

**Active and mid-scale, with a thin public-discussion footprint.**
4,237 stars with the repository pushed 2026-11-13, created 2024-12-02, as of 2026-11-13 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=basicmachines-co/basic-memory&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=basicmachines-co/basic-memory&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=basicmachines-co/basic-memory&type=date&legend=top-left" />
</picture>

The registry-lag record ended: PyPI moved to 0.24.1 on 2026-10-23, in sync with the repository's tagged releases, after two months pinned at 0.23.2.
**The 1.0 line shipped as v1.0.0 on 2026-10-29, with PyPI in sync**: the MCP server's tools are replaced one for one by bm_* tools (bm_read, bm_write, bm_edit, bm_move, bm_delete, bm_search, bm_find, bm_list, bm_context, bm_project, bm_project_delete, bm_schema) with changed arguments, shared parameter types, and typed error refusals, note and search tools require an explicit project in multi-project setups, and the line adds bm doctor, a read-only self-test that reports real-project problems with the fixing command, plus a memory-doctor skill that teaches an agent to run it; the release also refuses note creates and updates whose path leaves the project.
The Hacker News record is a 4-point Show HN in March 2025 (0 comments) and a 2-point third-party story in February 2026, so the 4.1k stars came through the MCP-ecosystem channels (registry listings, Discord) rather than public debate.
The post-1.0 fix train (2026-11-01 and 02) speeds the file-conflict check with two indexed columns (one query instead of a per-project scan on every write), stops a folder named like the project from colliding with its root note's permalink, refuses note moves onto paths equivalent to another note (case and Unicode twins), and conforms the Hermes Agent memory-provider plugin to Hermes v0.22's provider contract (inline capture on Hermes's worker thread, per-profile provider instances, and a new transcript note per session switch linked by a continues relation).
The November 4 fixes (pending release) start watching a newly added project right away and embed a caught-up project in the background instead of the watcher loop, rank Postgres prefix queries by the words typed with title scoring, stop recording a note's created_at after its updated_at, write CLI output as UTF-8 on Windows, and let the searching server own the similar-notes floor.
The November 5-to-7 train (pending release) is performance and fixes: note-resolve answers cached, vector search rows ranked in the database with search-byte counting, each path checked once per storage-event batch, the exact count dropped from search, hybrid legs run concurrently, non-numeric values dropped from numeric metadata filters, frontmatter btree indexes that reject long values removed, semantic search freshness reported to Cloud, local and cloud projects listed together when a project is unknown, and note formatting with format_on_save removed (breaking); PyPI stays at 1.0.0.
The November 11 train (pending release) restructures the MCP surface again: bm_schema and bm_project each split into one tool per operation and the `memory://ai_assistant_guide` resource dropped (all three breaking), bm_move now carries the destructive hint, bm_write's similar-notes probe made informational so a failed probe never fails the write, a memory-start skill added for a new user's first session, and the ChatGPT plugin rebuilt from checked-in configuration with permalink and search-boundary fixes beside it; PyPI stays at 1.0.0.
The November 12-to-13 train (still pending) keeps the fix cadence: cloud discovery connects shortened with fixed timeout messages, tool errors given structured content that fits the output schema, cloud-sync project names matched in any spelling, the Hermes integration running the bm and uv that PATH names and no longer orphaning a restarted bm mcp at shutdown, SessionStart hook environments compiled with a 45-second budget, the asyncpg import dropped from SQLite startup, and the ChatGPT upload built in portable format; PyPI stays at 1.0.0.

## Strengths

- **Plain markdown on your disk is the canonical store**, so exit is git and the human side already has a mature editor in Obsidian.
- The agent and the human write to the same files with sync keeping them in step, which most agent-memory products only pretend to offer.
- Semantic search with optional reranking is a step past the FTS-only local stores in this category.
- Behavior-tagged tools (read-only, destructive, idempotent) cut the wasted context of agents probing what tools do.

## Cautions

- **AGPL-3.0 is the only non-permissive local license in this category**: fine to use, restrictive if you embed the server in a product.
- **The beta's locked-for-life cloud rate was retired within a day of this note's creation, and the per-seat ladder that replaced it lasted five weeks before the workspace-credit restructure of November 8**, which is exactly the repricing the beta language invited, so treat early rates here as non-binding.
- PyPI lags the repository by weeks, so current fixes mean installing from source.
- The knowledge graph is only as good as the agent's linking discipline, the same statistical-adherence problem the file conventions have, with a graph view added.
- Public scrutiny is thin: two threads totaling 6 points, no independent reviews found.

## Pricing

Local server: free, AGPL-3.0, all data on your disk.
Cloud: $19/month per workspace (2 members, 1,900 usage credits included, 7-day trial), as of 2026-11-08.
Pro: $99/month (5 members, 9,900 credits, scoped API keys).
Business: $249/month (25 members, 24,900 credits, audit logs, granular permissions), with SSO and HIPAA BAA as paid add-ons.
Usage credits cost $0.01 each and pay for your model calls, the web app, and Basic Memory's agents; members cost nothing extra up to the plan's limit.
The per-seat Team and Business ladder is gone.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-06 | Cloud, Teams | Baseline: local free (AGPL-3.0), Cloud $15/mo beta locked ($12.50/mo yearly), 7-day trial, Teams same per-user price. | [basicmemory.com](https://basicmemory.com) |
| 2026-10-07 | Team, Business, Agent Infrastructure | The locked-for-life beta retired: Team $15/seat/mo (volume $13/seat at 10+, $12 at 20+), Business $30/seat/mo (SSO, audit, HIPAA hosting), Agent Infrastructure custom credits. | [basicmemory.com/pricing](https://basicmemory.com/pricing) |
| 2026-11-08 | Cloud, Pro, Business | The per-seat ladder replaced: Cloud $19/mo per workspace (2 members, 1,900 credits), Pro $99/mo (5 members, 9,900 credits, scoped API keys), Business $249/mo (25 members, 24,900 credits, audit logs, granular permissions), usage credits at $0.01 each, SSO and BAA now paid add-ons. | [basicmemory.com/pricing](https://basicmemory.com/pricing) |

## Compared to

- [Cabinet](../cabinet/index.md): both are markdown knowledge bases; Cabinet brings its own onboarded agent team and scheduler, Basic Memory is a server your existing agent talks to through MCP.
- [File-based agent memory](../file-based-agent-memory/index.md): the raw convention costs nothing and lives in the repo; Basic Memory adds the graph, semantic search, and cross-machine sync on top.
- [Memoryfields](../memoryfields/index.md): a portable format spec with minimal tooling, where Basic Memory is a working server; Memoryfields for transport between parties, Basic Memory for daily use on one disk.

## Bottom line

**Recommended for solo Claude or Codex users who want durable, Obsidian-editable agent memory without running a graph stack.**
Not for products embedding a memory engine (AGPL); teams get live shared workspaces with roles, though governance tooling (audit logs, granular permissions, and the SSO and BAA add-ons) starts at the $249 Business plan.

## Changes

- 2026-10-06 - Created from the 2026-10-06 entrant scan, with six fetched sources and the thin-discussion footprint plus the beta-pricing terms recorded as the critical angles.
- 2026-10-07 - Added the basicmachines-co/basic-memory star history chart to the Status section.
- 2026-10-07 - The cloud pricing restructured: the $15/mo locked-for-life beta retired in favor of Team $15/seat/mo with volume tiers, a new Business $30/seat/mo tier, and a custom credit-based Agent Infrastructure tier (Price history row); Teams moved from early to live with roles; the beta-repricing caution rewritten.
- 2026-10-17 - Rotation re-verification: every cited URL re-fetched live, no facts changed (the pricing page's schema.org data still lists Local $0, Team $15/seat, Business $30/seat; PyPI still 0.23.2 from 2026-08-25; the repository pushed 2026-10-16 as recorded).
- 2026-10-24 - Correction: the registry-lag record ended, PyPI moved to 0.24.1 on 2026-10-23 in sync with the repository's v0.24.1 tag, after two months pinned at 0.23.2.
- 2026-10-27 - Recorded the unreleased 1.0 line accumulating on main: the bm_* MCP tool replacement with typed refusals, explicit project arguments in multi-project setups, and the bm doctor self-test with its memory-doctor skill, published in the changelog's Unreleased section with a working migration guide and not yet in a release.
- 2026-10-30 - Recorded the v1.0.0 release (October 29, PyPI in sync): the bm_* tool line shipped as prepared, with shared parameter types and refusals for the bm_* tools and a fix refusing note writes whose path leaves the project.
- 2026-11-03 - Recorded the post-1.0 fix train (November 1 and 2): indexed file-conflict lookups, the folder-named-like-the-project permalink fix, note-move rejections on equivalent paths, and the Hermes plugin conformed to Hermes v0.22's provider contract (inline ordered capture, per-profile providers, session-switch notes); the PyPI figure in the opening moved to 1.0.0 and the push date refreshed to 2026-11-02.
- 2026-11-04 - Recorded the pending November 4 fixes: newly added projects watched immediately with caught-up projects embedded in the background, Postgres prefix queries ranked by the words typed, created_at no longer recorded after updated_at, UTF-8 CLI output on Windows, and the searching server owning the similar-notes floor; the push date refreshed to 2026-11-04.
- 2026-11-08 - Recorded the pricing restructure (November 8): the per-seat Team and Business ladder replaced by Cloud $19/mo per workspace (2 members, 1,900 credits), Pro $99/mo (5 members, 9,900 credits, scoped API keys), and Business $249/mo (25 members, 24,900 credits) with metered $0.01 credits and SSO/BAA as paid add-ons (Price history row); recorded the November 5-to-7 pending performance train with its breaking removal of note formatting and format_on_save, PyPI still at 1.0.0; the push date refreshed to 2026-11-07.
- 2026-11-11 - Recorded the pending November 11 MCP restructure (bm_schema and bm_project split into one tool per operation, the ai_assistant_guide resource dropped, bm_move marked destructive, bm_write's probe made informational, a memory-start skill, and ChatGPT plugin packaging fixes), PyPI still at 1.0.0; corrected the Bottom line's governance-starts-at figure to the $249 Business plan, which the November 8 restructure had left stale at the retired $30 seat; the push date refreshed to 2026-11-11.
- 2026-11-13 - Volatile re-verification: the pending November 12-to-13 train recorded (Hermes PATH and shutdown fixes, structured MCP tool errors, cloud-sync project-name case matching, the asyncpg startup-import removal, the portable-format ChatGPT upload, and the setup man page), PyPI still at 1.0.0, and the push date refreshed to 2026-11-13.

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
