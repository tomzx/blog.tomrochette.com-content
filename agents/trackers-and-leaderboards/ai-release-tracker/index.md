---
title: AI Release Tracker
created: 2026-09-24
updated: 2026-10-10
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, trackers-and-leaderboards, ai, releases, open-data]
readability: 3
audience_notes: >
  Engineers and agents that need a dated record of what AI models shipped when, with the launch-day numbers attached.
  Assumes you know what a model release cycle is; no benchmarking background required.
---

AI Release Tracker is a free, ad-free timeline of major frontier AI model releases since ChatGPT's launch on November 30, 2022, with launch-day benchmark scores, pricing, and machine-readable exports for each entry.

**It answers the one question every other site in this category layers something on top of: what shipped, when, with which launch-day numbers.**

## What it is

A timeline site whose FAQ describes "a free, continuously updated timeline of every major AI model release from the world's leading AI labs", tracking 258 models from 11 companies as of the 2026-10-07 archived homepage (OpenAI, Anthropic, Google, Meta, SpaceXAI, DeepSeek, Mistral, Moonshot AI, Z.ai, Qwen, NVIDIA).
Each entry records the release date, benchmark scores as published at launch (GPQA Diamond, SWE-Bench Verified, MMMU, Terminal-Bench, and others), parameter counts, context windows, license tier, and first-party API pricing where the lab publishes one.
Scores are framed as historical records, not live standings, and third-party-leaderboard figures are marked with their source.
The site also publishes "Expected" next-release dates per lab, which the author described as an average of the intervals between previous releases.
Surfaces: the timeline, per-benchmark ranking pages, model compare pages, analytics, pricing comparison, free email notifications on new releases, and flat-file exports: `/models.json` and a `llms-full.txt` corpus described as "plain text for LLM ingestion", free to use with an attribution link.

## Status

Alive and observable again: the Wayback gap closed, with an archived homepage dated 2026-10-07 showing a newest tracked release of Claude Haiku 5.5 (October 7, 2026), per-lab "expected next release" cards, and the September-October release wave confirmed recorded (the archived timeline lists GPT-6 Astra through GPT-6.1 Sol, Claude Opus 5.5 and Haiku 5.5, Gemini 4 Argon, Mistral Large 4, Grok 4.7, and DeepSeek-V4.1-Flash).
The archived homepage also claims a Business Insider citation ("As featured in Business Insider"), so the Show HN thread (2 points, 6 comments, 2025-12-02) is no longer the site's entire public footprint, though that citation remains self-claimed, and no GitHub repository exists.
The corpus flat files still have no archive captures after 2026-08-26 (CDX checked through 2026-10-10), and the live site 429'd this run's fetch, so the machine-readable exports remain pinned to the August snapshot.
The footer reads "© 2026 To sider ApS · CVR DK42753491", a Danish private limited company, so it is a side-project-grade operation with corporate paperwork.
**Treat it as alive, current through its rendered pages, useful, and one person away from dormant.**

## Strengths

- The flat files (`/models.json`, `llms-full.txt`) are the category's friendliest data source for agents: one fetch, structured, free, attribution-licensed.
- Launch-day scores are quotable in a way leaderboard standings are not, because a record of what the lab claimed on release day does not silently move.
- No ads, no account wall, and a scope (releases only) it does not pretend to extend past.

## Cautions

- Single-operator bus factor: one person, one company registration, no repository, no visible team.
- Verification is thin: the community footprint is one small Show HN thread, so data-entry errors would surface slowly.
- Naming quirks (xAI labeled "SpaceXAI") and via-attributed benchmark numbers mean the corpus needs spot checks before you cite it.
- The live site 429s automated fetchers, so agents should use the flat files or the archive rather than scraping the UI.

## Pricing

Free to use, no ads.
Free tier includes email notifications on new releases; a paid "Pro instant alerts" tier sends email the moment a model is added, with no price published.
No paid price is stated, so no price history applies.

## Compared to

- [LLM Stats](../llm-stats/index.md): current composite rankings with an API; AI Release Tracker is the historical log LLM Stats's score churns over.
- [Artificial Analysis](../artificial-analysis/index.md): live quality, price, and speed; choose it for what is true today, the tracker for what was claimed at launch.
- [Epoch AI](../epoch-ai/index.md): trend datasets and research; the tracker is the raw release stream Epoch-style analysis consumes.

## Bottom line

**Recommended for engineers and agents who want a dated, quotable "what shipped when" record with a machine-readable corpus, not for deciding what to deploy this week.**
My disagreeable claim: this is the most valuable site in the category for agents and the least visited by humans, because "what changed since last time" is the first question of every refresh run, and this is the only member that answers it as a flat file.

## Changes

- 2026-09-24 - Created.
- 2026-10-06 - Recorded the observability gap: no Wayback captures of the site or llms-full.txt after 2026-08-26, and the live site 429'd this run's models.json fetch, so coverage of the September-October release wave is unconfirmed.
- 2026-10-10 - The Wayback gap closed: the 2026-10-07 archived homepage shows 258 models from 11 companies (NVIDIA added), a newest tracked release of Claude Haiku 5.5 (October 7, 2026), and the September-October wave confirmed recorded, and the archived blurb adds a self-claimed Business Insider citation; the corpus flat files still lack archive captures after 2026-08-26.

## See also

- [LLM Stats](../llm-stats/index.md) - the live rankings layer that consumes the same release stream
- [Artificial Analysis](../artificial-analysis/index.md) - independent quality, price, and speed measurement of what the tracker logs
- [Epoch AI](../epoch-ai/index.md) - the long-run trend layer built from release-adjacent data
- [Trackers and Leaderboards Feature Matrix](../trackers-and-leaderboards-feature-matrix/index.md) - the category comparison this note joins
- [Keeping Up With AI Is a Losing Strategy](../../../keeping-up-with-ai/index.md) - why a cheap change-detector beats trying to read everything

## References

- https://web.archive.org/web/20260826134434/https://aireleasetracker.com/ - archived homepage: FAQ (231 models, 10 companies, free/pro alerts, no ads), footer "To sider ApS · CVR DK42753491" (fetched 200, 2026-09-24)
- https://web.archive.org/web/20260826134434/https://aireleasetracker.com/llms-full.txt - dataset scope, last-updated date, benchmark glossary, attribution terms (fetched 200, 2026-09-24)
- https://web.archive.org/web/20260826134434/https://aireleasetracker.com/models.json - structured export: 231 models with release dates, parameters, context windows, benchmarks (fetched 200, 2026-09-24)
- https://news.ycombinator.com/item?id=46119002 - the Show HN thread and the author's description of purpose and notifications (fetched 200, 2026-09-24)
- https://hn.algolia.com/api/v1/items/46119002 - full thread JSON backing the footprint claim (fetched 200, 2026-09-24)
- https://hn.algolia.com/api/v1/search?query=aireleasetracker&tags=story - the single-story footprint evidence (fetched 200, 2026-09-24)
- https://web.archive.org/cdx/search/cdx?url=aireleasetracker.com&matchType=domain - snapshot cadence and subpage inventory through 2026-08-26 (fetched 200, 2026-09-24)
- https://web.archive.org/cdx/search/cdx?url=aireleasetracker.com&matchType=domain&from=20260827&to=20261010&fl=timestamp,original,statuscode&limit=40 - site pages captured again from 2026-10-07: homepage, /about, /sitemap.xml, model pages (Claude Haiku 5.5), and compare pages (GPT-6.1 Sol, Claude Opus 5.5) (re-fetched 200, 2026-10-10, non-empty)
- https://web.archive.org/cdx/search/cdx?url=aireleasetracker.com/llms-full.txt&from=20260801&to=20261010&fl=timestamp,statuscode&limit=40 - corpus file captured only 2026-08-25 and 2026-08-26 (re-fetched 200, 2026-10-10, still two captures)
- https://web.archive.org/web/20261007193910/https://aireleasetracker.com/ - archived homepage: 258 models from 11 companies, newest tracked release Claude Haiku 5.5 (Oct 7, 2026), expected-next-release cards, the Business Insider mention, and per-company model lists (fetched 200, 2026-10-10)
