---
title: OpenWork
created: 2026-08-30
updated: 2026-09-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtimes, cowork, desktop, open-source]
readability: 3
audience_notes: >
  Engineers and non-engineers choosing a desktop agent workspace as an open alternative to Claude Cowork.
  Assumes you know what OpenCode and MCP are.
---

OpenWork is a free, MIT-licensed desktop app for macOS, Windows, and Linux that runs AI agent sessions on local files with shared skills, MCP connections, browser automation, and scheduled tasks, positioned as the open alternative to Anthropic's Claude Cowork and built on top of OpenCode.
Facts below verified as of 2026-09-21.

**OpenWork is the Cowork clone that outlived the clone jokes: seven and a half months of signed, weekly releases to 23.7k stars, an MCP gateway that makes its skills portable to any agent, and a license split that is the first thing a serious adopter should read.**

## What it is

An Electron desktop workspace for agent cowork sessions: chat on local files, install and run skills, automate Chrome, schedule tasks, and reuse capabilities across agents through the OpenWork MCP gateway (`search_capabilities` / `execute_capability`), so the same skills work from Claude Code, Codex, Cursor, or any MCP client.
It wraps OpenCode as its runtime, so any model OpenCode supports works, with BYO keys and local models; desktop mode keeps files local, and a web version plus an enterprise control plane (OpenWork Den: skill publishing, policies, SSO) round out the surface.
License is directory-split: MIT outside `ee/`, source-available subscription terms for the Den control plane (free up to five users, MIT after two years).
By different-ai (Benjamin Shafii), YC-backed.

## Status

Alive and shipping hard: 23,682 stars, 2,380 forks, 521 open issues and PRs as of 2026-09-21, created 2026-01-14, pushed today.
v0.18.42 on 2026-09-02 (signed Windows installers) through v0.18.48 on 2026-09-15, multiple releases per week.
**It outlived its launch-week skepticism, but the founder still carries 2,911 of the top contributors' roughly 4,000 commits.**

## Strengths

- Genuine open core with BYO providers and no hosted lock-in for the desktop app.
- The MCP gateway is the real differentiator: capabilities invest once and work from every agent your team runs.
- Extreme velocity with evals, CI hardening, and signed installers.
- A real enterprise path (Den) without abandoning the MIT core.

## Cautions

- Not uniformly open source: the Den control plane is subscription-gated for production beyond five users, and the repo launched with all rights reserved before MIT landed the same day.
- HN-raised security questions were never fully resolved in public: no VM or sandbox boundary between agent and filesystem, and unversioned file edits, treat it like running Claude Code with broad permissions.
- Single-dominant-maintainer risk.
- v0.x software that launched as very alpha, with the macOS notarization status unverified.

## Pricing

Free (Solo): $0 forever, the MIT open-source desktop app with BYO keys, macOS and Linux downloads, no user cap stated on the pricing page, as of 2026-09-21.
Team Starter: $10 per seat per month with the first 5 seats free (API access, extension marketplace, distributed LLM keys), as of 2026-09-21.
Enterprise: custom pricing (everything in Team Starter plus SSO/SAML and SCIM, BYO inference with self-hosted or private models, desktop policies and version controls, managed deployment self-hosted or hosted, custom skill development and MCP consulting, rollout support), as of 2026-09-21, with existing organizations already using SSO or desktop policies grandfathered at full access.
The Den control plane inside the repo stays free for organizations up to five users, free to evaluate for 30 days at any size, and each `ee/` release converts to MIT two years after publication.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-02 | All tiers | First recorded state: Free up to 5 users, Team $20 per seat, Enterprise $50 | https://openworklabs.com/pricing |
| 2026-09-05 | All tiers | Solo $0, Team Starter $10 per seat, Enterprise custom | https://openworklabs.com/pricing |
| 2026-09-07 | All tiers | Enterprise to $40 per user per month, Team Starter renamed to Team | https://openworklabs.com/pricing |
| 2026-09-09 | All tiers | Team $10 per seat up to 100 users, Enterprise $40 per user per month | https://openworklabs.com/pricing |
| 2026-09-12 | Enterprise | Enterprise back to custom pricing, per-user price and user caps dropped | https://openworklabs.com/pricing |
| 2026-09-16 | All tiers | Free tier named Solo, team tier back to Team Starter at $10 per seat with the first 5 seats free | https://openworklabs.com/pricing |
| 2026-09-20 | All tiers | Free tier back to Free at $0 up to 5 users, Team $10 per seat up to 100 users, Enterprise back to $40 per user per month | https://openworklabs.com/pricing |
| 2026-09-21 | All tiers | Free tier renamed Solo (free forever, no user cap stated), Team Starter $10 per seat with the first 5 seats free, Enterprise back to custom pricing with the grandfather clause restored for existing SSO and desktop-policy organizations | https://openworklabs.com/pricing |

## Compared to

- Claude Cowork: polished, closed, subscription-tied with managed security, and as of 2026-09-16 merging into Claude chat itself, which narrows the workflow gap OpenWork was built for; choose OpenWork for parity workflows without vendor or model lock-in.
- [Superset](../../orchestration/superset/index.md): the developer-IDE side of the same open wave; choose Superset for coding workflows, OpenWork for files-and-skills knowledge work beyond code.
- [Eigent](../eigent/index.md): the multi-agent workforce desktop; choose OpenWork for the OpenCode ecosystem and MCP portability, Eigent for visual multi-agent teams.

## Bottom line

**Recommended for mixed technical and non-technical teams that want Cowork-style agent work on their own machines and models, with skills that port across every agent they run.**
Not for teams that need a sandboxed security boundary the product does not provide, or uniform open-source licensing including the enterprise tier.

## Changes

- 2026-08-30 - Created in the Assistant runtimes category, recording the OpenCode-based Cowork alternative with license-split and security-boundary cautions.
- 2026-09-02 - Updated pricing: Free up to 5 users, Team $20 per seat, Enterprise $50.
- 2026-09-05 - Updated pricing again: Solo free, Team Starter $10 per seat, Enterprise custom.
- 2026-09-07 - Recorded Enterprise moving to $40 per user per month and Team Starter renamed to Team.
- 2026-09-09 - Updated pricing again: Team $10 per seat up to 100 users, Enterprise $40 per user per month.
- 2026-09-12 - Dropped the $40 per user and 100-user caps, moving Enterprise back to custom pricing.
- 2026-09-16 - Pricing page churned again: the free tier is named Solo and the paid team tier is back to Team Starter at $10 per seat with the first 5 seats free; releases through v0.18.48 recorded.
- 2026-09-18 - Recorded Claude Cowork merging into Claude chat itself (announced 2026-09-16), updating the comparison baseline; pricing re-checked unchanged.
- 2026-09-20 - Pricing churned a seventh time: the free tier is named Free and capped at 5 users, Team is $10 per seat up to 100 users, and Enterprise returned to $40 per user per month, the grandfather clause is gone from the pricing page, and a Price history table now records the full churn.
- 2026-09-21 - Pricing churned an eighth time: the free tier is renamed Solo (free forever, no user cap stated), the team tier is Team Starter at $10 per seat with the first 5 seats free, and Enterprise returned to custom pricing with the grandfather clause restored.

## See also

- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the category comparison this note joins
- [OpenCode](../../harnesses/opencode/index.md) - the runtime it wraps
- [Eigent](../eigent/index.md) - the multi-agent counterpart
- [Paperclip](../../control-planes/paperclip/index.md) - the control-plane layer above teams of these

## References

- https://github.com/different-ai/openwork - repository, description, license, adoption numbers
- https://raw.githubusercontent.com/different-ai/openwork/HEAD/README.md - the directory-split licensing terms and gateway
- https://openworklabs.com - product scope and the built-on-OpenCode positioning
- https://openworklabs.com/pricing - the tiers for the pricing rows
- https://github.com/different-ai/openwork/releases/tag/v0.18.42 - release cadence and installer signing
- https://news.ycombinator.com/item?id=46612494 - the launch thread with the security-boundary questions
