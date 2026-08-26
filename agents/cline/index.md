---
title: Cline
created: 2026-08-24
updated: 2026-08-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, coding-agents, harnesses, open-source, byok]
readability: 3
audience_notes: >
  Engineers who want one open agent across their editor, terminal, and CI.
  Assumes you know what a VS Code extension is and what BYOK billing means.

---

Cline is an open-source (Apache-2.0) coding agent from Cline Bot Inc. that began as a VS Code extension and now ships a CLI, a JetBrains plugin, a web-based kanban board, and an SDK off one runtime.
Facts below verified as of 2026-08-24.

**Cline is proof that the IDE-extension generation grew up into a full harness: about 5.1 million installs on the strength of one extension, and the closest thing to a vendor-neutral default inside VS Code.**

## What it is

**One agent runtime, four delivery surfaces.**
The `cline` CLI (npm) runs interactive or fully headless with JSON output for CI.
The VS Code extension and the JetBrains plugin host the same agent in the editor, and `@cline/sdk` embeds it in your own tools.
The separate kanban app runs task cards in parallel, each in its own worktree with auto-commit and dependency chains.
Core mechanics: Plan and Act modes, per-edit terminal command approval with opt-in auto-approve, checkpoints, `.clinerules` project rules, skills, MCP servers, SDK plugins, multi-agent teams, cron-scheduled agents, and connectors for Slack, Telegram, Discord, WhatsApp, and Linear.
Any provider works: Anthropic, OpenAI, Google, OpenRouter, Bedrock, Azure, Vertex, Cerebras, Groq, Ollama, LM Studio, or any OpenAI-compatible endpoint.

## Status

**Active and large.**
The repository shows about 66.8k stars and 7.2k forks as of 2026-08-24, with 250+ contributors and an Apache-2.0 license held by Cline Bot Inc.
The VS Code Marketplace page shows 5,083,914 installs and 313 ratings averaging 4.1/5; the product site claims 8M+ installs across the marketplace and Open VSX.
The project started as the "Claude Dev" extension in late 2024 and has been renamed and corporatized since.

## Strengths

- **The default open agent inside the world's default editor**, with an install base no terminal-first rival matches.
- One runtime across IDE, CLI, CI, and SDK, so approval flows and rules stay consistent.
- Human-in-the-loop by default rather than autonomy by default.
- BYOK breadth including local models, with usage-billed inference if you want zero key setup.

## Cautions

- **The JetBrains plugin is not open-sourced**, so "open source agent" is true of the core, not of every client.
- Token consumption is the recurring community complaint; this [Ask HN thread on reducing Cline's token usage](https://news.ycombinator.com/item?id=48525711) captures the pattern.
- The 8M+ install figure is the vendor's own; the marketplace verifiable number is 5.1M.
- ClinePass means a company now sells subscriptions on top; watch where the open core stops.

## Pricing

Free and open source for individuals; you pay inference per use or bring keys.
ClinePass ($9.99/month, first month $4.99) bundles access to open-weight labs: Z.ai, Moonshot AI, DeepSeek, MiniMax, MiMo, and Qwen.
Enterprise is custom (SSO, SLA, dedicated support).

## Compared to

- [OpenCode](../opencode/index.md): terminal-first and MIT with no extension history; choose it when the terminal is the primary surface.
- [Claude Code](../claude-code/index.md): subscription platform with deeper orchestration; Cline is the open, model-neutral counterweight.
- [goose](../goose/index.md): foundation-governed generalist; Cline is the coding-specialized, IDE-native pick.

## Bottom line

**Recommended for VS Code-first engineers who want one open agent from editor to CI on their own keys.**
It is also the harness I hand non-terminal teammates first.
Not for teams that require every client binary open or a coding-agnostic automation agent.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where Cline sits in the harness layer
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - capability rows for the harness field
- [Vibe Kanban](../vibe-kanban/index.md) - the orchestration pattern Cline's kanban app bakes in
- [my-ai-workflow](../../my-ai-workflow/index.md) - rotating an open agent into daily practice

## References

- https://github.com/cline/cline - surfaces, rules, SDK, license, repository scale as of 2026-08-24
- https://cline.bot/ - product overview, install and star claims
- https://cline.bot/pricing - free core, usage billing, enterprise tiers
- https://cline.bot/cline-pass - the open-weights subscription and its labs
- https://docs.cline.bot/ - agent overview and configuration documentation
- https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev - verifiable install count and ratings
- https://news.ycombinator.com/item?id=43360564 - early community thread on Cline as an autonomous VS Code agent
- https://news.ycombinator.com/item?id=48525711 - Ask HN thread on reducing Cline's token usage
