---
title: OpenAI for Science
created: 2026-09-13
updated: 2026-09-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, openai, mathematics, science]
readability: 3
audience_notes: >
  Engineers tracking how frontier labs actually behave when they claim scientific results, and what to demand before believing one.
  Assumes you follow AI lab announcements.
---

OpenAI for Science is the lab program, launched October 2025 under Kevin Weil, that points frontier models at scientific and mathematical research, and within a year it produced both a genuine first and the messiest credit dispute in the category.
Facts below verified as of 2026-09-25.

**The program shows the ceiling and the failure modes of lab-run automated research at once: real results exist, but every headline arrived wrapped in overclaims, deleted posts, or a dispute over who did the work.**

## What it is

A dedicated OpenAI team (announced October 2025, led by VP Kevin Weil, formerly chief product officer, with a physics PhD past) charged with making scientists more productive on GPT-5-class models.
The stated mechanism is collaboration rather than oracle: models surface forgotten results, sketch proofs, and propose tests, with a model-as-its-own-critic workflow passing output between generator and critic before the human sees it.
Weil's framing: "2026 will be for science what 2025 was for software engineering".
The program backs academic researchers with free and discounted access, and published a case-study collection in November 2025.

## Status

Active and escalating fast, as of 2026-09-25.
October 2025: senior OpenAI figures posted that GPT-5 had solved unsolved math problems; mathematicians showed the model had dug existing solutions out of old papers, and the posts were deleted.
March 2026: GPT-5.4 solved the first open problem from Epoch AI's FrontierMath benchmark (a hypergraph-theory constant-factor bound), the benchmark of 14 bespoke unsolved problems explicitly built below Millennium scale.
May 2026: OpenAI announced an internal model had disproved the Erdős unit distance conjecture, a result experts treated as genuinely productive.
September 2026: OpenAI published a claimed proof of forced blow-up in R3 and T3 for the Navier-Stokes equations, a Millennium Prize Problem, attributed to an internal model "with very little human input", and shipped it with a public Lean 4 formalization (about 616,000 lines, no extra axioms per a third-party audit, formalized in 17 hours via GPT-6 Astra per OpenAI); NYU's Tristan Buckmaster and Anthropic's Levent Alpöge, who published their own Lean-verified forced Euler proofs hours earlier, disputed credit, OpenAI's Sébastien Bubeck denied trying to cut Alpöge from authorship and apologized for a remark about his career, Sam Altman backed Bubeck and confirmed OpenAI had started the project after rumors that Anthropic's models had solved Millennium problems, and no independent process has adjudicated either account, while Clay still lists the problem as unsolved and OpenAI says it will not claim the prize.

## Strengths

- Real benchmark firsts: the FrontierMath open-problem solve and the unit-distance disproof are substantive, not vapor.
- The generator-critic loop Weil describes is the transferable engineering pattern here.
- The academic access program lowers the cost of reproducing lab claims for outside researchers.
- Speed: from team launch to a Millennium-problem claim in under a year.

## Cautions

- The overclaim pattern is documented: the October 2025 episode ended with deleted posts, and Weil now says models are "not there yet" for novel discovery.
- The Navier-Stokes claim ships with a checkable Lean artifact, but a Lean certificate only verifies the encoded statement: the fit to Clay's formulation is still being audited, and the credit dispute is unadjudicated.
- OpenAI wrote that it "cannot rule out" that the mathematicians' own Codex usage data helped improve the models involved.
- Independent scientists keep finding subtle errors in celebrated results, including a published paper whose core GPT-5-proposed idea tested the wrong property.

## Pricing

A lab program, not a product, so no direct pricing.
The surrounding stack is plan-based: the case studies feature GPT-5 Pro at $200 per month, and OpenAI grants academic researchers credits and discounted access, as of 2026-09-18.

## Compared to

- [Anthropic Claude mathematical research](../anthropic-claude-math/index.md): the rival lab loop, which ships machine-checkable artifacts and named reviewers; OpenAI's disputed claims currently rest on vendor write-ups.
- [AlphaProof](../alphaproof/index.md): DeepMind submits to official third-party grading (the IMO); OpenAI's Millennium claim has a checkable artifact but no official grader.
- [OpenAI Deep Research](../openai-deep-research/index.md): the productized tool tier the program sits above.

## Bottom line

**Recommended watching for anyone who needs to calibrate how much a lab announcement is worth: this program is the case study in demanding artifacts, graders, and named reviewers before believing a research claim.**
Not a source of settled results as of 2026-09-18; treat the Navier-Stokes claim as pending until someone independent checks it.

## Changes

- 2026-09-13 - Created as the OpenAI lab-program member of the new Automated research category.
- 2026-09-25 - Recorded that the Navier-Stokes claim shipped with a public Lean 4 formalization (audited at about 616,000 lines with no extra axioms), that Buckmaster and Alpöge published their own Lean-verified Euler certificates, and reworked the verification caution accordingly.

## See also

- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins
- [Anthropic Claude mathematical research](../anthropic-claude-math/index.md) - the rival loop on the other side of the credit dispute
- [AlphaProof](../alphaproof/index.md) - the officially-graded verification path
- [OpenAI Deep Research](../openai-deep-research/index.md) - the product tier below the program

## References

- https://www.technologyreview.com/2026/01/26/1131728/inside-openais-big-play-for-science/ - the Weil interview: mission, critic loop, deleted-posts episode, and scientist skepticism
- https://thenextweb.com/news/bubeck-navier-stokes-account-apology-altman - the Navier-Stokes credit dispute, both accounts, and the data-usage question
- https://en.wikipedia.org/wiki/FrontierMath - the Epoch AI benchmark, its below-Millennium scope, and the GPT-5.4 open-problem solve
- https://en.wikipedia.org/wiki/GPT-5.4 - the March 2026 model generation behind the benchmark first
- https://mashable.com/tech/anthropic-fable-5-disproves-jacobian-conjecture - the May 2026 unit-distance disproof context and expert reads on AI counterexamples
- https://stanfordtechreview.com/articles/openai-buckmaster-navier-stokes-lean-proofs - the third-party audit of both sides' Lean certificates (line counts, zero extra axioms)
