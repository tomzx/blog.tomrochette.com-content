---
title: "Trackers and Leaderboards Feature Matrix"
created: 2026-09-24
updated: 2026-10-10
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, trackers-and-leaderboards, benchmarks, leaderboards, open-data]
readability: 3
audience_notes: >
  Engineers deciding which field-watcher to trust for which question: releases, quality, trends, rotated public benchmarks, preference, or spend.
  Assumes you know what a benchmark leaderboard is; each column links to a full note with sources.
---

This matrix compares the eight members of the Trackers and leaderboards category: sites whose product is a continuously refreshed number about the AI field itself.
The members split cleanly on what their number measures: what shipped ([AI Release Tracker](../ai-release-tracker/index.md)), what the operator measured ([Artificial Analysis](../artificial-analysis/index.md)), what the field's benchmarks are doing ([Benchmark Radar](../benchmark-radar/index.md)), how the field moves ([Epoch AI](../epoch-ai/index.md)), what freshly rotated public questions score ([LiveBench](../livebench/index.md)), what public evidence aggregates to ([LLM Stats](../llm-stats/index.md)), what people prefer ([LMArena](../lmarena/index.md)), and what people pay for ([OpenRouter Rankings](../openrouter-rankings/index.md)).

**No row of this matrix crowns a winner, because the rows are different questions; the failure mode is citing a site for a question it does not answer, usually LMArena ranks quoted as capability or OpenRouter tokens quoted as market share.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| | [AI Release Tracker](../ai-release-tracker/index.md) | [Artificial Analysis](../artificial-analysis/index.md) | [Benchmark Radar](../benchmark-radar/index.md) | [Epoch AI](../epoch-ai/index.md) | [LiveBench](../livebench/index.md) | [LLM Stats](../llm-stats/index.md) | [LMArena](../lmarena/index.md) | [OpenRouter Rankings](../openrouter-rankings/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | release timeline plus flat-file corpus | independent benchmarking site and data business | open benchmark catalog and search engine (one researcher's project) | research nonprofit with open datasets | rotated public benchmark with published ground truth | composite aggregator with agent-facing API | blind preference arena | gateway usage rankings |
| The number measures | launch-day facts: what shipped, when, with which claimed scores | the operator's own controlled evals, prices, and speed runs | the benchmark landscape itself: which benchmarks exist, who documented them, and what scores were reported where | long-run trends: compute, cost, capability over time | objective ground-truth scoring of freshly rotated public questions | public benchmark evidence, normalized with uncertainty | blind human preference votes | tokens processed through one gateway |
| Run by | To sider ApS, a Danish side project (one visible operator) | venture-backed independent company (AI Grant seed) | Koutian Wu and contributors (individual project, nine-author technical report) | 501(c)(3) nonprofit, itemized donors, about 50 people | academic consortium (ICLR 2025 Spotlight), day-to-day work by Abacus.AI engineers | ZeroEval Inc. (self-displayed YC backing) | Arena Intelligence Inc. ($200M Series B at $3.1B, 2026-10-08) | OpenRouter, a gateway acquired-by-Stripe (announced 2026-08-19) |
| Coverage | 258 releases, 11 labs (as of the 2026-10-07 archived homepage) | 696 models (as of 2026-10-10), 100+ providers, 1,000+ endpoints, chips | 20,710+ records from 39 sources (badge as of 2026-10-10); the paper's audit held 1,283 records | over 3,600 models since 1950, data centers, chips, companies | about 1,000 questions, 6 categories, 18 tasks, plus an agentic coding track | 408 canonical models (as of 2026-10-10), 50+ benchmarks claimed | text, image, video, vision, search, webdev, agent, alignment arenas | 500+ models via the gateway, 80+ providers |
| Update cadence | on each release; newest tracked release 2026-10-07 (archived homepage); flat-file archive captures still end 2026-08-26 | daily changelog; index versions iterate weekly | daily crawls; the record badge regenerates on every collection | near-daily data updates, page-stamped | monthly question releases in 2024, bursts since, newest set 2026-01-08; model configs still merged | continuously; "within hours of release" claimed | continuous votes; product posts within days | daily UTC buckets, about one day of lag |
| Methodology published | ~ FAQ and data notes, no formal methodology | ✓ methodology hub with evaluation lists and weights | ✓ technical report, scoring rubric, catalog data contract, public corpus schema | ✓ transparency page, papers, and data documentation | ✓ paper, changelog, datasheet, and every question with its ground truth | ~ score construction published, details gated | ✓ methodology repo (arena-rank) plus founding paper | ✓ on-page caveats plus Data API docs |
| Data access | ✓ /models.json and llms-full.txt, free with attribution | ~ web charts free, data platform paid, no public API documented | ✓ data ZIP, Hugging Face dataset, RSS, and an offline CLI with an agent skill | ✓ CC BY datasets and a Python client | ✓ questions, model answers, and judgments on Hugging Face; run pipeline public | ✓ REST plus 11 MCP tools, free tier | ~ arenas open, methodology open, raw votes not re-offered | ✓ CC BY 4.0 JSON via Data API, history to 2025-01-01 |
| Reader pricing | free, no ads; Pro instant alerts, price unpublished | free site; enterprise and data-platform tiers, prices unpublished | free; MIT code, CC BY-NC-SA 4.0 content | free, donation funded | free; the team evaluates requested models at no charge | free tier; Builder $99/month; Commercial contract | free | free, attribution required |
| Independence caveat | one operator, one company registration, no second pair of eyes | sells private benchmarking to the labs it ranks (disclosed policy) | re-aggregates two category members' scores (credited), runs Microsoft Clarity analytics, no independent critique yet | consulted for OpenAI and DeepMind, disclosed and audited | day-to-day operation by Abacus.AI, a commercial ML-platform vendor the benchmark helps market | paid eval services and a consumer sibling in the same company | lab partnerships and a documented private-testing history | owned by the gateway it measures, being absorbed by Stripe |
| Verification hooks | ✓ full corpus re-downloadable and diffable | ~ changelog and methodology public, raw runs private | ✓ every record keeps source identity and citation; daily Issues; reproducible analysis | ✓ data, notebooks, and code public | ✓ whole chain of questions, answers, and judgments downloadable and recomputable | ~ API re-queryable, scoring internals partly gated | ✓ methodology code public, vote data not re-offered | ✓ daily snapshots re-fetchable under CC BY |

## Reading the matrix

**The row that sorts the category is "the number measures", and it doubles as a citation guide: release questions go to the tracker, present-tense quality to Artificial Analysis, benchmark-discovery and saturation questions to Benchmark Radar, trend claims to Epoch, rotated-question scores to LiveBench, quick composites to LLM Stats, preference to LMArena, spend to OpenRouter.**
The two most-quoted members are also the two most misquoted: LMArena ranks get read as capability, and gateway tokens get read as market share, when the matrix's own rows show both measure something narrower.

**Verification strength tracks institutional type, not popularity.**
The nonprofit (Epoch) publishes its funders, its consultations, and its data; the gateway (OpenRouter) publishes its raw daily numbers under CC BY; the side project (AI Release Tracker) lets you diff its whole corpus; the academic consortium (LiveBench) publishes every question, answer, and judgment; the researcher's catalog (Benchmark Radar) publishes its corpus, schema, and rubric; while the three venture-scale companies publish methodology and products but keep raw runs, votes, or scoring internals private.
**If you need to check the work rather than read the work, the checkable columns are the nonprofit's, the consortium's, the gateway's, the side project's, and the researcher catalog's, which is the opposite of what citation frequency would predict.**

**Every column carries a conflict row, and the conflicts are structural rather than scandals: the benchmark firm sells benchmarking to the benchmarked, the open benchmark doubles as its operator's research marketing, the arena partners with the labs it ranks, the aggregator sells evaluation services, the gateway's data is its own marketing, the catalog re-aggregates two of this category's own members' scores, and the nonprofit consults for the labs.**
Epoch's FrontierMath episode and LMArena's Maverick episode are the two documented failures, and both produced their institution's strongest disclosure artifacts, which is the pattern worth watching on every refresh of this page.

## Choosing from the matrix

- Needing a dated record of what shipped and what the lab claimed that day: AI Release Tracker, via its flat files.
- Picking a model or provider this week and needing quality against price and speed: Artificial Analysis, with the Endpoint Accuracy Index for the cheap-provider question.
- Trying to find which benchmarks exist for a capability and whether they are saturating: Benchmark Radar, via the catalog, the saturation views, or the agent CLI.
- Citing how fast the field moves, with downloadable data: Epoch AI.
- Wanting an objective capability score whose every question, answer, and judgment can be downloaded and rerun: LiveBench, while watching its rotation cadence.
- Wiring leaderboard data into an agent or a script: LLM Stats's free API and MCP tools, accepting the gated internals.
- Sensing which model people prefer right now: LMArena, read as a mood ring and never as a capability claim.
- Asking what developers actually spend on: OpenRouter Rankings, quoted with its as-of date and its single-gateway caveat.

## Changes

- 2026-09-24 - Created with six columns (AI Release Tracker, Artificial Analysis, Epoch AI, LLM Stats, LMArena, OpenRouter Rankings) when the category was seeded at the owner's request.
- 2026-09-29 - Coverage cells refreshed: Artificial Analysis to 679 models and LLM Stats to 399 canonical models; membership unchanged.
- 2026-10-02 - Coverage cells refreshed: Artificial Analysis to 689 models and LLM Stats to 400 canonical models; membership unchanged.
- 2026-10-06 - Extended from six to seven columns with LiveBench, the contamination-limiting public benchmark leaderboard, sorted between Epoch AI and LLM Stats; the intro, sorting guide, verification-strength, conflict, and choosing prose updated.
- 2026-10-10 - Extended from seven to eight columns with Benchmark Radar, the open benchmark catalog and search engine with linked evidence, sorted between Artificial Analysis and Epoch AI; the intro, sorting guide, verification-strength, conflict, and choosing prose updated.
- 2026-10-10 - Coverage and status cells refreshed: Artificial Analysis to 696 models, LLM Stats to 408 canonical models, AI Release Tracker to 258 releases from 11 labs per the 2026-10-07 archived homepage, and LMArena's run-by cell to the $200M Series B at a $3.1B valuation.

## See also

- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the decision layer these measurements feed, and the leaderboard skepticism it argues for
- [People and Publications Feature Matrix](../../people-and-publications/people-and-publications-feature-matrix/index.md) - the voices interpreting these numbers, compared on their own matrix
- [Keeping Up With AI Is a Losing Strategy](../../../keeping-up-with-ai/index.md) - the filtering argument for keeping this category small and pull-driven

## References

- https://web.archive.org/web/20260826134434/https://aireleasetracker.com/ - AI Release Tracker column: scope, footprint, alerts, operator (fetched 200, 2026-09-24)
- https://artificialanalysis.ai/ - Artificial Analysis column: model count, indexes, provider coverage (re-fetched 200, 2026-10-06)
- https://epoch.ai/data - Epoch AI column: update stamps and the models explorer's over-3,600 count (re-fetched 200, 2026-10-06)
- https://artificialanalysis.ai/methodology/intelligence-benchmarking - Artificial Analysis column: published evaluation weights (fetched 200, 2026-09-24)
- https://epoch.ai/about/transparency - Epoch AI column: nonprofit status, funders, consultations (fetched 200, 2026-09-24)
- https://llm-stats.com/developer - LLM Stats column: API tiers, MCP tools, quotas (re-fetched 200, 2026-10-04, tiers unchanged)
- https://techcrunch.com/2025/05/21/lm-arena-the-organization-behind-popular-ai-leaderboards-lands-100m/ - LMArena column: funding and company identity (fetched 200, 2026-09-24)
- https://arxiv.org/abs/2504.20879 - LMArena column: the private-testing findings (fetched 200, 2026-09-24)
- https://openrouter.ai/rankings - OpenRouter Rankings column: methodology, caveats, licensing (re-fetched 200, 2026-10-06, data through Oct 5)
- https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/ - OpenRouter Rankings column: the ownership question (fetched 200, 2026-09-24)
- https://minimaxir.com/2026/05/openrouter-hy3/ - OpenRouter Rankings column: the free-tier distortion evidence (fetched 200, 2026-09-24)
- https://livebench.ai/ - LiveBench column: the leaderboard surface, client-rendered to this fetch (fetched 200, 2026-10-06)
- https://raw.githubusercontent.com/LiveBench/LiveBench/main/README.md - LiveBench column: design, categories and tasks, evaluation offer (fetched 200, 2026-10-06)
- https://raw.githubusercontent.com/LiveBench/LiveBench/main/changelog.md - LiveBench column: release history and newest question set 2026-01-08 (fetched 200, 2026-10-06)
- https://arxiv.org/abs/2406.19314 - LiveBench column: the paper, ICLR 2025 Spotlight, author consortium (fetched 200, 2026-10-06)
- https://api.github.com/repos/LiveBench/LiveBench - LiveBench column: repository state, 1,339 stars as of 2026-10-06 (fetched 200, 2026-10-06)
