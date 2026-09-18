---
title: Anthropic Claude mathematical research
created: 2026-09-13
updated: 2026-09-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, anthropic, mathematics, formal-verification]
readability: 3
audience_notes: >
  Engineers who run multi-agent coding workflows and want to see the same tooling pointed at research mathematics.
  Assumes you know what Claude Code, subagents, and Lean are.
---

Anthropic's research-math program points unreleased Claude research models at open mathematics through Claude Code, with subagent fleets doing the work and Lean plus named human experts as the trust gates.
Facts below verified as of 2026-09-18.

**The frontier research loop is now ordinary engineering tooling: one staff member, a coding agent, about sixty subagents, thousands of shell commands, and a compiler as the judge.**

## What it is

A series of Anthropic Science results produced by Claude models working in a Claude Code multi-agent harness, validated and published with artifacts.
On August 10, 2026, Anthropic reported that an unreleased research version of Claude, asked to take a real stab at the Riemann hypothesis, failed at the hypothesis itself but raised the lower bound for the share of zeta zeros on the critical line from 41.6 to 67.2 percent.
The run took two sessions and 31 million output tokens: after 650 failed ideas, Claude spent a day and a half coordinating about sixty subagents that ran 2,400 shell commands and hundreds of Python scripts, checked against known zeta zeros, refereed one another, and downloaded 54 arXiv papers to confirm novelty.
Anthropic mathematicians Levent Alpöge and Ralph Furman validated the result, external experts Brian Conrey and Dan Goldston reviewed it on short notice, and the Lean formalization passes the comparator checker in the public anthropics/formal-math repository.
On September 4, 2026, Anthropic published the first complete computer-checked proof of Fermat's Last Theorem: 11 days, largely autonomous, 13 million lines of Lean, 30,300 theorems proved along the way, about six billion output tokens from an internal research model described as roughly comparable to Claude Fable 5.1, reviewed by Kevin Buzzard.
The FLT effort succeeded only after switching to Prove2Me, a platform maintaining a directed acyclic graph of theorem statements so parallel agents stop losing track of project state.
Anthropic's own zeta post footnote also credits a Claude model with disproving the Jacobian conjecture, which press coverage attributes to Fable 5 via Alpöge's announcement.

## Status

Very active, with three major publications in five weeks as of 2026-09-18.
The models are unreleased research versions, so the loop is not reproducible by outsiders today.
The artifacts are public and machine-checkable: the formal-math repository (241 stars as of 2026-09-18) is Apache-2.0 with pinned toolchains and CI that builds with no `sorry` outside trusted statement files.
Community footprint is strong, with the zeta result drawing a 282-point Hacker News discussion.
A three-person experiment formalized Vinogradov's three primes theorem in three days on consumer Claude Max plans, which is the first version of this loop an outside engineer could actually copy.

## Strengths

- Every headline result ships with a machine-checkable artifact, not just a blog post.
- The methodology notes read like engineering postmortems: failed attempts, state loss, and the DAG fix are documented.
- Novelty checking is built into the loop, including downloading and reading prior work before claiming a result.
- Failures still contributed: about 7 percent of the final FLT lines came from abandoned attempts.

## Cautions

- The results are vendor-validated first and community-validated slowly, and the zeta bound's external review was two experts on short notice.
- A counterexample-style disproof can be a weak result: mathematician Andrew Blumberg called the Jacobian counterexample unilluminating even while granting the achievement.
- The encouraging-prompt detail (a non-mathematician telling Claude to keep going) is charming but also a reminder that the model's own calibration failed here.
- Everything comes from the vendor's own write-ups; independent reproduction awaits the released models.

## Pricing

The published artifacts are free under Apache-2.0.
The compute is internal and not priced publicly, and Anthropic sells the ingredients (Claude subscriptions plus science grant programs) rather than the loop itself.

## Compared to

- [Math Inc. Gauss](../math-inc-gauss/index.md): a purpose-built autoformalization agent with an open harness and audited benchmarks; choose Gauss for formalization throughput, the Claude loop for genuinely new mathematics.
- [OpenAI for Science](../openai-for-science/index.md): the rival lab program, currently defined by a disputed Navier-Stokes claim; Anthropic's publish-the-artifacts-and-invite-review pattern is the sharper contrast.
- [Claude Code](../../harnesses/claude-code/index.md): the harness underneath, which you can run today with your own subagent fleets.

## Bottom line

**Recommended for anyone orchestrating long-horizon multi-agent work: this is the best-documented public example of subagent fleets, DAG coordination, and verification gates applied to real research.**
Not for anyone expecting to rerun the exact loops, since the models are unreleased as of 2026-09-18.

## Changes

- 2026-09-13 - Created as the Anthropic member of the new Automated research category.

## See also

- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins
- [Math Inc. Gauss](../math-inc-gauss/index.md) - the dedicated autoformalization agent and its comparator-audited benchmark
- [OpenAI for Science](../openai-for-science/index.md) - the rival lab loop and its credit dispute
- [Ouroboros](../../software-factory/ouroboros/index.md) - the same hidden-grading pattern applied to software instead of proofs
- [Claude Code](../../harnesses/claude-code/index.md) - the harness the loop runs on

## References

- https://www.anthropic.com/research/riemann-zeta - the zeta zero bound result, subagent methodology, validation chain, and the Jacobian footnote
- https://www.anthropic.com/research/formalizing-fermats-last-theorem - the FLT formalization, Prove2Me DAG platform, token costs, and Buzzard review
- https://github.com/anthropics/formal-math - the public Apache-2.0 Lean formalizations, Palomar/comparator CI, and the Alpoge-Furman arXiv reference
- https://mashable.com/tech/anthropic-fable-5-disproves-jacobian-conjecture - press account of the Jacobian disproof and the skeptical expert read
- https://hn.algolia.com/api/v1/search?query=Anthropic%20mathematics&tags=story&hitsPerPage=20 - the community footprint, including the 282-point zeta discussion
