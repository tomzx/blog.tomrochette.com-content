---
title: "Spec Driven Development Feature Matrix"
created: 2026-08-27
updated: 2026-09-24
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, comparison, spec-driven-development, process, llm=glm-5.3-flash]
readability: 3
audience_notes: >
  Engineers comparing spec-driven tooling before adopting one.
  Assumes you know what a review gate is, already run a coding agent, and can tell a repo-native toolkit from a hosted platform.
---

This matrix compares the five spec-driven development tools profiled in this section, feature by feature.

**The category splits on two axes: who owns the specs (your repo or a platform) and whether the ceremony sizes itself to the change, and the waterfall critique is the standing judge of the second axis, while the new column adds a third question, whether the steward survives their own controversy.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [BMad Method](../bmad-method/index.md) | [GitHub Spec Kit](../spec-kit/index.md) | [GSD](../gsd/index.md) | [OpenSpec](../openspec/index.md) | [Tessl](../tessl/index.md) |
| --- | --- | --- | --- | --- | --- |
| Kind | method plus agent workflows, npm install | Python CLI plus slash-command templates | npm command-and-prompt framework, multi-runtime, ecosystem growing around the loop | spec toolkit CLI, npm install | hosted platform, thin CLI |
| Steward | BMad Code, LLC | GitHub | original archived at TÂCHES (gsd-build), active as Open GSD community | Fission AI | Tessl (Podjarny), $125M raised |
| License | ✓ MIT | ✓ MIT | ✓ MIT | ✓ MIT | ✗ closed platform |
| Artifact model | briefs, specs, architecture carried forward | constitution, spec, plan, tasks files | milestone state persisted as STATE.md, CONTEXT.md, PLAN.md; heavy work in fresh-context subagents | delta proposals archived into a living ledger | specs live on the platform |
| Workflow entry | `bmad-build` with right-sized depth | `/speckit-constitution` then specify | `/gsd-new-project` or `/gsd-onboard`, then discuss-plan-execute-verify-ship per milestone | `/opsx:propose` then apply and archive | web workflow |
| Ceremony sizing | ✓ right-sizes to the change | ✗ fixed ceremony | ~ same five-step loop each milestone, lighter quick-task mode | ~ fixed but light | ? not verified |
| Brownfield support | ✓ establish-context path | ~ not the primary case | ✓ `/gsd-onboard` for existing repos | ✓ explicit design goal | ? not verified |
| Convergence checking | ✓ verify and learn loop | ✓ converge step | ✓ verify phase walks the build before done | ~ archive keeps ledger current | ? not verified |
| Unattended execution | ✓ BMad Loop module | ✗ | ~ parallel executor waves, human verify step, gsd-loop works a GitHub queue | ✗ | ? not verified |
| Adoption | about 53k stars | about 138k stars | original archived at 64.5k stars; successor 9.7k stars, 40.6k npm downloads a month | about 70k stars, 1.8M npm downloads a month | 24-point raise thread, thin OSS surface |
| Pricing | free | free | free | free | free tier plus Team at $100 per month, Enterprise custom |

## Reading the matrix

**The license and steward rows tell the ownership story: four repo-native MIT toolkits against one closed, funded platform, and the free tools set the price anchor at zero while Tessl spends $125M betting specs are rentable.**
The adoption row inverts the funding row, which is the tension to watch.
GSD adds the stewardship question the category had not faced: the archived original out-stars every column except Spec Kit, and its 9.6k-star successor is rebuilding trust in public.

**Ceremony sizing is the design axis the waterfall critique created: only BMad sends small changes straight to build, and the artifact-first tools pay for their simplicity with fixed ceremony (GSD at least ships a lighter quick-task mode).**
If your changes are mostly small, that row alone picks your column.

**Brownfield is the sleeper row: OpenSpec is explicitly built for existing code, BMad has an establish-context path, GSD's onboard command covers it, and spec-kit's scaffolding still assumes a fresher repo than most of us have.**

## Choosing from the matrix

- Existing codebase, want the spec ledger to stay current: OpenSpec.
- Want a whole delivery process with roles and retrospectives: BMad Method.
- Heterogeneous org, zero cost, constitution ceremony acceptable: Spec Kit.
- Want a phase loop that quarantines heavy work in fresh-context subagents: GSD, accepting the young successor's governance.
- Want specs as a managed product and accept portability questions: Tessl.

## Changes

- 2026-08-27 - Created as a single-column Spec Kit scaffold.
- 2026-08-27 - Rebuilt to four columns (BMad, OpenSpec, Spec Kit, Tessl) across the ownership and ceremony-sizing axes.
- 2026-09-16 - Refreshed the Spec Kit adoption cell to about 137k stars after the v1.0.7 release.
- 2026-09-16 - Extended from four to five columns with GSD (the archived get-shit-done lineage plus the active gsd-core successor), inserted alphabetically, every row gaining a cell, and the reading prose extended to the stewardship question.
- 2026-09-21 - Refreshed the GSD and OpenSpec adoption cells after their star and npm-download counts moved.
- 2026-09-24 - Removed the verification preamble line on owner request.

## See also

- [Task Management Feature Matrix](../../task-management/task-management-feature-matrix/index.md) - the boards these specs eventually fill
- [Kiro](../../surfaces/kiro/index.md) - the spec-first IDE, the closed alternative on the editor axis
- [AGENTS.md](../../protocols/agents-md/index.md) - the lighter convention all of these extend
- [Send Implementation, Not Issue](../../../send-implementation-not-issue/index.md) - the corpus argument for specs plus implementation

## References

- https://github.com/bmad-code-org/BMAD-METHOD - loop, modules, licensing for the BMad column
- https://github.com/Fission-AI/OpenSpec - opsx workflow and philosophy for the OpenSpec column
- https://github.com/github/spec-kit - workflow steps and integrations for the Spec Kit column
- https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html - the third-party analysis covering Kiro, Spec Kit, and Tessl
- https://www.tessl.io/blog/announcing-our-series-a-for-ai-native-software-development - the raise grounding the Tessl column
- https://api.npmjs.org/downloads/point/last-month/@fission-ai/openspec - the OpenSpec install velocity
- https://github.com/open-gsd/gsd-core - the successor loop, installer, and runtimes for the GSD column
- https://api.github.com/repos/open-gsd/gsd-core - successor stars and dates as of 2026-09-21
- https://api.github.com/repos/gsd-build/get-shit-done - the archived original, 64,514 stars
- https://opengsd.net/origin - the origin credit acknowledging the broken chapter
- https://blakewatson.com/journal/i-used-claude-code-and-gsd-to-build-the-accessibility-tool-ive-always-wanted/ - the 2026-07-31 update grounding the successor transition
- https://api.npmjs.org/downloads/point/last-month/@opengsd/gsd-core - the successor's install velocity
