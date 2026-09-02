---
title: QwenPaw
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtimes, python, self-hosted, open-source]
readability: 3
audience_notes: >
  Engineers choosing a self-hosted personal assistant that must live in chat apps, especially Chinese messaging platforms.
  Assumes you know what an agent runtime and a local LLM are.
---

QwenPaw is the AgentScope team's Apache-2.0, self-hostable personal AI assistant in Python, deployable on your own machine or the cloud, reachable through seven chat apps plus a web console, TUI, and beta desktop app, with three-layer memory, scheduled tasks, and purpose-trained small Qwen models for offline use.
Facts below verified as of 2026-09-02.

**QwenPaw's edge is the channel matrix, DingTalk, Lark, WeChat, QQ, Discord, Telegram, and iMessage from one self-hosted instance, which no Western-centric runtime in this category matches, and its built-in five-layer security stack is the strongest default posture in the category.**

## What it is

A Python (3.11 to 3.13) runtime with working context, verbatim history, and a self-evolving Markdown knowledge base (via the ReMe project), cron-style scheduled tasks, document skills, a file workspace, browser and computer use, multi-agent spawning, and MCP extensibility.
It ships purpose-trained QwenPaw-Flash 2B, 4B, and 9B models with a built-in llama.cpp runtime, so it runs fully offline, plus DashScope, OpenAI, Anthropic, Gemini, DeepSeek, OpenRouter, Ollama, and LM Studio providers.
v2.0 (July 2026) was a ground-up rewrite on the same org's AgentScope 2.0 framework (about 30k stars).
Install via pip, curl script, Docker, Alibaba Cloud ECS one-click, a free cloud platform, or a beta Tauri desktop app.
Apache-2.0, by the AgentScope team; Alibaba involvement is visible in the deploy and model stack but the repo itself credits the team, not the company.

## Status

Rapid and churny: 34,781 stars, 3,053 forks, 912 open issues and PRs as of 2026-09-02, created 2026-02-24, pushed 2026-09-02, 2,314 commits.
v2.1.0 released 2026-08-13 with a 2.2.0 beta already on PyPI.
**A ground-up rewrite one month before the current minor line is the churn signature: adoption is real, stability is not yet the product.**

## Strengths

- The broadest chat-channel matrix in the category, particularly the Chinese platforms peers skip.
- Five documented security layers (per-OS kernel sandbox, Tool Guard, File Guard, Skill Scanner, Access Policy) built into the core.
- A genuine offline path: local llama.cpp runtime with its own small trained models, no API key required.
- Memory stays as human-readable, editable Markdown.

## Cautions

- `qwenpaw init --defaults` auto-accepts the telemetry prompt, which privacy-conscious users must opt out of explicitly.
- Young and heavily rewritten, with much of the roadmap (voice, computer use, multi-workspace) still in progress.
- The macOS desktop app is beta and unnotarized, requiring a Gatekeeper bypass.
- 912 open issues and PRs, and the Alibaba-ecosystem gravity (ECS, DashScope, DingTalk) may bias defaults despite provider neutrality.

## Pricing

N/A, free and Apache-2.0.
The AgentScope Platform cloud deployment is described in the README as free; your costs are optional API keys for cloud models.

## Compared to

- [OpenClaw](../openclaw/index.md): the ecosystem and community leader; choose QwenPaw for the channel matrix and built-in security stack, OpenClaw for ecosystem depth.
- [Nanobot](../nanobot/index.md): the minimal readable Python core; choose QwenPaw for the fuller Agent OS surface, nanobot for hackability.
- [ZeroClaw](../zeroclaw/index.md): the Rust performance bet; choose ZeroClaw for footprint, QwenPaw for channels and offline models.

## Bottom line

**Recommended for self-hosters whose assistant must live in WeChat, DingTalk, or Lark, or who want an offline-capable assistant with defaults that assume things go wrong.**
Not for stability-first adopters mid-rewrite, or users who will not read the telemetry opt-out.

## See also

- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the category comparison this note joins
- [OpenClaw](../openclaw/index.md) - the category root
- [Nanobot](../nanobot/index.md) - the minimal alternative
- [PicoClaw](../picoclaw/index.md) - the other China-adjacent channel matrix, on microcontrollers

## References

- https://raw.githubusercontent.com/agentscope-ai/QwenPaw/HEAD/README.md - channels, security layers, install, roadmap
- https://github.com/agentscope-ai/QwenPaw - stars, forks, dates, language
- https://pypi.org/project/qwenpaw/ - package versions and cadence
- https://qwenpaw.agentscope.io/ - the docs site
- https://github.com/agentscope-ai/agentscope - the parent framework behind the v2.0 rewrite
- https://platform.agentscope.io/ - the free cloud deployment option
