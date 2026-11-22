---
title: bb
created: 2026-10-11
updated: 2026-11-22
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
The repository was created 2026-02-24 and shows 4,326 stars and 628 forks as of 2026-10-16, with commits landing the same day.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=get-bb/bb&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=get-bb/bb&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=get-bb/bb&type=date&legend=top-left" />
</picture>

The desktop train: v0.45.0 (October 2), v0.46.0 (October 9), v0.46.1 (October 15), v0.47.0 (October 23), v0.47.1 (October 24), and desktop-v0.48.1 (October 30), all carrying no written release notes, and desktop-v0.49.0 (November 6) as the latest stable, the first in months to carry full written notes on the product site's changelog ("A more reliable bb": stuck turns end on their own, retry pile-ups deduplicate, recurring automations ride out provider outages, the hourly database scan is gone, cold page loads roughly halve), which also rolls up 0.48.1's unnoted fixes, and desktop-v0.50.1 (November 18) as the current latest stable, whose notes live in the changelog's 0.50.0 entry (November 18, "Automatic updates, steadier turns, and a faster app"): opt-in auto-update that restarts when no thread runs, end-of-turn messages now arriving, turns surviving restarts and dropped connections, server stalls from thread deletion and pruning removed, lighter live timeline updates, and two security fixes (OpenCode 2 asking before running commands in Accept edits, and Cursor's allow-for-session approvals staying session-scoped); the changelog further documents a mobile front the README stays quiet on, an iOS app in the update path and an Android app in alpha since the 0.45.0 line, plus a rolling nightly.
An Algolia search of Hacker News found no story about bb as of 2026-10-11, a re-run on 2026-10-25 surfaced the same absence, a re-run on 2026-11-07 surfaced it again, a re-run on 2026-11-19 returned the same lone unrelated Agentastic.dev hit, and no third-party review has appeared; the product site's "used by" logo wall is the only social proof and it is unverifiable.
The ecosystem side has more life than the coverage side: a community-maintained plugin directory (MGrin/awesome-bb-plugins, 65 stars as of 2026-11-13) documents that bb ships 21 official plugins and retired its own remote marketplace rather than running a central one (PR #737), so third-party plugins spread by word of mouth, and counts 25 npm packages carrying the `bb-plugin` keyword as of 2026-08-31; third parties are building on bb's plugin system even though nobody has reviewed the experience.

## Strengths

- **The self-building loop is unique in this category: the IDE's own GitHub integration, memory, scheduling, and remote access are plugins written with its own agents, so the tool eats its own dog food by construction.**
- Four driving surfaces (desktop, web, CLI, HTTP API) mean the same threads are reachable from scripts and other programs, the widest automation front in the category.
- MIT end to end with local-first operation on your existing subscriptions: no new billing meter to watch.
- Agents can spawn and manage each other, one thread delegating to another, which turns the IDE into a small orchestration layer without leaving the editor.

## Cautions

- **Nothing independent verifies the experience: zero Hacker News footprint, no third-party coverage found this run, and the logo wall proves nothing, so adoption is an act of trust in the README.**
- Linux and Windows builds are alpha, so the practical platform today is Apple Silicon macOS.
- MCP and AGENTS.md support are not documented anywhere this run could find, so tool servers and rule files stay managed inside the wrapped CLIs.
- The README documents anonymous production telemetry (app starts, thread counts, plugin installs, opt out with `BB_TELEMETRY=false`), a disclosure the creation-time reading missed, so "local-first" does not mean silent.
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
- 2026-10-16 - Recorded desktop-v0.46.1 (October 15) as the new latest stable release; counts refreshed.
- 2026-10-25 - Rotation re-verification, all five cited URLs re-fetched live: the repository, the product site, the release list, and the still-empty Hacker News footprint stand; recorded v0.47.0 and v0.47.1 (October 23 and 24) as the new latest stable releases, and added the README's opt-out telemetry disclosure to Cautions.
- 2026-10-31 - Recorded desktop-v0.48.1 (October 30, no written release notes) as the new latest stable release.
- 2026-11-07 - Rotation re-verification, all cited URLs re-fetched live: recorded desktop-v0.49.0 (November 6) as the new latest stable, the first release in months carrying full written notes on the product site's changelog (the reliability release, rolling up 0.48.1), and recorded the changelog's mobile front (an iOS app in the update path, an Android app in alpha since 0.45.0); the repository (pushed 2026-11-07), the zero-coverage HN search (re-run, same absence), and the README's four-surface pitch stand; prices unchanged.
- 2026-11-13 - Volatile re-verification on the pushed signal (release train unchanged at desktop-v0.49.0), and added the community plugin directory (MGrin/awesome-bb-plugins) to Status as ecosystem evidence: 21 official plugins, the retired remote marketplace, and 25 npm bb-plugin packages per the directory's count; the zero-coverage caution stands, the directory documents plugins without reviewing the IDE.
- 2026-11-17 - Rotation re-verification, all cited URLs re-fetched live: the repository (pushed 2026-11-17, MIT, not archived), the README (same self-building pitch, telemetry section unchanged), the product site, and the changelog (still ending at the 0.49.0 reliability release, no 0.49.1 stable after it) stand, desktop-v0.49.0 confirmed as the latest stable through the releases API, the plugin directory stands unchanged with the recorded facts intact, and the HN search re-run returns the same lone unrelated Agentastic.dev hit; prices unchanged.
- 2026-11-19 - Volatile re-verification on the pushed and released signals, recorded desktop-v0.50.1 (November 18) as the new latest stable with the changelog's 0.50.0 notes entry (automatic updates once idle, end-of-turn message delivery, restart-surviving turns, server-stall removals, lighter timeline updates, and the OpenCode 2 permission and Cursor session-scoped-approval security fixes); the zero-coverage HN search re-run returns the same lone unrelated Agentastic.dev hit.
- 2026-11-22 - Volatile re-verification on the pushed signal, release train unchanged at desktop-v0.50.1 with feature work landing November 21 to 22 on the default branch (agent-writable folders decided per session with each thread granted only its own storage, an Android text-selection fix in the timeline, and split-pane keyboard-focus handling).

## See also

- [Cate](../cate/index.md) - the canvas neighbor for supervising the same CLIs
- [OpenChamber](../openchamber/index.md) - the OpenCode-native session cockpit
- [Conductor](../../orchestration/conductor/index.md) - the worktree-and-session manager bb compares itself to
- [Vibeyard](../vibeyard/index.md) - the other desktop that wraps provider CLIs on your own subscriptions

## References

- https://github.com/get-bb/bb - repository, README (threads, self-customization, provider CLI drivers, plugin-first features, bb spawn, and the opt-out telemetry disclosure), MIT license, 4,326 stars and 628 forks as of 2026-10-16, re-fetched 2026-11-07 (same pitch, telemetry section unchanged)
- https://api.github.com/repos/get-bb/bb - creation date 2026-02-24, language TypeScript, push date 2026-11-07, stars and forks as of 2026-10-16; re-fetched 2026-11-19 (pushed 2026-11-19, not archived)
- https://getbb.app - the product site: the self-building pitch, the plugin list (GitHub integration, agent memory, scheduled jobs, remote access), the four surfaces, platform support, the comparison links, and the 0.47.0 changelog headline (customizable navigation, new and improved ACP support, diff review)
- https://getbb.app/changelog - the product changelog: the 0.49.0 reliability release notes (stuck turns, retry dedupe, automation survival, the database scan removal, faster page loads, rolling up 0.48.1), the 0.45.0-to-0.49.0 mobile evidence (iOS app in the update path, Android app alpha), and the written notes behind 0.46.0, 0.47.0, and 0.48.0, fetched 2026-11-07, re-fetched 2026-11-19 with the 0.50.0 entry (November 18, "Automatic updates, steadier turns, and a faster app") grounding the desktop-v0.50.1 notes
- https://github.com/get-bb/bb/releases - desktop-v0.50.1 (2026-11-18, its GitHub body title-only) as the latest stable, after desktop-v0.49.0 (2026-11-06, no written notes on GitHub) and desktop-v0.48.1 (2026-10-30) and desktop-v0.48.0 (2026-10-28), desktop-v0.47.1 (2026-10-24) and v0.47.0 (October 23), v0.46.1 (October 15), v0.46.0 (October 9), and v0.45.0 (October 2), with the nightly tag rolling, re-fetched 2026-11-19
- https://github.com/MGrin/awesome-bb-plugins - the community plugin directory: 21 official plugins with the retired remote marketplace (PR #737), the git and npm install forms, and the 25-package bb-plugin npm count as of 2026-08-31, fetched 2026-11-13
- https://api.github.com/repos/MGrin/awesome-bb-plugins - the directory repository: 65 stars, pushed 2026-11-03, not archived (GitHub API, as of 2026-11-13)
- https://hn.algolia.com/api/v1/search?query=%22agent%20IDE%22%20builds%20itself&tags=story - the search that found no story about bb, the missing-footprint evidence, re-fetched 2026-11-07 (still only an unrelated Agentastic.dev hit)
