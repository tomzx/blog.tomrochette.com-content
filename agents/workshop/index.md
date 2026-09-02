---
title: Workshop
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation, observability, debugging, open-source]
readability: 3
audience_notes: >
  Engineers developing agents locally who want traces, evals, and fixes in one loop instead of a dashboard plus a spreadsheet.
  Assumes you know what a trace and an eval are.
---

Workshop is a free, MIT-licensed local debugger for AI agents from Raindrop that streams every token, tool call, and decision into a localhost web UI, and lets your coding agent read those traces, write evals against your codebase, and fix what fails.
Facts below verified as of 2026-09-02.

**Workshop's bet is that the eval writer should be the coding agent itself, inside the debug loop, and its weakest row is the one that decides enterprise adoption: nothing here touches CI.**

## What it is

A Bun-compiled binary (`curl -fsSL https://raindrop.sh/install | bash`) that runs a local daemon plus web UI on port 5899, storing traces in local SQLite unless you opt into Raindrop Cloud.
Slash-command skills (`/instrument-agent`, `/setup-agent-replay`) install into Claude Code, Codex, Devin, Cursor, and OpenCode, and a local MCP server exposes traces to the agent.
The self-healing loop is the product: the agent reads a captured trace, writes an eval file, runs your agent, sees the failure, patches the code, and re-runs, plus a replay endpoint that re-feeds a trace into local agent code.
SDKs exist for TypeScript, Python, Go, and Rust, about 15 frameworks are instrumented, and OTLP JSON ingest keeps it vendor-neutral.
Made by Raindrop, an agent-observability startup; Workshop is the free local tier of a paid cloud product.

## Status

Young with a strong launch: 1,068 stars, 63 forks, 7 open issues as of 2026-09-02, created 2026-05-01, latest release v0.1.21 on 2026-08-22.
39 commits, 9 contributors, 21 patch releases in four months.
**The launch testimonials are real engineers but the vendor's scale claims (billions of traces per month, Fortune 100 customers) are unverified marketing, and a 9-point Hacker News thread is the entire independent discussion.**

## Strengths

- The agent-in-the-loop eval loop is genuinely different from dashboard tools: your Claude Code or Codex session fixes what the trace shows.
- Local-first by default with a one-command install and MIT license.
- Broad instrumentation through SDKs, framework auto-instrumentors, and OTLP.
- Fast, founder-responsive shipping.

## Cautions

- Eval support is disconnected from CI, the sharpest criticism in its own launch thread, so nothing gates a merge.
- Install is a proprietary-built binary via curl; building from source is contributors-only.
- Pre-1.0 (v0.1.x) with a single-vendor contributor base.
- The free tool is the funnel for Raindrop Cloud at $299/month.

## Pricing

Workshop is free, local, MIT, no tiers.
Raindrop Cloud is optional: Hobby $0 (1,000 events/month), Pro $299/month plus per-event overage, Enterprise custom.

## Compared to

- [deepeval](../deepeval/index.md): a CI-run pytest-style eval framework with roughly 50 metrics; choose Workshop for the local agent-debug loop, deepeval to gate merges.
- [Phoenix](../phoenix/index.md): OTel-native observability spanning dev and production with experiments; choose Phoenix for vendor-neutral tracing at production scale.
- Hand-rolled scripts: right for a handful of deterministic assertions; Workshop buys the trace UI and the agent-fix loop.

## Bottom line

**Recommended for engineers actively developing agents with Claude Code or Codex who want the trace-to-fix loop on their laptop.**
Not for teams needing CI-gated eval suites today, or Windows-primary shops hedged by "probably Windows" support.

## See also

- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [deepeval](../deepeval/index.md) - the CI-gate counterpart
- [Phoenix](../phoenix/index.md) - the production-observability counterpart
- [Hamel Husain](../hamel-husain/index.md) - the eval-driven method this tooling automates

## References

- https://github.com/raindrop-ai/workshop - repository, README, install, license, adoption numbers
- https://www.raindrop.ai/workshop/ - the self-healing eval loop pitch and launch testimonials
- https://www.raindrop.ai/docs/workshop/overview - instrumentation, replay, and OTLP transport details
- https://www.raindrop.ai/ - Raindrop Cloud pricing tiers behind the free tool
- https://news.ycombinator.com/item?id=48196008 - the thin independent thread, including the CI-disconnect criticism
