---
title: Matt Pocock
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, developer, education, ai-coding]
readability: 3
audience_notes: >
  Engineers who want a structured, installable curriculum for AI-assisted coding rather than a daily feed, from TypeScript depth to agent skills and workflows.
  Assumes you write code daily, run at least one coding agent, and want tested practices over hot takes.
---

Matt Pocock is a full-time developer educator who built Total TypeScript and now runs AI Hero, where the same exercise-driven teaching is aimed at coding with AI agents.

**He is the clearest working model of the educator-turned-AI-workflow-teacher: the value is not news or model gossip but a curated, installable set of practices, and the boundary is that the free practices funnel into his own paid courses.**

## What it is

Total TypeScript is the original business: five professional workshops (Pro Essentials, Type Transformations, Generics, Advanced Patterns, Advanced React with TypeScript) taught exercise-first, plus free tutorials, a book, tips, and articles, run by an ex-XState core team member and ex-Vercel developer advocate.
AI Hero is the newer property: posts, a skills catalogue, an AI Coding Dictionary, workshops, cohorts, and events, concentrated on Claude Code, MCP, evals, and the Vercel AI SDK.
On GitHub (46.5k followers as of 2026-09-24) the flagship is the skills repo, "Skills for Real Engineers", MIT-licensed, at 268.6k stars, alongside sandcastle (sandboxed coding agents in TypeScript, 8.1k stars), dictionary-of-ai-coding (4.7k stars), and ts-reset (8.6k stars).
The skills are deliberately small, composable, and forkable: grill-me, grill-with-docs, wayfinder, to-spec, to-tickets, tdd, code-review, and a setup skill, organized around four failure modes of agentic coding.

## Status

Active and at the center of the agent-skills wave.
The AI Hero discovery index lists well over a hundred public items, including roughly two dozen documented skills with per-skill pages and a changelog, and the skills repo shows 472 commits.
His /grill-me skill went viral by his own account (his post on it was last updated 2026-03-23), and an Ask HN thread from 2026-09-08 names it as the one skill a respondent "found gets regular mileage".
Scale is real: in a May 2026 video he said his AI-coding cohort starting June 1 had around 4,000 to 4,500 students, his most subscribed course ever.
The trajectory is complete: TypeScript education is now the on-ramp, AI Hero and the skills repo are the main event.

## Strengths

- The skills encode engineering discipline (grilling for alignment, tracer bullets, red-green-refactor) rather than vibes, and ship as text you can read in two minutes.
- Exercise-driven pedagogy carries over from TypeScript: you practice against real failure modes instead of watching walkthroughs.
- Ecosystem validation is measurable: multiple third-party Show HN projects are built around his workflow, his skills, or specific skills like grill-me and wayfinder.
- He publishes criticism of vendor output inside his own catalogue (for example a post titled "Why the Anthropic Ralph plugin sucks (use a bash loop instead)"), which keeps the catalogue from being pure marketing.

## Cautions

- The commercial engine is large: free posts and skills lead to paid workshops and cohorts, and the cohort numbers above drew a goldrush reading on HN ("during a goldrush, sell shovels"), a fair warning that popularity is not evaluated effectiveness.
- Coverage is vendor-weighted toward Claude Code and the Vercel AI SDK, so planning around other harnesses means translating his examples.
- There is no model research, benchmarking, or neutral evaluation here; he teaches practice, he does not test claims about models.
- At 4,000-plus students per cohort, the feedback loop between his material and any individual team's context is thin by construction.

## Compared to

- [Simon Willison](../simon-willison/index.md): the daily raw chronicle versus the structured curriculum; Willison for what changed today, Pocock for what to practice this month.
- [Addy Osmani](../addy-osmani/index.md): Osmani writes enterprise-scale agentic engineering from inside Anthropic and Google, Pocock arms individual practitioners with installable skills.
- [AI Jason](../ai-jason/index.md): the video counterpart; Jason's workflows are something you watch, Pocock's are repo artifacts you install and modify.

## Bottom line

**Recommended for working engineers who want an opinionated, installable set of agent workflows and are comfortable with a TypeScript- and Claude Code-weighted lens.**
Not for anyone seeking model research, benchmarks, or vendor-neutral evaluation of agent tooling.

## Top 5 recommended reading

- [My "Grill Me" Skill Went Viral](https://www.aihero.dev/my-grill-me-skill-has-gone-viral) - The intro to his most popular skill, a two-minute read showing his method of encoding engineering discipline as installable text.
- [Skills for Real Engineers](https://github.com/mattpocock/skills) - The MIT-licensed skills repo behind the agent-skills wave, each skill small, composable, and forkable.
- [5 Agent Skills I Use Every Day](https://www.aihero.dev/5-agent-skills-i-use-every-day) - His daily-driver workflows in his own words, the practical companion to the skills catalogue.
- [A Complete Guide To AGENTS.md](https://www.aihero.dev/a-complete-guide-to-agents-md) - His deepest single practical guide, the reference piece for the file that structures agent work.
- [Total TypeScript](https://www.totaltypescript.com/) - The exercise-driven TypeScript curriculum where his teaching method was built, the foundation under everything at AI Hero.

## Changes

- 2026-09-24 - Created.
- 2026-09-24 - Added the Top 5 recommended reading section.

## See also

- [Simon Willison](../simon-willison/index.md) - the daily firehose his curriculum distills into practices
- [Addy Osmani](../addy-osmani/index.md) - the enterprise-scale counterpart on holding agent output to a production bar
- [Skills and plugins for OpenCode](../../skills/opencode-skills-and-plugins/index.md) - the packaging format his skills repo helped popularize
- [Context management patterns](../../context-management-patterns/index.md) - the practice his shared-language, handoff, and CONTEXT.md skills operationalize

## References

- https://www.totaltypescript.com/ - the TypeScript business: five workshops, exercise-driven format, his bio (ex-XState core team, ex-Vercel)
- https://www.aihero.dev/sitemap.md - the AI Hero public content inventory: posts, skills pages, AI Coding Dictionary, cohorts, events
- https://www.aihero.dev/my-grill-me-skill-has-gone-viral.md - the grill-me skill text, its design, and his viral-reach claim
- https://github.com/mattpocock - profile and pinned repos as of 2026-09-24 (46.5k followers; skills, sandcastle, dictionary-of-ai-coding, ts-reset)
- https://github.com/mattpocock/skills - the skills repo: MIT license, four failure modes, full skill list, ~60,000-person newsletter claim
- https://news.ycombinator.com/item?id=48321838 - the skeptical HN thread quoting his own cohort-size and revenue numbers
- https://hn.algolia.com/api/v1/search?query=%22matt+pocock%22&tags=story - the third-party build evidence: multiple Show HNs around his workflow and skills, including the September 2026 grill-me Ask HN
