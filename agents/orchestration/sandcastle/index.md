---
title: Sandcastle
created: 2026-09-27
updated: 2026-11-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, orchestration, sandboxing, typescript, library]
readability: 3
audience_notes: >
  Engineers who want to script coding agents from their own TypeScript rather than adopt a GUI.
  Assumes you run Docker, Podman, or Vercel sandboxes and are comfortable wiring an npm library.
---

Sandcastle is an MIT-licensed TypeScript library and CLI that orchestrates coding agents in isolated sandboxes, running them in a worktree, collecting the commits, and merging the branches back.

**Sandcastle's bet is that the orchestrator should be an npm package, not an app: one `sandcastle.run()` call gives you sandboxing, branch strategy, session capture, and merge-back, so teams compose their own pipelines instead of adopting a board.**

## What it is

A library from Matt Pocock (Total TypeScript, ex-Vercel and Stately) published as `@ai-hero/sandcastle`, with a CLI that scaffolds a `.sandcastle/` config directory and a default Dockerfile.
You call `run()` with an agent provider and a sandbox provider: built-in agents are Claude Code, Codex, Pi, Cursor, OpenCode, and Copilot, and built-in sandboxes are Docker and Podman (bind-mount), Vercel Firecracker microVMs, E2B, Modal, and Fly.io Sprites (isolated cloud), and native OS-process sandboxes (`bwrap()` on Linux and WSL2, `seatbelt()` on macOS, the documented default since v0.13.0), plus Daytona, `noSandbox()`, and custom providers built on `createBindMountSandboxProvider` or `createIsolatedSandboxProvider`.
Sandcastle creates a host worktree under a configurable branch strategy, runs the agent inside the sandbox, and merges the resulting commits back.
It captures each agent's native session transcript to the host and can resume a prior Claude Code, Codex, Pi, Copilot, Cursor, or OpenCode conversation inside a new sandbox (fork as well for Claude Code, Codex, Pi, and OpenCode), with resume rewrites so the provider's own resume command works.
Hooks are declared per location (`host` and `sandbox`, for example `onWorktreeReady` and `onSandboxReady`), and templates plus GitHub-issues, beads, or custom issue trackers are scaffolded by `sandcastle init`.

## Status

Small but well-known: about 8,366 stars and 894 forks as of 2026-10-11, created 2026-03-17, and more than 1,830 commits as of 2026-11-07.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=mattpocock/sandcastle&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=mattpocock/sandcastle&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=mattpocock/sandcastle&type=date&legend=top-left" />
</picture>

The activity picture flipped on 2026-11-02: after five months with no release (v0.12.0, 2026-06-29) and a maintenance trickle from 2026-10-02 (a Docker-based issue-triage skill merged through PR #1013, then CI and template fixes through 2026-10-19), the project shipped v0.13.0 and v0.14.0 the same day (GitHub releases, as of 2026-11-03).
v0.13.0 made native OS-process sandboxes the documented default (`bwrap()` on Linux and WSL2, `seatbelt()` on macOS 14 or later, no image and no daemon), added session resume to Copilot, Cursor, and OpenCode (fork for OpenCode), and closed two sandbox-escape paths (host git commands that ignored repository hooks and planted PATH entries, and sync-out writing outside the worktree, now refused with `SyncOutPathError`).
v0.14.0 added isolated cloud providers for E2B, Modal, and Fly.io Sprites beside Vercel and Daytona, and hardened Docker and Podman so the worktree's admin directories cannot be renamed from inside the sandbox.
The npm package now publishes 0.14.0.
**Five months without a release while the category moved daily remains the caution this note was built on, but the 2026-11-02 pair is a feature return rather than maintenance: the sandbox provider set widened from three to nine, and the resume surface now covers six agents.**

## Strengths

- Sandboxing is first-class, not bolted on: nine providers across native, container, and cloud classes, a documented custom-provider contract, and `noSandbox()` when you want the agent on the host.
- Session capture, resume, and fork let an agent continue its own conversation across sandboxes, which most GUI tools do not expose.
- Provider-agnostic and issue-tracker-agnostic, so it fits an existing CI or pipeline rather than dictating one.
- A real CLI (`init`, templates, flags, non-interactive fail-fast) and typed JS API for programmatic orchestration.
- MIT, by a maintainer with a large TypeScript following, so the docs and examples are unusually good.

## Cautions

- The release train only restarted on 2026-11-02 after five months silent (v0.12.0, 2026-06-29); the maintenance-trickle record earned its caution, so pin a version and test the new sandbox providers against your runtime before you depend on them.
- It is a library, not a product: no board, no diff review UI, no PR flow, no notifications.
- You must provide and pay for your own sandbox runtime; Vercel sandboxes carry their own usage bill.
- The default Dockerfile still installs Claude Code as a specific non-root `agent` user, a structure that produced broken Pi and Codex installs once (#223); the fix landed the same day it was reported (PR #224, 2026-04-03), but custom images deserve a build test.
- Session capture failure fails the run by default, so a provider upgrade can break a pipeline until you retune.

## Pricing

Free and open source under MIT.
No hosted tier; you pay only for the sandbox runtime you choose (local Docker or Podman, or billed usage on Vercel, E2B, Modal, Fly.io Sprites, or Daytona).
Agent access runs on your own subscriptions or keys.

## Compared to

- [Crewplane](../crewplane/index.md): a Python workflow runner with on-disk run records; choose Sandcastle when you want an in-process TypeScript API instead of a Markdown workflow engine.
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md): a tmux harness for visible Claude Code workers; choose Sandcastle when you want containers and merge-back rather than interactive panes.
- Plain Docker plus a shell script: the zero-dependency option; Sandcastle earns its keep once you need branch strategy, session resume, and hooks.

## Bottom line

**Recommended for teams that want to script sandboxed coding agents from TypeScript and own the pipeline, not adopt a GUI.**
Not for anyone who wants a board, diff review, or a maintained app.

## Changes

- 2026-09-27 - Created.
- 2026-10-03 - Status move: recorded the default branch waking on 2026-10-02 with two maintenance commits (a Docker-based issue-triage skill, PR #1013) after three quiet months, with no new release, and refreshed star and fork counts.
- 2026-10-07 - Added the mattpocock/sandcastle star history chart to the Status section.
- 2026-10-19 - Recorded the maintenance trickle continuing through 2026-10-18 (a CI fix moving agent workflows off `pull_request_target`, a Codex `.env` template key fix), still with no new release.
- 2026-10-27 - Refreshed the maintenance-trickle record through 2026-10-19 (the out-of-date docs site removed); no release past v0.12.0.
- 2026-11-03 - Status move: the five-month release gap closed with v0.13.0 and v0.14.0 on 2026-11-02 (native sandboxes as the documented default, session resume for Copilot, Cursor, and OpenCode, E2B, Modal, and Fly.io Sprites providers, and two sandbox-escape security fixes); corrected the #223 record (closed the same day it was reported, PR #224) and replaced the dead aihero.dev/open-source reference with the published docs site.
- 2026-11-08 - Re-verified in rotation: all cited sources re-fetched and live (repo, README, npm at 0.14.0, the published docs site, both release tags, issue #223); claims hold, v0.14.0 still the latest release, quiet since the 2026-11-02 pair.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Crewplane](../crewplane/index.md) - the CLI workflow-runner counterpart
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md) - the tmux-based, no-sandbox alternative
- [OpenCode](../../harnesses/opencode/index.md) - one of the harnesses Sandcastle drives
- [Codex](../../harnesses/codex/index.md) - another harness with a built-in Sandcastle provider

## References

- https://github.com/mattpocock/sandcastle - repository, API, sandbox and agent providers, license, stars, last-commit date
- https://raw.githubusercontent.com/mattpocock/sandcastle/HEAD/README.md - `run()`, branch strategy, hooks, session capture, resume and fork
- https://registry.npmjs.org/@ai-hero%2Fsandcastle - package metadata, 0.14.0 latest, version dates and license
- https://www.aihero.dev/sandcastle - the published documentation (the previously cited aihero.dev/open-source page now returns 404)
- https://github.com/mattpocock/sandcastle/releases/tag/v0.13.0 - native sandboxes as default, session resume for Copilot, Cursor, and OpenCode, and the sandbox-escape security fixes
- https://github.com/mattpocock/sandcastle/releases/tag/v0.14.0 - E2B, Modal, and Fly.io Sprites providers and the Docker/Podman admin-directory hardening
- https://github.com/mattpocock/sandcastle/issues/223 - broken global install for Pi and Codex agents, closed as completed by PR #224 the same day
