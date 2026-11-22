---
title: Agentlas OS
created: 2026-10-07
updated: 2026-11-22
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

Active and young: 1,583 stars, a push on 2026-11-18, and release os-v1.2.99 on 2026-11-17 (memory rules 1.17.0: what a person says about their own life kept as a `fact` every agent of theirs uses, `preference` scoped to how one agent answers them, and a `boundary` object accepted by `memory.record` and the ticket schema) after os-v1.2.98 on 2026-11-15 (the memory-layout release: memory kept in four places, personal, agent, project, and session, read across with one recall rule, `memory.record` writes by the working model, agent folders under `~/.agentlas/agents`, and a Windows long-path fix) after v1.2.97 on 2026-11-13 after v1.2.95 on 2026-11-09 (an `os-v1.2.96` tag the same day), v1.2.88 on 2026-11-07, and v1.2.86 on 2026-11-06 (v1.2.71 was October 29, v1.2.70 October 27, and v1.2.67 October 20, when Hub search candidates began carrying their own listing taglines) as of 2026-11-19 (GitHub API, releases), on a repository created 2026-06-04.
Beside the engine line the README now fronts a desktop product: Agentlas Desktop, a macOS, Windows, and Linux app distributed through the separate agentlas-desktop-releases repository, whose release list sits at 2.0.11 (2026-11-22), with an Android phone app on Google Play, an iOS app promised, and a self-reported 12,000-plus desktop downloads claim, the README commits of 2026-11-21 having retitled the pitch around this "2.0 desktop app" and "2.0 phone app" (README re-fetched 2026-11-22).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=agentlas-ai/Agentlas-OS&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=agentlas-ai/Agentlas-OS&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=agentlas-ai/Agentlas-OS&type=date&legend=top-left" />
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
- The desktop push brought monetization signals: the README carries an affiliate partner banner (Infistar.cc, an AI-subscription reseller signing users up under an AGENTLASOS referral code) and the 12,000-plus download claim is self-reported, so discount the traction numbers accordingly.

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
- 2026-10-10 - Recorded v1.2.61 (October 10) and refreshed the star count to 1,575 as of 2026-10-10.
- 2026-10-20 - Recorded v1.2.67 (2026-10-20, Hub search candidates carry listing taglines) on the release train.
- 2026-10-25 - Recorded v1.2.69 (2026-10-25) on the release train.
- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart markup (the light source carried the dark-theme parameter; the theme parameter now sits only on the dark source).
- 2026-10-27 - Recorded v1.2.70 (2026-10-27): native delegation from prepared agents on the current host, package read allowlists, and receipt telemetry that no longer blocks authorized host work.
- 2026-11-01 - Recorded v1.2.72 (2026-11-01) as the latest release and the same-day push.
- 2026-11-04 - Recorded v1.2.82 (2026-11-03) as the latest release, the push date refreshed to 2026-11-04.
- 2026-11-06 - Volatile refresh: Recorded v1.2.86 (2026-11-06) as the new latest release.
- 2026-11-13 - Volatile refresh: Recorded v1.2.97 (2026-11-13) as the latest release, the push date refreshed to 2026-11-13.
- 2026-11-16 - Recorded os-v1.2.98 (2026-11-15, the four-place memory layout with `memory.record` writes and a Windows long-path fix) as the latest release, the push date refreshed to 2026-11-15.
- 2026-11-19 - Volatile refresh: recorded os-v1.2.99 (2026-11-17, memory rules 1.17.0 splitting `fact` from `preference` with a `boundary` object on `memory.record`), the push date refreshed to 2026-11-18.
- 2026-11-22 - Volatile refresh: recorded the desktop push, the 2026-11-21 README commits retitling the pitch around the Agentlas Desktop 2.0 app (agentlas-desktop-releases at 2.0.11, 2026-11-22) and the 2.0 phone app on Google Play, plus the affiliate partner banner and the self-reported 12,000-plus download claim, the engine release line unmoved at os-v1.2.99.

## See also

- [Squad](../squad/index.md) - the repo-files agent team inside GitHub Copilot CLI, the closest pattern comparison.
- [OpenRig](../openrig/index.md) - the YAML-defined cross-harness team with snapshot restore.
- [oh-my-codex](../oh-my-codex/index.md) - the Codex-specific workflow layer with worktree teams.
- [Omnara](../omnara/index.md) - the control-plane alternative that owns execution state instead of embedding in hosts.

## References

- https://github.com/agentlas-ai/Agentlas-OS - the repository, README host list, hub economics, stars, and releases.
- https://github.com/agentlas-ai/agentlas-desktop-releases - the separate desktop distribution repository, Agentlas Desktop 2.0.11 (2026-11-22) its latest release (fetched 2026-11-22).
- https://agentlas.cloud - the project site and its "Put an AI team on your next idea" positioning.
- https://agentlas.cloud/desktop - the desktop download page for macOS, Windows, and Linux.
- https://raw.githubusercontent.com/agentlas-ai/Agentlas-OS/main/scripts/install-all-runtimes.sh - the installer script, including the AI-facing install block and the host config files it writes.
- https://github.com/agentlas-ai/Agentlas-OS/releases - the release list, v1.2.57 (2026-10-06) latest at verification.
