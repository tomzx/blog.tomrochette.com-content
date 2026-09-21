---
title: Jevlike
created: 2026-09-21
updated: 2026-09-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models, open-weights]
readability: 3
audience_notes: >
  Engineers who read the Jev note and want to see what the community's one-day reverse-engineering actually is: how a one-pass option scorer is built, what its demos prove and do not, and what it costs to train your own.
  Assumes you know what attention and a softmax over options are, and ideally have read this category's Jev note.
---

Jevlike is the community's one-day reverse-engineering of the Jev decision contract: an MIT Python starter that trains a small model to return one probability per text option in a single forward pass, with no text generation anywhere.
Facts below verified as of 2026-09-21.

**Jevlike matters less as a model than as evidence about the category: the Jev interface was copied in hours by one person with AI coding tools, so the moat, if TypeSafe has one, cannot be the interface.**

## What it is

An MIT repository by vinnylarouge, three commits all on 2026-09-16, whose trailers credit OpenAI Codex and Claude Fable 5.1 as co-authors, which makes the launch thread's "building in stealth for 2 hours" joke close to literal.
The mechanism is one option-attention head: each option becomes a query vector that attends over the context tokens, a shared dot product scores every option-context pair, and a softmax across options yields one probability per option in a single pass.
The default encoder learns byte embeddings from scratch (192 bytes of context, 32 per option by default), with an optional frozen Hugging Face encoder such as Qwen2.5-0.5B behind a small trained scorer head.
Training data is one JSON object per line (context, N options, correct index), and the CLI ships data generation, training, and an eval that prints top-1, top-3, expected calibration error, and a shuffled-context control.
A vision variant reuses the same head to score controller buttons from image patches: one 12-option table covering seven Doom buttons and five chess keys, with checkpoints checked into the repository.

## Status

Dormant since launch day by every number I can check, as of 2026-09-21.
Created and last pushed 2026-09-16, 1,122 stars and 98 forks, five open issues, a single contributor, and no tags or releases to pin.
The Show HN thread ("Reverse-engineered Jev-like model", 2026-09-16) reached 166 points as of 2026-09-21.
The afterlife is elsewhere: Cua's CUA-S1 form-filling checkpoint documents that its option-attention head is lifted from jevlike's `AttentionHead`, so the code's real legacy is inside other projects rather than in this one.

## Strengths

- **The eval discipline is the right discipline for this category: calibration error and a shuffled-context control are printed by default, and the data guide warns about near-duplicate leakage across splits.**
- The expectations section is unusually self-critical: about 98% on synthetic menus, but only 26-29% on target-disjoint Wikispeedia next-click against roughly 8% for shuffled and random-encoder controls, followed by the plain admission "We did not show equal quality with Jev or reproduce TypeSafe's private training method."
- The demos disclose their own weakness: the chess checkpoint wins 4-0-46-0 against a random mover and loses 0-2-48 to Stockfish level 0, with the film's windows flagged as "selected for activity and not typical-play or competence claims."
- In the launch thread, a commenter credited the three-sentence README with explaining Jev better than TypeSafe's own announcement, which is a real documentation contribution.

## Cautions

- **The Doom film drew the thread's sharpest fire: one commenter called the side-by-side "a satire at best" because the two panels' results visibly differ, and another noted they "almost never agree on anything", so the demo argues speed, not correctness.**
- It is a starter, not a reproduction: the shipped game checkpoints are early ones, and nothing here claims Jev-level quality, only the same input-output deal.
- Effectively frozen: one day of commits, then silence, five open issues, no releases, so anyone building on it inherits an unmaintained tree.
- The 192-byte default context is tiny against Jev's advertised long-state budget; you can raise it, but the training recipes shown were not demonstrated at longer states.

## Pricing

Free and open: MIT-licensed code and in-repository checkpoints, no hosted service, no paid tier.
The cost is your own training run and whatever encoder you freeze behind the head.

## Compared to

- [Jev](../jev/index.md): the closed, hosted original with frontier-class claims and no third-party verification; jevlike is the inspectable but weaker bracket on the same contract.
- [Laya](../laya/index.md): the open-weights effort that kept compounding after launch day (trained checkpoints, a router, multilingual coverage); choose Laya for a working open decision model, jevlike to understand or train a minimal one.
- [CUA-S1](../cua-s1/index.md): the downstream project that lifted this repo's AttentionHead into form filling, which is the strongest evidence that the starter's value was architectural.

## Bottom line

**Recommended for engineers who want to read or train a minimal one-pass option scorer, and for anyone teaching themselves why this contract is cheap; not for production decisions.**
The disagreeable claim I will defend: jevlike's one-day existence refutes more of Jev's mystique than any benchmark could, because if the interface is trivial to copy, then everything that matters is data and calibration, which is exactly the part no clone has shown.
I would not route a real decision through this repo today, but I would make every Jev skeptic read its README.

## Changes

- 2026-09-21 - Created from the owner-prompted open-source alternatives sub-run.

## See also

- [Jev](../jev/index.md) - the closed System One model this project reverse-engineered a day after launch
- [CUA-S1](../cua-s1/index.md) - the open checkpoint that lifted jevlike's AttentionHead into form filling
- [Laya](../laya/index.md) - the open-weights rival that kept compounding where jevlike went quiet
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where the text-generating model above a decision layer gets chosen

## References

- https://github.com/vinnylarouge/jevlike - repository: MIT, 1,122 stars, 98 forks, created and last pushed 2026-09-16 (GitHub API, as of 2026-09-21)
- https://raw.githubusercontent.com/vinnylarouge/jevlike/main/README.md - the option-attention architecture, data format, eval design, and the expectations section with the no-equal-quality admission
- https://news.ycombinator.com/item?id=49731282 - the 166-point launch thread (2026-09-16), including the satire and panel-disagreement criticisms (fetched via the Algolia items API)
- https://raw.githubusercontent.com/vinnylarouge/jevlike/main/examples/doom/README.md - the vision variant: 12-option table, DAgger-before-PPO training order, early-checkpoint caveat
- https://huggingface.co/cua-ai/cua-s1-forms - downstream adoption: its README credits "jevlike's `AttentionHead`" as the lifted component
