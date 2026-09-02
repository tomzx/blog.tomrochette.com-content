---
title: Paseo
created: 2026-08-30
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, parallel-agents, mobile, open-source]
readability: 3
audience_notes: >
  Engineers who run several coding agents and want to supervise them away from the desk.
  Assumes you know what a coding-agent CLI and an ACP adapter are.
---

Paseo is a free, open-source, self-hosted orchestration layer that runs coding agents as local processes on your own machines and drives them from desktop, web, mobile, and CLI clients over one daemon.
Facts below verified as of 2026-09-02.

**Paseo's differentiator is not parallelism, which is now table stakes, but reach: it is the only orchestrator in its class with native iOS and Android clients at full feature parity, wrapped around your existing agent subscriptions instead of replacing them.**

## What it is

A TypeScript daemon (`@getpaseo/cli` or Docker) manages agent processes, worktrees, schedules, and an E2E-encrypted relay for remote access; native iOS and Android apps, an Electron desktop app, a web PWA, and a CLI all connect to the same daemon.
It wraps each provider's own CLI rather than reimplementing it, so your subscriptions, configs, and MCP servers keep working.
Four native integrations (Claude Code, Codex, OpenCode, Pi) plus an in-app ACP catalog of roughly 36 more agents, including Cursor CLI, Gemini CLI, Goose, and Factory Droid.
No telemetry, no forced login, agents run locally; a Hub layer for GitHub, Slack, and Discord triggers and team access is self-hostable today.
Apache-2.0 (with a custom copyright notice), by Mohamed Boudra, an independent solo maintainer, with development supported by GitHub Sponsors.

## Status

Young and fast: 15,787 stars, 1,729 forks, 1,206 open issues as of 2026-09-02, created 2025-10-13, pushed the day of verification.
The 0.7 line reached stable while I watched: v0.7.0 shipped 2026-08-31 and v0.7.2 on 2026-09-02, with 165 contributors and an active subreddit and Discord.
**The structural risk is on the label: the maintainer described himself on Hacker News as a team of one, with monetization planned but not yet generally available.**

## Strengths

- Genuine cross-device supervision: phone steering of desktop agents over an encrypted relay, which no peer in the category ships.
- Broadest agent support in its class with minimal lock-in, because it wraps provider CLIs instead of replacing them.
- Privacy and self-host posture: local processes, optional encrypted relay, Docker for servers and NAS.
- More than a UI: CLI parity, a TypeScript SDK, an MCP server, schedules, and plugins.

## Cautions

- Pre-1.0 with fast churn, and a four-digit open-issue count that says demand is outrunning a tiny team.
- Subscription-billing friction: the maintainer confirmed Claude subscription usage through Paseo draws from a different, smaller credit pool than interactive use.
- Solo-maintainer bus factor with a business model still pending.
- Hacker News commenters noted it converges with Conductor, cmux, and Devin-style tools unless mobile-first steering is your actual need.

## Pricing

Free and open source under Apache-2.0; you bring your own agent CLIs, subscriptions, and API keys.
The hosted Hub (managed triggers and team access) is the intended commercial layer but is not generally available and registration is closed; self-hosting Hub works today.

## Compared to

- [Conductor](../conductor/index.md): polished, closed, macOS-only with cloud workspaces and commercial tiers; choose Conductor for hosted polish, Paseo for open source, Windows and Linux, and phones.
- [Vibe Kanban](../vibe-kanban/index.md): kanban-board fan-out for batch delegation, community-maintained since its vendor shut down; choose it for board thinking, Paseo for interactive conversation-steered sessions from anywhere.
- [Emdash](../emdash/index.md): a desktop-first parallel workbench from a YC team; choose Emdash for a VC-backed desktop IDE feel, Paseo when the phone and multi-machine daemons are the point.

## Bottom line

**Recommended for engineers whose agents run unattended while they are away from the desk, and who want self-hosted open source over a vendor's app.**
Not for teams needing a vendor's support contract, or Mac-only shops happy paying Conductor for polish.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Conductor](../conductor/index.md) - the commercial macOS counterpart
- [Vibe Kanban](../vibe-kanban/index.md) - the kanban-board alternative
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the supervision problem the category answers

## References

- https://github.com/getpaseo/paseo - repository, architecture, license, adoption numbers
- https://paseo.sh - product claims, platforms, privacy posture
- https://paseo.sh/docs/supported-providers - the native and ACP-catalog agent list
- https://paseo.sh/docs/hub/hosted - the commercial layer's status
- https://news.ycombinator.com/item?id=48377250 - the launch thread with the solo-maintainer statement and the credit-pool admission
- https://github.com/BloopAI/vibe-kanban - comparison data on the board alternative
