---
title: JevBench
created: 2026-09-22
updated: 2026-09-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, benchmarking, model-evaluation]
readability: 3
audience_notes: >
  Engineers trying to pick between Jev and the open decision-model wave, who want a scoreboard instead of launch posts.
  Assumes you know what expected calibration error and a chance-corrected accuracy score are.
---

JevBench is Benchmark Heaven's MIT-licensed benchmark for Jev-class typed decision models: 534 English decisions per system, scored on chance-corrected intelligence, calibration, speed, and cost, with public items, frozen and hashed artifacts, and per-task outcomes checked into the repository.
Facts below verified as of 2026-09-22.

**This is the first third-party scoreboard for this category, and its headline reading, hosted Jev first at 74.4 with SemIf's frozen-4B logit readout just 1.3 points behind on the same frozen items, is the closest thing the category has to independent verification, but it is one runner's contested methodology, not a verdict.**

## What it is

A benchmark harness by fstandhartinger under the Benchmark Heaven banner (benchmarkheaven.com), created 2026-09-19, MIT-licensed code, datasets, and scoring.
The v1.3.0 JevBench Score weights Intelligence, Calibration, Speed, and Cost at 25% each in a geometric mean, with a growing penalty below 50 intelligence so a cheap fast guesser cannot rank high.
Intelligence is measured above chance per tier (220 hard decisions written by Claude Opus 5 and GPT-5.6 Sol, cross-reviewed, frozen, and hashed before any system ran, plus easy, standard, and judge tiers, 534 decisions per system in total).
Calibration combines ECE on the hard tier with fidelity to exact gold distributions.
Cost is priced in dollars per 1,000 decisions, not per 1,000 tokens, which is the unit that actually matters for this contract.
The v1.2 board holds 48 ranked rows spanning hosted APIs, the open replicas, rerankers, and GLiNER-style classifiers, with classifier.dev listed as an honorable mention because its fast tier is Jev itself.

## Status

Active and four days old, as of 2026-09-22.
The repository was created 2026-09-19, pushed 2026-09-22, and shows 84 stars and 10 forks.
The Show HN thread (2026-09-22) sat at 92 points and 22 comments as of 2026-09-22, just under this category's 100-point bar, and I state that gap explicitly.
What carries it over: it fills the exact gap every note in this category names (nobody independent had measured these systems against each other), and the artifacts are built to be re-run, not admired.
The author has 36 GitHub followers and no prior public footprint I could find, so I weight the methodology criticisms heavily.

## Strengths

- **The scoreboard exists, and it is replayable: public items, frozen per-task outcomes, scoring code, and a script that rebuilds the final artifact from the frozen measurements.**
- The design anticipates this category's specific tricks: chance-corrected intelligence defeats tiny-model majority-class games, calibration is scored against full distributions rather than argmax only, and cost is per decision.
- It measured the vendors too: Jev 1.13.0 (74.4), GPT-5.6 Luna (65.9 with the board's best intelligence at 95.3), Gemini 3.1 Flash-Lite (60.1), and DeepSeek V4.1 Flash (57.5 with the best calibration at 96.7 and the worst cost at $0.5937 per 1,000 decisions).
- Combination experiments (confidence cascades, committees, best-of-n) are reported separately in RESULTS-COMBINATIONS.md, and none changed the ranked board, which is the negative result a lazy benchmark would have omitted.
- The limitations are stated in the launch post itself: English-only, latency from one German server, a disclosed times-two adjustment for self-hosted and demo endpoints, held-out prompts still reaching evaluated services, and roughly one-point gaps being noise.

## Cautions

- **One runner built, ran, and scored everything, and the thread pushed back hard: one commenter said the results "do not seem to add up" and objected to the model set, another's keysmash test of the slop-detector demo (86% confidence on keyboard noise) became the real finding, and a third read the site as vibecoded.**
- The times-two latency adjustment for self-hosted and demo endpoints is a disclosed assumption, not a measurement, and it moves every local row.
- The board mixes unlike things: djev is an inference method over DiffusionGemma rather than a trained model, several rows are author demo endpoints rather than production services, and some prices are announced preview prices.
- Small models are hypersensitive to option order on this suite too (one entrant scored 72% versus 21% on the same items with reversed options), so single-number rankings hide a real fragility.
- None of the category's own notes can cite it as ground truth yet, because nobody has reproduced it.

## Pricing

Free and open: MIT-licensed harness, datasets, and scoring code, no hosted service and no paid tier.
The benchmark is free to run; the systems it scores bill at their own rates.

## Compared to

- [Nimble](../nimble/index.md): Bespoke's PUBLIC_BENCHMARKS.md is the other independent yardstick, 13 human-labeled subsets measured against Jev only; JevBench covers the whole category but its gold labels are model-written, not human-labeled.
- The Jev workflow evals (evals.typesafe.ai): the vendor's own scoreboard, which measures everything against an Astra-plus-Fable average and concedes the bias; JevBench is the outside answer to it.
- [SemIf](../semif/index.md): its RESULTS.md measures one frozen-model setup against TypeSafe's published values; JevBench ran SemIf as an entrant and scored it second overall.

## Bottom line

**Recommended as the category's first-stop scoreboard, read with the thread open in another tab, and as the artifact to re-run if you want to check any of its rows yourself.**
Not as grounds for a procurement decision, and not as a refutation of Jev: a 1.3-point lead over a frozen 4B model on one contested suite is a reason to demand better verification, not a conclusion.
The disagreeable claim I will defend: this benchmark's most important number is not Jev's 74.4, it is DeepSeek V4.1 Flash's 96.7 calibration and Luna's 95.3 intelligence, because they show the frontier models this category claims to beat are one score column away from competing, which should make everyone here uncomfortable.

## Changes

- 2026-09-22 - Created from the entrant scan after the 2026-09-22 Show HN thread reached 92 points; accepted as category infrastructure despite the sub-100-point thread, with the author-standing gap and the thread's methodology criticisms recorded.

## See also

- [Jev](../jev/index.md) - the closed model this benchmark ranks first, and the vendor whose antibenchmaxxing stance it answers
- [SemIf](../semif/index.md) - the frozen-model readout that lands 1.3 points behind Jev on this suite
- [Nimble](../nimble/index.md) - the human-labeled alternative yardstick covering Jev and one replica
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note now belongs to
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where the decision layer you would benchmark this way gets chosen

## References

- https://github.com/fstandhartinger/jevbench - repository: MIT, created 2026-09-19, 84 stars, 10 forks, pushed 2026-09-22 (GitHub API, as of 2026-09-22)
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/README.md - the v1.3.0 score design, the 220 hard decisions frozen and hashed, the honorable-mention rule, and the option-order finding
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/RESULTS-v1.2.md - the full 48-row board with per-axis scores, endpoints, and the times-two adjustment note
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/results/v1.2/jevbench-v1.2-results.json - the frozen results artifact behind the board
- https://news.ycombinator.com/item?id=49800574 - the 92-point launch thread (2026-09-22, 22 comments), its methodology and model-set objections the critical source (fetched via the Algolia items API)
