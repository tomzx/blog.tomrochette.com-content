---
title: Symphony
created: 2026-10-10
updated: 2026-10-10
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, elixir, openai]
readability: 3
audience_notes: >
  Engineers deciding whether OpenAI's spec-first issue-to-implementation runner fits their team, and what the spec-first packaging really commits them to.
  Assumes you know what an issue tracker, a coding-agent harness, and a git worktree are.
---

Symphony is OpenAI's Apache-2.0 orchestration service that polls an issue tracker, gives each issue an isolated workspace, and runs an autonomous coding-agent session until the work reaches a handoff state such as Human Review or a merged PR.

**Its bet is that the deliverable is the spec, not the app: SPEC.md defines the scheduler in language-agnostic RFC-2119 terms, an Elixir reference implementation is offered as a prototype, and teams are told to harden or reimplement their own.**

## What it is

A long-running daemon (OpenAI calls it a "low-key engineering preview for testing in trusted environments") that reads candidate work from a tracker on a fixed cadence, dispatches with bounded concurrency, and keeps workflow policy in a repo-committed WORKFLOW.md so prompts and runtime settings version with the code.
The reference implementation drives Codex in App Server mode and ships tracker adapters for Linear, GitHub Issues, Jira Cloud, Asana, and GitLab, executing provider-native tools host-side so the agent child process never holds raw tracker tokens.
Per-issue workspaces are deterministic and preserved across runs, terminal-state issues stop their active runs, and restart recovery is tracker- and filesystem-driven with no persistent database.
It is made by OpenAI, works best in codebases that have adopted its harness-engineering practice (its own README's positioning), and self-contained executables ship via Burrito alongside the mise-managed Elixir setup.

## Status

Quiet preview: 27,630 stars as of 2026-10-11 on a repository created 2026-02-26 (GitHub API), with both the default branch and the release line last touched 2026-09-15, 26 days before this check.
The GitHub release line holds four tags: v0.0.2 (2026-07-24), v0.0.3 and a nightly (both 2026-09-15), and nothing since.
The Elixir reference implementation carries its own warning that it is prototype software for evaluation only.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=openai/symphony&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=openai/symphony&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=openai/symphony&type=date&legend=top-left" />
</picture>

**The independent footprint is thin for 27.6k stars: the biggest Hacker News thread about it is 25 points with three comments (2026-03-04), and the sharpest comment there calls the spec "inscrutable agent slop" that lists database fields without describing its own state machine.**
The spec has nonetheless spawned third-party implementations, including a one-file sandboxed example, a Codex-and-Linear bootstrap, and a Go port called Contrabass, which is evidence the contract, not the code, is what spread.

## Strengths

- The spec-first packaging makes the orchestration contract portable: any team can implement Symphony in its own language and own the hardening.
- Host-side credential handling is a design point: tracker tools execute with host-held tokens and declared secrets are stripped from the agent's environment.
- The WORKFLOW.md contract keeps prompts, statuses, and runtime policy versioned in the repo, and runs recover from tracker and filesystem state without a database.

## Cautions

- The reference implementation is a self-declared prototype for trusted environments, and the spec deliberately leaves approval, sandbox, and confirmation policy implementation-defined, so safety is whatever the implementer builds.
- The release train stopped at v0.0.3 on 2026-09-15 with preview warnings in both READMEs, so there is no supported product here.
- The reference implementation couples to Codex in App Server mode and to non-standard Linear statuses (Rework, Human Review, Merging) that a team must add to its workflow.
- Blocked-issue state lives in memory only and clears on restart, so a restart can re-dispatch work a human had parked.

## Pricing

Free and open source under Apache-2.0; you bring the Codex subscription and the tracker credentials, and OpenAI charges nothing for the service itself as of 2026-10-10.
No price history table until a paid tier exists.

## Compared to

- [Archon](../archon/index.md): the committed-YAML workflow engine over Claude Code and Codex SDKs; choose Archon for process-as-workflows with triggers, Symphony for issue-tracker-driven autonomous runs under a portable spec.
- [Bernstein](../bernstein/index.md): the deterministic scheduler with merge gates and audit receipts; Bernstein owns verification policy, Symphony owns work intake.
- [Agent Swarm](../agent-swarm/index.md): the lead/worker intake platform shipping PRs from chat and issue intake; Agent Swarm is a product you deploy, Symphony is a contract you implement.

## Bottom line

**Recommended for teams already running harness-engineered repos on Linear or GitHub Issues who want issue-driven autonomous runs and accept that they are adopting a spec plus a prototype.**
Not for anyone who needs a supported product, a UI-first session supervisor, or non-Codex agents from the reference implementation.
My disagreeable claim: **the 27.6k stars measure OpenAI's brand on a preview, because a 25-point launch thread, a train stopped since mid-September, and a reference implementation its own authors call prototype make this a design document wearing a repository's clothes.**

## Changes

- 2026-10-10 - Created from the orchestration entrant scan, the queue-flagged carve-out from the mission-control-tail family rejection.

## See also

- [Archon](../archon/index.md) - the closest committed-workflow runner in the category
- [Bernstein](../bernstein/index.md) - the deterministic-scheduler alternative for policy-owned coordination
- [Agent Swarm](../agent-swarm/index.md) - the deployable product counterpart for issue-to-PR intake
- [Crewplane](../crewplane/index.md) - the Markdown-workflow runner with on-disk run records
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/openai/symphony - repository, README positioning, preview warning, and license
- https://api.github.com/repos/openai/symphony - stars, created and pushed dates, and license, as of 2026-10-10
- https://api.github.com/repos/openai/symphony/releases - the release line: v0.0.2 (2026-07-24), v0.0.3 and nightly (2026-09-15)
- https://raw.githubusercontent.com/openai/symphony/main/SPEC.md - Draft v1 spec: problem statement, goals, non-goals, and implementation-defined policy
- https://raw.githubusercontent.com/openai/symphony/main/elixir/README.md - the reference implementation: Codex App Server mode, five tracker adapters, host-side auth, blocked-state behavior
- https://hn.algolia.com/api/v1/search?query=openai%20symphony&tags=story - the thin HN footprint, queried 2026-10-10
- https://hn.algolia.com/api/v1/items/47252045 - the 25-point launch thread with the "inscrutable agent slop" spec critique
