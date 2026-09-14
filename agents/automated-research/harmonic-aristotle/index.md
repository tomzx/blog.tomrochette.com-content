---
title: Harmonic Aristotle
created: 2026-09-13
updated: 2026-09-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, harmonic, mathematics, formal-verification]
readability: 3
audience_notes: >
  Engineers evaluating automated theorem provers and proof-carrying tooling for software verification.
  Assumes you know what Lean and a proof assistant are.
---

Aristotle is Harmonic's agentic theorem prover, sold as mathematical superintelligence applied to formal verification of software, hardware, and mathematics, and it is the one system in this category a working engineer can use today for free.
Facts below verified as of 2026-09-13.

**Aristotle's real results are machine-checkable and independent, but the benchmark fight around it shows the judging layer has become the battleground: its own vendor claims are unauditable, and its loudest rival publishes comparator-audited numbers against it.**

## What it is

A web agent at aristotle.harmonic.fun: give it an English problem and it proves and formalizes from scratch, or point it at your Lean project or code repository and it works on files directly.
The marketing leads with "the reasoning that earned IMO gold" applied to software correctness, and positions output as backed by machine-checked proof.
Harmonic also runs a $1,000,000 research grant program and accepts applications.
The company calls its category "Mathematical Superintelligence"; funding and leadership are not stated on the pages fetched for this note.

## Status

Live product, free with an account, as of 2026-09-13.
The strongest independent credential is a November 2025 result on Erdős problem #124: Aristotle produced a proof working only from the formal statement, Boris Alexeev formalized and cleaned the statement, Lean checked it, and the Erdős Problems site updated to record that a version of the problem was solved, with the community debate over exactly which version playing out in public.
Independent third-party benchmarking in July 2026 (the OpenATP project) scored Aristotle 10/10 on the FATE-H theorem set for free, at roughly twice the wall-clock time of Claude Code and Codex.
On Math Inc.'s FormalQualBench (March 2026), Aristotle solved 6 of 23 with no time limit, but those runs were not validated with the comparator tool and are excluded from the audited counts.

## Strengths

- Agentic end to end: natural language in, machine-checked proof out, or direct work inside your repository.
- The Lean-checked Erdős artifact is public and type-checkable in the browser, so the claim does not rest on Harmonic's word.
- Free access lowers the barrier to experimenting with proof agents to nearly zero.
- Harmonic claims formalization project leaders accept its code contributions without modification.

## Cautions

- The benchmark record is contested: Math Inc's comparator-audited run beat Aristotle's unaudited 6/23, and the "IMO gold reasoning" line is unverifiable marketing.
- The Erdős result solved "a version" of the problem, not the version the original authors posed, a nuance the community itself flagged.
- Closed system: no weights, no self-hosting, and a login wall between you and the agent.
- A formal statement typo it worked from made the target weaker, a reminder that autoformalization inherits upstream spec bugs.

## Pricing

Free with an account as of 2026-09-13.
Harmonic advertises a $1,000,000 research grant program; no paid tiers are published on the fetched pages.

## Compared to

- [Math Inc. Gauss](../math-inc-gauss/index.md): OpenGauss is open source, comparator-audited, and cheaper per solve on FormalQualBench; choose OpenGauss when auditability matters, Aristotle when you want a zero-setup hosted agent.
- Claude Code and Codex used as theorem provers: faster on the FATE sets but paid per token; Aristotle's free tier is the budget pick at half the speed.
- [AlphaProof](../alphaproof/index.md): DeepMind's systems are stronger published evidence but not runnable; Aristotle is weaker provenance but a usable product.

## Bottom line

**Recommended for engineers who want to feel what a proof agent is like this week, for free, with artifacts you can check.**
Not for audit-sensitive verification work as of 2026-09-13, where the comparator-audited open harness is the defensible choice.

## Changes

- 2026-09-13 - Created as the Harmonic member of the new Automated research category.

## See also

- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins
- [Math Inc. Gauss](../math-inc-gauss/index.md) - the rival harness whose FormalQualBench numbers target Aristotle directly
- [AlphaProof](../alphaproof/index.md) - the stronger-provenance, not-runnable alternative
- [deepeval](../../evaluation-review/deepeval/index.md) - the same "who judges the output" question in software evals

## References

- https://aristotle.harmonic.fun/ - the product page: agentic surfaces, IMO-gold positioning, grant program, free access
- https://math.inc/opengauss - the rival claim that OpenGauss beats Aristotle on FormalQualBench
- https://math.inc/formalqualbench - Aristotle's unaudited 6/23 column, the comparator exclusion, and the FATE-adjacent cost table
- https://www.erdosproblems.com/forum/thread/124 - the Lean-checked Erdős #124 result, the version-of-the-problem debate, and Tao's tooling experiments
- https://hn.algolia.com/api/v1/search?query=Harmonic%20Aristotle&tags=story&hitsPerPage=10 - community footprint and the independent OpenATP benchmark numbers
