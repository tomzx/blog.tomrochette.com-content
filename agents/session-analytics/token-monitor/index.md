---
title: Token Monitor
created: 2026-10-06
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, cost-tracking, desktop, open-source]
readability: 3
audience_notes: >
  Engineers who want a live desktop view of token usage and provider limits across every AI coding tool they run, on one machine or several.
  Assumes you know what a session file, a rate-limit window, and a token count are.
---

Token Monitor is an MIT-licensed desktop widget that parses the local session files of more than 43 AI coding tools and shows live token usage, provider limits, and cost trends, with optional multi-device sync through a hub you host.

**Token Monitor is this category's first live widget aimed at every tool at once: agents-observe streams one harness's events into a dashboard and CodeBurn puts spend in a menu bar, while Token Monitor reads 43-plus sources into one always-on window and keeps the history after the sources prune it.**

## What it is

A desktop application (Windows 10+, macOS 12+, Linux x64; Homebrew cask) whose source table grades each of 43-plus tools separately for token usage, account limits, and session details, following Tokscale's path and environment-variable conventions, including reading Tokscale's Cursor cache for account-level Cursor usage.
The widget updates within seconds of each turn, shows a live tok/s rate, and expands to cache hit versus miss breakdowns, per-session token splits, and cost in USD, TWD, HKD, or CNY with daily-updated exchange rates.
An opt-in retention archive keeps daily tool and model usage locally after sources prune it (Claude Code drops transcripts after 30 days by default), and usage exports to CSV and JSON for spreadsheets, Obsidian, or Grafana.
Multi-device sync is hub-backed over Server-Sent Events with three self-hosted backends (in-widget hub, Node CLI hub, or Cloudflare Worker) or eventually consistent iCloud Drive, and single-device use needs no server at all.
Per-session detail reads transcripts on demand and is never synced; prompts, responses, and file contents stay local.
Made by Javis603, MIT-licensed.

## Status

Young and shipping daily: 2,634 stars, 266 forks, 104 open issues, created 2026-05-19, pushed 2026-10-06, with v0.67.0 released 2026-10-06, v0.66.0 on 2026-10-04, and v0.65.0 on 2026-10-02, as of 2026-10-06.
I found no Hacker News thread for the project; the only search hit for the name is an unrelated ESP32 desk display.
**A four-month-old tool with a release cadence this category has never seen and zero independent discussion, which is exactly the profile to verify before trusting.**

## Strengths

- Live multi-tool coverage is a genuine gap: nothing else here renders usage across 43-plus tools in one view as turns happen.
- The retention archive answers a genuine loss: harnesses prune transcripts (Claude Code at 30 days by default), and the category's archive tools can only index what still exists.
- Provider-limit detection spans session, daily, weekly, billing, and credits windows across 28-plus providers, including multiple OpenRouter profiles and prepaid balances.
- The sync story is self-hosted by construction (your widget, Node hub, or Cloudflare Worker), with iOS widgets through the Worker hub.

## Cautions

- 104 open issues against 2,634 stars and v0.67 within four months is a fast, churny project; expect breaking changes in a widget you leave running.
- Coverage is graded and uneven by design, and several limit sources are account-level cookie reads (Ollama Cloud, Alibaba Cloud console) rather than file parsing, a different trust model than the local reads the rest of this category does.
- Cursor account usage arrives through Tokscale's cache, so Cursor numbers inherit Tokscale's Cursor pipeline.
- The community footprint is a Discord and a star graph, with no independent discussion, so treat the claims as unverified beyond the README.

## Pricing

Free and open source under MIT.
No paid tiers are published; the sync backends are self-hosted and the project accepts sponsorships.

## Compared to

- [CodeBurn](../codeburn/index.md): the desktop sibling with task and branch attribution and spend guards; Token Monitor is broader on live limits, CodeBurn deeper on spend reduction.
- [ccusage](../ccusage/index.md): the zero-install report; Token Monitor is the always-on window, ccusage the on-demand answer.
- [agentsview](../agentsview/index.md): the pre-indexed archive with search; choose Token Monitor to watch, agentsview to query months of history.

## Bottom line

**Recommended for engineers who want one live desktop view of tokens and limits across every tool they run, and who accept a fast-churning four-month-old app.**
Not for transcript search or provenance, and not for anyone who needs a settled, slow-moving tool.

## Changes

- 2026-10-06 - Created from the 2026-10-06 entrant scan: the category's first live multi-tool widget, with retention archiving and self-hosted sync, with five fetched sources.

## See also

- [CodeBurn](../codeburn/index.md) - the desktop spend sibling
- [ccusage](../ccusage/index.md) - the report-first incumbent
- [agentsview](../agentsview/index.md) - the archive alternative for history and search
- [Tokscale](../tokscale/index.md) - the CLI whose conventions and Cursor cache this widget follows
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/Javis603/token-monitor - 2,634 stars, 266 forks, MIT license, created 2026-05-19, as of 2026-10-06
- https://raw.githubusercontent.com/Javis603/token-monitor/main/README.md - the 43-plus-tool source table, live features, retention archive, hub sync options, and export formats
- https://api.github.com/repos/Javis603/token-monitor/releases - v0.67.0 (2026-10-06), v0.66.0 (2026-10-04), v0.65.0 (2026-10-02)
- https://formulae.brew.sh/cask/token-monitor - the Homebrew cask
- https://hn.algolia.com/api/v1/search?query=%22token%20monitor%22%20coding - the empty HN footprint behind the thin-community claim (the only name hit is an unrelated ESP32 project)
