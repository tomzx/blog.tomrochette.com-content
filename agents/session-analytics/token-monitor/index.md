---
title: Token Monitor
created: 2026-10-06
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, cost-tracking, desktop, open-source]
readability: 3
audience_notes: >
  Engineers who want a live desktop view of token usage and provider limits across every AI coding tool they run, on one machine or several.
  Assumes you know what a session file, a rate-limit window, and a token count are.
---

Token Monitor is an MIT-licensed desktop widget that parses the local session files of 54 named AI coding tools and shows live token usage, provider limits, and cost trends, with optional multi-device sync through a hub you host.

**Token Monitor is this category's first live widget aimed at every tool at once: agents-observe streams one harness's events into a dashboard and CodeBurn puts spend in a menu bar, while Token Monitor reads 54 named sources into one always-on window and keeps the history after the sources prune it.**

## What it is

A desktop application (Windows 10+, macOS 13+, Linux x64; Homebrew cask) whose source table grades each of 54 named tools separately for token usage, account limits, and session details, following Tokscale's path and environment-variable conventions, including reading Tokscale's Cursor cache for account-level Cursor usage.
The widget updates within seconds of each turn, shows a live tok/s rate, and expands to cache hit versus miss breakdowns, per-session token splits, and cost in USD, TWD, HKD, or CNY with daily-updated exchange rates.
An opt-in retention archive keeps daily tool and model usage locally after sources prune it (Claude Code drops transcripts after 30 days by default), and usage exports to CSV and JSON for spreadsheets, Obsidian, or Grafana.
Multi-device sync is hub-backed over Server-Sent Events with three self-hosted backends (in-widget hub, Node CLI hub, or Cloudflare Worker) or eventually consistent iCloud Drive, and single-device use needs no server at all.
Per-session detail reads transcripts on demand and is never synced; prompts, responses, and file contents stay local.
Made by Javis603, MIT-licensed.

## Status

Young and shipping daily: 3,038 stars, 358 forks, 143 open issues, created 2026-05-19, pushed 2026-11-14 (stars keep their earlier fetch date, the other counts are this run's), with v0.92.0 released 2026-11-13 (multiple GitHub Copilot accounts each with its own quota reading and enable, refresh, and remove actions, featured plugins auto-updating to stable releases while third-party sources wait behind a single Trust-and-update review, quota refresh buttons on the Limits rows and the Edge Dock card, an optional DeepSeek console token adding this month's Search and Fetch fees to the Spend tooltip, and last-known Today, Month, and Total figures with archived History shown right at launch in local mode), v0.91.0 released 2026-11-11 (an Edge Dock cache-hit-rate item, session search over titles, tool and model labels, and IDs, and ten more display currencies from AUD to SGD, beside a sync upload limit raised to 2 MiB), v0.90.0 released 2026-11-10 (Hark account quotas with desktop session detection or a manual cookie, Spanish across the app and the macOS widget, WSL scanning now off by default with saved choices preserved, and Thinking Machines' Inkling models named in charts), v0.89.0 released 2026-11-09 (Gemini CLI local session usage, plugin quota modules rendered natively on Home, Edge Dock, Notch Panel, Tray, and Floating Bubble, last-used models shown per session, and lower steady-state memory), and v0.88.0 released 2026-11-08 (Mistral Vibe local session usage, the Prime Agent and Jcode rows shipped after merging pending release, Mistral quota for API and Vibe Code subscriptions, MiniMax Code points split from API billing, native plugin quota modules, the OpenAI API credit-balance plugin available through discovery, and Copilot CLI native session-state usage), after the late-October line recorded in Changes (v0.83.0's network proxy and Claude Max and Ultra naming, v0.82.0's quota alerts and macOS 13 floor, v0.81.0's experimental desktop plugins, v0.80.0's multiple Claude Web accounts, and v0.79.0 through v0.70.0 before those), as of 2026-11-14; unreleased work keeps landing (Qoder international usage tracking with a Tokscale update, contribution guidance with issue forms and a security policy, and a Windows fix stopping the main window flashing grey on reopen), with the previously pending Prime Agent and Jcode rows, the credit-balance plugin, and the native quota modules all shipped.
Its source table keeps widening: the README now grades 54 named tools plus a third-party APIs aggregate (the README headline reads 54-plus AI coding tools, counting the aggregate), up from the 43-plus this note recorded at creation, with Hark and Gemini CLI the newest released rows beside OpenDesign, Prime Agent, and Jcode, and account-level quota sources (TypeSafe, OpenRouter, Volcengine, Ollama Cloud, Trae CN, Alibaba Cloud, StepFun, Notion AI, Manus, Hark) alongside session-file tools.
Its fork accounting was externally probed: the September 2026 AgentMeasure audit filed that Pi forks copied prior assistant records into new session files without cross-session dedup (issue 627), closed completed on 2026-09-12.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Javis603/token-monitor&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Javis603/token-monitor&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Javis603/token-monitor&type=date&legend=top-left" />
</picture>

I found no Hacker News thread for the project; the only search hit for the name is an unrelated ESP32 desk display.
**A four-month-old tool with a release cadence this category has never seen and zero independent discussion, which is exactly the profile to verify before trusting.**

## Strengths

- Live multi-tool coverage is a genuine gap: nothing else here renders usage across 54 named tools in one view as turns happen.
- The retention archive answers a genuine loss: harnesses prune transcripts (Claude Code at 30 days by default), and the category's archive tools can only index what still exists.
- Provider-limit detection spans session, daily, weekly, billing, and credits windows across 28-plus providers, including multiple OpenRouter profiles and prepaid balances.
- The sync story is self-hosted by construction (your widget, Node hub, or Cloudflare Worker), with iOS widgets through the Worker hub.

## Cautions

- A three-digit open-issue count against 3,038 stars and a daily release cadence within six months is a fast, churny project; expect breaking changes in a widget you leave running.
- Coverage is graded and uneven by design, and several limit sources are account-level cookie reads (Ollama Cloud, Alibaba Cloud console, Hark) rather than file parsing, a different trust model than the local reads the rest of this category does.
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
- 2026-10-28 - Recorded v0.80.0 (2026-10-26): multiple Claude Web accounts beside the detected Claude Code account with per-account login renewal, Muse Code session and weekly subscription quotas after muse login, and Ollama API-key authentication with monthly-credit display; a desktop plugin platform, Codex Pro tiers named by monthly price, and hub buffering fixes are landing unreleased; repository counts refreshed (forks 322 to 327, open issues 149 to 144) and the pushed date moved to 2026-10-28.
- 2026-10-31 - Recorded v0.81.0, v0.82.0, and v0.83.0 (2026-10-29 through 10-31): experimental desktop plugins with a community catalog, session reasoning effort for Codex and Claude Code, and Volcengine Coding Plan quotas; quota-alert notifications, official-catalog plugin updates independent of app releases, the macOS floor moving to 13 with macOS 12 dropped, and the Codex cache-expiry countdown removed; then a network proxy with a bypass list, Claude Max and Ultra plan naming, and memory reductions for Codex archive scanning; repository counts refreshed (forks 327 to 330, open issues 144 to 142) and the pushed date moved to 2026-10-31.
- 2026-11-01 - Recorded v0.84.0 (2026-11-01): Manus credits from a signed-in desktop account or supplied web session, Muse web quota beside Muse Code CLI limits, an Edge Dock that detaches into a draggable floating capsule, live token rates and measurement coverage exposed to plugins, and Codex empty completions excluded from output rates; the README's coverage claim moved to 48-plus tools (Manus the newest account-level row); repository counts refreshed (forks 330 to 333, open issues 142 to 150) and the pushed date moved to 2026-11-01.
- 2026-11-07 - Recorded v0.85.0, v0.86.0, and v0.87.0 (2026-11-03 to 11-06): a session filter by tool with remote-device labels and device icons, a 14-day quota-history hover and a Claude CLI fallback toggle, and OpenDesign subscription quotas with wider service-status monitoring and delta sync uploads; the README's coverage claim moved to 51 named tools plus a third-party APIs aggregate, up from 48-plus (OpenDesign the newest released row, Prime Agent and Jcode merged pending release); forks refreshed 333 to 348 and open issues 150 to 163, and the pushed date moved to 2026-11-07.
- 2026-11-08 - Volatile re-verification: no release after v0.87.0 with unreleased work continuing (an OpenAI API credit balance plugin published in the official catalog, native quota modules with manual credentials, Edge Dock detail-window sizing, and the Prime Agent and Jcode rows still pending release); the README headline reads 52-plus AI coding tools as of 2026-11-08, counting the third-party APIs aggregate beside the 51 named rows; forks refreshed 348 to 347 and open issues 163 to 156, and the pushed date moved to 2026-11-08.
- 2026-11-12 - Recorded v0.88.0 through v0.91.0 (2026-11-08 to 11-11): Mistral Vibe usage and quota, the Prime Agent and Jcode rows shipped after merging pending release, MiniMax Code points split from API billing, native plugin quota modules, the OpenAI API credit-balance plugin, Copilot CLI native session-state usage, Gemini CLI usage, Hark quotas, Spanish, WSL scanning off by default, session search, an Edge Dock cache-hit-rate item, and ten more display currencies; the README's coverage claim moved to 54 named tools plus a third-party APIs aggregate, up from 51 named (Hark and Gemini CLI the newest released rows); forks refreshed 347 to 355 and open issues 156 to 149, and the pushed date moved to 2026-11-12.
- 2026-11-14 - Recorded v0.92.0 (2026-11-13): multiple GitHub Copilot accounts each with its own quota reading and enable, refresh, and remove actions, featured plugins auto-updating to stable releases with third-party sources waiting behind a Trust-and-update review, quota refresh buttons on the Limits and Edge Dock rows, an optional DeepSeek console token adding this month's Search and Fetch fees to the Spend tooltip, and last-known usage with archived History shown right at launch in local mode; unreleased work continues (Qoder international usage tracking with a Tokscale update, contribution guidance with issue forms and a security policy, a Windows grey-flash fix, and a sync-status row fix); the README headline re-verified still 54-plus counting the aggregate; forks refreshed 355 to 358 and open issues 149 to 143, and the pushed date moved to 2026-11-14.

## See also

- [CodeBurn](../codeburn/index.md) - the desktop spend sibling
- [ccusage](../ccusage/index.md) - the report-first incumbent
- [agentsview](../agentsview/index.md) - the archive alternative for history and search
- [Tokscale](../tokscale/index.md) - the CLI whose conventions and Cursor cache this widget follows
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins

## References

- https://api.github.com/repos/Javis603/token-monitor - 3,038 stars (the dated baseline, never refreshed), 358 forks, 143 open issues, MIT license, created 2026-05-19, counts as of 2026-11-14
- https://raw.githubusercontent.com/Javis603/token-monitor/main/README.md - the 54 named-tool source table (headline 54-plus counting the third-party APIs aggregate), live features, retention archive, hub sync options, and export formats (re-fetched 2026-11-14)
- https://api.github.com/repos/Javis603/token-monitor/releases - v0.92.0 (2026-11-13), v0.91.0 (2026-11-11), v0.90.0 (2026-11-10), v0.89.0 (2026-11-09), v0.88.0 (2026-11-08), v0.87.0 (2026-11-06), and the October line back to v0.68.0 (re-fetched 2026-11-14)
- https://github.com/Javis603/token-monitor/issues/627 - the external audit's Pi fork dedup finding, closed completed 2026-09-12
- https://raw.githubusercontent.com/roy-tong/AgentMeasure/main/campaigns/audit-report-2026-09.md - the audit behind the external-probe sentence
- https://formulae.brew.sh/cask/token-monitor - the Homebrew cask
- https://hn.algolia.com/api/v1/search?query=%22token%20monitor%22%20coding - the empty HN footprint behind the thin-community claim (the only name hit is an unrelated ESP32 project)
