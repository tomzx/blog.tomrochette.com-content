---
title: Tokscale
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, cost-tracking, cli, open-source]
readability: 3
audience_notes: >
  Engineers running several coding agents who want one token and cost ledger across all of them, and who are curious how their usage ranks publicly.
  Assumes you know where harnesses keep session files and what a pricing catalog is.
---

Tokscale is an MIT-licensed terminal CLI and TUI that reads the local usage data of about 50 coding agents and reports tokens and estimated cost in one ledger, with an opt-in public leaderboard at tokscale.ai.

**Tokscale's twist on this category's cost-report formula is social: the same numbers ccusage prints privately can be submitted to a public profile, which makes it the first member here whose default is local and whose pull is toward sharing.**

## What it is

A TypeScript CLI (`bunx tokscale@latest`, or npm) whose source table names about 50 clients with exact local paths, from OpenCode, Claude Code, Codex, OpenClaw, Copilot CLI, Gemini CLI, Cursor, Amp, Droid, Pi, Kimi, Qwen, Cline, Goose, Crush, Zed, Kiro, Devin, and Junie to Cherry Studio, LM Studio, and WorkBuddy.
Cost comes from LiteLLM's pricing catalog with cache-token discounts and tiered-pricing support, and a TUI plus a visualization dashboard render daily, per-model, and project views.
Some sources need help: `tokscale antigravity sync`, `tokscale trae sync`, and `tokscale warp sync` pull account-level usage into local caches, and Freebuff is estimated from transcripts because it writes no usage records of its own.
`tokscale submit` uploads usage data to the hosted leaderboard to build a public profile, with an autosubmit mode for CI and headless machines.
Made by junhoyeo, an independent developer, MIT-licensed.

## Status

Young and fast: 5,630 stars, 465 forks, 77 open issues, created 2025-12-01, pushed 2026-10-05, as of 2026-10-06.

<a href="https://www.star-history.com/?repos=junhoyeo%2Ftokscale&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=junhoyeo/tokscale&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=junhoyeo/tokscale&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=junhoyeo/tokscale&type=date&legend=top-left" />
 </picture>
</a>

npm shows 153,501 downloads in the trailing month (2026-09-05 to 2026-10-04), second in this category only to ccusage, and the release line is v4.18.0 (2026-10-05) after v4.17.0 (2026-09-15).
Its Show HN reached 2 points and zero comments in December 2025, so the audience arrived without a forum argument.
**The star and download numbers say adoption, the empty Hacker News footprint says no independent scrutiny yet, and both are true at once.**

## Strengths

- The declared source table is the widest in the category after agentsview's, and each row names the exact path it reads, so the coverage claim is auditable rather than asserted.
- Cost estimates name their source: LiteLLM's catalog with cache discounts, not a private pricing table.
- The sync subcommands reach sources that cannot be read passively (the Antigravity language server, Trae and Warp account APIs) while keeping the pulled data in local caches.
- Zero-install invocation plus a TUI and dashboard put it in the same minute-to-first-answer class as ccusage.

## Cautions

- `tokscale submit` and autosubmit exist to publish your usage on a public leaderboard, a stance no other local tool in this category takes, and the README does not lead with exactly what gets uploaded.
- Several sources are estimates or aggregates, not reads: Freebuff from transcripts, Warp as request-and-spend aggregates only, and Cursor through a tokscale-managed CSV cache rather than the IDE's own files.
- That Cursor cache matters beyond this tool: Token Monitor (a sibling entrant this run) reads it for its own Cursor numbers, so an error in it propagates between products.
- One maintainer, a 2-point Show HN with zero comments, and no independent audit of its numbers against provider bills.

## Pricing

Free and open source under MIT.
No paid tier; the hosted leaderboard is free and the project accepts GitHub sponsorships.

## Compared to

- [ccusage](../ccusage/index.md): the zero-install incumbent; Tokscale covers more sources and adds the TUI and leaderboard, while ccusage has the longer track record and Claude's 5-hour blocks report.
- [agentsview](../agentsview/index.md): the pre-indexed archive with search and team push; choose Tokscale for a quick wide report, agentsview for months of queryable history.
- [CodeBurn](../codeburn/index.md): the desktop sibling with task and branch attribution and spend guards; Tokscale counts, CodeBurn manages.

## Bottom line

**Recommended for engineers running many different agents who want one auditable token ledger, and who read the leaderboard as opt-in rather than default.**
Not for teams needing shared dashboards (agentsview) or spend management (CodeBurn).

## Changes

- 2026-10-06 - Created from the 2026-10-06 entrant scan: the widest declared source table in the category after agentsview, 5.6k stars, and the first opt-in public leaderboard, with seven fetched sources.
- 2026-10-07 - Added the junhoyeo/tokscale star history chart to the Status section.

## See also

- [ccusage](../ccusage/index.md) - the incumbent cost report Tokscale extends to more sources
- [agentsview](../agentsview/index.md) - the archive with the broader 60-plus claim and search
- [CodeBurn](../codeburn/index.md) - the spend-management sibling
- [Token Monitor](../token-monitor/index.md) - the live widget built on Tokscale's path conventions and Cursor cache
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/junhoyeo/tokscale - repository, 5,630 stars and 465 forks as of 2026-10-06, MIT license, created 2025-12-01
- https://raw.githubusercontent.com/junhoyeo/tokscale/main/README.md - the about-50-client data-path table, LiteLLM pricing, sync subcommands, and the submit-to-leaderboard flow
- https://registry.npmjs.org/tokscale - npm latest 4.18.0
- https://api.npmjs.org/downloads/point/last-month/tokscale - 153,501 trailing-month downloads (2026-09-05 to 2026-10-04), fetched 2026-10-06
- https://api.github.com/repos/junhoyeo/tokscale/releases - v4.18.0 (2026-10-05), v4.17.0 (2026-09-15), v4.16.0 (2026-09-12)
- https://tokscale.ai - the hosted leaderboard and Wrapped pages
- https://hn.algolia.com/api/v1/items/46365999 - the 2-point, zero-comment Show HN of 2025-12-23, cited as the thin-discussion signal
