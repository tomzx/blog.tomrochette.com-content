---
title: Container Use
created: 2026-10-12
updated: 2026-10-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, sandboxing, containers, mcp, isolation, git, open-source]
readability: 3
audience_notes: >
  Engineers running several coding agents against one repository who want each agent
  in its own environment and each environment reviewable with git.
  Assumes you know what Docker containers, git worktrees, and MCP are.
---

Container Use is Dagger's Apache-2.0 Go MCP server and CLI that gives each coding agent its own containerized environment on its own git branch, so several agents work in parallel and their changes are reviewed with plain git.

**It is the only member of the category that makes environment creation an agent-side act: the agent calls MCP tools to spin up its own containers, and the branch is the review surface.**

## What it is

An MCP server (`container-use stdio`) that any MCP-compatible agent mounts, powered by Dagger for container workflows and git worktrees for branching, installable with Homebrew or a shell script on any host with Docker and Git.
Each environment is a fresh container plus a branch: the agent runs commands, edits files, and serves URLs inside it, while your working copy stays untouched until you merge or cherry-pick what you want.
A companion CLI (`cu`, with `container-use` as the long form) lists environments, streams command history and logs, and drops you into an environment's terminal for direct intervention.
The docs document configuration helpers for fifteen agent clients, including Claude Code, Codex, Cursor, Goose, GitHub Copilot, Amazon Q, Cline, Windsurf, Zed, Sourcegraph Amp, Kilo Code, Qodo Gen, and Kiro.
Built by Dagger, the containers-as-CI company; the project carries an experimental stability badge.

## Status

Star-heavy and development-light: 4.1k stars and about 36 contributors as of 2026-10-12, created 2025-05-23, pushed 2026-09-21, Apache-2.0.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=dagger/container-use&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=dagger/container-use&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=dagger/container-use&type=date&legend=top-left" />
</picture>

The Show HN launch on 2025-06-05 drew 82 points, the category's mid-sized launch.
The release train stopped at v0.4.2 on 2025-08-19, and no release has followed in the fourteen months since.
2026 brought three commit days: one in February, one in June, and an August 11-12 burst of seven commits that shipped a path-traversal fix for the environment export path (issue #337), with the last repository push on 2026-09-21.
**The boundary works and the docs are live, but an experimental badge, a dead release train, and a handful of 2026 commits read as a slowed project the Dagger team parked, not an actively maintained one.**

## Strengths

- Parallel multi-agent workflow built in: each agent gets its own container and branch, so ten agents never collide on one checkout.
- The review tool is git itself: `git checkout <branch>` shows any agent's work, with `cu` adding command history and logs of what the agent did.
- The secrets model keeps values away from the model: `op://`, `env://`, `vault://`, and `file://` references resolve in-container, and values are stripped from logs and command outputs.
- The widest documented MCP-client coverage in the category, with per-agent configuration helpers.

## Cautions

- Development slowed: no release since 2025-08-19, three commit days in all of 2026, and the experimental badge still up.
- The container boundary shares the host kernel, and no audit or threat model is published; the August 2026 path-traversal patch shows the environment-export surface needed a security fix within living memory.
- No documented egress policy or network controls: environments get normal container networking, unlike CubeSandbox's per-domain policy or Brood Box's profiles.
- Requires Docker and Git on the host, with Dagger's engine doing the container work underneath.

## Pricing

Free and open source under Apache-2.0; the costs are Docker host resources and your own agent subscriptions.
No hosted tier or pricing page exists as of 2026-10-12.

## Compared to

- [Yolobox](../yolobox/index.md): the container wrapper for one operator-run agent with full sudo; Container Use makes environments the agent's own act and adds branch-scoped review.
- [Brig](../brig/index.md): the microVM boundary with a stronger kernel story; Brig runs one agent per VM, Container Use trades kernel strength for cheap parallel environments.
- [Flue](../flue/index.md): the framework that embeds sandbox tiers in TypeScript agents; choose Container Use for a language-agnostic MCP bolt-on to an agent you already run.

## Bottom line

**Recommended for engineers running several agents on one repository who want isolation plus a git-native review loop, and who accept an experimental project whose release train has stopped.**
Not for untrusted-code isolation (the kernel is shared and no egress policy exists), or for teams that require maintained releases or an audited boundary.

## Changes

- 2026-10-12 - Created from the 2026-10-12 entrant-resolution scan (two sources), profiling the category's container-workflow entrant with the stalled release train recorded as the central caution.

## See also

- [Sandboxing Feature Matrix](../sandboxing-feature-matrix/index.md) - the category comparison this note joins
- [Yolobox](../yolobox/index.md) - the other container-boundary member, wrapper-style instead of agent-created
- [Brig](../brig/index.md) - the microVM alternative when the kernel boundary matters more than parallelism
- [Microsandbox](../microsandbox/index.md) - the other member whose agent can create sandboxes itself
- [Flue](../flue/index.md) - the framework-side take on sandbox tiers

## References

- https://github.com/dagger/container-use - repository, 4.1k stars, contributor count, dates, license, README mechanism, as of 2026-10-12
- https://container-use.com - documentation introduction: MCP server, Dagger containers plus git worktrees, environment model
- https://container-use.com/quickstart.md - Docker and Git requirements, install paths, the MCP wiring
- https://container-use.com/secrets.md - the four secret-reference schemas, in-container resolution, log and output stripping
- https://container-use.com/environment-configuration.md - default environment config, agent adaptations, the import workflow
- https://container-use.com/agent-integrations.md - the documented agent-client coverage
- https://api.github.com/repos/dagger/container-use/releases - the release record ending at v0.4.2 (2025-08-19)
- https://hn.algolia.com/api/v1/items/44193933 - the 82-point Show HN launch of 2025-06-05
