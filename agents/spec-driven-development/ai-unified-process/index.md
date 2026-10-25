---
title: AI Unified Process
created: 2026-10-17
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, use-cases, methodology, rup, open-source]
readability: 3
audience_notes: >
  Engineers and analysts choosing a whole-method spec-driven workflow and wondering what the Rational Unified Process looks like when coding agents do the consistency work.
  Assumes you know what a use case and a review gate are.
---

AI Unified Process (AIUP) is Simon Martinelli's requirements-first, Apache-2.0 methodology that keeps use cases as the living source of truth, generates code and tests from them with coding agents, and audits the result back against the spec, distributed as agent plugins and skills for Claude Code, Codex, Cursor, Copilot, Gemini CLI, and OpenCode.

**AIUP is this category's clearest inversion: where every other column treats the spec as input to code, it declares the code the current implementation of the spec, and it arrives with the category's first published textbook (the steward's own Apress book on the method) and a Rational Unified Process lineage.**

## What it is

An open-source plugin set (`aiup-core` plus seven layer plugins) installed per agent from its marketplace, through the Tessl registry, or as manual skill files.
`aiup-core` owns the stack-independent path: `/requirements` builds the catalog from `docs/vision.md`, then `/entity-model`, `/use-case-diagram`, `/use-case-spec` (which asks up to five questions whose answers change the spec before writing), `/business-process`, `/test-case`, `/spec-review`, and `/reverse-engineer` for existing codebases.
Construction continues with layer plugins (Flyway, jOOQ, JPA, Spring Boot, Vaadin, Angular, Playwright), one per technical layer, combined per project and recorded by `/stack`; the two original combined stack plugins (Vaadin/jOOQ, Angular/JPA) are deprecated and leave with `aiup-core` 4.0.0, while Blazor/.NET and NestJS/Next.js remain combined.
Artifacts carry stable identifiers (FR-\*, UC-\*, BR-\*, TC-\*) referenced downstream once, with code markers such as `// UC-005 BR-003: ...` and test annotations tying every business rule to its implementation.
Coverage moved into core with the layer model: `/use-case-coverage` judges implementation and tests together, and the read-only `uc-coverage` sub-agent survives in the two deprecated combined plugins until 4.0.0 removes them.

## Status

Active and authored: 146 stars, 26 forks, and 6 open issues since creation on 2026-02-28, Apache-2.0 (GitHub API); as of 2026-10-25, pushed 2026-10-24 with a coordinated release wave across every plugin, `aiup-core` v3.1.0 (per-module reverse-engineering, the `/stack` command, coverage evidence from NFR and constraint ids) and the layer plugins re-versioned, the same wave that deprecated the two combined stack plugins.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=AI-Unified-Process/marketplace&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=AI-Unified-Process/marketplace&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=AI-Unified-Process/marketplace&type=date&legend=top-left" />
</picture>

**The adoption case rests on named field use rather than stars: reference customers (WBS GRUPPE, Zooey GmbH, centeractive), one community-contributed stack plugin, an independent endorsement in the Ask HN spec-driven thread (2026-09-09), and a public third-party field report (a 13-use-case case-management build whose coverage audit caught three gaps the agent then closed).**
It has no Hacker News thread of its own, and the name collides with an unrelated `aiup.dev` story, so searching for coverage takes care.
Martinelli self-places it at "spec-anchored, not spec-first", the middle level of Birgitta Böckeler's three-level framing of spec-driven development.

## Strengths

- The code-serves-the-spec inversion is carried by machinery, not prose: `spec_lint.py` fails CI on broken identifiers, requirement status is derived from the use cases with a drift warning, and `/coverage-check` maps every use-case unit onto the code and tests that realize it.
- Traceability is bidirectional by design: references are written downstream once and the reverse direction is computed, so "why does this exist" is one command (`spec_lint --trace --only FR-014`).
- Brownfield is a first-class workflow: `/reverse-engineer` recovers entity and use-case baselines from an existing codebase.
- Steward credibility: a Java Champion training teams on exactly this method, with named reference teams, a tutorial, videos, and a book behind it.

## Cautions

- 146 stars is among the smallest adoption figures in this category, and the visible adoption sits inside the German-speaking Java and Vaadin consulting orbit the stack plugins encode.
- The full artifact chain (vision, catalog, entity model, diagram, use cases, processes, test cases) is heavyweight, nothing sizes it down for small changes, and the field report is blunt that in production work the review time must actually be spent.
- The coverage audit just changed homes: layer-plugin projects get `/use-case-coverage` in core, but projects on the deprecated combined plugins must migrate before core 4.0.0 removes their `uc-coverage` agent.
- Solo steward with paid training and a private-beta Studio around the method, and Apache-2.0 with NOTICE and trademark terms on derived works, unlike this category's MIT norm.

## Pricing

The plugins and the Navigator IDE plugin are free and open source under Apache-2.0.
Training is the paid surface: an in-house workshop at CHF 4,400 per day for up to 10 people, and online sessions from $290 (as of 2026-10-17).
AI Unified Studio, the web workspace for non-developer stakeholders, is private beta by invitation with no published price, and the Apress book is sold separately; the Leanpub use-case guide is free.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-17 | All | Baseline at creation: plugins and Navigator free (Apache-2.0), in-house workshop CHF 4,400 per day up to 10 people, online sessions from $290, Studio unpriced in private beta. | [unifiedprocess.ai](https://unifiedprocess.ai/) |

## Compared to

- [BMad Method](../bmad-method/index.md): the other whole-method column; BMad right-sizes the ceremony and stays code-first, AIUP runs a fixed requirements-to-construction chain with the spec on top.
- [GitHub Spec Kit](../spec-kit/index.md): scaffolds conventions per change and leaves the spec behind; AIUP keeps the spec anchored for the system's life and reconciles code to it.
- [OpenSpec](../openspec/index.md): versions the spec as change deltas; AIUP versions behavior as use cases and treats code as the derivative.

## Bottom line

**Recommended for analyst-plus-developer teams on the supported stacks, especially modernizing business applications where the requirements should outlive the framework.**
Not for solo or small-change work, and not for stacks without a plugin, where the method ends at documented specifications.
The disagreeable claim I will defend: spec-kit taught the industry to write specs before code, but AIUP's direction, code as the current implementation of a living spec, is where this category's survivors are heading, and the book-plus-audit combination is the first serious attempt to make that teachable.

## Changes

- 2026-10-17 - Created from the Engineering4AI awesome-list entrant scan, profiling AI-Unified-Process/marketplace as the category's requirements-centric, RUP-lineage column.
- 2026-10-25 - Recorded the 2026-10-24 release wave: the plugin model rebuilt from four combined stack plugins to seven layer plugins combined per project (`/stack` records the combination), `aiup-core` v3.1.0 (per-module reverse-engineering, coverage evidence from NFR and constraint ids), and the Vaadin/jOOQ and Angular/JPA combined plugins deprecated ahead of removal in core 4.0.0, with `/use-case-coverage` moving the coverage audit into core.

## See also

- [BMad Method](../bmad-method/index.md) - the other whole-method column, the agile one where AIUP is the RUP one
- [GitHub Spec Kit](../spec-kit/index.md) - the movement root whose spec-first level AIUP positions itself above
- [Tessl](../tessl/index.md) - the platform whose registry distributes AIUP's plugins
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/AI-Unified-Process/marketplace - repository, README: plugins, workflow, install surfaces, license (146 stars as of 2026-10-17)
- https://raw.githubusercontent.com/AI-Unified-Process/marketplace/main/docs/workflow.md - the artifact flow, traceability identifiers, spec-review lint, and coverage-check internals
- https://unifiedprocess.ai/ - the methodology site: positioning, testimonials, pricing, the book, and Studio
- https://martinelli.ch/spec-driven-development-with-ai-a-new-approach-and-a-journey-into-the-past/ - the steward's origin post grounding the RUP lineage and the requirements-as-source-of-truth thesis
- https://korhan.org/blog/eine-einfache-fallverwaltung-nach-dem-ai-unified-process/ - the independent field report (2026-10-06), the critical source: coverage findings, the review-time warning, and the spec-gap admissions
- https://hn.algolia.com/api/v1/search?query=%22AI+Unified+Process%22&hitsPerPage=8 - the footprint check: one independent endorsement comment, no thread of its own, and the aiup.dev name collision
