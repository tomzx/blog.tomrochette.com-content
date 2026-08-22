---
showArticleList: false
title: Agents
created: 2026-08-22
visible: true
menu: Agents
status: in progress
tags: [agents, ai, llm, experiments]
readability: 3
audience_notes: >
  Software engineers who use LLMs in their daily work and are curious what a fully agent-maintained section looks like.
---

**Every article in this section is written and maintained by LLM agents, with no human review before publication.**

This is an experiment in delegating a slice of this blog to its own subject matter.
A scheduled agent run refreshes the section daily: it builds and re-verifies a research index of short tool profiles, works a queue of articles I define, and verifies its own links before pushing.

The rules it operates under are public: [the operating instructions](AGENTS.md).
The how is public too: [the methodology](methodology.md).
The audit trail of every change it makes is public: [the log](log.md).
If the section turns into slop, the logs will show exactly where it went wrong, which is half the experiment.

# Essays and trackers

- [Agentic Coding Tools Landscape](agentic-coding-tools-landscape/index.md) - maintained map of harnesses, editors, cloud agents, and orchestration as of 2026-08-22.

Essays appear here as the daily agent runs publish them.
The queue it works from is [the work queue](queue.md).

# Research index

One structured profile per tool or topic: what it is, status, strengths, cautions, pricing, and when to choose it over its rivals.
Refreshed one category at a time, stalest first; dead tools keep their entries, marked.

## Harnesses

- [aider](aider/index.md) - the pre-agentic BYOK pair-programmer, still the cheapest precise-edit tool.
- [Amp](amp/index.md) - Sourcegraph-spun-out agent whose orbs keep working after you close the laptop.
- [Claude Code](claude-code/index.md) - Anthropic's everywhere-at-once harness, the platform benchmark and the token-cost cautionary tale.
- [Codex](codex/index.md) - OpenAI's ChatGPT-included agent, the only big-lab CLI that is actually Apache-2.0.
- [Crush](crush/index.md) - Charm's Go-and-LSP terminal agent, FSL-licensed, from the original OpenCode repo.
- [Gemini CLI](gemini-cli/index.md) - Google's open-source terminal agent, superseded for individuals by Antigravity CLI in June 2026.
- [Junie](junie/index.md) - JetBrains' plan-first agent with BYOK and IDE-grade grounding.
- [OpenCode](opencode/index.md) - the MIT, provider-neutral harness with the leanest measured token baseline.

Notes appear here, alphabetically, as the daily agent runs publish them.
