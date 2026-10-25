---
title: PDD Kit
created: 2026-10-23
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, product-model, agent-skills, open-source]
readability: 3
audience_notes: >
  Engineers deciding where the product's standing definition should live when coding agents
  write most of the code.
  Assumes you know what a spec delta and a review gate are.
---

PDD Kit is a solo-maintained, MIT-licensed trio of agent skills (map, ideate, verify) plus a CLI that keeps a standing, present-tense Product Model as typed Markdown under `product-model/` in your repository and checks the code against it on every change.

**PDD Kit's bet inverts this category's: the artifact worth keeping is not the per-change spec but a standing model of the product itself, and the change-scoped specs every other member writes describe deltas against a product description none of them hold in one place.**

## What it is

An npm package (`pdd-toolkit`, first published 2026-10-13, at v0.37.1) that installs three skills into Claude Code, Codex, Cursor, Gemini CLI, and GitHub Copilot: `/pdd-map` reads an existing repository without running it and writes the model once you approve, `/pdd-ideate` records the next change in the model before any code exists, and `/pdd-verify` checks the implementation against the model and reports every gap, fixing only the ones you choose.
The model is a folder of typed resources: one Product, Entities (Actors when they act), Interfaces with Experiences and Screens, optional Domains, Capabilities proven by Scenarios, Journeys, Business Rules (the only place that says who may act), and Variations, plus a `coverage.md` that declares which of the repository's code the model accounts for and names what stayed unmapped.
A strict lint (`npx pdd-toolkit lint`) enforces the structure (unknown frontmatter keys are errors), a local `view` command opens the model as a browser report, and Blueprints are reviewed product models for common products you can pull instead of a blank page.
It is deliberately not a workflow: implementation stays with your agent, with plan mode, an SDD tool, or freestyle, and the docs' own line is "keep the spec-driven framework you use, or use none at all".
Made by Itai Gendler, who dogfoods it: the repository's own `product-model/` describes pdd-kit.

## Status

Active and young: 80 stars, 9 forks, repository created 2026-07-26, pushed 2026-10-24, as of 2026-10-25 (GitHub API), MIT, solo steward.
The npm package (published 2026-10-13) has six releases to v0.37.1 and 200 downloads last month (the 2026-09-23 to 2026-10-22 window, as of 2026-10-25), so adoption is the star count and nothing else yet.
It ships a complete docs site (pdd-kit.dev) with a reasoned blog, and the steward's SDD critique (2026-10-06) names OpenSpec, spec-kit, and Kiro directly, arguing their specs describe the change while the product stays scattered.
It entered this category's scan as the Engineering4AI awesome list's Development Frameworks entry, listed there as BusinessLens until the 2026-10-21 rename to pdd-kit; a 2026-10-13 sweep had rejected the repository under its old name below the bar, and the rebrand, the shipped site, and continued daily development re-listed it.

**The independent footprint is empty, and that is this note's critical angle: a Hacker News search returns one 1-point submission and nothing else, with no third-party coverage anywhere, so the claims rest on the steward's own docs and the dogfooded model in the repository.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=itai-gendler/pdd-kit&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=itai-gendler/pdd-kit&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=itai-gendler/pdd-kit&type=date&legend=top-left" />
</picture>

## Strengths

- **The standing artifact is the product, not the change**: a refactor never touches the model, a product decision is written once instead of restated in every change folder, and the next agent reads journeys, scenarios, and rules instead of reconstructing intent from tickets.
- Coverage is declared, not implied: `coverage.md` names the code the model accounts for, the code it excludes, and the code still unmapped, so verify's blind spots are written down before the check runs.
- The present-tense doctrine is enforced in the lint, not just the prose: the model holds no plans, priorities, or metrics, which keeps the standing artifact from rotting into a roadmap.
- It composes instead of replacing: the same repository can run spec-kit's per-change ceremony and PDD Kit's standing model, which no other member designs for.

## Cautions

- Zero independent coverage and an npm package published 2026-10-13 mean nothing here is validated by anyone but its steward, the same profile that kept thinner records out of this category.
- Verify reports gaps but names no guilty side: unlike Archcore's review, the human decides whether the code or the model moved, so the convergence check is advisory.
- The model is a standing artifact, which is standing maintenance: every behavioral change touches it, and the docs' answer (a product decision written once) still costs a review on each change.
- Solo steward, pre-1.0, and the resource-type vocabulary (Interfaces, Experiences, Screens, Capabilities, Journeys, Variations) is a learning curve of its own before the first model exists.

## Pricing

Does not apply: MIT, free, no paid tier found as of 2026-10-23.

## Compared to

- [AI Unified Process](../ai-unified-process/index.md): the other standing-artifact column; AIUP's use cases and business rules live inside a full method with a fixed artifact chain, PDD Kit keeps the product model and drops the method, and its verify reports gaps where AIUP's coverage-check maps every use-case unit with a justified status.
- [Archcore](../archcore/index.md): the other typed-documents-in-git context layer; Archcore's documents mix specs, plans, and decisions and its review names the side that is wrong, PDD Kit holds one present-tense product model with declared coverage and leaves the verdict to you.
- [OpenSpec](../openspec/index.md): the foil PDD Kit argues against; OpenSpec versions the product as an archive of change deltas, PDD Kit says the deltas never add up to the product and keeps one model beside them.

## Bottom line

**Recommended for teams running any spec-driven tool whose product definition is scattered across change folders, who want the standing model as a separate, reviewable artifact the agents read before they build.**
Not for anyone who needs an enforced gate or third-party validation before adopting a two-week-old package, and not for solo work too small to carry a model at all.

## Changes

- 2026-10-23 - Created from the Engineering4AI awesome-list entrant scan (listed as BusinessLens until the 2026-10-21 rename, previously rejected below the bar under the old name), resolving itai-gendler/pdd-kit as the product-model column with the zero-coverage record as the critical angle.

- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).

## See also

- [AI Unified Process](../ai-unified-process/index.md) - the method-carrying standing-artifact alternative, requirements-first where PDD Kit is model-only
- [Archcore](../archcore/index.md) - the other typed-document context layer, decision-scoped where PDD Kit is product-scoped
- [OpenSpec](../openspec/index.md) - the change-ledger foil the steward's SDD critique names first
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/itai-gendler/pdd-kit - repository: counts, dates, license, the dogfooded product-model/ (80 stars as of 2026-10-23)
- https://raw.githubusercontent.com/itai-gendler/pdd-kit/main/README.md - the three-skill loop, the resource list, the kanban Blueprint example, and the SDD-contrast framing
- https://pdd-kit.dev - the site: positioning, the scattered-knowledge argument, the one-loop ideate-implement-verify cycle
- https://pdd-kit.dev/docs/product-model - the resource types, coverage.md, the lint contract, and the present-tense doctrine
- https://pdd-kit.dev/blog/pdd-and-spec-driven-development - the steward's SDD critique (2026-10-06) grounding the product-versus-change thesis
- https://registry.npmjs.org/pdd-toolkit - the npm package: v0.37.1, six versions, MIT, first published 2026-10-13
- https://api.npmjs.org/downloads/point/last-month/pdd-toolkit - 200 downloads last month (2026-09-23 to 2026-10-22 window), as of 2026-10-25
- https://api.github.com/repos/itai-gendler/pdd-kit - stars, forks, creation and push dates as of 2026-10-23
- https://hn.algolia.com/api/v1/search?query=pdd-kit&hitsPerPage=5 - the footprint check: one 1-point submission, no third-party coverage
