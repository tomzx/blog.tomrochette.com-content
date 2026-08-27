---
title: "Spec Driven Development Feature Matrix"
created: 2026-08-27
updated: 2026-08-27
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, comparison, spec-driven-development, process]
readability: 3
audience_notes: >
  Engineers comparing spec-driven tooling before adopting one.
  Assumes you know what a review gate is and already run a coding agent.
---

This matrix compares the spec-driven development tools profiled in this section.
The category currently has one profiled member, so today this is a single-column scaffold rather than a comparison, and I say so plainly rather than pad it.
Everything below was verified against live sources on 2026-08-27 (member facts as of their note's 2026-08-26 verification).

**The category's real comparison is not between tools but between the toolkit and its own critique, and the matrix exists now so the moment Tessl, OpenSpec, or a Kiro port earns a note, the columns land here without a deferral.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.

## The matrix

| Feature | [GitHub Spec Kit](../spec-kit/index.md) |
| --- | --- |
| Kind | MIT process toolkit: Python CLI plus slash-command and skills templates |
| Steward | GitHub |
| Workflow steps | constitution, specify, plan, tasks, implement, converge |
| Agent neutrality | ✓ 30+ agents via plain markdown artifacts |
| Review gates | ✓ spec and plan artifacts plus converge checking code against spec |
| Extension model | presets, extensions, role-based bundles |
| Adoption | 131,489 stars in year one, v1.0.0 and v1.0.1 shipped 2026-08-21 |
| Maintenance posture | active, original creators moved on, releases de-emphasize stability |
| Pricing | free, MIT |

## Reading the matrix

**Spec Kit's single column still answers the category's core question, whether spec-first needs a product or just a convention: it is conventions plus scaffolding, no runtime, no hosting, and that lightness is why it spread across every harness at once.**

The named-but-unprofiled neighbors stay in prose until they earn notes: Tessl (the spec-driven platform), OpenSpec and the SDD CLI ecosystem (smaller toolkits), and Kiro, which ships the same workflow as a closed, metered IDE and is profiled under Surfaces.

## Choosing from the matrix

- Heterogeneous harnesses and zero license cost: Spec Kit today, the only profiled column.
- Want the workflow bundled with the editor: Kiro, accepting metered credits.
- Waiting for a second column before standardizing: reasonable, and this page is where it will appear.

## See also

- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the boards these specs eventually fill
- [Kiro](../kiro/index.md) - the spec-first IDE alternative
- [AGENTS.md](../agents-md/index.md) - the lighter convention the constitution step extends
- [Send Implementation, Not Issue](../../send-implementation-not-issue/index.md) - the corpus argument for specs plus implementation

## References

- https://github.com/github/spec-kit - workflow steps, license, integrations count
- https://github.github.io/spec-kit/ - official docs, extensions and presets
- https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/ - the launch post
- https://www.manorrock.com/blog/2026/08/21/spec_kit_turns_one.html - the anniversary post behind the maintenance-posture row
