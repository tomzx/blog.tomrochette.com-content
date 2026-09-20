---
title: Memex
created: 2026-09-20
updated: 2026-09-20
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, search, open-source]
readability: 3
audience_notes: >
  Engineers with months of accumulated coding-agent sessions who want terminal search with semantic matching and one action to resume the original session.
  Assumes you run at least one CLI coding agent and know what a session transcript is.
---

Memex is an MIT-licensed Rust CLI and TUI that indexes the session transcripts your coding agents already wrote on disk, searches them with BM25 or optional local embeddings, and resumes a selected session in the harness that produced it.
Facts below verified as of 2026-09-20.

**Search quality plus resume is the combination this category lacked: agentsview archives and counts cost, ctx retrieves for agents, and Memex answers the human question, where did I already do this, then drops you back into the original session.**

## What it is

A Rust CLI (brew, AUR, Nix, or cargo-binstall) that auto-discovers supported sources and indexes them locally, with a TUI browser, a local web UI, native macOS and Qt apps, and an MCP server so agents can search transcripts as a tool.
Its engine support table covers fifteen harnesses, including Claude Code, Codex, Cursor, OpenCode, Pi, GitHub Copilot CLI, Grok, and Antigravity, each graded separately for history, token usage, resume, saved memories, and experimental import into another tool.
Search is BM25 by default with optional local embeddings for semantic and hybrid queries; saved Claude and Codex memories are searchable alongside transcripts, and federated search queries history on other machines over SSH.
Made by an independent developer, MIT-licensed, with no cloud service in the default path.

## Status

Active and quietly growing: created 2026-01-01, 222 stars, 28 forks, pushed 2026-09-18, as of 2026-09-20.
Its Show HN on 2026-09-18 reached 2 points and a single comment, written by the author.
**The launch footprint is nearly empty, which I read as adoption through word of mouth and through agents rather than through launches, the same reading this category applied to ctx, and as thin independent verification.**

## Strengths

- Semantic and hybrid search is a genuinely distinct cell in this category: agentsview's FTS5 index and ctx's retrieval are keyword-driven, Memex embeds locally.
- Resume-in-place closes the loop the other tools leave open: finding the session and continuing it are one action in the TUI.
- The MCP server and search skill put the same index in front of agents, so the archive serves both readers of this section at once.
- Distribution is serious for its size: brew, AUR, Nix, cargo-binstall, and native desktop apps.

## Cautions

- Fifteen engines graded per capability means real unevenness: Cursor resume is CLI-only, Antigravity token counting is unsupported, and several engines have no resume at all.
- Embeddings and token tracking are off by default, so the semantic-search headline requires opt-in setup and local model downloads.
- The only community signal beyond 222 stars is an author-commented launch thread, so there is no independent verdict on reliability.
- Experimental session transfers and the announced object-storage sync are the roadmap promises most likely to churn.

## Pricing

Free and open source under MIT.
No paid tier is published; embeddings run locally on your own hardware.

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

## See also

- [agentsview](../agentsview/index.md) - the retrospective archive with the broadest engine coverage
- [ctx](../ctx/index.md) - the agent-facing retrieval and blame-attribution sibling
- [agents-observe](../agents-observe/index.md) - the live half of the category
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/nicosuave/memex - repository, description, engine support table, surfaces
- https://api.github.com/repos/nicosuave/memex - stars, forks, dates, MIT license as of 2026-09-20
- https://raw.githubusercontent.com/nicosuave/memex/main/README.md - features, engine matrix, install, MCP server, herdr plugin
- https://raw.githubusercontent.com/nicosuave/memex/main/docs/installation.md - brew, AUR, Nix, and cargo install paths
- https://hn.algolia.com/api/v1/items/49754771 - the 2-point Show HN of 2026-09-18, cited as the thin-footprint signal
