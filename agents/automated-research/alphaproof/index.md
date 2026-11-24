---
title: AlphaProof
created: 2026-09-13
updated: 2026-11-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, automated-research, deepmind, mathematics, formal-verification]
readability: 3
audience_notes: >
  Engineers tracking how far automated mathematical research has come and what its verification loop looks like.
  Assumes you know what a proof assistant and reinforcement learning are.
---

AlphaProof is Google DeepMind's reinforcement-learning system for proving mathematical statements in Lean, and its lineage now runs from an IMO silver medal in 2024 to an officially graded IMO gold medal in 2025 through Gemini Deep Think, and, since November 2026, to AlphaProof Code, its agent framework for formally verifying software at the machine-code level.

**The arc is the clearest public evidence that verified-reasoning loops scale: the 2024 result needed manual Lean translation and up to three days of compute, while the 2025 result ran end to end in natural language inside the 4.5-hour contest clock.**

## What it is

AlphaProof couples a pre-trained Gemini-based language model with the AlphaZero reinforcement-learning algorithm over Lean proofs.
A formalizer network translates natural-language problems into formal statements, the system generates candidate solutions, searches over proof steps in Lean, and every proof it verifies reinforces the model.
AlphaGeometry 2 is the neuro-symbolic geometry sibling, and both were built by Google DeepMind.
Since November 2026 the family includes AlphaProof Code, which turns the same pattern toward software: agents write Lean specifications under human guidance, a formal semantics of AArch64 machine code grounds them in the compiled binary, and prover agents work only against Lean's verdicts.
In July 2025 the flagship became an advanced version of Gemini Deep Think, a reasoning mode using parallel thinking trained with reinforcement learning on theorem-proving data plus a curated corpus of high-quality solutions.

## Status

Very much active, as a research line that now also ships a public engineering artifact.
At IMO 2024, AlphaProof plus AlphaGeometry 2 solved four of six problems for 28 of 42 points, silver-medal standard, with problems manually translated into Lean and solve times from minutes to three days, scored by Fields Medalist Timothy Gowers and Joseph Myers.
At IMO 2025, Gemini Deep Think solved five of six problems perfectly for 35 of 42 points, graded by IMO coordinators under the same criteria as student solutions, within the official time limit.
The IMO stated its review did not extend to validating the system, processes, or underlying model.
DeepMind published the AlphaProof methodology in Nature on November 12, 2025, and says it believes agents combining natural-language fluency with verified formal reasoning are the path forward.
In February 2026, Google shipped the updated Deep Think as Gemini 3 Deep Think, which again reached gold-medal level on the IMO 2025 problems and, for the first time, opened a Gemini API early-access path for select researchers, engineers, and enterprises.
On October 8, 2026, the lineage's open-problems chapter landed in Science: AlphaProof Nexus (preprint arXiv 2605.22763, May 2026) pairs Gemini 3.1 Pro prover subagents with Lean compiler feedback, and its full-featured agent, which coordinates subagents evolutionarily and calls AlphaProof itself as a tool, resolved 9 of 353 attempted formalized Erdős problems (two open for 56 years) and proved 44 of 492 autoformalized OEIS conjectures, with every proof public in the alphaproof-nexus-results repository and a Science Perspective (Avigad and Ballard) declaring AI for research mathematics arrived.
On November 10, 2026, the name moved from mathematics to software: AlphaProof Code, a multi-agent framework pairing a human-guided specification-writing agent with a formal semantics of AArch64 machine code and a team of autonomous prover agents whose proofs Lean's kernel accepts only against the approved specification, proved key security properties of libsignal, the Signal protocol's reference implementation, at the machine-code level.
The development is about 6.3 million lines of machine-checked Lean on about 27,000 lines of trusted specification and semantics, covers the post-quantum PQXDH handshake and the Triple Ratchet (forward secrecy, authentication, post-compromise security, and handshake secrecy), took four weeks, and is open-sourced at google-deepmind/code-verification, with a 679-point, 197-comment Hacker News thread as the lineage's largest as of 2026-11-24.
As a check that the specifications catch bugs, the team reintroduced two previously fixed libsignal bugs and the system produced machine-checked proofs that the buggy versions were insecure.

## Strengths

- The training loop is grounded in machine-verified proofs, so reward is never a hallucinated "looks right".
- Official IMO grading in 2025 is the strongest third-party validation any system in this category has.
- Parallel thinking explores and combines multiple solution paths instead of one chain of thought.
- The 2024-to-2025 jump is documented with both systems' artifacts public.
- AlphaProof Code is the first artifact an engineer can read: the Lean development and the AArch64 semantics are public, and the bug-reintroduction check shows the specifications discriminate.

## Cautions

- The 2024 result required humans to translate problems into Lean, and took days, so it is not a tool an engineer can run.
- The 2025 result is a closed model behind a rollout to trusted testers and Google AI Ultra subscribers, with no API for the IMO configuration.
- Mathematicians flagged caveats around what the gold-medal claims mean, and the IMO disclaimer matters.
- Competition problems are verified and bounded; no Millennium-problem claim has been made.
- AlphaProof Code's specification is the trusted part: the paper says it cannot be automatically checked and a flaw there weakens the guarantee, so human experts review and approve it, the prover agents are general-purpose coding agents steered by skills, and GitHub records the artifact's license as NOASSERTION, so reuse terms need reading.
- The Nexus ablation cuts the architecture down to size: the basic generate-and-check agent solved the same nine Erdős problems, the cost figures count successful runs, and Lean verifies the encoded statement rather than that the encoding matches the intended problem.

## Pricing

No standalone pricing.
Deep Think access ships through the Google AI Ultra subscription tier as it rolls out, and the research systems themselves are not publicly runnable, though AlphaProof Code's Lean development is open.

## Compared to

- [Math Inc. Gauss](../math-inc-gauss/index.md): autoformalizes known mathematics at record scale with an auditable open harness; choose Gauss when the job is formalizing results, AlphaProof when it is solving new problems.
- [Anthropic Claude mathematical research](../anthropic-claude-math/index.md): a general model in a coding harness producing novel research results; choose the Claude loop for open-ended problems, AlphaProof for formal, verifiable competition-style targets.
- [Harmonic Aristotle](../harmonic-aristotle/index.md): a closed theorem-proving product you can actually use today; choose Aristotle when you need proofs now, AlphaProof when you need the strongest published evidence of capability.

## Bottom line

**Recommended reading for anyone designing verification-gated agent systems: this is the reference implementation of "the judge is a kernel, the worker is trained on verdicts".**
Not for practitioners who need a runnable prover today: the prover agents are not released, the Lean development of AlphaProof Code is readable but not a tool, and the Deep Think API path is early-access gated rather than open, as of 2026-11-24.

## Changes

- 2026-09-13 - Created as the DeepMind member of the new Automated research category.
- 2026-10-02 - Recorded the February 2026 Gemini 3 Deep Think update: the lineage now has a first Gemini API early-access path, so the bottom line no longer calls it strictly non-API.
- 2026-10-12 - Recorded AlphaProof Nexus's October 8 Science publication (nine formalized Erdős problems, 44 OEIS conjectures, public Lean artifacts) and the basic-agent ablation caveat.
- 2026-10-29 - Rotation re-verification: all eight references re-fetched, no drift; the alphaproof-nexus-results repository still holds the public Apache-2.0 proofs.
- 2026-11-15 - Rotation re-verification: all eight references re-fetched and live, no drift; the nexus-results repository still holds the public Apache-2.0 proofs and the DeepMind, Google, Wikipedia, arXiv, and Technology Review pages are unchanged.
- 2026-11-24 - Rotation re-verification: all eight references re-fetched and live with no drift in the nexus-results repository; recorded AlphaProof Code (November 10, 2026), the lineage's move into software verification, with the libsignal machine-code proofs, their size and scope, the open-sourced Lean development, the bug-reintroduction check, and the specification-as-trusted-base caution, and moved the pricing and bottom-line lines with it.

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
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-deep-think/ - the February 2026 Gemini 3 Deep Think update, its repeat IMO gold, and the first Gemini API early-access path
- https://arxiv.org/abs/2605.22763 - the AlphaProof Nexus paper: the two agents, the 9 of 353 Erdős and 44 of 492 OEIS results (fetched 200, 2026-10-28)
- https://github.com/google-deepmind/alphaproof-nexus-results - the public Apache-2.0 Lean proofs for the solved problems (fetched 200 via the API, 2026-10-28)
- https://magica.com/news/alphaproof-nexus-nine-erdos-problems-44-oeis-conjectures - the critical read: the basic-agent ablation, the cost-accounting gaps, and the encoding caveat (fetched 200, 2026-10-28)
- https://deepmind.google/blog/introducing-alphaproof-code/ - the November 10, 2026 AlphaProof Code announcement: the Signal verification, the Gemini Carbon prover agents, the six-million-line scale, the four-week timeline, and the bug-reintroduction check (fetched 200, 2026-11-24)
- https://google-deepmind.github.io/code-verification/ - the technical paper: the framework's three parts, the 6.3 million proof lines on 27,000 trusted lines, the PQXDH and Triple Ratchet coverage, the specification as the trusted base, and the two historical libsignal bugs (fetched 200, 2026-11-24)
- https://github.com/google-deepmind/code-verification - the open-sourced Lean development (fetched 200, 2026-11-24)
- https://hn.algolia.com/api/v1/items/50439193 - the 679-point, 197-comment Hacker News thread on AlphaProof Code as of 2026-11-24, including the spec-fidelity questions (fetched 200, 2026-11-24)
