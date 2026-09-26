---
title: Nimble
created: 2026-09-21
updated: 2026-09-25
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

A typed-decision scorer: text plus a flat schema in, one picked answer and per-candidate probabilities out, with enum fields capped at 26 single-token letter codes, a 2,048-token prompt limit, and no nested fields.
Serving runs on Apple Silicon through an MLX `ParallelScorer` that processes the shared context once, or on CUDA where each field is scored against the full prompt; observed medians are 106 ms per example on an H100 and 444 ms on an M5 Pro, against Jev's 247 ms through its API on the same holdout.
Training used 2,676 examples built by the project's own contrastive data curation (near-identical pairs differing in one fact that flips the label), LoRA rank 16, one epoch, and the README states no Jev outputs were distilled.
The authors are Bespoke Labs with Maheswaran Sathiamoorthy, whose earlier Bespoke-MiniCheck work with Greg Durett and Liyan Tang the acknowledgments credit as the foundation.

## Status

**Active and seven days old, with a near-zero HN footprint and the strongest verification artifacts of any project in the wave.**
The repository was created 2026-09-18 and pushed 2026-09-24, with about 1,700 stars and 131 forks as of 2026-09-25; the weights were created 2026-09-18 and show about 2,600 downloads and 187 likes.
The Hacker News submission (2026-09-18) sits at 7 points and zero comments, so I state plainly that the community footprint is absent.
What substitutes is in the repo: a 13-subset, 3,880-record human-labeled suite (VitaminC, MASSIVE in English and German, BoolQ, SQuAD 2.0, PAWS, MultiNLI, Civil Comments, Aegis 2, HelpSteer2, two SummEval slices, PubMedQA) run against Jev 1.13.0, which no vendor and no other replica has done.
The project has kept shipping: the 2,676 training examples and the 324-example holdout were published on 2026-09-20 (they had been left out of the first release by mistake), the hosted deployment's prompt limit rose to 8,192 tokens on 2026-09-19, and on 2026-09-22 a temperature was fitted for the checkpoint (same picked answers, better-matching probabilities).

## Strengths

- **The external evidence nobody else has: on human labels Jev macros 76.0% against Nimble's 74.8%, Jev takes the boolean tasks, Nimble takes the rubric-rating tasks, and Jev has the lower calibration error on 11 of 13 subsets; these 3,880 records are the fairest public yardstick this category has.**
- Contrastive data curation is a transferable recipe: one-fact-flips-the-label pairs, model-checked with replayable requests, published with checksums and an offline dataset verifier.
- The self-criticism is unusual for the genre: the README concedes the holdout is 324 synthetic examples from six source families, that no temperature was fitted, that contamination is plausible, and that position bias is unmeasured.
- It runs locally on a Mac with no TypeSafe key, and a contract file pins the base revision and a prompt-code hash against the scorer.

## Cautions

- **The probabilities now ship with a fitted temperature (2026-09-22): the picked answers are unchanged, noul probabilities and score values shift, so thresholds must be retested, and the suite still showed Jev better calibrated on 11 of 13 subsets before the refit.**
- The repository ships no license file as of 2026-09-25 (GitHub's API reports none, and no LICENSE exists at any conventional path), so the code and the curated data are technically all rights reserved even though the weights are Apache-2.0.
- The training coverage remains the binding limit: the model was trained on prompts of up to 2,048 tokens (the hosted limit is now 8,192, so longer prompts are less tested), enum fields cap at 26 single-token letter codes, and the checkpoint is one day of work across ten subject categories against Jev's advertised 32k-plus context.
- Six points and zero comments on HN means none of the suite's methodology has been publicly stress-tested yet; the German MASSIVE dip (3.5 points, p = 0.023) is exactly the kind of finding replication would probe.
- On the third-party JevBench board Bespoke-Nimble-9B ranked mid-pack on the v1.2 board (60.5 overall), well behind Jev (74.4) and behind SemIf's frozen-4B readout (73.1), and then fell to 18.7 on the sealed v1.4 revision, the steepest drop JevBench measured among the named replicas, which tempers the checkpoint's standing even as the benchmark suite remains this note's crown jewel.

## Pricing

Free and open where licensed: Apache-2.0 weights on Hugging Face, no hosted service and no paid tier.
The repo's code and data carry no license today, so treat reuse of anything but the weights as unlicensed until that changes.

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

## See also

- [Jev](../jev/index.md) - the closed model the suite measures head-to-head on human labels
- [Kev](../kev/index.md) - the other Qwen3.5-based replica, API-compatible with TypeSafe's SDK
- [Laya](../laya/index.md) - the multilingual open-weights family from the same wave
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where the planner that pairs with a decision layer gets chosen

## References

- https://github.com/bespokelabsai/nimble - repository: created 2026-09-18, about 1,700 stars, 131 forks, no license file (GitHub API and contents listing, as of 2026-09-25)
- https://raw.githubusercontent.com/bespokelabsai/nimble/main/README.md - capabilities, contrastive curation, the 90.1% versus 93.2% holdout, the updates log (temperature, dataset release, prompt limit), and the latency table
- https://raw.githubusercontent.com/bespokelabsai/nimble/main/docs/PUBLIC_BENCHMARKS.md - the 13-subset human-labeled suite and its full results, caveats, and rejected-datasets list
- https://huggingface.co/bespokelabs/Bespoke-Nimble-9B - weights: Apache-2.0, created 2026-09-18, about 2,600 downloads, 187 likes (as of 2026-09-25)
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/RESULTS-v1.2.md - the third-party board that ranks Bespoke-Nimble-9B 60.5 against Jev's 74.4
- https://sanand0.github.io/llmevals/jev/ - the prior independent Jev measurement (77 BANKING77 requests) the suite names as its only predecessor
- https://news.ycombinator.com/item?id=49757009 - the 6-point, zero-comment submission grounding the missing-footprint claim
- https://bespokelabs.ai - the lab behind the project
