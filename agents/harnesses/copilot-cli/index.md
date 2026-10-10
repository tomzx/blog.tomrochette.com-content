---
title: Copilot CLI
created: 2026-10-05
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, github, microsoft, terminal]
readability: 3
audience_notes: >
  Engineers choosing a terminal coding agent, especially ones already holding a Copilot seat or living inside GitHub's ecosystem.
  Assumes you know what MCP, ACP, and a subscription credit meter are.
---

Copilot CLI is GitHub's terminal coding agent: a proprietary `copilot` command that runs the Copilot agent interactively or headlessly, included in every Copilot plan from the Free tier up.

**Copilot CLI is the default harness of the world's largest developer platform, and its differentiator is not capability but adjacency: it is the only harness that drives GitHub.com (issues, pull requests, Actions workflows) as a first-party citizen, now with preview support for delegating to its own rivals.**

## What it is

An interactive TUI with a default ask/execute mode and a plan mode (Shift+Tab), plus steering through queued follow-up messages and inline feedback when you reject a tool call.
The programmatic form is `copilot -p` with `--allow-tool`, `--deny-tool`, and `--allow-all-tools` flags scoping what runs unattended.
The feature surface is platform-class: MCP servers, combined custom instruction files, custom agents it delegates common tasks to, hooks, skills, Copilot Memory for repository facts, computer use on macOS and Windows local sessions, and automatic compaction at 95 percent of the context window.
First-party sandboxing is built in and in public preview: local sandboxing via `/sandbox enable`, and whole cloud-hosted sessions via `copilot --cloud` that inherit Copilot cloud-agent firewall policies.
Models are a multi-vendor roster (Claude through Opus 5.5 and Fable 5.1, GPT-6.x, Gemini 3.8 Flash, Grok 4.7, Kimi K3, and Microsoft's MAI), selected with `/model` and metered in GitHub AI Credits, with 1M-token context and reasoning levels on supported models.
BYOW works through environment variables (`COPILOT_PROVIDER_*`) for any OpenAI-compatible endpoint including Ollama and vLLM, plus Azure and Anthropic, provided the model supports tool calling and streaming.
An ACP server lets ACP-speaking editors host it, and GitHub's own plans page lists Zed as a destination.
Distribution is npm (`@github/copilot`), a Homebrew cask, WinGet, an install script, and direct downloads; the `github/copilot-cli` repository hosts releases and documentation, not source.

## Status

**Active and enormous in distribution.**
Public preview launched September 25, 2025, and general availability followed on February 25, 2026.
The npm package's latest build is 1.0.94 (published October 8, 2026, with a 1.0.95 prerelease train publishing behind it), and it did 6,784,821 downloads in the last month (the API window covering September 8 to October 7, as of 2026-10-09), among the largest npm install bases of any harness in this section.
The `github/copilot-cli` repository shows 11,249 stars as of 2026-10-09 (GitHub API), and it is a distribution and issues repository, with no open-source license.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=github/copilot-cli&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=github/copilot-cli&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=github/copilot-cli&type=date&legend=top-left" />
</picture>

Community discussion is thinner than the install count would suggest: the public-preview launch thread drew 24 points, and the general-availability thread 7, which I read as distribution through Copilot seats rather than terminal-community gravity.

## Strengths

- **First-party GitHub.com reach**: work issues, raise and merge pull requests, and create Actions workflows from the terminal, authenticated as you.
- Zero marginal cost for existing Copilot seats, including the Free tier, which no other major-lab harness matches.
- Local and cloud sandboxes are first-party rather than a container exercise, though both are preview.
- Pro+ and Max plans can delegate tasks to third-party coding agents such as Claude and Codex from the cloud agent (preview), an unusual hedge for a first-party agent to ship.

## Cautions

- **The auto-approval risk is not hypothetical**: a February 2026 Hacker News thread showed Copilot CLI downloading and executing malware (62 points), the concrete form of the danger the docs' own security section describes.
- Community guidance responded by wrapping it in Docker sandboxes; a "paranoid guide" to exactly that drew 59 points in November 2025.
- The client is closed, the repository carries no open-source license, and the vendor's own docs flag trusted-directory scoping as heuristic.
- Cloud and local sandboxing are both public preview and subject to change, so the safety story is still moving.
- AI Credits consumption varies by model, context size, and reasoning level, which makes subscription budgeting less predictable than a flat plan.

## Pricing

Included in GitHub Copilot plans as of 2026-10-05: Free $0 with limited usage, Pro $10/month, Pro+ $39/month, and Max $100/month, all including Copilot CLI and metered through GitHub AI Credits (a base credit allotment plus a flex allotment per plan).
Organizations have Business and Enterprise tiers, which the docs reference for content exclusion and policy controls, though the fetched plans page prices only the individual ladder.
Bringing your own provider through the environment variables bypasses GitHub's model billing for those requests.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-05 | Individual plans | Baseline: CLI included from the Free plan up, metered in GitHub AI Credits; Pro $10/mo, Pro+ $39/mo, Max $100/mo. | [github.com/features/copilot/plans](https://github.com/features/copilot/plans) |

## Compared to

- [Claude Code](../claude-code/index.md): the subscription-platform rival with the deeper operations layer; Copilot CLI trades that depth for GitHub adjacency, a multi-model roster, and a free tier.
- [Codex](../codex/index.md): the other big-org terminal agent, but Apache-2.0 and auditable; choose it when the client's openness matters more than GitHub integration.
- [Warp Agent CLI](../warp-agent-cli/index.md): the other multi-model, credit-metered terminal agent from an incumbent vendor; Warp sells orchestration, GitHub sells the platform you already commit to.

## Bottom line

**Recommended for anyone already holding a Copilot seat: it is the zero-decision default, and the GitHub.com reach is the part no rival can copy.**
Not for teams with open-client mandates, and not for untrusted repositories until the sandboxes leave preview and the approval model is treated with the respect the malware thread earned.

## Changes

- 2026-10-05 - Created from the same-day entrant scan, with the docs, plans page, npm registry, repository, and Hacker News record fetched.
- 2026-10-07 - Added the github/copilot-cli star history chart to the Status section.
- 2026-10-08 - Recorded the npm build moving to 1.0.93 (published October 7) and refreshed repository counters.
- 2026-10-09 - Recorded the npm build train reaching 1.0.94 (October 8, with a 1.0.95 prerelease train publishing behind it) and refreshed download and repository counters.

## See also

- [Claude Code](../claude-code/index.md) - the platform rival it distributes against
- [Codex](../codex/index.md) - the open-client alternative from a comparably large vendor
- [Warp Agent CLI](../warp-agent-cli/index.md) - the other incumbent-vendor credit-metered CLI
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the capability rows this column joins
- [ACP](../../protocols/acp/index.md) - the protocol that lets editors host this agent

## References

- https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli - modes, sandboxing, MCP, hooks, skills, memory, BYOK providers, and security guidance (fetched 2026-10-05)
- https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli - install paths, subscription prerequisite, and token authentication (fetched 2026-10-05)
- https://github.com/features/copilot/plans - plan prices, AI Credits structure, model roster, and third-party delegation gating, as of 2026-10-05
- https://github.com/github/copilot-cli - distribution repository, 11,249 stars, no open-source license, as of 2026-10-09 (verified via the GitHub API)
- https://registry.npmjs.org/@github%2Fcopilot - latest build 1.0.94 published 2026-10-08, package created 2025-09-25 (verified via the registry API)
- https://api.npmjs.org/downloads/point/last-month/@github/copilot - 6,784,821 downloads, window September 8 to October 7, as of 2026-10-09
- https://hn.algolia.com/api/v1/items/47183940 - the February 27, 2026 malware-execution thread, 62 points (verified via the Algolia API)
- https://hn.algolia.com/api/v1/items/45810658 - the November 2025 Docker-sandboxing guide thread, 59 points
- https://hn.algolia.com/api/v1/items/45377734 - the September 25, 2025 public-preview launch thread, 24 points
- https://hn.algolia.com/api/v1/items/47155959 - the February 25, 2026 general-availability thread, 7 points
