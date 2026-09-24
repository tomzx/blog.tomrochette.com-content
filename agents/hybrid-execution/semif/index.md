---
title: SemIf
created: 2026-09-21
updated: 2026-09-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-source, webgpu]
readability: 3
audience_notes: >
  Engineers who read the Jev note and want the strongest open answer using models they already have: what frozen open models give you for typed decisions, what the project admits it did not reproduce, and why it renamed itself away from OpenJev.
  Assumes you know what logit readout and balanced accuracy are, and ideally have read this category's Jev note.
---

SemIf, until 2026-09-18 called OpenJev, is an MIT research project that reproduces Jev's interface pattern with open models: it reads typed option probabilities directly from the logits of frozen checkpoints such as Qwen3.5-4B, with no answer tokens, in a browser demo you can run today.
Facts below verified as of 2026-09-22.

**SemIf is the most verifiable entry in this category, and its own results document says the part no vendor will: the interface is reproduced, the calibrated probabilities are not, and that is the gap that matters.**

## What it is

An MIT repository by TheoLeeCJ (2,680 stars as of 2026-09-21) plus a WebGPU site at openjev.com whose tagline, "Wow! No waitlist", aims directly at Jev's early-access queue.
The method needs no training: runtime criteria and typed options go into a frozen open model (Qwen3 0.6B, MiniCPM5 2B, or Qwen3.5 4B), one forward pass per question reads the declared option logits, and a shared state is prefilled once, then branched across many criteria in parallel.
Every output row carries timing, the exact model revision, and a prompt hash, and the fixtures, runners, and raw results are committed to the repository.
An Apple Silicon MLX backend landed as a community PR on 2026-09-19, and the browser demo runs the same comparison entirely client-side with weights cached in the browser.
The rename is part of the artifact: after its launch thread debated trademark risk, the project added an independence disclaimer ("not affiliated with or endorsed by TypeSafe") in commits dated 2026-09-18, and the old `TheoLeeCJ/openjev` URL now redirects here.

## Status

Days old and active, as of 2026-09-22.
Created 2026-09-16, last push 2026-09-21, two contributors, no tags or releases, 257 forks, about 3,900 stars.
The community footprint is large but lives under the old name: the "OpenJev" thread linking openjev.com reached 720 points as of 2026-09-22, the second-largest thread in the Jev wave after Jev's own launch.
Three community PRs merged on 2026-09-22: PyTorch/MPS scoring for Apple Silicon, a Qwen3.8-27B EXL3 bridge, and per-workload temperature calibration with calibrated prediction outputs.
The headline numbers are self-run: on 102 aligned public rows, direct logit readout with Qwen3.5-4B agrees with TypeSafe's published values 0.845 of the time against Jev's published 0.883, with balanced accuracy of 0.813 on authored decisions and 0.766 under perturbation.
The first third-party scoreboard of the category now exists and ranks SemIf (Qwen3.5-4B) second overall at 73.1 against Jev's 74.4, the wave's strongest independent showing, on a methodology contested in that benchmark's own thread.

## Strengths

- **The speed evidence is measured, committed, and reproducible: 21 criteria in a 1.023-second median direct readout versus 5.332 seconds for a compact generated JSON array on one RTX 3090, zero output tokens, with raw runs checked in.**
- Shared-state reuse is quantified: parallel suffix execution reaches 20.03 decisions per second over a 777-decision workload, with the argmax drift from batching (5-6 of 777) disclosed rather than hidden.
- The claim boundaries are explicit and rare in this category: RESULTS.md lists what was not reproduced (Jev's architecture, RLCD training, calibrated probabilities, the 711-row benchmark), gives distribution-distance numbers (0.177 total-variation versus Jev's published 0.127), and concedes the comparison subset is small and selected.
- The browser demo is genuinely local: no backend, inputs never leave the page, and three model tiers from 639 MB to 3.01 GB, which makes the interface independently experienceable in a way no closed vendor allows.

## Cautions

- **The rename is the cautionary tale for this whole wave: the launch thread's own commenters flagged "Jev" naming as confusing and legally dangerous, and the project capitulated with a disclaimer within a day, so every clone is one letter away from the same problem.**
- Thread skeptics read the project as evidence about classifiers, not a breakthrough: one called the moment "mostly harness hype" around capabilities GLiNER2-style models and small local classifiers already served, and another posted a live failure where the model answered wrongly at 80% confidence.
- The probabilities shipped explicitly not calibrated, and RESULTS.md still states the core scores "cannot be treated as Jev-like operational calibration"; the 2026-09-22 per-workload temperature-calibration PR adds a calibration layer, but it is community work layered after the fact, not the RLCD-trained calibration the category actually wants, and option-order flips remain unsolved (10 flips on the reversal variant).
- Every number is self-run on owned or small public workloads, Jev was never run live by the project, and no third party has replicated any of it.

## Pricing

Free and open: MIT-licensed code, no hosted service, no paid tier, and the models are third-party open weights you serve yourself.
The cost is your GPU, a 0.6-4B model download, and the engineering to keep the shared-state paths warm.

## Compared to

- [Jev](../jev/index.md): the closed original; SemIf's own table puts open 4B at 0.845 versus 0.883 agreement on the aligned subset, which is close on choices while probability quality stays behind.
- [Laya](../laya/index.md): the trained-checkpoint answer; Laya specializes small models for the decision layer and wins on latency and languages, SemIf refuses to train in phase one and measures what frozen general models already give you.
- [Jevlike](../jevlike/index.md): the from-scratch tiny-scorer answer; SemIf's bet is the opposite, that runtime-defined criteria over models you already run beats any task-trained head.
- [CUA-S1](../cua-s1/index.md): the narrow specialist; choose it for form-filling scoring, SemIf for general runtime-defined decisions.

## Bottom line

**Recommended for engineers who want Jev-style decisions running locally today and will wrap the probabilities behind their own validation and thresholds.**
Not for consequential automated decisions, and not for anyone who needs a vendor or a calibration guarantee.
The disagreeable claim I will defend: the 3.8-point agreement gap on a selected 102-row subset is too weak to call "almost Jev at home", and the number that actually separates them is distribution distance, where Jev's published outputs are meaningfully tighter; what SemIf really proves is that the interface costs almost nothing to copy, which is a different and quieter result.
I run the browser demo before I believe any latency claim in this category, and this is the only project in it that lets me.

## Changes

- 2026-09-21 - Created from the owner-prompted open-source alternatives sub-run.
- 2026-09-22 - Recorded the 2026-09-22 community PRs (MPS scoring, a Qwen3.8-27B EXL3 bridge, per-workload temperature calibration), the third-party JevBench reading (SemIf second at 73.1 versus Jev's 74.4), and refreshed star (about 3,900), fork (257), and thread (720 points) counts.

## See also

- [Jev](../jev/index.md) - the closed service whose interface pattern SemIf reproduces and whose trademark forced the rename
- [Laya](../laya/index.md) - the open-weights, trained-checkpoint rival answer to the same contract
- [Jevlike](../jevlike/index.md) - the from-scratch community starter SemIf explicitly does not follow
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where the frozen open model you point at this contract gets chosen

## References

- https://github.com/TheoLeeCJ/SemIf - repository: MIT, about 3,900 stars, 257 forks, created 2026-09-16, last push 2026-09-21 (GitHub API, as of 2026-09-22)
- https://raw.githubusercontent.com/TheoLeeCJ/SemIf/master/README.md - the rename notice, speed tables, browser model ladder, MLX backend, and the 2026-09-22 PR log
- https://openjev.com/ - the project site: WebGPU demo, quality table, and the independence notice
- https://news.ycombinator.com/item?id=49752041 - the OpenJev thread (720 points as of 2026-09-22, 2026-09-18): the trademark debate, the hype and failure criticisms (fetched via the Algolia items API)
- https://raw.githubusercontent.com/TheoLeeCJ/SemIf/master/docs/RESULTS.md - claim boundaries: what was and was not reproduced, TVD numbers, robustness flips
- https://github.com/TheoLeeCJ/openjev - the pre-rename URL, verified to redirect to this repository (GitHub API)
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/RESULTS-v1.2.md - the third-party board ranking SemIf second at 73.1 against Jev's 74.4
