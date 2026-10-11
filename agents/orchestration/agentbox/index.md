---
title: AgentBox
created: 2026-10-10
updated: 2026-10-10
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, sandboxing, docker, cloud, checkpoints]
readability: 3
audience_notes: >
  Engineers running parallel coding agents who have hit port, browser, and machine-state collisions between worktrees.
  Assumes you know what a Docker container and a cloud VM are.
---

AgentBox is Marco D'Alia's MIT TypeScript CLI that runs coding agents in parallel sandboxed VMs, locally in Docker or on five cloud providers, teleporting the whole project into each box with one command.

**Its bet is that the box, not the worktree, is the right unit of parallel isolation: a full computer per agent (browser, shells, warmed IDE) with sub-second checkpoint starts, so agents stop fighting over ports, browsers, and shared machine state.**

## What it is

`agentbox claude` boots a sandboxed box with your project, skills, plugins, and subscription auth copied in; `agentbox hetzner claude` does the same on Hetzner, and the provider table covers local Docker, remote Docker, Hetzner, Daytona (partial), Vercel, E2B, and DigitalOcean, with the npm package's workspace modules confirming the same provider list.
Checkpoints capture warm box state so a new box starts in under a second from a previous checkpoint and idle boxes auto-pause to stop burning resources; git credentials and tokens never enter the box, and pushes relay through your host with approval shims.
Surfaces are a dashboard (box list plus the selected box's live agent session), attach and detach over tmux sessions, webVNC screen sharing, `.local` URL tunnels for box web apps, a macOS menu-bar tray app, and a provider-plugin SDK for adding your own infrastructure.
MIT, solo-maintained by Marco D'Alia, distributed as the npm package @madarco/agentbox.

## Status

Active and early: 526 stars and 51 forks as of 2026-10-10 on a repository created 2026-05-12, last push 2026-10-07, npm latest 0.33.0, and the tray app at 0.4.3 (2026-09-21).
The Show HN thread from 2026-09-16, posted by the author, drew 4 points and one comment, so the independent footprint outside GitHub and npm is close to zero; the docs site at agent-box.sh returned 503 on both fetch attempts during this check.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=madarco/agentbox&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=madarco/agentbox&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=madarco/agentbox&type=date&legend=top-left" />
</picture>

## Strengths

- The checkpoint mechanism is unique in this category: sub-second warm starts from prior box state, auto-pause for idle boxes, and checkpoints listed and managed as first-class objects.
- The same command runs your agents on a laptop or five clouds, and remote Docker over SSH means any machine you own becomes a provider without a vendor account.
- The credential relay is the trust model sandboxes usually promise and rarely ship: tokens stay on the host, and git or gh calls pass through approval-gated shims.
- The author's own "Firstmate" flow shows the multi-agent use: one lead agent splits a backlog across parallel cloud boxes and drives them with wait-for-idle and plan-approval commands.

## Cautions

- Thin independent footprint: the 4-point Show HN, no third-party coverage in the sources, and a docs site that was down during this check.
- Solo maintainer, 0.x CLI, and a CLA on first contributions.
- An operational floor of Docker plus Node 20.10, with a first box image build of about 1 GB.
- The name collides with at least three unrelated projects (Twill's agentbox-sdk, Zabaca's agent-box, rcarmo's agentbox), so every search for it is polluted.

## Pricing

Free and open source under MIT.
You pay the cloud providers it drives (Hetzner, Vercel, E2B, Daytona, DigitalOcean) at their own rates; AgentBox charges nothing and has no hosted tier.

## Compared to

- [Sandcastle](../sandcastle/index.md): the TypeScript sandbox library with merge-back; choose Sandcastle to script your own pipeline, AgentBox for turnkey boxes, checkpoints, and a dashboard.
- [Scion](../scion/index.md): Google's container hypervisor giving each agent a container, worktree, and credentials; choose Scion for laptop-to-HA fleets, AgentBox for a single-command local-first habit.
- [herdr](../herdr/index.md): the terminal runtime that owns agents' terminals on machines you already have; choose herdr when isolation is not the point, AgentBox when each agent needs a whole computer.

## Bottom line

**Recommended for engineers whose parallel agents collide on ports, browsers, and machine state, especially those who want to burst onto cloud VMs without changing workflow.**
Not for review-centric flows, since there is no diff or PR surface, or for Windows, which the requirements exclude.
My disagreeable claim: **if warm checkpoints work as advertised, the worktree is revealed as a coding-specific hack, and the matrix's worktree row becomes the wrong question for a whole class of tools.**

## Changes

- 2026-10-10 - Created from the sandboxing scan's orchestration-fit flag.

## See also

- [Sandcastle](../sandcastle/index.md) - the closest existing column, the scriptable sandbox library
- [Scion](../scion/index.md) - the container-per-agent hypervisor at datacenter scale
- [herdr](../herdr/index.md) - the terminal-runtime contrast admitted the same day
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this category extends

## References

- https://api.github.com/repos/madarco/agentbox - stars, forks, MIT license, creation and push dates, and topics, as of 2026-10-10
- https://raw.githubusercontent.com/madarco/agentbox/main/README.md - the box model, provider table, checkpoint and credential claims, and requirements
- https://api.github.com/repos/madarco/agentbox/releases?per_page=3 - tray app 0.4.3 (2026-09-21) and the nightly channel
- https://registry.npmjs.org/@madarco/agentbox/latest - npm 0.33.0, engines, and the sandbox provider workspace modules
- https://hn.algolia.com/api/v1/search?query=agentbox&hitsPerPage=8 - the thin HN footprint and the same-named collisions, queried 2026-10-10
- https://news.ycombinator.com/item?id=49728120 - the author's Show HN description of the credential relay and the Firstmate drive flow
