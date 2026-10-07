---
title: "Trackers and Leaderboards Feature Matrix"
created: 2026-09-24
updated: 2026-10-07
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, trackers-and-leaderboards, benchmarks, leaderboards, open-data]
readability: 3
audience_notes: >
  Engineers deciding which field-watcher to trust for which question: releases, quality, trends, rotated public benchmarks, preference, or spend.
  Assumes you know what a benchmark leaderboard is; each column links to a full note with sources.
---

This matrix compares the seven members of the Trackers and leaderboards category: sites whose product is a continuously refreshed number about the AI field itself.
The members split cleanly on what their number measures: what shipped ([AI Release Tracker](../ai-release-tracker/index.md)), what the operator measured ([Artificial Analysis](../artificial-analysis/index.md)), how the field moves ([Epoch AI](../epoch-ai/index.md)), what freshly rotated public questions score ([LiveBench](../livebench/index.md)), what public evidence aggregates to ([LLM Stats](../llm-stats/index.md)), what people prefer ([LMArena](../lmarena/index.md)), and what people pay for ([OpenRouter Rankings](../openrouter-rankings/index.md)).

**No row of this matrix crowns a winner, because the rows are different questions; the failure mode is citing a site for a question it does not answer, usually LMArena ranks quoted as capability or OpenRouter tokens quoted as market share.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| | [AI Release Tracker](../ai-release-tracker/index.md) | [Artificial Analysis](../artificial-analysis/index.md) | [Epoch AI](../epoch-ai/index.md) | [LiveBench](../livebench/index.md) | [LLM Stats](../llm-stats/index.md) | [LMArena](../lmarena/index.md) | [OpenRouter Rankings](../openrouter-rankings/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | release timeline plus flat-file corpus | independent benchmarking site and data business | research nonprofit with open datasets | rotated public benchmark with published ground truth | composite aggregator with agent-facing API | blind preference arena | gateway usage rankings |
| The number measures | launch-day facts: what shipped, when, with which claimed scores | the operator's own controlled evals, prices, and speed runs | long-run trends: compute, cost, capability over time | objective ground-truth scoring of freshly rotated public questions | public benchmark evidence, normalized with uncertainty | blind human preference votes | tokens processed through one gateway |
| Run by | To sider ApS, a Danish side project (one visible operator) | venture-backed independent company (AI Grant seed) | 501(c)(3) nonprofit, itemized donors, about 50 people | academic consortium (ICLR 2025 Spotlight), day-to-day work by Abacus.AI engineers | ZeroEval Inc. (self-displayed YC backing) | Arena Intelligence Inc. ($100M seed at $600M) | OpenRouter, a gateway acquired-by-Stripe (announced 2026-08-19) |
| Coverage | 231 releases, 10 labs (as of 2026-08-26) | 691 models (as of 2026-10-07), 100+ providers, 1,000+ endpoints, chips | over 3,600 models since 1950, data centers, chips, companies | about 1,000 questions, 6 categories, 18 tasks, plus an agentic coding track | 400 canonical models, 50+ benchmarks claimed | text, image, video, vision, search, webdev, agent arenas | 500+ models via the gateway, 80+ providers |
| Update cadence | on each release; dataset last updated 2026-08-26 | daily changelog; index versions iterate weekly | near-daily data updates, page-stamped | monthly question releases in 2024, bursts since, newest set 2026-01-08; model configs still merged | continuously; "within hours of release" claimed | continuous votes; product posts within days | daily UTC buckets, about one day of lag |
| Methodology published | ~ FAQ and data notes, no formal methodology | ✓ methodology hub with evaluation lists and weights | ✓ transparency page, papers, and data documentation | ✓ paper, changelog, datasheet, and every question with its ground truth | ~ score construction published, details gated | ✓ methodology repo (arena-rank) plus founding paper | ✓ on-page caveats plus Data API docs |
| Data access | ✓ /models.json and llms-full.txt, free with attribution | ~ web charts free, data platform paid, no public API documented | ✓ CC BY datasets and a Python client | ✓ questions, model answers, and judgments on Hugging Face; run pipeline public | ✓ REST plus 11 MCP tools, free tier | ~ arenas open, methodology open, raw votes not re-offered | ✓ CC BY 4.0 JSON via Data API, history to 2025-01-01 |
| Reader pricing | free, no ads; Pro instant alerts, price unpublished | free site; enterprise and data-platform tiers, prices unpublished | free, donation funded | free; the team evaluates requested models at no charge | free tier; Builder $99/month; Commercial contract | free | free, attribution required |
| Independence caveat | one operator, one company registration, no second pair of eyes | sells private benchmarking to the labs it ranks (disclosed policy) | consulted for OpenAI and DeepMind, disclosed and audited | day-to-day operation by Abacus.AI, a commercial ML-platform vendor the benchmark helps market | paid eval services and a consumer sibling in the same company | lab partnerships and a documented private-testing history | owned by the gateway it measures, being absorbed by Stripe |
| Verification hooks | ✓ full corpus re-downloadable and diffable | ~ changelog and methodology public, raw runs private | ✓ data, notebooks, and code public | ✓ whole chain of questions, answers, and judgments downloadable and recomputable | ~ API re-queryable, scoring internals partly gated | ✓ methodology code public, vote data not re-offered | ✓ daily snapshots re-fetchable under CC BY |

## Reading the matrix

**The row that sorts the category is "the number measures", and it doubles as a citation guide: release questions go to the tracker, present-tense quality to Artificial Analysis, trend claims to Epoch, rotated-question scores to LiveBench, quick composites to LLM Stats, preference to LMArena, spend to OpenRouter.**
The two most-quoted members are also the two most misquoted: LMArena ranks get read as capability, and gateway tokens get read as market share, when the matrix's own rows show both measure something narrower.

**Verification strength tracks institutional type, not popularity.**
The nonprofit (Epoch) publishes its funders, its consultations, and its data; the gateway (OpenRouter) publishes its raw daily numbers under CC BY; the side project (AI Release Tracker) lets you diff its whole corpus; the academic consortium (LiveBench) publishes every question, answer, and judgment; while the three venture-scale companies publish methodology and products but keep raw runs, votes, or scoring internals private.
**If you need to check the work rather than read the work, the checkable columns are the nonprofit's, the consortium's, the gateway's, and the side project's, which is the opposite of what citation frequency would predict.**

**Every column carries a conflict row, and the conflicts are structural rather than scandals: the benchmark firm sells benchmarking to the benchmarked, the open benchmark doubles as its operator's research marketing, the arena partners with the labs it ranks, the aggregator sells evaluation services, the gateway's data is its own marketing, and the nonprofit consults for the labs.**
Epoch's FrontierMath episode and LMArena's Maverick episode are the two documented failures, and both produced their institution's strongest disclosure artifacts, which is the pattern worth watching on every refresh of this page.

## Choosing from the matrix

- Needing a dated record of what shipped and what the lab claimed that day: AI Release Tracker, via its flat files.
- Picking a model or provider this week and needing quality against price and speed: Artificial Analysis, with the Endpoint Accuracy Index for the cheap-provider question.
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
