---
title: Claude Code
created: 2026-08-22
updated: 2026-08-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, coding-agents, harnesses, anthropic, developer-tools]
readability: 3
audience_notes: >
  Engineers who already drive a terminal coding agent and are deciding whether to standardize on Anthropic's harness.
  Assumes familiarity with the edit-test-commit loop and MCP.

---

Claude Code is Anthropic's agentic coding tool: a terminal-first harness that also runs as IDE extensions, a desktop app, on the web, and from Slack.
Facts below verified as of 2026-08-27.

**It is the most complete harness platform shipping today, and also the most expensive way to run the same tokens, because you pay a large per-request baseline for orchestration whether you use it or not.**

## What it is

The CLI (`claude`) runs the edit-test-commit loop locally with permissions, hooks, skills, subagents, and MCP support.
The same engine surfaces in VS Code and JetBrains extensions, a desktop app, the web (claude.ai/code), mobile, and Slack.
**Sessions move between them (`claude --teleport` pulls a web session back to the terminal).**
Routines run scheduled tasks in the cloud, and the Agent SDK wraps the harness for custom agents.
The npm install is deprecated in favor of a native installer; third-party providers (Bedrock, Vertex) work in the CLI and IDE extensions.

## Status

**Active and dominant.**
The `anthropics/claude-code` repository shows about 142.8k stars and about 15.2k open issues and pull requests as of 2026-08-24; it hosts plugins, docs, and the issue tracker rather than the CLI source, which is proprietary.
Shipping pace in 2026 is high: agent view (May), dynamic workflows across tens of parallel subagents (May), routines (April), computer use (March).

## Strengths

- **The broadest surface coverage of any harness**: terminal, IDE, desktop, web, mobile, Slack, CI.
- Skills, hooks, subagents, and scheduled routines are the deepest operations layer in the field.
- Sessions are portable across surfaces in one product.
- First-party pairing with Claude models, which are trained against its tool syntax.

## Cautions

- **The harness baseline is heavy**: an independent proxy study measured about 33k input tokens sent before the user's prompt on a minimal task, versus about 7k for OpenCode.
The same study measured mid-session cache re-writes up to 54x and a 4.2x token multiplier on a two-subagent fan-out (July 2026 snapshot).
- The same study found 2.1.207 ignored `AGENTS.md` and only read `CLAUDE.md`, so cross-tool instruction files silently do nothing.
- The client binary is closed; a June 2026 reverse-engineering post found hidden Unicode markers in the system prompt encoding the user's API base URL and timezone classification, and the March 31, 2026 npm sourcemap leak exposed roughly 512k lines of internals Anthropic had not documented.
- Cost complaints on API-billed usage are a running theme in community threads.

## Pricing

Included in Claude Pro ($17/month annual, $20 monthly), Max 5x ($100/month), and Max 20x ($200/month), subject to usage limits.
**Alternatively, pay per token through the Anthropic Console or a cloud provider.**
Price and plan changes are at Anthropic's discretion, per the product page.

## Compared to

- [Codex](../codex/index.md): the other subscription-first platform, but its CLI is Apache-2.0; choose it if you live on OpenAI models.
- [OpenCode](../opencode/index.md): the lean open alternative, roughly a fifth the baseline tokens in the July 2026 proxy study; choose it when you pay for tokens yourself.
- [Gemini CLI](../gemini-cli/index.md): was the free outlier, now consumer-superseded by Antigravity CLI.

## Bottom line

**Recommended for teams standardized on Claude models who will actually use the orchestration layer.**
I run it where someone else pays the token bill, and reach for OpenCode when I pay it myself.
Not for the token-frugal or for anyone who needs an open, auditable client.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where this harness sits in the four-layer map
- [Rethinking Code Review in the Age of LLMs](../../rethinking-code-review-in-the-age-of-llms/index.md) - the review surface this harness's output still has to survive
- [agent-skills-that-render](../../agent-skills-that-render/index.md) - making the skills layer of this harness render correctly
- [OpenCode](../opencode/index.md) - the measured counterpoint on harness token overhead

## References

- https://code.claude.com/docs/en/overview - surfaces, skills, hooks, subagents, routines, installation
- https://claude.com/product/claude-code - pricing tiers and 2026 feature timeline
- https://github.com/anthropics/claude-code - repository scale (about 142.8k stars) and npm deprecation, as of 2026-08-24
- http://web.archive.org/web/20260814104128/https://thereallo.dev/blog/claude-code-prompt-steganography - independent analysis of hidden prompt markers (archived; the live site blocks automated fetches)
- https://systima.ai/blog/claude-code-vs-opencode-token-overhead - measured baseline, cache, and subagent token costs (July 2026)
- https://news.ycombinator.com/item?id=47584540 - the March 31, 2026 npm sourcemap-leak discussion (2,095 points)
