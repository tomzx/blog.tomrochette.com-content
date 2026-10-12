---
title: CodeNomad
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surfaces, opencode, desktop, session-cockpit, open-source]
readability: 3
audience_notes: >
  Engineers running OpenCode V2 who want a desktop cockpit for their sessions, with worktrees,
  phone remote control, and browser access, profiled against OpenChamber, bb, and Cate.
  Assumes you know what OpenCode and Git worktrees are.
---

CodeNomad is an MIT desktop and browser workspace for OpenCode V2: projects, nested sessions, worktrees, diff review, MCP and plugin management, and a self-hosted server mode, with phone pairing through an OpenTunnel relay.

**Its bet is that OpenCode's shared background service is the engine and a cockpit can be a separate desktop product, which makes CodeNomad the first OpenCode-centric surface that is desktop-first rather than web-first.**

## What it is

An Electron or Tauri desktop app plus a browser client, built by the NeuralNomadsAI organization (created 2025-11-14), speaking to one shared OpenCode V2 background service (2.0.7 minimum, 2.0.21 recommended for 0.20.1); OpenCode owns the sessions, messages, and agent execution, and closing CodeNomad leaves the service running.
The surface covers projects with per-window tabs and drafts, full-history session search with a timeline and forks, worktree creation and session moves, rich conversations (markdown, diffs, tool-result images, reasoning visibility, a `/btw` side question), background shells, MCP connection and plugin management, agent-driven browser previews, voice input, and SideCars, tabs that proxy web tools running on the server host (including an OpenVSCode Server container).
The CodeNomad Server (`npx @neuralnomads/codenomad`) serves the same workspace from your machine with password authentication and self-signed HTTPS, and Remote Control pairs a phone or another computer through an OpenTunnel relay without opening ports, TLS ending on your machine.

## Status

**Active on a daily train, young, and without independent coverage.**
2,620 stars, 177 forks, and 21 open issues and pull requests, created 2025-11-01, pushed 2026-10-12, as of 2026-10-12 (GitHub API).
Stable v0.20.1 (2026-10-03) after v0.20.0 (2026-09-25), with a daily `v0.20.1-dev` release train running through the writing of this note.
The server package drew 1,267 npm downloads in the month ending 2026-10-10.
A Hacker News search returns no story about the project (2026-10-11), only substring matches, so the footprint is GitHub-side.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=NeuralNomadsAI/CodeNomad&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=NeuralNomadsAI/CodeNomad&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=NeuralNomadsAI/CodeNomad&type=date&legend=top-left" />
</picture>

## Strengths

- **Desktop-first does change the job**: per-window project tabs, drafts, view restoration, and voice input are things a browser cockpit reaches awkwardly, and the Tauri build keeps the footprint smaller than Electron.
- The remote-control story is the most complete in the category: your own server, password auth, HTTPS, and phone pairing through a relay that terminates TLS on your machine, no port forwarding.
- OpenCode compatibility is treated as a contract, with a minimum and recommended CLI version validated at startup rather than assumed.
- SideCars are a quiet good idea: any web tool on the server host becomes a tab in the workspace, which is how a second editor or a browser IDE joins an OpenCode session.

## Cautions

- **One-harness commitment**: OpenCode V2 only, with V1 and the former V2 beta explicitly unsupported, so your surface choice is chained to one engine's release cadence.
- The dev train outpaces the stable channel (multiple dev releases per day against one stable in October so far), and the 0.20 UI requires a matching 0.20 server, so remote users must upgrade in step.
- First remote launch shows a self-signed-certificate warning by design; teams that cannot click through it need the HTTPS configuration path documented in the server README.
- No Hacker News footprint and no third-party reviews found, so the 2.6k stars are uncorroborated by public discussion.

## Pricing

Pricing does not apply: the app and server are free and MIT, with no hosted tier.
The costs are your OpenCode subscriptions or API keys and the machine that runs the shared service.

## Compared to

- [OpenChamber](../openchamber/index.md): the other OpenCode-centric cockpit; OpenChamber is web-first with the deepest OpenCode feature coverage, CodeNomad is desktop-first with remote control, voice, and SideCars.
- [bb](../bb/index.md): the self-building agent IDE that drives any provider CLI; bb is broader and Mac-silicon-forward, CodeNomad is narrower and OpenCode-committed.
- [Cate](../cate/index.md): the canvas workspace where agent terminals become territories; Cate visualizes many agents spatially, CodeNomad organizes sessions hierarchically per project.

## Bottom line

**Recommended for OpenCode V2 users who want a native desktop cockpit, worktree-per-session organization, and phone remote control they can self-host.**
Not for multi-harness users (bb or a plain terminal covers that), and not for teams that need a vendor to call when the dev train breaks a remote setup.
My disagreeable claim: two serious cockpits around one harness is the correct market density, not duplication, because OpenCode's service contract has become a platform layer and platforms get one client per interaction model.

## Changes

- 2026-10-11 - Created after the owner-star entrant scan flagged the repository, with the one-harness commitment and the stable-versus-dev train gap recorded as the central cautions.

## See also

- [OpenChamber](../openchamber/index.md) - the web-first OpenCode cockpit this note's closest comparison
- [bb](../bb/index.md) - the desktop IDE that builds itself, the multi-harness alternative
- [Codeg](../codeg/index.md) - the session-aggregating workspace with native mobile clients
- [Surface Feature Matrix](../surface-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/NeuralNomadsAI/CodeNomad - repository facts: 2,620 stars, 177 forks, MIT, created 2025-11-01, pushed 2026-10-12 (GitHub API, as of 2026-10-12)
- https://raw.githubusercontent.com/NeuralNomadsAI/CodeNomad/main/README.md - the feature set, OpenCode V2 version contract, SideCars, remote control, and install paths (fetched 2026-10-11)
- https://raw.githubusercontent.com/NeuralNomadsAI/CodeNomad/main/packages/server/README.md - the server mode: remote access, authentication, prerequisites, deployment model
- https://api.github.com/repos/NeuralNomadsAI/CodeNomad/releases - stable v0.20.1 (2026-10-03), v0.20.0 (2026-09-25), and the daily dev train
- https://api.npmjs.org/downloads/point/last-month/@neuralnomads/codenomad - 1,267 downloads in the month ending 2026-10-10
- https://hn.algolia.com/api/v1/search?query=CodeNomad&tags=story - the footprint scan finding no dedicated story (2026-10-11)
