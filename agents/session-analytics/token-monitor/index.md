---
title: Token Monitor
created: 2026-10-06
updated: 2026-10-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, cost-tracking, desktop, open-source]
readability: 3
audience_notes: >
  Engineers who want a live desktop view of token usage and provider limits across every AI coding tool they run, on one machine or several.
  Assumes you know what a session file, a rate-limit window, and a token count are.
---

Token Monitor is an MIT-licensed desktop widget that parses the local session files of more than 47 AI coding tools and shows live token usage, provider limits, and cost trends, with optional multi-device sync through a hub you host.

**Token Monitor is this category's first live widget aimed at every tool at once: agents-observe streams one harness's events into a dashboard and CodeBurn puts spend in a menu bar, while Token Monitor reads 47-plus sources into one always-on window and keeps the history after the sources prune it.**

## What it is

A desktop application (Windows 10+, macOS 12+, Linux x64; Homebrew cask) whose source table grades each of 47-plus tools separately for token usage, account limits, and session details, following Tokscale's path and environment-variable conventions, including reading Tokscale's Cursor cache for account-level Cursor usage.
The widget updates within seconds of each turn, shows a live tok/s rate, and expands to cache hit versus miss breakdowns, per-session token splits, and cost in USD, TWD, HKD, or CNY with daily-updated exchange rates.
An opt-in retention archive keeps daily tool and model usage locally after sources prune it (Claude Code drops transcripts after 30 days by default), and usage exports to CSV and JSON for spreadsheets, Obsidian, or Grafana.
Multi-device sync is hub-backed over Server-Sent Events with three self-hosted backends (in-widget hub, Node CLI hub, or Cloudflare Worker) or eventually consistent iCloud Drive, and single-device use needs no server at all.
Per-session detail reads transcripts on demand and is never synced; prompts, responses, and file contents stay local.
Made by Javis603, MIT-licensed.

## Status

Young and shipping daily: 3,038 stars, 322 forks, 149 open issues, created 2026-05-19, pushed 2026-10-26, with v0.79.0 released 2026-10-25 (OmO Native and standalone Senpi token usage tracking with session details, the macOS Notch Panel graduating from experimental to a standard display mode with trackpad navigation and menu-bar quick controls, display-mode settings pages with previews, and OpenCode Console Go quota and Zen balance fixes), v0.78.0 released 2026-10-23 (Edge Dock System glass on Windows 11 and Transparent glass for the Edge Dock and Notch Panel on macOS, ZCode session titles with subagent sessions grouped under their parent, and fixes for lingering tooltips, an Edge Dock card revealing behind other windows, and Claude quota checks running in the shared temporary directory), v0.77.0 released 2026-10-21 (per-account API spend totals for today, the rolling week, and the month, plus optional batched Node Hub saves to cut disk writes), v0.76.0 released 2026-10-20 (configurable Home list counts of one to fifty items per section, macOS notch swipe gestures with a Grow mode, a separate Antigravity Gemini 4 Argon quota, and a Windows Edge Dock fix for the dock hiding behind other windows), v0.75.0 released 2026-10-19 (Antigravity subagents grouped under their parent, DeepSeek Harness project breakdowns, an experimental macOS Notch Panel with Home, Limits, Sessions, and Breakdown pages, and Windows scan-priority lowering), v0.74.0 released 2026-10-18, v0.73.0 released 2026-10-16 (Oh My Pi session details, Claude Desktop usage across Chat, Code, and Cowork, Goose on Windows, and Cursor Included-usage quota fixes), v0.72.0 released 2026-10-15, v0.71.0 on 2026-10-14, and v0.70.0 on 2026-10-13, as of 2026-10-26.
Its source table keeps widening: the README now grades 47-plus tools, up from the 43-plus this note recorded at creation, with OmO Native's local session records the newest session-file row and account-level quota sources (TypeSafe, OpenRouter, Volcengine, Ollama Cloud, Trae CN, Alibaba Cloud, StepFun, Notion AI) alongside session-file tools.
Its fork accounting was externally probed: the September 2026 AgentMeasure audit filed that Pi forks copied prior assistant records into new session files without cross-session dedup (issue 627), closed completed on 2026-09-12.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Javis603/token-monitor&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Javis603/token-monitor&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Javis603/token-monitor&type=date&legend=top-left" />
</picture>

I found no Hacker News thread for the project; the only search hit for the name is an unrelated ESP32 desk display.
**A four-month-old tool with a release cadence this category has never seen and zero independent discussion, which is exactly the profile to verify before trusting.**

## Strengths

- Live multi-tool coverage is a genuine gap: nothing else here renders usage across 47-plus tools in one view as turns happen.
- The retention archive answers a genuine loss: harnesses prune transcripts (Claude Code at 30 days by default), and the category's archive tools can only index what still exists.
- Provider-limit detection spans session, daily, weekly, billing, and credits windows across 28-plus providers, including multiple OpenRouter profiles and prepaid balances.
- The sync story is self-hosted by construction (your widget, Node hub, or Cloudflare Worker), with iOS widgets through the Worker hub.

## Cautions

- 141 open issues against 3,038 stars and v0.78 within six months is a fast, churny project; expect breaking changes in a widget you leave running.
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
- 2026-10-07 - Added the Javis603/token-monitor star history chart to the Status section.
- 2026-10-10 - Recorded v0.68.0 (2026-10-08): experimental Codex Dots local-task usage tracking (disabled by default), a manual Edge Dock refresh button, and Edge Dock size options; repository counts refreshed (2,646 to 2,714 stars, 268 to 269 forks).
- 2026-10-13 - Recorded v0.69.0 (2026-10-11): Claude Code and Codex waiting states shown before token usage arrives, Codex subagents grouped under their parent with combined usage, T3 Code session grouping, Cursor Grok Bot grouping, Antigravity session titles and native generation-speed readings, and Antigravity reasoning tokens included in usage totals; repository counts refreshed (2,765 to 2,988 stars, 107 to 119 open issues).
- 2026-10-13 - Recorded v0.70.0 (2026-10-13): CatPaw local-assistant usage tracking for the domestic and overseas editions on macOS and Windows (disabled by default), MiniMax pay-as-you-go API balance display in CNY or USD in Limits and Edge Dock, the digit-roll token animation, and usage fixes for Codex compressed sessions and Hermes double-charged reasoning tokens; repository counts refreshed (2,988 to 3,038 stars, 281 to 286 forks, 119 to 120 open issues).
- 2026-10-16 - Recorded v0.71.0 and v0.72.0 (2026-10-14 and 10-15) and the external AgentMeasure audit's Pi fork dedup finding closed completed on 2026-09-12 (issue 627); the pushed date moved to 2026-10-16.
- 2026-10-17 - Recorded v0.73.0 (2026-10-16): Oh My Pi session details, Claude Desktop usage across Chat, Code, and Cowork, Goose on Windows, and Cursor Included-usage quota fixes; the pushed date moved to 2026-10-17.
- 2026-10-19 - Recorded v0.74.0 (2026-10-18): a Liquid Glass clear style on macOS 26 or later, project breakdowns switching between tools and models token shares, Kilo Code native VS Code extension usage tracking, an experimental Top Notch entry, and Grok reasoning tokens folded into output and total usage; the pushed date moved to 2026-10-19.
- 2026-10-21 - Recorded v0.75.0 (2026-10-19: Antigravity subagents grouped under their parent, DeepSeek Harness project breakdowns, an experimental macOS Notch Panel, Windows scan-priority lowering) and v0.76.0 (2026-10-20: configurable Home list counts, notch swipe gestures with a Grow mode, a separate Antigravity Gemini 4 Argon quota, and a Windows Edge Dock z-order fix); the pushed date moved to 2026-10-21 and repository counts refreshed (forks 286 to 308, open issues 120 to 125).
- 2026-10-23 - Recorded v0.77.0 (2026-10-21: per-account API spend totals and batched Node Hub saves) and the README's coverage move to 46-plus graded tools, up from 43-plus, with the newest rows being account-level quota sources rather than session files.
- 2026-10-25 - Recorded v0.78.0 (2026-10-23): Edge Dock System glass on Windows 11 and Transparent glass for the Edge Dock and Notch Panel on macOS, ZCode session titles with subagent grouping, and fixes for lingering tooltips, an Edge Dock z-order regression, and Claude quota checks running in a shared temporary directory; repository counts refreshed (forks 308 to 318, open issues 125 to 141) and the pushed date moved to 2026-10-25.
- 2026-10-26 - Recorded v0.79.0 (2026-10-25): OmO Native and standalone Senpi token usage tracking with session details, the macOS Notch Panel graduated to a standard display mode with trackpad navigation and menu-bar quick controls, and OpenCode Console Go quota and Zen balance fixes; the README's coverage claim moved to 47-plus tools (OmO Native the newest session-file row), with Ollama API-key and Cookie-credit support and notch session-summary work landing unreleased; repository counts refreshed (forks 318 to 322, open issues 141 to 149) and the pushed date moved to 2026-10-26.

## See also

- [CodeBurn](../codeburn/index.md) - the desktop spend sibling
- [ccusage](../ccusage/index.md) - the report-first incumbent
- [agentsview](../agentsview/index.md) - the archive alternative for history and search
- [Tokscale](../tokscale/index.md) - the CLI whose conventions and Cursor cache this widget follows
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/Javis603/token-monitor - 3,038 stars, 286 forks, MIT license, created 2026-05-19, as of 2026-10-13
- https://raw.githubusercontent.com/Javis603/token-monitor/main/README.md - the 47-plus-tool source table, live features, retention archive, hub sync options, and export formats
- https://api.github.com/repos/Javis603/token-monitor/releases - v0.79.0 (2026-10-25), v0.78.0 (2026-10-23), v0.77.0 (2026-10-21), v0.76.0 (2026-10-20), v0.75.0 (2026-10-19), v0.74.0 (2026-10-18), v0.73.0 (2026-10-16), v0.72.0 (2026-10-15), v0.71.0 (2026-10-14), v0.70.0 (2026-10-13), v0.69.0 (2026-10-11), v0.68.0 (2026-10-08) (re-fetched 2026-10-26)
- https://github.com/Javis603/token-monitor/issues/627 - the external audit's Pi fork dedup finding, closed completed 2026-09-12
- https://raw.githubusercontent.com/roy-tong/AgentMeasure/main/campaigns/audit-report-2026-09.md - the audit behind the external-probe sentence
- https://formulae.brew.sh/cask/token-monitor - the Homebrew cask
- https://hn.algolia.com/api/v1/search?query=%22token%20monitor%22%20coding - the empty HN footprint behind the thin-community claim (the only name hit is an unrelated ESP32 project)
