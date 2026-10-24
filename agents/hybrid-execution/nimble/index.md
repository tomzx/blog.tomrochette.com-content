---
title: Nimble
created: 2026-09-21
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights, data-curation, model-evaluation]
readability: 3
audience_notes: >
  Engineers deciding between Jev and an open checkpoint, who care about human-labeled evidence more than launch posts.
  Assumes you know what a LoRA fine-tune, logits, and expected calibration error are.
---

Nimble is Bespoke Labs' one-day "open Jev": Bespoke-Nimble-9B, an Apache-2.0 LoRA fine-tune of Qwen3.5-9B that reads a flat schema of enum and boolean questions off the logits with no generated JSON, published together with the data, the training recipe, and a human-labeled benchmark suite run head-to-head against Jev.

**The checkpoint is average for the replica wave, but its benchmark suite is the only place in this category where Jev has been measured against human labels, and Jev wins by just 1.2 macro points.**

## What it is

A typed-decision scorer: text plus a flat schema in, one picked answer and per-candidate probabilities out; the original release capped enum fields at 26 single-token letter codes and prompts at 2,048 tokens, limits the 2026-09-24 checkpoint raised to 255 choices per field and 8,192-token prompts (the original preserved under the `original-2676` tag).
Serving runs on Apple Silicon through an MLX `ParallelScorer` that processes the shared context once, or on CUDA where each field is scored against the full prompt; observed medians are 106 ms per example on an H100 and 444 ms on an M5 Pro, against Jev's 247 ms through its API on the same holdout.
Training used 2,676 examples built by the project's own contrastive data curation (near-identical pairs differing in one fact that flips the label), LoRA rank 16, one epoch, and the README states no Jev outputs were distilled.
The authors are Bespoke Labs with Maheswaran Sathiamoorthy, whose earlier Bespoke-MiniCheck work with Greg Durett and Liyan Tang the acknowledgments credit as the foundation.

## Status

**Active and twenty-seven days old, with a near-zero HN footprint and the strongest verification artifacts of any project in the wave.**
The repository was created 2026-09-18 and shows about 2,200 stars and 165 forks as of 2026-10-15 (pushed 2026-10-24, branch activity, with the default branch's newest commits still the 2026-10-14 README timeline additions, after the 2026-10-05 Requesty transport and Unicode-separator fixes); the original weights were created 2026-09-18 and show 6,753 downloads and 242 likes, with the v3 checkpoint at 555 downloads and 14 likes, as of 2026-10-20.

The project has shipped a second generation: Bespoke-Nimble-9B-v2 (created 2026-09-23) carries the fitted-temperature checkpoint this note records below, and Bespoke-Nimble-9B-v3 (created 2026-09-30) is a retrained LoRA on the same Qwen3.5-9B base released under CC BY-NC 4.0, non-commercial, unlike the Apache-2.0 v1 weights; the README's timeline also credits v2's move into Ollama (2026-09-29, `ollama pull nimble`) and v3's 2026-10-06 turn as the top open model under 25B on the Decision Index.
A third generation runs on Bespoke's hosted API since 2026-10-13: Nimble-v4 (9B) and Nimble-v4-max (27B) at console.bespokelabs.ai, self-measured in the company's own 2026-10-12 run at 68.46 and 63.70 on the DI public suite, v4-max first overall and v4 first of the under-25B models, against Jev 1.13's 57.96 on the same suite; the board's edition-0.4 rebuild (2026-10-22, 229 configurations after the same-day regeneration, the Full score now entirely private) then carried a Bespoke Nimble v4 Max row at seventeenth of 229 (66.56), with Nimble 9B v3 at eightieth (51.06, down from 56.88 on the 0.2.1 board) and v2 at 114th (42.06).
Bespoke submitted v3 to the Decision Index the day it shipped, publishing a full 0.2.1 run (56.88) with raw results in its own dataset, and on JevBench's v1.6.1 open-weights board Nimble v3 ranks thirty-first at 53.5 while the original 9B composites at 21.1 (as of 2026-10-15, the board now 184 ranked rows).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=bespokelabsai/nimble&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=bespokelabsai/nimble&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=bespokelabsai/nimble&type=date&legend=top-left" />
</picture>

The Hacker News submission (2026-09-18) sits at 7 points and zero comments, so I state plainly that the community footprint is absent.
What substitutes is in the repo: a 13-subset, 3,880-record human-labeled suite (VitaminC, MASSIVE in English and German, BoolQ, SQuAD 2.0, PAWS, MultiNLI, Civil Comments, Aegis 2, HelpSteer2, two SummEval slices, PubMedQA) run against Jev 1.13.0, which no vendor and no other replica has done.
The project has kept shipping: the 2,676 training examples and the 324-example holdout were published on 2026-09-20 (they had been left out of the first release by mistake), the hosted deployment's prompt limit rose to 8,192 tokens on 2026-09-19, and on 2026-09-22 a temperature was fitted for the checkpoint (same picked answers, better-matching probabilities).

## Strengths

- **The external evidence nobody else has: on human labels Jev macros 76.0% against Nimble's 74.8%, Jev takes the boolean tasks, Nimble takes the rubric-rating tasks, and Jev has the lower calibration error on 11 of 13 subsets; these 3,880 records are the fairest public yardstick this category has.**
- Contrastive data curation is a transferable recipe: one-fact-flips-the-label pairs, model-checked with replayable requests, published with checksums and an offline dataset verifier.
- The self-criticism is unusual for the genre: the README concedes the holdout is 324 synthetic examples from six source families, that no temperature was fitted, that contamination is plausible, and that position bias is unmeasured.
- It runs locally on a Mac with no TypeSafe key, and a contract file pins the base revision and a prompt-code hash against the scorer.

## Cautions

- **The probabilities are checkpoint-dependent now: the original release's fitted temperature (2026-09-22) belongs to the `original-2676` revision, while the current 9B checkpoint and the v3 line ship T=1.0 unfitted, so thresholds must be retested per revision, and the suite still showed Jev better calibrated on 11 of 13 subsets before any refit.**
- The repository ships no license file as of 2026-10-20 (GitHub's API reports none, and no LICENSE exists at any conventional path), so the code and the curated data are technically all rights reserved, the v1 weights are Apache-2.0, and the newer v3 weights are CC BY-NC 4.0, so commercial reuse stops at the first generation.
- The training coverage that binds each release differs: the original checkpoint trained on 2,048-token prompts and 26 letter codes, and while the 2026-09-24 checkpoint serves 8,192 tokens and 255 choices, the training recipe documented in the repository is still the original 2,676-example, 2,048-token run, so the widened limits are less tested than the launch configuration.
- Seven points and zero comments on HN means none of the suite's methodology has been publicly stress-tested yet; the German MASSIVE dip (3.5 points, p = 0.023) is exactly the kind of finding replication would probe.
- On the third-party JevBench board Bespoke-Nimble-9B ranked mid-pack on the v1.2 board (60.5 overall), well behind Jev (74.4) and behind SemIf's frozen-4B readout (73.1), and then fell to 18.7 on the sealed v1.4 revision, the steepest drop JevBench measured among the named replicas, which tempers the checkpoint's standing even as the benchmark suite remains this note's crown jewel.

## Pricing

Free and open where licensed: Apache-2.0 weights (the v1 checkpoint) on Hugging Face, no hosted service fee beyond Bespoke's own API pricing for v4 and v4-max, and the repo's code and data carry no license today, so treat reuse of anything but the weights as unlicensed until that changes.

## Compared to

- [Jev](../jev/index.md): 90.1% against 93.2% on the synthetic holdout and 74.8% against 76.0% macro on human labels, with Jev's calibration clearly better; choose Jev for accuracy and calibration, Nimble for local and private decisions.
- [Kev](../kev/index.md): both are Qwen3.5-based and self-evaluating; kev has the API-compatible server and delta fine-tuning, Nimble has the human-labeled suite and the curation recipe.
- [Laya](../laya/index.md): Laya is encoder-scale, multilingual, and faster per question; Nimble is a 9B decoder with a published data methodology worth stealing.

## Bottom line

**Recommended for teams whose actual product is the training data: take the contrastive curation method, then decide whether the checkpoint clears the bar for your slice.**
Not for probability thresholds carried over from before the 2026-09-22 temperature refit without retesting them, and not for anyone who needs a license-clean codebase this week.
The disagreeable claim I will defend: this note's most valuable artifact is not a model at all, it is the 1.2-point gap on 3,880 human-labeled records, which is simultaneously the best evidence for Jev and the proof that the moat the closed vendor charges for is thinner than its launch post implied.

## Changes

- 2026-09-21 - Created from the owner-prompted open-alternative scan; accepted on traction plus the in-repo human-labeled benchmark suite, with the near-zero HN footprint stated.
- 2026-09-22 - Recorded the fitted temperature (2026-09-22, same answers, shifted probabilities), the published 2,676 training and 324 holdout examples, the 8,192-token hosted prompt limit, the JevBench reading (60.5), and refreshed star and download counts; license file still absent.
- 2026-09-25 - Refreshed traction (about 1,700 stars, about 2,600 weight downloads, license file still absent) and recorded the JevBench v1.4 sealed re-scoring (Nimble 18.7, from 60.5, the steepest drop among the named replicas).
- 2026-09-29 - Refreshed traction (about 1,900 stars, 151 forks, about 3,500 weight downloads, 202 likes); license file still absent.
- 2026-10-07 - Added the bespokelabsai/nimble star history chart to the Status section.
- 2026-10-07 - Recorded the v3 generation (Bespoke-Nimble-9B-v3, created 2026-09-30, CC BY-NC 4.0 non-commercial weights, v2 the fitted-temperature checkpoint) with Bespoke's published Decision Index 0.2.1 run (56.88) and the JevBench v1.6.1 reading (v3 eleventh at 53.5, the original 9B at 21.1); refreshed stars to about 2,100, weight downloads to about 5,900, and recorded the 2026-10-05 default-branch commits.
- 2026-10-15 - The JevBench v3 rank moved from eleventh to thirty-first at the unchanged 53.5 as the open board passed 162 ranked rows; refreshed stars to about 2,200 and the pushed date to 2026-10-14.
- 2026-10-20 - Rotation re-verification, every cited URL re-fetched: recorded the third generation (Nimble-v4 9B and Nimble-v4-max 27B on Bespoke's hosted API since 2026-10-13, self-measured 2026-10-12 at 68.46 and 63.70 on the Decision Index public suite, v4-max first overall and not yet on the dashboard), the 2026-09-24 checkpoint update (8,192-token prompts, 255 choices per field, T=1.0 unfitted, the original preserved under `original-2676`), v2's Ollama packaging and v3's DI under-25B open lead per the README timeline, the per-revision temperature caution rewritten, and the v1 weights refreshed to 6,753 downloads and 242 likes (v3: 555 and 14); the board row now reads 184 ranked systems.
- 2026-10-22 - The Decision Index's edition-0.4 rebuild (226 configurations, the Full score now entirely private) put a Bespoke Nimble v4 Max row on the board at seventeenth (66.56), moved v3 to 51.06 (seventy-ninth, from 56.88 on the 0.2.1 suite) and v2 to 42.06 (112th), and retired the "not yet on the dashboard" qualifier.
- 2026-10-24 - The 0.4.1 board's same-day regeneration (229 configurations) left v4 Max seventeenth at its unchanged 66.56 while crowd-shifts moved v3 from seventy-ninth to eightieth and v2 from 112th to 114th at unchanged scores; pushed date moved to 2026-10-24 (branch activity, no default-branch commit).

## See also

- [Jev](../jev/index.md) - the closed model the suite measures head-to-head on human labels
- [Kev](../kev/index.md) - the other Qwen3.5-based replica, API-compatible with TypeSafe's SDK
- [Laya](../laya/index.md) - the multilingual open-weights family from the same wave
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where the planner that pairs with a decision layer gets chosen

## References

- https://github.com/bespokelabsai/nimble - repository: created 2026-09-18, about 2,200 stars, 165 forks, no license file, pushed 2026-10-24 (GitHub API, as of 2026-10-24)
- https://raw.githubusercontent.com/bespokelabsai/nimble/main/README.md - capabilities, contrastive curation, the 90.1% versus 93.2% holdout, the timeline (v2 into Ollama, v3's DI under-25B open lead, v4 and v4-max on the hosted API with their self-measured suite scores), the per-revision temperature story, and the latency table (re-fetched 2026-10-20)
- https://raw.githubusercontent.com/bespokelabsai/nimble/main/docs/PUBLIC_BENCHMARKS.md - the 13-subset human-labeled suite and its full results, caveats, and rejected-datasets list
- https://huggingface.co/bespokelabs/Bespoke-Nimble-9B - weights: Apache-2.0, created 2026-09-18, 6,753 downloads, 242 likes (as of 2026-10-20)
- https://huggingface.co/bespokelabs/Bespoke-Nimble-9B-v3 - the v3 checkpoint: CC BY-NC 4.0, created 2026-09-30, 555 downloads, carrying Decision Index 0.2.1: 56.88 (as of 2026-10-20)
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/RESULTS-v1.2.md - the third-party board that ranks Bespoke-Nimble-9B 60.5 against Jev's 74.4
- https://sanand0.github.io/llmevals/jev/ - the prior independent Jev measurement (77 BANKING77 requests) the suite names as its only predecessor
- https://news.ycombinator.com/item?id=49757009 - the 7-point, zero-comment submission grounding the missing-footprint claim
- https://huggingface.co/spaces/multimodalart/jev-decision-index/resolve/main/data/v03.json - the Decision Index 0.4.1 rows for the Bespoke family: Nimble v4 Max seventeenth at 66.56, 9B v3 eightieth at 51.06, 9B v2 114th at 42.06 (generated 2026-10-22, fetched 2026-10-24)
- https://bespokelabs.ai - the lab behind the project
