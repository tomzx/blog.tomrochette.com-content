---
title: Nanocoder
created: 2026-10-08
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, local-first, community-governance]
readability: 3
audience_notes: >
  Engineers choosing a terminal coding agent who want community ownership and local models,
  and anyone comparing the collective-governance bet against foundation and company governance.
  Assumes you know what BYOK, MCP, and AGENTS.md mean.
---

Nanocoder is the Nano Collective's open-source terminal coding agent: a BYOM, local-first agent built by a community collective rather than a company, with its feature surface (skills, subagents, hooks, MCP, cron through a daemon) mirroring the commercial harnesses.

**Nanocoder is the governance counter-bet: goose proved an agent can outlive its corporate parent by joining a foundation, and Nanocoder asks whether a sponsor-funded collective can build and own one from the start.**

## What it is

A TypeScript CLI installed by npm, Homebrew, or Nix flake (`@nanocollective/nanocoder`), running fullscreen or inline in the terminal, with `nanocoder review` for branch and PR review and an ACP server mode so Zed or its native VS Code sidebar extension can host it.
The extension surface is the modern harness set: five development modes (normal, auto-accept, yolo, plan, architect), an AGENTS.md written by `/init` and auto-loaded every session, skills as the unified extension model (commands, subagents, custom tools, and event triggers in one `.nanocoder/skills/` bundle format), lifecycle hooks that deny tool calls on non-zero exit, MCP servers, semantic memory, checkpointing, and an optional OS sandbox for shell commands.
Model access is the widest BYOK roster in this section: roughly 30 documented providers including OpenRouter, Anthropic, Google, Groq, Mistral, MiniMax, Requesty, Kimi Code, Z.ai, GitHub Copilot, and ChatGPT Codex device-code sign-in, plus seven local engines (Ollama, LM Studio, vLLM, llama.cpp, llama-swap, MLX, LocalAI), each with its own provider page.
It is made by the Nano Collective, a self-described home for privacy-first, local-first AI tools funded through sponsorships (Atlas Cloud is the named sponsor) rather than a company, and it ships sister projects (Nanotune for local fine-tuning, Roster and Sentinel in alpha).

## Status

**Active and healthy for its size, with a footprint that is easy to miss.**
The repository shows 2,502 stars and 343 forks, was created July 30, 2025, and was pushed the day of verification (GitHub API, as of 2026-10-08).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Nano-Collective/nanocoder&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Nano-Collective/nanocoder&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Nano-Collective/nanocoder&type=date&theme=dark&legend=top-left" />
</picture>

Releases run monthly on the v1.x line: v1.29.0 (July 26, 2026), v1.30.0 (August 26), and v1.31.0 (September 26, which added Anthropic prompt caching, auto titles, retry caps, and `.nanocoderignore`).
The npm package did 8,537 downloads in the last month (the API window covering September 5 to October 4, as of 2026-10-08).
The Hacker News footprint is near zero: a 1-point Show HN in August 2025 and a 1-point thread for the VS Code sidebar in July 2026, so its growth is word-of-mouth and search, not launch-thread gravity.

## Strengths

- **The governance story is distinctive and testable**: a collective that accepts outside projects, publishes its sponsor list, and owns no venture roadmap, one step more community-native than goose's foundation.
- Local models are first-class, not a compatibility checkbox: seven local engines documented, each with its own provider page, the longest local-engine list in this section.
- The skills model is a real design: one bundle format covering commands, subagents, tools, and cron and `file.changed` event subscriptions through a per-project daemon, after the standalone scheduler was deliberately removed.
- Hooks and modes match harness conventions (plan mode, auto-accept, yolo), so migrating in from Claude Code or Codex is configuration, not relearning.

## Cautions

- **The repo ships no LICENSE file, and GitHub detects no license, while the npm metadata declares MIT**, so pin your expectations from the package metadata and ask before embedding.
- Adoption is thin against its surface: 2.5k stars and 8.5k monthly npm downloads means the 30-provider roster and skills system rest on a small user base and its own documentation.
- No independent evaluation exists; its claims are its docs, and the near-zero discussion footprint means no critical source has stress-tested it yet.
- The collective depends on volunteer and sponsor capacity (one named sponsor), and its adjacent alpha projects (Roster, Sentinel) share the same maintainers.

## Pricing

Does not apply: the agent is free and open source under MIT (per the npm metadata), with no paid tiers and no hosted service; the collective funds itself through sponsorships.
You pay your own model provider, or nothing at all on local models, so no price history table applies.

## Compared to

- [goose](../goose/index.md): the other non-corporate-governance agent; goose has the Linux Foundation process, the Rust core, and the larger community, Nanocoder is more local-first and ships faster on harness features.
- [Zerostack](../zerostack/index.md): the other independent small-footprint bet; Zerostack is one maintainer and a RAM-floor thesis, Nanocoder is a collective and a governance thesis.
- [OpenCode](../opencode/index.md): the company-backed open harness with the large community; pick OpenCode for ecosystem gravity, Nanocoder when the ownership structure is the point.

## Bottom line

Recommended for privacy-minded engineers who want the full modern harness surface on their own hardware and prefer their tooling owned by no company.
Not for teams that need an audited, independently evaluated agent today, or anyone whose policy requires a repository license file to exist.
My disagreeable claim: governance is currently Nanocoder's only hard moat, and a collective with one sponsor and near-zero discussion has not yet proven governance is enough.

## Changes

- 2026-10-08 - Created from the harness entrant sweep, with the repository, README, docs, scheduler and ACP pages, npm registry and downloads, the collective site, and the Hacker News record fetched.

## See also

- [goose](../goose/index.md) - the foundation-governed comparison point on ownership
- [Zerostack](../zerostack/index.md) - the other independent harness built outside a company
- [OpenCode](../opencode/index.md) - the company-backed open harness it declines to be
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the capability rows this column joins

## References

- https://github.com/Nano-Collective/nanocoder - repository scale (2,502 stars, 343 forks), created 2025-07-30, pushed 2026-10-08, no LICENSE file detected (verified via the GitHub API)
- https://raw.githubusercontent.com/Nano-Collective/nanocoder/main/README.md - positioning, install paths, CLI flags, screen modes, and the review command
- https://raw.githubusercontent.com/Nano-Collective/nanocoder/main/docs/features/index.md - AGENTS.md via /init, the skills model, lifecycle hooks, and MCP servers
- https://raw.githubusercontent.com/Nano-Collective/nanocoder/main/docs/features/scheduler.md - the standalone scheduler's removal in favor of cron and file.changed skill subscriptions through the per-project daemon
- https://raw.githubusercontent.com/Nano-Collective/nanocoder/main/docs/features/acp.md - the ACP server mode for editor hosting
- https://raw.githubusercontent.com/Nano-Collective/nanocoder/main/docs/features/vscode-extension.md - the native VS Code sidebar extension over ACP
- https://raw.githubusercontent.com/Nano-Collective/nanocoder/main/docs/configuration/providers/ollama.md - the local-engine provider documentation pattern (seven local engines listed in the providers index)
- https://registry.npmjs.org/@nanocollective%2Fnanocoder - latest build 1.31.0 published 2026-09-26 and the MIT license declaration (verified via the registry API)
- https://api.npmjs.org/downloads/point/last-month/@nanocollective/nanocoder - 8,537 downloads, window September 5 to October 4, as of 2026-10-08
- https://github.com/Nano-Collective/nanocoder/releases - v1.29.0, v1.30.0, and v1.31.0 with publication dates (verified via the GitHub API)
- https://nanocollective.org - the collective's principles, sponsor list, project family, and contributor counts
- https://hn.algolia.com/api/v1/search?query=nanocoder&tags=story - the near-zero HN footprint (1-point threads of 2025-08-08 and 2026-07-31), cited as the adoption signal
- https://docs.nanocollective.org/nanocoder/docs - the docs hub (client-rendered shell on direct fetch; content taken from the repository docs)
