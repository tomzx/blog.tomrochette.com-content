---
title: Superset
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, parallel-agents, ide, worktrees]
readability: 3
audience_notes: >
  Engineers on macOS choosing an app to run many coding agents in parallel with their own subscriptions.
  Assumes you know what a git worktree and a CLI coding agent are.
---

Superset is a source-available, YC-backed agentic IDE that runs many CLI coding agents in parallel, each in its own isolated git worktree, using the subscriptions you already pay for.
Facts below verified as of 2026-08-30.

**Superset's bet is that the orchestrator should be a terminal-first IDE that touches no SDK, so any agent works today and a new harness works the day it ships, and its free-forever local core under an Elastic License is the price wedge against Conductor.**

## What it is

An Electron desktop app that gives every task an isolated worktree with its own branch, terminal, environment, and detected ports, plus a built-in terminal with sessions that survive restarts (a background daemon keeps them alive), a diff viewer and editor, per-workspace browser previews, scheduled automations, and beta remote workspaces.
It is agent-agnostic and terminal-first, deliberately built on no vendor SDK: presets exist for Claude Code, Codex, Cursor Agent, Gemini CLI, OpenCode, Amp, Copilot, Grok, Droid, Kimi, Kiro, and Antigravity, and any CLI agent works without configuration.
A standalone CLI, a TypeScript SDK, and an MCP server let humans and other agents drive it; iOS is coming.
macOS is the primary platform, Linux is experimental, Windows has no build.
Elastic License 2.0 (source-available, not OSI open source), by Superset Inc., three ex-YC-company CTOs, YC P26, $11M raised.

## Status

Fast and funded: 13,498 stars, 1,228 forks, roughly 577 open issues and PRs as of 2026-08-30, created 2025-10-21, 3,973 commits, pushed the day of verification, latest desktop release v1.25.0 on 2026-08-26.
The Launch HN thread drew 108 points and 135 comments, and the founders say they ship daily.
**Adoption claims beyond GitHub ("tens of thousands of engineers", big-company logos) are self-reported, and the codebase is still founder-dominated.**

## Strengths

- Real isolation plumbing: per-worktree setup and teardown scripts, port detection, browser previews, and sessions that survive app restarts.
- Agent-agnostic by design, so harness churn in the market does not strand your orchestrator.
- Programmable from CLI, SDK, and MCP, which means other agents can drive your orchestration.
- The local desktop app is free forever under ELv2 with self-hosting permitted.

## Cautions

- macOS-first with Linux explicitly experimental and no Windows build; the founders said on HN that nobody there daily-drives either.
- The launch thread records freezing, terminal rendering glitches, around 2 GB of memory use, and one user who left for Zellij, plus a sign-in requirement in the hosted build.
- Name collision with Apache Superset confuses search and procurement.
- The 100+ agents framing is parallel independent sessions, not coordinated swarms; the founders' own sweet spot is five or six.

## Pricing

Free ($0) for one user with local workspaces, the desktop app, GitHub integration, and CLI.
Pro at $20/user/month ($15 annually) adds unlimited users, beta remote access, Linear and Slack integrations, and priority support.
Enterprise adds SAML SSO, SCIM, audit logs, SOC 2 report, and SLAs at custom annual pricing.
Agents and models always run on your own subscriptions; Superset never charges for tokens.

## Compared to

- [Paseo](../paseo/index.md): open source, cross-platform, phone-first; choose Superset for macOS-native terminal ergonomics and SDK-grade programmability, Paseo for mobile and FOSS.
- [Conductor](../conductor/index.md): chat-centric and built on the Claude Code and Codex SDKs with cloud sandboxes; note that Anthropic's 2026 pricing meters SDK-based wrapper usage differently, which Superset's terminal-first design sidesteps.
- Plain terminal with worktrees (tmux plus `git worktree`): zero lock-in and zero memory overhead; Superset earns its keep past roughly five parallel sessions, when ports, sessions, and diffs need tracking.

## Bottom line

**Recommended for macOS engineers running five or more parallel agent sessions who want diff review and session persistence without per-token fees.**
Not for Windows or Linux-primary teams, and not for anyone who needs coordinated multi-agent workflows rather than parallel independent sessions.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Paseo](../paseo/index.md) - the open-source, mobile-first counterpart
- [Conductor](../conductor/index.md) - the SDK-based commercial incumbent
- [cmux](../cmux/index.md) - the terminal-native macOS alternative

## References

- https://github.com/superset-sh/superset - repository, feature set, license, adoption numbers
- https://raw.githubusercontent.com/superset-sh/superset/HEAD/README.md - supported agents, platforms, licensing statement
- https://superset.sh/pricing - tiers and the free-forever local core
- https://superset.sh/team - founders, batch, and the self-reported raise and adoption
- https://docs.superset.sh - workspaces, CLI, SDK, MCP server, automations
- https://news.ycombinator.com/item?id=48236770 - the launch thread with stability complaints and the Conductor-metering note
