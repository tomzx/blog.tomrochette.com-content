---
title: BenchLM
created: 2026-10-11
updated: 2026-11-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, trackers-and-leaderboards, benchmarks, leaderboards, open-data]
readability: 3
audience_notes: >
  Engineers who want one composite model ranking and need to know how much evidence stands behind each position.
  Assumes you know what a benchmark aggregate is and why composites are contested.
---

BenchLM is a solo-maintained composite leaderboard that blends public benchmark evidence and other published leaderboards into one BenchAlign score per model, and labels every ranked position by how much evidence stands behind it.

**It is the only member of this category whose product is not a measurement but a provenance-labeled reading of everyone else's measurements.**

## What it is

A website, a downloadable dataset, and a query API covering 1,034 model profiles and 828 canonical benchmark pages, with 215 ranked entries (145 Supported, 70 Estimated) (as of 2026-11-21).
The BenchAlign score (v6.0 as of 2026-11-21) now fits a category-first two-parameter item-response model across open-licensed benchmarks, primary benchmark-owner boards, and capped developer launch cards, standardized on a frozen 92-model reference cohort, with no single evaluator exceeding 40 percent of a multi-evaluator score; a source legend apportions the 6,946 results behind the model pages at 50 percent developer cards, 40 percent benchmark-owner boards, 6 percent independent, 3 percent other-lab, and 1 percent upstream.
Missing tests stay missing, generated rows never enter the boards, and the confidence page cuts the 215 into four levels: 28 High, 75 Good, 58 Moderate, 54 Low/Estimated, with sourced-versus-generated row counts per model.
Data access is unusually complete for the genre: eight static JSON downloads with a SHA-256 manifest and content versions, a ninth dynamic endpoint (ai-model-changes.json) that sits outside the hashed manifest, plus a free Data account exposing REST and MCP endpoints under a CC BY-NC 4.0 license for BenchLM's own outputs.
It is built and maintained by one person publishing as Glevd, with an email contact and an X handle as the only disclosed identities.

## Status

Active and fresh: the site stamps its data refreshed November 21, 2026, with 1,034 tracked models, and the scoring policy iterates in dated steps (BenchAlign v6.0 as of this re-check, rebuilt from current inputs on every build).
The board's headline moved again: Claude Fable 5.2 is first by point estimate at 93.30 with a 90 percent interval of 88.6 to 98.0, now a Supported entry rather than an Estimated one, while the ranked total sits at 215 and Supported jumped from 77 to 145, the widest evidence base the board has printed.
The community footprint is close to zero: an HN search finds no BenchLM story of its own as of 2026-11-21, and the one independent sighting is still the June 2026 Show HN (Models Pie, 4 points) that names BenchLM as one of its three data sources.
No company, funding, or team is disclosed, so treat it as a one-person project with institutional-scale coverage and no institutional ballast.
**Treat it as a working cross-check layer, not a source of record.**

## Strengths

- The evidence labels are the genre's best: a reader can see, per rank, whether the position rests on exact sources or on the estimator's blend, and the confidence page counts sourced versus generated rows per model.
- The v6.0 methodology grounds its fit in a published source legend (50 percent developer launch cards, 40 percent benchmark-owner boards, 6 percent independent over 6,946 results), so a reader can see how much of the score comes from launch-card self-reporting.
- Agent-facing data without a paywall to start: hashed static JSON for offline use, plus REST and MCP on a free tier.

## Cautions

- It runs nothing itself, so every number is another board's measurement twice removed, and the errors inherit: a distorted input leaderboard distorts the blend.
- The headline breadth overstates the depth: 1,004 tracked profiles reduce to 216 ranked entries, and only 77 carry exact-source support.
- The Estimated intervals carry the operator's own warning that they do not establish confidence in a rank or future performance, and the machine metadata still reads roster-coverage and future-truth validation false as of 2026-11-21.
- The v5.8-era prose that disclosed its own three worsened retrospective checks is gone from the v6.0 methodology page, so the publish-your-own-failures distinction this note once credited now rests on machine flags alone.
- CC BY-NC 4.0 blocks commercial republication without a separate agreement, a sharper restriction than this category's other open datasets.
- One pseudonymous operator, no repository, no funding disclosure, and no second pair of eyes on the pipeline.

## Pricing

The site is free to read.
A free Data account covers REST and MCP queries; Pro and Research plans add saved ranking history and publisher snapshots, with no public prices.
Commercial display or redistribution of BenchLM-owned outputs needs a separate agreement, so no stated price exists and no price history applies.

## Compared to

- [LLM Stats](../llm-stats/index.md): the other composite aggregator; choose LLM Stats for its API maturity and MCP tooling, BenchLM when the question is how much evidence sits behind a rank.
- [Benchmark Radar](../benchmark-radar/index.md): the catalog of benchmarks themselves; BenchLM consumes that kind of evidence to rank models instead.
- [Artificial Analysis](../artificial-analysis/index.md): first-party measurement with published weights; BenchLM is a second opinion on that measurement, not a replacement.

## Bottom line

**Recommended as an evidence-reading layer over other people's leaderboards, and for agents that want hashed, dated JSON; not as a primary source for any deployment decision, because nothing in it was measured by the site that publishes it.**
My disagreeable claim: the most valuable writing BenchLM ever shipped was the failed-checks paragraph, and its quiet disappearance from the v6.0 methodology page is the better lesson, because the publish-your-own-broken-validation artifact every larger player in this category declines to ship proved fragile even here.

## Changes

- 2026-10-11 - Created.
- 2026-10-16 - Coverage refreshed from re-fetched homepage and confidence pages: 950 tracked models (from 889), 638 benchmark pages (from 625), 224 ranked entries (from 218) with 89 Supported (from 83), the confidence split now 27/62/69/66, the board's own verification stamp moved to October 15, and the BenchAlign leader reading 86.49.
- 2026-10-23 - Rotation re-verification with every cited URL re-fetched live: coverage to 972 tracked models (from 950), 668 benchmark pages (from 638), and 227 ranked entries (from 224) with 87 Supported (from 89) against 140 Estimated, the confidence split now 26/65/70/66, the board's verification stamp moved to October 20, and the site now declaring its own headline a statistical tie (Claude Opus 5.5 at 86.69 and GPT-6.1 Sol at 84.19 on overlapping 90 percent intervals); the data page added a ninth dynamic endpoint (ai-model-changes.json) outside the hashed manifest.
- 2026-11-01 - Rotation re-verification with every cited URL re-fetched live: coverage to 1,004 tracked models (from 972), 724 benchmark pages (from 668), and 216 ranked entries (from 227) with 77 Supported (from 87) against 139 Estimated, the confidence split now 27 High / 64 Good / 66 Moderate / 59 Low-Estimated with the level labels renamed from Full/Limited/Estimated, the board's stamp moved to October 29, 2026, and the headline tie replaced by Gemini 4 Carbon first by point estimate at 88.38 (Estimated, conditional range 78.7 to 98.1) with Claude Opus 5.5 the top Supported entry at 86.29; BenchAlign stays v5.8 and the CC BY-NC 4.0 data terms and ninth dynamic endpoint unchanged.
- 2026-11-21 - Rotation re-verification with every cited URL re-fetched live: coverage to 1,034 tracked models (from 1,004), 828 benchmark pages (from 724), and 215 ranked entries (from 216) with Supported jumping from 77 to 145 against 70 Estimated, the confidence split now 28 High / 75 Good / 58 Moderate / 54 Low-Estimated, the board's stamp moved to November 21, 2026, the headline replaced by Claude Fable 5.2 first by point estimate at 93.30 (a Supported entry with a 90 percent interval of 88.6 to 98.0), and the scoring policy recorded at BenchAlign v6.0 (a category-first two-parameter item-response fit over open-licensed benchmarks, primary benchmark-owner boards, and capped developer launch cards, on a frozen 92-model reference cohort with no single evaluator above 40 percent, with a source legend over 6,946 results); the v5.8-era prose disclosing the three worsened retrospective checks is gone from the methodology page (machine validation flags remain), so the Strengths, Cautions, and Bottom line were corrected, and the CC BY-NC 4.0 data terms and ninth dynamic endpoint unchanged.

## See also

- [LLM Stats](../llm-stats/index.md) - the incumbent composite aggregator BenchLM re-ranks against
- [Benchmark Radar](../benchmark-radar/index.md) - the benchmark-discovery layer whose catalogs feed composites like this one
- [Artificial Analysis](../artificial-analysis/index.md) - the first-party measurement layer BenchLM consumes as an input
- [Trackers and Leaderboards Feature Matrix](../trackers-and-leaderboards-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where a composite rank lands when a model choice gets made

## References

- https://benchlm.ai/ - homepage: 1,004 tracked, 724 benchmarks, 216 ranked, 77 Supported, leader Gemini 4 Carbon at 88.38 (Estimated, conditional range 78.7 to 98.1) with Claude Opus 5.5 at 86.29 the top Supported entry, data stamped "verified October 29, 2026" (fetched 200, 2026-10-11; re-fetched 200, 2026-10-23, counts up from 950/224/87 and the leader score from 86.49; re-fetched 200, 2026-11-01, counts up from 972/668/227/87 and the headline tie replaced by the Gemini 4 Carbon point-estimate lead; re-fetched 200, 2026-11-21, now 1,034 tracked, 828 benchmarks, 215 ranked with 145 Supported, leader Claude Fable 5.2 at 93.3 with a 90 percent interval of 88.6 to 98.0, data refreshed November 21, 2026)
- https://benchlm.ai/about - operator identity (Glevd), data sources, Supported/Estimated policy, what the site does not track (fetched 200, 2026-10-11; re-fetched 200, 2026-10-23, now also 141 grouped benchmarks, dataset stamped October 20; re-fetched 200, 2026-11-01, unchanged, 1,004 models and 724 benchmarks with 141 grouped into eight categories; re-fetched 200, 2026-11-21, dataset updated November 21, 2026, 6,946 results counted on model pages)
- https://benchlm.ai/methodology - BenchAlign v5.8 rules, the preference cap and peer constraints, and the three failed validation checks (fetched 200, 2026-10-11; re-fetched 200, 2026-10-23, unchanged, catalog refreshed October 20; re-fetched 200, 2026-11-01, BenchAlign v5.8 unchanged, rebuilt from current inputs on every build, dataset refresh stamped October 29, 2026; re-fetched 200, 2026-11-21, now BenchAlign v6.0, a two-parameter item-response fit on a frozen 92-model reference cohort with no single evaluator above 40 percent, with a source legend over 6,946 results; the v5.8-era failed-checks prose no longer appears on the page)
- https://benchlm.ai/data - CC BY-NC 4.0 terms, free Data account, REST and MCP endpoints, eight static JSON downloads with a SHA-256 manifest (fetched 200, 2026-10-11; re-fetched 200, 2026-10-23, now also the ninth dynamic ai-model-changes.json endpoint outside the manifest; re-fetched 200, 2026-11-01, unchanged, schema 1.0 source last updated October 29, 2026; re-fetched 200, 2026-11-21, 828 canonical benchmark pages as of November 21, 2026, schema 1.0 source last updated November 21, 2026, still eight static downloads plus the dynamic endpoint)
- https://benchlm.ai/benchmark-confidence - the confidence distribution (27 High, 64 Good, 66 Moderate, 59 Low/Estimated over 216 ranked as of 2026-11-01, the labels renamed from Full/Good/Limited/Estimated) and sourced-versus-generated coverage (fetched 200, 2026-10-11; re-fetched 200, 2026-10-16, 2026-10-23, and 2026-11-01; re-fetched 200, 2026-11-21, split 28 High / 75 Good / 58 Moderate / 54 Low-Estimated over 215 ranked)
- https://hn.algolia.com/api/v1/search?query=benchlm&tags=story - no BenchLM story of its own; the June 2026 Models Pie Show HN names BenchLM as a data source (fetched 200, 2026-10-11; re-fetched 200, 2026-10-23 and 2026-11-01, still no own story; re-fetched 200, 2026-11-21, still no own story, Models Pie still the sighting)
