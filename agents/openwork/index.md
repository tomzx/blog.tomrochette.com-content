---
title: OpenWork
created: 2026-08-30
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, assistant-runtimes, cowork, desktop, open-source]
readability: 3
audience_notes: >
  Engineers and non-engineers choosing a desktop agent workspace as an open alternative to Claude Cowork.
  Assumes you know what OpenCode and MCP are.
---

OpenWork is a free, MIT-licensed desktop app for macOS, Windows, and Linux that runs AI agent sessions on local files with shared skills, MCP connections, browser automation, and scheduled tasks, positioned as the open alternative to Anthropic's Claude Cowork and built on top of OpenCode.
Facts below verified as of 2026-09-04.

**OpenWork is the Cowork clone that outlived the clone jokes: seven and a half months of signed, weekly releases to 23k stars, an MCP gateway that makes its skills portable to any agent, and a license split that is the first thing a serious adopter should read.**

## What it is

An Electron desktop workspace for agent cowork sessions: chat on local files, install and run skills, automate Chrome, schedule tasks, and reuse capabilities across agents through the OpenWork MCP gateway (`search_capabilities` / `execute_capability`), so the same skills work from Claude Code, Codex, Cursor, or any MCP client.
It wraps OpenCode as its runtime, so any model OpenCode supports works, with BYO keys and local models; desktop mode keeps files local, and a web version plus an enterprise control plane (OpenWork Den: skill publishing, policies, SSO) round out the surface.
License is directory-split: MIT outside `ee/`, source-available subscription terms for the Den control plane (free up to five users, MIT after two years).
By different-ai (Benjamin Shafii), YC-backed.

## Status

Alive and shipping hard: 23,270 stars, 2,312 forks, 431 open issues and PRs as of 2026-09-02, created 2026-01-14, pushed the day of verification.
v0.18.41 on 2026-09-02 with signed Windows installers, multiple releases per week.
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

Free up to five users: the MIT desktop app, self-hosting the full platform including the Den control plane, BYO keys.
Team: $20 per seat per month for up to 100 users (marketplace, distributed keys, standard support), billed monthly.
Enterprise: $50 per user per month (SSO/SAML, SCIM, analytics, desktop policies, white-labeling, self-hosted inference, SLA), volume pricing above 100 users.

## Compared to

- Claude Cowork: polished, closed, subscription-tied with managed security; choose OpenWork for parity workflows without vendor or model lock-in.
- [Superset](../superset/index.md): the developer-IDE side of the same open wave; choose Superset for coding workflows, OpenWork for files-and-skills knowledge work beyond code.
- [Eigent](../eigent/index.md): the multi-agent workforce desktop; choose OpenWork for the OpenCode ecosystem and MCP portability, Eigent for visual multi-agent teams.

## Bottom line

**Recommended for mixed technical and non-technical teams that want Cowork-style agent work on their own machines and models, with skills that port across every agent they run.**
Not for teams that need a sandboxed security boundary the product does not provide, or uniform open-source licensing including the enterprise tier.

## See also

- [Assistant Runtimes Feature Matrix](../assistant-runtimes-feature-matrix/index.md) - the category comparison this note joins
- [OpenCode](../opencode/index.md) - the runtime it wraps
- [Eigent](../eigent/index.md) - the multi-agent counterpart
- [Paperclip](../paperclip/index.md) - the control-plane layer above teams of these

## References

- https://github.com/different-ai/openwork - repository, description, license, adoption numbers
- https://raw.githubusercontent.com/different-ai/openwork/HEAD/README.md - the directory-split licensing terms and gateway
- https://openworklabs.com - product scope and the built-on-OpenCode positioning
- https://openworklabs.com/pricing - the tiers for the pricing rows
- https://github.com/different-ai/openwork/releases/tag/v0.18.41 - release cadence and installer signing
- https://news.ycombinator.com/item?id=46612494 - the launch thread with the security-boundary questions
