---
title: "whatmodel.sh"
created: 2026-10-17
updated: 2026-10-17
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, leaderboards, benchmarks, llm, local-models, terminal]
readability: 3
audience_notes: >
  Engineers choosing a model and needing to know whether it fits the machine and budget they already have, plus anyone citing composite scores who wants the raw results one download away.
  Assumes you know what a benchmark leaderboard is and why averaging percentages across tests is unreliable.
---

whatmodel.sh is a curl-first composite leaderboard that fits every public benchmark result it can find onto one item-response-theory scale, then tells you which models your specific machine can run, at what speed, and at what price.

## What it is

A terminal-first leaderboard: `curl whatmodel.sh` returns the overall table, query parameters (`ram=`, `gpu=`, `vram=`, `max=`) filter it to what a given machine can run and afford, and `?format=json` exposes the same data to scripts and agents.
The scoring fits a single latent ability per model across 22,113 linked results with item response theory, pooling a level per evaluator run so one hot or cold setup cannot move a score ([method](https://whatmodel.sh/method)).
It covers 1,182 scored text models plus separate image, video, TTS, and STT lists, publishes raw results and benchmark definitions as downloads, and measures API speeds itself with the raw runs published ([terms](https://whatmodel.sh/terms), [API](https://whatmodel.sh/api?format=json)).
It is operated by Merlinsbeard Pty Ltd, a company with no public team page, and launched with a Show HN on 2026-10-12 ([the thread](https://news.ycombinator.com/item?id=50053608)).

## Status

Live and actively maintained as of 2026-10-17: the homepage stamp reads 2026-10-14, the terms page was last updated 2026-09-25, and the JSON API, help surface, and per-model pages all served on the day of writing.
The community footprint is close to zero: the launch thread carries two points and zero comments, and no independent coverage surfaced in search.
There is no public repository; the Show HN title says open source, but the terms license only the compiled dataset (CC BY-SA 4.0) and explicitly do not license the application code.

## Strengths

- The statistical grounding is the strongest in its kind: IRT with per-run level pooling, guessing-rate removal, saturated-test downweighting, and explicit uncertainty, with the prior art (Epoch's Capabilities Index, LMArena, HELM) credited and differentiated.
- Every result keeps a source link, and the raw data is re-downloadable (`results.json`, `benchmarks.json`), so a cited score can be traced and the board re-derived offline.
- The machine-fit angle is unique in its category: RAM and VRAM estimates from GGUF headers, measured per-chip speed medians rather than estimates, and price-cap filters in the query itself.
- Its own API speed measurements are published as raw runs, and a community bench script feeds reviewed submissions into the same tables.

## Cautions

- The method validation is self-reported: the hidden-test replay (about 85% pair accuracy, versus 77% for naive averaging) has no independent replication.
- One operator, no team page, no repository, and near-zero community footprint, so there is no second pair of eyes anywhere in the pipeline.
- Scores shift as models arrive and scores from different scales are not comparable, a documented but easy-to-cite-wrong property.
- The "open source" framing covers the CC BY-SA dataset only; the code that produces the scores is closed.

## Pricing

Free, with no paid tier and no sponsor slots documented.
The compiled numerical dataset is contributed under CC BY-SA 4.0; each underlying source keeps its own licence.

## Compared to

- [LLM Stats](../llm-stats/index.md): both are agent-facing composites, but LLM Stats normalizes public evidence into per-model entries with an MCP server, while whatmodel.sh fits one latent scale and answers the machine-fit question LLM Stats never asks.
- [BenchLM](../benchlm/index.md): both re-rank other boards' outputs, but BenchLM labels how much evidence stands behind each position while whatmodel.sh collapses everything into a single fitted score and hands you the raw results instead.
- [Epoch AI](../epoch-ai/index.md): the methodological sibling, since Epoch's Capabilities Index fits the same kind of model to benchmarks; Epoch is the nonprofit with the open datasets and the audits, whatmodel.sh the smaller operator adding run-level pooling and the hardware-fit layer.

## Bottom line

**Recommended for engineers picking a model that fits the machine and budget they already have, and for anyone who wants a comparable score with the raw results one download away.**
Not for citation as ground truth: one self-validated method, one operator, and no independent replication.

## Changes

- 2026-10-17 - Created after the trackers-and-leaderboards pass surfaced it in a candidate search and the coordinator resolved it the same run, with six sources fetched, the self-validation and thin-footprint cautions recorded as the critical angles, and the twelfth matrix column added.

## See also

- [LLM Stats](../llm-stats/index.md) - the closest composite by kind, and the API-and-MCP alternative when the machine-fit question does not matter.
- [BenchLM](../benchlm/index.md) - the other evidence-collapsing composite, worth reading beside this one for its per-position evidence labels.
- [Epoch AI](../epoch-ai/index.md) - the nonprofit whose Capabilities Index is the published prior art for the IRT fit used here.
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the decision layer these composite scores feed, and its argument for not trusting any one of them.

## References

- https://whatmodel.sh - the live board and its query interface, as of 2026-10-17.
- https://whatmodel.sh/method - the IRT methodology, per-run level pooling, validation replay, and data publications.
- https://whatmodel.sh/terms - the operator of record (Merlinsbeard Pty Ltd), the CC BY-SA dataset licence, and the code exclusion.
- https://whatmodel.sh/api?format=json - the agent-facing JSON surface served on the day of writing.
- https://whatmodel.sh/?help=1 - the full query-parameter surface grounding the machine-fit and price-cap claims.
- https://news.ycombinator.com/item?id=50053608 - the 2026-10-12 Show HN launch (two points, zero comments), the community-footprint record.
