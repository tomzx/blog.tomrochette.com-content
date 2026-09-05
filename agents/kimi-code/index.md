---
title: "Kimi Code"
created: 2026-09-05
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, cli, coding-agent, moonshot, byok]
readability: 3
audience_notes: >
  Engineers choosing a terminal coding agent, especially ones already paying for Kimi models or looking for a big-vendor CLI that is not Claude Code or Codex.
  Assumes you know what MCP, ACP, and BYOK mean.
---

**Kimi Code CLI is Moonshot AI's terminal coding agent, and it is the first big-model-vendor harness whose default path is a challenger model instead of Claude or GPT.**
Facts below verified as of 2026-09-05.

## What it is

A terminal AI coding agent that reads and edits code, runs shell commands, searches files, fetches pages, and picks its next step from the feedback.
It works out of the box with Moonshot's Kimi models and can be pointed at other compatible providers.
Distribution is a single binary (install script or npm), with a purpose-built TUI, video input in chat, conversational `/mcp-config` editing, a plugin marketplace with per-install trust levels, built-in `coder`, `explore`, and `plan` subagents, lifecycle hooks, and ACP support so Zed or JetBrains can drive a session.
The code lives in two repositories: the original `MoonshotAI/kimi-cli` (Apache-2.0, created 2025-10-15) and the newer canonical `MoonshotAI/kimi-code` (MIT, created 2026-05-22).

## Status

Active and big-vendor backed, about 18.6k combined stars as of 2026-09-05: `kimi-code` at 7,256 stars pushed the day of verification, `kimi-cli` at 11,323 stars last pushed 2026-09-01.
**The independent FrontierHarness Eval pegs it mid-pack on quality and cheap on cost: 56.7 percent pass at a $3.65 median cost per task, with an 88 percent cache rate on Kimi K3.**
The Hacker News footprint is thin (a 5-point 2025-10-31 thread and a 1-point 2026-01-27 one), which I read as distribution through Kimi's own channels rather than developer-mindshare gravity.

## Strengths

- Cheapest credible big-vendor harness path: the same token budget that buys one Claude Code task in FrontierHarness bought several Kimi Code ones.
- Full agent surface in one binary: subagents, hooks, marketplace skills, MCP, and ACP editor integration without plugins or Node.js.
- The model and the harness come from the same vendor, so prompt-to-model tuning is first-party.

## Cautions

- The repository split (Apache-2.0 `kimi-cli` versus MIT `kimi-code`) is unresolved: which repo receives long-term investment is the reader's guess as of 2026-09-05.
- Your tokens flow to Moonshot's API in the default path, the same vendor-dependency trade Claude Code and Codex make, just with a cheaper vendor.
- Thin independent coverage means the FrontierHarness numbers are nearly the only third-party evidence available.

## Pricing

The harness is free and open source.
Usage is Kimi Code OAuth (your Kimi subscription) or a Moonshot Open Platform API key: kimi-k3 at $3/$15 per million tokens and kimi-k2.7-code at $0.95/$4.00 as of 2026-09-05, with other OpenAI-compatible providers configurable.

## Compared to

- [Codex](../codex/index.md): the other big-vendor open CLI, stronger on FrontierHarness quality (66.7 percent) but at roughly five times Kimi Code's median task cost.
- [Qwen Code](../qwen-code/index.md): Alibaba's fork-and-rebrand path into the same market; Kimi Code is a from-scratch Moonshot product rather than a Gemini CLI derivative.
- [OpenCode](../opencode/index.md): the provider-neutral alternative when you want the harness decoupled from any one model vendor.

## Bottom line

Recommended for engineers already inside the Kimi ecosystem and for token-payers who want a big-vendor-polished agent on challenger-model economics.
Not for teams that need local models, or anyone who needs more than one independent evaluation before trusting a harness.

## See also

- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the Kimi pricing this note's economics ride on
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where a vendor-built CLI sits in the harness layer
- [Codex](../codex/index.md) - the subscription-included big-vendor CLI comparison point
- [Protocols Feature Matrix](../protocols-feature-matrix/index.md) - ACP and MCP, both of which Kimi Code speaks

## References

- https://github.com/MoonshotAI/kimi-code - the canonical repository: license, features, subagents, ACP
- https://github.com/MoonshotAI/kimi-cli - the original repository and its Apache-2.0 history
- https://moonshotai.github.io/kimi-code/en/ - official documentation
- https://www.kimi.com/code/docs/ - product docs and login paths
- https://frontierharness.org - the independent pass-rate and cost-per-task numbers
- https://hn.algolia.com/api/v1/items/45767884 - the largest HN thread, cited as the thin-footprint signal
