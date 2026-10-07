---
showArticleList: false
title: Session analytics
created: 2026-09-24
visible: true
status: in progress
tags: [agents, session-analytics]
readability: 3
---

Tools that turn what coding agents already record into searchable history, cost reports, and audits, plus the ones that watch the sessions as they happen.

- [Agent Analytics](agent-analytics/index.md) - the agent-readable web analytics layer, tracker events in your own D1 or SQLite (or its cloud), queried through skill, MCP, CLI, or HTTP.
- [agents-observe](agents-observe/index.md) - the live dashboard for Claude Code and Codex sessions, hooks feeding a local server, multi-agent trees and cost breakdowns in real time.
- [agentsview](agentsview/index.md) - the local-first indexer for roughly 60 agents' session files, retrospective search and token-cost reporting in one SQLite store.
- [AgentTrace](agenttrace/index.md) - the local Rust TUI and CLI that audits session cost, tokens, latency, failures, and health across about 15 coding-agent formats, with CI gates.
- [ccusage](ccusage/index.md) - the zero-install CLI that turns eighteen coding agents' local usage files into daily-to-session cost reports, the incumbent every tool here benchmarks against.
- [claude-devtools](claude-devtools/index.md) - the local desktop DevTools that reconstruct Claude Code sessions from ~/.claude logs, with per-turn token attribution across seven context categories, tool-call inspection, and subagent trees.
- [claude-replay](claude-replay/index.md) - the zero-dependency CLI compiling sessions from seven harnesses into one self-contained interactive HTML replay with speed control, diffs, and secret redaction, the category's first shareable-artifact output, 843 stars.
- [ClawTrace](clawtrace/index.md) - the hosted tracing and cost-attribution platform for OpenClaw runs, with full-payload traces and an AI analyst named Tracy, billed in credits.
- [CodeBurn](codeburn/index.md) - the local desktop app and CLI that cuts AI coding spend by task, branch, and project, with plan-quota tracking, config optimization, and session spend guards.
- [ctx](ctx/index.md) - local search over the sessions agents already recorded, with blame attribution from any line of code back to its transcript.
- [Memex](memex/index.md) - the Rust CLI that indexes multi-harness session transcripts locally with BM25 or embeddings and resumes the session you find.
- [Token Monitor](token-monitor/index.md) - the live desktop usage widget across 43-plus AI coding tools, with provider-limit tracking, retention archiving, and self-hosted multi-device sync.
- [Tokscale](tokscale/index.md) - the terminal CLI and TUI that reads about 50 agents' local usage stores into one token and cost report, with an opt-in public leaderboard.

Its members are compared on shared rows in the [Session Analytics Feature Matrix](session-analytics-feature-matrix/index.md).

## Changes

- 2026-08-30 - Added agentsview.
- 2026-09-05 - Added ctx.
- 2026-09-16 - Added agents-observe.
- 2026-09-20 - Added Memex.
- 2026-09-27 - Added Agent Analytics.
- 2026-09-27 - Added AgentTrace.
- 2026-09-27 - Added ClawTrace.
- 2026-10-05 - Added ccusage.
- 2026-10-05 - Added CodeBurn.
- 2026-10-06 - Added claude-devtools.
- 2026-10-06 - Added Token Monitor.
- 2026-10-06 - Added Tokscale.
- 2026-10-07 - Added claude-replay.
