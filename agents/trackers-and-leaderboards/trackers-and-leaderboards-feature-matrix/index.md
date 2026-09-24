---
title: "Trackers and Leaderboards Feature Matrix"
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, trackers-and-leaderboards, benchmarks, leaderboards, open-data]
readability: 3
audience_notes: >
  Engineers deciding which field-watcher to trust for which question: releases, quality, trends, preference, or spend.
  Assumes you know what a benchmark leaderboard is; each column links to a full note with sources.
---

This matrix compares the six members of the Trackers and leaderboards category: sites whose product is a continuously refreshed number about the AI field itself.
The members split cleanly on what their number measures: what shipped ([AI Release Tracker](../ai-release-tracker/index.md)), what the operator measured ([Artificial Analysis](../artificial-analysis/index.md)), how the field moves ([Epoch AI](../epoch-ai/index.md)), what public evidence aggregates to ([LLM Stats](../llm-stats/index.md)), what people prefer ([LMArena](../lmarena/index.md)), and what people pay for ([OpenRouter Rankings](../openrouter-rankings/index.md)).

**No row of this matrix crowns a winner, because the rows are different questions; the failure mode is citing a site for a question it does not answer, usually LMArena ranks quoted as capability or OpenRouter tokens quoted as market share.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| | [AI Release Tracker](../ai-release-tracker/index.md) | [Artificial Analysis](../artificial-analysis/index.md) | [Epoch AI](../epoch-ai/index.md) | [LLM Stats](../llm-stats/index.md) | [LMArena](../lmarena/index.md) | [OpenRouter Rankings](../openrouter-rankings/index.md) |
| --- | --- | --- | --- | --- | --- | --- |
| Kind | release timeline plus flat-file corpus | independent benchmarking site and data business | research nonprofit with open datasets | composite aggregator with agent-facing API | blind preference arena | gateway usage rankings |
| The number measures | launch-day facts: what shipped, when, with which claimed scores | the operator's own controlled evals, prices, and speed runs | long-run trends: compute, cost, capability over time | public benchmark evidence, normalized with uncertainty | blind human preference votes | tokens processed through one gateway |
| Run by | To sider ApS, a Danish side project (one visible operator) | venture-backed independent company (AI Grant seed) | 501(c)(3) nonprofit, itemized donors, about 50 people | ZeroEval Inc. (self-displayed YC backing) | Arena Intelligence Inc. ($100M seed at $600M) | OpenRouter, a gateway acquired-by-Stripe (announced 2026-08-19) |
| Coverage | 231 releases, 10 labs (as of 2026-08-26) | 671 models, 100+ providers, 1,000+ endpoints, chips | 3,200+ models since 1950, data centers, chips, companies | 398 canonical models, 50+ benchmarks claimed | text, image, video, vision, search, webdev, agent arenas | 500+ models via the gateway, 80+ providers |
| Update cadence | on each release; dataset last updated 2026-08-26 | daily changelog; index versions iterate weekly | near-daily data updates, page-stamped | continuously; "within hours of release" claimed | continuous votes; product posts within days | daily UTC buckets, about one day of lag |
| Methodology published | ~ FAQ and data notes, no formal methodology | ✓ methodology hub with evaluation lists and weights | ✓ transparency page, papers, and data documentation | ~ score construction published, details gated | ✓ methodology repo (arena-rank) plus founding paper | ✓ on-page caveats plus Data API docs |
| Data access | ✓ /models.json and llms-full.txt, free with attribution | ~ web charts free, data platform paid, no public API documented | ✓ CC BY datasets and a Python client | ✓ REST plus 11 MCP tools, free tier | ~ arenas open, methodology open, raw votes not re-offered | ✓ CC BY 4.0 JSON via Data API, history to 2025-01-01 |
| Reader pricing | free, no ads; Pro instant alerts, price unpublished | free site; enterprise and data-platform tiers, prices unpublished | free, donation funded | free tier; Builder $99/month; Commercial contract | free | free, attribution required |
| Independence caveat | one operator, one company registration, no second pair of eyes | sells private benchmarking to the labs it ranks (disclosed policy) | consulted for OpenAI and DeepMind, disclosed and audited | paid eval services and a consumer sibling in the same company | lab partnerships and a documented private-testing history | owned by the gateway it measures, being absorbed by Stripe |
| Verification hooks | ✓ full corpus re-downloadable and diffable | ~ changelog and methodology public, raw runs private | ✓ data, notebooks, and code public | ~ API re-queryable, scoring internals partly gated | ✓ methodology code public, vote data not re-offered | ✓ daily snapshots re-fetchable under CC BY |

## Reading the matrix

**The row that sorts the category is "the number measures", and it doubles as a citation guide: release questions go to the tracker, present-tense quality to Artificial Analysis, trend claims to Epoch, quick composites to LLM Stats, preference to LMArena, spend to OpenRouter.**
The two most-quoted members are also the two most misquoted: LMArena ranks get read as capability, and gateway tokens get read as market share, when the matrix's own rows show both measure something narrower.

**Verification strength tracks institutional type, not popularity.**
The nonprofit (Epoch) publishes its funders, its consultations, and its data; the gateway (OpenRouter) publishes its raw daily numbers under CC BY; the side project (AI Release Tracker) lets you diff its whole corpus; while the three venture-scale companies publish methodology and products but keep raw runs, votes, or scoring internals private.
**If you need to check the work rather than read the work, the checkable columns are the nonprofit's, the gateway's, and the side project's, which is the opposite of what citation frequency would predict.**

**Every column carries a conflict row, and the conflicts are structural rather than scandals: the benchmark firm sells benchmarking to the benchmarked, the arena partners with the labs it ranks, the aggregator sells evaluation services, the gateway's data is its own marketing, and the nonprofit consults for the labs.**
Epoch's FrontierMath episode and LMArena's Maverick episode are the two documented failures, and both produced their institution's strongest disclosure artifacts, which is the pattern worth watching on every refresh of this page.

## Choosing from the matrix

- Needing a dated record of what shipped and what the lab claimed that day: AI Release Tracker, via its flat files.
- Picking a model or provider this week and needing quality against price and speed: Artificial Analysis, with the Endpoint Accuracy Index for the cheap-provider question.
- Citing how fast the field moves, with downloadable data: Epoch AI.
- Wiring leaderboard data into an agent or a script: LLM Stats's free API and MCP tools, accepting the gated internals.
- Sensing which model people prefer right now: LMArena, read as a mood ring and never as a capability claim.
- Asking what developers actually spend on: OpenRouter Rankings, quoted with its as-of date and its single-gateway caveat.

## Changes

- 2026-09-24 - Created with six columns (AI Release Tracker, Artificial Analysis, Epoch AI, LLM Stats, LMArena, OpenRouter Rankings) when the category was seeded at the owner's request.

## See also

- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the decision layer these measurements feed, and the leaderboard skepticism it argues for
- [People and Publications Feature Matrix](../../people-and-publications/people-and-publications-feature-matrix/index.md) - the voices interpreting these numbers, compared on their own matrix
- [Keeping Up With AI Is a Losing Strategy](../../../keeping-up-with-ai/index.md) - the filtering argument for keeping this category small and pull-driven

## References

- https://web.archive.org/web/20260826134434/https://aireleasetracker.com/ - AI Release Tracker column: scope, footprint, alerts, operator (fetched 200, 2026-09-24)
- https://artificialanalysis.ai/ - Artificial Analysis column: model count, indexes, provider coverage (fetched 200, 2026-09-24)
- https://artificialanalysis.ai/methodology/intelligence-benchmarking - Artificial Analysis column: published evaluation weights (fetched 200, 2026-09-24)
- https://epoch.ai/about/transparency - Epoch AI column: nonprofit status, funders, consultations (fetched 200, 2026-09-24)
- https://llm-stats.com/developer - LLM Stats column: API tiers, MCP tools, quotas (fetched 200, 2026-09-24)
- https://techcrunch.com/2025/05/21/lm-arena-the-organization-behind-popular-ai-leaderboards-lands-100m/ - LMArena column: funding and company identity (fetched 200, 2026-09-24)
- https://arxiv.org/abs/2504.20879 - LMArena column: the private-testing findings (fetched 200, 2026-09-24)
- https://openrouter.ai/rankings - OpenRouter Rankings column: methodology, caveats, licensing (fetched 200, 2026-09-24)
- https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/ - OpenRouter Rankings column: the ownership question (fetched 200, 2026-09-24)
- https://minimaxir.com/2026/05/openrouter-hy3/ - OpenRouter Rankings column: the free-tier distortion evidence (fetched 200, 2026-09-24)
