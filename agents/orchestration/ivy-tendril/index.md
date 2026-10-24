---
title: Ivy Tendril
created: 2026-10-24
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, agentic-development-environment, multi-agent, worktrees, source-available]
readability: 3
audience_notes: >
  Engineers choosing a plan-to-pull-request cockpit over the coding-agent CLIs
  they already run, who can weigh a young source-available vendor tool in the
  middle of a rewrite against MIT and Apache alternatives. Assumes you know git
  worktrees and run at least one agent CLI.
---

Ivy Tendril is a source-available, local-first desktop software factory from Stockholm's Ivy Interactive that turns a plan into reviewed pull requests by running your existing terminal coding agents in parallel git worktrees.

**Its bet is that the developer's job shifts to knowing what good looks like, so the tool's job is to plan, gate, and verify agent work instead of editing code.**

## What it is

Ivy Interactive AB, a Stockholm company founded in 2025 by Niels Bosma and Renco Smeding, positions Tendril as "the agentic software factory for 10x builders" that "replaces your IDE in an agentic era".
The desktop app (macOS, Windows, and Linux, built on the founders' own Ivy C# framework) runs a fixed lifecycle: you create a plan, agents draft implementations in parallel, each in an isolated git worktree, and nothing ships without your review, which the vendor counts as two human checkpoints plus automated verification gates.
It drives any terminal CLI agent and names Claude Code, Codex, GitHub Copilot CLI, Gemini, and OpenCode, and it ships official skills or plugins for VS Code and Copilot, Claude Code, Cursor, Codex, Gemini CLI, and Antigravity, plus its own VS Code extension.
An automated inbox ingests GitHub Issues or jam.dev bug reports through webhooks and turns them into plan-backed jobs, and Cloudflare Quick Tunnels expose the local server so you can steer runs from anywhere, including a phone.
Everything is local-first by design: code stays on your machine, and the only external calls are to the LLM API you configure and to GitHub.
A headless mode (`tendril --web`) runs the same engine as a local web server without the desktop UI.

## Status

Mid-rewrite and cooling: the C# main repository was created 2026-04-15, held 203 stars, 9 forks, and 173 open issues as of 2026-10-24, and has not been pushed since 2026-09-15, with the release train stopping at v1.2.4 on 2026-09-14 (GitHub API, as of 2026-10-24).
Development moved to Ivy-Tendril-V2, a TypeScript-and-Rust monorepo (Tauri desktop shell, React frontend, Axum server daemon, SQLite worktree engine, pnpm and Cargo workspaces) created 2026-09-14 and pushed 2026-09-23.
The V2 README says it is "a WIP upgrade of Tendril" and that the repo "will be deleted once we are done", and neither repository shows a push in the month to 2026-10-24, so the rewrite itself is quiet too.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Ivy-Interactive/Ivy-Tendril&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Ivy-Interactive/Ivy-Tendril&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Ivy-Interactive/Ivy-Tendril&type=date&legend=top-left" />
</picture>

The community footprint is the vendor plus silence: the exact-phrase HN search returns zero stories, the loose search returns only botanical and academic hits, and the only writing about Tendril outside its repository is the company's own 24-post blog, much of it a "Tendril versus" comparison wave.

## Strengths

- The plan-to-PR lifecycle is complete in one app: plans, parallel worktree drafts, diff review with approve, request-changes, or send-back actions, and verification gates before anything ships.
- Agent-agnostic and model-agnostic with bring-your-own keys, so the factory sits above the CLIs and model bills you already have.
- Local-first architecture (external calls only to your LLM API and GitHub) fits regulated and sovereignty-sensitive shops, and Enterprise adds on-prem hosting.
- Distribution is broad for a five-month-old tool: installers for all three desktops, a headless server mode, and skills or plugins across six agent ecosystems.
- The vendor eats its own cooking: v1 is built on Ivy-Framework, the founders' open-source .NET internal-tools framework.

## Cautions

- The documentation layer is broken as of 2026-10-24: both tendril.ivy.app and docs.ivy.app, the docs hosts the README badges and the vendor homepage link, fail DNS, so the repository and ivy.app are the only working sources.
- Zero independent coverage: no HN story, no third-party review or benchmark, so every performance and fit claim is a vendor claim.
- The product is mid-rewrite: v1 is quiet since 2026-09-15 and the V2 monorepo is silent since 2026-09-23 and promised for deletion, so neither branch is a stability bet today.
- FSL-1.1-ALv2 is source-available, not open source: competing use is restricted until each version's two-year Apache-2.0 conversion, and GitHub detects the license as NOASSERTION.
- The site sells engagements around the app (Boardroom Briefing, Move Faster Package, Full Implementation), an enterprise-services motion wrapped around a single-user free tier.

## Pricing

Free at $0 per user per month for a single user, Pro at $59 per user per month (20 percent off with annual billing) adding marketplace integrations, AI plan triage, and advanced verifications, and Enterprise at custom pricing with multi-tenant, on-prem, and SSO/SAML (as of 2026-10-24).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-24 | Free | introduced at $0 per user/month at note creation | https://ivy.app/pricing |
| 2026-10-24 | Pro | listed at $59 per user/month, 20 percent annual-billing discount | https://ivy.app/pricing |
| 2026-10-24 | Enterprise | custom pricing, contact sales | https://ivy.app/pricing |

## Compared to

- [Conductor](../conductor/index.md): the polished closed macOS session manager covers the same review-gated parallel loop for Claude Code and Codex, while Tendril is cross-platform, source-available, and adds the plan lifecycle and verification gates.
- [Agent Swarm](../agent-swarm/index.md): the MIT self-hosted lead/worker platform turns the same issue-to-PR intake into Docker-isolated workers, where Tendril keeps the loop on your desktop behind human gates.
- [Agent Orchestrator](../agent-orchestrator/index.md): the Apache-2.0 kanban drives 26-plus CLIs at 13.2k stars with looser gates, the volume alternative to Tendril's tighter, smaller factory.

## Bottom line

Recommended for a developer or small team who wants plan-to-pull-request discipline over the CLI agents they already run, especially on Windows or in sovereignty-sensitive settings, and who will accept a young source-available tool in the middle of a rewrite.
Not for anyone needing an OSI open-source license, working documentation links, or independent evidence today.

## Changes

- 2026-10-24 - Created.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Conductor](../conductor/index.md) - the closed macOS seat Tendril's review-gated loop most resembles
- [Agent Swarm](../agent-swarm/index.md) - the MIT issue-to-PR platform alternative
- [Agent Orchestrator](../agent-orchestrator/index.md) - the high-volume open kanban alternative

## References

- https://api.github.com/repos/Ivy-Interactive/Ivy-Tendril - repository, license detection, counts, and dates (as of 2026-10-24)
- https://raw.githubusercontent.com/Ivy-Interactive/Ivy-Tendril/development/README.md - the feature table, agent list, skills catalog, and FSL notice
- https://api.github.com/repos/Ivy-Interactive/Ivy-Tendril/releases?per_page=5 - the release train ending at v1.2.4 (2026-09-14)
- https://raw.githubusercontent.com/Ivy-Interactive/Ivy-Tendril/development/LICENSE - the FSL-1.1-ALv2 terms and the two-year Apache-2.0 conversion
- https://raw.githubusercontent.com/Ivy-Interactive/Ivy-Tendril/main/LICENSE - the same license on the main branch
- https://api.github.com/repos/Ivy-Interactive/Ivy-Tendril-V2 - the V2 monorepo's dates, stack, and WIP positioning (as of 2026-10-24)
- https://raw.githubusercontent.com/Ivy-Interactive/Ivy-Tendril-V2/development/README.md - the Tauri, React, and Rust layout and the delete-when-done notice
- https://ivy.app - the plan-draft-review lifecycle, the sovereignty claims, and the engagement FAQ
- https://ivy.app/pricing - the Free, Pro $59, and Enterprise tiers (as of 2026-10-24)
- https://ivy.app/llms.txt - the company facts, founders, and the use-and-do-not-use guidance
- https://hn.algolia.com/api/v1/search?query=%22Ivy+Tendril%22&hitsPerPage=10 - the zero-story HN footprint
