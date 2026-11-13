---
title: Tokscale
created: 2026-10-06
updated: 2026-11-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, cost-tracking, cli, open-source]
readability: 3
audience_notes: >
  Engineers running several coding agents who want one token and cost ledger across all of them, and who are curious how their usage ranks publicly.
  Assumes you know where harnesses keep session files and what a pricing catalog is.
---

Tokscale is an MIT-licensed terminal CLI and TUI that reads the local usage data of 63 named coding agents and reports tokens and estimated cost in one ledger, with an opt-in public leaderboard at tokscale.ai.

**Tokscale's twist on this category's cost-report formula is social: the same numbers ccusage prints privately can be submitted to a public profile, which makes it the first member here whose default is local and whose pull is toward sharing.**

## What it is

A TypeScript CLI (`bunx tokscale@latest`, or npm) whose source table names 63 clients with exact local paths, from OpenCode, Claude Code, Codex, OpenClaw, Copilot CLI, Gemini CLI, Cursor, Amp, Droid, Pi, Kimi, Qwen, Cline, Goose, Crush, Zed, Kiro, Devin, and Junie to Cherry Studio, LM Studio, BB, Qoder, and WorkBuddy.
Cost comes from LiteLLM's pricing catalog with cache-token discounts and tiered-pricing support, and a TUI plus a visualization dashboard render daily, per-model, and project views.
Some sources need help: `tokscale antigravity sync`, `tokscale trae sync`, and `tokscale warp sync` pull account-level usage into local caches, and Freebuff is estimated from transcripts because it writes no usage records of its own.
`tokscale submit` uploads usage data to the hosted leaderboard to build a public profile, with an autosubmit mode for CI and headless machines.
Made by junhoyeo, an independent developer, MIT-licensed.

## Status

Young and fast: 5,656 stars, 476 forks, 77 open issues, created 2025-12-01, pushed 2026-11-12, as of 2026-11-12 (the star figure keeps its earlier fetch date, everything else refreshed this run).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=junhoyeo/tokscale&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=junhoyeo/tokscale&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=junhoyeo/tokscale&type=date&legend=top-left" />
</picture>

npm shows 123,064 downloads in the trailing month (2026-10-13 to 2026-11-12, six zero days inside the window), second in this category only to ccusage, and the release line is v4.22.0 (2026-11-11, which added BB and Qoder clients, Copilot native session-state event discovery, leaderboard submissions that automatically withhold extreme token spoofers, Antigravity CSRF token discovery with session sync, codebuddy generation and turn duration, and a long fix tail including Codex usage attributed from Magpie evidence and Kimi K3.1 Pro priced at the Moonshot API card) after v4.21.0 (2026-11-02, offline reports with an explicit pricing refresh, UTC-aligned ranking windows, bounded reusable group invitations with atomic redemption, Proma native and mirrored Agent session usage counting, plus a long fix tail including Cursor snapshot dedup and atomic credential writes) and v4.20.1 (2026-10-23) and v4.20.0 (2026-10-17, which added Mistral Vibe and Aside browser clients, Amp server-side thread sync through the amp CLI, custom pricing rates scoped by billing provider, Cursor Auto/API tracks and Grok Bot quotas, and leaderboard group member management).
The unreleased wave the previous pass recorded shipped in v4.22.0: the spoofer withholding and the Copilot native session-state files are in the release, leaving nothing substantive pending as of 2026-11-12.
Its parsers have also been externally probed: the September 2026 AgentMeasure audit filed that forked and continued Pi sessions double-counted (issue 1306), fixed the same day via PR 1323.
Its Show HN reached 2 points and zero comments in December 2025, so the audience arrived without a forum argument.
**The star and download numbers say adoption, the empty Hacker News footprint says no independent scrutiny yet, and both are true at once.**

## Strengths

- The declared source table now leads the category at 63 named clients as of 2026-11-12, past agentsview's 60-plus claim, and each row names the exact path it reads, so the coverage claim is auditable rather than asserted.
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
- 2026-10-16 - Recorded v4.19.0 and v4.19.1 (2026-10-14 and 10-15), the external AgentMeasure audit's Pi fork double-count finding with its same-day fix (issue 1306, PR 1323), and trailing-month downloads refreshed (173,488 to 182,342).
- 2026-10-18 - Recorded v4.20.0 (2026-10-17): Mistral Vibe and Aside browser clients, Amp server-side thread sync through the amp CLI, custom pricing rates scoped by billing provider, Cursor Auto/API tracks and Grok Bot quotas, and leaderboard group member management; trailing-month downloads refreshed (182,342 to 178,917), npm latest moved to 4.20.0, open issues 100 to 67, and the pushed date moved to 2026-10-18.
- 2026-10-21 - Recorded two unreleased submit-path fixes merged 2026-10-20: devin-cli duplicate counts healed from a parser recount proof and snapshot-integrity clients kept complete on filtered scans, both after v4.20.0; trailing-month downloads refreshed (178,917 to 180,721, window 2026-09-19 to 2026-10-18), open issues 67 to 82, and the pushed date moved to 2026-10-20.
- 2026-10-25 - Recorded v4.20.1 (2026-10-23), which shipped those two submit-path fixes and added Antigravity family re-attribution coverage across model re-attributions plus frontend layout fixes; trailing-month downloads refreshed (180,721 to 167,077, window 2026-09-23 to 2026-10-22), npm latest moved to 4.20.1, open issues 82 to 98, and the pushed date moved to 2026-10-25.
- 2026-10-26 - Recorded unreleased post-v4.20.1 fixes merged 2026-10-25: Cursor usage events now count once across their snapshots, pre-5.6 OpenAI cache writes inherit the input rate, legacy OpenCode and MiMo entries stop replaying over complete scans, and OpenCode's V2 providers config supplies model names; open issues 98 to 100 and the pushed date moved to 2026-10-26, with downloads and npm latest unchanged.
- 2026-11-01 - Rotation re-verification: every cited URL re-fetched and live; no release after v4.20.1 with a wave of twelve unreleased fixes landing 2026-10-30; the source table moved to 61 named clients, up from about 50 (the coverage claim moved through the definition, the Strengths line, and the matrix), trailing-month downloads refreshed (167,077 to 122,835, window 2026-10-03 to 2026-11-01 with ten zero days), forks refreshed 470 to 471 and open issues 100 to 89, and the pushed date moved to 2026-10-30; the downloads reference moved to the dated-range endpoint and the audit-report reference repointed to its Verovo path.
- 2026-11-07 - Recorded v4.21.0 (2026-11-02: offline reports with an explicit pricing refresh, UTC-aligned ranking windows, bounded reusable group invitations, Proma native and mirrored session usage, Cursor snapshot dedup, atomic credential writes) and the unreleased wave after it (leaderboard spoofer withholding, Copilot native session-state files); the source table moved to 62 named clients, up from 61, trailing-month downloads refreshed (122,835 to 131,512, window 2026-10-09 to 2026-11-07 with six zero days), npm latest moved to 4.21.0, forks refreshed 471 to 478 and open issues 89 to 74, and the pushed date moved to 2026-11-06.
- 2026-11-12 - Recorded v4.22.0 (2026-11-11: BB and Qoder clients, Copilot native session-state discovery, leaderboard spoofer withholding, Antigravity CSRF token discovery with session sync, codebuddy generation and turn duration, Codex usage attributed from Magpie evidence, Kimi K3.1 Pro priced at the Moonshot API card), shipping the previously unreleased wave; the source table moved to 63 named clients, up from 62, trailing-month downloads refreshed (131,512 to 123,064, window 2026-10-13 to 2026-11-12 with six zero days), npm latest moved to 4.22.0, forks refreshed 478 to 476 and open issues 74 to 77, and the pushed date moved to 2026-11-12.

## See also

- [ccusage](../ccusage/index.md) - the incumbent cost report Tokscale extends to more sources
- [agentsview](../agentsview/index.md) - the archive with the broader 60-plus claim and search
- [CodeBurn](../codeburn/index.md) - the spend-management sibling
- [Token Monitor](../token-monitor/index.md) - the live widget built on Tokscale's path conventions and Cursor cache
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/junhoyeo/tokscale - repository, stars fetched at creation (5,656 as of 2026-10-11), MIT license, created 2025-12-01
- https://raw.githubusercontent.com/junhoyeo/tokscale/main/README.md - the 63-client data-path table, LiteLLM pricing, sync subcommands, and the submit-to-leaderboard flow (re-fetched 2026-11-12)
- https://registry.npmjs.org/tokscale - npm latest 4.22.0 (re-verified 2026-11-12)
- https://api.npmjs.org/downloads/range/2026-10-13:2026-11-12/tokscale - 123,064 trailing-month downloads (six zero days inside the window), fetched 2026-11-12 via the dated-range endpoint per the npm-window ruling
- https://api.github.com/repos/junhoyeo/tokscale/releases - v4.22.0 (2026-11-11), v4.21.0 (2026-11-02), v4.20.1 (2026-10-23), v4.20.0 (2026-10-17), v4.19.1 (2026-10-15), v4.19.0 (2026-10-14) (re-fetched 2026-11-12)
- https://github.com/junhoyeo/tokscale/issues/1306 - the external audit's Pi fork double-count finding, closed completed via PR 1323 the same day (re-fetched 2026-11-01)
- https://raw.githubusercontent.com/roy-tong/Verovo/main/campaigns/audit-report-2026-09.md - the audit behind the external-probe sentence (repointed to the Verovo path 2026-11-01 after the project renamed)
- https://tokscale.ai - the hosted leaderboard and Wrapped pages
- https://hn.algolia.com/api/v1/items/46365999 - the 2-point, zero-comment Show HN of 2025-12-23, cited as the thin-discussion signal
