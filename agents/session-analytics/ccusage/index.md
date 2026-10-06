---
title: ccusage
created: 2026-10-05
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, cost-tracking, cli, open-source]
readability: 3
audience_notes: >
  Engineers running coding-agent CLIs who want to know what their token usage costs without installing anything.
  Assumes you know what a session file and a token price are.
---

ccusage is a free, MIT-licensed terminal tool that reads the usage data coding-agent CLIs already wrote on disk and reports token counts and estimated costs by day, week, month, and session.

**ccusage is the incumbent of this category, the tool every cost report here gets compared against, and its open question is the one its launch thread raised: every dollar it prints is an estimate computed from a pricing catalog, not a bill.**

## What it is

A TypeScript CLI (`npx ccusage@latest`, or bunx, or a global install) that parses the local usage files of eighteen named sources into one unified report: Claude Code, Codex, OpenCode, Amp, Droid, Codebuff, Hermes Agent, pi, Goose, OpenClaw, Kilo, Kimi, Qwen, GitHub Copilot CLI, Gemini CLI, Antigravity, Grok Build CLI, and ZCode.
Reports cover daily, weekly, monthly, and session views, plus Claude's 5-hour billing windows (blocks), a beta Claude Code statusline integration, per-model breakdowns, project grouping, JSON output, timezone control, and custom pricing overrides in a ccusage.json file.
Costs are computed locally against a fetched model-pricing catalog, with an `--offline` mode for pre-cached prices.
The repository is a monorepo created by ryoppippi (the project moved from his personal account to the ccusage organization), sponsored by Lineman.io, CodeRabbit, and Blacksmith rather than sold.

## Status

**The most-installed tool in this category by an order of magnitude, and until today the only one this section had never profiled.**
About 18.9k stars and 862 forks as of 2026-10-06, created 2025-05-29, pushed 2026-10-06 (GitHub API).
The npm package pulled 556,660 downloads in the trailing month (2026-09-05 to 2026-10-04), roughly eight times the claude-mem plugin and far ahead of every session-analytics peer here.
The release line is v20.x with rapid patches: v20.0.26 (2026-09-27) is the latest tagged release, after v20.0.24 (2026-09-21) and v20.0.23 (2026-09-18).
Its Show HN launch thread reached 75 points in July 2025, and the README carries an Awesome Claude Code mention badge.

## Strengths

- Zero-install invocation makes it the first cost answer anyone runs, which is why other tools' docs benchmark against it.
- Eighteen sources in one unified report is the widest declared coverage of any local tool in this category's notes.
- The blocks report maps usage onto Claude's 5-hour billing windows, and the statusline beta puts spend into the prompt view, both aimed at subscription-plan users rather than API payers.
- Offline mode and per-model pricing overrides make the cost numbers auditable instead of magical.

## Cautions

- **Every dollar is an estimate from a pricing catalog, not a provider bill**, so plan-flat-rate users see API-equivalent numbers that can overstate or understate what they actually paid.
- The launch thread's sharpest question was the npx pattern itself: getting people comfortable piping unvetted npm code with full read access to their home directory.
- It produces report tables, not an archive: there is no transcript search, no session store, and no history beyond what the source agents still have on disk.
- Coverage per source is uneven by construction, since each harness writes its own formats, and sibling notes here document how some of those formats undercount cache and side-call tokens.

## Pricing

Free and open source under MIT (the license file lives at apps/ccusage/LICENSE in the monorepo).
No paid tier; the project carries sponsors (Lineman.io, CodeRabbit, Blacksmith) and accepts GitHub sponsorships.

## Compared to

- [agentsview](../agentsview/index.md): the pre-indexed archive with web, desktop, and search; ccusage is the report-first tool you run once without installing anything.
- [AgentTrace](../agenttrace/index.md): the Rust audit with CI gates and latency diagnosis; ccusage covers cost breadth, AgentTrace covers run health.
- [CodeBurn](../codeburn/index.md): the desktop-app sibling that cuts spend by task and branch and proposes config fixes; ccusage stays the quick terminal report.

## Bottom line

**Recommended as the default first cost report for anyone running two or more coding-agent CLIs, and as the baseline every pricier dashboard should be compared against.**
Not for transcript search or provenance, and not as an authority on what a subscription plan actually cost you.

## Changes

- 2026-10-05 - Created from the 2026-10-05 entrant scan: the category's most-installed tool, previously known here only as the comparator named in agentsview's note, profiled with seven fetched sources.

## See also

- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins
- [agentsview](../agentsview/index.md) - the archive tool whose docs name ccusage as covering the same core job
- [AgentTrace](../agenttrace/index.md) - the terminal audit sibling
- [CodeBurn](../codeburn/index.md) - the desktop spend-analysis sibling
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the per-token economics behind the pricing catalog

## References

- https://github.com/ccusage/ccusage - repository, 18.9k stars and 864 forks as of 2026-10-05, created 2025-05-29, the ryoppippi origin and ccusage-org move (the ryoppippi/ccusage URL redirects here)
- https://raw.githubusercontent.com/ccusage/ccusage/main/apps/ccusage/README.md - the eighteen-source table, report types, blocks and statusline features, offline mode, and pricing overrides
- https://raw.githubusercontent.com/ccusage/ccusage/main/apps/ccusage/LICENSE - the MIT license text, copyright ryoppippi
- https://api.npmjs.org/downloads/point/last-month/ccusage - 556,660 trailing-month downloads (2026-09-05 to 2026-10-04), fetched 2026-10-06
- https://registry.npmjs.org/ccusage - npm latest 20.0.26, matching the v20.0.26 GitHub tag
- https://api.github.com/repos/ccusage/ccusage/releases - the v20.0.26 (2026-09-27), v20.0.24 (2026-09-21), and v20.0.23 (2026-09-18) release dates
- https://news.ycombinator.com/item?id=44610925 - the 75-point launch thread (2025-07-18), carrying the npx-security critique and the estimate-versus-bill debates
- https://ccusage.com - the docs site, a client-rendered VitePress shell this run, with the title and description verified in the served HTML
