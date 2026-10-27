---
title: OpenHarness
created: 2026-10-24
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, agentic-development-environment, multi-agent, encryption, hardware]
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

Active and young: the repository was created 2026-08-04, held 1,358 stars and 125 forks as of 2026-10-24, and was pushed 2026-10-27 (GitHub API, as of 2026-10-27).
The release train runs two lines: a `v0.4.x_cli` stable line at v0.4.76_cli (2026-10-27) and daily `v1.3.x_web` browser builds served from harness.autonomous.ai (GitHub releases, as of 2026-10-27).
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

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-24 | Harness app | free, open source at note creation | https://www.autonomous.ai/harness |
| 2026-10-24 | Harness Device | introduced at $149 | https://www.autonomous.ai/harness |
| 2026-10-24 | Harness Pro | introduced at $299 | https://www.autonomous.ai/harness |

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
- https://www.autonomous.ai/harness - the vendor page and the $149 and $299 hardware prices
- https://harness.autonomous.ai/llms.txt - the agent-facing CLI contract, consent gating, and agent limits
- https://hn.algolia.com/api/v1/search?query=openharness&tags=story - the nine name-collision hits and the absent HN footprint
- https://reveneau.com/ainews/openharness-autonomous-command-center-coding-agents-mit-1266-stars - the launch facts and the vendor-measurement caveat
