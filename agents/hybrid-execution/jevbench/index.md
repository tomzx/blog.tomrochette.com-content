---
title: JevBench
created: 2026-09-22
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, benchmarking, model-evaluation]
readability: 3
audience_notes: >
  Engineers trying to pick between Jev and the open decision-model wave, who want a scoreboard instead of launch posts.
  Assumes you know what expected calibration error and a chance-corrected accuracy score are.
---

JevBench is Benchmark Heaven's MIT-licensed benchmark for Jev-class typed decision models: 534 English decisions per system in its v1.2 run plus 308 fresh sealed decisions in v1.4, scored on chance-corrected intelligence, calibration, speed, and cost, with public items, frozen and hashed artifacts, and per-task outcomes checked into the repository.

**This is the first third-party scoreboard for this category, and its readings now frame the whole debate: on the public v1.2 board Jev led at 74.4 with SemIf's frozen-4B logit readout 1.3 points behind, the sealed-decision v1.4 revision kept Jev first (63.3) while the open replicas fell away, the v1.4.2 point release then added eleven systems and a new #1, decider-4b v2 (64.13), with Jev second at 63.29, the v1.4.2.1 point release of 2026-09-27 added Plumb-4B (65.84) to push Jev to third, and the v1.4.2.2 point release a day later added Imajev-4B (67.37) to push Jev to fourth, which is still the closest thing the category has to independent verification, arrived at by one runner's contested methodology.**

## What it is

A benchmark harness by fstandhartinger under the Benchmark Heaven banner (benchmarkheaven.com), created 2026-09-19, MIT-licensed code, datasets, and scoring.
The current v1.4 score blends 20% chance-corrected intelligence from the 308 fresh sealed decisions with 80% of the v1.3 intelligence axis, combines the four axes in an equal-weight harmonic mean, and cuts a system's intelligence when its public-to-sealed accuracy gap exceeds 25 points, so nothing can rank high on items it has effectively seen.
The earlier v1.3.0 score weighted Intelligence, Calibration, Speed, and Cost at 25% each in a geometric mean, with a growing penalty below 50 intelligence so a cheap fast guesser cannot rank high.
Intelligence is measured above chance per tier (220 hard decisions written by Claude Opus 5 and GPT-5.6 Sol, cross-reviewed, frozen, and hashed before any system ran, plus easy, standard, and judge tiers, 534 decisions per system in total).
Calibration combines ECE on the hard tier with fidelity to exact gold distributions.
Cost is priced in dollars per 1,000 decisions, not per 1,000 tokens, which is the unit that actually matters for this contract.
The v1.2 board holds 48 ranked rows spanning hosted APIs, the open replicas, rerankers, and GLiNER-style classifiers, with classifier.dev listed as an honorable mention because its fast tier is Jev itself, and the v1.4.2 board held 93 measured systems, 89 of them ranked, before the v1.4.2.1 point release took it to 94 and 90 with the single addition of Plumb-4B and the v1.4.2.2 point release took it to 95 and 91 with the single addition of Imajev-4B.

## Status

Active and gaining traction, as of 2026-10-06.
The repository was created 2026-09-19, pushed 2026-09-29, and shows 227 stars and 23 forks, with five scoring releases since my first check (v1.4.0 through v1.4.2.2, September 23-27).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=fstandhartinger/jevbench&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=fstandhartinger/jevbench&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=fstandhartinger/jevbench&type=date&legend=top-left" />
</picture>

The Show HN thread (2026-09-22) climbed from 92 points when this note was created to 154 as of 2026-10-06, clearing the 100-point bar it originally sat under.
The author has also opened a second front: an ImageJevBench v0.1.x image-modality track now lives in the repository under results/imagejevbench, with a frozen 228-public plus 456-sealed split, and its v0.1.3 candidate re-measured Imajev-4B first of 49 at 76.39 on a paid fast-serving GPU run, a separate board from the unchanged text ranking.
A third front is the next text board itself: on 2026-09-29 the author published the frozen v1.5 scoring method with its disclosed addenda (an equal-axis, equal-type headline amendment over the byte-identical frozen method, pricing addenda including a DeepInfra disclosure correction, and a SHA-256 manifest), with the v1.4.2.2 board still current and no v1.5 results published yet.
The v1.4 sealed-decision revision is the significant event: re-scoring against 308 decisions the entrants had not seen dropped SemIf from second (73.1) to eighth (47.7), kev-4B from 59.7 to 36.1, and Nimble from 60.5 to 18.7, while Jev held first, which is either the benchmark working as designed or evidence the public half was being selected against, depending on whose thread comment you read.
The v1.4.2 point release (September 24) then added eleven new systems and completed swanOne's sealed run, and the new #1 was not Jev: decider-4b v2 (Mapika) took the top spot at 64.13 with Jev second at 63.29, JevK5 third (62.04), Cygnet fourth (61.76), and Hopper fifth (59.43), and the new leader's row carried its own caveats (34.7% sealed accuracy, an estimated price basis, and unaudited private stage-2 training rows).
The v1.4.2.1 point release (2026-09-27) then added Plumb-4B, a JevK5 v0.2 plus LoRA rebuild by crh225, which took the top spot at 65.84 and pushed Jev to third, though Jev keeps the best intelligence (53.1) and calibration (76.3) of the new top five, and Plumb's row leans on an estimated price basis of its own (a bookable GPU rate, not a bill).
The v1.4.2.2 point release (2026-09-27, with a 2026-09-28 text-only cost-basis correction) then added Imajev-4B by mohit67890, measured on the full v1.4 protocol and priced at a public DeepInfra Qwen3.5-4B rate estimate rather than a GPU bill, which took the top spot at 67.37 and pushed Jev to fourth; the release notes also record that Laya Vision stays out of the board under a separate author-confirmation hold.
The author has 36 GitHub followers and no prior public footprint I could find, so I weight the methodology criticisms heavily.

## Strengths

- **The scoreboard exists, and it is replayable: public items, frozen per-task outcomes, scoring code, and a script that rebuilds the final artifact from the frozen measurements.**
- The design anticipates this category's specific tricks: chance-corrected intelligence defeats tiny-model majority-class games, calibration is scored against full distributions rather than argmax only, and cost is per decision.
- It measured the vendors too: on the v1.2 board Jev 1.13.0 scored 74.4, GPT-5.6 Luna 65.9 with the board's best intelligence at 95.3, Gemini 3.1 Flash-Lite 60.1, and DeepSeek V4.1 Flash 57.5 with the best calibration at 96.7 and the worst cost at $0.5937 per 1,000 decisions; the v1.4 sealed revision kept Jev first at 63.3 with two new entrants, JevK5 (62.0) and Hopper (59.4), directly behind it, and the v1.4.2 through v1.4.2.2 additions then put decider-4b v2 (64.13), Plumb-4B (65.84), and Imajev-4B (67.37) at the top with Jev fourth at 63.29.
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
Not as grounds for a procurement decision, and not as a refutation of Jev: Jev held first until three consecutive point releases put two LoRA stacks and an Imajev-4B fine-tune ahead of it, and a sealed-decision revision that erased most of the open replicas' standing in one pass is a reason to demand replication, not a conclusion.
The disagreeable claim I will defend: this benchmark's most important number is not Jev's 74.4, it is DeepSeek V4.1 Flash's 96.7 calibration and Luna's 95.3 intelligence, because they show the frontier models this category claims to beat are one score column away from competing, which should make everyone here uncomfortable.

## Changes

- 2026-09-22 - Created from the entrant scan after the 2026-09-22 Show HN thread reached 92 points; accepted as category infrastructure despite the sub-100-point thread, with the author-standing gap and the thread's methodology criticisms recorded.
- 2026-09-25 - Recorded the v1.4.0-v1.4.2 releases (September 23-24): 308 fresh sealed decisions and a public-to-sealed gap penalty re-scored the board, Jev held first (63.3) with new entrants JevK5 and Hopper behind, SemIf fell from 73.1 to 47.7; refreshed stars (121), forks (13), pushed date (2026-09-24), and the thread (145 points, now over the bar).
- 2026-09-26 - The v1.4.2 point release (September 24) added eleven systems and a new #1: decider-4b v2 (Mapika) 64.13, Jev second at 63.29 with the top five's best intelligence and calibration, JevK5, Cygnet, and Hopper rounding out the five; refreshed stars (136), forks (14), pushed date (2026-09-25), and the thread (147 points); the board now holds 93 systems, 89 ranked, with a v1.4.3 roster pending.
- 2026-09-27 - The v1.4.2.1 point release added Plumb-4B (crh225, JevK5 v0.2 plus LoRA), which took the top spot at 65.84 and pushed Jev to third at 63.29, still the top five's best intelligence and calibration; refreshed stars (141), forks (15), pushed date (2026-09-27), and the thread (149 points); the board holds 94 systems, 90 ranked.
- 2026-09-29 - The v1.4.2.2 point release added Imajev-4B (mohit67890, priced on a public DeepInfra Qwen3.5-4B rate estimate), which took the top spot at 67.37 and pushed Jev to fourth at 63.29, and recorded that Laya Vision stays off the board under an author-confirmation hold; refreshed stars (175), forks (18), pushed date (2026-09-28), and the thread (151 points); the board holds 95 systems, 91 ranked.
- 2026-10-02 - Recorded the ImageJevBench v0.1.x image-modality track (frozen 228-public plus 456-sealed split; its v0.1.3 candidate re-measured Imajev-4B first of 49 at 76.39 on a paid fast-serving GPU run, a second board beside the unchanged text ranking); refreshed stars (195), forks (22), pushed date (2026-09-29), and the thread (153 points).
- 2026-10-02 - Recorded the frozen v1.5 scoring method published 2026-09-29 (equal-axis, equal-type headline amendment, pricing addenda including a DeepInfra disclosure correction, SHA-256 manifest) with the v1.4.2.2 board still current and no v1.5 results out.
- 2026-10-07 - Added the fstandhartinger/jevbench star history chart to the Status section.

## See also

- [Jev](../jev/index.md) - the closed model this benchmark ranks first on both boards, and the vendor whose antibenchmaxxing stance it answers
- [SemIf](../semif/index.md) - the frozen-model readout that led the open field on the v1.2 board and fell on the sealed v1.4 revision
- [Nimble](../nimble/index.md) - the human-labeled alternative yardstick covering Jev and one replica
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note now belongs to
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where the decision layer you would benchmark this way gets chosen

## References

- https://github.com/fstandhartinger/jevbench - repository: MIT, created 2026-09-19, 227 stars, 23 forks, pushed 2026-09-29 (GitHub API, as of 2026-10-06)
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/results/imagejevbench/v0.1.3/README.md - the ImageJevBench v0.1.x candidate: 228-public plus 456-sealed image split, Imajev-4B re-measured first of 49 at 76.39
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/docs/METHOD-v1.5-README.md - the frozen v1.5 method index: the byte-identical frozen method, the equal-axis equal-type headline amendment, the pricing addenda, and the SHA-256 manifest
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/README.md - the v1.4.1 score design, the 220 hard decisions frozen and hashed, the honorable-mention rule, and the option-order finding
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/results/v1.4.2.2/jevbench-v1.4.2.2-results.json - the v1.4.2.2 aggregate board (95 systems, 91 ranked) behind the Imajev-4B addition, read together with docs/RELEASE-v1.4.2.2.md and its 2026-09-28 text-only cost-basis correction
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/results/v1.4.2.1/jevbench-v1.4.2.1-results.json - the v1.4.2.1 aggregate board (94 systems, 90 ranked) behind the Plumb-4B addition, read together with docs/RELEASE-v1.4.2.1.md
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/RESULTS-v1.2.md - the full 48-row v1.2 board with per-axis scores, endpoints, and the times-two adjustment note
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/results/v1.2/jevbench-v1.2-results.json - the frozen results artifact behind the board
- https://news.ycombinator.com/item?id=49800574 - the launch thread (154 points as of 2026-10-06, 2026-09-22, 22 comments at creation), its methodology and model-set objections the critical source (fetched via the Algolia items API)
