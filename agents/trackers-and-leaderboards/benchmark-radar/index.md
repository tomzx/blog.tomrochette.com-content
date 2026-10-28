---
title: Benchmark Radar
created: 2026-10-10
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, trackers-and-leaderboards, benchmarks, open-data, search-engine]
readability: 3
audience_notes: >
  Engineers and evaluation builders who need to find out which benchmarks exist for a capability, whether they are saturating, and where a reported score was published.
  Assumes you know what a benchmark leaderboard is.
---

Benchmark Radar is an open benchmark catalog and search engine that crawls 40 public sources daily, indexes AI benchmark records with their evidence, and tracks reported model scores over time, and it is the only member of its category whose subject is the benchmarks themselves rather than the models.

**Every other site in this category measures models; Benchmark Radar measures the measurement landscape, answering "which benchmarks exist, who ran them, and what did they report" from a corpus where every record keeps its source.**

## What it is

A web dashboard (benchmark-radar.org), a downloadable data ZIP, a Hugging Face dataset, an RSS feed, and an offline CLI with an agent skill (npx skills add ktwu01/benchmark-radar), built by Koutian Wu and contributors, MIT licensed for code and CC BY-NC-SA 4.0 for the technical report and editorial content.
Daily discovery draws on 40 sources (16 direct connectors and 24 first-party lab and research feeds, as of 2026-10-18), and the catalog merges the benchmark catalogs (OpenCompass Hub, Artificial Analysis, LLM Stats, and the Claire radar among them), with numeric score observations whose citations are preserved.
Surfaces: a Today feed with a daily briefing, a Benchmark Frontier leaderboard with a Pareto view of score against measured use, saturation and trend views, and per-record evidence pages.
The technical report (arXiv:2609.11115, v3, revised 22 September 2026) audited the catalog at 1,283 source records from 37 sources and 12,916 numeric observations on 790 records, and the project's data-driven badge states 39,640 records over 93 days as of 2026-10-28, so the corpus keeps outgrowing the paper's snapshot; the repository's citation, expanded on 2026-10-25 to list every contributor, now names 15 report authors.

## Status

Young and fast-moving: created 2026-07-27, 291 stars and 45 forks as of 2026-10-11, pushed 2026-10-28, with 143 open issues and discussions enabled (as of 2026-10-28).
The v0.13.0 stable release (published 2026-10-16) widened discovery to DataCite, OpenAIRE, the XBsleepy daily agent-benchmarks digest, and the Benchmark-Radar.com corpus, recovered roughly 150 benchmark release dates from their papers, made Chinese and Japanese source text searchable, and hardened the daily run so a failed GPT briefing no longer costs the day its snapshot.
The README badge claims Hugging Face's #1 Paper of the Day for 14 September 2026, and the README lists institutions whose researchers it says use the project (Google, Amazon, IBM, ByteDance, CMU, MIT, Tsinghua, and others), a self-reported claim.
Community footprint outside its own surfaces is near zero: an HN search for the project returns no stories as of 2026-10-10.
The 2026-10-20 push added a Models view to the dashboard (every scored model by lab, one column per source checkpoint), the project's first surface contributed by an outside developer, Qiming Bao, merged as PR #862, with the contributor's commit messages recording repeated AI-assisted review passes over the change.
The outside-contributed stream kept going: the 2026-10-22 merges add Models-panel and route-recovery fixes (PRs #910 and #927), unknown-star handling in the popular-repository ranking (PR #869), and a Phi-4 mini reasoning model card (PR #826), so three outside contributors have now landed changes beyond the first.
The 2026-10-24 and 10-25 merges add daily share cards (the day's top results as shareable images, PRs #930 and #934), a fourth outside contributor (rudycelekli, PR #938), and a consent gate for the analytics (see Cautions).
The 2026-10-27 and 10-28 merges widen sharing from the daily digest to any benchmark record (PR #1017, with the deploy gated on the card actually being served by the cards repository) and shorten the homepage title to lead with the brand for search results (PR #1022), both again co-authored by Claude models.
The dashboard is a client-rendered app, and this run's fetch returned the shell with a "Dashboard unavailable" data-file fallback, so live counts come from the repository badge and the Hugging Face dataset viewer rather than the rendered page.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ktwu01/benchmark-radar&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ktwu01/benchmark-radar&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ktwu01/benchmark-radar&type=date&legend=top-left" />
</picture>

## Strengths

- It answers a question no other member even frames: given a capability, which benchmarks exist for it, which are saturating, and where was each reported score published.
- The counts are auditable by design: every record retains source identity and citation, and the project publishes a catalog data contract, a public corpus schema, a scoring rubric, and daily Issues.
- The agent surface is a first-class product: an installable CLI skill for coding agents, plus a full data ZIP and a Hugging Face dataset for offline queries.

## Cautions

- One researcher's project, under three months old, with no independent critique, replication, or press coverage yet, so every quality claim currently traces back to the project itself.
- Its frontier score views mostly re-aggregate Artificial Analysis and LLM Stats scores (both credited in the README), so it inherits those members' methodologies and adds discovery and bookkeeping, not independent measurement.
- Microsoft Clarity analytics (session replay and heatmaps) now loads only after opt-in consent, with replay stopped across tabs on withdrawal, a 2026-10-25 change from the always-on load with a footer disclosure this note first recorded; the privacy cost is now conditional, but it is still present and still most rivals' absence.
- Licensing is mixed: MIT for code, but the technical report and editorial content are CC BY-NC-SA 4.0, and commercial republication requires written permission, so treat the corpus as attribution-plus for anything beyond the code.

## Pricing

Free: the dashboard, the data ZIP, the Hugging Face dataset, the RSS feed, and the CLI are public, with funding through GitHub Sponsors.
No paid tier exists, so no price history applies.

## Compared to

- [Artificial Analysis](../artificial-analysis/index.md): first-party measurement of models; Benchmark Radar consumes those published scores and indexes them alongside everything else.
- [LLM Stats](../llm-stats/index.md): aggregates model scores for ranking; Benchmark Radar catalogs benchmarks and their evidence for discovery and saturation questions.
- [LiveBench](../livebench/index.md): generates its own ground-truth scores; Benchmark Radar catalogs what others generated.

## Bottom line

**Recommended for evaluation builders choosing or designing a benchmark, and for agents that need benchmark discovery and score history offline; not for choosing a model this week.**
My disagreeable claim: the interesting numbers on this site are not any scores but the saturation and frontier views, because the field's benchmark pile grows daily (the project's own corpus is the evidence), and nobody else in this category watches the pile itself.

## Changes

- 2026-10-10 - Created.
- 2026-10-16 - The v0.13.0 stable release (published 2026-10-16) and its evidence recorded: discovery widened to DataCite, OpenAIRE, the XBsleepy daily digest, and the Benchmark-Radar.com corpus (the source count rose from 39 to 40), roughly 150 release dates recovered, CJK source text made searchable, and the badge count refreshed to 31,624 records over 81 days as of 2026-10-16.
- 2026-10-21 - Rotation re-verification with every cited URL re-fetched live, plus the 2026-10-20 push recorded: the dashboard gained a Models view (every scored model by lab, one column per source checkpoint), merged as PR #862 from an outside contributor with AI-assisted review passes noted in the commit messages, and the badge count refreshed to 35,064 records over 86 days as of 2026-10-21; v0.13.0 remains the newest release and the HN footprint still zero stories.
- 2026-10-23 - Volatile re-verification after the 2026-10-22 merges: three more outside contributors landed Models-panel, route-recovery, and unknown-star fixes (PRs #910, #927, #869) plus a Phi-4 mini reasoning card (PR #826), and the badge count refreshed to 36,762 records over 88 days as of 2026-10-23.
- 2026-10-25 - Volatile re-verification after the 2026-10-24/25 merges: the repository's citation now lists 15 report authors (expanded from nine named), daily share cards landed as the newest surface (PRs #930 and #934), a fourth outside contributor merged (rudycelekli, PR #938), Microsoft Clarity analytics moved to opt-in consent with cross-tab withdrawal, and the badge count refreshed to 37,927 records over 90 days as of 2026-10-25.
- 2026-10-28 - Volatile re-verification after the 2026-10-27/28 pushes: sharing extended from the daily digest to any benchmark record as a card (PR #1017, with deploys gated on card serving), a homepage-title search-engine change merged (PR #1022), and the badge count refreshed to 39,640 records over 93 days as of 2026-10-28; v0.13.0 remains the newest release.

## See also

- [Artificial Analysis](../artificial-analysis/index.md) - the measurement layer whose published scores feed this catalog
- [LLM Stats](../llm-stats/index.md) - the aggregator whose leaderboard data is one of the catalog's score sources
- [LiveBench](../livebench/index.md) - a benchmark that generates its own evidence instead of indexing others'
- [Trackers and Leaderboards Feature Matrix](../trackers-and-leaderboards-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where a benchmark choice lands when a model decision gets made

## References

- https://api.github.com/repos/ktwu01/benchmark-radar - repository metadata: 291 stars, 45 forks, MIT, created 2026-07-27 (re-fetched 200, 2026-10-28, pushed 2026-10-28, 143 open issues; star and fork figures unchanged by policy)
- https://raw.githubusercontent.com/ktwu01/benchmark-radar/main/README.md - 40 sources (16 connectors, 24 first-party feeds), the catalog sources including Artificial Analysis and LLM Stats, the CLI skill, the mixed license, the HF Paper of the Day badge, the citation expanded to 15 authors on 2026-10-25, and the paper citation (re-fetched 200, 2026-10-25, source count unchanged)
- https://api.github.com/repos/ktwu01/benchmark-radar/releases - the release train through v0.13.0 "stable release" (published 2026-10-16: DataCite, OpenAIRE, XBsleepy digest, and Benchmark-Radar.com corpus discovery sources, about 150 recovered release dates, CJK search, a hardened daily run) (re-fetched 200, 2026-10-28, v0.13.0 still newest)
- https://api.github.com/repos/ktwu01/benchmark-radar/commits?per_page=8 - the 2026-10-22 merge run behind the volatile refresh: PRs #910 and #927 (Models panel and route recovery), #869 (unknown-star handling), #826 (Phi-4 mini reasoning card), #918 (dark-theme fix) (fetched 200, 2026-10-23); the 2026-10-24/25 run behind that refresh: share-card features (#930, #934), the 15-author citation fix (#940), and the Clarity consent gate (#942) plus rudycelekli's OpenCompass category fix (#938) (fetched 200, 2026-10-25); the 2026-10-27/28 run behind this refresh: PR #1017 (share any benchmark as a card, with Pillow, share-activation, and deploy-gating fixes) and PR #1022 (homepage title shortened to lead with the brand) (fetched 200, 2026-10-28)
- https://benchmark-radar.org/data/records-badge.json - the data-driven record badge: 39,640 records over 93 days (re-fetched 200, 2026-10-28, up from 37,927 over 90 days)
- https://benchmark-radar.org/ - the dashboard surface: Today feed, Benchmark Frontier, the new Models view in the navigation, saturation and trend views, the Microsoft Clarity privacy notice, and the "Dashboard unavailable" client fallback observed by this fetch (fetched 200, 2026-10-10; re-fetched 200, 2026-10-21, shell again with the fallback)
- https://arxiv.org/abs/2609.11115 - the technical report: v3 revised 2026-09-22, nine authors, 37 sources, 1,283 source records, 12,916 numeric observations on 790 records (fetched 200, 2026-10-10; re-fetched 200, 2026-10-21, unchanged)
- https://huggingface.co/datasets/ktwu01/benchmark-radar - the dataset: four subsets (catalog 3.76k rows, radar_artifacts 19.7k, radar_observations 35.1k, scores 13.1k) under a benchmark-radar-mixed-terms license (fetched 200, 2026-10-10; re-fetched 200, 2026-10-21, subsets grown)
- https://hn.algolia.com/api/v1/search?query=%22benchmark%20radar%22&tags=story - zero stories: the missing independent footprint, stated as a signal (fetched 200, 2026-10-10; re-fetched 200, 2026-10-21, still zero)
