---
title: "bestvaluemodel"
created: 2026-10-25
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, trackers-and-leaderboards, leaderboards, price-performance, open-source]
readability: 3
audience_notes: >
  Engineers choosing a model against a budget who want the value-for-money frontier computed for them,
  and anyone deciding whether a one-person derived view deserves their trust.
  Assumes you know what price per million tokens means.
---

bestvaluemodel is a single-page, automatically refreshed view that plots every model on Artificial Analysis's Intelligence Index against its API price and computes the value frontier, the models that nothing cheaper also beats on score.

**It answers the question the member it derives from never renders directly: at my budget, which is the most capable model I can buy.**

## What it is

A static page (bestvaluemodel.terrydjony.workers.dev) plus a public repository, built by a solo developer publishing as terryds and deployed on Cloudflare Workers.
A GitHub Actions workflow fetches Artificial Analysis's free data API every six hours, commits the snapshot to the repository only when something changed, and redeploys only on change, so the git history doubles as a dated diff log of the market.
The page computes the frontier client-side (sort by price ascending, keep every model that outscores everything cheaper, ties to the higher score then the lower price) and renders it three ways: a price-versus-score scatter, a budget lookup table with a pick and a runner-up per price rung, and a full sortable table with one row per reasoning setting.
A "What changed" card renders changelog.json, a per-run diff of added, removed, re-scored, and re-priced models, capped at 90 entries.
Every number on the page belongs to one source, Artificial Analysis's Intelligence Index and prices, attributed per that API's terms, with AA's cost-per-task figures taken as published.
The operator credits a hand-maintained predecessor (vps.sonnylab.com's "Which model is worth it" chart) as the inspiration this project automates.

## Status

Young but demonstrating the sustained operation its first rejection demanded: created 2026-09-24, with 45 commits through 2026-10-25 and data refreshes landing nearly every day since (the changelog shows diffs on almost every October day, including Beam 1.0's price cut and a Quasar reprice).
The repository held 26 stars and 4 forks as of 2026-10-25, with no license file, so the code is public but carries no reuse rights.
Community footprint is zero: an HN search returns no stories as of 2026-10-25, and I found no independent write-up of any kind.
The category rejected it at one day old in September as a derivative of member Artificial Analysis; the standing decision allowed a reopen on demonstrated sustained operation, and this run resolves that reopen with admission.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=terryds/bestvaluemodel&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=terryds/bestvaluemodel&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=terryds/bestvaluemodel&type=date&legend=top-left" />
</picture>

## Strengths

- The budget lookup is the only artifact in this category that turns a capability score into a purchase decision directly: find your price rung, read the pick.
- The pipeline is auditable end to end: public code, committed daily snapshots, a per-run diff feed, and a deploy that fires only when data moved.
- The reading caveats are careful for a one-person page: it documents why cached-input and batch pricing are excluded, why reasoning settings get separate rows, and that AA's cost-per-task covers fewer models.

## Cautions

- Every number is one member's measurement, so the frontier inherits Artificial Analysis's methodology wholesale; a distorted Index distorts every rung.
- One operator, 26 stars, zero independent coverage, and no license file, so there is no second pair of eyes and no reuse rights.
- The site lives on AA's free API (1,000 requests a day, attribution required, terms AA can change), so its continuity is borrowed.
- The frontier resets whenever AA re-bases the Index, and the page itself warns against comparing figures across versions.

## Pricing

Free: the page, the code, and the committed data snapshots are public, with no paid tier and no advertising.
No price history applies.

## Compared to

- [Artificial Analysis](../artificial-analysis/index.md): the first-party measurement this view consumes; AA publishes the inputs, bestvaluemodel computes the frontier AA never renders.
- [whatmodel.sh](../whatmodel-sh/index.md): the other composite that converts leaderboard data into a decision; whatmodel.sh answers what fits your machine, bestvaluemodel what fits your budget.
- [OpenRouter Rankings](../openrouter-rankings/index.md): what developers actually spend on, as the revealed-preference counterweight to what the price-quality math says they should buy.

## Bottom line

**Recommended as a quick value-for-money lookup before picking a model on a budget, and as a clean example of a derived view that shows its diffs; not as a capability source (it measures nothing itself) and not as a substitute for AA's own data.**
My disagreeable claim: this one-page derivative is more useful to a buyer than most leaderboards it sits beside, because its output is a decision rather than another number.

## Changes

- 2026-10-25 - Created, resolving the reopen the standing decision granted on demonstrated sustained operation (a month of refreshes through 2026-10-25).

## See also

- [Artificial Analysis](../artificial-analysis/index.md) - the measurement layer this frontier view is computed from
- [whatmodel.sh](../whatmodel-sh/index.md) - the other decision-facing composite, machine-fit instead of budget-fit
- [OpenRouter Rankings](../openrouter-rankings/index.md) - revealed spend as the counterweight to price-quality arithmetic
- [Trackers and Leaderboards Feature Matrix](../trackers-and-leaderboards-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the decision layer this budget table feeds

## References

- https://bestvaluemodel.terrydjony.workers.dev/ - the live page: frontier definition, budget lookup, what-changed card, and the how-to-read caveats (fetched 200, 2026-10-25)
- https://raw.githubusercontent.com/terryds/bestvaluemodel/main/README.md - architecture, the AA API attribution and its 1,000-request daily quota, and the vps.sonnylab.com inspiration (fetched 200, 2026-10-25)
- https://raw.githubusercontent.com/terryds/bestvaluemodel/main/.github/workflows/update-and-deploy.yml - the every-six-hours cron and the commit-and-deploy-only-on-change design (fetched 200, 2026-10-25)
- https://bestvaluemodel.terrydjony.workers.dev/data/changelog.json - the per-run diff feed, entries on nearly every October day including Beam 1.0's 2026-10-22 price cut (fetched 200, 2026-10-25)
- https://api.github.com/repos/terryds/bestvaluemodel - repository state: created 2026-09-24, 26 stars and 4 forks as of 2026-10-25, no license (fetched 200, 2026-10-25; star figure as the dated baseline)
- https://api.github.com/repos/terryds/bestvaluemodel/commits?per_page=100 - 45 commits from 2026-09-24 through 2026-10-25, the sustained-operation record (fetched 200, 2026-10-25)
- https://hn.algolia.com/api/v1/search?query=%22bestvaluemodel%22&tags=story - zero stories: the missing community footprint, stated as a signal (fetched 200, 2026-10-25)
- https://vps.sonnylab.com/model-value-2026-07.html - the hand-maintained predecessor the project cites as inspiration, itself updated through 2026-10-24 (fetched 200, 2026-10-25)
