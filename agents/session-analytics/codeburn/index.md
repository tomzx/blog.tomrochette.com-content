---
title: CodeBurn
created: 2026-10-05
updated: 2026-10-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, cost-tracking, open-source]
readability: 3
audience_notes: >
  Engineers whose AI coding spend outran their visibility and who want spend cut by task, branch, and project, with guardrails on top.
  Assumes you know what a session file and a token price are.
---

CodeBurn is a free, MIT-licensed local desktop app and CLI that reads the session files coding agents already wrote and breaks spend down by tool, model, project, git branch, and task, then goes one step further than counting: an optimize mode proposes config changes with estimated savings, and a guard can stop a session that spends too much.

**CodeBurn is the cost tool that tries to change the number instead of just reporting it, and the fight in its own launch thread shows the catch: the dollars it shows are API-equivalent estimates, not what a subscription user actually paid.**

## What it is

`npx codeburn` (or `npm install -g`, brew; Node 22.13+) opens a terminal dashboard, and a desktop app (0.9.27, signed and notarized on macOS, on the Microsoft Store for Windows, deb/rpm/AppImage on Linux) adds a menu bar or tray popover, a Capacity Dock of per-provider plan rings, a `codeburn web` view, and, since v0.9.26, a VS Code extension (status-bar spend plus the dashboard in an editor tab, working in Cursor, Windsurf, Antigravity, and VSCodium), all reading the same local files.
The spend cuts run four ways: by project, by git branch, by model, and by task, where task (coding, debugging, planning) is worked out from the session itself, and each session drills down to its turns.
`codeburn optimize` lists what costs tokens without earning it (re-read files, idle MCP servers, an oversized CLAUDE.md), applies fixes with backup and undo, and later reports what each fix actually saved.
Plan tracking (`codeburn plan set claude-max`, `codeburn quota`) reads live limit state from signed-in tools, and `codeburn guard install` adds Claude Code hooks that warn at $5 and stop a session at $15, both configurable.
A local MCP server (`codeburn mcp`) lets an agent answer spend questions inside the conversation, with project names pseudonymized until asked for.
Made by AgentSeal (the repository moved from the AgentSeal org to getagentseal, and the old URL redirects), which claims 42 supported integrations including Claude Code, Codex, Cursor, Gemini, Amp, and Command Code (the last two added in v0.9.26).

## Status

Young and fast: 11,377 stars and 901 forks as of 2026-10-21, created 2026-04-13, pushed 2026-10-20 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=getagentseal/codeburn&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=getagentseal/codeburn&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=getagentseal/codeburn&type=date&legend=top-left" />
</picture>

The npm package pulled 38,716 downloads in the trailing month (2026-09-13 to 2026-10-12).
The current release line is desktop/CLI v0.9.27 (2026-10-11, tagged separately per platform).
v0.9.26 (2026-10-10) added Amp and Command Code as providers, the VS Code extension, a pull-request view with per-review cost, `--why` explanations for Claude Code sessions, Cursor usage synced from cursor.com with an app login, a tilde prefix on every estimated dollar, a long list of money-accuracy fixes, and removed Roo Code as an archived project.
v0.9.27 added one-click updates across the CLI, menu bar, and desktop app.
The repository description still says 37 tools where the README says 42, a drift to read as the README being newer.
Its token accounting has been externally probed: the September 2026 AgentMeasure audit of about 110 usage tools filed a Codex token_count dedup finding against it, the fix merged as PR 1264 on 2026-09-16, and the audit's own methodology note records that a 53-rollout corpus check vindicated CodeBurn's re-emission behavior against the auditor's first assertion.
Its Show HN launch reached 112 points and 15 top-level comments on 2026-04-13, and it also launched on Product Hunt.

## Strengths

- Task and branch attribution is the capability no other cost cell in this category offers: the cost of a feature, not just of a day.
- The optimize loop closes with evidence: apply, undo, and a later report comparing each fix's promised savings against what the sessions did.
- Guard and quota serve subscription-plan users, the majority this category's API-priced tools quietly miss.
- The desktop polish is unusual for the category: signed macOS builds, a Microsoft Store listing, a GNOME extension, and WSL-aware reads.

## Cautions

- **The headline dollars are API-equivalent estimates computed from session tokens, and the launch thread's sharpest exchange was exactly this**, a "$1,400/week" framing that a commenter called misleading for a user on the $200 plan; since v0.9.26 every estimated dollar carries a visible `~`.
- Task labels are CodeBurn's own classification of each session, with no published methodology to check them against.
- Cursor usage synced from cursor.com with an app login (or a CSV import) since v0.9.26, closing the IDE-only gap the launch thread criticized but making Cursor numbers ride a vendor sync instead of local files.
- `optimize --apply` asks you to trust a tool with your config; backups and undo exist, and the report step is how to verify it earned that trust.

## Pricing

Free and open source under MIT.
No paid tiers are published; the project accepts GitHub sponsorships.

## Compared to

- [ccusage](../ccusage/index.md): the zero-install, report-first incumbent; CodeBurn adds attribution, optimization, and guardrails, at the price of a bigger install.
- [agentsview](../agentsview/index.md): the retrospective archive with search and team push; choose agentsview for history questions, CodeBurn for spend questions.
- [AgentTrace](../agenttrace/index.md): the terminal health audit with CI gates; CodeBurn's optimize findings are the closest thing to AgentTrace's slow-run diagnosis, but money-first.

## Bottom line

**Recommended for engineers whose spend needs managing, not just measuring, especially subscription-plan users who want quota tracking and session guardrails.**
Not for anyone who wants plain unclassified numbers (ccusage is the simpler instrument), or for teams needing a searchable archive.

## Changes

- 2026-10-05 - Created from the 2026-10-05 entrant scan: a 112-point launch, 11.3k stars in six months, and a by-task cost angle the category lacked, with six fetched sources.
- 2026-10-07 - Added the getagentseal/codeburn star history chart to the Status section.
- 2026-10-11 - Recorded the v0.9.26 (2026-10-10) and v0.9.27 (2026-10-11) releases: Amp and Command Code providers, the VS Code extension, a pull-request view, `--why` session explanations, Cursor usage synced from cursor.com replacing local estimates, a tilde on estimated dollars, Roo Code removed, and one-click updates; the README's integration claim moved to 42 while the repository description still says 37, and repository counts and trailing-month downloads refreshed (36,881 to 38,579).
- 2026-10-16 - Recorded the external AgentMeasure audit evidence: the Codex token_count dedup fix merged as PR 1264 on 2026-09-16 and the audit's methodology note vindicating the re-emission behavior against the auditor's first assertion; trailing-month downloads refreshed (38,579 to 38,716) and the pushed date moved to 2026-10-15.
- 2026-10-21 - Recorded unreleased post-v0.9.27 work merged 2026-10-20: a Claude Code plugin and an MCP Registry listing, plus signing-environment gating and dependency bumps; the pushed date moved to 2026-10-20 and forks refreshed 879 to 901.

## See also

- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins
- [ccusage](../ccusage/index.md) - the report-first incumbent it overlaps
- [agentsview](../agentsview/index.md) - the archive alternative for history and search
- [AgentTrace](../agenttrace/index.md) - the run-health audit sibling

## References

- https://github.com/getagentseal/codeburn - repository, 11,377 stars and 879 forks as of 2026-10-11, MIT license, created 2026-04-13 (the AgentSeal/codeburn URL redirects here)
- https://raw.githubusercontent.com/getagentseal/codeburn/main/README.md - surfaces, the four spend cuts, optimize/quota/guard behavior, the MCP server, the 42-tool claim, and the desktop install matrix
- https://api.npmjs.org/downloads/point/last-month/codeburn - 38,716 trailing-month downloads (2026-09-13 to 2026-10-12), fetched 2026-10-16
- https://raw.githubusercontent.com/roy-tong/AgentMeasure/main/campaigns/audit-report-2026-09.md - the external audit that filed the Codex dedup finding and documents the 53-rollout correction of its own first assertion
- https://github.com/getagentseal/codeburn/pull/1264 - the merged token_count dedup fix (2026-09-16) behind the external-probe sentence
- https://registry.npmjs.org/codeburn - npm latest 0.9.27
- https://api.github.com/repos/getagentseal/codeburn/releases - the v0.9.27, windows-v0.9.27, and mac-v0.9.27 tags of 2026-10-11 and v0.9.26 of 2026-10-10, after the v0.9.25 line of 2026-09-21
- https://hn.algolia.com/api/v1/items/47759035 - the 112-point launch thread: the API-equivalent-cost fight, the Cursor Agent CLI gap, and the author's answers
