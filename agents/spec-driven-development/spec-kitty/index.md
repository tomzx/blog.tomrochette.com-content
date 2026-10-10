---
title: Spec Kitty
created: 2026-10-06
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, governance, worktrees, open-source]
readability: 3
audience_notes: >
  Engineers running more than one coding agent who want review gates, audit evidence, and parallel execution around a spec workflow.
  Assumes you know what a work package and a review gate are.
---

Spec Kitty is Spec Kitty, Inc.'s MIT-licensed Python CLI for spec-driven development that keeps specs, plans, work packages, review state, and merge decisions in your repository, and runs every work package in an isolated git worktree.

**Spec Kitty is the first member of this category born as a company product around another member's workflow: it started from Spec Kit, replaced the comprehensive-spec model with change-request deltas, and sells teams the governance and audit trail the free toolkits leave as conventions.**

## What it is

A Python 3.11+ CLI (PyPI `spec-kitty-cli`, MIT, by Spec Kitty, Inc.) whose pipeline runs spec, plan, tasks, next, review, accept, merge, with mission artifacts under `kitty-specs/` and work packages moving through lifecycle lanes (planned, in_progress, for_review, approved, done).
Implementation happens in isolated git worktrees under `.worktrees/`, so parallel agents work without branch collisions, and review, accept, and merge are explicit gates with evidence attached.
A governance layer keeps runtime decisions in the repo (`spec-kitty advise`, `ask`, and `do` map operator intent through a trail model), and every completed mission generates a retrospective by default.
Slash commands or skills integrate Claude Code, Codex, Cursor, Gemini, Copilot, Windsurf, and OpenCode; the company sells demo-booked team platform access (TeamSpace, tracker sync) and training around the free CLI, and positions the whole thing as a governed software factory.

## Status

Active, company-backed, and mid-adoption.
As of 2026-10-09: 1,678 stars and 180 forks since creation on 2025-10-09, pushed 2026-10-09, MIT, stable PyPI release 3.2.7 (2026-09-09) and 3,251 PyPI downloads last month, with the 4.x release-candidate line at v4.0.0rc6 (2026-10-08), whose README says stable launch acceptance remains pending.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=spec-kitty/spec-kitty&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=spec-kitty/spec-kitty&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=spec-kitty/spec-kitty&type=date&legend=top-left" />
</picture>

The repository moved from its original Priivacy-ai org to the spec-kitty org, which GitHub's redirect confirmed this run.
**Its Hacker News footprint is one 5-point thread (January 2026), so its adoption case rests on stars, installs, and the company's own surfaces, not on independent discussion.**
Creator Robert Douglass presented the workflow at FrOSCon 2026 on 2026-08-16.

## Strengths

- Per-work-package git worktree isolation is a first-class feature here, not a pattern you assemble yourself, and no other column runs implementation this way by default.
- Review, accept, and merge are stateful gates with attached evidence, the strongest convergence machinery in this category alongside AI-DLC's audit trail.
- Specs are change requests describing the delta and code stays the source of truth, the same delta insight OpenSpec is built on.
- The founder's own comparison concedes the boundary plainly: if one developer at one keyboard is your problem, use Spec Kit.

## Cautions

- The company gravity is structural: the CLI is free, but TeamSpace, tracker sync, and training are the paid surface, the same pattern Tessl runs at larger scale.
- The 4.x line is a prerelease and PyPI shows a yanked 4.1.5 (uploaded 2026-04-15), so pin 3.2.7 until the stable launch lands.
- Adoption sits an order of magnitude under the category leaders, 3.3k PyPI downloads a month against OpenSpec's 2.45M npm downloads.
- Independent coverage is one third-party review (Hysenlabs, 2026-09-10) and that 5-point thread, so the claims rest on the project's own documentation and blog.
- The positioning wanders across its own surfaces (governed software factory, delivery control plane, doctrine-driven delivery), and the vocabulary churn this category keeps producing is already visible.

## Pricing

The CLI is free and open source under MIT.
The company sells demo-booked team platform access and training; no tiers are published as of 2026-10-06.

## Compared to

- [GitHub Spec Kit](../spec-kit/index.md): the upstream Spec Kitty broke from; Spec Kit scaffolds markdown conventions for one developer-agent pair, Spec Kitty adds lanes, worktrees, gates, and governance for teams.
- [OpenSpec](../openspec/index.md): the other delta-spec member; OpenSpec archives a ledger with no company attached, Spec Kitty wraps the delta model in execution state and a vendor.
- [GSD](../gsd/index.md): the other loop with isolation; GSD quarantines context in fresh subagents per phase, Spec Kitty isolates per work package in git worktrees with human review gates.

## Bottom line

**Recommended for teams past the one-agent stage that want parallel implementation, review gates, and an auditable record, and that accept a company product sitting on their repo's spec state.**
Not for solo work (its own docs call it overkill), and not for anyone who needs the 4.x line before its stable launch.
The disagreeable claim I will defend: two members reaching delta specs from opposite directions, OpenSpec by design and Spec Kitty by breaking from Spec Kit, is evidence that the comprehensive-spec model at Spec Kit's root is the part of this movement that will not survive, while the governance plumbing both added is the part that will.

## Changes

- 2026-10-06 - Created from the entrant-resolution run, profiling spec-kitty/spec-kitty as the category's first company-born governance column.
- 2026-10-07 - Added the spec-kitty/spec-kitty star history chart to the Status section.
- 2026-10-09 - Recorded the v4.0.0rc6 release candidate (2026-10-08) and refreshed counts.

## See also

- [GitHub Spec Kit](../spec-kit/index.md) - the upstream toolkit and the movement root
- [OpenSpec](../openspec/index.md) - the delta-ledger alternative with no company attached
- [GSD](../gsd/index.md) - the other isolation-centered loop
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/spec-kitty/spec-kitty - repository and README: pipeline, lanes, worktrees, governance layer (1,678 stars as of 2026-10-09)
- https://raw.githubusercontent.com/spec-kitty/spec-kitty/main/README.md - the supported agents, work-package model, and the 4.x prerelease notice
- https://www.spec-kitty.ai/ - the company site: control-plane positioning, demo-booked platform, no published tiers
- https://docs.spec-kitty.ai/ - the documentation site
- https://pypi.org/pypi/spec-kitty-cli/json - stable 3.2.7, MIT, Python 3.11+, release history
- https://pypi.org/pypi/spec-kitty-cli/4.1.5/json - the yanked 2026-04-15 upload grounding the 4.x caution
- https://pypistats.org/api/packages/spec-kitty-cli/recent - 3,251 downloads last month as of 2026-10-06
- https://www.spec-kitty.ai/blog/spec-kit-alternatives-why-i-built-spec-kitty-instead-of-stopping-at-githubs-toolkit - the founder's Spec Kit comparison, the primary fork-rationale source
- https://hysenlabs.com/en/projects/spec-kitty-spec-kitty - the third-party review (2026-09-10), the critical source; the page renders client-side and was read through its published search snapshot
- https://hn.algolia.com/api/v1/items/46515942 - the 5-point January 2026 thread, the thin-footprint evidence
- https://www.spec-kitty.ai/blog/robert-douglass-spec-driven-development-froscon-2026 - creator Robert Douglass's FrOSCon 2026 session
