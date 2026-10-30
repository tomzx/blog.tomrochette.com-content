---
title: OpenAI for Science
created: 2026-09-13
updated: 2026-10-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, openai, mathematics, science]
readability: 3
audience_notes: >
  Engineers tracking how frontier labs actually behave when they claim scientific results, and what to demand before believing one.
  Assumes you follow AI lab announcements.
---

OpenAI for Science is the lab program, launched October 2025 under Kevin Weil, that points frontier models at scientific and mathematical research, and within a year it produced both a genuine first and the messiest credit dispute in the category.

**The program shows the ceiling and the failure modes of lab-run automated research at once: real results exist, but every headline arrived wrapped in overclaims, deleted posts, or a dispute over who did the work.**

## What it is

A dedicated OpenAI team (announced October 2025, led by VP Kevin Weil, formerly chief product officer, with a physics PhD past) charged with making scientists more productive on GPT-5-class models.
The stated mechanism is collaboration rather than oracle: models surface forgotten results, sketch proofs, and propose tests, with a model-as-its-own-critic workflow passing output between generator and critic before the human sees it.
Weil's framing: "2026 will be for science what 2025 was for software engineering".
The program backs academic researchers with free and discounted access, and published a case-study collection in November 2025.

## Status

Active and escalating fast, as of 2026-10-06.
October 2025: senior OpenAI figures posted that GPT-5 had solved unsolved math problems; mathematicians showed the model had dug existing solutions out of old papers, and the posts were deleted.
March 2026: GPT-5.4 solved the first open problem from Epoch AI's FrontierMath benchmark (a hypergraph-theory constant-factor bound), the benchmark of 14 bespoke unsolved problems explicitly built below Millennium scale.
May 2026: OpenAI announced an internal model had disproved the Erdős unit distance conjecture, a result experts treated as genuinely productive.
August 2026: OpenAI announced ten results across mathematics and theoretical computer science from an unreleased internal version of Astra, each shipped with a machine-checkable Lean 4 certificate in the Apache-2.0 openai/ten-proofs repository plus a 249-page manuscript: the first construction of a non-sofic group (open since Gromov defined soficity in 1999), a disproof of Connes's rigidity conjecture, Erdős problems 146, 180, and 183, the first improvement to the general sphere-packing bound since 1978, and a circuit lower bound for the permanent, at a claimed token cost of about $2,000, with erdosproblems.com's Thomas Bloom calling the set "big news" and bigger than the unit-distance disproof.
September 2026: OpenAI published a claimed proof of forced blow-up in R3 and T3 for the Navier-Stokes equations, a Millennium Prize Problem, attributed to an internal model "with very little human input", and shipped it with a public Lean 4 formalization (about 616,000 lines, no extra axioms per a third-party audit, formalized in 17 hours via GPT-6 Astra per OpenAI); NYU's Tristan Buckmaster and Anthropic's Levent Alpöge, who published their own Lean-verified forced Euler proofs hours earlier, disputed credit, OpenAI's Sébastien Bubeck denied trying to cut Alpöge from authorship and apologized for a remark about his career, Sam Altman backed Bubeck and confirmed OpenAI had started the project after rumors that Anthropic's models had solved Millennium problems, and no independent process has adjudicated either account, while Clay's September 11 statement says the problem "has apparently been settled", now badges it Active on its site, and calls verification "deliberately unhurried", and OpenAI says it will not claim the prize.
At DevDay on September 29, research lead Tejal Patwardhan said OpenAI's models have already helped solve more than 100 mathematics problems that had been open for decades, and Altman confirmed the September "automated research intern" goal set a year earlier was met.
October 2026: OpenAI published the openai/math repository (created October 6), 722 manuscripts in 372 result families claimed from roughly 4,000 posed problems at an average three hours of ChatGPT Pro thinking compute each, with a matrix-multiplication upper bound near n^2.25 among the headlines; a sign error invalidated one construction and two papers that depended on it, withdrawn on October 7 to leave 719, fourteen others were revised, and about 42 percent of top-line results now carry Lean formalizations; on October 26 the catalogue grew to 721 manuscripts in 373 families with two added formalized results, a local-smoothing proof for the Euclidean wave equation and a claimed refutation of the Exponential Time Hypothesis, the latter released at the request of an independent working group led by Impagliazzo, Paturi, and Williams before its examination.
October also produced the category's sharpest verification finding: a Cambridge and King's College London team posted (arXiv 2610.08144, October 6) that the Navier-Stokes Lean code does not match its written proof, proving a weaker Lemma 8.6 (a value below m + 5 where the paper states m + 4); the authors do not claim either proof wrong, New Scientist covered it as a mistranslation, OpenAI acknowledged the mismatch, and Kevin Buzzard separated the two, confident in the result and far less confident in the PDF.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=openai/ten-proofs&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=openai/ten-proofs&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=openai/ten-proofs&type=date&legend=top-left" />
</picture>

## Strengths

- Substantive firsts: the FrontierMath open-problem solve, the unit-distance disproof, and the ten Lean-certificated results of August are not vapor, and anyone can build the certificates.
- The generator-critic loop Weil describes is the transferable engineering pattern here.
- The academic access program lowers the cost of reproducing lab claims for outside researchers.
- Speed: from team launch to a Millennium-problem claim in under a year.

## Cautions

- The overclaim pattern is documented: the October 2025 episode ended with deleted posts, and Weil now says models are "not there yet" for novel discovery.
- The Navier-Stokes claim ships with a checkable Lean artifact, but the encoded statement is option C of Charles Fefferman's 2000 Clay formulation, the variant that allows an external force: Luis Silvestre's summary is "the Clay problem is settled, but the main problem for the Navier-Stokes equations is not", three mathematicians posted a proof on September 17 that OpenAI's forced-blowup method can never extend to the unforced problem, and the credit dispute is unadjudicated.
- OpenAI first wrote that it "cannot rule out" that the mathematicians' own Codex usage data helped improve the models involved, then said a follow-up investigation confirmed those Codex prompts "could not have influenced the system in any way, including through training", then extended the claim on September 13 to "no user inputs past July 3rd", and the period before July 3, when the use was heaviest, has not been addressed.
- Twenty-eight Fields Medalists published "A Severe Misalignment of AI in Mathematics" on September 11, warning that treating unsolved problems as benchmarks is "detrimental to the science of mathematics", the strongest institutional criticism this program has drawn.
- Independent scientists keep finding subtle errors in celebrated results, including a published paper whose core GPT-5-proposed idea tested the wrong property.
- The certificate-prose gap is now documented: the Navier-Stokes Lean code proves a weaker Lemma 8.6 than the paper states, so a compiling artifact does not stand in for the written argument, and the released batch already took three withdrawals for a sign error.

## Pricing

A lab program, not a product, so no direct pricing.
The surrounding stack is plan-based: the case studies feature GPT-5 Pro at $200 per month, and OpenAI grants academic researchers credits and discounted access, as of 2026-09-18.

## Compared to

- [Anthropic Claude mathematical research](../anthropic-claude-math/index.md): the rival lab loop, which ships machine-checkable artifacts and named reviewers; OpenAI's disputed claims currently rest on vendor write-ups.
- [AlphaProof](../alphaproof/index.md): DeepMind submits to official third-party grading (the IMO); OpenAI's Millennium claim has a checkable artifact but no official grader.
- [OpenAI Deep Research](../openai-deep-research/index.md): the productized tool tier the program sits above.

## Bottom line

**Recommended watching for anyone who needs to calibrate how much a lab announcement is worth: this program is the case study in demanding artifacts, graders, and named reviewers before believing a research claim.**
Not a source of settled results as of 2026-10-12; the Navier-Stokes certificate checks out against its own encoded statement, but that statement is provably weaker in Lean than the written lemma it claims to formalize, the formulation is contested, and three of the 719 released manuscripts were withdrawn for a sign error.

## Changes

- 2026-09-13 - Created as the OpenAI lab-program member of the new Automated research category.
- 2026-09-25 - Recorded that the Navier-Stokes claim shipped with a public Lean 4 formalization (audited at about 616,000 lines with no extra axioms), that Buckmaster and Alpöge published their own Lean-verified Euler certificates, and reworked the verification caution accordingly.
- 2026-09-29 - Recorded the formulation finding: the certificate covers Clay option C (forced blow-up), Silvestre and other experts name the unforced problem as the real one, and a September 17 three-mathematician proof shows OpenAI's method cannot extend to it (Scientific American, 2026-09-21).
- 2026-10-02 - Recorded OpenAI's follow-up investigation claim that Buckmaster's Codex prompts could not have influenced the system in any way, including through training, superseding its earlier "cannot rule out" line, and added the Wikipedia priority-controversy article as a reference.
- 2026-10-05 - Corrected the Clay status (its September 11 statement says the problem has "apparently been settled", the problem page now reads Active, verification "deliberately unhurried"), recorded the 28-Fields-Medalist declaration of September 11, and the September 13 extension of OpenAI's data-influence claims to "no user inputs past July 3rd".
- 2026-10-06 - Recorded the August 1 ten-results release (unreleased Astra, public Lean certificates in the openai/ten-proofs repository, Bloom's "big news" read, about $2,000 of claimed compute) and DevDay's September 29 claims (more than 100 long-open mathematics problems helped solved, the September "research intern" goal met).
- 2026-10-07 - Added the openai/ten-proofs star history chart to the Status section.
- 2026-10-12 - Recorded the October 6 openai/math release (722 manuscripts, three withdrawn over a sign error, about 42 percent formalized) and the lost-in-translation finding that the Navier-Stokes Lean code proves a weaker Lemma 8.6 than the written proof.
- 2026-10-29 - Rotation re-verification: recorded the October 26 openai/math additions (the catalogue at 721 manuscripts in 373 families, a formalized local-smoothing proof for the wave equation, and the claimed ETH refutation released for the Impagliazzo-Paturi-Williams working group's examination).

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
- https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/ - the formulation fight: Clay option C, Silvestre's "main problem is unsolved", and the September 17 no-extension proof
- https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy - the consolidated timeline of the credit dispute, both sides' statements, the Clay status change, and the Fields Medalist declaration (fetched 200, 2026-10-05)
- https://www.claymath.org/news/navier-stokes-announcement - Clay's September 11 statement: "apparently been settled" and "deliberately unhurried" verification (fetched 200, 2026-10-05)
- https://mathandai.org/ - "A Severe Misalignment of AI in Mathematics", the declaration text and its 28 Fields Medalist signatories, DOI 10.5281/zenodo.22737750 (fetched 200, 2026-10-05)
- https://github.com/openai/ten-proofs - the Apache-2.0 repository of Lean certificates for the ten August results, created 2026-08-05 (fetched via GitHub API, 2026-10-06)
- https://thenextweb.com/news/openai-astra-model-ten-math-proofs-non-sofic-groups - the ten-results release: non-sofic group, Connes rigidity disproof, Erdős 146/180/183, the sphere-packing bound, and Bloom's reaction (fetched 200, 2026-10-06)
- https://thenextweb.com/news/sam-altman-openai-ai-research-intern-devday-keynote - DevDay September 29: the research-intern milestone and Patwardhan's more-than-100-problems claim (fetched 200, 2026-10-06)
- https://github.com/openai/math - the manuscript catalogue: 721 in 373 families after the October 26 additions, the history with the sign-error retraction and the new-results entries, and the 42 percent formalization count (fetched 200, 2026-10-29)
- https://arxiv.org/abs/2610.08144 - "Navier-Stokes lost in translation": the mistranslation argument and its solvability-hierarchy framing (fetched 200, 2026-10-12; re-fetched 200, 2026-10-29)
- https://www.newscientist.com/article/2592824-openai-mistranslated-mathematics-into-code-for-its-navier-stokes-proof/ - the Lemma 8.6 m+4 versus m+5 finding and OpenAI's response (fetched 200, 2026-10-12; bot-walled to automated refetch on 2026-10-29, still indexed)
