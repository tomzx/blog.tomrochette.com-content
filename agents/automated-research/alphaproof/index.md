---
title: AlphaProof
created: 2026-09-13
updated: 2026-09-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, deepmind, mathematics, formal-verification]
readability: 3
audience_notes: >
  Engineers tracking how far automated mathematical research has come and what its verification loop looks like.
  Assumes you know what a proof assistant and reinforcement learning are.
---

AlphaProof is Google DeepMind's reinforcement-learning system for proving mathematical statements in Lean, and its lineage now runs from an IMO silver medal in 2024 to an officially graded IMO gold medal in 2025 through Gemini Deep Think.
Facts below verified as of 2026-09-18.

**The arc is the clearest public evidence that verified-reasoning loops scale: the 2024 result needed manual Lean translation and up to three days of compute, while the 2025 result ran end to end in natural language inside the 4.5-hour contest clock.**

## What it is

AlphaProof couples a pre-trained Gemini-based language model with the AlphaZero reinforcement-learning algorithm over Lean proofs.
A formalizer network translates natural-language problems into formal statements, the system generates candidate solutions, searches over proof steps in Lean, and every proof it verifies reinforces the model.
AlphaGeometry 2 is the neuro-symbolic geometry sibling, and both were built by Google DeepMind.
In July 2025 the flagship became an advanced version of Gemini Deep Think, a reasoning mode using parallel thinking trained with reinforcement learning on theorem-proving data plus a curated corpus of high-quality solutions.

## Status

Very much active, as a research line rather than a product.
At IMO 2024, AlphaProof plus AlphaGeometry 2 solved four of six problems for 28 of 42 points, silver-medal standard, with problems manually translated into Lean and solve times from minutes to three days, scored by Fields Medalist Timothy Gowers and Joseph Myers.
At IMO 2025, Gemini Deep Think solved five of six problems perfectly for 35 of 42 points, graded by IMO coordinators under the same criteria as student solutions, within the official time limit.
The IMO stated its review did not extend to validating the system, processes, or underlying model.
DeepMind published the AlphaProof methodology in Nature on November 12, 2025, and says it believes agents combining natural-language fluency with verified formal reasoning are the path forward.

## Strengths

- The training loop is grounded in machine-verified proofs, so reward is never a hallucinated "looks right".
- Official IMO grading in 2025 is the strongest third-party validation any system in this category has.
- Parallel thinking explores and combines multiple solution paths instead of one chain of thought.
- The 2024-to-2025 jump is documented with both systems' artifacts public.

## Cautions

- The 2024 result required humans to translate problems into Lean, and took days, so it is not a tool an engineer can run.
- The 2025 result is a closed model behind a rollout to trusted testers and Google AI Ultra subscribers, with no API for the IMO configuration.
- Mathematicians flagged caveats around what the gold-medal claims mean, and the IMO disclaimer matters.
- Competition problems are verified and bounded; no Millennium-problem claim has been made.

## Pricing

No standalone pricing.
Deep Think access ships through the Google AI Ultra subscription tier as it rolls out, and the research systems themselves are not publicly runnable.

## Compared to

- [Math Inc. Gauss](../math-inc-gauss/index.md): autoformalizes known mathematics at record scale with an auditable open harness; choose Gauss when the job is formalizing results, AlphaProof when it is solving new problems.
- [Anthropic Claude mathematical research](../anthropic-claude-math/index.md): a general model in a coding harness producing novel research results; choose the Claude loop for open-ended problems, AlphaProof for formal, verifiable competition-style targets.
- [Harmonic Aristotle](../harmonic-aristotle/index.md): a closed theorem-proving product you can actually use today; choose Aristotle when you need proofs now, AlphaProof when you need the strongest published evidence of capability.

## Bottom line

**Recommended reading for anyone designing verification-gated agent systems: this is the reference implementation of "the judge is a kernel, the worker is trained on verdicts".**
Not for practitioners who need a runnable tool today, since nothing here is self-hostable or API-accessible as of 2026-09-18.

## Changes

- 2026-09-13 - Created as the DeepMind member of the new Automated research category.

## See also

- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins
- [Math Inc. Gauss](../math-inc-gauss/index.md) - the autoformalization counterpart on the who-produces axis
- [Anthropic Claude mathematical research](../anthropic-claude-math/index.md) - the general-model rival loop
- [Evaluation and Review Feature Matrix](../../evaluation-review/evaluation-review-feature-matrix/index.md) - where "who judges" sits across the tooling ecosystem

## References

- https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/ - the 2024 silver result, Lean pipeline, scoring, and 2024-11 Nature methodology note
- https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/ - the 2025 official gold, parallel thinking, rollout, and the IMO validation disclaimer
- https://en.wikipedia.org/wiki/AlphaGeometry - AlphaGeometry and AlphaGeometry 2 lineage, Gemini-based autoformalization, and the applicability caution
- https://www.technologyreview.com/2026/01/26/1131728/inside-openais-big-play-for-science/ - independent framing of the IMO gold claims and their caveats in the landscape context
