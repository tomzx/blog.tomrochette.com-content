---
title: AnyJev
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, decision-models, training-free]
readability: 3
audience_notes: >
  Engineers who want typed, calibrated decisions from models they already run, without training one.
  Assumes you know what the Jev-style typed-decision contract is in this category.
---

AnyJev is Nokia Applied Research's Apache-2.0 method that turns any instruction-tuned LLM into a Jev-style decision model: it reads a typed choice as probabilities straight from the logits, then corrects the two biases that readout suffers, no gradient steps and no generated text.

**AnyJev is the training-free entry in the decision-model wave, and its arXiv-backed claim inverts the family's economics: instead of paying for a fine-tune or a specialist checkpoint, you pay a few extra prefills per decision, spent only where a stopping rule says the calibration needs them.**

## What it is

A pip-installable Python method plus a paper (arXiv 2610.00831, submitted 2026-09-30, authors from Nokia, Tencent Hunyuan, and Hong Kong Polytechnic University) from nokia-applied-research (1,092 stars, pushed 2026-10-07, as of 2026-10-07).
The raw readout restricts the next-token distribution at the answer position to the option tokens; AnyJev then corrects its two documented defects by dividing out a label prior estimated from unlabelled inputs and averaging log-probabilities over the K cyclic rotations of the option list, which lowers the order-flip rate from 0.33 to 0.14 and 0.18 on two 20-option tasks and raises accuracy on 11 of 11 models tested.
A stopping rule selected on unlabelled splits cuts the rotation count: 10.6 of 18 rotations at a verified 0.008 disagreement bound on two of four cells, or 7.3 when selected on one split, which served 2.2 times as many decisions per second on vLLM.
The same team publishes Tacit, a self-distilled 1.7B-to-9B model line on Hugging Face that compresses the method to one forward pass per decision, with an adaptive mode routing a capped share of low-confidence decisions back to the base model's reasoning.

## Status

Active and freshly credible: created 2026-09-21, 1,092 stars, release v0.3.0 published 2026-10-07, as of 2026-10-07.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=nokia-applied-research/AnyJev&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=nokia-applied-research/AnyJev&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=nokia-applied-research/AnyJev&type=date&legend=top-left" />
</picture>

This note reverses this section's 2026-09-25 rejection of the same project, which then had 506 stars and no independent coverage; the promised re-review trigger, a second implementation, now exists in kind.
The third-party local-jev-bench benchmark (2026-09-30, updated 2026-10-05) runs AnyJev against Kev, Winnow, Clef, Von, Jeff, Laya, and CLM on Apple Silicon and reports training-free AnyJev level with the trained engines on the six public transfer sources; community builds such as mesa-anyjev and a Tetris-playing AnyJev judge extend it.
The HN footprint remains thin (mentions inside decision-model threads, no thread of its own), which this note records as the standing signal.

## Strengths

- No training: any instruction-tuned model you already serve becomes a decision engine, which removes the fine-tune cost and the frozen-weights staleness the rest of the wave accepts.
- The corrections are principled and measured, with the rotation-averaging and prior-division effects reported across 11 of 11 models and the early-exit bound verified rather than asserted.
- The calibration pipeline (thresholds selected and bounded on unlabelled splits) addresses the abstention question most replicas leave open.
- Apache-2.0 code, a peer-readable technical report, and PyPI packaging make it the wave's most reproducible-looking method entry.

## Cautions

- Rotation reads cost prefills: the fair cost comparison is against trained single-pass models, and the stopping-rule numbers are per-cell, not a universal 7.3.
- Independent benchmark coverage exists (local-jev-bench) but is one hobbyist-scale suite; no lab replication yet, as of 2026-10-07.
- The project is three weeks old, so API stability and the Tacit line's licenses are early-grade.
- The vendor is a telecom research lab, and the wave has already seen research artifacts go quiet after launch; the community builds are promising but 0-star so far.

## Pricing

Free and open source under Apache-2.0; the Tacit checkpoints are published on Hugging Face, so pricing does not apply.
Costs are your own model serving and the extra prefills the rotations or early-exit read.

## Compared to

- [Jev](../jev/index.md): the closed contract that defined the category, single-pass and priced per million tokens; AnyJev is the open, bring-your-own-model alternative with prefill-based costs.
- [Kev](../kev/index.md): the strongest open trained family; choose AnyJev to avoid training entirely, Kev when a single-pass fine-tune beats multi-prefill reads on your latency budget.
- [SemIf](../semif/index.md): the other logit-readout entrant over frozen models, without AnyJev's bias corrections or stopping rule.

## Bottom line

**Recommended for teams already serving an instruction-tuned model who need typed, calibrated decisions and cannot justify training or a specialist checkpoint, starting with the early-exit configuration and validating calibration on your own label splits.**
Not for single-digit-millisecond budgets, where the trained single-pass models keep the edge, and not for production trust before an independent lab replicates the paper's bounds.

## Changes

- 2026-10-07 - Created.

## See also

- [Jev](../jev/index.md) - the closed contract AnyJev replicates without training
- [Kev](../kev/index.md) - the trained open alternative with the strongest eval discipline
- [SemIf](../semif/index.md) - the frozen-model logit readout without the bias corrections
- [Ollaya](../ollaya/index.md) - the runtime that could serve a Tacit checkpoint beside the trained families
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/nokia-applied-research/AnyJev - repository, Apache-2.0 license, the readout and correction design, and the Tacit line (fetched 200, 2026-10-07)
- https://api.github.com/repos/nokia-applied-research/AnyJev - stars, forks, created date, and push date for the as-of status (fetched 200, 2026-10-07)
- https://arxiv.org/abs/2610.00831 - the technical report: rotation-averaging and prior-division results, the early-exit bounds, and the vLLM serving numbers (fetched 200, 2026-10-07)
- https://api.github.com/repos/nokia-applied-research/AnyJev/releases - the v0.0.2 through v0.3.0 releases, v0.3.0 on 2026-10-07 (fetched 200, 2026-10-07)
- https://raw.githubusercontent.com/tak-bro/local-jev-bench/HEAD/README.md - the third-party Apple Silicon benchmark running AnyJev against Kev, Winnow, Clef, Von, Jeff, Laya, and CLM (fetched 200, 2026-10-07)
- https://huggingface.co/collections/morriszjm/tacit-6ac41d0b50af9e5417c5c234 - the Tacit collection: five checkpoints (1.7B to 9B) self-distilled on Qwen bases, one forward pass per decision (fetched 200, 2026-10-07)
- https://github.com/idss-mesa/mesa-anyjev - a second implementation of the method, calibrated ontology and schema decisions for the MESA stack, part of the re-review evidence (fetched 200, 2026-10-07)
