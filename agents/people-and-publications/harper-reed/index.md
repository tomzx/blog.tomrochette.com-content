---
title: Harper Reed
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, llm-codegen, spec-first, agentic-coding, workflows]
readability: 3
audience_notes: >
  Developers adopting LLM code generation who want one concrete, end-to-end workflow to start from and mutate, plus the adoption ladder to go with it.
  Assumes you have used an IDE and at least one coding assistant or agent, and that you can tolerate profanity and personal asides in exchange for signal.
---

Harper Reed is a Chicago technologist and entrepreneur (CTO of Obama's 2012 campaign, former CTO of Threadless, founder of Modest, now CEO of 2389.ai) who writes about shipping software with LLMs at harper.blog.
Facts below verified as of 2026-09-24.

**His essay "My LLM codegen workflow atm" became the reference spec-first codegen workflow that Hacker News threads cite as best practice, and its boundary is that it is one person's fast-aging loop, dated on purpose.**

## What it is

A personal blog running about 24 years, roughly 1444 posts at about 1.04 posts per week on average, split into long-form posts, near-daily short notes, and a Now page.
The signature piece (2025-02-16) lays out a three-file greenfield workflow: brainstorm a spec with a one-question-at-a-time prompt, have a reasoning model turn spec.md into a prompt_plan.md and todo.md, then execute prompt by prompt with Claude or Aider while tests gate each step, plus a repomix-based context loop for existing codebases.
The follow-ups generalize it: "An LLM Codegen Hero's Journey" maps the nine-step adoption ladder from autocomplete to full agents, and "Basic Claude Code" ports the workflow to Claude Code with TDD as the anti-hallucination device ("The robots LOVE TDD").
Everything ships with the actual prompts inline, and posts carry his "written 98% by a human" disclosure.

## Status

Active and still iterating in public.
As of 2026-09-24 the homepage leads with "Why Don't My Agents Break Containment?" (2026-09-22), an agent-containment experiment out of his 2389.ai research, with recent long-form posts in January, March, August, and September 2026 and near-daily notes.
He is CEO of 2389.ai, where his whole team adopted the Claude Code workflow, and his history page records the arc: CTO of Obama for America from April 2011, Modest sold to PayPal in 2015, 2389 started in 2024.
The workflow post's footprint is verifiable on Hacker News: commenters in the Kiro IDE launch, the Claude 4, and the GitHub Copilot Coding Agent threads point to it as the popular workflow, one calling it "basically best practice today" (as of 2026-09-24).
He also translates major posts into Japanese, Spanish, Korean, and Chinese.

## Strengths

- Concreteness: the prompts, the three files, and the exact execution loop are all in the post, and the workflow is tool-agnostic (it outlived his own Aider phase).
- Practitioner credibility at scale: many shipped side products, a C interpreter built with Claude Code in about an hour, and a whole team running the process.
- Calibrated humility: he dates his own advice ("this is working well NOW, it will probably not work in 2 weeks") and updated it within weeks when Claude Code shipped.
- The follow-ups cover the two gaps most workflow posts leave: how beginners climb to agentic coding, and how a team adopts it through pilots, rotation, and documentation.

## Cautions

- Shelf life is short by his own admission: the original post was Aider-centric, Claude Code landed eight days later, and his current work has moved on to agent containment experiments.
- Greenfield and small-team skew: the multiplayer problem ("the bots collide, the merges are horrific") is named, not solved.
- Skeptics exist in the same threads that praise him: one engineer reports never succeeding at building a complete feature or prototype with the technique (visible in the HN results as of 2026-09-24).
- The signal is buried in a personal blog: profanity, photography, and a high-volume notes stream mean RSS or targeted visits beat casual scrolling.

## Compared to

- [Simon Willison](../simon-willison/index.md): both practitioner bloggers, but Willison tracks the whole tool-and-security landscape while Reed commits to one opinionated workflow; take breadth from Willison, a starting loop from Reed.
- [Hamel Husain](../hamel-husain/index.md): Husain covers the evaluation side of LLM systems, Reed covers the generation loop; pair them when your question shifts from "how do I generate" to "how do I know it works".
- [Chip Huyen](../chip-huyen/index.md): Huyen's systems-level ML engineering framing versus Reed's single-developer daily loop; Huyen for organizations, Reed for the individual.

## Bottom line

Recommended for developers starting out with agentic codegen who need a concrete, proven workflow to run and mutate, and for leads designing a first team pilot.
Not for readers wanting evaluation methodology, organization-level platform strategy, or advice stable enough to survive the next model release.

## Top 5 recommended reading

- [My LLM codegen workflow atm](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/) - the reference spec-first workflow, with every prompt inline, that HN threads still cite as best practice.
- [An LLM Codegen Hero's Journey](https://harper.blog/2025/04/17/an-llm-codegen-heros-journey/) - the nine-step adoption ladder from autocomplete to letting agents run, and why experienced developers should walk it in order.
- [Basic Claude Code](https://harper.blog/2025/05/08/basic-claude-code/) - the workflow ported to Claude Code, including the prompt_plan.md driver prompt and TDD as the anti-hallucination device.
- [Waterfall in 15 Minutes or Your Money Back](https://harper.blog/2025/04/10/waterfall-in-15-minutes-or-your-money-back/) - the clearest articulation of spec-then-generate-then-review as micro-waterfall cycles, with team pilot advice and a disclosed AI-assisted draft.
- [Why Don't My Agents Break Containment?](https://harper.blog/2026/09/22/break-away/) - the 2026 frontier: what unlimited tokens change about agent harness design, and what happened when his agent got loose on his lab network.

## Changes

- 2026-09-24 - Created.

## See also

- [Simon Willison](../simon-willison/index.md) - the other practitioner blogger to follow once you need breadth beyond one workflow.
- [Hamel Husain](../hamel-husain/index.md) - the evaluation counterpart to Reed's generation loop.
- [Chip Huyen](../chip-huyen/index.md) - the systems and org-level framing around what Reed does day to day.
- [GitHub Spec Kit](../../spec-driven-development/spec-kit/index.md) - the spec-driven tooling category that industrializes his spec.md and prompt_plan.md habits.
- [Context Management Patterns](../../context-management-patterns/index.md) - the repomix context-packing step in his brownfield loop, generalized.

## References

- https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/ - the reference workflow post: spec.md, prompt_plan.md, todo.md, and both execution loops
- https://harper.blog/ - the blog home: current posts (through 2026-09-22), the notes stream, RSS, and translations
- https://harper.blog/about/ - the blogging record: about 24 years, about 1444 posts, about 1.04 posts per week
- https://harperreed.com/ - credentials and timeline: Obama 2012 campaign CTO, Threadless, Modest to PayPal, 2389.ai
- https://harper.blog/2025/04/17/an-llm-codegen-heros-journey/ - the adoption-ladder follow-up
- https://harper.blog/2025/05/08/basic-claude-code/ - the Claude Code port and team adoption
- https://harper.blog/2025/04/10/waterfall-in-15-minutes-or-your-money-back/ - the micro-waterfall framing and team pilot advice
- https://harper.blog/2026/09/22/break-away/ - the current agent-containment work
- https://hn.algolia.com/api/v1/search?query=harper%20reed%20llm%20codegen&hitsPerPage=8 - third-party HN evidence: cited as best practice across Kiro, Claude 4, and Copilot Coding Agent threads, plus one skeptic (as of 2026-09-24)
