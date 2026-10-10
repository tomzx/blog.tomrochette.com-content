---
title: Agentlas OS
created: 2026-10-07
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, hub, orchestrator, local-first, host-embedded]
readability: 3
audience_notes: >
  Engineers wiring specialist agent teams into existing coding-agent hosts, who
  know Squad and OpenRig and will read installers before running them. Assumes
  familiarity with Claude Code or Codex configuration files.
---

Agentlas OS is a local-first hub that keeps specialist agents available and spins up a temporary orchestrator per task, wiring itself into Claude Code, Codex, Cursor, Gemini, and Antigravity hosts.

## What it is

Agentlas OS, created 2026-06-04 and Apache-2.0, ships as a desktop app plus host-embedded runtimes: the hub stores reusable specialist agents and methods, and when work needs a team it brings one, with a temporary orchestrator stood up per task and retired after.
Its installer writes plugin, command, MCP, and hook configuration into the config directories of the hosts it finds (`~/.claude/`, `~/.codex/`, `~/.cursor/`, `~/.gemini/`), so the agents it manages appear inside the coding CLIs you already run rather than in a separate console.
Beside the hub it ships Agent Mail (an inbox and draft-review flow for the orchestrator) and the Agentlas Hub, a public directory for publishing and calling agents.

## Status

Active and young: 1,582 stars, a push on 2026-10-08, and release v1.2.59 on 2026-10-08 as of 2026-10-09 (GitHub API, releases), on a repository created 2026-06-04, one day after v1.2.58.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=agentlas-ai/Agentlas-OS&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=agentlas-ai/Agentlas-OS&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=agentlas-ai/Agentlas-OS&type=date&theme=dark&legend=top-left" />
</picture>

**Two signals cut against the clean story: the README opens with an install block addressed to AI assistants handed only the repository URL, a distribution channel aimed at agents rather than people, and the README itself warns that the installer edits host config files that already exist, so the setup surface is invasive by design.**
I found no Hacker News thread and no independent coverage this run, so 1.6k stars in four months rests on the repository and the vendor's site alone.

## Strengths

- The hub-plus-temporary-orchestrator pattern names something the session managers beside it do not: specialists persist, orchestrators are per-task and disposable.
- Host-embedded operation means the team appears inside Claude Code or Codex instead of beside it.
- Org-chart validation that rejects a review pointing back to an earlier task is a real check on runaway delegation loops.

## Cautions

- The installer rewrites existing host configuration across four home directories, so read `scripts/install-all-runtimes.sh` before running it, which the README itself instructs.
- The economics language (credits, leases, creator settlement, subscription plans) is half-built, and the README states new Hub creator settlement is closed.
- No worktree model is recorded, review lives in org-chart steps and Agent Mail rather than diffs, and four months of history is a short audit trail for something this invasive.

## Pricing

The hub community, desktop app, and agent publishing are free; the README states subscription plans cover Agentlas software and hosted features, with no public price table found as of 2026-10-07, and no prices recorded here.

## Compared to

Squad defines a persistent human-led agent team as versioned repo files inside GitHub Copilot CLI; Agentlas OS is the host-agnostic, hub-backed version of that idea.
OpenRig defines a cross-harness team in YAML and restores it by name; choose OpenRig for a terminal-native team you own end to end.
oh-my-codex adds worktree teams, skills, and memory specifically to Codex CLI; choose it when Codex is the only host.

## Bottom line

Recommended for engineers who want persistent specialists orchestrated per task inside the coding CLIs they already run, and who will audit the installer first.
Not for locked-down machines where an installer that rewrites host configuration across home directories is a non-starter.

## Changes

- 2026-10-07 - Created.
- 2026-10-08 - Recorded v1.2.58 (October 8) and the star count as of 2026-10-08.
- 2026-10-09 - Recorded v1.2.59 (October 8) and refreshed the star count to 1,582 as of 2026-10-09.

## See also

- [Squad](../squad/index.md) - the repo-files agent team inside GitHub Copilot CLI, the closest pattern comparison.
- [OpenRig](../openrig/index.md) - the YAML-defined cross-harness team with snapshot restore.
- [oh-my-codex](../oh-my-codex/index.md) - the Codex-specific workflow layer with worktree teams.
- [Omnara](../omnara/index.md) - the control-plane alternative that owns execution state instead of embedding in hosts.

## References

- https://github.com/agentlas-ai/Agentlas-OS - the repository, README host list, hub economics, stars, and releases.
- https://agentlas.cloud - the project site and its "Put an AI team on your next idea" positioning.
- https://agentlas.cloud/desktop - the desktop download page for macOS, Windows, and Linux.
- https://raw.githubusercontent.com/agentlas-ai/Agentlas-OS/main/scripts/install-all-runtimes.sh - the installer script, including the AI-facing install block and the host config files it writes.
- https://github.com/agentlas-ai/Agentlas-OS/releases - the release list, v1.2.57 (2026-10-06) latest at verification.
