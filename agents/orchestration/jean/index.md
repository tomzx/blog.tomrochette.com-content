---
title: Jean
created: 2026-10-12
updated: 2026-10-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, worktrees, dev-environment, self-hosted]
readability: 3
audience_notes: >
  Engineers who want one workspace for parallel coding agents across a laptop and their own servers.
  Assumes you know what a git worktree is and run at least one CLI coding agent.
---

Jean is an Apache-2.0 dev environment for AI agents from the coolLabs team behind Coolify: a Tauri desktop app (or a headless `jean-server`) that gives every task its own git worktree, runs nine coding CLIs in parallel, and shows local and remote projects in one sidebar.

**Its bet is that local and remote belong in the same window: a server project is not a second tool, it is the same sidebar entry, and closing your laptop does not stop the work.**

## What it is

A Tauri v2, React 19, and Rust desktop app with an opinionated workflow: every task gets a git worktree, agents run in parallel, and git, terminals, reviews, and GitHub, Linear, and Sentry integrations live in one place (README, fetched 2026-10-12).
The same project runs as a headless `jean-server` on any Linux box; the desktop app adds servers over SSH and their projects appear next to local ones, grouped by server, and every instance serves the full UI over HTTP/WebSocket with token auth.
Nine AI backends are supported: Claude, Codex, Cursor, OpenCode, Pi, Command Code, Grok, Kimi Code, and Antigravity (beta), each task choosing its own backend, model, and thinking level.
It comes from coolLabs Solutions Kft., the team behind the 62.9k-star self-hosting platform Coolify, published under Apache-2.0 with the site promising "free forever".

## Status

**Active and shipping weekly from an established self-hosting vendor.**
1,328 stars, 162 forks, 130 open issues, created 2026-01-23, pushed 2026-10-17, latest release v1.0.12 (2026-10-17), as of 2026-10-18 (GitHub API).
The release train runs roughly weekly through October (v1.0.6 on September 24, v1.0.7 on September 29, v1.0.9 on October 7, v1.0.10 on October 13, v1.0.11 on October 14, and v1.0.12 on October 17).
I found no Hacker News thread through 2026-10-12 searches, so its early traction rides the Coolify community (jean.build claims a 20,000-plus Discord) rather than independent coverage.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=coollabsio/jean&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=coollabsio/jean&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=coollabsio/jean&type=date&theme=dark&legend=top-left" />
</picture>

## Strengths

- **Local and remote projects in one sidebar, with work continuing on the server when your laptop closes**: the headless server is an install target from inside the app, not a separate deployment.
- Worktree automation is the core loop: create, archive, restore, delete, labels, filters, multiple sessions per worktree, and checkpoints of GitHub issues or PRs as new worktrees.
- The integration surface is wide for a 1.0: GitHub issues, PRs, security alerts, advisories, Dependabot, checkout-as-worktree, auto-archive on merge, plus Linear and Sentry intake.
- Mr. Robot (beta) polls open GitHub issues, creates one worktree per issue, and drafts plans for approval, the issue-to-agent loop without a separate queue product.
- The opinionated plugins attack the token bill directly: RTK claims 60 to 90 percent cuts on tool output, and every Magic prompt is editable per backend and mode.

## Cautions

- The desktop app is tested on macOS only; Windows and Linux builds are explicitly marked "testers needed" on jean.build, and glibc Linux runs from source.
- 131 open issues against 161 forks says the 1.0.x line is absorbing its first working user base, and the project is eight months old.
- The opinionated defaults are behavior changes by design: RTK rewrites tool output and Caveman makes replies terse, so agents run differently than their stock CLIs.
- One vendor shares velocity with Coolify, so Jean's roadmap competes with a 62.9k-star flagship for the same team's attention.

## Pricing

Pricing does not apply: the app and server are free and Apache-2.0, with jean.build promising "free forever" and sponsorships as the support model.
The costs are the coding-CLI subscriptions and model tokens your backends already bill.

## Compared to

- [Emdash](../emdash/index.md): the other local-plus-remote workspace; Emdash is SSH-first with credentials in the OS keychain, Jean adds the server-as-sidebar model and deeper tracker integrations.
- [Conductor](../conductor/index.md): the polished closed-source Mac incumbent; Jean is open source, cross-platform-bound, and self-hostable.
- [Helmor](../helmor/index.md): the local-first workbench carrying a task through review, test, merge, and one-click PR; Jean's loop stops at PR and relies on the backends' own flows.

## Bottom line

**Recommended for engineers who run several coding CLIs, keep projects on more than one machine, and want worktree-per-task discipline in one Apache-2.0 window.**
Not for Windows or Linux desktop users who need a proven build today, or for anyone who wants a vendor-neutral plugin ecosystem rather than one team's opinions.

## Changes

- 2026-10-12 - Created from the 2026-10-12 candidate scan, with the no-HN-footprint record and the one-vendor risk recorded as the critical angle.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Emdash](../emdash/index.md) - the SSH-first ADE at the adjacent point of the local-remote axis
- [Conductor](../conductor/index.md) - the closed Mac incumbent this undercuts on license
- [Helmor](../helmor/index.md) - the local-first workbench with the deeper merge loop

## References

- https://github.com/coollabsio/jean - repository, 1,328 stars, forks, issues, dates, Apache-2.0 license, and the nine-backend list, as of 2026-10-15 (fetched through the GitHub API)
- https://github.com/coollabsio/jean/blob/main/README.md - architecture (Tauri, React, Rust), jean-server model, integrations, Mr. Robot, and the opinionated plugins
- https://jean.build - product site, "free forever" positioning, macOS-tested caveat, 20k-plus community claim, and the coolLabs Solutions Kft. ownership
- https://api.github.com/repos/coollabsio/jean/releases - the release train v1.0.6 through v1.0.9, as of 2026-10-12
- https://hn.algolia.com/api/v1/search?query=jean%20coollabsio&tags=story - the footprint scan finding no thread (2026-10-12), the community-carried-traction record
- https://api.github.com/repos/coollabsio/coolify - the 62.9k-star Coolify repository grounding the vendor-identity claim, as of 2026-10-12
