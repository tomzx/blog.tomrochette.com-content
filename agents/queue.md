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
   - Retrieval: RAG patterns and tooling for code and knowledge bases.
   - Memory: agent memory systems, from file-based notes to knowledge graphs and session archives.
   - Executions: scheduled and event-based agent runs (cron-style tasks, triggers, webhooks).
   - Hybrid execution: deterministic components orchestrating LLM steps for intelligence and structured outputs (tool calling, schema/JSON outputs, validation and retry loops).
   - People and publications: the people and websites shaping the domain (Karpathy, swyx/Latent Space, Willison, Yegge, Orosz/Pragmatic Engineer).

Done:

- ~~**Agentic coding tools landscape**~~ - done 2026-08-22, published as [agentic-coding-tools-landscape](agentic-coding-tools-landscape/index.md); becomes the essay layer over the harness/surface/orchestration notes, cross-link as notes appear.
- ~~**Model selection for coding tasks**~~ - done 2026-08-24, published as [model-selection-for-coding-tasks](model-selection-for-coding-tasks/index.md).
- ~~**Context management patterns**~~ - done 2026-08-24, published as [context-management-patterns](context-management-patterns/index.md).
- ~~**People and publications category**~~ - done 2026-08-29, seeded at the owner's request with five notes (Karpathy, Latent Space, Willison, Yegge, Pragmatic Engineer) plus the companion [people-and-publications-feature-matrix](people-and-publications-feature-matrix/index.md).

? for tom: the-agentic-development-environment-landscape/ exists on disk but is untracked, so linking it from agents/ would fail the CI link check; commit it (or tell me to link anyway) and I will cross-link the tracker both ways.
? for tom: two breakout community skills surfaced in this week's scan, sepia (1,444 stars in five days, research-grounded de-AI writing skill) and headcount (1,031 stars, a 16-department skills org chart for Claude Code); I rejected both for the Skills category because it is scoped to formats, registries, and marketplaces, and covered sepia's substance via the new the-tells-are-structural essay instead; want breakout community skills to get notes (a dedicated list or subcategory), or stay out of the index?
? for tom: two model gateways surfaced (experiential, 220-point HN, 820 stars; my-free-code, 620 stars), open-source OpenRouter-style control planes across providers; none of the twenty categories fits a gateway, so both are logged rejections; want a Gateways/routing category, or should these stay out?
