---
title: Qwen Code
created: 2026-08-24
updated: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, coding-agents, harnesses, open-source, alibaba]
readability: 3
audience_notes: >
  Engineers evaluating a zero-cost terminal agent or standardizing on Qwen models.
  Assumes you know what a fork is and what an OAuth free tier bills in.

---

Qwen Code is the Alibaba Qwen team's open-source (Apache-2.0) terminal coding agent, forked from Google's Gemini CLI v0.8.2 and developed independently since v0.1.
Facts below verified as of 2026-08-24.

**Qwen Code is the free on-ramp of the harness field, and the only major harness whose companion model family is itself open weights, which makes it the cleanest demonstration of model and harness evolving together.**

## What it is

**A Gemini CLI descendant that outgrew the original.**
The `qwen` TUI runs interactive sessions with `@file` references, and `qwen -p` runs headless for scripts and CI.
Beyond the terminal: IDE plugins for VS Code, Zed, and JetBrains, a desktop app, a daemon mode (`qwen serve`) that shares one agent across clients over ACP, TypeScript/Python/Java SDKs, and IM bot channels (Telegram, DingTalk, WeChat, Feishu).
Agent features include subagents, agent teams, auto-memory, auto-skills, hooks, sandboxing, git worktrees, computer use, and an agent arena for multi-model head-to-head runs.
It speaks OpenAI, Anthropic, Gemini, and Qwen APIs plus local models via Ollama or vLLM, switchable at runtime.

## Status

**Active and self-hosting in an unusual sense: the README states the project uses its own agent to file issues, submit PRs, review code, and run tests.**
The repository shows about 27.3k stars as of 2026-08-24 and was pushed the same day.
It launched in July 2025 as a Qwen3-Coder-optimized CLI; the Acknowledgments section records the Gemini CLI v0.8.2 origin and the split from upstream at v0.1.

## Strengths

- The launch free tier, 2,000 requests per day with no token limits via Qwen OAuth (August 2025), was the most generous in the field at the time.
- Open weights plus open harness: you can run the full stack, model included, on your own hardware.
- Multi-protocol support makes it a single client for every provider you hold keys to.
- Daemon mode and IM channels push it toward an always-on assistant, not just a terminal session.

## Cautions

- **The Claude Code parity table in the README is the vendor's own assertion**, not an independent measurement.
- Model behavior incidents attach to the model family: an April 2026 report describes Qwen correcting code to retract a "Taiwan is a country" statement, a governance consideration for behavior-sensitive work.
- Install assets and OAuth route through Alibaba cloud infrastructure, a data-residency factor for some organizations.
- English-language community footprint is thin: launch and release threads sit in single-digit points.

## Pricing

The agent is free and open source.
The launch free tier was 2,000 requests/day through Qwen OAuth (no token limits, as of August 2025); verify the current quota on the docs before budgeting around it.
BYOK works with any supported provider, including local models at no API cost.

## Compared to

- [Gemini CLI](../gemini-cli/index.md): the upstream project, now consumer-superseded by Antigravity CLI; Qwen Code is the fork that kept building for individuals.
- [OpenCode](../opencode/index.md): provider-neutral with no model-family agenda; choose it when you want no vendor gravity at all.
- [Claude Code](../claude-code/index.md): the parity target Qwen Code measures itself against in its own table.

## Bottom line

**Recommended for engineers trying an agentic harness at zero cost and for teams standardized on Qwen models.**
Not for workflows where model behavior provenance or data residency is tightly governed.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - Qwen Code in the independent tail of the harness layer
- [Gemini CLI](../gemini-cli/index.md) - the upstream whose shutdown of consumer access Qwen Code sidesteps
- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - where Qwen coding models sit in the price-performance field
- [ai-tools-i-have-used](../../ai-tools-i-have-used/index.md) - how fast tool allegiances rot, and why forks outlive their parents

## References

- https://github.com/QwenLM/qwen-code - README capabilities, fork acknowledgment, repository scale as of 2026-08-24
- https://qwenlm.github.io/qwen-code-docs/en/users/overview - modes, surfaces, and configuration documentation
- https://news.ycombinator.com/item?id=44653981 - the July 2025 launch thread
- https://news.ycombinator.com/item?id=44842523 - the 2,000 free requests/day announcement as launched
- https://news.ycombinator.com/item?id=45032918 - a critical look at Qwen Code's ecosystem context
- https://news.ycombinator.com/item?id=47956058 - the April 2026 Taiwan-correction behavior report
