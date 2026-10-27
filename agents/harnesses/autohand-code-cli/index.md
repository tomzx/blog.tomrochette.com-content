---
title: Autohand Code CLI
created: 2026-10-27
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, typescript, bun, byok, local-models]
readability: 3
audience_notes: >
  Engineers who want Claude Code's terminal-agent form factor as an open client they can run on
  their own keys or local models, and who can tolerate a prerelease from a small vendor.
  Assumes you know what BYOK, MCP, ACP, and a git worktree are.
---

Autohand Code CLI is an Apache-2.0 terminal coding agent from Autohand AI LLC, written in TypeScript on Bun, that imports your Claude Code setup and adds cost-capped autonomous loops and process-based agent teams.

**Autohand Code CLI is the discipline bet: its auto mode runs a task in its own git worktree under iteration, runtime, and dollar caps with a circuit breaker, and its agent teams are separate processes with task dependencies, not prompt theater.**

## What it is

A terminal-native agent (`autohand`, also installed as `autohand-code`, `agent`, and `ah`) with an interactive Ink REPL, one-shot `autohand -p` command mode, JSON streaming for scripts, and an ACP mode for editors.
It reads AGENTS.md natively (`/init` writes one), plans read-only before editing, carries 40-plus tools including `semantic_search`, `save_memory`, and `recall_memory`, and speaks MCP (client side, with a curated registry) and ACP.
Skills come in Claude and Codex formats from local directories or the vendor's community registry, and `/import` pulls settings from Claude, Codex, Gemini, Cursor, OpenCode, Kimi, and Grok.
Around the CLI sit a VS Code extension, Zed and JetBrains hosting over ACP, a Chrome extension, an iOS pairing app, a local Squad app for agent teams, and SDKs in nine-plus languages.
Providers split three ways: the vendor's hosted models (its own small Fantail and Moa plus GPT-6 Sol, Grok 4.7, GPT-5.6 Luna, DeepSeek V4 Flash, Qwen 3.8 Max, and Gemini 4 Argon on paid plans), BYOK (OpenRouter, LLMGateway, OpenAI, Bedrock, DeepSeek, Azure Foundry, Z.ai), or local Ollama, llama.cpp, and MLX.
Auto mode works a task on its own branch in a separate worktree, commits checkpoints, and stops on iteration limits (default 50), a runtime cap (default 120 minutes), a cost cap (default $10), or a circuit breaker when it stops making progress.

## Status

**Active, prerelease, and almost without an independent footprint.**
The repository was created December 12, 2025 and shows 211 stars and 37 forks as of 2026-10-27 (GitHub API), with 3,250 commits and a push on the day of verification; GitHub releases are 0.9.9-alpha hashes (the newest published October 23, 2026) and the npm package `autohand-cli` sits at latest 0.9.8 with the alpha train behind it.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=autohandai/code-cli&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=autohandai/code-cli&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=autohandai/code-cli&type=date&theme=dark&legend=top-left" />
</picture>

The changelog queues persistent goals as default-on for 0.9.9 and redefines `-c` to mean `--continue` as a breaking change.
Every Hacker News trace is the vendor's own: an "Intent Weaving" post at 22 points in October 2025, a Fantail small-model Show HN and the repo itself at 1 to 2 points, and no third-party coverage found as of 2026-10-27, which I read as the missing-signal signal for a ten-month-old tool.

## Strengths

- **Autonomy with a governor**: iteration, runtime, and dollar caps with checkpoint commits and a circuit breaker make the unattended loop a bounded spend decision, which most harnesses leave to your own discipline.
- Agent teams are processes, not personas: a lead agent delegates to up to five teammates with task dependencies, and a crashed teammate fails its task visibly instead of silently.
- The open-client surface is complete for a 0.9: AGENTS.md, MCP, ACP, hooks, skills in two formats, worktree isolation, and a plan mode that requires explicit acceptance even under `--yes`.
- Pipe mode with `--json local` and `--output-schema` treats the agent as a composable Unix component.
- The wrapper surface is unusually broad for the star count: nine-plus SDK languages, iOS pairing with squash-merge safeguards, and a Chrome extension.

## Cautions

- **The installers replace any existing `agent` command on your PATH, across every writable PATH directory, with no prompt**, the README's own disclosure; if another tool owns `agent`, Autohand takes it.
- Closed-source companions ride inside the open installers: `ahtraces`, a trace monitor built from private source with consent-gated cloud upload to the vendor's console, plus a bundled Zit binary and a Computer Use wrapper over the MIT Cua engine.
- **The Apache-2.0 grant carries a string**: organizations with annual recurring revenue over $5 million need a paid commercial license, which fails procurement policies that require a pure OSI license.
- Prerelease churn continues: 0.9.x with a queued breaking `-c` redefinition and default flags flipping between versions.
- The site's testimonials from engineers at Grab, Mercari, Razorpay, Notion, and Rocket Lab, and its SOC 2 claim, are unverifiable from anywhere independent, and the HN record shows no adoption discussion at all.
- Cloud sandboxes (Cloudflare-hosted, paid tiers) are temporary environments you must export from before they expire.

## Pricing

The CLI is free and open source, and BYOK or local usage never consumes credits on any plan.
Hosted plans as of 2026-10-27: Free $0 (Fantail only, 15 credits per rolling 5-hour window, 100 per month), Lite $6/month, Pro $20/month, Pro+ $59/month, Max $200/month, Team $59/seat/month, and Enterprise $119/seat/month; every hosted model costs one credit per successful response regardless of tier, paid annual runs 10 percent off, and cloud sandboxes start at Pro (4 concurrent) and cap at Max (10).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-27 | All plans | Baseline: CLI free (Apache-2.0 with the ARR-over-$5M commercial clause); hosted Free $0, Lite $6/mo, Pro $20/mo, Pro+ $59/mo, Max $200/mo, Team $59/seat/mo, Enterprise $119/seat/mo; one credit per hosted response; BYOK never metered. | [autohand.ai/code/pricing](https://autohand.ai/code/pricing/) |

## Compared to

- [Claude Code](../claude-code/index.md): the setup Autohand imports and the subscription ladder it undercuts; pick Claude Code for the mature platform and ecosystem, Autohand for the same form factor as an open client with BYOK, local models, and a cheaper hosted entry.
- [OpenCode](../opencode/index.md): the other open, provider-neutral terminal harness; OpenCode brings years of community and plugins, Autohand the cost-capped auto mode, process-based teams, and hosted small models.
- [Codex](../codex/index.md): the big-lab subscription CLI with a similarly free entry; Codex is Apache-2.0 with no revenue clause and a lab behind it, Autohand a startup prerelease with one.

## Bottom line

Recommended for terminal-first engineers who want Claude Code's workflow on their own keys or local models and will treat the dollar-capped auto mode as the product, eyes open about the installer defaults and the ARR clause.
Not for organizations needing an unmodified Apache-2.0 story, and not for anyone who requires independent evaluation before trusting a prerelease with their repository.

## Changes

- 2026-10-27 - Created from the context-engines scanner's handoff (Meirtz list), resolving the entrant with the repository, GitHub API, npm registry, product site, pricing page, commercial license, changelog, and the Hacker News footprint record all fetched in this run.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the capability column this note adds
- [Claude Code](../claude-code/index.md) - the incumbent whose setup this client imports
- [OpenCode](../opencode/index.md) - the open provider-neutral harness it most resembles
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where this lands in the harness layer

## References

- https://github.com/autohandai/code-cli - repository and README: feature surface, installer behaviors including the PATH `agent` takeover, provider table, skills and tools (fetched 2026-10-27)
- https://api.github.com/repos/autohandai/code-cli - created 2025-12-12, 211 stars, 37 forks, Apache-2.0, 3,250 commits, pushed 2026-10-27 (GitHub API, as of 2026-10-27)
- https://api.github.com/repos/autohandai/code-cli/releases?per_page=3 - the 0.9.9-alpha prerelease train, newest published 2026-10-23 (GitHub API, as of 2026-10-27)
- https://registry.npmjs.org/autohand-cli - npm distribution: latest 0.9.8, alpha prereleases, package created 2025-12-17 (registry API, as of 2026-10-27)
- https://www.autohand.ai/code/ - product surface, hosted model roster, surfaces, testimonials, and the SOC 2 claim (fetched 2026-10-27)
- https://autohand.ai/code/pricing/ - the plan ladder, credit mechanics, BYOK exemption, and cloud-sandbox tiers, as of 2026-10-27
- https://raw.githubusercontent.com/autohandai/code-cli/main/COMMERCIAL.md - the commercial-license requirement for organizations over $5M ARR
- https://raw.githubusercontent.com/autohandai/code-cli/main/CHANGELOG.md - the 0.9.9 queued defaults: goals on, `-c` redefined as `--continue`
- https://hn.algolia.com/api/v1/search?query=autohand&tags=story - the vendor-submitted, near-zero-traction Hacker News record, searched 2026-10-27
