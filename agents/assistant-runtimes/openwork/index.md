---
title: OpenWork
created: 2026-08-30
updated: 2026-10-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtimes, cowork, desktop, open-source]
readability: 3
audience_notes: >
  Engineers and non-engineers choosing a desktop agent workspace as an open alternative to Claude Cowork.
  Assumes you know what OpenCode and MCP are.
---

OpenWork is a free, MIT-licensed desktop app for macOS, Windows, and Linux that runs AI agent sessions on local files with shared skills, MCP connections, browser automation, and scheduled tasks, positioned as the open alternative to Anthropic's Claude Cowork and built on top of OpenCode.

**OpenWork is the Cowork clone that outlived the clone jokes: seven and a half months of signed, weekly releases to 23.7k stars, an MCP gateway that makes its skills portable to any agent, and a license split that is the first thing a serious adopter should read.**

## What it is

An Electron desktop workspace for agent cowork sessions: chat on local files, install and run skills, automate Chrome, schedule tasks, and reuse capabilities across agents through the OpenWork MCP gateway (`search_capabilities` / `execute_capability`), so the same skills work from Claude Code, Codex, Cursor, or any MCP client.
It wraps OpenCode as its runtime, so any model OpenCode supports works, with BYO keys and local models; desktop mode keeps files local, and a web version plus an enterprise control plane (OpenWork Den: skill publishing, policies, SSO) round out the surface.
License is directory-split: MIT outside `ee/`, source-available subscription terms for the Den control plane (free up to five users, MIT after two years).
By different-ai (Benjamin Shafii), YC-backed.

## Status

Alive and shipping hard: 23,834 stars, 2,401 forks, 598 open issues and PRs as of 2026-10-04, created 2026-01-14, pushed 2026-10-03.
v0.18.42 on 2026-09-02 (signed Windows installers) through v0.18.54 on 2026-09-25, multiple releases per week, then v0.18.55 and v0.18.56 on 2026-10-03 after a week-long pause.
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

Free: $0, the MIT open-source desktop app with BYO keys, macOS, Windows, and Linux downloads, and the first 5 Cloud seats free at any team size, as of 2026-10-02.
Team: $10 per seat per month (everything in Free, unlimited users, SSO/SAML, the extension marketplace, distributed LLM keys, Cloud automations, basic usage analytics, standard support), as of 2026-10-02.
Enterprise: custom pricing on an annual contract with a 60-day opt-out (everything in Team plus SCIM provisioning, usage and adoption analytics, desktop policies and version controls, audit log and spend observability, internal white-labeling, and BYO inference self-hosted or private models), as of 2026-10-02, with no grandfather clause shown on the pricing page.
Two add-ons joined the page on 2026-09-29: OpenWork Cloud Computer at $50 per member per month, a browser-accessible cloud computer for each member, and OpenWork models at $10 per user per month, managed inference with no keys to bring, both available on Team and Enterprise.
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
| 2026-09-27 | All tiers | Ninth churn: free tier renamed Free with the first 5 Cloud seats free at any team size, team tier renamed Team at $10 per seat with unlimited users, Enterprise fixed at $20 per user per month billed annually, grandfather clause gone from the page | https://openworklabs.com/pricing |
| 2026-09-29 | Team, add-ons | Tenth churn: SSO/SAML moved from Enterprise into Team, and two add-ons introduced, Cloud Computer at $50 per member per month and managed OpenWork models at $10 per user per month; the three main tier prices unchanged | https://openworklabs.com/pricing |
| 2026-10-02 | Enterprise | Eleventh churn: Enterprise returned to custom pricing on an annual contract with a 60-day opt-out (the fixed $20 per user per month gone after three days); Free, Team, and both add-ons unchanged | https://openworklabs.com/pricing |

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
- 2026-09-22 - Recorded releases through v0.18.50 (2026-09-22), with refreshed adoption numbers and pricing re-checked unchanged for a second consecutive day.
- 2026-09-24 - Recorded releases through v0.18.52 (2026-09-24), with refreshed adoption numbers and pricing re-checked unchanged for a fourth consecutive day despite a pricing-presentation note in the v0.18.50 release notes.
- 2026-09-27 - Pricing churned a ninth time: the free tier is named Free with the first 5 Cloud seats free at any team size, the team tier is Team at $10 per seat with unlimited users, and Enterprise is fixed at $20 per user per month billed annually, with the grandfather clause gone from the page; releases through v0.18.54 (2026-09-25) recorded with refreshed adoption numbers.
- 2026-09-29 - Pricing churned a tenth time: SSO/SAML moved from Enterprise into Team, and the page gained two add-ons, Cloud Computer at $50 per member per month and managed OpenWork models at $10 per user per month, with the three main tier prices unchanged; refreshed adoption numbers.
- 2026-10-02 - Pricing churned an eleventh time: Enterprise returned to custom pricing on an annual contract with a 60-day opt-out, undoing the fixed $20 per user per month set on 2026-09-29; Free, Team, and both add-ons unchanged; refreshed adoption numbers.
- 2026-10-03 - Recorded releases resuming after a week: v0.18.55 and v0.18.56 (both 2026-10-03), ending v0.18.54's run as latest, with refreshed adoption numbers and pricing re-checked unchanged (Free $0, Team $10 per seat, Enterprise custom, both add-ons intact).

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
- https://api.github.com/repos/different-ai/openwork/releases - the release tags through v0.18.56 (2026-10-03, still latest as of 2026-10-04)
- https://github.com/different-ai/openwork/releases/tag/v0.18.42 - release cadence and installer signing
- https://news.ycombinator.com/item?id=46612494 - the launch thread with the security-boundary questions
