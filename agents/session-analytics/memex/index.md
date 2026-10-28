---
title: Memex
created: 2026-09-20
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, search, open-source]
readability: 3
audience_notes: >
  Engineers with months of accumulated coding-agent sessions who want terminal search with semantic matching and one action to resume the original session.
  Assumes you run at least one CLI coding agent and know what a session transcript is.
---

Memex is an MIT-licensed Rust CLI and TUI that indexes the session transcripts your coding agents already wrote on disk, searches them with BM25 or optional local embeddings, and resumes a selected session in the harness that produced it.

**Search quality plus resume is the combination this category lacked: agentsview archives and counts cost, ctx retrieves for agents, and Memex answers the human question, where did I already do this, then drops you back into the original session.**

## What it is

A Rust CLI (brew, AUR, Nix, or cargo-binstall) that auto-discovers supported sources and indexes them locally, with a TUI browser, a local web UI, native macOS and Qt apps, and an MCP server so agents can search transcripts as a tool.
Its engine support table covers eighteen harnesses, including Claude Code, Codex, Cursor, OpenCode, Pi, GitHub Copilot CLI, Grok, Hermes, Kimi Code, and KiloCode CLI, each graded separately for history, token usage, resume, saved memories, and experimental import into another tool.
Search is BM25 by default with optional embeddings for semantic and hybrid queries, local by default, with an opt-in OpenAI-compatible remote path (v0.26.0) whose docs warn that remote embeddings send transcript text and memory documents to that API; saved Claude and Codex memories are searchable alongside transcripts, and federated search queries history on other machines over SSH.
Made by an independent developer, MIT-licensed, with no cloud service in the default path.

## Status

Active and quietly growing: created 2026-01-01, 259 stars, 40 forks, pushed 2026-10-28, as of 2026-10-28.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=nicosuave/memex&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=nicosuave/memex&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=nicosuave/memex&type=date&legend=top-left" />
</picture>

Releases ship in bursts: v0.25.0 (2026-10-02) added the Hermes and KiloCode CLI engines (fifteen to seventeen harnesses), then v0.26.0, v0.26.1, and v0.27.0 all landed 2026-10-03 (OpenAI-compatible remote embeddings plus the full fastembed catalog, Homebrew tap updates, and conversation-search relevance improvements), v0.27.1 followed on 2026-10-04 without release notes, v0.27.2 and v0.28.0 landed 2026-10-12 (Homebrew as the update source for Homebrew installs, remembered phrases prioritized in search results, relevance ranking shared across the search interfaces, and OpenCode v1 session indexing when the v2 projection is empty), and v0.29.0 landed 2026-10-14 (the Kimi Code CLI engine, seventeen to eighteen harnesses, Homebrew core formula installs, multiple Claude profile support with deduplicated agent transcripts, and an Antigravity WAL-store read fix), v0.29.1 followed on 2026-10-16, and v0.30.0 landed 2026-10-20 without release notes (one change: the index refreshes before session reads, independent of the scan TTL), and v0.31.0 landed 2026-10-22, also without release notes, adding the Goose SQLite store as the nineteenth engine in the support table, and v0.31.1 followed on 2026-10-24, again without notes, with the compare view showing a fix wave (ten code-review findings across resume, search, usage, and ingest, Hermes turn overlap and Kimi incremental retry drift, client source filters and stale reader caches and Qt search ranking, and a stray .DS_Store wedging segment collection), and one more unreleased fix merged 2026-10-28 (CPU embeddings kept off CoreML and read-triggered refreshes bounded).
Its Show HN on 2026-09-18 reached 2 points and a single comment, written by the author.
**The launch footprint is nearly empty, which I read as adoption through word of mouth and through agents rather than through launches, the same reading this category applied to ctx, and as thin independent verification.**

## Strengths

- Semantic and hybrid search is a genuinely distinct cell in this category: agentsview's FTS5 index and ctx's retrieval are keyword-driven, Memex embeds locally.
- Resume-in-place closes the loop the other tools leave open: finding the session and continuing it are one action in the TUI.
- The MCP server and search skill put the same index in front of agents, so the archive serves both readers of this section at once.
- Distribution is serious for its size: brew, AUR, Nix, cargo-binstall, and native desktop apps.

## Cautions

- Eighteen engines graded per capability means unevenness by construction: Cursor resume is CLI-only, Antigravity token counting is unsupported, and several engines have no resume at all.
- Embeddings and token tracking are off by default, so the semantic-search headline requires opt-in setup, and since v0.26.0 that setup can point at a remote OpenAI-compatible API that receives transcript text, not only at local models.
- The only community signal beyond 246 stars is an author-commented launch thread, so there is no independent verdict on reliability.
- Experimental session transfers and the announced object-storage sync are the roadmap promises most likely to churn.

## Pricing

Free and open source under MIT.
No paid tier is published; embeddings run locally by default, and the remote-embedding path is opt-in.

## Compared to

- [agentsview](../agentsview/index.md): the broader archive with 60-plus formats and cost reporting; Memex covers fewer engines but adds semantic search and resume.
- [ctx](../ctx/index.md): the agent-facing retriever with blame attribution; Memex's MCP server overlaps, but its center of gravity is the human in the terminal.
- [agents-observe](../agents-observe/index.md): the live dashboard while sessions run; Memex reads only what was already written.

## Bottom line

**Recommended for terminal-first engineers with months of multi-harness session history who want semantic recall and resume without a database service.**
Not for live observability (agents-observe), cost reporting at scale (agentsview), or provenance attribution (ctx).
My disagreeable claim: resume-in-place is the feature every archive tool in this category will copy within a year, because a found session you cannot re-enter is a dead letter.

## Changes

- 2026-09-20 - Created.
- 2026-09-27 - Re-verified: repository counts refreshed (228 to 231 stars), releases, engine table, and launch thread all unchanged.
- 2026-10-03 - Recorded the v0.25.0 release (2026-10-02), which added Hermes and KiloCode CLI engine support (fifteen to seventeen harnesses) alongside index-statistics and daemon fixes; the push date moved to 2026-10-02 with star and fork counts unchanged (239 stars, 33 forks).
- 2026-10-04 - Recorded the v0.26.0, v0.26.1, and v0.27.0 releases (all 2026-10-03: opt-in OpenAI-compatible remote embeddings plus the full fastembed catalog, Homebrew tap updates, conversation-search relevance improvements), qualified the local-embeddings claims in What it is, Cautions, and Pricing accordingly, and refreshed repository counts (241 stars, pushed 2026-10-04).
- 2026-10-05 - Recorded v0.27.1 (2026-10-04, released without notes); refreshed stars to 243 and the push date to 2026-10-05.
- 2026-10-07 - Added the nicosuave/memex star history chart to the Status section.
- 2026-10-13 - Recorded the v0.27.2 and v0.28.0 releases (2026-10-12): Homebrew as the update source for brew installs, remembered phrases prioritized and relevance ranking shared across the search interfaces, and OpenCode v1 session indexing when the v2 projection is empty; repository counts refreshed (251 to 259 stars, pushed 2026-10-13).
- 2026-10-16 - Recorded v0.29.0 (2026-10-14): the Kimi Code CLI engine (seventeen to eighteen harnesses), Homebrew core formula installs, multiple Claude profile support with deduplicated agent transcripts, and an Antigravity WAL-store read fix, with v0.29.1 following 2026-10-16; the engine count moved through What it is, the caution, the matrix cell, and the reading prose, and the pushed date moved to 2026-10-16.
- 2026-10-21 - Recorded v0.30.0 (2026-10-20, released without notes): the index refreshes before session reads, independent of the scan TTL; the pushed date moved to 2026-10-20 and forks refreshed 36 to 38.
- 2026-10-23 - Recorded v0.31.0 (2026-10-22, released without notes): the Goose session database joined the engine table as the nineteenth engine, with history, token usage, and resume graded yes.
- 2026-10-25 - Recorded v0.31.1 (2026-10-24, released without notes): a fix wave over resume, search, usage, and ingest (ten code-review findings, Hermes turn overlap and Kimi incremental retry drift, Qt search ranking, and a stray .DS_Store wedging segment collection); repository counts refreshed (forks 38 to 40) and the pushed date moved to 2026-10-24.
- 2026-10-28 - Volatile re-verification: no release after v0.31.1 with one unreleased fix merged 2026-10-28 (CPU embeddings kept off CoreML and read-triggered refreshes bounded); the pushed date moved to 2026-10-28.

## See also

- [agentsview](../agentsview/index.md) - the retrospective archive with the broadest engine coverage
- [ctx](../ctx/index.md) - the agent-facing retrieval and blame-attribution sibling
- [agents-observe](../agents-observe/index.md) - the live half of the category
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/nicosuave/memex - repository, description, engine support table, surfaces
- https://api.github.com/repos/nicosuave/memex - stars, forks, dates, MIT license as of 2026-10-11
- https://raw.githubusercontent.com/nicosuave/memex/main/README.md - features, engine matrix, install, MCP server, herdr plugin, and the remote-embeddings warning that transcript text and memory documents are sent to the configured API (fetched 2026-10-04)
- https://github.com/nicosuave/memex/releases - v0.31.1 (2026-10-24, no notes), v0.31.0 (2026-10-22, no notes), and v0.30.0 (2026-10-20, no notes) as the newest tags (re-fetched 2026-10-25), after v0.29.1 (2026-10-16), v0.29.0 (2026-10-14), the v0.28.0 and v0.27.2 releases of 2026-10-12, v0.27.1 (2026-10-04, no notes published), and the v0.26.0, v0.26.1, v0.27.0 releases of 2026-10-03 and v0.25.0 (2026-10-02)
- https://raw.githubusercontent.com/nicosuave/memex/main/docs/installation.md - brew, AUR, Nix, and cargo install paths
- https://hn.algolia.com/api/v1/items/49754771 - the 2-point Show HN of 2026-09-18, cited as the thin-footprint signal
