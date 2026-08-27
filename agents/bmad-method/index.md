---
title: BMad Method
created: 2026-08-27
updated: 2026-08-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, spec-driven-development, agile, multi-agent, open-source]
readability: 3
audience_notes: >
  Engineers who want a full agile method with agent roles around their coding assistant, not just spec artifacts.
  Assumes you already run an AI coding tool and know what a retrospective is for.
---

BMad Method (bmad-code-org) is the open-source Breakthrough Method for Agile AI-Driven Development: an installable method plus agent workflows (`npx bmad-method install`) that turn an idea or change request into working software through an explicit clarify, plan, build, learn loop, with the ceremony sized to the change.
Facts below verified as of 2026-08-27.

**BMad is the anti-waterfall wing of the spec movement: it sends small changes straight to build and reserves deep planning for big ones, which is the direct answer to the 225-point waterfall-strikes-back critique that static spec workflows still wear.**

## What it is

MIT-licensed (BMad Code, LLC) with no paywalled workflows, installed via npm with Node 20.12+, Python 3.10+, and uv as prerequisites.
The delivery loop runs clarify to plan to build-and-verify to learn-and-adjust, invoked as `bmad-build` in whatever AI coding tool you use, and the method's agents supply specialized perspectives (product, architecture, UX, development, testing) as multi-agent discussions where judgment stays with you.
**Its distinctive move is durable context: product and technical decisions carry forward as briefs, specifications, and architecture instead of being re-explained in every chat.**
The ecosystem is modular: BMad Builder, a Creative Intelligence Suite, an enterprise Test Architect, BMad Loop for unattended whole-epic build-verify-retro runs, a Game Dev Studio, and web bundles that package planning workflows as Gemini Gems and ChatGPT GPTs.

## Status

Large, active, and quietly adopted.
As of 2026-08-27: 52,371 stars and 5,958 forks since creation on 2025-04-13, 131 open issues, pushed the morning of verification.
The derivative community is real (third-party skill packs and hybrids like boss-skill at 550 stars and bmalph at 405), but its HN threads run 2 to 4 points, so the method spread through the ecosystem rather than the front page.

## Strengths

- Right-sizing the process to the change is the correct fix for spec theater, and it is BMad's core design decision, not a setting.
- Brownfield-first: an establish-context path for inherited codebases instead of assuming a fresh repo.
- The module system lets you adopt the planning loop without the creative suite or game studio baggage.
- Web bundles meet planners where they already are (Gemini, ChatGPT) and hand artifacts to the coding tool.

## Cautions

- It is a whole method to learn; adoption cost is the highest in this category and the docs map shows it.
- Node plus Python plus uv prerequisites make the install heavier than a pip or npx one-liner.
- Thin third-party coverage means the method's claims rest mostly on its own docs.
- The unattended BMad Loop module is autonomy with a feedback loop, read its verification story before trusting an epic to it.

## Pricing

Free and open source under MIT.
The README states no paywalled workflows or gated community; web bundles and modules are also open.

## Compared to

- [GitHub Spec Kit](../spec-kit/index.md): constitution and artifacts without the agile loop; choose Spec Kit for lightweight conventions, BMad when the delivery process itself needs structure.
- [OpenSpec](../openspec/index.md): the living spec ledger; choose OpenSpec for the artifact model, BMad for the roles and retrospectives.
- [Tessl](../tessl/index.md): the commercial platform route; choose BMad when the method must stay in your repo and your control.

## Bottom line

**Recommended for teams that want a genuine delivery process around their agents and will pay the learning cost.**
Not for solo prototypes or anyone allergic to method vocabulary.
The disagreeable claim I will defend: within a year the waterfall critique will be aimed at spec-kit and OpenSpec while BMad's size-the-ceremony loop becomes the orthodox form, because it is the only design here that took the critique seriously on day one.

## See also

- [GitHub Spec Kit](../spec-kit/index.md) - the movement root it extends
- [OpenSpec](../openspec/index.md) - the artifact-ledger alternative
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category compared
- [The Future of Code Review](../../the-future-of-code-review/index.md) - where the learn-and-adjust loop lands in review

## References

- https://github.com/bmad-code-org/BMAD-METHOD - README: loop, modules, prerequisites, licensing
- https://api.github.com/repos/bmad-code-org/BMAD-METHOD - stars, forks, issues as of 2026-08-27
- https://docs.bmad-method.org/ - the documentation map
- https://github.com/bmad-code-org/bmad-loop - the unattended epic module
- https://news.ycombinator.com/item?id=44879862 - the 4-point launch-era thread, the thin-footprint evidence
- https://github.com/LarsCowe/bmalph - a 405-star community hybrid as ecosystem evidence
