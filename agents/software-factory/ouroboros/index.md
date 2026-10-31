---
title: Ouroboros
created: 2026-08-30
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, software-factory, verification, self-improving-agents, open-source]
readability: 3
audience_notes: >
  Engineers who want coding agents to produce verified software from vague briefs, and who worry about agents grading their own homework.
  Assumes you know what a spec, an acceptance gate, and an MCP server are.
---

Ouroboros is an MIT-licensed Python "Agent OS" that turns a vague brief into verified code by running a Socratic interview, freezing an immutable spec, executing through one of 14 coding-agent runtimes, and verifying the result with a three-stage gate whose grading commands and expected outputs are withheld from the worker agent.

**Ouroboros earns its anti-cheating tagline architecturally, not rhetorically: the worker's success contract omits the grading command and expected result, and the first verification stage is LLM-free, which is a cleaner separation than most self-improving agent systems attempt.**

## What it is

A local-first workflow layer around existing coding agents: Interview produces a Seed (an immutable spec with an ambiguity gate at 0.2 or lower before any code is written), Execute decomposes work through a Double Diamond process, Evaluate runs the gate, and Evolve refines specs and accumulates reusable assets across generations within a budgeted loop (30-generation cap, stagnation detection, a three-tier cost router).
The verification gate runs outside the worker: mechanical checks first (lint, build, tests, coverage at a 70 percent default, no LLM), then a semantic LLM judge against acceptance criteria at a 0.8 threshold, then multi-model consensus voting triggered only by six conditions such as seed modification or drift above 0.3.
It drives 14 runtimes including Claude Code, Codex CLI, Copilot CLI, OpenCode, Gemini, Goose, Kiro, Pi, OMP, and Antigravity, installs as `ouroboros-ai` on PyPI or a Claude Code plugin, and ships an MCP server.
The README now frames a three-repo Agent OS stack around this core: Ouro-labs/ourocode (a terminal shell, 22 stars) and Ouro-labs/ouroboros-plugins (a plugin contract, MIT, 16 stars), per the PyPI page and the GitHub API as of 2026-10-11.
MIT, by Ouro Labs (Q00), solo-maintained with around 80 contributors.

## Status

Very young, very active: 6,214 stars as of 2026-10-13, 631 forks and 105 open issues as of 2026-10-21, created 2026-01-14, pushed 2026-10-30.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Q00/ouroboros&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Q00/ouroboros&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Q00/ouroboros&type=date&legend=top-left" />
</picture>

Latest release v0.59.9 on 2026-10-25 (routine verification, provider, and updater fixes), after the v0.59.8 patch of 2026-10-23 (artifact-store path safety, interview, and MCP fixes), the v0.59.4 through v0.59.7 patches of 2026-10-21 to 2026-10-23 (each keeping only sourced Seed content in the worker prompt and tightening context-pack manifest reporting), the v0.59.0 minor of 2026-10-19 (the self-answer investigates the repository and binds only checked evidence), the v0.58.0 minor of 2026-10-17 (only confirmed content binds the Seed, and the verify gate needs a signal), and the v0.57.x and v0.56.x lines before them; PyPI self-labels it Beta and carries 0.59.9 as well.
**Headline results are self-reported, its Hacker News threads are self-submitted with single-digit points, and no independent evaluation exists as of 2026-10-31.**
An unrelated arXiv paper shares the name (a self-developing coding agent, arXiv 2608.08311), which muddies coverage searches for this project.

## Strengths

- The hidden-grading design is structurally sound: separating verification from the worker contract rules out the most obvious reward hacking.
- The mechanical-first gate means a large share of acceptance needs no LLM opinion at all.
- Unusual breadth of runtime integrations with per-host install modes and live model discovery.
- Real engineering artifacts: event sourcing with full replay, lineage records, and a roadmap that labels every claim verified, planned, or conditional.

## Cautions

- The semantic judge is an LLM, and consensus voting triggers only under six conditions, so a worker tuned to satisfy a predictable judge is not fully ruled out.
- The ambiguity, drift, and similarity scores are LLM self-assessments and heuristics; the docs themselves call the thresholds defaults worth arguing with.
- Beta churn: 21 releases in the seven weeks to 2026-10-07, documented breakage below specific versions, and an extras matrix with install warnings.
- The loop spends real tokens on evaluation, which is the price of the gate.

## Pricing

Free and open source under MIT, funded by GitHub Sponsors.
Enterprise offerings and a marketplace are marked conditional in the roadmap; no tiers exist today.

## Compared to

- [Hermes](../../assistant-runtimes/hermes/index.md): a full agent product whose self-improvement optimizes skills across general tasks; choose Ouroboros when the job is verified software from an ambiguous brief inside runtimes you already run.
- [SkillOpt](../../skills/skillopt/index.md): distills experience into one portable skill artifact behind a validation gate; choose SkillOpt for artifacts, Ouroboros for the whole loop.
- Hand-written AGENTS.md conventions: zero dependencies and fully transparent for stable repos; choose Ouroboros for one-off ambiguous tasks where you want automated gates, accepting token cost and beta churn.

## Bottom line

**Recommended for engineers who already trust one of the 14 runtimes and want spec-freeze plus hidden grading on top, in projects where verification failures cost more than evaluation tokens.**
Not for quick edits, for teams needing proven evaluation rigor, or for anyone who cannot tolerate beta-grade install friction.

## Changes

- 2026-08-30 - Created as a software-factory note on the hidden-grading verification loop, with a banned term caught and reworded the same day.
- 2026-09-12 - Updated the count of supported coding-agent runtimes to 14.
- 2026-09-25 - Recorded the v0.54.5 release (2026-09-20) and refreshed counts.
- 2026-09-27 - Recorded the v0.54.6 release (2026-09-25) and refreshed counts.
- 2026-09-29 - Recorded the v0.55.0 release (2026-09-28) and refreshed counts (6,130 stars, 617 forks, 95 open issues).
- 2026-10-02 - Recorded the v0.55.3 release (2026-09-30) and refreshed counts (6,165 stars, 620 forks, 87 open issues).
- 2026-10-03 - Recorded the v0.55.4 release (2026-10-02) and refreshed counts (6,174 stars, 622 forks, 88 open issues).
- 2026-10-07 - Added the Q00/ouroboros star history chart to the Status section.
- 2026-10-07 - Recorded the v0.55.5 and v0.55.6 releases (both 2026-10-06) and refreshed counts; noted the same-named arXiv project that muddies coverage searches.
- 2026-10-09 - Recorded the three-repo Agent OS stack framing (Ouro-labs/ourocode shell and Ouro-labs/ouroboros-plugins around the Q00/ouroboros kernel); re-verified status otherwise unchanged, with v0.55.6 still the newest release and no PyPI movement since 2026-10-06.
- 2026-10-13 - Recorded the v0.55.7 release (2026-10-12, GitHub and PyPI) and refreshed counts (6,211 stars, 100 open issues, pushed 2026-10-12).
- 2026-10-16 - Recorded the v0.56.0 minor release (2026-10-15, deciding gates record by default) after the v0.55.8 and v0.55.9 patches (2026-10-14).
- 2026-10-17 - Recorded the v0.57.0 minor (2026-10-16, brownfield registry reads with BM25 repo ranking, opt-in requester command, compressed onboarding skills) and the v0.57.1 patch (2026-10-17, both on GitHub and PyPI, still Beta); pushed date refreshed.
- 2026-10-21 - Recorded the train from v0.57.1 to v0.59.3 (2026-10-20, GitHub and PyPI): the v0.58.0 minor binds only confirmed content to the Seed and requires a signal for the verify gate, and the v0.59.0 minor makes the self-answer investigate the repository and bind only checked evidence; pushed date refreshed.
- 2026-10-23 - Recorded the v0.59.4 through v0.59.7 patches (2026-10-21 to 2026-10-23, GitHub and PyPI, sourcing-gated Seed content in the worker prompt and context-pack manifest reporting); pushed date refreshed.
- 2026-10-25 - Recorded the v0.59.8 and v0.59.9 patches (2026-10-23 and 2026-10-25, GitHub and PyPI, routine fixes with no design change); pushed date refreshed.
- 2026-10-31 - Rotation re-verification: every cited URL re-fetched (repository via the API, the evaluate and roadmap docs, the docs home, the PyPI project page, the same-named arXiv paper, and the HN search) and all claims confirmed, including the README's 14-runtime roster, v0.59.9 still the newest release on GitHub and PyPI, the three-stage gate's thresholds, the conditional enterprise and marketplace horizons, and the single-digit self-submitted threads; pushed date refreshed, no material change.

## See also

- [Software Factory Feature Matrix](../software-factory-feature-matrix/index.md) - the category comparison this note joins
- [Fluent](../fluent/index.md) - the factory with the deterministic final Tester and learning loop
- [HAR](../har/index.md) - the fleet harness with deterministic verification and evidence trails
- [GitHub Spec Kit](../../spec-driven-development/spec-kit/index.md) - the spec-first layer without the evolution loop
- [SkillOpt](../../skills/skillopt/index.md) - the artifact-level counterpart in self-improvement

## References

- https://github.com/Q00/ouroboros - repository, pitch, runtimes, install, license
- https://ouroboros.page/learn/en/evaluate/ - the three-stage gate and the grading-outside-the-worker design
- https://pypi.org/project/ouroboros-ai/ - release cadence and beta status
- https://ouroboros.page/roadmap/ - claim-status policy and the conditional enterprise plans
- https://ouroboros.page/ - official docs and Ouro Labs attribution
- https://arxiv.org/abs/2608.08311 - the unrelated same-named coding-agent paper that complicates coverage searches
- https://hn.algolia.com/api/v1/search?query=Q00%2Fouroboros&tags=story - the thin independent-discussion footprint this note records
