---
title: Lanes
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, orchestration, macos, worktrees, issue-board]
readability: 3
audience_notes: >
  Mac-based engineers shortlisting a parallel-agent workspace that centers an issue board.
  Assumes you run Claude Code or Codex and know what a git worktree is.
---

Lanes is a freemium, native macOS workspace that runs many CLI coding agents as parallel real-PTY sessions, each on an issue and its own git worktree, with a board, editor, SQLite browser, and git client around them.

**Lanes' bet is that parallel agent work is a git problem first and a UI problem second, so it wraps every session in a real worktree and an issue card, and pairs the closed desktop app with an open, self-hostable MCP endpoint that manages what all your agents may reach.**

## What it is

A native macOS app (Apple Silicon and Intel, macOS Ventura or later) from Lanes, installed with `brew install --cask lanes-sh/lanes/lanes`.
Each issue is a board card that moves through Planning, Implementation, Review, and Done, and each card holds live PTY-backed terminal sessions (Claude Code and Codex detected and resumed natively, any other CLI as a plain shell), a generated worktree and branch, and an inline diff.
Around the agent surface it ships a git client, a Monaco editor, a read-only SQLite browser, dependency links with cycle detection, quick commands, voice dictation, and a local MCP server so an agent can read the board and start sessions.
The second half is Lanes Link, a self-hostable MCP endpoint (Apache-2.0, one endpoint you own) that holds accounts, memory, tasks, skills, identity, and a vault behind deny-by-default access profiles and a hash-chained audit log, plus Lanes Forms and per-second Lanes Compute GPUs.
The app runs agents locally, never proxies model calls, and points sessions at whatever provider you configure, including local Ollama or LM Studio.

## Status

Active and iterating: version v0.49.6 shipped 2026-10-06, continuing the v0.49 line that shipped 2026-09-08, the macOS app is on Homebrew, and the changelog runs through October 2026.
The public source repository, lanes-sh/app, shows about 273 stars as of 2026-10-07, created 2026-03-22, last pushed 2026-10-06; the product also spans the Apache-2.0 lanes-sh/link endpoint and the hosted Lanes Forms and Compute services.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=lanes-sh/app&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=lanes-sh/app&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=lanes-sh/app&type=date&legend=top-left" />
</picture>

**The open question is provenance: the site says "open source from day one" and links both repositories, but the app repository carries no license metadata on GitHub as of 2026-09-27, whereas the Link endpoint is explicitly Apache-2.0.**

## Strengths

- The issue board is the differentiator: cards, columns, dependencies, labels, and per-project tabs make a fleet legible in a way terminal tabs do not.
- Real PTY sessions in your own shell with your credentials, and session resume across restarts.
- A full local coding surface around the agents (git client, Monaco editor, SQLite browser, diff), so review does not mean switching to an IDE.
- Lanes Link is a genuinely separate, self-hostable product with 105 providers, access profiles, and an append-only audit log.
- Local-first and model-agnostic: nothing is proxied, and any provider or local model works.

## Cautions

- macOS only (Ventura or later), with no advertised Windows or Linux build; Linux users are directed to hand-managed worktrees.
- The desktop app's license is not declared in its repository metadata even though the site calls it open source; treat the claim as unverified for the app.
- Sessions run as real terminals with your dotfiles and credentials, so assume anything you can do in Terminal an agent can do in Lanes.
- GitHub and Linear are the only tracker integrations; everything else is deep links.
- The pricing page mixes product tiers with GPU Compute, which complicates budgeting if you only want the desktop app.

## Pricing

Free ($0) for one user and unlimited local sessions with the full desktop app.
Pro at $19/month covers up to 10 members, collaboration, higher Forms limits, and security features.
Enterprise is custom for SSO/SAML, audit log, IP restrictions, and data residency.
Lanes Compute is separate and billed per second per GPU; agents run on your own provider subscriptions.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-27 | Free, Pro, Enterprise | Baseline: Free $0 for one user, Pro $19/mo for up to 10 members, Enterprise custom; Compute billed per second. | [lanes.sh/pricing](https://lanes.sh/pricing) |

## Compared to

- [Conductor](../conductor/index.md): the closed, heavily funded Mac app with the deepest review flow; choose Lanes when the issue board and an open MCP endpoint matter more than cloud execution.
- [Orca](../orca/index.md): MIT and cross-platform with a mobile app; choose Lanes for a board-first macOS workflow and the broader Link access layer.
- [Helmor](../helmor/index.md): Apache-2.0, local-first, and also macOS plus Windows; choose Lanes for the board and Provider/Forms/Compute family, Helmor for an open license and Windows support.

## Bottom line

**Recommended for macOS engineers who want parallel agents organized as issues on a board with a real git and editor surface around them, and who want their agent access governed by one self-hosted endpoint.**
Not for Windows or Linux shops, and not for anyone who needs a verifiably open licensed desktop client.

## Changes

- 2026-09-27 - Created.
- 2026-09-29 - Recorded v0.49.5 (September 25) on the v0.49 line.
- 2026-10-07 - Added the lanes-sh/app star history chart to the Status section.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Conductor](../conductor/index.md) - the closest Mac worktree dashboard
- [Orca](../orca/index.md) - the cross-platform, MIT ADE
- [Helmor](../helmor/index.md) - the other local-first worktree workbench
- [Superset](../superset/index.md) - the source-available macOS IDE rival

## References

- https://lanes.sh/ - product overview, the Desktop and Link split, and trust claims
- https://lanes.sh/docs - desktop board, sessions, worktrees, git, editor, MCP, and Link documentation map
- https://lanes.sh/pricing - Free, Pro $19/month, Enterprise custom, and per-second Compute
- https://lanes.sh/llms.txt - agent-readable product description, Link providers, APIs, and CLI install paths
- https://github.com/lanes-sh/app - app repository, README, and the missing license metadata as of 2026-09-27
- https://runany.dev/blog/lanes-parallel-ai-coding-workspace/ - independent walkthrough and critique of the worktree and board model
