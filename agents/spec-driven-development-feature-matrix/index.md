---
title: "Spec Driven Development Feature Matrix"
created: 2026-08-27
updated: 2026-08-30
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, comparison, spec-driven-development, process, llm=glm-5.3-flash]
readability: 3
audience_notes: >
  Engineers comparing spec-driven tooling before adopting one.
  Assumes you know what a review gate is, already run a coding agent, and can tell a repo-native toolkit from a hosted platform.
---

This matrix compares the four spec-driven development tools profiled in this section, feature by feature.
Everything below was re-verified against live sources on 2026-08-30.

**The category splits on two axes: who owns the specs (your repo or a platform) and whether the ceremony sizes itself to the change, and the waterfall critique is the standing judge of the second axis.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [BMad Method](../bmad-method/index.md) | [GitHub Spec Kit](../spec-kit/index.md) | [OpenSpec](../openspec/index.md) | [Tessl](../tessl/index.md) |
| --- | --- | --- | --- | --- |
| Kind | method plus agent workflows, npm install | Python CLI plus slash-command templates | spec toolkit CLI, npm install | hosted platform, thin CLI |
| Steward | BMad Code, LLC | GitHub | Fission AI | Tessl (Podjarny), $125M raised |
| License | ✓ MIT | ✓ MIT | ✓ MIT | ✗ closed platform |
| Artifact model | briefs, specs, architecture carried forward | constitution, spec, plan, tasks files | delta proposals archived into a living ledger | specs live on the platform |
| Workflow entry | `bmad-build` with right-sized depth | `/speckit-constitution` then specify | `/opsx:propose` then apply and archive | web workflow |
| Ceremony sizing | ✓ right-sizes to the change | ✗ fixed ceremony | ~ fixed but light | ? not verified |
| Brownfield support | ✓ establish-context path | ~ not the primary case | ✓ explicit design goal | ? not verified |
| Convergence checking | ✓ verify and learn loop | ✓ converge step | ~ archive keeps ledger current | ? not verified |
| Unattended execution | ✓ BMad Loop module | ✗ | ✗ | ? not verified |
| Adoption | 52,475 stars | 132,331 stars | 66,714 stars, 1.6M npm downloads a month | 24-point raise thread, thin OSS surface |
| Pricing | free | free | free | subscription, tiers unverified |

## Reading the matrix

**The license and steward rows tell the ownership story: three repo-native MIT toolkits against one closed, funded platform, and the free tools set the price anchor at zero while Tessl spends $125M betting specs are rentable.**
The adoption row inverts the funding row, which is the tension to watch.

**Ceremony sizing is the design axis the waterfall critique created: only BMad sends small changes straight to build, and the two artifact-first tools pay for their simplicity with fixed ceremony.**
If your changes are mostly small, that row alone picks your column.

**Brownfield is the sleeper row: OpenSpec is explicitly built for existing code, BMad has an establish-context path, and spec-kit's scaffolding still assumes a fresher repo than most of us have.**

## Choosing from the matrix

- Existing codebase, want the spec ledger to stay current: OpenSpec.
- Want a whole delivery process with roles and retrospectives: BMad Method.
- Heterogeneous org, zero cost, constitution ceremony acceptable: Spec Kit.
- Want specs as a managed product and accept portability questions: Tessl.

## See also

- [Task Management Feature Matrix](../task-management-feature-matrix/index.md) - the boards these specs eventually fill
- [Kiro](../kiro/index.md) - the spec-first IDE, the closed alternative on the editor axis
- [AGENTS.md](../agents-md/index.md) - the lighter convention all of these extend
- [Send Implementation, Not Issue](../../send-implementation-not-issue/index.md) - the corpus argument for specs plus implementation

## References

- https://github.com/bmad-code-org/BMAD-METHOD - loop, modules, licensing for the BMad column
- https://github.com/Fission-AI/OpenSpec - opsx workflow and philosophy for the OpenSpec column
- https://github.com/github/spec-kit - workflow steps and integrations for the Spec Kit column
- https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html - the third-party analysis covering Kiro, Spec Kit, and Tessl
- https://www.tessl.io/blog/announcing-our-series-a-for-ai-native-software-development - the raise grounding the Tessl column
- https://api.npmjs.org/downloads/point/last-month/@fission-ai/openspec - the OpenSpec install velocity
