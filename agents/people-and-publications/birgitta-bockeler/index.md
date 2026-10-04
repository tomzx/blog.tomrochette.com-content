---
title: Birgitta Böckeler
created: 2026-10-04
updated: 2026-10-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, consulting, agentic-engineering, tdd, harness-engineering, spec-driven-development]
readability: 3
audience_notes: >
  Engineers and leads inside established, non-AI-company organizations who want evidence-grade answers about which craft practices still matter when agents write most of the code.
  Assumes you know what TDD, spec-driven development, and a coding-agent harness are.
---

Birgitta Böckeler is a Distinguished Engineer for AI-assisted delivery at Thoughtworks whose "Exploring Generative AI" memo series on martinfowler.com is the longest-running practitioner evaluation record in this field, running since July 2023.

**She is the methodical evaluator of the agentic-coding wave: a consultant who runs small, self-skeptical experiments on her own craft's sacred cows, published under the most durable byline in software, with the boundary that her sample sizes are small and her employer sells the transformation she studies.**

## What it is

A memo series, a set of long-form articles, and a constant talk circuit, backed by more than 20 years as a developer, architect, and technical leader.
The memo series has run on martinfowler.com since the first memo, "The toolchain" (2023-07-26), and holds 32 memos as of 2026-10-04, most authored by her and the rest by Thoughtworks colleagues under the same franchise.
Her 2026 solo pieces are the substantive layer: "Context Engineering for Coding Agents" (2026-02-05), "Harness engineering for coding agent users" (2026-04-02), "Maintainability sensors for coding agents" (2026-05-07), the local-models pair (2026-07-07 and 2026-07-08), and "TDD inside the agent loop - theater or actual value?" (2026-08-10).
She iterates a "State of Play: AI Coding" talk at QCon London, AI DevCon London, and other stages, and reached practitioners through a June 2025 guest post on The Pragmatic Engineer and interviews including Software Engineering Radio 730 (July 2026).
Her own site, birgitta.info, indexes all of it by topic.

## Status

Active and current as of 2026-10-04.
Her newest piece is the TDD evaluation (2026-08-10), and the series continued with colleagues' memos after it, the latest being "An Accidental Blackboard" (2026-09-02) on an all-agentic team accidentally building a blackboard coordination system inside git.
The TDD evaluation is her most consequential claim: across five batches of paired TDD and non-TDD runs judged blind by Opus 4.8, TDD showed no discernible quality benefit and cost roughly 3 to 8.5 times the tokens, and she states she has stopped telling her coding agents to write tests first.
Community reception is uneven: her spec-driven-development comparison drew a 128-point Hacker News thread with 32 comments (October 2025), while the TDD evaluation drew a 4-point thread (August 2026), and her conference talks, not her links, carry most of her reach.

## Strengths

- She tests her own assumptions and publishes unfavorable results: the TDD piece concludes against the practice her audience (and her employer's heritage) is most attached to, with mutation scores and token multipliers in an appendix.
- The martinfowler.com venue makes her arc citable: from "coding assistants do not replace pair programming" (2023) to harness engineering and agent-loop evaluations (2026) in one place.
- **The vantage is the one this category was missing: she coaches teams inside large non-AI companies, so her examples are brownfield constraints and team habits, not frontier-lab budgets.**
- She coins and then operationalizes her vocabulary: harness engineering for users got a follow-up article on maintainability sensors, and the spec-driven-development memo became the field's reference comparison of Kiro, spec-kit, and Tessl.

## Cautions

- The experiments are small by her own wording: "far from a comprehensive and structured eval result", greenfield Python tasks, judgment delegated to Opus, so her anti-TDD conclusion is a hypothesis, not a benchmark.
- Thoughtworks sells AI-transformation consulting, and her "state of play" franchise doubles as the firm's positioning, so discount the framing rather than the data.
- The memo series is partly a shared byline: some entries are colleagues' memos, so "she published" needs checking against the author line.
- Her reach runs through talks and podcasts more than through linkable discussion threads, which makes her claims harder to audit in public argument than Willison's or Zechner's.

## Pricing

Free to read.
No paid tier and no products; Thoughtworks sells consulting around the practices she writes about.

## Compared to

- [Harper Reed](../harper-reed/index.md): both document working methods, but Reed hands you one opinionated loop to run, Böckeler evaluates which practices survive contact with agents at all.
- [Shreya Shankar](../shreya-shankar/index.md): both make agent claims measurable, Shankar with peer-reviewed data-systems benchmarks, Böckeler with consultant-grade field experiments on craft practices.
- [Simon Willison](../simon-willison/index.md): Willison chronicles tools daily from the outside, Böckeler evaluates practices monthly from inside client organizations.

## Bottom line

**Recommended for engineers and leads in established companies who want measured answers about which craft practices still matter when agents do the typing.**
Not for release tracking, model news, or anyone who needs large-sample benchmark evidence before acting.

## Top 5 recommended reading

- [TDD inside the agent loop - theater or actual value?](https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html) - the evaluation that ends with her abandoning TDD instructions for agents, mutation scores and token multipliers included.
- [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) - the framing article that defines what users can build on top of any harness, the idea behind her 2026 interview round.
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) - the three-tool evaluation that became the Hacker News reference discussion on SDD.
- [Context Engineering for Coding Agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) - the map of context-configuration features, using Claude Code as the worked example.
- [Two years of using AI tools for software engineering](https://newsletter.pragmaticengineer.com/p/two-years-of-using-ai) - her broadest first-person retrospective, from autocomplete to agents and the team-level consequences.

## Changes

- 2026-10-04 - Created, filling the enterprise non-AI-company practitioner slot the matrix named as its empty scaffold.

## See also

- [Harper Reed](../harper-reed/index.md) - the workflow-documenting counterpart to her practice-evaluating lens
- [Shreya Shankar](../shreya-shankar/index.md) - the other measurement voice, academic where Böckeler is consulting-grade
- [GitHub Spec Kit](../../spec-driven-development/spec-kit/index.md) - the tool her SDD comparison evaluates and the section's note covers in depth
- [Context Management Patterns](../../context-management-patterns/index.md) - the essay behind the context-configuration practices she maps
- [Simon Willison](../simon-willison/index.md) - the daily chronicler she acts as the monthly evaluator against

## References

- https://martinfowler.com/articles/exploring-gen-ai.html - the memo series index: cadence since July 2023, authorship split, and the full piece list
- https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html - the TDD evaluation: five batches, token multipliers, and her decision to stop instructing agents to write tests first
- https://martinfowler.com/articles/harness-engineering.html - the harness-engineering framing article for coding agent users (2026-04-02)
- https://martinfowler.com/articles/sensors-for-coding-agents.html - the maintainability-sensors follow-up (2026-05-07)
- https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html - the Kiro, spec-kit, and Tessl comparison (2025-10-15)
- https://birgitta.info - her own index of memos, articles, talks, and interviews, grounding the role and the record
- https://newsletter.pragmaticengineer.com/p/two-years-of-using-ai - her June 2025 Pragmatic Engineer guest post
- https://news.ycombinator.com/item?id=45610996 - the 128-point Hacker News discussion of the SDD comparison, including the skeptical comments on markdown specs (as of 2026-10-04)
- https://github.com/birgitta410/tdd-comparisons - the TDD evaluation's session transcripts and analysis artifacts
