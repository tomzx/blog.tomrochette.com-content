---
title: Nanobot
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtimes, python, self-hosted, open-source]
readability: 3
audience_notes: >
  Engineers who want a small, readable, self-hosted personal agent runtime and do not need the largest ecosystem.
  Assumes you know what a chat channel integration and an MCP server are.
---

Nanobot is an MIT-licensed, self-hosted personal AI agent runtime in Python that packages a small agent core with a bundled WebUI, terminal UI, eight-plus chat channels, tools, long-term memory, MCP support, scheduled automations, and an OpenAI-compatible API, positioned openly as the lightweight alternative to OpenClaw.
Facts below verified as of 2026-09-05.

**Nanobot is the category's readability bet: an agent core small enough to read in an afternoon, at the price of alpha maturity and a bus factor of essentially one maintainer.**

## What it is

A Python 3.11+ package (`pip install nanobot-ai`) with one agent loop over an OpenAI-compatible provider abstraction: WebUI on localhost, terminal TUI, one-shot CLI, background gateway, and chat channels for Telegram, Discord, Slack, WeChat or Feishu, Email, and Mattermost.
Tools cover files, shell, web search, images, and MCP; memory includes a long-horizon "Dream" mechanism; v0.3.0 added inline subagents and automation scheduling.
Model routing spans any OpenAI-compatible API, Ollama, and vLLM with per-session presets and fallback chains, and an OpenAI-compatible HTTP API plus Python SDK support embedding.
Started by Xubin Ren as a personal project, now under the HKUDS lab banner (the Data Intelligence Lab at HKU), MIT-licensed, Docker and Render deploy paths.

## Status

One of the fastest adoption curves in the category: 47,634 stars, 8,409 forks, 758 open issues as of 2026-09-02, created 2026-02-01, pushed the day of verification.
Fifteen PyPI releases from February to July 2026 (v0.3.0 on 2026-07-25), and the launch HN thread drew 257 points.
**PyPI still classifies it Alpha, and one listed maintainer carries the release burden, the two facts I would weight against the star count.**

## Strengths

- The irreducible core: HN's technical commenters read it as the minimum viable agent, roughly a 99 percent codebase reduction against OpenClaw by omitting heavyweight orchestration.
- Full surface out of the box: WebUI in the wheel, eight-plus channels, API, SDK, Docker.
- Provider freedom including fully local models, with per-session routing and fallbacks.
- Permissive MIT at a moment when the category's root project carries a custom license.

## Cautions

- Alpha maturity: seven months old, breaking-speed releases, and a 762-issue backlog large for its age.
- Single-maintainer concentration on PyPI.
- The category-level security problem applies in full: shell access plus chat channels plus prompt injection is the surface HN called a security nightmare, and a sibling runtime had an RCE exploit.
- Lineage questions from the community about NanoClaw inspiration were never clearly addressed.

## Pricing

N/A, fully open source under MIT and self-hosted.
You supply LLM keys and infrastructure; the only money path is third-party hosting.

## Compared to

- [OpenClaw](../openclaw/index.md): the 388k-star root with the largest ecosystem and heaviest codebase; choose OpenClaw for ecosystem, nanobot for readable Python.
- [ZeroClaw](../zeroclaw/index.md): the Rust single-binary performance bet; choose ZeroClaw for footprint, nanobot for hackability.
- [NanoClaw](../nanoclaw/index.md): the containerized, auditable security-first rewrite; choose NanoClaw when isolation is the priority, nanobot when extensibility in Python is.

## Bottom line

**Recommended for engineers who want to read and extend their assistant runtime in Python, binding it to localhost and taking the security surface seriously themselves.**
Not for production assistants unattended on the open internet, or anyone who needs vendor support.

## See also

- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the category comparison this note joins
- [OpenClaw](../openclaw/index.md) - the ecosystem heavyweight it positions against
- [QwenPaw](../qwenpaw/index.md) - the channel-breadth counterpart
- [ZeroClaw](../zeroclaw/index.md) - the performance counterpart

## References

- https://github.com/HKUDS/nanobot - repository, features, license, adoption numbers
- https://raw.githubusercontent.com/HKUDS/nanobot/HEAD/README.md - surfaces, install paths, and the OpenClaw positioning
- https://pypi.org/project/nanobot-ai/ - the Alpha classification, release cadence, and maintainer record
- https://news.ycombinator.com/item?id=46897737 - the 257-point launch thread, including the security critique
- https://github.com/openclaw/openclaw - the comparison baseline
- https://github.com/zeroclaw-labs/zeroclaw - the comparison data
