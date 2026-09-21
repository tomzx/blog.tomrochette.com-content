---
title: Nimble
created: 2026-09-21
updated: 2026-09-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights, data-curation, model-evaluation]
readability: 3
audience_notes: >
  Engineers deciding between Jev and an open checkpoint, who care about human-labeled evidence more than launch posts.
  Assumes you know what a LoRA fine-tune, logits, and expected calibration error are.
---

Nimble is Bespoke Labs' one-day "open Jev": Bespoke-Nimble-9B, an Apache-2.0 LoRA fine-tune of Qwen3.5-9B that reads a flat schema of enum and boolean questions off the logits with no generated JSON, published together with the data, the training recipe, and a human-labeled benchmark suite run head-to-head against Jev.
Facts below verified as of 2026-09-21.

**The checkpoint is average for the replica wave, but its benchmark suite is the only place in this category where Jev has been measured against human labels, and Jev wins by just 1.2 macro points.**

## What it is

A typed-decision scorer: text plus a flat schema in, one picked answer and per-candidate probabilities out, with enum fields capped at 26 single-token letter codes, a 2,048-token prompt limit, and no nested fields.
Serving runs on Apple Silicon through an MLX `ParallelScorer` that processes the shared context once, or on CUDA where each field is scored against the full prompt; observed medians are 106 ms per example on an H100 and 444 ms on an M5 Pro, against Jev's 247 ms through its API on the same holdout.
Training used 2,676 examples built by the project's own contrastive data curation (near-identical pairs differing in one fact that flips the label), LoRA rank 16, one epoch, and the README states no Jev outputs were distilled.
The authors are Bespoke Labs with Maheswaran Sathiamoorthy, whose earlier Bespoke-MiniCheck work with Greg Durett and Liyan Tang the acknowledgments credit as the foundation.

## Status

**Active and three days old, with a near-zero HN footprint and the strongest verification artifacts of any project in the wave.**
The repository was created 2026-09-18 and pushed 2026-09-20, with 1,311 stars and 91 forks as of 2026-09-21; the weights were created 2026-09-18 and show 382 downloads and 128 likes.
The Hacker News submission (2026-09-18) sits at 6 points and zero comments, so I state plainly that the community footprint is absent.
What substitutes is in the repo: a 13-subset, 3,880-record human-labeled suite (VitaminC, MASSIVE in English and German, BoolQ, SQuAD 2.0, PAWS, MultiNLI, Civil Comments, Aegis 2, HelpSteer2, two SummEval slices, PubMedQA) run against Jev 1.13.0, which no vendor and no other replica has done.

## Strengths

- **The external evidence nobody else has: on human labels Jev macros 76.0% against Nimble's 74.8%, Jev takes the boolean tasks, Nimble takes the rubric-rating tasks, and Jev has the lower calibration error on 11 of 13 subsets; these 3,880 records are the fairest public yardstick this category has.**
- Contrastive data curation is a transferable recipe: one-fact-flips-the-label pairs, model-checked with replayable requests, published with checksums and an offline dataset verifier.
- The self-criticism is unusual for the genre: the README concedes the holdout is 324 synthetic examples from six source families, that no temperature was fitted, that contamination is plausible, and that position bias is unmeasured.
- It runs locally on a Mac with no TypeSafe key, and a contract file pins the base revision and a prompt-code hash against the scorer.

## Cautions

- **The repository ships no license file as of 2026-09-21** (GitHub's API reports none, and no LICENSE exists at any conventional path), so the code and the curated data are technically all rights reserved even though the weights are Apache-2.0.
- The probabilities are not calibrated: the README says outright that 0.9 does not mean 90% right, no temperature has been fitted, and the suite shows Jev better calibrated almost everywhere.
- The checkpoint is one day of work across ten subject categories, with a 2,048-token cap and 26-option limit that bind far tighter than Jev's advertised 32k-plus context.
- Six points and zero comments on HN means none of the suite's methodology has been publicly stress-tested yet; the German MASSIVE dip (3.5 points, p = 0.023) is exactly the kind of finding replication would probe.

## Pricing

Free and open where licensed: Apache-2.0 weights on Hugging Face, no hosted service and no paid tier.
The repo's code and data carry no license today, so treat reuse of anything but the weights as unlicensed until that changes.

## Compared to

- [Jev](../jev/index.md): 90.1% against 93.2% on the synthetic holdout and 74.8% against 76.0% macro on human labels, with Jev's calibration clearly better; choose Jev for accuracy and calibration, Nimble for local and private decisions.
- [Kev](../kev/index.md): both are Qwen3.5-based and self-evaluating; kev has the API-compatible server and delta fine-tuning, Nimble has the human-labeled suite and the curation recipe.
- [Laya](../laya/index.md): Laya is encoder-scale, multilingual, and faster per question; Nimble is a 9B decoder with a published data methodology worth stealing.

## Bottom line

**Recommended for teams whose actual product is the training data: take the contrastive curation method, then decide whether the checkpoint clears the bar for your slice.**
Not for calibrated probability thresholds (fit a temperature or use Jev), and not for anyone who needs a license-clean codebase this week.
The disagreeable claim I will defend: this note's most valuable artifact is not a model at all, it is the 1.2-point gap on 3,880 human-labeled records, which is simultaneously the best evidence for Jev and the proof that the moat the closed vendor charges for is thinner than its launch post implied.

## Changes

- 2026-09-21 - Created from the owner-prompted open-alternative scan; accepted on traction plus the in-repo human-labeled benchmark suite, with the near-zero HN footprint stated.

## See also

- [Jev](../jev/index.md) - the closed model the suite measures head-to-head on human labels
- [Kev](../kev/index.md) - the other Qwen3.5-based replica, API-compatible with TypeSafe's SDK
- [Laya](../laya/index.md) - the multilingual open-weights family from the same wave
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where the planner that pairs with a decision layer gets chosen

## References

- https://github.com/bespokelabsai/nimble - repository: created 2026-09-18, 1,311 stars, 91 forks, no license file (GitHub API and contents listing, as of 2026-09-21)
- https://raw.githubusercontent.com/bespokelabsai/nimble/main/README.md - capabilities, contrastive curation, the 90.1% versus 93.2% holdout, and the latency table
- https://raw.githubusercontent.com/bespokelabsai/nimble/main/docs/PUBLIC_BENCHMARKS.md - the 13-subset human-labeled suite and its full results, caveats, and rejected-datasets list
- https://huggingface.co/bespokelabs/Bespoke-Nimble-9B - weights: Apache-2.0, created 2026-09-18, 382 downloads, 128 likes (as of 2026-09-21)
- https://sanand0.github.io/llmevals/jev/ - the prior independent Jev measurement (77 BANKING77 requests) the suite names as its only predecessor
- https://news.ycombinator.com/item?id=49757009 - the 6-point, zero-comment submission grounding the missing-footprint claim
- https://bespokelabs.ai - the lab behind the project
