---
title: Dex Horthy
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, developer, agents, context-engineering]
readability: 3
audience_notes: >
  Engineers building LLM-powered software who want production-grade principles for agent architecture, owned context windows, and human checkpoints.
  Assumes you have tried an agent framework, hit its quality ceiling around 80 percent, and are deciding what to build yourself.
---

Dex Horthy is the founder of HumanLayer and author of 12-Factor Agents, the most-starred open methodology for building reliable LLM applications.
Facts below verified as of 2026-09-24.

**His sustained publication is not a blog but a methodology plus a weekly live show: 12-Factor Agents gave agent builders a shared vocabulary for owning context, and the weekly AI That Works recordings document the practice in public, while the written cadence is irregular and everything now routes into a commercial product.**

## What it is

12-Factor Agents (github.com/humanlayer/12-factor-agents) states twelve principles, including own your prompts, own your context window, tools are just structured outputs, contact humans with tool calls, and make your agent a stateless reducer, under a CC BY-SA 4.0 content license, with 26.4k stars and 2.0k forks as of 2026-09-24.
AI That Works is his weekly Zoom show and podcast with Vaibhav Gupta (BAML), every Tuesday at 10 AM PST, 76 numbered episodes dated from 2025-03-31 through 2026-09-29, each with code in a public repo.
The Outer Loop is his Substack ("AI Agents, Human in the Loop, maybe-agi", launched about two years ago), with the archive behind the subscribe wall.
HumanLayer itself pivoted from a human-approval API into a multiplayer coding-agent workspace (local daemons, cloud daemons, tasks and artifacts, an RPI-to-QRSPI workflow), with a free Starter tier for teams of up to three, Pro at $100/user/month, and BYOK for Claude Code, Codex, and Copilot.

## Status

Active on a talk-first cadence.
AI That Works ran weekly through #74 (2026-09-15) with #75 and #76 scheduled for 2026-09-22 and 2026-09-29, so the dependable publication is the weekly recorded conversation.
The 12-factor repo moves slowly now: 273 commits across roughly seventeen months, mostly refinements, and 2026 re-posts of it on HN drew 2 to 3 points, indicating maintenance-mode mindshare after the April 2025 spike (the original Show HN took 475 points and 78 comments).
His own show bio reads: founder at HumanLayer, 10+ years building devops tools at Replicated, Sprout Social, and JPL, "coiner of the term Context Engineering".
I read the trajectory as: methodology in 2025, product in 2026, with the open methodology now serving as the top of the funnel for the commercial workspace.

## Strengths

- Factor 3 (own your context window) and factor 7 (contact humans with tool calls) became shared vocabulary, and the guide remains the cleanest articulation of "mostly just software, with LLM steps sprinkled in".
- The framework skepticism is earned and specific: 100+ SaaS builder conversations distilled into "take small, modular concepts into your existing product" instead of greenfield framework adoption.
- He engages critics in public; the Show HN thread shows him answering framework defenders, eval skeptics, and cost arguments point by point.
- The show ships code per episode, so claims are checkable against artifacts rather than slides.

## Cautions

- Everything is commercial now: the methodology sits on humanlayer.dev next to $100/user/month pricing, so read the principles as correct but also as marketing for the stack that embodies them.
- The "coiner of the term Context Engineering" billing is contested; the term's spread is usually traced to Tobi Lutke's June 2025 tweet amplified by Karpathy (see Simon Willison's definition post), which predates only part of that story, and the 12-factor repo itself treats context engineering as factor 3's subject rather than a coinage.
- The written output is talk-driven and irregular: the Substack archive is not publicly browsable, the repo is quiet, so anyone following him for text will be disappointed.
- The guide optimizes for build-it-yourself control, which is the right bias for product teams at the reliability frontier and the wrong one for teams that just need a working harness.

## Compared to

- [Hamel Husain](../hamel-husain/index.md): Husain's discipline is measurement and evals, Horthy's is architecture and control flow; read Husain when you do not know whether it works, Horthy when you must decide what to own.
- [Simon Willison](../simon-willison/index.md): Willison documents the whole landscape daily, Horthy argues one methodology weekly; breadth versus a single playbook.
- [Steve Yegge](../steve-yegge/index.md): both are opinionated builders with products; Yegge declares manifestos that his code may later falsify, Horthy codifies checklists designed to survive model churn.

## Bottom line

**Recommended for engineers designing their own agent runtime who want battle-tested principles for context ownership, state, and human checkpoints.**
Not for people who want regular written analysis, model research, or a neutral survey of alternatives, since his job is now to sell the stack that implements the principles.

## Changes

- 2026-09-24 - Created.

## See also

- [Hamel Husain](../hamel-husain/index.md) - the measurement-side counterpart to his architecture-side principles
- [Simon Willison](../simon-willison/index.md) - the daily landscape feed against his single-methodology depth
- [Context management patterns](../../context-management-patterns/index.md) - the pattern stream factor 3 anticipated and feeds
- [Steve Yegge](../steve-yegge/index.md) - the other builder-voice, one that declares manifestos where Horthy ships checklists

## References

- https://github.com/humanlayer/12-factor-agents - the guide: all twelve factors, licenses, 26.4k stars and 2.0k forks as of 2026-09-24, related resources and talks
- https://humanlayer.dev/ - the product pivot, tier pricing (Starter free to 3 members, Pro $100/user/mo), BYOK, and the "team that brought you context engineering" positioning
- https://github.com/ai-that-works/ai-that-works - the weekly show: episode list #1 through #76 with dates, hosts' bios, and per-episode code
- https://news.ycombinator.com/item?id=43699271 - the April 2025 Show HN (475 points, 78 comments) with his in-thread responses to critics
- https://theouterloop.substack.com/about - his Substack exists, its topic line, and its roughly two-year launch age
- https://simonwillison.net/tags/context-engineering/ - the community record of how the term spread (Lutke tweet, Karpathy amplification), used to weigh the coiner claim
- https://hn.algolia.com/api/v1/search?query=%2212-factor+agents%22&tags=story - 2026 re-posts of the guide drawing minimal traction, evidence on current mindshare
