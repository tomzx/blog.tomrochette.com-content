---
title: Sandcastle
created: 2026-09-27
updated: 2026-09-27
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
You call `run()` with an agent provider and a sandbox provider: built-in agents are Claude Code, Codex, Pi, Cursor, OpenCode, and Copilot, and built-in sandboxes are Docker and Podman (bind-mount) and Vercel Firecracker microVMs (isolated), plus `noSandbox()` and custom providers built on `createBindMountSandboxProvider` or `createIsolatedSandboxProvider`.
Sandcastle creates a host worktree under a configurable branch strategy, runs the agent inside the sandbox, and merges the resulting commits back.
It captures each agent's native session transcript to the host and can resume or fork a prior Claude Code, Codex, or Pi conversation inside a new sandbox, with `--resume` rewrites so the provider's own resume command works.
Hooks are declared per location (`host` and `sandbox`, for example `onWorktreeReady` and `onSandboxReady`), and templates plus GitHub-issues, beads, or custom issue trackers are scaffolded by `sandcastle init`.

## Status

Small but well-known: about 8,215 stars and 886 forks as of 2026-10-02, created 2026-03-17, and 1,193 commits.
The warning sign is activity: the last commit and the latest release (v0.12.0) both landed on 2026-06-29, so the project has been quiet for more than three months as of 2026-10-02, even as stars kept accruing.
The npm package reached 0.12.0 across 44 versions.
**A popular library that stops shipping while its category moves daily is a bet on stability over feature parity, and an open issue about broken global `npm install` for the Pi and Codex Dockerfiles (#223) has sat unresolved since April 2026.**

## Strengths

- Sandboxing is first-class, not bolted on: three providers plus a documented custom-provider contract, and `noSandbox()` when you want the agent on the host.
- Session capture, resume, and fork let an agent continue its own conversation across sandboxes, which most GUI tools do not expose.
- Provider-agnostic and issue-tracker-agnostic, so it fits an existing CI or pipeline rather than dictating one.
- A real CLI (`init`, templates, flags, non-interactive fail-fast) and typed JS API for programmatic orchestration.
- MIT, by a maintainer with a large TypeScript following, so the docs and examples are unusually good.

## Cautions

- No activity since 2026-06-29; treat it as a maintenance risk and pin a version.
- It is a library, not a product: no board, no diff review UI, no PR flow, no notifications.
- You must provide and pay for your own sandbox runtime; Vercel sandboxes carry their own usage bill.
- The default Dockerfile installs Claude Code as a specific non-root `agent` user, and the documented Pi and Codex installs are reported broken (#223).
- Session capture failure fails the run by default, so a provider upgrade can break a pipeline until you retune.

## Pricing

Free and open source under MIT.
No hosted tier; you pay only for the sandbox runtime you choose (local Docker or Podman, or Vercel usage).
Agent access runs on your own subscriptions or keys.

## Compared to

- [Crewplane](../crewplane/index.md): a Python workflow runner with on-disk run records; choose Sandcastle when you want an in-process TypeScript API instead of a Markdown workflow engine.
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md): a tmux harness for visible Claude Code workers; choose Sandcastle when you want containers and merge-back rather than interactive panes.
- Plain Docker plus a shell script: the zero-dependency option; Sandcastle earns its keep once you need branch strategy, session resume, and hooks.

## Bottom line

**Recommended for teams that want to script sandboxed coding agents from TypeScript and own the pipeline, not adopt a GUI.**
Not for anyone who wants a board, diff review, or a maintained app, given the quiet repository.

## Changes

- 2026-09-27 - Created.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Crewplane](../crewplane/index.md) - the CLI workflow-runner counterpart
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md) - the tmux-based, no-sandbox alternative
- [OpenCode](../../harnesses/opencode/index.md) - one of the harnesses Sandcastle drives
- [Codex](../../harnesses/codex/index.md) - another harness with a built-in Sandcastle provider

## References

- https://github.com/mattpocock/sandcastle - repository, API, sandbox and agent providers, license, stars, last-commit date
- https://raw.githubusercontent.com/mattpocock/sandcastle/HEAD/README.md - `run()`, branch strategy, hooks, session capture, resume and fork
- https://registry.npmjs.org/@ai-hero%2Fsandcastle - package metadata, 0.12.0 latest, 44 versions, version dates and license
- https://www.aihero.dev/open-source - Matt Pocock's framing of Sandcastle among his tools
- https://github.com/mattpocock/sandcastle/issues/223 - unresolved broken global install for Pi and Codex agents
