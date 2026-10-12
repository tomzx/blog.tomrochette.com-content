---
title: bb
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surfaces, ai-editors, open-source]
readability: 3
audience_notes: >
  Engineers who want an IDE that treats its own features as agent work, and who already run provider CLIs with their own subscriptions.
  Assumes you know what a worktree and a provider CLI are.
---

bb is an MIT-licensed agentic IDE built to control, customize, and automate itself, where the desktop app, web app, CLI, and HTTP API are all first-class ways to drive agent threads.

**bb's bet is that an IDE is just another program an agent can modify, so its own features ship as plugins built with the same agent tooling you use, and anything you can describe becomes part of the editor.**

## What it is

A local-first IDE organized around threads: work runs in threads you follow live, steer at any point, or hand to another agent, each in its own worktree.
It drives the provider CLIs you already authenticated (Claude Code, Codex, Cursor, Pi, OpenCode, Grok Build, oh-my-pi, Hermes Agent, and more), so model access stays on your own subscriptions and bb adds no billing layer.
Almost anything in the app is prompt-changeable, and the flagship features are themselves plugins: the GitHub integration, agent memory, scheduled jobs, and remote access.
The `bb spawn` CLI is open to any program, so a cron job, a shell script, or a Telegram bot can start a thread that waits in your sidebar.
It is free and MIT end to end, installed as a macOS (Apple Silicon) desktop build or anywhere via `npx bb-app@latest`, with Linux and Windows builds in alpha and a nightly channel alongside.

## Status

**Active, shipping weekly, and without independent coverage.**
The repository was created 2026-02-24 and shows 4,241 stars and 628 forks as of 2026-10-12, with commits landing the same day.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=get-bb/bb&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=get-bb/bb&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=get-bb/bb&type=date&legend=top-left" />
</picture>

The desktop train: v0.45.0 (October 2), then v0.46.0 (October 9) as the latest stable, with a rolling nightly.
An Algolia search of Hacker News found no story about bb as of 2026-10-11, and this run's search surfaced no third-party review; the product site's "used by" logo wall is the only social proof and it is unverifiable.

## Strengths

- **The self-building loop is unique in this category: the IDE's own GitHub integration, memory, scheduling, and remote access are plugins written with its own agents, so the tool eats its own dog food by construction.**
- Four driving surfaces (desktop, web, CLI, HTTP API) mean the same threads are reachable from scripts and other programs, the widest automation front in the category.
- MIT end to end with local-first operation on your existing subscriptions: no new billing meter to watch.
- Agents can spawn and manage each other, one thread delegating to another, which turns the IDE into a small orchestration layer without leaving the editor.

## Cautions

- **Nothing independent verifies the experience: zero Hacker News footprint, no third-party coverage found this run, and the logo wall proves nothing, so adoption is an act of trust in the README.**
- Linux and Windows builds are alpha, so the practical platform today is Apple Silicon macOS.
- MCP and AGENTS.md support are not documented anywhere this run could find, so tool servers and rule files stay managed inside the wrapped CLIs.
- v0.x on a weekly train, and the self-modification premise means the tool you adopt is partly written by its own agents, a provenance question no other member raises.

## Pricing

Free and open source under MIT; model usage bills through the provider subscriptions and keys you already have, and no paid tier exists.

## Compared to

- [Cate](../cate/index.md): the canvas workspace; Cate supervises many CLIs in space, bb makes one IDE extensible by the agents it hosts.
- [OpenChamber](../openchamber/index.md): the session cockpit; OpenChamber is OpenCode-native, bb is CLI-agnostic with the plugin system.
- [Conductor](../../orchestration/conductor/index.md): the orchestration desktop bb itself names as a comparison; Conductor manages worktrees and sessions from outside the editor, bb folds them into the IDE.

## Bottom line

**Recommended for engineers on Apple Silicon who live in provider CLIs and want an editor that grows by prompting rather than by waiting for releases.**
Not for Windows or Linux daily drivers, and not for anyone who needs independently reviewed security before pointing agents at their own IDE.

## Changes

- 2026-10-11 - Created from the category entrant scan, admitted on its differentiated self-building plugin loop and four-surface automation front, with the zero-coverage caution recorded.
- 2026-10-11 - Added the star history chart.

## See also

- [Cate](../cate/index.md) - the canvas neighbor for supervising the same CLIs
- [OpenChamber](../openchamber/index.md) - the OpenCode-native session cockpit
- [Conductor](../../orchestration/conductor/index.md) - the worktree-and-session manager bb compares itself to
- [Vibeyard](../vibeyard/index.md) - the other desktop that wraps provider CLIs on your own subscriptions

## References

- https://github.com/get-bb/bb - repository, README (threads, self-customization, provider CLI drivers, plugin-first features, bb spawn), MIT license, 4,241 stars and 628 forks as of 2026-10-12
- https://api.github.com/repos/get-bb/bb - creation date 2026-02-24, language TypeScript, push date 2026-10-12, stars and forks as of 2026-10-12
- https://getbb.app - the product site: the self-building pitch, the plugin list (GitHub integration, agent memory, scheduled jobs, remote access), the four surfaces, platform support, and the comparison links
- https://github.com/get-bb/bb/releases - desktop-v0.46.0 (2026-10-09) as the latest stable, after v0.45.0 (October 2), with the nightly tag rolling
- https://hn.algolia.com/api/v1/search?query=%22agent%20IDE%22%20builds%20itself&tags=story - the search that found no story about bb, the missing-footprint evidence, fetched 2026-10-11
