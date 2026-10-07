---
title: CodeBurn
created: 2026-10-05
updated: 2026-10-07
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

`npx codeburn` (or `npm install -g`, brew; Node 22.13+) opens a terminal dashboard, and a desktop app (0.9.25, signed and notarized on macOS, on the Microsoft Store for Windows, deb/rpm/AppImage on Linux) adds a menu bar or tray popover, a Capacity Dock of per-provider plan rings, and a `codeburn web` view, all reading the same local files.
The spend cuts run four ways: by project, by git branch, by model, and by task, where task (coding, debugging, planning) is worked out from the session itself, and each session drills down to its turns.
`codeburn optimize` lists what costs tokens without earning it (re-read files, idle MCP servers, an oversized CLAUDE.md), applies fixes with backup and undo, and later reports what each fix actually saved.
Plan tracking (`codeburn plan set claude-max`, `codeburn quota`) reads live limit state from signed-in tools, and `codeburn guard install` adds Claude Code hooks that warn at $5 and stop a session at $15, both configurable.
A local MCP server (`codeburn mcp`) lets an agent answer spend questions inside the conversation, with project names pseudonymized until asked for.
Made by AgentSeal (the repository moved from the AgentSeal org to getagentseal, and the old URL redirects), which claims 41 supported integrations including Claude Code, Codex, Cursor, and Gemini.

## Status

Young and fast: 11,345 stars and 876 forks as of 2026-10-06, created 2026-04-13, pushed 2026-10-06 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=getagentseal/codeburn&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=getagentseal/codeburn&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=getagentseal/codeburn&type=date&legend=top-left" />
</picture>

The npm package pulled 36,881 downloads in the trailing month (2026-09-05 to 2026-10-04).
The current release line is desktop/CLI v0.9.25 (2026-09-21, tagged separately per platform), and the repository description still says 37 tools where the README says 41, a drift to read as the README being newer.
Its Show HN launch reached 112 points and 15 top-level comments on 2026-04-13, and it also launched on Product Hunt.

## Strengths

- Task and branch attribution is the capability no other cost cell in this category offers: the cost of a feature, not just of a day.
- The optimize loop closes with evidence: apply, undo, and a later report comparing each fix's promised savings against what the sessions did.
- Guard and quota serve subscription-plan users, the majority this category's API-priced tools quietly miss.
- The desktop polish is unusual for the category: signed macOS builds, a Microsoft Store listing, a GNOME extension, and WSL-aware reads.

## Cautions

- **The headline dollars are API-equivalent estimates computed from session tokens, and the launch thread's sharpest exchange was exactly this**, a "$1,400/week" framing that a commenter called misleading for a user on the $200 plan.
- Task labels are CodeBurn's own classification of each session, with no published methodology to check them against.
- Cursor coverage reads the IDE's state database only, per the launch thread, so Cursor Agent CLI transcripts are missed.
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

## See also

- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins
- [ccusage](../ccusage/index.md) - the report-first incumbent it overlaps
- [agentsview](../agentsview/index.md) - the archive alternative for history and search
- [AgentTrace](../agenttrace/index.md) - the run-health audit sibling

## References

- https://github.com/getagentseal/codeburn - repository, 11,345 stars and 876 forks as of 2026-10-06, MIT license, created 2026-04-13 (the AgentSeal/codeburn URL redirects here)
- https://raw.githubusercontent.com/getagentseal/codeburn/main/README.md - surfaces, the four spend cuts, optimize/quota/guard behavior, the MCP server, the 41-tool claim, and the desktop install matrix
- https://api.npmjs.org/downloads/point/last-month/codeburn - 36,881 trailing-month downloads (2026-09-05 to 2026-10-04), fetched 2026-10-06
- https://registry.npmjs.org/codeburn - npm latest 0.9.25
- https://api.github.com/repos/getagentseal/codeburn/releases - the v0.9.25, windows-v0.9.25, mac-v0.9.25, and desktop-v0.9.25 tags of 2026-09-21
- https://hn.algolia.com/api/v1/items/47759035 - the 112-point launch thread: the API-equivalent-cost fight, the Cursor Agent CLI gap, and the author's answers
