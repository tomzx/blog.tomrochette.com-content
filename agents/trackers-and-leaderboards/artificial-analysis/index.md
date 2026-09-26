---
title: Artificial Analysis
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, trackers-and-leaderboards, ai, benchmarks, evaluation]
readability: 3
audience_notes: >
  Engineers choosing models and inference providers who need independent quality, price, and speed numbers in one place.
  Assumes you know what tokens per second and price per million tokens mean.
---

Artificial Analysis is an independent benchmarking company whose site measures AI at four layers, agents, models, cloud inference providers, and chips, and publishes the results as leaderboards, price and speed comparisons, and a public changelog.

**It is the closest thing the field has to a consumer reports for model inference: one place where quality, cost, and speed are measured the same way across 671 models.**

## What it is

A website and data business covering models (proprietary and open weights), coding agents, inference providers, and accelerator hardware.
The flagship Artificial Analysis Intelligence Index (v4.3.2 as of 2026-09-24) incorporates ten evaluations with published weights (agents 30%, coding 20%, scientific reasoning 20%, general 30%), and a separate Coding Agent Index (v1.5) combines DeepSWE, Terminal-Bench, and SWE-Atlas-QnA.
The homepage compares 671 models on price per token, output speed, and latency, and its Endpoint Accuracy Index re-runs the same evals against 16 third-party providers of one model to measure how much accuracy each endpoint loses to quantization or configuration.
Products around the data include Optima (build-your-own benchmarks), MicroEvals, a Model Recommender, and a Data Playground.
Scale claims from the about page: 500+ models benchmarked, 100+ inference providers, 1,000+ endpoints, 1T+ evaluation tokens.

## Status

Very active and heavily cited: the changelog had entries dated 23 September 2026, one day before verification, and the Intelligence Index itself iterates weekly (v4.2 on September 5, v4.3 two days later, v4.3.2 by September 24).
Its numbers are market-moving enough that HN threads are titled by its rankings ("GLM-5.2 is the new leading open weights model on Artificial Analysis", 916 points in June 2026), and providers market against its measurements (Baseten's "fastest Kimi K2.5" post).
Founded by Micah Hill-Smith (CEO, ex-McKinsey) and George Cameron (CPO); started as a side project in 2023, launched January 2024, went viral after a Swyx retweet, and raised a seed from Nat Friedman and Daniel Gross's AI Grant with angels including Andrew Ng, Adam D'Angelo, Clem Delangue, Guillermo Rauch, and swyx.

## Strengths

- Breadth no rival matches: quality, price, speed, providers, and now chips, in one methodology.
- The methodology hub publishes evaluation lists, weights, and scoring detail, and the Endpoint Accuracy Index measures an error source (endpoint drift) nobody else prices in.
- A dated public changelog makes its own update cadence auditable.

## Cautions

- Its own methodology concedes prompts are partly written in-house and grading partly uses LLM judges, so the indexes measure the measurer as much as the models.
- HN criticism is persistent: "the benchmarks are bunk", a "lost all trustworthiness with the astra blunder" comment on the v4.2 thread, and a pay-to-play analogy for the benchmark-firm business model; a counterpoint in the same thread calls it "the best option currently available".
- It sells private custom benchmarking and an enterprise insights subscription to AI companies, the same companies it ranks; the founders state "no one pays to be on the public leaderboard" and describe a mystery-shopper policy, which you can accept or audit.
- Index version churn means any citation needs the version number and date or it goes stale within weeks.

## Pricing

The public site is free.
Revenue comes from an enterprise benchmarking-insights subscription and private custom benchmarking; a paid data platform exists (its terms PDF is published) with no public prices.
No public price is stated, so no price history applies.

## Compared to

- [LMArena](../lmarena/index.md): blind human votes instead of controlled evals; choose the arena for preference, Artificial Analysis for price and speed.
- [Epoch AI](../epoch-ai/index.md): trends and open datasets rather than leaderboard-style comparisons.
- [OpenRouter Rankings](../openrouter-rankings/index.md): revealed preference (actual spend) rather than constructed measurement.

## Bottom line

**Recommended as the default first stop when a decision needs a specific model's quality against its price and speed across providers, not for trend or adoption questions.**
My disagreeable claim: the Endpoint Accuracy Index is the most underrated page on the site, because quantization and endpoint defaults are the silent error source teams accept when they pick the cheap provider, and this is the only ranking in the category that makes that tradeoff visible.

## Changes

- 2026-09-24 - Created.

## See also

- [LMArena](../lmarena/index.md) - the crowd-preference counterpart to controlled benchmarking
- [OpenRouter Rankings](../openrouter-rankings/index.md) - what developers actually spend, as a check on what benchmarks imply
- [Epoch AI](../epoch-ai/index.md) - the trend-and-dataset layer this site's snapshots feed
- [Trackers and Leaderboards Feature Matrix](../trackers-and-leaderboards-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the per-token economics these benchmarks feed

## References

- https://artificialanalysis.ai/ - homepage: 671 models, Intelligence Index v4.3.2, Coding Agent Index v1.5, Endpoint Accuracy Index across 16 providers (fetched 200, 2026-09-24)
- https://artificialanalysis.ai/about - founders, backers, scale claims, four-layer scope (fetched 200, 2026-09-24)
- https://artificialanalysis.ai/methodology - methodology hub: scope, blended-price definition, benchmark inventory (fetched 200, 2026-09-24)
- https://artificialanalysis.ai/methodology/intelligence-benchmarking - the ten evaluations, weights, and scoring detail (fetched 200, 2026-09-24)
- https://artificialanalysis.ai/changelog - update cadence, entries dated 23 September 2026 (fetched 200, 2026-09-24)
- https://www.latent.space/p/artificialanalysis - founding story, seed round, revenue model, mystery-shopper policy (fetched 200, 2026-09-24)
- https://news.ycombinator.com/item?id=48567759 - 916-point HN thread showing citation scale (fetched 200, 2026-09-24)
- https://news.ycombinator.com/item?id=49586403 - the "astra blunder" criticism on the v4.2 thread (fetched 200, 2026-09-24)
- https://news.ycombinator.com/item?id=45706969 - the "benchmarks are bunk" skeptical take (fetched 200, 2026-09-24)
- https://artificialanalysiscdn.com/legal/ProDataPlatformTerms.pdf - existence of the paid data platform terms (fetched 200, 2026-09-24)
