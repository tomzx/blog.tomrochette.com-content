---
title: OpenHarness
created: 2026-10-24
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, orchestration, agentic-development-environment, multi-agent, encryption, hardware]
readability: 3
audience_notes: >
  Engineers running several coding-agent CLIs across more than one machine who want one
  command center for all of them, and who can weigh a young vendor-operated project against
  the alternatives. Assumes you already run at least one agent CLI and know what tmux is.
---

OpenHarness (marketed as Harness by Autonomous) is a free, MIT-licensed native desktop command center for macOS and Linux that runs your existing coding-agent CLIs side by side, fourteen engines from Claude Code to Devin, each in its own tmux pane and git worktree, and links every machine you own into one end-to-end-encrypted workspace reachable from desktop, terminal, phone, web, and a desk device.

**Its bet is that the harness should own the machines and the transport while the agents stay untouched: it never wraps an agent, it reads transcripts and installs the vendor's own hooks.**

## What it is

Autonomous, the hardware company whose store sells lamps, computers, and office furniture, built it, and the whole stack lives in one MIT repository: the Flutter desktop app, the hn terminal client, the per-machine daemon, the Node relay backend, and the desk device's firmware, PCB, and enclosure files.
One daemon per machine runs the agents in tmux, restores panes, tails each engine's transcript, and dials out to the vendor's relay, so no machine opens a port.
Machines pair through a six-character password over a CPace-style PAKE, and every path is encrypted with pinned Ed25519 identities, X25519 session keys, and ChaCha20-Poly1305, whether traffic runs direct over WebRTC, through Cloudflare TURN, or through the relay, which holds no keys.
Engine support is the broadest I have recorded at this layer: Claude Code, Codex, Cursor, OpenCode, Pi, Hermes, Command Code, Devin, Muse Code, Amp, Kilo, Grok Build, Antigravity, and GitHub Copilot, followed through their own hooks, transcripts, and resume flags.
A Store of 49 domain-specific harnesses extends the same pattern past software: each is a folder with a harness.json pinning a toolchain, instructions, checks, and a live viewer for crafts like CAD, circuit design, robotics, games, and music, and the README's answer to what carries them is that code stays the common medium, so the coding agents remain the spine.
An experimental Agent Messages surface lets harnesses in one tab message each other, and agents can start other agents, but only after the account holder turns that on deliberately.

## Status

Active and young: the repository was created 2026-08-04, held 1,358 stars and 125 forks as of 2026-10-24, and was pushed 2026-11-25 (GitHub API, as of 2026-11-25).
The release train runs two lines: a CLI stable line that stepped from the `v0.4.x` tags (v0.4.97_cli, 2026-10-28) onto `v0.5.x` with v0.5.66_cli on 2026-11-07 (v0.5.60_cli on 2026-11-06, itself after v0.5.38_cli on 2026-11-04 and v0.5.31_cli on 2026-11-03 carrying merge batches plus a Harness OS 0.1.14 build), then onto `v0.6.x` on 2026-11-12 with a same-day burst through v0.6.47_cli (v0.6.38 through v0.6.47 all landing 2026-11-12), v0.6.56_cli on 2026-11-13, v0.6.57_cli on 2026-11-16 (the dial wave: herdr's agents listed, followed, and spoken to over herdr's socket, tmux and VS Code agents reachable with the app closed, and the dial's state exposed to Orca through a plugin), and v0.6.60_cli on 2026-11-17 (Claude Code and Codex reaching the dial with no setting, and a program keeping one harness when ensured), the CLI line then bursting from v0.6.62_cli through v0.6.71_cli across 2026-11-18 and 2026-11-19 (a held agent saying why: a missing helper or replaced program is a named state that wait, show, watch, and ps read, and Linux following the XDG Base Directory paths) and on to v0.6.79_cli (2026-11-21, Harness Pro reporting how many agents of each app are working, and the Claude and ChatGPT apps' dial sessions and follow running on Windows and Linux) and v0.6.80_cli on 2026-11-22 (the dial's eval for the Claude and ChatGPT apps: tiers A and B, a 0-100 score per app, the wrong-session gate, and the baseline, plus an agent browser spec), then v0.6.81_cli through v0.6.85_cli across 2026-11-22 and 2026-11-23 (a dial eval for VS Code and Cursor with voice typed into the focused terminal, a Needs-you ask that agents raise without blocking and the dial shows with its recommendation, and dial usage kept as counts only), v0.6.86_cli on 2026-11-24 (a replugged dial found on the operating system's arrival signal, tmux and herdr as their own apps on the Apps screen, and a held registration naming its own engine), v0.6.87_cli and v0.6.88_cli on 2026-11-25 (held launches starting again by themselves, Orca's chats on the ring with their worktree on screen, and the Harness OS 0.1.18 build), and a desktop-and-web line that stepped from `v1.3.x` onto `v1.4.x` the same day, v1.4.8_desktop (2026-11-07) following v1.3.89_desktop (2026-11-07), which follows v1.3.59_desktop (2026-11-04), v1.3.44_desktop, and a web line through v1.3.99_web (2026-11-06), after v1.3.83_web (2026-10-30) and the earlier browser builds served from harness.autonomous.ai, with the desktop line then bursting to v1.4.49_desktop on 2026-11-13, v1.4.50_desktop on 2026-11-16 (removing Swarm and its retired settings, and opening an agent's Browser in a pane beside its terminal), v1.4.51_desktop on 2026-11-17, the web line following onto `v1.4.x` at v1.4.2_web (2026-11-17) through v1.4.4_web (2026-11-19) and v1.4.8_web (2026-11-21, a website-only update with the existing app bundle preserved), and the desktop line continuing with v1.4.52_desktop on 2026-11-18 (installing the Harness menu-bar app when a dial is plugged in, and the dial scroll reaching the agent terminal in Herdr tab on one route with VS Code) and v1.4.53_desktop on 2026-11-19, then v1.4.54_desktop on 2026-11-20 (the desktop setting up and managing Intern 3 as the phone does, OpenClaw message handling fixes, and dial voice recordings reaching the agent in one-minute pieces on a slow uplink), a release the 2026-11-21 and 2026-11-22 refreshes missed when they recorded the desktop line unmoved (GitHub releases, as of 2026-11-25).
As of 2026-11-27 the CLI line has run from v0.6.93_cli and v0.6.94_cli (2026-11-26, dial skill usage counting and signing Claude Code or Codex in from the phone) through v0.6.95_cli to v0.6.99_cli (2026-11-27, dial voice to Codex and other engines in terminals, the session-start line sending the agent to the dial skill) to v0.7.1_cli (2026-11-27, a separate cliVersion field for the CLI's version beside the dial's firmwareVersion), per the GitHub releases feed.
Autonomous launched it publicly in mid-October 2026, and the launch coverage recorded 213 Product Hunt upvotes about seven hours into launch day and about 3,553 commits at 1,266 stars (Reveneau, 2026-10-16).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=autonomous-ai/openharness&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=autonomous-ai/openharness&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=autonomous-ai/openharness&type=date&legend=top-left" />
</picture>

No HN thread of its own exists: every one of the nine OpenHarness hits on HN is an earlier, unrelated project from February through April 2026, which is also a name-collision hazard for anyone searching the name.
Independent coverage is launch echo only: the news roundups restate the vendor's page, and the performance figures (11-13 ms UI medians, 304 MiB idle, 0.1 percent of a core) are the company's own measurements on its own benchmark, with no independent test cited.

## Strengths

- The multi-machine model is the differentiator: password pairing, always-on encryption, WebRTC with TURN and relay fallbacks, and no SSH keys or port forwarding.
- Fourteen engines through vendor-native hooks means new agent features arrive without waiting for Harness to reimplement them.
- The full stack is open, including the relay backend and the device hardware down to Gerbers, which is unusual at this layer.
- The agent-facing surface (an llms.txt contract, the harness CLI with whoami, ps, wait, and send, an MCP server, and a Claude Code plugin) is designed so agents themselves can delegate and wait on background harnesses.
- A worktree per harness keeps the working copy clean by default.

## Cautions

- Zero independent coverage: no benchmark or critical review exists, and every performance number is the vendor's own.
- Distribution is vendor-hosted: the app and CLI installer download from harness.autonomous.ai rather than the repository, and multi-machine linking, discovery, and sign-in run through the vendor's hosted relay and account, though single-machine use needs no account and the relay code is open.
- The name collides with at least five earlier OpenHarness projects, which poisons search and attribution.
- The beyond-code store is a breadth bet: 49 craft harnesses of unmeasured quality, wrapped around a marketing funnel for the $149 and $299 desk hardware.
- New harnesses default to the engine's auto-approve permission mode, and agent-starts-agents exists at all, so the consent settings deserve a read before fleet use.

## Pricing

The app, CLI, daemon, and relay are free and MIT-licensed.
Autonomous sells the desk hardware beside it: the Harness Device at $149 and the Harness Pro display at $299 (as of 2026-10-24).
On 2026-11-24 the vendor page listed both on sale, the Device at $129 and the Pro at $249, the list prices struck through beside them.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-24 | Harness app | free, open source at note creation | https://www.autonomous.ai/harness |
| 2026-10-24 | Harness Device | introduced at $149 | https://www.autonomous.ai/harness |
| 2026-10-24 | Harness Pro | introduced at $299 | https://www.autonomous.ai/harness |
| 2026-11-24 | Harness Device, Harness Pro | sale prices: Device $129 (list $149) and Pro $249 (list $299) | https://www.autonomous.ai/harness |

## Compared to

- [Emdash](../emdash/index.md): the other open ADE covers all three desktops with SSH-first remote work, while OpenHarness is Mac and Linux only but adds multi-machine encrypted transport, phone clients, and hardware.
- [Omnara](../omnara/index.md): Omnara owns execution as a YAML control plane with phone supervision, while OpenHarness keeps your CLIs untouched and wraps transport and devices around them.
- [Conductor](../conductor/index.md): Conductor is the polished closed macOS session manager for parallel Claude Code and Codex, and OpenHarness is the open, encrypted, multi-machine answer with broader engine support.

## Bottom line

Recommended for engineers running three or more agent CLIs across a laptop plus a home server or GPU box who want one encrypted window and will accept a young, vendor-operated dependency.
Not for Windows users, and not for anyone who needs independent performance evidence or a turn-key self-hosted multi-machine path today.

## Changes

- 2026-10-24 - Created.
- 2026-10-27 - Recorded the release train (v0.4.76_cli stable on 2026-10-27, daily v1.3.x_web browser builds) and refreshed the push date.
- 2026-11-01 - Recorded the desktop-and-web line at v1.3.44_desktop and v1.3.83_web (both 2026-10-30) and the 2026-11-01 push.
- 2026-11-04 - Recorded v0.5.38_cli (2026-11-04) on the CLI line and v1.3.59_desktop (2026-11-04) on the desktop line, the push date refreshed to 2026-11-04.
- 2026-11-06 - Volatile refresh: Recorded v0.5.60_cli (2026-11-06) on the CLI stable line.
- 2026-11-13 - Volatile refresh: Recorded v0.6.54_cli (2026-11-13) on the CLI line and v1.4.49_desktop (2026-11-13) on the desktop line, the push date refreshed to 2026-11-13.
- 2026-11-16 - Recorded v0.6.57_cli (2026-11-16, the dial wave: herdr socket listing, closed-app tmux and VS Code agents, an Orca plugin) on the CLI line.
- 2026-11-17 - Recorded v0.6.60_cli (2026-11-17) on the CLI line and v1.4.51_desktop (2026-11-17, after v1.4.50 removed Swarm and opened the agent Browser pane) on the desktop line, the push date refreshed to 2026-11-17.
- 2026-11-19 - Volatile refresh: recorded the CLI line bursting to v0.6.71_cli, desktop v1.4.52_desktop (menu-bar app on dial plug-in, dial scroll into Herdr tabs) and v1.4.53_desktop (held agents saying why), and the web line stepping onto v1.4.2 through v1.4.4_web, the push date refreshed to 2026-11-19.
- 2026-11-21 - Volatile refresh: recorded v0.6.79_cli (2026-11-21, Harness Pro app ring counts, dial sessions and follow on Windows and Linux) on the CLI line and v1.4.8_web (2026-11-21, website-only update) on the web line.
- 2026-11-22 - Volatile refresh: recorded v0.6.80_cli (2026-11-22, dial eval for the Claude and ChatGPT apps: tiers A and B, a 0-100 score per app, the wrong-session gate, and the baseline) on the CLI line, the desktop line unmoved at v1.4.53_desktop.
- 2026-11-24 - Re-verified in rotation: every cited URL re-fetched live (repo API, README, the architecture and engines docs, the vendor page, llms.txt, the HN search, and the launch coverage; the fourteen-engine table and transport model as recorded); recorded v0.6.81_cli through v0.6.85_cli (2026-11-22 and 2026-11-23, the VS Code and Cursor dial eval, Needs-you asks raised without blocking) and v1.4.54_desktop (2026-11-20, Intern 3 setup from the desktop, OpenClaw message fixes, dial voice uploads in one-minute pieces), which the two prior refreshes missed, the push date refreshed to 2026-11-24.
- 2026-11-24 - Recorded the hardware sale prices on the vendor page, Harness Device $129 and Harness Pro $249 against the $149 and $299 list prices, with a Price history row.
- 2026-11-25 - Volatile refresh: recorded v0.6.86_cli (2026-11-24, a replugged dial found on the arrival signal, tmux and herdr as their own apps on the Apps screen) and v0.6.87_cli and v0.6.88_cli (2026-11-25, held launches recovering by themselves, Orca's chats on the ring, the Harness OS 0.1.18 build) on the CLI line, the desktop line unmoved at v1.4.54_desktop and the web line at v1.4.8_web, the push date refreshed to 2026-11-25.
- 2026-11-27 - Volatile refresh: recorded v0.6.93_cli and v0.6.94_cli (2026-11-26) through v0.7.1_cli (2026-11-27, the cliVersion field) on the CLI line.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Emdash](../emdash/index.md) - the cross-platform open ADE in the same seat
- [Omnara](../omnara/index.md) - the control-plane alternative that owns execution
- [herdr](../herdr/index.md) - the terminal-runtime approach to owning the agents' terminals
- [Conductor](../conductor/index.md) - the closed macOS counterpart

## References

- https://api.github.com/repos/autonomous-ai/openharness - repository, license, counts, and dates (as of 2026-10-24)
- https://raw.githubusercontent.com/autonomous-ai/openharness/main/README.md - the product surface, transport model, store catalog, and device
- https://raw.githubusercontent.com/autonomous-ai/openharness/main/docs/architecture.md - the daemon, session registry, E2EE stack, and ownership boundaries
- https://raw.githubusercontent.com/autonomous-ai/openharness/main/docs/engines.md - the fourteen-engine table and the auto-approve default
- https://www.autonomous.ai/harness - the vendor page and the $149 and $299 hardware prices; on 2026-11-24 the same list prices struck through beside sale prices of $129 and $249
- https://harness.autonomous.ai/llms.txt - the agent-facing CLI contract, consent gating, and agent limits
- https://hn.algolia.com/api/v1/search?query=openharness&tags=story - the nine name-collision hits and the absent HN footprint
- https://reveneau.com/ainews/openharness-autonomous-command-center-coding-agents-mit-1266-stars - the launch facts and the vendor-measurement caveat
- https://api.github.com/repos/autonomous-ai/openharness/releases/tags/v0.6.88_cli - the v0.6.88_cli release notes (2026-11-25), with the v0.6.86_cli and v0.6.87_cli notes: the dial, held-launch recovery, and the Harness OS 0.1.18 build (fetched 2026-11-25)
