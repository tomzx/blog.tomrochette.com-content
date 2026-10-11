---
title: Oh My Pi
created: 2026-10-10
updated: 2026-10-10
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, cli, coding-agent, lsp, fork]
readability: 3
audience_notes: >
  Engineers choosing a terminal coding agent who want IDE-grade grounding, and readers of the Pi note deciding between the frozen core and its batteries-included fork.
  Assumes you know what MCP, AGENTS.md, and BYOK mean.
---

Oh My Pi (omp) is a batteries-included fork of the Pi harness, built by Stencil Labs, whose bet is that the IDE should be wired into the agent loop instead of the core staying frozen.

## What it is

A TypeScript CLI on Bun with a native Rust core of roughly 80,000 lines, MIT-licensed, distributed through an install script at omp.sh, Homebrew, bun/npm (`@oh-my-pi/pi-coding-agent`), Nix, and a Windows PowerShell script.
It is a fork of Mario Zechner's Pi (the `badlogic/pi-mono` line), and it keeps Pi's extensibility while adding what Pi refuses to ship: 60-plus providers, 31 built-in tools, LSP operations wired into every write, DAP debugger control (lldb, dlv, debugpy), first-class subagents that fan out into worktrees and return typed results, an advisor model that watches every turn, live session sharing over `/collab`, and native Windows without WSL.
The hook is the name of the design: everything your IDE knows, the agent knows.

## Status

Very active and past its parent in stars: 34,842 stars and 3,791 forks as of 2026-10-10 (GitHub API), on a repository created 2025-12-31 and pushed the day of verification.
The npm latest is 18.8.7 (published 2026-10-09), and the changelog logs a near-daily train with pull requests numbered past 15,000.
Contribution policy loosened from a vouch requirement to temporarily-open PRs while the maintainers evaluate how open contributions go.
The Hacker News footprint is modest for the star count: a 42-point launch thread on July 21, 2026, and a 35-point "Harness Playbook" thread in September, which reads as adoption spreading through practitioners rather than through tech-media coverage.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=can1357/oh-my-pi&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=can1357/oh-my-pi&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=can1357/oh-my-pi&type=date&legend=top-left" />
</picture>

## Strengths

- **The strongest editor grounding in the terminal-harness field: renames go through LSP, and debugging happens through a DAP adapter (lldb, dlv, debugpy) instead of print statements.**
- It inherits what your other tools already wrote, reading Cursor MDC, Cline `.clinerules`, Codex AGENTS.md, Copilot `applyTo`, and more in their native shapes, plus MCP servers from `.claude`, `.cursor`, and friends on first run.
- Coding-plan and OAuth routes cover the subscription you may already pay (Anthropic, OpenAI Codex, GitHub Copilot, Kimi Code, GLM Coding Plan), alongside 60-plus raw providers and local Ollama, LM Studio, llama.cpp, and vLLM endpoints.

## Cautions

- Fork lineage is the structural risk: at 18.x against its parent's 1.1.x, omp is a permanently diverging codebase, and a re-merge is not a realistic plan.
- Subscription reuse carries terms-of-service risk: the launch thread's sharpest comment reports provider OAuth flows warning that only official tools may log in, so routing a paid plan through omp could violate the provider's terms.
- The benchmark table in the README is self-run, and launch-thread commenters questioned the evaluation rigor (one called the CI "benchmaxxing" incomplete); the surface is also large enough that reviewing what omp does is a project of its own.

## Pricing

Free and MIT-licensed.
There is no paid tier; usage flows through your own providers, subscriptions, or local servers, on their prices.

## Compared to

- [Pi](../pi/index.md): its parent, which keeps the core frozen and pushes features into extensions you can read in an afternoon; choose Pi for auditability, omp for the batteries.
- [Claude Code](../claude-code/index.md): the closed incumbent omp out-features on paper, with none of Anthropic's first-party model economics.
- [OpenCode](../opencode/index.md): the other big open terminal harness, provider-neutral like omp but without the LSP-first grounding.

## Bottom line

Recommended for power users who want IDE-grade diagnostics, debugger control, and heavy subagent fan-out in one terminal agent.
Not for anyone who needs a small core they can fully audit, and not for ToS-cautious subscription reuse until the provider OAuth question is settled.

## Changes

- 2026-10-10 - Created from the awesome-claude-code and GitHub topic scan, admitted as the batteries-included fork counterargument to the Pi column.

## See also

- [Pi](../pi/index.md) - the frozen-core parent whose minimalism omp exists to argue with
- [Claude Code](../claude-code/index.md) - the closed platform benchmark omp's feature table is measured against
- [OpenCode](../opencode/index.md) - the other large open harness in the same buyer's shortlist
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the capability comparison this column joins

## References

- https://omp.sh - the product site, install script, and the "IDE wired in" positioning
- https://api.github.com/repos/can1357/oh-my-pi - 34,842 stars, 3,791 forks, MIT, created 2025-12-31, pushed 2026-10-10, as of 2026-10-10
- https://api.github.com/repos/can1357/oh-my-pi/readme - the feature surface: 60-plus providers, LSP and DAP wiring, subagents, advisor, rules-format inheritance, local engines, and the provider list
- https://raw.githubusercontent.com/can1357/oh-my-pi/main/packages/coding-agent/CHANGELOG.md - the 18.8.7 release (2026-10-09) and the near-daily train behind the Status section
- https://registry.npmjs.org/@oh-my-pi/pi-coding-agent - npm distribution and the 18.8.7 latest tag
- https://hn.algolia.com/api/v1/items/48994611 - the 42-point launch thread, cited for the OAuth terms-of-service caution and the benchmark-rigor skepticism
