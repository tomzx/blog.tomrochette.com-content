---
title: The Perfect Orchestrator
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, orchestration, tmux, verification, claude-code]
readability: 3
audience_notes: >
  Engineers who run Claude Code and want a minimal, scriptable multi-agent harness with adversarial verification.
  Assumes you use tmux and are comfortable with shell scripts and shared Claude credentials.
---

The Perfect Orchestrator is an MIT-licensed bash and tmux harness in which one lead Claude Code session spawns, briefs, monitors, and adversarially verifies multiple autonomous Claude Code worker sessions through plain files, with no daemons or servers.

**Its thesis is that workers lie, so findings do not count until a different worker has tried to tear them apart, and the whole coordination layer is deliberately plain files rather than a broker.**

## What it is

A Claude Code plugin (installed with `claude plugin marketplace add daman8271/the-perfect-orchestrator`) from a solo developer, danny (daman8271).
You talk to one lead session; it spawns N fully interactive Claude Code workers in tmux panes, writes each a task brief, watches their screens, nudges the ones that drift, and lets them coordinate through a shared `bus.md` message bus.
Each worker appends lines prefixed with its ID, reads peers' findings, writes `agent-n.result.md`, and touches a done flag; the lead reads results and cross-checks each finding with a different worker before reporting anything.
Coordination is plain files (briefs, bus, results, done flags), so there are no servers, daemons, or message brokers, and the lead stays live to monitor, correct, and re-plan mid-flight.
The README includes a comparison table against SDK and headless approaches, a security model, and a roadmap.

## Status

Quiet and tiny: about 1 star and 1 fork as of 2026-09-27, created 2026-06-05, with the last commit on 2026-06-30 and a latest release of v0.2.0 (2026-06-06).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=daman8271/the-perfect-orchestrator&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=daman8271/the-perfect-orchestrator&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=daman8271/the-perfect-orchestrator&type=date&legend=top-left" />
</picture>

It is a single-author project with no community footprint on Hacker News or Reddit during this run; the README notes the recorded fleet run and a website that it says were themselves built and QA'd by the tool's own fleet.
The Awesome Multi-Agent Orchestrators directory removed it on 2026-10-05 (PR 64, among seven low-star players), which a 1-star repository will not feel, but which records the curator's verdict.
**A one-star repository with a three-month-old last commit is best read as a well-documented pattern to copy, not a dependency to adopt.**

## Strengths

- Adversarial verification is a first-class design, not an afterthought: a finding needs a different worker's failed attempt to refute it.
- No infrastructure: plain files mean nothing to deploy, and a human can read the entire coordination state.
- Workers are full interactive sessions, so the lead and the human can watch a worker go down a rabbit hole and yank it back.
- A thoughtful security model with a documented allowlist, an isolated config dir, and explicit advice to run fleets on a VPS or in a container.
- It cost nothing to try: a plugin install and a `tmux` requirement.

## Cautions

- Effectively a single-author, single-star project; no maintainer community and no activity since 2026-06-30.
- Requires Linux or macOS, `tmux` 3.0+, and a Claude Code login, and it runs only Claude Code.
- Workers consume real Claude plan usage in parallel; the FAQ is explicit that fleets trade tokens for wall-clock time.
- Workers run with a generous permission allowlist (though `rm` is not allowlisted), so it is unsafe to point at the only copy of anything.
- The roadmap's most useful pieces (`orch verify`, `orch demo`, `orch watch`) are unshipped.

## Pricing

Free and open source under MIT.
No hosted tier; cost is your existing Claude subscription or API plan, multiplied by the number of parallel sessions you run.

## Compared to

- [Claude Squad](../claude-squad/index.md): a free terminal TUI managing several agents in worktrees; choose The Perfect Orchestrator when you want one lead to brief and adversarially verify workers rather than supervise panes yourself.
- [dmux](../dmux/index.md): a tmux TUI giving each task its own worktree and branch; choose The Perfect Orchestrator for the verification protocol and the lead-driven briefs.
- [GraphCode](../graphcode/index.md): a native macOS graph of live loops; choose The Perfect Orchestrator for a zero-dependency tmux harness you can read end to end.

## Bottom line

**Recommended for tinkerers who run Claude Code over tmux and want a minimal, readable template for lead-and-worker orchestration with adversarial verification.**
Not for anyone who needs a maintained tool, multiple harnesses, worktree isolation, or a community to ask.

## Changes

- 2026-09-27 - Created.
- 2026-10-06 - Recorded the Awesome Multi-Agent Orchestrators directory's removal of the entry on 2026-10-05 (PR 64, among seven low-star players) as a second status signal.
- 2026-10-07 - Added the daman8271/the-perfect-orchestrator star history chart to the Status section.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Claude Squad](../claude-squad/index.md) - the free tmux worktree alternative
- [dmux](../dmux/index.md) - the tmux TUI with per-task worktrees
- [GraphCode](../graphcode/index.md) - the native graph-of-loops counterpoint
- [Claude Code](../../harnesses/claude-code/index.md) - the only harness this runs

## References

- https://github.com/daman8271/the-perfect-orchestrator - repository, protocol, security model, roadmap, license, and stars
- https://raw.githubusercontent.com/daman8271/the-perfect-orchestrator/HEAD/README.md - the lead-and-worker design, the adversarial verification rule, and the FAQ
- https://the-perfect-orchestrator.vercel.app - the site the README says its own fleet built and QA'd
- https://github.com/daman8271/the-perfect-orchestrator/tree/main/docs/realrun-2026-06-06 - the recorded fleet run referenced as evidence
- https://openorchestrators.org/ - the curated directory's the-perfect-orchestrator entry
