---
title: Gemini CLI
created: 2026-08-22
updated: 2026-08-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, coding-agents, harnesses, google, developer-tools]
readability: 3
audience_notes: >
  Engineers who keep hearing Gemini CLI recommended as the free open-source terminal agent.
  Assumes you know the terminal agent pattern and what a free-tier rate limit is.

---

Gemini CLI is Google's open-source terminal agent for Gemini, Apache-2.0, launched June 25, 2025, and superseded for individual users by Antigravity CLI on June 18, 2026.
Facts below verified as of 2026-08-22.

**Every 2025 recommendation of Gemini CLI as the free terminal agent is dead advice for individuals: Google stopped serving free and AI Pro/Ultra users on June 18, 2026, and moved the product to Antigravity.**

## What it is

A TypeScript CLI (`gemini`) running a ReAct loop with built-in file, shell, web-fetch, and Google Search grounding tools, GEMINI.md project context, MCP support, conversation checkpointing, and a GitHub Action for issue triage and PR review.
It authenticated three ways: **Google OAuth (the famous free tier of 60 requests/minute and 1,000/day)**, a Gemini API key, or Vertex AI.

## Status

**Superseded for consumers, alive for enterprises.**
On May 19, 2026, Google announced it was unifying terminal agent work into Google Antigravity, whose Antigravity CLI (written in Go, multi-agent, sharing a harness with the Antigravity 2.0 desktop app) carries over skills, hooks, subagents, and extensions.
On June 18, 2026, Gemini CLI and the Gemini Code Assist IDE extensions stopped serving requests for Google AI Pro and Ultra subscribers and free individual users.
Enterprise Code Assist Standard/Enterprise licenses and paid API keys keep working, and the repository is still active: about 106.6k stars, 6,384 commits, weekly release channels as of 2026-08-22.
The README still advertises the free tier, which is stale for individuals; treat the README as the enterprise path's documentation.

## Strengths

- **The first Apache-2.0 CLI from a major lab, and until June 2026 the most generous free tier in the field.**
- Gemini 3 models with a 1M-token context window, unmatched for whole-repository prompting.
- Google Search grounding built in, not bolted on.
- Continuity for enterprise Code Assist customers is explicitly guaranteed by Google.

## Cautions

- **The consumer shutdown is the caution**: a product individuals built workflows around redirected them to a successor that did not ship 1:1 feature parity at transition.
- The launch thread was full of first-day quality complaints (failed edits, quota errors, weaker than Claude Code on hard tasks) alongside the enthusiasm; Gemini CLI was never the best harness, only the free one.
- Workspace account billing was confusing from day one and stays confusing in the enterprise paths.
- Quotas are shared between Gemini CLI and Gemini Code Assist agent mode, so the two products eat one allowance.

## Pricing

**For individuals: nothing to pay anymore, because there is no service**; Antigravity CLI is the successor product.
For enterprises: Gemini Code Assist Standard or Enterprise licensing, or pay-as-you-go Gemini API keys, with Vertex AI for regulated setups.

## Compared to

- [Antigravity](../antigravity/index.md): its CLI is the official successor, Go-based and multi-agent; individuals should start there, not with Gemini CLI.
- [Codex](../codex/index.md): still a genuinely open big-lab CLI with a consumer free tier.
- [OpenCode](../opencode/index.md): the provider-neutral way to keep using Gemini models from a terminal without Google's harness decisions.

## Bottom line

**Recommended only for organizations holding Code Assist licenses or paid API budgets.**
Not for individuals, whatever the 2025 blog posts (several of which I believed at the time) told you.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the harness layer map this note belongs to
- [my-ai-workflow](../../my-ai-workflow/index.md) - a rotation that treated Gemini tools as one option among several
- [ai-tools-i-have-used](../../ai-tools-i-have-used/index.md) - how fast tool recommendations go stale, this note being the proof
- [OpenCode](../opencode/index.md) - keeping Gemini models with a vendor-neutral harness

## References

- https://github.com/google-gemini/gemini-cli - repository, README free-tier claims, release channels, as of 2026-08-22
- https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ - the May 19, 2026 transition and June 18, 2026 consumer cutoff
- https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/ - the June 25, 2025 launch announcement
- https://developers.google.com/gemini-code-assist/docs/gemini-cli - current enterprise documentation and quota model
- https://news.ycombinator.com/item?id=44376919 - launch-day discussion, enthusiasm and failures side by side
