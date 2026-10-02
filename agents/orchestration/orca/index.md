---
title: Orca
created: 2026-09-27
updated: 2026-10-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, orchestration, agent-ide, worktrees, mobile]
readability: 3
audience_notes: >
  Engineers choosing a desktop environment for running many coding agents in parallel on their own subscriptions.
  Assumes you know what a git worktree and a CLI coding agent are.
---

Orca is a free, MIT-licensed agent development environment (ADE) that runs a fleet of CLI coding agents side by side, each in its own git worktree, from desktop, phone, or a remote machine.

**Orca's bet is breadth: one MIT app that is at once the most cross-platform, the broadest in harness support, and the only one in this category bundling a first-party mobile companion, so it can absorb whatever CLI agent you settle on.**

## What it is

A desktop app built by Stably AI (YC W22, founded by Jinjing Liang, an ex-Google Chrome engineer, and Neil Parker, ex-Uber), also the makers of the Stably testing product.
Every task gets its own git worktree, branch, terminal, and browser tab, with Ghostty-class WebGL terminals that survive restarts, a Monaco editor, per-worktree Chromium for a Design Mode that grabs a clicked element's HTML, CSS, and screenshot into the prompt, and inline diff annotations shipped back to the agent.
It is agent-agnostic and terminal-first: the site lists 27 supported agents (Claude Code, Codex, Cursor CLI, Gemini, Copilot, OpenCode, Pi, Amp, Antigravity, Grok, Kimi, Kiro, Droid, Qwen, and others) and says any other CLI drops in.
Beyond local desktop it spans SSH worktrees, a self-hosted Orca server, on-demand cloud VMs, and an iOS and Android companion app for watching and steering sessions.
MIT licensed, TypeScript and Electron, and the repo's README carries translations into six languages.

## Status

Fast and well-funded: about 83.2k stars and 5,384 forks as of 2026-10-02, created 2026-03-17, more than 11,900 commits, with v1.4.218 (2026-09-30) the latest release.
The changelog shows daily shipping through September 2026, including OpenCode 2 support (2026-09-20), a Muse Code harness and Codex goals in native chat (2026-09-25), and a Design Mode and browser stack.
Stably is a YC W22 company with a separate revenue product (Stably testing), so Orca does not have to monetize itself yet, which is why it can stay free and MIT.
**The caution is scale: 7,014 open issues and pull requests against a repository roughly six months old, and the loudest proof of adoption is a wall of self-selected X quotes rather than independent field reports.**

## Strengths

- The widest platform footprint in the category: macOS, Windows, and Linux desktops plus iOS and Android companions, where Conductor is macOS only and Superset treats Linux as experimental.
- 27 supported agents and a plain "any other CLI" fallback, so harness churn does not strand the tool.
- Genuine review surface (diff viewer, inline annotations, GitHub and Linear review) rather than a bare terminal.
- Remote execution done three ways (SSH worktrees, self-hosted server, cloud VMs) without hosting your code itself.
- A powerful CLI (`orca worktree create`, snapshot, click, fill) so agents can drive the environment, plus hooks, skills, and MCP.

## Cautions

- The open-issue count is very high (7,303 open issues and pull requests as of 2026-10-02); expect rough edges and duplicates, and read the issue tracker before trusting a workflow.
- "Ship 100x" and "hundreds of agents" are marketing framing; the practical unit is still a worktree per task and a human reviewing diffs.
- Adoption evidence is largely self-reported (X quotes, company logos); the Hacker News footprint is thin (a three-point story and a small third-party review as of 2026-09-27).
- Enterprise features (SOC 2 readiness, SAML, org defaults) are behind a sales conversation, so regulated teams cannot self-serve.
- It bundles no models; cost is entirely your existing subscriptions, which the app does not meter for you.

## Pricing

Free and open source under MIT for the desktop, mobile, CLI, and self-hosted server.
Enterprise adds rollout, compliance, and support via a sales conversation at custom pricing; no public dollar tiers.
Agents and models run on your own subscriptions, and Orca does not charge for tokens.

## Compared to

- [Superset](../superset/index.md): source-available (ELv2), macOS-first, and stronger on SDK and automation; choose Orca for Windows and Linux, a real mobile app, and an MIT license.
- [Conductor](../conductor/index.md): the best-funded closed Mac app with the deepest review flow; choose Orca when you need open source, cross-platform desktops, or phone supervision.
- [Lanes](../lanes/index.md): macOS-only and board-centric; choose Orca for a board-light, worktree-and-terminal workspace across all three desktop OSes.

## Bottom line

**Recommended for engineers who run many CLI agents and want the broadest, most open, most cross-platform ADE, including phone supervision and remote execution.**
Not for teams that need a closed, vendor-supported enterprise product today, or for anyone who wants the orchestrator to own model execution and billing.

## Changes

- 2026-09-27 - Created.
- 2026-09-29 - Recorded v1.4.216 (September 28) and refreshed star and tracker counts.
- 2026-09-30 - Recorded v1.4.217 (September 29, Codex workers start again on Codex 0.158) as the latest release and refreshed the star count.
- 2026-10-02 - Recorded v1.4.218 (September 30) as the latest release and refreshed star, fork, and tracker counts.

## See also

- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker that already named Orca the open-source ADE with the widest feature surface
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Superset](../superset/index.md) - the source-available, macOS-first rival
- [Conductor](../conductor/index.md) - the closed, heavily funded Mac incumbent
- [Lanes](../lanes/index.md) - the macOS board-first alternative

## References

- https://github.com/stablyai/orca - repository, feature set, 27-agent list, MIT license, stars and release data
- https://www.onorca.dev/ - product positioning, supported agents, pricing "free and open source"
- https://www.onorca.dev/docs - worktrees, terminals, Design Mode, SSH, CLI, mobile, and the "not a model" scope statement
- https://www.onorca.dev/changelog - release cadence and daily shipping through September 2026
- https://www.onorca.dev/enterprise - Enterprise rollout, compliance readiness, and self-hosting claims
- https://www.ycombinator.com/companies/stably-ai-orca - founders, batch, and the "10 to 100 agents" framing
- https://andrew.ooo/posts/orca-stablyai-parallel-coding-agents-ide-review/ - independent review of the ADE positioning and adoption
