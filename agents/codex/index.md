---
title: Codex
created: 2026-08-22
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, coding-agents, harnesses, openai, developer-tools]
readability: 3
audience_notes: >
  Engineers choosing a subscription-backed coding agent who want to know what OpenAI's Codex actually ships today.
  Assumes you have used at least one terminal agent and know what AGENTS.md is.

---

Codex is OpenAI's coding agent: a Rust CLI, an IDE extension, a desktop app, and a cloud service, all included in ChatGPT plans.
Facts below verified as of 2026-09-05.

**Codex is the only big-lab harness whose Apache-2.0 CLI an individual can still just run, and that matters more day to day than any single feature difference with Claude Code.**

## What it is

The `codex` CLI runs locally against your repository, with `/init` writing an AGENTS.md, sandboxed permissions, `/review` for local code review, skills and a plugin marketplace, subagents, and `codex exec` for scripts and CI.
**Codex cloud runs the same agent** in cloud environments reachable from web, CLI, and GitHub (`@codex` on issues and PRs), and the SDK, app server, and MCP server expose the harness as a platform.
Default models are the GPT-5.6 family (Sol for hard reasoning, Terra the workhorse, Luna cheap and fast), with GPT-5.3-Codex-Spark in research preview for Pro users.

## Status

**Active.**
`openai/codex` shows about 121.6k stars, about 18.6k forks, and about 10.3k commits under Apache-2.0 as of 2026-09-05.
The CLI launched April 2025 and has been rewritten and rebuilt since; the current docs position it as an open agent harness platform.

## Strengths

- **Open-source CLI you can audit, fork, and drive with an API key**, no subscription required.
- Included from the ChatGPT Free tier upward, so the entry price is zero.
- AGENTS.md is the first-class configuration convention, not a vendor variant.
- Model tiering (Sol/Terra/Luna) makes high-volume work cheaper without changing tools.
- Sandboxing and permission profiles are documented and prominent.

## Cautions

- **API-key mode drops the cloud features** (GitHub code review, Slack integration); those need a ChatGPT plan.
- Usage is metered in shared five-hour windows across ChatGPT and Codex features, and the published per-window message ranges are wide (for example 10-100 local Sol messages on Plus).
- The April 2025 launch drew sharp comparisons: early builds hallucinated docs Claude Code wrote correctly, and the original TypeScript CLI was rough; judge current releases, not that launch thread.
- Skills and plugins are converging on formats every vendor now claims, so expect churn.

## Pricing

**Included in ChatGPT Free**, Go ($8/month), Plus ($20/month), Pro 5x ($100/month), Pro 20x ($200/month), Business ($20-25 per user), Enterprise and Edu.
Overage is sold as credits; API-key usage is plain token pricing.

## Compared to

- [Claude Code](../claude-code/index.md): deeper orchestration layer, heavier token baseline, closed client; pick Anthropic's stack only if you are all-in on Claude models.
- [Gemini CLI](../gemini-cli/index.md): also Apache-2.0, but Google ended free consumer access in June 2026.
- [OpenCode](../opencode/index.md): provider-neutral and MIT, but no bundled subscription usage.

## Bottom line

**Recommended for anyone already paying for ChatGPT**: it is the subscription-backed harness with the least lock-in.
My own split: work that suits a subscription goes here, metered work goes to aider or OpenCode on my keys.
Not the cheapest path if your usage is light and token-based (aider or OpenCode with your own keys costs less).

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - Codex's place in the four-layer map
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - what running Codex plus siblings in parallel looks like
- [my-ai-workflow](../../my-ai-workflow/index.md) - a practitioner's harness rotation that includes Codex
- [Claude Code](../claude-code/index.md) - the direct subscription-first rival

## References

- https://learn.chatgpt.com/docs - product overview and surfaces
- https://learn.chatgpt.com/docs/codex/cli - CLI features, plugins, review, exec
- https://learn.chatgpt.com/docs/pricing - plans, usage windows, credit rate card
- https://github.com/openai/codex - repository scale and Apache-2.0 license, as of 2026-09-05
- https://news.ycombinator.com/item?id=43708025 - launch discussion with early critical comparisons
