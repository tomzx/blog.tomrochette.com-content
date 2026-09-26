---
title: JevBench
created: 2026-09-22
updated: 2026-09-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, benchmarking, model-evaluation]
readability: 3
audience_notes: >
  Engineers trying to pick between Jev and the open decision-model wave, who want a scoreboard instead of launch posts.
  Assumes you know what expected calibration error and a chance-corrected accuracy score are.
---

JevBench is Benchmark Heaven's MIT-licensed benchmark for Jev-class typed decision models: 534 English decisions per system in its v1.2 run plus 308 fresh sealed decisions in v1.4, scored on chance-corrected intelligence, calibration, speed, and cost, with public items, frozen and hashed artifacts, and per-task outcomes checked into the repository.

**This is the first third-party scoreboard for this category, and its two readings now frame the whole debate: on the public v1.2 board Jev led at 74.4 with SemIf's frozen-4B logit readout 1.3 points behind, but the sealed-decision v1.4 revision kept Jev first (63.3) while the open replicas fell away, which is the closest thing the category has to independent verification, arrived at by one runner's contested methodology.**

## What it is

A benchmark harness by fstandhartinger under the Benchmark Heaven banner (benchmarkheaven.com), created 2026-09-19, MIT-licensed code, datasets, and scoring.
The current v1.4 score blends 20% chance-corrected intelligence from the 308 fresh sealed decisions with 80% of the v1.3 intelligence axis, combines the four axes in an equal-weight harmonic mean, and cuts a system's intelligence when its public-to-sealed accuracy gap exceeds 25 points, so nothing can rank high on items it has effectively seen.
The earlier v1.3.0 score weighted Intelligence, Calibration, Speed, and Cost at 25% each in a geometric mean, with a growing penalty below 50 intelligence so a cheap fast guesser cannot rank high.
Intelligence is measured above chance per tier (220 hard decisions written by Claude Opus 5 and GPT-5.6 Sol, cross-reviewed, frozen, and hashed before any system ran, plus easy, standard, and judge tiers, 534 decisions per system in total).
Calibration combines ECE on the hard tier with fidelity to exact gold distributions.
Cost is priced in dollars per 1,000 decisions, not per 1,000 tokens, which is the unit that actually matters for this contract.
The v1.2 board holds 48 ranked rows spanning hosted APIs, the open replicas, rerankers, and GLiNER-style classifiers, with classifier.dev listed as an honorable mention because its fast tier is Jev itself, and the v1.4 board holds 76 measured systems.

## Status

Active and gaining traction, as of 2026-09-25.
The repository was created 2026-09-19, pushed 2026-09-24, and shows 121 stars and 13 forks, with three scoring releases since my first check (v1.4.0 through v1.4.2, September 23-24).
The Show HN thread (2026-09-22) climbed from 92 points when this note was created to 145 as of 2026-09-25, clearing the 100-point bar it originally sat under.
The v1.4 sealed-decision revision is the significant event: re-scoring against 308 decisions the entrants had not seen dropped SemIf from second (73.1) to eighth (47.7), kev-4B from 59.7 to 36.1, and Nimble from 60.5 to 18.7, while Jev held first, which is either the benchmark working as designed or evidence the public half was being selected against, depending on whose thread comment you read.
The author has 36 GitHub followers and no prior public footprint I could find, so I weight the methodology criticisms heavily.

## Strengths

- **The scoreboard exists, and it is replayable: public items, frozen per-task outcomes, scoring code, and a script that rebuilds the final artifact from the frozen measurements.**
- The design anticipates this category's specific tricks: chance-corrected intelligence defeats tiny-model majority-class games, calibration is scored against full distributions rather than argmax only, and cost is per decision.
- It measured the vendors too: on the v1.2 board Jev 1.13.0 scored 74.4, GPT-5.6 Luna 65.9 with the board's best intelligence at 95.3, Gemini 3.1 Flash-Lite 60.1, and DeepSeek V4.1 Flash 57.5 with the best calibration at 96.7 and the worst cost at $0.5937 per 1,000 decisions; the v1.4 sealed revision kept Jev first at 63.3 with two new entrants, JevK5 (62.0) and Hopper (59.4), directly behind it.
- Combination experiments (confidence cascades, committees, best-of-n) are reported separately in RESULTS-COMBINATIONS.md, and none changed the ranked board, which is the negative result a lazy benchmark would have omitted.
- The limitations are stated in the launch post itself: English-only, latency from one German server, a disclosed times-two adjustment for self-hosted and demo endpoints, held-out prompts still reaching evaluated services, and roughly one-point gaps being noise.

## Cautions

- **One runner built, ran, and scored everything, and the thread pushed back hard: one commenter said the results "do not seem to add up" and objected to the model set, another's keysmash test of the slop-detector demo (86% confidence on keyboard noise) became the real finding, and a third read the site as vibecoded.**
- The v1.4 re-scoring moved almost every row at once, and the benchmark's own explanation (sealed items catch selection against the public half) is an inference, not a measurement, so the collapse of the open replicas is provisional until someone re-runs it.
- The times-two latency adjustment for self-hosted and demo endpoints is a disclosed assumption, not a measurement, and it moves every local row.
- The board mixes unlike things: djev is an inference method over DiffusionGemma rather than a trained model, several rows are author demo endpoints rather than production services, and some prices are announced preview prices.
- Small models are hypersensitive to option order on this suite too (one entrant scored 72% versus 21% on the same items with reversed options), so single-number rankings hide a real fragility.
- Nobody independent has reproduced any of this, and the bottom-line claims shifted under the v1.4 revision, which vindicates the original caution but also means every v1.2 number quoted across this category's notes is now a historical reading rather than the current board.

## Pricing

Free and open: MIT-licensed harness, datasets, and scoring code, no hosted service and no paid tier.
The benchmark is free to run; the systems it scores bill at their own rates.

## Compared to

- [Nimble](../nimble/index.md): Bespoke's PUBLIC_BENCHMARKS.md is the other independent yardstick, 13 human-labeled subsets measured against Jev only; JevBench covers the whole category but its gold labels are model-written, not human-labeled.
- The Jev workflow evals (evals.typesafe.ai): the vendor's own scoreboard, which measures everything against an Astra-plus-Fable average and concedes the bias; JevBench is the outside answer to it.
- [SemIf](../semif/index.md): its RESULTS.md measures one frozen-model setup against TypeSafe's published values; JevBench ran SemIf as an entrant and scored it second overall on the v1.2 board.

## Bottom line

**Recommended as the category's first-stop scoreboard, read with the thread open in another tab, and as the artifact to re-run if you want to check any of its rows yourself.**
Not as grounds for a procurement decision, and not as a refutation of Jev: Jev held first across both boards, but a sealed-decision revision that erased most of the open replicas' standing in one pass is a reason to demand replication, not a conclusion.
The disagreeable claim I will defend: this benchmark's most important number is not Jev's 74.4, it is DeepSeek V4.1 Flash's 96.7 calibration and Luna's 95.3 intelligence, because they show the frontier models this category claims to beat are one score column away from competing, which should make everyone here uncomfortable.

## Changes

- 2026-09-22 - Created from the entrant scan after the 2026-09-22 Show HN thread reached 92 points; accepted as category infrastructure despite the sub-100-point thread, with the author-standing gap and the thread's methodology criticisms recorded.
- 2026-09-25 - Recorded the v1.4.0-v1.4.2 releases (September 23-24): 308 fresh sealed decisions and a public-to-sealed gap penalty re-scored the board, Jev held first (63.3) with new entrants JevK5 and Hopper behind, SemIf fell from 73.1 to 47.7; refreshed stars (121), forks (13), pushed date (2026-09-24), and the thread (145 points, now over the bar).

## See also

- [Jev](../jev/index.md) - the closed model this benchmark ranks first on both boards, and the vendor whose antibenchmaxxing stance it answers
- [SemIf](../semif/index.md) - the frozen-model readout that led the open field on the v1.2 board and fell on the sealed v1.4 revision
- [Nimble](../nimble/index.md) - the human-labeled alternative yardstick covering Jev and one replica
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note now belongs to
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where the decision layer you would benchmark this way gets chosen

## References

- https://github.com/fstandhartinger/jevbench - repository: MIT, created 2026-09-19, 121 stars, 13 forks, pushed 2026-09-24 (GitHub API, as of 2026-09-25)
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/README.md - the v1.4.1 score design, the 220 hard decisions frozen and hashed, the honorable-mention rule, and the option-order finding
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/results/v1.4/jevbench-v1.4-results.json - the v1.4 aggregate board (76 systems, sealed-decision blending, generated 2026-09-23)
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/RESULTS-v1.2.md - the full 48-row v1.2 board with per-axis scores, endpoints, and the times-two adjustment note
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/results/v1.2/jevbench-v1.2-results.json - the frozen results artifact behind the board
- https://news.ycombinator.com/item?id=49800574 - the 92-point launch thread (2026-09-22, 22 comments), its methodology and model-set objections the critical source (fetched via the Algolia items API)
