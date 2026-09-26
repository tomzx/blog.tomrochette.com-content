---
title: CUA-S1
created: 2026-09-20
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, computer-use, system-one-models, open-weights]
readability: 3
audience_notes: >
  Engineers who read the Jev launch and wondered whether the no-text-generation decision-model idea has an open-weights counterpart.
  Assumes you know what a classification head and calibrated probabilities are.
---

CUA-S1 is Cua's research family of small, specialist "System One" models for computer use, and its first checkpoint, cua-s1-forms, is a 706,048-parameter open-weights scorer that assigns one probability to fill, check, click, or skip for each form element without generating any text.

**This is the first open-weights take on the decision-model contract TypeSafe's Jev launched with: the same no-text-generation input/output deal, but 2.8 MB, MIT-licensed, and trained in public on synthetic forms data, which makes the category's core question, who can verify the numbers, suddenly answerable.**

## What it is

The model is a byte-level embedding plus a two-layer Transformer encoder (width 128, four heads) that scores each interface element independently: every candidate option (fill with one extracted document entity, check, click, skip) attends against the context tokens and softmaxes into one probability per option, in a single forward pass.
The option-attention head is lifted from the community jevlike project, the checkpoint metadata names a source file `jevform-best.pt`, and the Hugging Face README calls it "jev-like", so the lineage is explicit rather than implied.
Plain code, not the model, extracts `Label: value` entities, orders the chosen actions, and hands them to the Cua Driver for execution; planning stays with whatever general LLM you already run.
It lives inside the trycua/cua monorepo (MIT) as a source component, with weights published separately on Hugging Face under MIT.

## Status

Early research artifact, days old, and unusually candid about it.
The component README still describes a source-only release whose checkpoint table reads "weights not distributed", while the main README and the checkpoint metadata point at the `cua-ai/cua-s1-forms` weights created on Hugging Face on 2026-09-18, a documentation wrinkle worth knowing before you cite either.
The launch Show HN thread (2026-09-19) reached 94 points as of 2026-09-26, and the host repository shows about 26,500 stars as of 2026-09-26, though nearly all of that is the surrounding Cua computer-use project, created 2025-01-31, not the model.
The original headline numbers remain vendor-run and synthetic-only: 99.94% top-1 on a held-out 22,054-example synthetic split, ECE 0.000148, and 2,589 rows per second, all from the checkpoint's own metadata.
The Hugging Face model card was materially expanded on 2026-09-21: the checkpoint now ships as a safetensors pair (the loader rejects pickled files by design), a first real-world demo eval landed (100% top-1 over 196 decisions on three real forms and three real PDFs, plus a 37% shuffled-context control), and a zero-fine-tuning head-to-head against the hosted Jev API scored 99.7% for this model against 83.6% for Jev, with the card conceding Jev was never trained on this project's no-op labeling convention.
The first independent artifacts appeared the following days: three community quantizations on Hugging Face and a browser-demo Space built on the checkpoint, with card likes at 111 as of 2026-09-26.

## Strengths

- **The guarantee is architectural: with no token-by-token generation, a malformed action or a refusal string is not a failure mode, which is the same property Jev sells, now inspectable.**
- Open weights at 2.8 MB make the whole thing reproducible on a laptop: architecture, synthetic data generator, training code, and evaluation metrics ship in the same repository.
- Calibration is a first-class output (the checkpoint reports ECE, and the runtime separates accuracy, abstention, and wrong-action metrics), which is what threshold-based auto-accept logic needs.
- The safety boundary is designed rather than bolted on: dry-run by default, snapshot-bound element tokens, submission restricted to a single exactly-labeled Submit button, and PDF reads confined to configured roots.

## Cautions

- **The performance evidence is still vendor-run: synthetic-only at launch, now extended with a 196-decision real eval and a Jev head-to-head published on the model card itself, but no independent party has re-run any of it, and the model card still warns that specialist models overfit their evaluation distribution.**
- Scope is one profile, form filling over `Label: value` documents, on a 706k-parameter model: it is a research checkpoint, not a computer-use agent, and there is no evidence yet of transfer to real interface variation.
- The Show HN thread's sharpest question, whether the Jev nod implies RLCD training, went unanswered, and "System One" is by the project's own admission an engineering analogy, not an architecture class.
- Hugging Face does not track downloads for the checkpoint and the API surface is days old, with the model card reserving the right to license future checkpoints separately for commercial production use.

## Pricing

Free and open where it exists today: MIT-licensed source code and MIT-licensed weights on Hugging Face, with no hosted service or paid tier.
The model card reserves the right to attach artifact-specific terms, including separate commercial licensing, to future checkpoints.

## Compared to

- [Jev](../jev/index.md): the closed, hosted, frontier-class version of the same contract with no public weights and no third-party verification; CUA-S1 is the toy-scale open bracket on the same idea, and together they frame the category's open-closed axis.
- [Outlines](../outlines/index.md): constrained decoding guarantees schema-valid text from a general model you serve; CUA-S1 instead removes text generation for one narrow decision class, at the cost of generality.
- [Instructor](../instructor/index.md): still the right layer when the decision needs semantic judgment or business rules an option scorer cannot express.

## Bottom line

**Recommended for computer-use and form-automation researchers who want to inspect, retrain, or benchmark a real decision-model checkpoint instead of trusting a launch post.**
Not for production form automation today: synthetic-only validation and a 706k-parameter scope make this a research artifact, not a dependency.
The disagreeable claim I will defend: a 706k-parameter model trained in public on synthetic data answers the "can't hallucinate" question more usefully than Jev's 1,981-point thread did, because everything here can be checked by anyone, and the category's winners will be decided by verifiability, not launch-day points.

## Changes

- 2026-09-20 - Created from the entrant scan after the 2026-09-19 Show HN launch.
- 2026-09-21 - Recorded the expanded Hugging Face model card: safetensors checkpoint format, a first real-world eval (196 decisions, 100% top-1, 37% shuffled-context control), and a head-to-head against hosted Jev (99.7% versus 83.6%); refreshed thread (89 points) and repository (about 25,300 stars) counts.
- 2026-09-22 - Recorded the first independent artifacts (three community quantizations and a browser-demo Space), and refreshed thread (92 points), repository (about 26,000 stars), and card (107 likes) counts.

## See also

- [Jev](../jev/index.md) - the closed System One model whose decision contract this open-weights checkpoint mirrors
- [Outlines](../outlines/index.md) - the self-hosted constrained-decoding path to output guarantees
- [Instructor](../instructor/index.md) - the validate-and-retry layer for decisions that still need generated text
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where the planning model that pairs with a decision model gets chosen

## References

- https://github.com/trycua/cua - host repository: 26,483 stars, MIT, created 2025-01-31, CUA-S1 announced in the main README (GitHub API, as of 2026-09-26)
- https://github.com/trycua/cua/tree/main/libs/cua-s1 - component README: source-only framing, checkpoint table, safety boundary, MCP server caveats
- https://github.com/trycua/cua/blob/main/libs/cua-s1/MODEL_CARD.md - model card: tinyx byte-level encoder, option-attention head, synthetic-only evaluation, licensing caveat
- https://huggingface.co/cua-ai/cua-s1-forms - weights: MIT, created 2026-09-18, 706,048 parameters, 111 likes as of 2026-09-26, downloads not tracked, now shipping a safetensors pair alongside the original pickle
- https://huggingface.co/cua-ai/cua-s1-forms/raw/main/cua-s1-forms.json - checkpoint config and best-validation metrics (top1 0.9994, ECE 0.000148, 2,589 rows/s, source checkpoint jevform-best.pt)
- https://news.ycombinator.com/item?id=49767564 - the Show HN thread (94 points as of 2026-09-26, 5 top-level comments, 2026-09-19), including the unanswered RLCD question
- https://github.com/trycua/cua/blob/main/libs/cua-s1/SECURITY.md - deployment threat model and least-privilege guidance
