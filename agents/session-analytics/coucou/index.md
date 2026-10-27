---
title: Coucou
created: 2026-10-10
updated: 2026-10-25
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
Since Mac v0.4.0 (2026-10-15) it is also a windowed Dock app: Flow hold-a-key dictation with an optional offline Parakeet model on Apple silicon, call recording with a speaker-split transcript and summary, and one window gathering the notch settings, all free and open source.
The mechanism is hook-and-relay: an `nb-hook` script receives Claude Code hook events over a Unix socket, waits for your click on the Allow, Deny, or Always card, then answers the hook, and if Coucou is not running the hook exits immediately so Claude Code is never blocked.
Coverage beyond Claude Code comes through hooks (Gemini CLI, Antigravity), `--agent` flags (Codex, Copilot CLI, Muse Code, any agent), and plugins installed into OpenCode, Amp, and Hermes config directories; any agent can tag a hook payload `coucou_agent` for its own pill.
The iPhone app (iOS 18, TestFlight) reads sessions, turns, and service state from a private CloudKit zone in your iCloud with sensitive fields encrypted under your iCloud keys, and writes back decisions the Mac only applies when they match the exact pending request, Face ID required on every Allow; Live Activities update through APNs pushes from a stateless Cloudflare Worker relay that sees only the agent's name and state.
A companion Android app (Android 11 or later), built by Rhytam Biswas as the project's first outside contribution, pairs over your local network with Coucou 0.4.0 for Windows or Linux, answers approvals with a fingerprint, and the link is off by default with a pairing code that re-pairing replaces.
Around that core sit service pills (GitHub, Stripe, Vercel, n8n, Notion, Resend, Cal.com), chat with Claude, Gemini, OpenAI, or local Ollama and LM Studio models, plan-usage pills for Claude and Codex limits, a weekly recap image, and voice control through an "OK Coucou" command.
It is built by Louis Raillé (the Louis-CFM account), with the project's own contributors table listing Claude Code itself as the second-largest contributor.

## Status

In its fourth week and shipping hard: created 2026-09-27 with v0.1.0 the same day, with the Mac release line moving to v0.5.3 on 2026-10-22 (Mochi turns blue when a new version waits and then shows what it brings) after v0.5.2 on 2026-10-20 (in-notch update offers verified against the Developer ID signature, a Homebrew cask, Claude Code plan-approval cards offering the terminal's own Auto, Manual, or Change plan choices, and fourteen languages), after v0.5.0 and v0.5.1 on 2026-10-18 (WhatsApp in the notch, behind it a one-click install of the GOWA gateway checked against its published SHA-256), after v0.4.0 on 2026-10-15 (the windowed app with dictation and call recording), Windows and Linux at 0.5.3 since 2026-10-23 (MSI and setup installers, still unsigned, now matching the Mac line's version number), and Coucou for Android at 0.3.0 since 2026-10-22, as of 2026-10-25.
5,119 stars and 1,029 forks in that window, 486 open issues, MIT.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Louis-CFM/coucou&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Louis-CFM/coucou&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Louis-CFM/coucou&type=date&legend=top-left" />
</picture>

**The adoption curve outruns the scrutiny: no Hacker News thread, no third-party review, and no Reddit trace surfaced in this run's searches, so the vetting so far is the README against the commits.**

## Strengths

- **The broadest live coverage in this category: eleven named agents plus a generic flag, against the two or three every other live view watches.**
- The approval loop is safe by construction: the Mac applies only a decision matching the pending request, and Face ID gates every Allow from the phone.
- The phone companion is native (Live Activities, Dynamic Island, Lock Screen actions, Siri, widgets), not a web page in a shell.
- Local-first defaults: no telemetry, no account, keys in the system keychain, sync through your private iCloud database.
- A dated, fast release train with a changelog you can audit release by release.

## Cautions

- **Zero independent footprint at 5.1k stars is the caution: two-plus weeks of stars with no thread and no review is distribution, not verification.**
- The 0.x line moves so fast that documented behavior can change within days, and first-run setup modifies `~/.claude/settings.json` (backed up with a diff shown first, but still an agent-config mutation).
- The Windows installer is unsigned and trips SmartScreen, and the future App Store build will drop the plan-usage, Apple Music, and window-attach features.
- Feature gravity pulls away from analytics: the wardrobe, music, Stripe, WhatsApp, voice, dictation, and call recording make it a personal companion that watches agents, not an audit tool, and there is no token-cost accounting anywhere.
- One maintainer plus an AI co-author wrote essentially all of it; the Android app and its phone link are the first outside contribution (Rhytam Biswas).

## Pricing

Free and open source under MIT; no paid tier.
App Store versions for Mac and iPhone are announced but not published as of 2026-10-10.

## Compared to

- [Claude Code Agent Monitor](../claude-code-agent-monitor/index.md): the local control room that also launches and resumes agents; Coucou covers far more agents but watches and answers rather than driving runs.
- [agents-observe](../agents-observe/index.md): the lighter hook-fed dashboard for Claude Code and Codex; Coucou adds approvals, service pills, and the phone.
- [Token Monitor](../token-monitor/index.md): the always-on usage widget; Coucou shows plan-limit pills instead of token accounting.

## Bottom line

**Recommended for Mac users of Claude Code or Codex who want permission requests answered from the notch or a locked iPhone, and who accept a weeks-old 0.x dependency that rewrites its own docs weekly.**
Not for token-cost audits (ccusage and agentsview stay the tools for that), and not for Windows-first users unwilling to run an unsigned installer today.

## Changes

- 2026-10-10 - Created from the category entrant scan, admitted on its eleven-agent live coverage and notch-and-Lock-Screen approval mechanism with the empty independent footprint recorded.
- 2026-10-13 - Recorded Coucou for Android 0.1.0 (Rhytam Biswas, Android 11 or later, pairing over the local network with the Windows and Linux apps) and the v0.4.0 Windows and Linux builds that carry the phone link, while the Mac release line stays at v0.3.0; repository counts refreshed (4,736 to 4,993 stars, 785 to 838 forks, 252 to 314 open issues).
- 2026-10-13 - Recorded Coucou for Android 0.2.0 (2026-10-13, two days after 0.1.0, with the release note describing the same pairing flow and no feature list); repository counts refreshed (4,993 to 5,119 stars, 838 to 853 forks, 314 to 321 open issues), and the thin-footprint caution's star figure moved with them.
- 2026-10-16 - Recorded Mac v0.4.0 (2026-10-15): Coucou became a windowed Dock app with Flow hold-a-key dictation, an optional offline Parakeet model on Apple silicon, and call recording with a speaker-split transcript, signed and notarized; Windows and Linux moved to v0.5.0 the same day (still unsigned), and the feature-gravity caution gained the dictation and call-recording evidence.
- 2026-10-19 - Recorded the Mac v0.5.0 and v0.5.1 releases (both 2026-10-18): WhatsApp in the notch with a one-click install of the GOWA gateway verified against its published SHA-256, Mochi reacting to Mac state, a screen capture for Claude, and dictation that writes prompts or translates; the feature-gravity caution gained WhatsApp.
- 2026-10-21 - Recorded the Mac v0.5.2 release (2026-10-20): in-notch update offers that download from GitHub and verify the Developer ID signature before swapping the app, a Homebrew cask, Claude Code plan-approval cards offering Auto, Manual, or Change plan, fourteen languages, and community fixes; Windows and Linux moved to v0.5.1 the same day, the installer still unsigned; repository counts refreshed (forks 853 to 961, open issues 321 to 420).
- 2026-10-25 - Recorded the Windows and Linux 0.5.3 builds (2026-10-23, now matching the Mac line's version number) and Coucou for Android 0.3.0 (2026-10-22, a pairing-flow release with no feature list); repository counts refreshed (forks 961 to 1,029, open issues 420 to 486).

- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).

## See also

- [Claude Code Agent Monitor](../claude-code-agent-monitor/index.md) - the live control room this note joins as the mobile approval counterpart
- [agents-observe](../agents-observe/index.md) - the lighter hook-fed live view
- [Token Monitor](../token-monitor/index.md) - the usage-widget neighbor for limits without the character
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/Louis-CFM/coucou - 5,119 stars, 853 forks, MIT license, created 2026-09-27, pushed 2026-10-13, as of 2026-10-13
- https://raw.githubusercontent.com/Louis-CFM/coucou/main/README.md - the agents table, hook and plugin mechanisms, CloudKit sync and relay design, privacy statements, and the versions table
- https://api.github.com/repos/Louis-CFM/coucou/releases - the Mac line v0.1.0 (2026-09-27) through v0.5.3 (2026-10-22), the Windows/Linux builds through 0.5.3 (2026-10-23), and android-v0.1.0 (2026-10-11) through android-v0.3.0 (2026-10-22) (re-fetched 2026-10-25)
- https://api.github.com/repos/Louis-CFM/coucou/releases/tags/v0.4.0 - the Mac 0.4.0 release note: the Dock window, Flow dictation, Parakeet, and the notetaker
- https://api.github.com/repos/Louis-CFM/coucou/contributors - the Louis-CFM 192 and claude 156 commit split behind the AI-co-author caution
- https://louis-cfm.github.io/coucou/ - the homepage grounding the product summary, downloads, and the 0.3 voice announcement
- https://github.com/Louis-CFM/coucou/releases/tag/android-v0.2.0 - the Android 0.2.0 release note: download, pairing steps, and checksum verification (fetched 2026-10-13)
- https://github.com/Louis-CFM/coucou/releases/tag/android-v0.1.0 - the Android 0.1.0 release, its pairing steps, and the Windows-or-Linux requirement (fetched 2026-10-13)
- https://github.com/Louis-CFM/coucou/releases/tag/windows-v0.4.0 - the Windows 0.4.0 build note, still unsigned with the SmartScreen warning (fetched 2026-10-13)
- https://hn.algolia.com/api/v1/search?query=coucou%20notch&tags=story - zero hits, the empty independent footprint this note states
