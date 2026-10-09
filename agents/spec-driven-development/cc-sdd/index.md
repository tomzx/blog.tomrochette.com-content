---
title: cc-sdd
created: 2026-10-06
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, agent-skills, multi-agent, open-source]
readability: 3
audience_notes: >
  Engineers who want a spec-driven workflow installed as skills in the agent they already run, and who wonder what the Kiro-style flow looks like when it is portable.
  Assumes you know what a slash command and a phase gate are.
---

cc-sdd is a solo-maintained, MIT-licensed npm installer that sets up a 17-skill spec-driven development workflow inside eight coding agents' native skill systems, from `/kiro-discovery` routing through long-running autonomous implementation with per-task independent review.

**cc-sdd turns spec-driven development from a CLI you run into a skill set your agent already speaks, and its per-task fresh-context reviewer is an oversight primitive none of the human-gated columns in this category attempt.**

## What it is

An npm package (`npx cc-sdd@latest`, MIT, 14 UI languages) that installs the same 17 skills into Claude Code, Codex, Cursor, Copilot, Devin, OpenCode, Gemini CLI, and Antigravity (the first two stable, the rest beta), using each host's native subagents when available and inline review otherwise.
The workflow opens with `/kiro-discovery`, which routes new work to extending a spec, implementing with no spec, one new spec, or a multi-spec decomposition (`/kiro-spec-batch` writes specs by dependency wave with cross-spec review), so ceremony is a routing outcome rather than a fixed ritual.
Specs are boundary-first: `design.md` carries a File Structure Plan, tasks carry `_Boundary:_` and `_Depends:_` annotations, and review checks boundary violations rather than style.
`/kiro-impl` then runs one task per iteration, each behind a fresh implementer doing TDD, an independent reviewer running `git diff` and the test suite, and an auto-debug pass bounded to two rounds; `/kiro-validate-impl` closes with a GO, NO-GO, or MANUAL_VERIFY_REQUIRED verdict.
Made by Gota (gotalab), an agentic-AI engineer in Japan; the project is Kiro-inspired and keeps existing Kiro specs compatible and portable.

## Status

Established and mid-scale, with adoption that bypassed Hacker News entirely.
As of 2026-10-08: 3,709 stars, 290 forks, created 2025-07-17, pushed 2026-09-23, release v3.1.0 (2026-09-23, the same day as the last push), 24,272 npm downloads last month, MIT.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=gotalab/cc-sdd&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=gotalab/cc-sdd&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=gotalab/cc-sdd&type=date&legend=top-left" />
</picture>

The v3.0 rework (spring 2026) moved everything to Agent Skills and added the autonomous implementation loop; the older `/kiro:*` command modes still install but are deprecated.
**No significant Hacker News thread exists, so like OpenSpec its traction is measured in installs, and its claims rest on its own documentation.**

## Strengths

- Per-task independent review with a fresh-context reviewer, plus a completion gate that demands fresh evidence before any success claim, is structural oversight rather than a convention the agent can skip.
- Discovery routing makes "no spec needed, implement directly" a first-class outcome, which is the direct answer to the fixed-ceremony critique this category keeps earning.
- One install covers eight agents, and Kiro spec compatibility gives AWS-IDE teams an exit path instead of a lock-in.
- Learnings propagate: cross-cutting findings land in `## Implementation Notes` and are injected into later task prompts.

## Cautions

- Solo maintainer, and the v3.0 rewrite was a ground-up rework, so expect the same vocabulary churn OpenSpec went through.
- Only Claude Code and Codex integrations are stable; the other six hosts are beta and inline fallbacks, so a skill installation alone does not prove independent review is happening.
- The `kiro-` prefix on every command borrows AWS's brand for a project AWS does not maintain, which will confuse more than it signals.
- The category-level waterfall critique (Marmelab's "waterfall strikes back") applies here too, and the project's own when-not-to-use list (solo work, prototypes, true vibe coding) is the boundary where that critique wins.

## Pricing

Free and open source under MIT.
No paid tier exists.

## Compared to

- [GitHub Spec Kit](../spec-kit/index.md): the movement root scaffolds conventions with a Python CLI; cc-sdd installs skills with review machinery and no CLI runtime, and routes small work around the ceremony.
- [OpenSpec](../openspec/index.md): the delta-ledger alternative; OpenSpec versions the spec itself, cc-sdd versions task state and review evidence per task.
- [BMad Method](../bmad-method/index.md): the other skill-and-role workflow; BMad brings agile roles and retrospectives, cc-sdd brings a review pipeline and stays inside one agent host per run.

## Bottom line

**Recommended for teams running Claude Code or Codex who want phase-gated specs plus per-task independent review without adopting a whole method's vocabulary.**
Not for solo prototype work (its own docs say so), and not for the six beta hosts if independent review is the reason you are choosing it.
The disagreeable claim I will defend: a fresh-context reviewer per task is a stronger oversight primitive than any human phase gate in this category, because review attention scales with task count instead of competing for one human's patience, and the columns that gate on humans have been selling attention as if it were free.

## Changes

- 2026-10-06 - Created from the entrant-resolution run, profiling gotalab/cc-sdd as the category's first installable skill-set column.
- 2026-10-07 - Added the gotalab/cc-sdd star history chart to the Status section.

## See also

- [Kiro](../../surfaces/kiro/index.md) - the AWS IDE whose spec workflow cc-sdd replicates as portable skills
- [GitHub Spec Kit](../spec-kit/index.md) - the movement root it offers a skill-based alternative to
- [OpenSpec](../openspec/index.md) - the brownfield delta-ledger alternative
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/gotalab/cc-sdd - repository, README: workflow, hosts, languages, licensing (3,709 stars as of 2026-10-08)
- https://raw.githubusercontent.com/gotalab/cc-sdd/main/README.md - the v3.0 skills-mode scope and install surface
- https://raw.githubusercontent.com/gotalab/cc-sdd/main/docs/guides/why-cc-sdd.md - the spec-as-contract philosophy and the when-not-to-use list
- https://raw.githubusercontent.com/gotalab/cc-sdd/main/docs/guides/skill-reference.md - the 17-skill surface and the /kiro-impl dispatch internals
- https://api.npmjs.org/downloads/point/last-month/cc-sdd - 24,272 downloads last month, fetched 2026-10-06
- https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html - the category-level critique, the critical source
- https://hn.algolia.com/api/v1/search?query=cc-sdd&tags=story - the missing HN footprint, checked 2026-10-06
