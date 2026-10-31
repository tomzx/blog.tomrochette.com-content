---
title: ax
created: 2026-10-23
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, observability, memory, local-first, cost-tracking]
readability: 3
audience_notes: >
  Engineers running Claude Code or Codex daily who want their session history to answer questions and to fix the next run, not just to be searchable.
  Assumes you know what a session transcript, BM25 search, and a subagent dispatch are.
---

ax is a local-first agent-experience graph for AI coding agents: it ingests six harnesses' sessions, installed skills, git history, and GitHub PRs into an embedded DuckDB graph on your machine, then answers recall, cost, skill-triage, and friction questions over it, and turns repeated session friction into reviewed fixes for the next run.

**ax's bet is that the archive should act: where the other tools in this category stop at showing you history, ax reads the same history to score your skills, price your branches, route cheap work off expensive models, and propose AGENTS.md fixes with verdicts tracked at plus 3, 10, and 30 sessions.**

## What it is

A Bun 1.3+ CLI (installed by a curl script) that builds a typed graph over Claude Code, Codex, Pi, oh-my-pi, OpenCode, and Cursor transcripts plus installed skills, local git history, and GitHub PR reviews and checks, stored as an embedded DuckDB file with a small SQLite sidecar for the decisions you make, with no database server and no daemon to run.
Reading keeps it current: a query against a stale graph quietly forks a catch-up ingest in the background.
The surfaces: `ax recall` for BM25 search across turns, commits, and skills; `ax costs` for per-session, per-commit, and per-branch pricing resolved through model pricing rows; `ax skills taste` for scoring which installed skills earn their keep; `ax insights` for 31 read-only graph views; `ax studio`, an ephemeral local dashboard that binds a port only while a browser is attached; `ax share`, which publishes a sanitized session as a GitHub gist rendered by a hosted viewer; an MCP server exposing ten read-only graph queries; and `ax improve`, the retro loop that emits structured session retros, ranks proposals, and tracks experiment verdicts.
A hooks SDK lets you author typed TypeScript guards, backtest them against weeks of your own tool history, and install them into Claude Code and Codex.
Made by Necmettin Karakaya (Necmttn) under AGPL-3.0, with a paid commercial license offered for uses the AGPL does not permit.

## Status

Young and shipping in public: 121 stars, 14 forks, 42 open issues, created 2026-05-08, pushed 2026-10-28, v0.44.4 the latest version (announced releases run through v0.44.3 on 2026-09-14), as of 2026-10-31.
The release history is unusually transparent for a 0.x project: v0.40.0 (2026-08-20) rebuilt storage from SurrealDB to embedded DuckDB at a claimed 21 times faster ingest, and v0.40.1 (2026-08-21) closed 19 of the 24 bugs a five-lane audit found in it, mixed-model session costs and silent duplicate-row drops included.
An independent RepoGrade scan of the repository (its scan data from mid-2026) graded it C at 76/100, top 38% of 5,156 graded repositories: documentation 94 and project health 92, engineering 58, with no linter configuration found and thin test coverage, while median issue response ran 3 hours and the median PR merged in under an hour.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Necmttn/ax&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Necmttn/ax&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Necmttn/ax&type=date&legend=top-left" />
</picture>

**A solo-maintained 0.x with a thin 121-star footprint and no independent review of its claims, but with public engineering records (16 architecture decision records), a changelog that documents its own bugs, and an author who answers issues in hours.**

## Strengths

- The graph answers questions no other archive here asks: which skills earn their keep, what did this branch cost, which dispatches should have run a cheaper model.
- Cost routing closes the loop with receipts: ax measures the main-loop versus subagent spend split, nudges at dispatch time through a hook, and re-mines the routing table from your own dispatch history.
- The improve loop turns session evidence into reviewed fixes with verdicts on session-count windows, so an accepted proposal that stops working gets caught rather than forgotten.
- Agent-callable by design: an MCP server, installable skills, and `ax project context` hand the next session your stack, recent friction, and verification commands before it starts.
- The privacy posture is explicit and narrow: ingest makes no outbound calls, and the only network surfaces (public profile gists, profile widgets, pattern PRs) are separate consent-gated commands documented one by one.

## Cautions

- 121 stars and no independent review: the routing savings, the 21-times ingest claim, and the skill scores all rest on the project's own measurements.
- The mid-2026 RepoGrade scan found engineering hygiene gaps (no linter or formatter configuration detected, thin tests), and the stack (Bun, Effect TS) narrows the field of outside contributors.
- macOS-first: Linux works for ingest and the CLI, but the dashboard experience and the one optional launchd agent assume a Mac.
- AGPL-3.0 keeps the source open but complicates embedding in commercial tooling; the escape hatch is a commercial license by negotiation.
- The onboarding prompt (meant to be pasted into your agent) is assertive: it instructs the agent to draft GitHub issues and to publish shared sessions, each on your explicit confirmation, a pattern worth reading carefully before you let it run.

## Pricing

The CLI and the graph are free under AGPL-3.0; the README offers a commercial license for uses the AGPL does not permit, by contact through the project's Discord.
A team rollup is sold to a founding cohort capped at five teams at $20 per developer per month: each seat pushes redacted aggregates (counts, sums, ratios) as one JSON file into a private git repo your org owns, the dashboard aggregates client-side with the viewer's own GitHub token, ax's servers hold nothing, cells under five contributors are hidden, and there is no per-person leaderboard.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-23 | Team | Baseline: free AGPL-3.0 CLI; $20 per developer per month founding-cohort team rollup (five-team cap), commercial licenses by contact | https://ax.necmttn.com/teams |

## Compared to

- [agentsview](../agentsview/index.md): the wider archive, roughly 60 local formats indexed for months of history questions; ax covers six harnesses but reads them into interventions rather than views.
- [Memex](../memex/index.md): the closest search-and-resume peer; Memex stays a search tool, ax adds cost routing, skill scoring, and the improve loop on top of recall.
- [ccusage](../ccusage/index.md): the print-what-it-cost incumbent; ccusage totals your spend, ax prices by branch and commit and names the spend that was routable to a cheaper model.
- [AgentMeasure](../agentmeasure/index.md): the evidence auditor; both distrust naive token math, but AgentMeasure verifies whether the records count while ax builds interventions on them.

## Bottom line

**Recommended for Claude Code and Codex power users who want their session history to change the next run, and who accept a young solo project to get skill scoring and cost routing that nothing else here ships.**
Not for teams needing hosted multi-user analytics today, for AGPL-incompatible embedding without a license, or for anyone who requires an independently reviewed tool.

## Changes

- 2026-10-23 - Created from the coordinator's entrant handoff, admitted on six fetched sources with the $20 per seat founding-cohort pricing recorded and the independent RepoGrade grade as the skeptical source.
- 2026-10-31 - Rotation re-verification: every cited URL re-fetched and live (README, docs hub, changelog, teams page, RepoGrade report, repository); the release line unchanged at v0.44.4 with the changelog still announcing through v0.44.3, the teams page unchanged at $20 per seat with one of five founding spots claimed and per-seat receipts marked live today, and the RepoGrade grade unchanged at C 76/100; the Pricing section's commercial-license contact moved to the project's Discord per the README, and repository counts refreshed (pushed 2026-10-07 to 2026-10-28, forks 15 to 14, open issues 40 to 42).

## See also

- [Memex](../memex/index.md) - the closest search-and-resume archive, without the improve loop
- [agentsview](../agentsview/index.md) - the broad multi-format archive ax narrows into interventions
- [ccusage](../ccusage/index.md) - the cost-report incumbent ax extends with per-branch and routable-spend answers
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/Necmttn/ax - the repository, 121 stars, AGPL-3.0, created 2026-05-08, pushed 2026-10-28 (as of 2026-10-31)
- https://raw.githubusercontent.com/Necmttn/ax/main/README.md - the graph model, six-harness ingest, recall, costs, routing, hooks SDK, MCP server, and privacy rules
- https://ax.necmttn.com/docs - the docs hub at v0.44.4, the guide set, and the MCP server's ten read-only queries
- https://ax.necmttn.com/changelog - the release history from v0.1.0 (2026-05-09) through v0.44.3 (2026-09-14), the DuckDB rebuild in v0.40.0, and the 19-bug fix wave in v0.40.1
- https://ax.necmttn.com/teams - the $20 per seat founding-cohort team rollup, the redacted-aggregate privacy model, and the five-team cap
- https://www.repo-grade.com/report/necmttn/ax - the independent C grade (76/100), the engineering hygiene findings, and the 3-hour median issue response
