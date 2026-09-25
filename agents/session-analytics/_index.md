---
showArticleList: false
title: Session analytics
created: 2026-09-24
visible: true
status: in progress
tags: [agents, session-analytics]
readability: 3
---

Tools that turn what coding agents already record into searchable history, cost reports, and audits, plus one that watches the sessions as they happen.

- [agents-observe](agents-observe/index.md) - the live dashboard for Claude Code and Codex sessions, hooks feeding a local server, multi-agent trees and cost breakdowns in real time.
- [agentsview](agentsview/index.md) - the local-first indexer for roughly 60 agents' session files, retrospective search and token-cost reporting in one SQLite store.
- [ctx](ctx/index.md) - local search over the sessions agents already recorded, with blame attribution from any line of code back to its transcript.
- [Memex](memex/index.md) - the Rust CLI that indexes multi-harness session transcripts locally with BM25 or embeddings and resumes the session you find.

Its members are compared on shared rows in the [Session Analytics Feature Matrix](session-analytics-feature-matrix/index.md).

## Changes

- 2026-08-30 - Added agentsview.
- 2026-09-05 - Added ctx.
- 2026-09-16 - Added agents-observe.
- 2026-09-20 - Added Memex.
