---
title: Bernstein
created: 2026-10-06
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, deterministic-scheduling, policy-as-code, worktrees, audit]
readability: 3
audience_notes: >
  Engineers who want parallel coding agents under a deterministic scheduler with policy gates and an auditable run record, and who can weigh a beta tool against that promise.
  Assumes you know git worktrees and what a merge gate is.
---

**Bernstein is the deterministic-scheduler answer to LLM-in-the-loop orchestration: policy as code, a planner-free coordination loop, parallel agents in worktrees behind merge gates, and a run record you can verify offline, at Apache-2.0 and v3.21.0.**

## What it is

Bernstein is a Python 3.12+ orchestration and governance layer for AI agents from sipyourdrink-ltd: you write the policy (who may do what, what needs approval, what must be recorded), and a plain-Python scheduler with no model in the coordination loop runs agents in parallel, gates their output, and records every step.
Coding tasks each get their own git worktree behind merge gates, artifact tasks (reports, datasets, audit evidence packs) get a workspace under `.sdd/workspaces/` and complete on signed lineage receipts instead of commits.
A replay journal records every run, a lineage spine records every lineage-bearing step, and an opt-in HMAC-chained audit log produces receipts a reviewer verifies offline without rerunning anything.
It ships as a CLI, TUI, and web UI on PyPI (`bernstein`), drives 50-plus CLI agent adapters plus a generic `--prompt` wrapper, and offers cluster mode and an air-gap install profile with no SaaS hop.

## Status

Active and fast-releasing: 1,404 stars, 30 contributors, and a push on 2026-10-06 as of 2026-10-06, created 2026-03-22, with v3.21.0 published 2026-10-05 (GitHub API, PyPI, as of 2026-10-06).

[![Star History Chart](https://api.star-history.com/chart?repos=sipyourdrink-ltd/bernstein&type=date&legend=top-left)](https://www.star-history.com/?repos=sipyourdrink-ltd%2Fbernstein&type=date&legend=top-left)

The README calls the project beta and solo-maintained, and warns that minor versions may change interfaces, so pinning is advised.
**The community footprint is thin for the ambition: a 1-point Show HN in August 2026 and a 3-point story in May are the whole independent record, and the strongest third-party coverage is a commercial roundup (Augment Code, updated 2026-08-12) whose hands-on test praised the design, calling it the most architecturally interesting tool in its survey and noting its Janitor verification caught a type error before the merge queue.**
The governance framing puts it next to control-plane products, but its unit of work is the parallel coding-agent session in a worktree, which is this category's daily work.

## Strengths

- The no-LLM coordination loop makes runs reproducible: replay yesterday's plan and get the same task graph, with non-determinism surfacing as a hash mismatch at the exact step.
- Verification is an artifact, not a vibe: merge gates, lineage receipts, and the opt-in HMAC audit chain are checkable offline after the fact.
- Broad and local: 50-plus agent adapters, file-based state, no SaaS dependency, and an air-gap profile for restricted environments.

## Cautions

- Beta software with a version number that counts releases, not maturity, and a solo maintainer by its own description.
- Deterministic scheduling buys reproducibility by giving up LLM-driven planning flexibility, the same trade LoopTroop and Crewplane make, and teams that want an LLM to decompose goals will find the planner layer thin.
- The 1.4k-star count has almost no independent discussion behind it, so the governance claims rest on the project's own documentation and one commercial review.

## Pricing

Free and open source under Apache-2.0, installable from PyPI with `uv tool install bernstein` or `pipx`; no hosted tier or paid plan exists.

## Compared to

- [Foremerge](../foremerge/index.md): the other deterministic layer above Git, but advisory (it flags intent collisions) where Bernstein enforces policy and gates merges.
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md): the adversarial-verification counterpart; both distrust worker self-report, but Bernstein encodes the distrust in policy and receipts while TPO encodes it in a second agent's refutation attempt.
- [Crewplane](../crewplane/index.md): the closest determinism-first runner; Crewplane versioning Markdown runs, Bernstein adding policy gates, lineage, and audit to the same instinct.

## Bottom line

Recommended for teams that must be able to prove what their agents did, after the fact, from artifacts alone, and accept beta-grade tooling to get it.
Not for teams that want LLM-driven planning, a GUI-first experience, or a project with community depth behind it.

## Changes

- 2026-10-06 - Created after the entrant scan surfaced the active v3.21.0 repository with no note in the section.
- 2026-10-07 - Added the sipyourdrink-ltd/bernstein star history chart to the Status section.

## See also

- [Foremerge](../foremerge/index.md) - the advisory deterministic-coordination counterpart
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md) - the other verification-first design in the category
- [Crewplane](../crewplane/index.md) - the Markdown-run determinism instinct Bernstein extends
- [Agent Swarm](../agent-swarm/index.md) - the intake-to-PR lead/worker platform, LLM-led where Bernstein is policy-led

## References

- https://github.com/sipyourdrink-ltd/bernstein - repository, README positioning, status banner, license, and stars (GitHub API, as of 2026-10-06)
- https://bernstein.run - the project website and tagline
- https://docs.bernstein.run/en/latest/ - documentation root (install, glossary, known limitations)
- https://pypi.org/project/bernstein/ - PyPI version 3.21.0 and summary
- https://www.augmentcode.com/tools/open-source-agent-orchestrators - the hands-on commercial roundup with the Janitor verification anecdote
- https://hn.algolia.com/api/v1/search?query=bernstein.run - the near-empty HN record grounding the thin-footprint claim (one 1-point Show HN, 2026-08-15)
