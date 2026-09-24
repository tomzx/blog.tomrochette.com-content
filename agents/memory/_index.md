---
showArticleList: false
title: Memory
created: 2026-09-24
visible: true
status: in progress
tags: [agents, memory]
readability: 3
---

Persistent memory for agents: the file conventions, the portable format, the capture plugins, and the hosted and self-hostable services, from graph pipelines to temporal stores.

- [claude-mem](claude-mem/index.md) - the 94k-star plugin that captures coding-agent sessions, compresses them with your tokens, and reinjects the context.
- [Cognee](cognee/index.md) - the Apache-2.0 graph-memory pipeline with the whole engine self-hostable and a flat per-token cloud.
- [Engrim](engrim/index.md) - the local-first SQLite episodic memory engine for multiple AI CLIs on one machine, provenance-first, new this week.
- [File-based agent memory](file-based-agent-memory/index.md) - the CLAUDE.md and AGENTS.md conventions, memory as plain markdown files.
- [Letta](letta/index.md) - the MemGPT creators' memory-first platform, agent plus cloud tier.
- [mem0](mem0/index.md) - the hosted and self-hostable memory layer across vector, graph, and key-value backends.
- [Memoryfields](memoryfields/index.md) - Cal Paterson's portable memory-as-file-format spec, markdown pages plus a deletable vector index, the files-over-pipelines argument in RFC form.
- [Zep](zep/index.md) - temporal knowledge graphs where contradictions invalidate old facts.

Its members are compared on shared rows in the [Memory Feature Matrix](memory-feature-matrix/index.md).

## Changes

- 2026-08-24 - Added File-based agent memory.
- 2026-08-24 - Added Letta.
- 2026-08-24 - Added mem0.
- 2026-08-24 - Added Zep.
- 2026-08-26 - Added Cognee.
- 2026-08-30 - Added claude-mem.
- 2026-09-04 - Added Memoryfields.
- 2026-09-10 - Added Engrim.
