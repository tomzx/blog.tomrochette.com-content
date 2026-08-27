---
title: OpenSpec
created: 2026-08-27
updated: 2026-08-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, spec-driven-development, specs, open-source]
readability: 3
audience_notes: >
  Engineers who want spec-driven development on an existing codebase rather than a greenfield scaffold.
  Assumes you already run an AI coding assistant that supports slash commands and know what a delta spec is for.
---

OpenSpec is Fission AI's MIT-licensed spec-driven development toolkit for AI coding assistants: a lightweight CLI and slash-command workflow where every change is a delta proposal (proposal, specs, design, tasks) that implements, then archives into a living spec ledger under `openspec/`.
Facts below verified as of 2026-08-27.

**OpenSpec is the brownfield answer the spec movement was missing: instead of scaffolding a ceremony, it versions the spec itself as change proposals that accumulate, and about 66k stars plus 1.6 million npm downloads a month say the delta model is what iterative teams actually wanted.**

## What it is

An npm package (`@fission-ai/openspec`) whose philosophy block reads fluid not rigid, iterative not waterfall, easy not complex, built for brownfield not just greenfield.
The rebuilt artifact workflow runs as slash commands any assistant can drive: `/opsx:explore` to think, `/opsx:propose` to write `proposal.md`, specs, `design.md`, and `tasks.md` into `openspec/changes/<change>/`, `/opsx:apply` to implement the checklist, and `/opsx:archive` to fold the delta into the standing spec.
The docs live at [openspec.dev](https://openspec.dev/), with a Discord for support.

## Status

Half of spec-kit's stars in a third of the time.
As of 2026-08-27: 66,398 stars and 4,571 forks since creation on 2025-08-05, 190 open issues, pushed the day before verification, MIT, and 1,610,142 npm downloads last month.
**Its Hacker News footprint is effectively empty (no significant thread found this run), so adoption spread through X and Discord, and third-party verification is thinner than the install count implies.**
The README's own superlative ("the most loved spec framework") is vendor framing, not a measured claim.

## Strengths

- The delta-archive model keeps the spec current without re-scaffolding, which is exactly where static spec trees rot.
- Explicitly designed for existing codebases, the segment spec-kit's greenfield scaffolding serves worst.
- Agent-agnostic slash commands, so it works with whatever assistant you already run.
- Massive measured install velocity (1.6M downloads a month) means the rough edges get found fast.

## Cautions

- Corporate single-steward (Fission AI) with no foundation governance, unlike GitHub's spec-kit or BMad's LLC-plus-community posture.
- The workflow was rebuilt once already (the opsx artifact flow replaced an older one), so expect vocabulary churn.
- No significant independent writing to check marketing claims against.
- Ceremony still depends on the assistant asking for it; a yolo-configured agent skips the gates as easily as anywhere else.

## Pricing

Free and open source under MIT.
No paid tier or hosted product as of 2026-08-27.

## Compared to

- [GitHub Spec Kit](../spec-kit/index.md): the movement's root, constitution-first and greenfield-friendly; choose Spec Kit for process scaffolding across a heterogeneous org, OpenSpec for living specs on one real codebase.
- [BMad Method](../bmad-method/index.md): the full agile method with agent roles; choose BMad when you want the roles and retrospectives, OpenSpec when you want the artifact ledger.
- [Tessl](../tessl/index.md): the funded platform play; choose Tessl when you want specs as a hosted product, OpenSpec when you want them as files you own.

## Bottom line

**Recommended as the default spec toolkit for existing repositories, which is most repositories.**
Not for organizations that need a vendor to call or a constitution ceremony.
My disagreeable claim: the delta-archive idea is the one durable invention this category has produced, spec-kit popularized the movement but OpenSpec's change-ledger is what the survivors will copy.

## See also

- [GitHub Spec Kit](../spec-kit/index.md) - the movement root it complements
- [BMad Method](../bmad-method/index.md) - the method-heavy alternative
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category compared
- [Send Implementation, Not Issue](../../send-implementation-not-issue/index.md) - the corpus argument for specs plus implementation

## References

- https://github.com/Fission-AI/OpenSpec - README: philosophy, opsx workflow, artifact layout
- https://api.github.com/repos/Fission-AI/OpenSpec - stars, forks, issues as of 2026-08-27
- https://openspec.dev/ - official documentation site
- https://api.npmjs.org/downloads/point/last-month/@fission-ai/openspec - 1,610,142 downloads last month
- https://github.com/Fission-AI/OpenSpec/blob/main/docs/opsx.md - the rebuilt artifact workflow
