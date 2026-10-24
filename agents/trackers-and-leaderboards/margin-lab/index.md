---
title: Margin Lab
created: 2026-10-11
updated: 2026-10-23
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, trackers-and-leaderboards, benchmarks, monitoring, open-source]
readability: 3
audience_notes: >
  Engineers who use Claude Code or Codex daily and want an outside canary on silent quality regressions.
  Assumes you know what a pass rate and a confidence interval are.
---

Margin Lab runs daily benchmarks of Claude Code and Codex inside their shipped CLIs and publishes pass rates with statistical degradation detection, alongside Margin Evals, its open-source agent-eval runtime.

**It is the only member of this category that measures the deployed stack you run, tool and model together, instead of a model inside the operator's own harness.**

## What it is

A small independent shop (marginlab.ai, self-described as having no affiliation with frontier model providers) with two products: the Margin Evals runtime, an AGPL-3.0 Go orchestrator for reproducible agent evals that records accuracy, tokens, duration, and execution traces, and two public degradation trackers built on it.
Each tracker runs the current CLI release (Claude Code, Codex) against the frontier model of the moment (Opus 5.5/high and GPT-6 Sol/high as of 2026-10-11) on a curated, contamination-resistant subset of SWE-Bench Pro, N=50 instances per day, with 95% confidence intervals, weekly and monthly aggregates, and email alerts when a drop passes its per-window significance threshold.
The framing comes from Anthropic's September 2025 degradation postmortem, which the methodology cites as the reason the trackers exist.
The site also hosts benchmark explorers for SWE-Bench Pro and Terminal-Bench 2.0, plus historical performance pages for every earlier model generation.

## Status

Active but paused at its own gate: both trackers switched models on 2026-09-24 and are collecting fresh baselines, so degradation detection and significance verdicts are suspended until those baselines establish (the pages were last stamped September 29, 2026, re-confirmed 2026-10-23).
The 30-day pass rates as of 2026-10-23 read 81 percent for Claude Code (1,200 trials) and 79 percent for Codex (1,450 trials), unchanged across the 2026-10-11, 10-21, and 10-23 readings.
One wrinkle survived the rotation re-check: while the paused banners stand, the pages' change-overview panels still print rolling delta labels, and Codex's 30-day reading of minus 4.6 percent carries a "Statistically Significant" tag against its own plus or minus 1.7 percent threshold, a contradiction a reader relying on the banners would miss.
The footprint is the strongest in the category for its size: the launch thread ("Claude Code daily benchmarks for degradation tracking") drew 760 points on HN in January 2026, and the evals repository holds 160 stars as of 2026-10-11, though the public code has not been pushed since 2026-07-31 while the site's numbers update daily.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Margin-Lab/evals&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Margin-Lab/evals&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Margin-Lab/evals&type=date&legend=top-left" />
</picture>

## Strengths

- The measurement target is the one developers care about and nobody else watches: the shipped CLI plus the model behind it, where a regression costs productivity regardless of which side caused it.
- Statistical discipline most leaderboards skip: per-window significance thresholds derived from sample size, infrastructure failures excluded from the denominator, and verdicts withheld while a baseline re-establishes.
- The runtime is open source (AGPL-3.0), so the pipeline behind the numbers can be read and rerun.

## Cautions

- The confound is the design: a drop may be the model, the CLI, or the benchmark subset, and the top HN criticism was exactly that the daily scale (N=50, a plus or minus 13 percent threshold) cannot resolve anything.
- Coverage is narrow: two stacks and one benchmark family, so nothing here generalizes to the field.
- The current pause (detection suspended since the 2026-09-24 model switches) means the alerts a reader might subscribe for are not firing.
- The public repository has been quiet since July 2026 while the hosted numbers update daily, so the code and the site have drifted apart.
- The tracker pages carry a promote-your-product contact, an advertising side channel the methodology does not discuss.

## Pricing

Free: the trackers, the historical pages, the explorers, and the email alerts are public, and the runtime is AGPL-3.0 open source.
No paid tier is visible, so no price history applies.

## Compared to

- [LiveBench](../livebench/index.md): rotates public question sets for the whole field; Margin Lab freezes one subset and watches one stack daily.
- [Artificial Analysis](../artificial-analysis/index.md): controlled first-party evals of models in the operator's own harness; Margin Lab evals the tool the way a user runs it.
- [LMArena](../lmarena/index.md): preference votes on model output; Margin Lab pass rates on agentic task completion.

## Bottom line

**Recommended for teams that live inside Claude Code or Codex and want a canary for silent regressions in the exact stack they ship with; not for comparing models across labs, which its two-stack, one-benchmark scope cannot support.**
My disagreeable claim: the paused state is the best thing about it, because a detector that refuses to publish verdicts until its baseline re-establishes is measuring more carefully than the always-on leaderboards that never pause for anything.

## Changes

- 2026-10-11 - Created.
- 2026-10-11 - Added the star history chart.
- 2026-10-23 - Rotation re-verification with every cited URL re-fetched live: 30-day pass rates unchanged (81 percent Claude Code, 79 percent Codex), both trackers still collecting baselines and stamped September 29, 2026, the public repository still unpushed since 2026-07-31, and the change-overview panels observed printing statistically-significant delta labels while the paused banners stand (Codex 30-day minus 4.6 percent against a plus or minus 1.7 percent threshold).

## See also

- [LiveBench](../livebench/index.md) - the rotating-question counterpart to a fixed-subset daily watcher
- [Artificial Analysis](../artificial-analysis/index.md) - the controlled-eval layer whose harness difference Margin Lab exists to eliminate
- [Trackers and Leaderboards Feature Matrix](../trackers-and-leaderboards-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the decision these pass rates feed when a stack choice gets made

## References

- https://marginlab.ai/trackers/claude-code/ - the Claude Code tracker: method, N=50 daily runs, CIs and thresholds, paused baseline collection, 30-day 81 percent (fetched 200, 2026-10-11; re-fetched 200, 2026-10-23, unchanged, still stamped September 29, 2026)
- https://marginlab.ai/trackers/codex - the Codex tracker: the GPT-6 Sol/high baseline, the prior 83.40 percent baseline, 30-day 79 percent, and the exclusion rules (fetched 200, 2026-10-11; re-fetched 200, 2026-10-23, unchanged, with the change-overview panel now printing a statistically-significant minus 4.6 percent 30-day delta while paused)
- https://marginlab.ai/ - homepage: Margin Evals identity, supported agents and benchmarks, tracker summary cards (fetched 200, 2026-10-11; re-fetched 200, 2026-10-23, unchanged, 7-day cards 76 and 59 percent)
- https://api.github.com/repos/Margin-Lab/evals - repository metadata: 160 stars, AGPL-3.0, Go, pushed 2026-07-31 (fetched 200, 2026-10-11; re-fetched 200, 2026-10-23, pushed_at still 2026-07-31, star figure unchanged by policy)
- https://hn.algolia.com/api/v1/items/46810282 - the 760-point January 2026 thread and the significance criticism in its comments (fetched 200, 2026-10-11; re-fetched 200, 2026-10-23, unchanged)
