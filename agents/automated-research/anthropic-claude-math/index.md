---
title: Anthropic Claude mathematical research
created: 2026-09-13
updated: 2026-11-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, automated-research, anthropic, mathematics, formal-verification]
readability: 3
audience_notes: >
  Engineers who run multi-agent coding workflows and want to see the same tooling pointed at research mathematics.
  Assumes you know what Claude Code, subagents, and Lean are.
---

Anthropic's research-math program points unreleased Claude research models, and since November 2026 its own mathematicians working with Claude, at open mathematics through Claude Code, with subagent fleets doing the work and Lean plus named human experts as the trust gates.

**The frontier research loop is now ordinary engineering tooling: one staff member, a coding agent, about sixty subagents, thousands of shell commands, and a compiler as the judge.**

**On November 20, 2026 the program crossed from bounds to a Millennium Problem: Anthropic mathematician Levent Alpöge posted a 17-million-line Lean proof of the Riemann hypothesis that he says he discovered working with Claude, and the Lean FRO and the Mathlib Initiative certified the statement and the proof the next day, while no human-readable write-up exists and the Clay prize sits at least two years of scrutiny away.**

## What it is

A series of Anthropic Science results produced by Claude models working in a Claude Code multi-agent harness, validated and published with artifacts.
On August 10, 2026, Anthropic reported that an unreleased research version of Claude, asked to take a real stab at the Riemann hypothesis, failed at the hypothesis itself but raised the lower bound for the share of zeta zeros on the critical line from 41.6 to 67.2 percent.
The run took two sessions and 31 million output tokens: after 650 failed ideas, Claude spent a day and a half coordinating about sixty subagents that ran 2,400 shell commands and hundreds of Python scripts, checked against known zeta zeros, refereed one another, and downloaded 54 arXiv papers to confirm novelty.
Anthropic mathematicians Levent Alpöge and Ralph Furman validated the result, external experts Brian Conrey and Dan Goldston reviewed it on short notice, and the Lean formalization passes the comparator checker in the public anthropics/formal-math repository.
On September 4, 2026, Anthropic published the first complete computer-checked proof of Fermat's Last Theorem: 11 days, largely autonomous, 13 million lines of Lean, 30,300 theorems proved along the way, about six billion output tokens from an internal research model described as roughly comparable to Claude Fable 5.1, reviewed by Kevin Buzzard.
The FLT effort succeeded only after switching to Prove2Me, a platform maintaining a directed acyclic graph of theorem statements so parallel agents stop losing track of project state.
Anthropic's own zeta post footnote also credits a Claude model with disproving the Jacobian conjecture, which press coverage attributes to Fable 5 via Alpöge's announcement.
The human-piloted variant arrived on November 20, 2026: Alpöge, a number theorist at Anthropic on leave from Harvard, posted a four-page note and a 17-million-line Lean library, writing that he believes he has, working with Claude, discovered a proof of the Riemann hypothesis, one that extends to its generalized form for Dirichlet L-functions.
His note calls the argument a descendant of Stepanov's function-field proof that recovers multiplicity over the integers by chaining theta lifts, gives a timeline from an October 6 Stepanov determinant to GRH on November 16, says Claude far outpaced him near the finish line, and states that he decided to only present Lean rather than post what he calls a massive unreadable travesty, with the write-up he generated for his own amusement running past 250,000 pages.

## Status

Very active and widening, as of 2026-11-24.
**The Riemann claim is machine-checked and not yet understood: the Lean FRO and the Mathlib Initiative certified on November 21 that Alpöge's library compiles, that the theorem it proves is exactly Mathlib's `RiemannHypothesis` statement (confirmed by two independent comparison tools, comparator and con-leche), and that the exported proof passes Lean's kernel, the nanoda and con-leche checkers, and several third-party checkers, and Andrew Sutherland's MIT verification page records the same results as of November 23 with one end-to-end comparator run still in progress.**
The proof now lives at leanprover-community/riemann-hypothesis, a community cleanup effort whose `original` branch preserves Alpöge's release.
The human side is unsettled: hours after the post Ravi Vakil published a rival, all-human preprint by Alessandro Maria Masullo, Andrew Granville told Nature the released document is garbled and should have had a clearer write-up, James Maynard suspects the proof will turn out correct, and Anthropic did not comment to Nature or The Verge.
The timing is part of the record: the post came a day after Anthropic's initial public offering on November 19, which Nature reports initially valued the company at $1.5 trillion before its valuation dropped, and Alpöge's note says he asked Dario Amodei about announcing and that the obvious cynical view of the timing is false.
Under the Clay institute's rules a proposed solution must be published and withstand at least two years of scrutiny before it can be considered for the prize.
September alone brought the nine-loop amplitude in N=4 super Yang-Mills (September 25, guest-posted by the physicist who issued the challenge) and, beyond mathematics, a new life-sciences laboratory whose agents discovered a novel CRISPR-like enzyme system (September 23).
The models are unreleased research versions, so that loop is not reproducible by outsiders, while the Riemann work ran on Claude with a mathematician at the controls.
The artifacts are public and machine-checkable: the formal-math repository (297 stars as of 2026-10-11) is Apache-2.0 with pinned toolchains and CI that builds with no `sorry` outside trusted statement files, on October 6 it absorbed a new formalization of a 3SUM/APSP algorithms-paper result (truly subquadratic 3SUM via triangles in sparse lopsided graphs), on October 27 it added a second algorithms-paper formalization, a Lean 4 rendering of the 2^o(n)-time 3-SAT algorithm, widening the artifact chain beyond pure mathematics, and on November 23 it added `vp-vnp`, a paper by Claude with its Lean 4 proof that VP ≠ VNP over every field (circuits for the Hamiltonian cycle polynomial, and for the permanent outside characteristic 2, need more than m^(c (log m)^(1/3)) gates), 73,324 added lines whose merge passed the from-scratch CI build and comparator check.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=anthropics/formal-math&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=anthropics/formal-math&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=anthropics/formal-math&type=date&legend=top-left" />
</picture>

Community footprint is strong, with the zeta result drawing a 282-point Hacker News discussion, and the vp-vnp folder drawing a Hacker News thread opened 26 minutes after its merge (184 points and 140 comments as of 2026-11-24), whose critical comments call it proof by slop and note that no human mathematician is credited.
A three-person experiment formalized Vinogradov's three primes theorem in three days on consumer Claude Max plans, and the October 1 Claude-shaped science post documents the loop's most copyable instance yet: 36 manuscripts in 18 fields in three months, driven through Claude Code sessions on cloud VMs and an open-source harness (BootLoops), with human collaborators supplying taste and expert review.
The widening continued on October 8 with the first complete UV map of the sky, built by Johns Hopkins astrophysicist and Anthropic researcher Brice Ménard with Claude Science: merged GALEX-era datasets, cross-wavelength inpainting for the never-observed third of the sky, and over 100 million Gaia-inferred stars.
The loop has also escaped the vendor: Nobel laureate Giorgio Parisi and Francesco Zamponi proved the decade-old jamming identity a + b = 1 with Claude and published the full transcript alongside their paper (October 10), and Tom Verhoeff's proof of Lehmer's permutation conjecture (arXiv 2610.01240, submitted October 1) reports Claude Opus 5.5 autonomously finding two core concepts that cut a 150-page human-AI proof under 30 pages.
Independent human follow-up has started too: Youness Lamzouri re-derived the 67.2 percent zeta bound with a simpler argument drawn from the same prior work, added a corollary (at most 11 percent of zeros neither simple nor on the line), and James Maynard held up the episode as the positive path for AI-assisted mathematics.

## Strengths

- Every headline result ships with a machine-checkable artifact, not just a blog post.
- The methodology notes read like engineering postmortems: failed attempts, state loss, and the DAG fix are documented.
- Novelty checking is built into the loop, including downloading and reading prior work before claiming a result.
- Failures still contributed: about 7 percent of the final FLT lines came from abandoned attempts.
- The nine-loop solve stayed inside an academic budget, about $100 of compute on 96 CPUs for a week on the bootstrap path, and was validated by Lance Dixon, the researcher whose team had queued the problem.
- The Riemann proof went to an outside certification within a day: the statement is Mathlib's own, and the checks were run by the Lean FRO, the Mathlib Initiative, and an MIT mathematician rather than by Anthropic.

## Cautions

- The results are vendor-validated first and community-validated slowly, and the zeta bound's external review was two experts on short notice.
- A counterexample-style disproof can be a thin result: mathematician Andrew Blumberg told Mashable the Jacobian counterexample was the kind of thing he expected AI to find, granted it as a significant achievement, and said you want to learn something from the answer, not just get it.
- The encouraging-prompt detail (a non-mathematician telling Claude to keep going) is charming but also a reminder that the model's own calibration failed here.
- The Riemann proof's open question is comprehension, not the correctness of the formal statement: the only write-up is four pages that Granville calls garbled, Nature's sources expect the argument to take a long time to digest, Alpöge says he has not yet mastered the mathematics around it, and the vendor stayed silent.
- vp-vnp carries the program's thinnest validation: its paper and README say the proofs were found and written by AI, that no human mathematician has checked them, that whether the statements say what is meant was judged only by AI readers, and that the contracting case, and with it every main result, rests on Lean at four machine-verified steps.
- The program's own results still come from the vendor's write-ups, though independent follow-up has begun: Lamzouri re-derived and simplified the zeta bound, Parisi and Zamponi published their full transcript, and the Lean FRO and Mathlib Initiative certified the Riemann proof.
- The independent reads cut against the breakthrough framing: von Hippel's own takeaway is that Claude solved his challenge with known methods on more compute, and Song He's group matched most of the nine-loop result days later with GPT-6 assistance, so the low-hanging-fruit reading beats the new-capability reading.
- The Claude-shaped science post is also a failure-mode catalog: the author documents Claude declaring victory with an unproven lemma, having no sense of time, and needing every result looked at by a human.

## Pricing

The published artifacts are free under Apache-2.0.
The compute is internal and not priced publicly, and Anthropic sells the ingredients (Claude subscriptions plus science grant programs) rather than the loop itself.

## Compared to

- [Math Inc. Gauss](../math-inc-gauss/index.md): a purpose-built autoformalization agent with an open harness and audited benchmarks; choose Gauss for formalization throughput, the Claude loop for genuinely new mathematics.
- [OpenAI for Science](../openai-for-science/index.md): the rival lab program, currently defined by a disputed Navier-Stokes claim; Anthropic's publish-the-artifacts-and-invite-review pattern is the sharper contrast.
- [AlphaProof](../alphaproof/index.md): the trained prover with official IMO grading; choose AlphaProof for the strongest third-party-graded evidence, the Claude program for the claimed open-problem results.
- [Claude Code](../../harnesses/claude-code/index.md): the harness underneath, which you can run today with your own subagent fleets.

## Bottom line

**Recommended for anyone orchestrating long-horizon multi-agent work: this is the best-documented public example of subagent fleets, DAG coordination, and verification gates applied to research, and since November 2026 also the best-documented case of a machine-checked result that mathematicians expect to take years to digest.**
Not for anyone expecting to rerun the exact research-model loops, since the models are unreleased as of 2026-09-18.

## Changes

- 2026-09-13 - Created as the Anthropic member of the new Automated research category.
- 2026-10-05 - Recorded the September-to-October widening: the nine-loop N=4 super Yang-Mills amplitude (September 25, Fable 5.1 in Claude Science, Dixon-validated), the life-sciences laboratory and its ART enzyme discovery (September 23), and the 36-manuscript BootLoops campaign (October 1); formal-math stars refreshed to 253.
- 2026-10-07 - Added the anthropics/formal-math star history chart to the Status section.
- 2026-10-11 - Recorded the formal-math repository's October 6 addition of a 3SUM/APSP algorithms-paper formalization and refreshed the star count to 297.
- 2026-10-12 - Recorded the October 8 UV sky map, the first third-party Claude proofs (Parisi-Zamponi's jamming identity with full transcript, Verhoeff's Lehmer conjecture), and the independent zeta follow-up (Lamzouri's simpler re-derivation).
- 2026-10-28 - Recorded the formal-math repository's October 27 addition of a Lean 4 formalization of the 2^o(n)-time 3-SAT algorithm paper, the artifact chain's second algorithms result.
- 2026-11-14 - Rotation re-verification: all thirteen references re-fetched and live (two api.github.com 403s retried through the authenticated API), with the formal-math default branch quiet since the October 27 3-SAT formalization (the November 1 repository-level push was a side branch, per the standing default-branch rule) and every other claim standing.
- 2026-11-24 - Rotation re-verification: all thirteen references re-fetched and live; recorded the November 20 Riemann hypothesis proof Levent Alpöge says he discovered working with Claude (the 17-million-line Lean library, the Lean FRO and Mathlib Initiative certification of November 21, Sutherland's verification page, Masullo's rival all-human preprint, Granville's and Maynard's reads, the day-after-the-IPO timing, and the Clay two-year rule), the formal-math repository's November 23 `vp-vnp` paper and Lean proof of VP ≠ VNP over every field with its passed CI check and no-human-review disclosure, Anthropic's November 19 initial public offering, and the AlphaProof comparison line; reworded the Blumberg caution to Mashable's quoted words.

## See also

- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins
- [Math Inc. Gauss](../math-inc-gauss/index.md) - the dedicated autoformalization agent and its comparator-audited benchmark
- [OpenAI for Science](../openai-for-science/index.md) - the rival lab loop and its credit dispute
- [AlphaProof](../alphaproof/index.md) - the trained-prover lineage whose AlphaProof Code shares the Lean-gated pattern
- [Ouroboros](../../software-factory/ouroboros/index.md) - the same hidden-grading pattern applied to software instead of proofs
- [Claude Code](../../harnesses/claude-code/index.md) - the harness the loop runs on

## References

- https://www.anthropic.com/research/riemann-zeta - the zeta zero bound result, subagent methodology, validation chain, and the Jacobian footnote
- https://www.anthropic.com/research/formalizing-fermats-last-theorem - the FLT formalization, Prove2Me DAG platform, token costs, and Buzzard review
- https://github.com/anthropics/formal-math - the public Apache-2.0 Lean formalizations, Palomar/comparator CI, and the Alpöge-Furman arXiv reference
- https://api.github.com/repos/anthropics/formal-math - the star count, the October 6 3sum-apsp commit behind the status line, and the October 27 commit adding the 3-SAT algorithm paper's Lean formalization (fetched 200, 2026-10-28)
- https://mashable.com/tech/anthropic-fable-5-disproves-jacobian-conjecture - press account of the Jacobian disproof and Blumberg's skeptical read (fetched 200, 2026-10-12 and 2026-11-24)
- https://hn.algolia.com/api/v1/search?query=Anthropic%20mathematics&tags=story&hitsPerPage=20 - the community footprint, including the 282-point zeta discussion
- https://www.anthropic.com/research/yes-claude-can-do-nine-loops - the nine-loop challenge and solve: budgets, Dixon's validation, and the concurrent GPT-6-assisted human result (fetched 200, 2026-10-05)
- https://www.anthropic.com/research/claude-shaped-science - the BootLoops campaign: 36 manuscripts in 18 fields, the coordination setup, and the failure-mode catalog (fetched 200, 2026-10-05)
- https://www.anthropic.com/news/claude-discovers-novel-enzyme-system - the life-sciences lab and the ART discovery, about 950 agents over 21 hours (fetched 200, 2026-10-05)
- https://www.anthropic.com/research/the-missing-map-of-the-sky - the October 8 UV map: GALEX-era merge, cross-wavelength inpainting, and the Gaia star layer (fetched 200, 2026-10-12)
- https://www.livescience.com/technology/artificial-intelligence/this-is-what-happened-with-claude-and-me-ais-failed-attempt-to-crack-the-riemann-hypothesis-led-mathematician-to-a-breakthrough - Lamzouri's re-derivation of the zeta bound and Maynard's assessment (fetched 200, 2026-10-12)
- https://hypothesiswire.com/articles/nobel-laureate-and-colleague-crack-10-year-jamming-proof-with-claude-9074d2a3 - the Parisi-Zamponi jamming identity proof and the published transcript (fetched 200, 2026-10-12)
- https://arxiv.org/abs/2610.01240 - Verhoeff's proof of Lehmer's permutation conjecture (fetched 200, 2026-10-12)
- https://alpo.ge/remark.pdf - Alpöge's November 20, 2026 note: the claim, the Generalized Riemann Hypothesis extension, the October 6 to November 16 timeline, the decision to present only Lean, and the timing footnote (fetched 200, 2026-11-24)
- https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ - the Lean FRO and Mathlib Initiative joint statement of November 21, 2026: 17 million lines, the four satisfied criteria, and the independent checkers (fetched 200, 2026-11-24)
- https://math.mit.edu/~drew/grh/ - Andrew Sutherland's verification page: the check-by-check results as of November 23, 2026, with the lake comparator run still in progress (fetched 200, 2026-11-24)
- https://github.com/leanprover-community/riemann-hypothesis - the community cleanup repository: the five theorem statements, the comparator setup, and the `original` branch preserving Alpöge's release (fetched 200, 2026-11-24)
- https://www.nature.com/articles/d41586-026-03812-7 - Nature's November 20, 2026 report (updated November 23): Masullo's rival preprint, Granville's and Maynard's assessments, the $1.5 trillion IPO valuation, and Anthropic's non-response (fetched 200, 2026-11-24)
- https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/ - Scientific American's November 20, 2026 report: Sutherland's independent compilation and the Pasten and Pagano reactions (fetched 200, 2026-11-24)
- https://www.theverge.com/ai-artificial-intelligence/1010051/anthropic-riemann-hypothesis-millennium-prize-problem - The Verge's November 20, 2026 report: the Thursday IPO, Anthropic's non-involvement, and the Clay two-year rule (fetched 200, 2026-11-24)
- https://github.com/anthropics/formal-math/tree/main/vp-vnp - the vp-vnp README: the VP ≠ VNP statement, the internal-research-model discovery, the no-human-check disclosure, and the build and comparator instructions (fetched 200, 2026-11-24)
- https://raw.githubusercontent.com/anthropics/formal-math/main/vp-vnp/paper.pdf - the vp-vnp paper by Claude: the m^(c (log m)^(1/3)) lower bound, the flat and contracting cases, and Appendix Q's statement-fidelity disclosure (fetched 200, 2026-11-24)
- https://github.com/anthropics/formal-math/pull/51 - the November 23, 2026 merge adding vp-vnp (333 files, 73,324 lines) (fetched 200, 2026-11-24)
- https://github.com/anthropics/formal-math/actions/runs/45272623486 - the from-scratch CI run on the merge commit: 9,032 build jobs, `sorry` only in Challenge.lean, and the comparator's acceptance (fetched 200, 2026-11-24)
- https://hn.algolia.com/api/v1/items/50620102 - the Hacker News thread on vp-vnp, 184 points and 140 comments as of 2026-11-24 (fetched 200, 2026-11-24)
