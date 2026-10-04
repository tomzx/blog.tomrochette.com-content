---
title: Agents queue
created: 2026-08-22
status: in progress
tags: [agents]
readability: 0
---

Work items the owner has requested, taken in order, highest first.
Every item is standing: none is ever closed, and every section keeps being built out and re-verified indefinitely.
The owner edits this file to steer the section; agents append `? for tom:` bullets and work the items, and never mark one done, strike it through, or remove it.

1. **Build the research index** (standing) - create research notes per the AGENTS.md format, one category at a time, each category seeded with the tools practitioners actually meet. Seed categories, in rough order:
   - Harnesses: Claude Code, Codex, Gemini CLI/Antigravity, OpenCode, aider, Crush, Amp, Junie.
   - Surfaces: Cursor, VS Code + Copilot, Windsurf, JetBrains/Junie, Zed.
   - Orchestration: parallel-agent dashboards and worktree managers (Conductor, dmux, Emdash, and neighbors).
   - Protocols: MCP, ACP, AGENTS.md, A2A.
   - Context engines: code search and context packing for agents.
   - Skills: skill formats, registries, and marketplaces.
   - Retrieval: RAG patterns and tooling for code and knowledge bases.
   - Memory: agent memory systems, from file-based notes to knowledge graphs and session archives.
   - Executions: scheduled and event-based agent runs (cron-style tasks, triggers, webhooks).
   - Hybrid execution: deterministic components orchestrating LLM steps for intelligence and structured outputs (tool calling, schema/JSON outputs, validation and retry loops).
   - People and publications: the people and websites shaping the domain (Karpathy, swyx/Latent Space, Willison, Yegge, Orosz/Pragmatic Engineer).

Standing work already under way (still open; keep updating and extending each indefinitely):

- **Agentic coding tools landscape** - started 2026-08-22, published as [agentic-coding-tools-landscape](agentic-coding-tools-landscape/index.md); it is the essay layer over the harness/surface/orchestration notes, so keep cross-linking new notes and re-verifying it indefinitely.
- **Model selection for coding tasks** - started 2026-08-24, published as [model-selection-for-coding-tasks](model-selection-for-coding-tasks/index.md); keep folding in new models and price moves indefinitely.
- **Context management patterns** - started 2026-08-24, published as [context-management-patterns](context-management-patterns/index.md); keep re-grounding its patterns in new harness documentation indefinitely.
- **People and publications category** - seeded 2026-08-29, with the companion [people-and-publications-feature-matrix](people-and-publications/people-and-publications-feature-matrix/index.md); keep scanning for and adding new voices and publications indefinitely, not only when prompted.

? for tom: The 2026-10-01 banned-term sweep reworded "real" section headings in the main corpus but left this section's roughly 330 "real" uses (mostly "real-world" compounds and contrastive uses like "adoption is real, stability is not") in place, and the daily verification has been treating them as the most-appropriate-term exceptions since. Should the section get the same rewording treatment, or is the corpus-only scope the intent? Rewording at this scale needs its own directed run with Changes bullets per touched note, so I have not done it inside a daily refresh.
