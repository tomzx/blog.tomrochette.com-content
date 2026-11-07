---
title: Harmonic Aristotle
created: 2026-09-13
updated: 2026-11-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, harmonic, mathematics, formal-verification]
readability: 3
audience_notes: >
  Engineers evaluating automated theorem provers and proof-carrying tooling for software verification.
  Assumes you know what Lean and a proof assistant are.
---

Aristotle is Harmonic's agentic theorem prover, sold as mathematical superintelligence and applied since October 2026 to formal verification of code (C and Verilog) as well as mathematics, and it is the one system in this category a working engineer can sign up for and use today.

**Aristotle's real results are machine-checkable and independent, but the benchmark fight around it shows the judging layer has become the battleground: its own vendor claims are unauditable, and its loudest rival publishes comparator-audited numbers against it.**

## What it is

A web agent at aristotle.harmonic.fun: give it an English problem and it proves and formalizes from scratch, or point it at your Lean project or code repository and it works on files directly.
The product page now leads with "Code, proven correct": your agents write more code than your team can review, Aristotle proposes the properties your code must satisfy and proves each one on every commit, and the company banner stays "Mathematical Superintelligence".
On October 27, 2026, Harmonic expanded Aristotle into formal verification for software and hardware, starting with C (functional correctness and classes of undefined behavior) and Verilog (safety, liveness, and data-path properties), running in CI and deployable on-prem or in a private cloud.
Harmonic runs a $1,000,000 Mathematician Sponsorships program (announced 2026-01-22) that takes applications at aristotle.harmonic.fun/sponsorships.
The company calls its category "Mathematical Superintelligence"; it raised a $120 million Series C at a $1.45 billion valuation led by Ribbit Capital in November 2025, and is led by co-founders Tudor Achim (CEO) and Vlad Tenev (executive chairman).

## Status

Live product, as of 2026-11-07.
On October 27, 2026, Harmonic expanded Aristotle from research mathematics into software and hardware verification: it proposes properties from your code, engineers review and commit them to the repository, and Aristotle runs in CI on every commit, returning proved, refuted (with a runnable counterexample), or unresolved per property.
The expansion launched with vendor case studies: at Tensordyne it found bugs up to 110,000 cycles deep in the block their team considered hardest to verify, and on LibTomMath it fixed three bugs and made modular exponentiation 31 to 38 percent faster in Harmonic's own benchmarks, with the faster code proved against the same spec.
The strongest independent credential is still a November 2025 result on Erdős problem #124: Aristotle produced a proof working only from the formal statement, Boris Alexeev formalized and cleaned the statement, Lean checked it, and the Erdős Problems site updated to record that a version of the problem was solved, with the community debate over exactly which version playing out in public.
Independent third-party benchmarking in July 2026 (the OpenATP project) scored Aristotle 10/10 on the FATE-H theorem set for free, at roughly twice the wall-clock time of Claude Code and Codex.
On Math Inc.'s FormalQualBench (March 2026), Aristotle solved 6 of 23 with no time limit, but those runs were not validated with the comparator tool and are excluded from the audited counts.

## Strengths

- Agentic end to end: natural language in, machine-checked proof out, or direct work inside your repository.
- Self-serve access keeps the barrier to experimenting with proof agents low, and the Lean-checked Erdős artifact is public and type-checkable in the browser, so the claim does not rest on Harmonic's word.
- Harmonic claims formalization project leaders accept its code contributions without modification.

## Cautions

- The benchmark record is contested: Math Inc's comparator-audited run beat Aristotle's unaudited 6/23, and the "IMO gold reasoning" line is unverifiable marketing.
- The Erdős result solved "a version" of the problem, not the version the original authors posed, a nuance the community itself flagged.
- Closed system: no weights, no self-hosting, and a login wall between you and the agent; on-prem deployment exists but only as an enterprise offering.
- A formal statement typo it worked from made the target weaker, a reminder that autoformalization inherits upstream spec bugs.
- The October expansion's headline results are Harmonic's own case studies, and the pivot moves the product toward exactly the code-review workload whose judging the category's comparator lessons say needs independent verification.
- The move to consumption-based pricing ended the free tier, and per-proof amounts are not published, so budgeting a verification campaign is guesswork until you run one.

## Pricing

Consumption-based self-serve pricing since the October 27, 2026 expansion: "pay for what you use, with no seats or licenses", with per-proof amounts unpublished on the fetched pages.
Enterprise plans add volume pricing, dedicated support, and on-prem or private-cloud deployment via contact.
Harmonic's $1,000,000 Mathematician Sponsorships program continues to take applications.

## Compared to

- [Math Inc. Gauss](../math-inc-gauss/index.md): OpenGauss is open source, comparator-audited, and cheaper per solve on FormalQualBench; choose OpenGauss when auditability matters, Aristotle when you want a zero-setup hosted agent.
- Claude Code and Codex used as theorem provers: faster on the FATE sets but paid per token; Aristotle matched their accuracy for free in the July benchmark at half the speed, though it has been consumption-priced since October.
- [AlphaProof](../alphaproof/index.md): DeepMind's systems are stronger published evidence but not runnable; Aristotle is weaker provenance but a usable product.

## Bottom line

**Recommended for engineers who want to point a proof agent at Lean, C, or Verilog artifacts this week, with every result Lean-checked.**
Not for audit-sensitive verification work as of 2026-11-07, where the comparator-audited open harness is the defensible choice.

## Changes

- 2026-09-13 - Created as the Harmonic member of the new Automated research category.
- 2026-10-02 - Named the $1,000,000 program (Mathematician Sponsorships, announced 2026-01-22) and added the funding and leadership facts the note previously lacked (Series C, Achim and Tenev).
- 2026-10-19 - Full re-verification pass: all seven references re-fetched and current (the sponsorship and Series C pages are client-rendered, confirmed via their page metadata), with the OpenATP comparison, the FormalQualBench exclusion, and the Erdős record unchanged.
- 2026-11-07 - Rotation re-verification turned a material pivot: recorded the October 27 expansion into C and Verilog verification (CI integration, the Tensordyne and LibTomMath case studies, on-prem or private-cloud deployment), moved Pricing from free-with-an-account to consumption-based self-serve with unpublished amounts, and rewrote the positioning to the "Code, proven correct" framing; all seven prior references re-fetched and current, with the Erdős record, the OpenATP result, and the FormalQualBench comparison unchanged.

## See also

- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins
- [Math Inc. Gauss](../math-inc-gauss/index.md) - the rival harness whose FormalQualBench numbers target Aristotle directly
- [AlphaProof](../alphaproof/index.md) - the stronger-provenance, not-runnable alternative
- [deepeval](../../evaluation-review/deepeval/index.md) - the same "who judges the output" question in software evals

## References

- https://aristotle.harmonic.fun/ - the product page: the "Code, proven correct" positioning, the C and Verilog surfaces, the on-prem story, and the consumption-pricing framing (fetched 200, 2026-11-07)
- https://www.harmonic.fun/news/aristotle-software-hardware-verification - the October 27, 2026 expansion announcement: the C and Verilog scope, the case studies, self-serve consumption pricing, and enterprise on-prem (fetched 200, 2026-11-07)
- https://math.inc/opengauss - the rival claim that OpenGauss beats Aristotle on FormalQualBench
- https://math.inc/formalqualbench - Aristotle's unaudited 6/23 column, the comparator exclusion, and the FATE-adjacent cost table
- https://www.erdosproblems.com/forum/thread/124 - the Lean-checked Erdős #124 result, the version-of-the-problem debate, and Tao's tooling experiments
- https://hn.algolia.com/api/v1/search?query=Harmonic%20Aristotle&tags=story&hitsPerPage=10 - community footprint and the independent OpenATP benchmark numbers
- https://www.harmonic.fun/news/mathematician-sponsorships - the $1,000,000 Mathematician Sponsorships announcement (2026-01-22) and the application link
- https://www.harmonic.fun/news/series-c - the $120 million Series C at a $1.45 billion valuation (November 2025)
