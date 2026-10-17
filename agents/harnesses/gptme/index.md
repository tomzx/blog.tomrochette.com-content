---
title: gptme
created: 2026-10-13
updated: 2026-10-17
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, harness, cli, terminal, local-first, autonomous-agents]
readability: 3
audience_notes: >
  Engineers choosing a terminal coding agent who want open source, local-first operation, and an agent that persists between runs.
  Assumes you know what bring-your-own-key means and what an agent tool loop is.
---

gptme is an MIT terminal agent by Erik Bjäreholt, first committed on March 24, 2023, that pairs local tools (shell, Python, files, browser, desktop) with a persistent agent layer built on a git repository as the agent's memory and workspace.

**Its claim to the harnesses category is seniority plus the persistent-agent thesis: it predates aider by eleven days and every big-lab CLI by about two years, and it is the only member of this category whose most prolific contributor is its own autonomous agent.**

## What it is

A Python package on PyPI (`pipx install gptme`) offering a plain CLI, a Textual TUI, a server with a REST API and self-hostable web UI, and a desktop app since v0.32.0 (July 2026).
Built-in tools cover shell, IPython, file edits, Playwright browsing, vision, tmux sessions, full-desktop computer use, subagents, and GitHub through the gh CLI.
Extensibility is layered: Python plugins, Anthropic-format skills, keyword-matched lessons, and lifecycle hooks, with MCP in both directions (client and server) and ACP for editors.
Providers are your choice: Anthropic, OpenAI, Google, Grok, DeepSeek, OpenRouter, existing ChatGPT or SuperGrok subscriptions, or local Ollama, LM Studio, vLLM, and llama.cpp.

## Status

Active and steadily shipped: 4,448 stars, 451 forks, and 38 open issues as of 2026-10-13, pushed the day of this check, with weekly dev pre-releases and stable v0.35.1 (October 15, 2026) on top of v0.35.0 the same day, a 61-feature release adding a memory guard that kills the agent's largest command when system memory runs low, queued prompts that steer the running turn, Ctrl+C tool stops in the TUI, and an IPython kernel-process split (v0.35.1); stable v0.34.0 (September 2026) added cross-harness memory and skills as slash commands.
Bootstrap-funded by its author, with a managed cloud (gptme.ai, early access) that bills usage-based credits.
PyPI downloads run about 32,000 per month as of 2026-10-13, modest next to this category's mass-market members.
**The governance curiosity is the contributor table: the top contributor is TimeToBuildBob, the project's own autonomous agent, at 2,506 contributions against the author's 1,915.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=gptme/gptme&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=gptme/gptme&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=gptme/gptme&type=date&legend=top-left" />
</picture>

## Strengths

- The persistent-agent layer is the differentiator: a git-based agent template holds identity, memory, lessons, and workspace, so an agent's brain is versioned, reviewable, and forkable.
- Cross-harness memory (gptme-util memory) uses Claude Code's format and is shared across gptme, Claude Code, and Codex sessions, so context is not trapped in one tool.
- Broadest surface-to-code ratio in the table: terminal, TUI, server, web UI, desktop app, computer use, and MCP in both directions, in a codebase its own "Are we tiny?" page keeps under watch.
- Genuine longevity: continuous development since March 2023 across the entire lifetime of the agent CLI category, with the release train still weekly.
- The autonomous track record is specific: the Bob agent claims 5,000+ merged pull requests across runs since 2025.

## Cautions

- The independent-discussion record is thin for a four-year-old project: its Show HN threads sit at 5, 5, and 1 points, and adoption (about 32k PyPI downloads a month) trails every category peer with comparable maturity.
- The README cites an August 2024 Show HN thread that no longer resolves in the Hacker News index, so part of the advertised launch history is unverifiable.
- Solo-maintainer concentration: the human bus factor is one, and the top contributor being an agent is as much a governance question as a feature.
- Running shell, Python, and desktop tools on your host (rather than in a sandbox) keeps the Anthropic-style security question open, though v0.33.0 added optional Docker and Wasmtime sandboxing.
- The managed cloud is early access with unpublished prices, so hosted economics are not yet knowable.

## Pricing

Free and open source under MIT.
The gptme.ai managed service is in early access with usage-based credits and no published prices as of 2026-10-13.
Model cost on your own machine is whatever your configured providers or local hardware charge.

## Compared to

- [aider](../aider/index.md): the other 2023-bootstrap terminal agent; aider stayed the precise-edit pair-programmer, gptme grew into the persistent general agent, and aider's development has stalled since May 2026.
- [Open Interpreter](../openinterpreter/index.md): the Rust Codex CLI fork that emulates provider harnesses; gptme is the older, tool-richer original whose scope is the whole assistant rather than cheap open-weight emulation.
- [OpenCode](../opencode/index.md): the vendor-neutral terminal default; OpenCode is the leaner daily driver, gptme the one that keeps working after you close the laptop.

## Bottom line

**Recommended for engineers who want one agent that codes, browses, and runs unattended on their own machine, with memory and lessons that survive between runs.**
Not for teams needing a large independent community, published hosted pricing, or sandboxed-by-default execution.

## Changes

- 2026-10-13 - Created.
- 2026-10-17 - Recorded the stable train reaching v0.35.1 (October 15) on top of the 61-feature v0.35.0 the same day (memory guard, steerable queued prompts, Ctrl+C tool stops, Jupyter kernel-process split), and re-fetched every cited reference in the rotation-adjacent volatile pass.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the category comparison this note joins
- [aider](../aider/index.md) - the other bootstrap 2023 terminal agent, eleven days younger
- [Open Interpreter](../openinterpreter/index.md) - the open terminal assistant gptme's own alternatives page names as its nearest neighbor
- [OpenCode](../opencode/index.md) - the vendor-neutral terminal default this note measures adoption against
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this section extends

## References

- https://api.github.com/repos/gptme/gptme - repository metadata: MIT license, 4,448 stars, 451 forks, push and creation dates (as of 2026-10-13)
- https://api.github.com/repos/gptme/gptme/readme - the README: tools table, plugins/skills/lessons/hooks, MCP and ACP, cross-harness memory, provider list, and the news timeline back to the March 2023 first commit
- https://gptme.org/docs/alternatives.html - the project's own positioning: coding-agent and persistent-agent comparison tables, bootstrap funding, first-commit dates for gptme and aider, and the Bob track-record claim
- https://gptme.org/docs/arewetiny.html - the small-by-design policy with startup-time and lines-of-code benchmarks
- https://gptme.org/docs/cloud.html - the gptme.ai managed service: early access, usage-based credits, GitHub integration
- https://api.github.com/repos/gptme/gptme/releases?per_page=5 - the weekly dev pre-release train and the stable v0.35.1 stamp (October 15, 2026)
- https://pypistats.org/api/packages/gptme/recent - the 32,174 downloads in the last month as of 2026-10-13
- https://api.github.com/repos/gptme/gptme/contributors?per_page=5 - the contributor table with TimeToBuildBob (the autonomous agent) first at 2,506
- https://hn.algolia.com/api/v1/search?query=gptme&tags=story - the thin independent-discussion record: Show HN threads at 5 (2023), 5 (2024), and 1 (2025) points
