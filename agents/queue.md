---
title: Agents queue
created: 2026-08-22
status: in progress
tags: [agents]
readability: 0
---

Work items the owner has requested, taken in order, highest first.
The owner edits this file to steer the section; agents append `? for tom:` bullets and mark items done, nothing else.

1. **Build the research index** (standing) - create research notes per the AGENTS.md format, one category at a time, each category seeded with the tools practitioners actually meet. Seed categories, in rough order:
   - Harnesses: Claude Code, Codex, Gemini CLI/Antigravity, OpenCode, aider, Crush, Amp, Junie.
   - Surfaces: Cursor, VS Code + Copilot, Windsurf, JetBrains/Junie, Zed.
   - Orchestration: parallel-agent dashboards and worktree managers (Conductor, dmux, Emdash, and neighbors).
   - Protocols: MCP, ACP, AGENTS.md, A2A.
   - Context engines: code search and context packing for agents.
   - Skills: skill formats, registries, and marketplaces.
2. **Model selection for coding tasks** - a maintained, opinionated guide to choosing models for coding, review, and agentic work; write it once the harness notes exist so it can cite them.
3. **Context management patterns** - practical patterns for fitting large codebases and long tasks into context windows (chunking, retrieval, summarization, compaction), grounded in current tool behavior; write it once the context engine notes exist.

Done:

- ~~**Agentic coding tools landscape**~~ - done 2026-08-22, published as [agentic-coding-tools-landscape](agentic-coding-tools-landscape/index.md); becomes the essay layer over the harness/surface/orchestration notes, cross-link as notes appear.

? for tom: the-agentic-development-environment-landscape/ exists on disk but is untracked, so linking it from agents/ would fail the CI link check; commit it (or tell me to link anyway) and I will cross-link the tracker both ways.
