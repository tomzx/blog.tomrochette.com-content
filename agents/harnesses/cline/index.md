---
title: Cline
created: 2026-08-24
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, coding-agents, harnesses, open-source, byok]
readability: 3
audience_notes: >
  Engineers who want one open agent across their editor, terminal, and CI.
  Assumes you know what a VS Code extension is and what BYOK billing means.

---

Cline is an open-source (Apache-2.0) coding agent from Cline Bot Inc. that began as a VS Code extension and now ships a CLI, a JetBrains plugin, a web-based kanban board, and an SDK off one runtime.

**Cline is proof that the IDE-extension generation grew up into a full harness: about 5.7 million installs on the strength of one extension, and the closest thing to a vendor-neutral default inside VS Code.**

## What it is

**One agent runtime, five delivery surfaces.**
The `cline` CLI (npm) runs interactive or fully headless with JSON output for CI.
The VS Code extension and the JetBrains plugin host the same agent in the editor, `@cline/sdk` embeds it in your own tools, and a native Cline Desktop app (macOS, Windows, Linux) runs it with no editor at all.
The separate kanban app runs task cards in parallel, each in its own worktree with auto-commit and dependency chains.
Core mechanics: Plan and Act modes, per-edit terminal command approval with opt-in auto-approve, checkpoints, `.clinerules` project rules, skills, MCP servers, SDK plugins, multi-agent teams, cron-scheduled agents, and connectors for Slack, Telegram, Discord, WhatsApp, and Linear.
Any provider works: Anthropic, OpenAI, Google, OpenRouter, Bedrock, Azure, Vertex, Cerebras, Groq, Ollama, LM Studio, or any OpenAI-compatible endpoint.

## Status

**Active and large.**
The repository shows about 70.3k stars and 7.7k forks as of 2026-10-15, with 250+ contributors and an Apache-2.0 license held by Cline Bot Inc.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=cline/cline&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=cline/cline&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=cline/cline&type=date&legend=top-left" />
</picture>

The VS Code Marketplace page shows 5,736,752 installs as of 2026-10-26 and a 4.1/5 average rating as of 2026-09-22; the product site claims 11M+ installs across the marketplace and Open VSX.
The project started as the "Claude Dev" extension in late 2024 and has been renamed and corporatized since.
v4.1.25 (October 16, 2026) began rolling out Cline Cloud sessions: a task runs in a hosted sandbox on a GitHub repo and branch you pick, shows up in Recent and History with its status, notifies you when it finishes, and keeps running after you close your editor ([release notes](https://github.com/cline/cline/releases), rolling out gradually).
v4.1.26 (October 26, 2026) deepened the cloud side with a Local/Cloud model toggle for new cloud tasks (the hosted model saved separately from local ones) and a progress card for sandbox starts, and refreshed the provider catalog: ClinePass now defaults to Kimi K3.1 Pro, the free list swaps in Reflection Beam, Nemotron 3.5 Lightning, and Laguna S 2.1, and GPT-6 models get `max_completion_tokens` on OpenAI-compatible endpoints while Gemini free-tier keys stop failing on native Google Search; the component tags moved the same day (cli-v3.0.74, desktop-v0.0.49, and sdk v0.2.0).
Beyond the open harness, the vendor now sells Cline Spec Driven, an enterprise agent platform built with LG CNS that runs a specialized-agent pipeline over a licensed, self-hostable deployment, listed on the product site as of 2026-10-06.

## Strengths

- **The default open agent inside the world's default editor**, with an install base no terminal-first rival matches.
- One runtime across IDE, CLI, CI, and SDK, so approval flows and rules stay consistent.
- Human-in-the-loop by default rather than autonomy by default.
- BYOK breadth including local models, with usage-billed inference if you want zero key setup.

## Cautions

- **The JetBrains plugin is not open-sourced**, so "open source agent" is true of the core, not of every client.
- Token consumption is the recurring community complaint; this [Ask HN thread on reducing Cline's token usage](https://news.ycombinator.com/item?id=48525711) captures the pattern.
- The 11M+ install figure is the vendor's own; the marketplace verifiable number is 5.7M.
- ClinePass means a company now sells subscriptions on top; watch where the open core stops.

## Pricing

Free and open source for individuals; you pay inference per use or bring keys.
ClinePass is $9.99/month flat (the docs now describe it that way, offering 2-5x the standard-API usage on popular open coding models; the promotional-rate wording that marked earlier reads has retired from the docs), bundling access to open-weight labs: Z.ai, Moonshot AI, DeepSeek, MiniMax, MiMo, and Qwen.
Enterprise is custom (SSO, SLA, dedicated support).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09 | ClinePass | Baseline: core free and open source; ClinePass $9.99/mo at a promotional rate bundling open-weight labs (Z.ai, Moonshot AI, DeepSeek, MiniMax, MiMo, Qwen); Enterprise custom. | [cline.bot/pricing](https://cline.bot/pricing) |
| 2026-10-18 | ClinePass | The docs now describe the subscription as a flat $9.99/month offering 2-5x standard-API usage on popular open coding models; the promotional-rate wording retired, the $9.99 headline unchanged. | [docs.cline.bot](https://docs.cline.bot/) |

## Compared to

- [OpenCode](../opencode/index.md): terminal-first and MIT with no extension history; choose it when the terminal is the primary surface.
- [Claude Code](../claude-code/index.md): subscription platform with deeper orchestration; Cline is the open, model-neutral counterweight.
- [goose](../goose/index.md): foundation-governed generalist; Cline is the coding-specialized, IDE-native pick.

## Bottom line

**Recommended for VS Code-first engineers who want one open agent from editor to CI on their own keys.**
It is also the harness I hand non-terminal teammates first.
Not for teams that require every client binary open or a coding-agnostic automation agent.

## Changes

- 2026-08-24 - Created in a new-entrant scan that added three harness notes, recording ClinePass and the closed-source JetBrains plugin.
- 2026-08-26 - Linked the Ask HN token-usage thread inline and in references, and added a first-person Bottom line.
- 2026-09-08 - Revised ClinePass wording to "promotional rate" after the $4.99 first-month promo left the page.
- 2026-09-10 - Dropped the unverifiable ratings count from the marketplace figures.
- 2026-09-16 - Refreshed marketplace installs to 5,341,071 and repository scale, and recorded the vendor install claim moving from 8M+ to 11M+.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-10-06 - Recorded the native Cline Desktop app as a fifth delivery surface, the Cline Spec Driven enterprise platform built with LG CNS, and refreshed repository and marketplace counters.
- 2026-10-07 - Added the cline/cline star history chart to the Status section.
- 2026-10-18 - Recorded Cline Cloud sessions rolling out gradually in v4.1.25 (October 16, 2026): hosted sandbox tasks on a picked repo and branch that keep running after the editor closes, and refreshed the marketplace install count.
- 2026-10-18 - Recorded the ClinePass pricing wording settling at a flat $9.99/month in the docs (promotional-rate wording retired, headline unchanged), and appended the matching Price history row.
- 2026-10-27 - Rotation re-verification, every cited reference live; recorded v4.1.26 (October 26): the Local/Cloud model toggle and sandbox progress card for cloud tasks, the provider-catalog refresh with ClinePass defaulting to Kimi K3.1 Pro, GPT-6 `max_completion_tokens` fixes, and the Gemini native-search 429 fix, with the cli-v3.0.74, desktop-v0.0.49, and sdk v0.2.0 component tags.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where Cline sits in the harness layer
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - capability rows for the harness field
- [Vibe Kanban](../../orchestration/vibe-kanban/index.md) - the orchestration pattern Cline's kanban app bakes in
- [my-ai-workflow](../../../my-ai-workflow/index.md) - rotating an open agent into daily practice

## References

- https://github.com/cline/cline - surfaces, rules, SDK, license, repository scale as of 2026-10-17
- https://cline.bot/ - product overview, install and star claims
- https://cline.bot/pricing - free core, usage billing, enterprise tiers
- https://cline.bot/cline-pass - the open-weights subscription and its labs
- https://docs.cline.bot/ - agent overview and configuration documentation
- https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev - verifiable install count, 5,736,752 as of 2026-10-26, and ratings
- https://news.ycombinator.com/item?id=43360564 - early community thread on Cline as an autonomous VS Code agent
- https://news.ycombinator.com/item?id=48525711 - Ask HN thread on reducing Cline's token usage
