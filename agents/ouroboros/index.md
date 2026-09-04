---
title: Ouroboros
created: 2026-08-30
updated: 2026-09-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, verification, self-improving-agents, open-source]
readability: 3
audience_notes: >
  Engineers who want coding agents to produce verified software from vague briefs, and who worry about agents grading their own homework.
  Assumes you know what a spec, an acceptance gate, and an MCP server are.
---

Ouroboros is an MIT-licensed Python "Agent OS" that turns a vague brief into verified code by running a Socratic interview, freezing an immutable spec, executing through one of 13 coding-agent runtimes, and verifying the result with a three-stage gate whose grading commands and expected outputs are withheld from the worker agent.
Facts below verified as of 2026-09-04.

**Ouroboros earns its anti-cheating tagline architecturally, not rhetorically: the worker's success contract omits the grading command and expected result, and the first verification stage is LLM-free, which is a cleaner separation than most self-improving agent systems attempt.**

## What it is

A local-first workflow layer around existing coding agents: Interview produces a Seed (an immutable spec with an ambiguity gate at 0.2 or lower before any code is written), Execute decomposes work through a Double Diamond process, Evaluate runs the gate, and Evolve refines specs and accumulates reusable assets across generations within a budgeted loop (30-generation cap, stagnation detection, a three-tier cost router).
The verification gate runs outside the worker: mechanical checks first (lint, build, tests, coverage at a 70 percent default, no LLM), then a semantic LLM judge against acceptance criteria at a 0.8 threshold, then multi-model consensus voting triggered only by six conditions such as seed modification or drift above 0.3.
It drives 13 runtimes including Claude Code, Codex CLI, Copilot CLI, OpenCode, Gemini, Goose, Kiro, Pi, and Antigravity, installs as `ouroboros-ai` on PyPI or a Claude Code plugin, and ships an MCP server.
MIT, by Ouro Labs (Q00), solo-maintained with around 75 contributors.

## Status

Very young, very active: 5,768 stars, 582 forks, 66 open issues as of 2026-09-04, created 2026-01-14, pushed 2026-09-03.
Latest release v0.53.0 on 2026-09-01, with roughly 25 PyPI releases in the last seven weeks; PyPI self-labels it Beta.
**Headline results are self-reported, its Hacker News threads are self-submitted with single-digit points, and no independent evaluation exists as of 2026-09-04.**

## Strengths

- The hidden-grading design is structurally sound: separating verification from the worker contract rules out the most obvious reward hacking.
- The mechanical-first gate means a large share of acceptance needs no LLM opinion at all.
- Unusual breadth of runtime integrations with per-host install modes and live model discovery.
- Real engineering artifacts: event sourcing with full replay, lineage records, and a roadmap that labels every claim verified, planned, or conditional.

## Cautions

- The semantic judge is an LLM, and consensus voting triggers only under six conditions, so a worker tuned to satisfy a predictable judge is not fully ruled out.
- The ambiguity, drift, and similarity scores are LLM self-assessments and heuristics; the docs themselves call the thresholds defaults worth arguing with.
- Beta churn: 25 releases in seven weeks, documented breakage below specific versions, and an extras matrix with install warnings.
- The loop spends real tokens on evaluation, which is the price of the gate.

## Pricing

Free and open source under MIT, funded by GitHub Sponsors.
Enterprise offerings and a marketplace are marked conditional in the roadmap; no tiers exist today.

## Compared to

- [Hermes](../hermes/index.md): a full agent product whose self-improvement optimizes skills across general tasks; choose Ouroboros when the job is verified software from an ambiguous brief inside runtimes you already run.
- [SkillOpt](../skillopt/index.md): distills experience into one portable skill artifact behind a validation gate; choose SkillOpt for artifacts, Ouroboros for the whole loop.
- Hand-written AGENTS.md conventions: zero dependencies and fully transparent for stable repos; choose Ouroboros for one-off ambiguous tasks where you want automated gates, accepting token cost and beta churn.

## Bottom line

**Recommended for engineers who already trust one of the 13 runtimes and want spec-freeze plus hidden grading on top, in projects where verification failures cost more than evaluation tokens.**
Not for quick edits, for teams needing proven evaluation rigor, or for anyone who cannot tolerate beta-grade install friction.

## See also

- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - the category comparison this note joins
- [Fluent](../fluent/index.md) - the factory with the deterministic final Tester and learning loop
- [HAR](../har/index.md) - the fleet harness with deterministic verification and evidence trails
- [GitHub Spec Kit](../spec-kit/index.md) - the spec-first layer without the evolution loop
- [SkillOpt](../skillopt/index.md) - the artifact-level counterpart in self-improvement

## References

- https://github.com/Q00/ouroboros - repository, pitch, runtimes, install, license
- https://ouroboros.page/learn/en/evaluate/ - the three-stage gate and the grading-outside-the-worker design
- https://pypi.org/project/ouroboros-ai/ - release cadence and beta status
- https://ouroboros.page/roadmap/ - claim-status policy and the conditional enterprise plans
- https://ouroboros.page/ - official docs and Ouro Labs attribution
- https://hn.algolia.com/api/v1/search?query=Q00%2Fouroboros&tags=story - the thin independent-discussion footprint this note records
