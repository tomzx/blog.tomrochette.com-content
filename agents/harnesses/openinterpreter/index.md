---
title: Open Interpreter
created: 2026-09-27
updated: 2026-10-01
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, harnesses, coding-agents, open-source, harness-emulation]
readability: 3
audience_notes: >
  Engineers choosing a terminal coding agent to drive open-weight or low-cost
  models. Assumes you know what a harness, BYOK, AGENTS.md, MCP, and ACP are.
---

Open Interpreter is an Apache-2.0 terminal coding agent relaunched in July 2026 as a Rust fork of OpenAI's Codex CLI, positioned as the agent layer for low-cost and open-weight models like Kimi K3 and GLM.

**The 2023 code-execution chat agent is gone: today's Open Interpreter bets that the harness, not the model, is the product, and emulates whichever harness each model was trained on.**

## What it is

A terminal agent installed by a curl script and run as `interpreter` or `i`, built on the Codex CLI core and inheriting its interface, app-server protocol, and cross-platform sandboxing.
Its distinguishing feature is `/harness`, which switches the active emulation among native, claude-code, kimi-code, qwen-code, deepseek-tui, swe-agent, and minimal profiles.
The pitch is that Claude drives a Claude Code-like harness, GPT drives the Codex harness, and Kimi, Qwen, and DeepSeek drive emulations of their provider-recommended harnesses instead of one generic tool set.
The portability story is explicit: repository `AGENTS.md`, shared `.agents/skills` directories, MCP, ACP for editors, and a one-line `codexPathOverride` for existing Codex SDK users.
A separate Open Interpreter Desktop app covers cross-app knowledge work (spreadsheets, PDFs, email, browsers) with profiles, voice mode, approvals, and subagents.
The fork is documented rather than hidden: FORK_BRANDING.md defines the distribution as `variant: "open-interpreter"` on Codex internals, with `rust-v` release tags and `~/.openinterpreter` as the product home.

## Status

Active and fast-moving again after roughly nineteen quiet months: 68,451 stars, 5,881 forks, and a push on 2026-09-25 as of 2026-09-27, with only 4 open issues, which tells you issue intake is tightly curated.
The latest release is rust-v0.0.45, published 2026-09-20, and the 0.0.43 notes describe a maintenance release on the "stable upstream Codex rust-v0.154.0 compatibility baseline" with presets for glm-5.1, glm-4.7-flash, Gemini, Claude, and OpenAI IDs.
The legacy Python line is stranded: PyPI shows open-interpreter 0.4.3, the last of 130 releases, uploaded 2024-10-26.
The history matters: a Show HN on 2023-08-30 (82 points), a 117-point thread in November 2023, a 72-point "natural language interface for computers" thread in November 2024, then silence until the relaunch post of 2026-07-13.
The README now opens with "Today: Kimi K3 is here", saying the project reimplemented the provider-recommended Kimi Code harness in Rust.

## Strengths

- **Harness emulation is a genuinely different bet: instead of one generic agent loop, each model gets the tool behavior, system instructions, and compaction workflow its RL environment resembled.**
- The portability list is checkable rather than aspirational: AGENTS.md, `.agents/skills`, MCP, ACP, and the Codex exec protocol, with a script (`scripts/test-codex-sdk-compat.sh`) that verifies SDK compatibility without a provider.
- BYOK breadth reaches the cheap end of the market, down to Z.AI's lightweight `glm-4.7-flash`, and local models work through any OpenAI-compatible Chat Completions endpoint.
- A computer-use QA skill (driving web apps through agent-browser and native apps through trycua) ships in the box, a niche most terminal agents leave to plugins.

## Cautions

- **The star count flatters the present: most of the 68k stars date to the 2023 hype cycle, and the current user base is whoever adopted a July 2026 fork, not the historical total.**
- It is a downstream fork of Codex with a `rust-v0.154.0` baseline, so OpenAI owns the core and Open Interpreter's differentiation is a provider, harness, and branding layer on top.
- The evidence for harness emulation is vendor-run: the relaunch post reports the project's own Terminal-Bench 2.1 measurement of DeepSeek V4 Flash, unverified independently.
- The identity churn is three pivots deep (code interpreter, OS-mode natural language interface, Codex fork), so anything built on its platform story should expect another turn.
- An installer that pipes `curl | sh` from the project's own domain, for a binary fork of a fast-moving upstream, is a supply-chain surface worth pinning.

## Pricing

Free and open source under Apache-2.0, and I found no Open Interpreter-operated hosted or metered tier anywhere I fetched: the sitemap scan of 2026-09-27 lists no pricing pages, and the desktop FAQ describes a pure BYOK model where data goes only to the provider in your active profile.
Usage therefore bills at whatever provider the profile points at (Z.AI, DeepSeek, OpenAI, Anthropic, Google, or a local Ollama or LM Studio endpoint), so no prices belong in this note and no price history table applies.

## Compared to

- [OpenCode](../opencode/index.md): the established open terminal agent with an original codebase; choose OpenCode for community governance and a longer track record, Open Interpreter if the open-model harness-emulation pitch fits your stack.
- [Grok Build](../grok-build/index.md): the other fork-lineage terminal agent in this section; Grok Build is a vendor monorepo sync that takes no contributions, while Open Interpreter is an Apache-2.0 fork you can patch.
- [Codex](../codex/index.md): the upstream itself; the shared exec protocol and SDK override mean you can run both, and Open Interpreter is best described as a tuned Codex distribution for cheap models.

## Bottom line

**Recommended for engineers standardizing on open-weight or low-cost models who want a maintained terminal agent without building one, and who accept that the core is Codex's.**
Not for anyone needing a mature plugin ecosystem today (the old Python one is stranded), and not as evidence of community health via its star count.
My disagreeable claim: harness emulation is a configuration layer rather than new research, and its long-term value depends on whether upstream Codex eventually makes per-model harnesses easy for everyone.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars scan surfaced it.
- 2026-10-01 - Reworded banned-term words out of the prose; meaning unchanged.

## See also

- [OpenCode](../opencode/index.md) - the category's reference open terminal agent, and the comparison point for original codebase versus fork
- [Grok Build](../grok-build/index.md) - the other fork-lineage harness, with the opposite contribution model
- [OpenRouter](../../model-access/openrouter/index.md) - the open-model access layer this agent's BYOK profiles typically bill through
- [Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - the section-root guide to picking the models these harnesses drive

## References

- https://api.github.com/repos/openinterpreter/openinterpreter - 68,451 stars, 5,881 forks, Apache-2.0, pushed 2026-09-25, 4 open issues, as of 2026-09-27
- https://raw.githubusercontent.com/openinterpreter/openinterpreter/main/README.md - the Kimi K3 note, the `/harness` list, ACP and Codex SDK compatibility, and the portability story
- https://www.openinterpreter.com/blog/open-interpreter - the 2026-07-13 relaunch post: Apache-2.0, built on Codex CLI, and the harness-emulation rationale (the page is JS-rendered, so I extracted its text through a proxy; the direct fetch returned 200 with only the title)
- https://raw.githubusercontent.com/openinterpreter/openinterpreter/main/RELEASE_NOTES.md - version 0.0.43 on the Codex rust-v0.154.0 baseline, with the Z.AI and other provider presets
- https://raw.githubusercontent.com/openinterpreter/openinterpreter/main/FORK_BRANDING.md - the fork identity contract: variant open-interpreter, `interpreter`/`i` commands, rust-v tag prefix
- https://api.github.com/repos/openinterpreter/openinterpreter/releases/latest - rust-v0.0.45, published 2026-09-20
- https://pypi.org/pypi/open-interpreter/json - the legacy Python line: 0.4.3, 130 releases, last upload 2024-10-26
- https://hn.algolia.com/api/v1/items/37315866 - the Show HN of 2023-08-30, 82 points, the original CodeLlama terminal CLI
- https://hn.algolia.com/api/v1/items/38242343 - the 2023-11-12 thread, 117 points, carrying the early local-execution skepticism
- https://hn.algolia.com/api/v1/search?query=%22open%20interpreter%22&tags=story - the HN footprint scan, including the 72-point thread of 2024-11-18
- https://www.openinterpreter.com/docs/desktop/faq - the desktop app's BYOK data handling and local-model profiles
- https://www.openinterpreter.com/sitemap.xml - the surface scan (terminal and desktop docs, downloads, no pricing pages) as of 2026-09-27
