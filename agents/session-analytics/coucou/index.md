---
title: Coucou
created: 2026-10-10
updated: 2026-10-10
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, observability, live-observation, approvals, macos, ios, open-source]
readability: 3
audience_notes: >
  Engineers running coding agents who want permission requests and session state to follow them
  away from the terminal, and anyone comparing live observation mechanisms.
  Assumes you know what a Claude Code hook is.
---

Coucou is an MIT-licensed Mac notch companion (a top-edge island on Windows and Linux) with an iPhone app beside it, watching coding-agent sessions live across Claude Code, Codex, Cursor, Gemini CLI, Antigravity, Copilot CLI, Muse Code, OpenCode, Amp, Hermes, and Claude Desktop, and letting you answer permission requests from the notch or the Lock Screen.

**Coucou moves the approval surface off the terminal entirely: hooks render the request in the notch, your tap answers the hook, and the same session follows you onto a locked phone through your own iCloud.**

## What it is

A native Swift 6 and SwiftUI macOS app with zero third-party dependencies (Windows and Linux ride a Tauri 2 build), fronted by Mochi, a character that pops out of the notch, waves, and jumps when a session finishes.
The mechanism is hook-and-relay: an `nb-hook` script receives Claude Code hook events over a Unix socket, waits for your click on the Allow, Deny, or Always card, then answers the hook, and if Coucou is not running the hook exits immediately so Claude Code is never blocked.
Coverage beyond Claude Code comes through hooks (Gemini CLI, Antigravity), `--agent` flags (Codex, Copilot CLI, Muse Code, any agent), and plugins installed into OpenCode, Amp, and Hermes config directories; any agent can tag a hook payload `coucou_agent` for its own pill.
The iPhone app (iOS 18, TestFlight) reads sessions, turns, and service state from a private CloudKit zone in your iCloud with sensitive fields encrypted under your iCloud keys, and writes back decisions the Mac only applies when they match the exact pending request, Face ID required on every Allow; Live Activities update through APNs pushes from a stateless Cloudflare Worker relay that sees only the agent's name and state.
Around that core sit service pills (GitHub, Stripe, Vercel, n8n, Notion, Resend, Cal.com), chat with Claude, Gemini, OpenAI, or local Ollama and LM Studio models, plan-usage pills for Claude and Codex limits, a weekly recap image, and voice control through an "OK Coucou" command.
It is built by Louis Raillé (the Louis-CFM account), with the project's own contributors table listing Claude Code itself as the second-largest contributor.

## Status

Two weeks old and shipping hard: created 2026-09-27 with v0.1.0 the same day, at v0.3.0 on 2026-10-10 after near-daily releases, with Windows and Linux tags trailing the Mac by days, as of 2026-10-10.
4,717 stars and 781 forks in that window, 250 open issues, MIT.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Louis-CFM/coucou&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Louis-CFM/coucou&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Louis-CFM/coucou&type=date&theme=dark&legend=top-left" />
</picture>

**The adoption curve outruns the scrutiny: no Hacker News thread, no third-party review, and no Reddit trace surfaced in this run's searches, so the vetting so far is the README against the commits.**

## Strengths

- **The broadest live coverage in this category: eleven named agents plus a generic flag, against the two or three every other live view watches.**
- The approval loop is safe by construction: the Mac applies only a decision matching the pending request, and Face ID gates every Allow from the phone.
- The phone companion is native (Live Activities, Dynamic Island, Lock Screen actions, Siri, widgets), not a web page in a shell.
- Local-first defaults: no telemetry, no account, keys in the system keychain, sync through your private iCloud database.
- A dated, fast release train with a changelog you can audit release by release.

## Cautions

- **Zero independent footprint at 4.7k stars is the caution: two weeks of stars with no thread and no review is distribution, not verification.**
- The 0.x line moves so fast that documented behavior can change within days, and first-run setup modifies `~/.claude/settings.json` (backed up with a diff shown first, but still an agent-config mutation).
- The Windows installer is unsigned and trips SmartScreen, and the future App Store build will drop the plan-usage, Apple Music, and window-attach features.
- Feature gravity pulls away from analytics: the wardrobe, music, Stripe, and voice make it a personal companion that watches agents, not an audit tool, and there is no token-cost accounting anywhere.
- One maintainer plus an AI co-author wrote essentially all of it.

## Pricing

Free and open source under MIT; no paid tier.
App Store versions for Mac and iPhone are announced but not published as of 2026-10-10.

## Compared to

- [Claude Code Agent Monitor](../claude-code-agent-monitor/index.md): the local control room that also launches and resumes agents; Coucou covers far more agents but watches and answers rather than driving runs.
- [agents-observe](../agents-observe/index.md): the lighter hook-fed dashboard for Claude Code and Codex; Coucou adds approvals, service pills, and the phone.
- [Token Monitor](../token-monitor/index.md): the always-on usage widget; Coucou shows plan-limit pills instead of token accounting.

## Bottom line

**Recommended for Mac users of Claude Code or Codex who want permission requests answered from the notch or a locked iPhone, and who accept a two-week-old 0.x dependency that rewrites its own docs weekly.**
Not for token-cost audits (ccusage and agentsview stay the tools for that), and not for Windows-first users unwilling to run an unsigned installer today.

## Changes

- 2026-10-10 - Created from the category entrant scan, admitted on its eleven-agent live coverage and notch-and-Lock-Screen approval mechanism with the empty independent footprint recorded.

## See also

- [Claude Code Agent Monitor](../claude-code-agent-monitor/index.md) - the live control room this note joins as the mobile approval counterpart
- [agents-observe](../agents-observe/index.md) - the lighter hook-fed live view
- [Token Monitor](../token-monitor/index.md) - the usage-widget neighbor for limits without the character
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/Louis-CFM/coucou - 4,717 stars, 781 forks, MIT license, created 2026-09-27, pushed 2026-10-10, as of 2026-10-10
- https://raw.githubusercontent.com/Louis-CFM/coucou/main/README.md - the agents table, hook and plugin mechanisms, CloudKit sync and relay design, privacy statements, and the versions table
- https://api.github.com/repos/Louis-CFM/coucou/releases - v0.1.0 (2026-09-27) through v0.3.0 (2026-10-10) plus the windows-v* and linux-v* tag trains
- https://api.github.com/repos/Louis-CFM/coucou/contributors - the Louis-CFM 192 and claude 156 commit split behind the AI-co-author caution
- https://louis-cfm.github.io/coucou/ - the homepage grounding the product summary, downloads, and the 0.3 voice announcement
- https://hn.algolia.com/api/v1/search?query=coucou%20notch&tags=story - zero hits, the empty independent footprint this note states
