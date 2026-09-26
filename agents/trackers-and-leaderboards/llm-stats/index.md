---
title: LLM Stats
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, trackers-and-leaderboards, llm, benchmarks, api]
readability: 3
audience_notes: >
  Engineers who want one composite leaderboard over current models, and agents that want leaderboard data through an API or MCP.
  Assumes you know what a benchmark aggregate is and why aggregating one is contested.
---

LLM Stats is a model-comparison platform that ranks 398 canonical models on a composite "LLM Stats Score", publishes task-level leaderboards, pricing, and comparison pages, and exposes the whole dataset through a REST API and an MCP server aimed at agents.

**It is the only member of this category that treats an agent, not a human, as the primary consumer of the leaderboard.**

## What it is

A website and data service: a composite leaderboard ("Rankings for 300+ Top AI Models by Intelligence, Speed & Price"), category boards for reasoning, coding, agents, math, long context, vision, and more, model compare and pricing pages, an AI news feed, a weekly newsletter, and arena products hosted under its sibling brand huggle.ai.
The methodology (score v3.1, updated 2026-09-02) is more careful than the aggregator genre demands: scores normalize within each benchmark, missing results are treated as missing rather than as failures, models with less evidence carry wider uncertainty, and lab-reported numbers are labeled separately from independently verified ones.
The developer surface lists endpoints for models, benchmarks, scores, rankings, and updates, plus "11 MCP tools" with one-click OAuth for Cursor, Claude Code, and Windsurf.
It is operated by ZeroEval Inc., which describes itself as building "the independent measurement layer for AI" and names LLM Stats as its first product; the founder is Jonathan Chavez, who Show HN'd earlier versions in November 2024 and January 2025.

## Status

Actively maintained: the methodology page was modified 2026-09-02, the docs repository was pushed 2026-09-08, and the news page is titled by the current month.
Traction is modest but growing: two small Show HNs (3 and 7 points), 20 HN comments referencing the site, and a small GitHub org, with self-reported reach (people at OpenAI, Anthropic, Google, Meta, "400,000+ more") that cannot be verified.
The corporate backing is self-displayed: a "Backed by" strip on zeroeval.com lists Y Combinator, Hugging Face, Harvard Medical, Google, and Datadog.

## Strengths

- The agent surface is the category's best: a free API tier plus MCP tools means your next session can query leaderboard data directly.
- The uncertainty-aware, missing-is-missing scoring policy is more statistically defensible than the genre's usual single-number bravado.
- Breadth of coverage (398 models, 50+ benchmarks claimed) with a compare tool and per-task boards for quick narrowing.

## Cautions

- The site is dressed for search engines: dozens of "best AI for X" landing pages (lawyers, architects, YouTube thumbnails) whose purpose is search traffic rather than measurement.
- Methodology details are partly gated: "We share additional methodology details with researchers, customers, and partners when appropriate", and pages sit behind a Cloudflare Turnstile for non-interactive clients.
- Early HN feedback flagged coverage gaps (Cerebras missing, "makes me wonder if other evaluations are missing") and the author's own admission that "some labs cherry pick the benchmarks they want to report".
- Paid evaluation services (custom benchmarking, data labeling) put revenue on the same side of the table as the companies being scored.

## Pricing

Free to browse, with a free Community API tier (250 data responses/day, 50 req/min, rolling 6-month history).
Builder: $99/month with 5,000 responses/day, 300 req/min, 12-month history, bulk snapshots, and an incremental-updates API.
Commercial: contract pricing with redistribution licensing and signed webhooks.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-24 | Community | Baseline: free tier at 250 data responses/day, 50 req/min, 6-month history | https://llm-stats.com/developer |
| 2026-09-24 | Builder | Baseline: $99/month at 5,000 responses/day, 300 req/min, 12-month history | https://llm-stats.com/developer |

## Compared to

- [Artificial Analysis](../artificial-analysis/index.md): first-party controlled evals with published weights; LLM Stats aggregates public evidence and labels it.
- [AI Release Tracker](../ai-release-tracker/index.md): the dated release log; LLM Stats is the current-rankings view of the same population.
- [LMArena](../lmarena/index.md): human preference rather than benchmark aggregation.

## Bottom line

**Recommended for wiring leaderboard data into agents and scripts on the free tier, and for a quick conservative read across many models; not as the deciding source for a deployment commitment.**
My disagreeable claim: the MCP server is the most consequential feature introduced in this category in years, because the reader of these leaderboards is becoming an agent that cannot click through a chart-dense SPA, and LLM Stats is the only member that noticed.

## Changes

- 2026-09-24 - Created.

## See also

- [Artificial Analysis](../artificial-analysis/index.md) - the first-party-measurement alternative to aggregation
- [AI Release Tracker](../ai-release-tracker/index.md) - the release log whose entries become LLM Stats rows
- [OpenRouter Rankings](../openrouter-rankings/index.md) - usage data as the counterweight to benchmark aggregates
- [Trackers and Leaderboards Feature Matrix](../trackers-and-leaderboards-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - what a composite score is and is not useful for when picking a model

## References

- https://llm-stats.com/ - homepage: 398 canonical models, composite score, task boards, newsletter (fetched 200, 2026-09-24)
- https://llm-stats.com/methodology/llm-stats-score - score v3.1 construction, evidence policy, limitations, 2026-09-02 modification date (fetched 200, 2026-09-24)
- https://llm-stats.com/developer - API and MCP endpoints, plan tiers and quotas, "updated within hours" claim (fetched 200, 2026-09-24)
- https://llm-stats.com/about-us - founder Jonathan Chavez and the zeroeval relationship (fetched 200, 2026-09-24)
- https://llm-stats.com/ai-news - the news feed and self-reported reach claim (fetched 200, 2026-09-24)
- https://zeroeval.com - ZeroEval Inc. description, product list, self-displayed "Backed by" strip (fetched 200, 2026-09-24)
- https://api.github.com/orgs/zeroeval - org metadata and docs-repo activity (fetched 200, 2026-09-24)
- https://news.ycombinator.com/item?id=42590841 - the January 2025 Show HN and authorship evidence (fetched 200, 2026-09-24)
- https://news.ycombinator.com/item?id=42231372 - the November 2024 launch thread with the Cerebras coverage-gap criticism (fetched 200, 2026-09-24)
