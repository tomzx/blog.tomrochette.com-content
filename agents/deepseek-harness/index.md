---
title: DeepSeek Harness
created: 2026-08-30
updated: 2026-09-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, harnesses, coding-agents, plugins, open-source]
readability: 3
audience_notes: >
  Engineers choosing a coding-agent harness who care about extensibility and traceability more than turnkey polish.
  Assumes you know what an agent harness, a plugin system, and BYOK mean.
---

DeepSeek Harness (`dsh`) is DeepSeek's open-source, MIT-licensed coding-agent harness built on an everything-is-a-plugin kernel where the model, tools, UI, and even the agent loop are hot-swappable plugins.
Facts below verified as of 2026-09-04.

**The bet is not another agent but a harness with nothing built in: if the plugin architecture holds, forking a harness to change it becomes obsolete.**
Three weeks in, the bet is unproven and the project says so itself.

## What it is

A TypeScript CLI and web UI (`npx @deepseek-ai/dsh web`) that runs coding agents against local workspaces with file editing, shell, search, skills, planning, subagents, and workflows.
Four runtime modes set the tool surface: Standard, Code (the model orchestrates tool calls through generated TypeScript), Minimal (bash plus editor only, aimed at fair benchmarking), and Creator (authoring new plugins at runtime).
Everything sits on Cordis, a plugin kernel with hot reload and reversible side effects, described in a companion paper from Peking University and DeepSeek-AI.
Surfaces beyond the web UI: a headless one-shot mode, a JSON-RPC SDK, an ACP adapter for editors, and a Python SDK wheel.
It is local-first and BYOK: API keys stay in a local credentials file, with providers including Anthropic, OpenAI, Bedrock, Vertex, Azure, and any OpenAI-compatible endpoint.

## Status

New and extremely loud: 211,461 stars, 24,782 forks, and roughly 15,000 commits as of 2026-09-04, three weeks after the repo was created on 2026-08-13.
No stable release exists, only alpha and rc prereleases (dsh-v0.1.2-rc.1 on 2026-09-03), and the README warns there will be compatibility-breaking changes.
The launch thread drew 747 points and 301 comments on Hacker News, with the author answering questions directly.
An ecosystem is already forming: a Tauri desktop port with 1,640 stars, a plugin directory site, and an MCP plugin catalog.
**I read the star count as attention, not adoption, and the safest status label is developer preview.**

## Strengths

- Full traceability: an append-only session log records prompts, reasoning, tool calls, and subagent scheduling, with resume, fork, and replay over one event stream.
- Capability swaps happen through configuration, not forks, which is the cleanest test of the plugin thesis.
- Minimal mode exists specifically so model benchmarks run on identical harness scaffolding.
- DeepSeek shipped it MIT with multiple provider support, so it is usable without DeepSeek models.

## Cautions

- The project's own SAFETY.md states it has not undergone a security audit, executes model-generated code, and that its sandboxing and approval prompts do not guarantee isolation.
- Alpha software with announced breaking changes; anything built on it will churn.
- Hacker News debate flagged plugin ecosystems as an attack surface and a long-term compatibility burden, and found the Cordis paper's novelty overstated.
- Issues are disabled in favor of Discussions, which makes the bug backlog harder to read than peers.

## Pricing

Free and open source under MIT.
No hosted tier and no pricing page; costs are whatever your model provider charges.

## Compared to

- [Claude Code](../claude-code/index.md): the turnkey choice with subscription billing and polished defaults; choose dsh when you want open internals and full traces instead.
- [OpenCode](../opencode/index.md): the stable community-governed daily driver; choose dsh when you want to modify the harness itself rather than configure it.
- [Codex](../codex/index.md): OpenAI's CLI with real OS-level sandboxing; dsh has stronger observability but no sandbox guarantees today.

## Bottom line

**Recommended for harness builders and benchmark runners who want a hackable, fully traced agent platform, with eyes open that it is an alpha.**
Not for anyone whose threat model includes untrusted repos on day one, or who wants a stable daily driver this quarter.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the capability comparison this note joins
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map of the harness layer
- [OpenCode](../opencode/index.md) - the stable open-source alternative
- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - what the models you plug into dsh change

## References

- https://github.com/deepseek-ai/deepseek-harness - repository, README, install, MIT license
- https://www.deepseek.com/harness/en/ - runtime modes and plugin architecture claims
- https://raw.githubusercontent.com/deepseek-ai/deepseek-harness/HEAD/SAFETY.md - the project's own security warnings
- https://news.ycombinator.com/item?id=49285244 - the 747-point launch thread, including critical takes on plugins and the Cordis paper
- https://arxiv.org/abs/2608.25512 - the Cordis composability paper behind the architecture
- https://github.com/hairyf/deepseek-harness-desktop - the community desktop port, evidence of early ecosystem pull
