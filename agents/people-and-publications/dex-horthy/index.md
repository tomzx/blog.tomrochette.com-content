---
title: Dex Horthy
created: 2026-09-24
updated: 2026-11-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, developer, agents, context-engineering]
readability: 3
audience_notes: >
  Engineers building LLM-powered software who want production-grade principles for agent architecture, owned context windows, and human checkpoints.
  Assumes you have tried an agent framework, hit its quality ceiling around 80 percent, and are deciding what to build yourself.
---

Dex Horthy is the founder of HumanLayer and author of 12-Factor Agents, the most-starred open methodology for building reliable LLM applications.

**His sustained publication is not a blog but a methodology plus a weekly live show: 12-Factor Agents gave agent builders a shared vocabulary for owning context, and the weekly AI That Works recordings document the practice in public, while the written cadence is irregular and everything now routes into a commercial product.**

## What it is

12-Factor Agents (github.com/humanlayer/12-factor-agents) states twelve principles, including own your prompts, own your context window, tools are just structured outputs, contact humans with tool calls, and make your agent a stateless reducer, under a CC BY-SA 4.0 content license, with 26.7k stars and 2.0k forks as of 2026-10-15.
AI That Works is his weekly Zoom show and podcast with Vaibhav Gupta (BAML), every Tuesday at 10 AM PST, 79 aired numbered episodes dated from 2025-03-31 through 2026-10-27, each with code in a public repo, with #80 (Using AI for Writing) scheduled for 2026-11-03.
The Outer Loop is his Substack ("AI Agents, Human in the Loop, maybe-agi", launched about two years ago), with the archive behind the subscribe wall.
HumanLayer itself pivoted from a human-approval API into a multiplayer coding-agent workspace (local daemons, cloud daemons, tasks and artifacts, an RPI-to-QRSPI workflow), with a free Starter tier for teams of up to three, Pro at $100/user/month, and BYOK for Claude Code, Codex, and Copilot.
The open-source story moved in two steps in 2026: from June 2026 the repo's own README declared the earlier open-source code, the human-approval HITL control included, largely deprecated ("pretty much all deprecated") in favor of a closed rebuild, and on 2026-10-22 the repo itself became the rebuilt workspace's open-source monorepo (Apache-2.0, 12.8k stars as of 2026-11-05), with the earlier code preserved on the legacy branch and the legacy-final tag.

## Status

Active on a talk-first cadence.
AI That Works ran through #77 (2026-10-06, Building a Memory Pipeline), #78 (the Software Factory Debate with Warp's CTO Zach, aired 2026-10-20 per the show repo's episode list, which moved it from the 10-13 slot the last check recorded), and #79 (Building Evals on Production Data, aired 2026-10-27), with #80 (Using AI for Writing) slated for 2026-11-03 but still flagged upcoming in the show repo's episode list as of 2026-11-05, so 79 aired numbered episodes through #79 remains the count and the dependable publication is the weekly recorded conversation.
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
- The open-source history is choppy: the site's FAQ still answers "not yet" to whether HumanLayer is open source even though the repo has carried the rebuilt product under Apache-2.0 since 2026-10-22, and the original open-source HITL code that factor 7's vocabulary grew from sits deprecated on the legacy branch, so read the site and the repo together.

## Pricing

The methodology and the show are free; HumanLayer the product is paid: a free Starter tier for teams of up to three members and Pro at $100/user/month with BYOK for Claude Code, Codex, and more, plus a custom-priced Enterprise tier.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-24 | HumanLayer Pro | Baseline: Starter free for teams of up to three; Pro $100/user/month with BYOK. | https://humanlayer.dev/ |

## Compared to

- [Hamel Husain](../hamel-husain/index.md): Husain's discipline is measurement and evals, Horthy's is architecture and control flow; read Husain when you do not know whether it works, Horthy when you must decide what to own.
- [Simon Willison](../simon-willison/index.md): Willison documents the whole landscape daily, Horthy argues one methodology weekly; breadth versus a single playbook.
- [Steve Yegge](../steve-yegge/index.md): both are opinionated builders with products; Yegge declares manifestos that his code may later falsify, Horthy codifies checklists designed to survive model churn.

## Bottom line

**Recommended for engineers designing their own agent runtime who want battle-tested principles for context ownership, state, and human checkpoints.**
Not for people who want regular written analysis, model research, or a neutral survey of alternatives, since his job is now to sell the stack that implements the principles.

## Top 5 recommended reading

- [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) - The methodology itself, twelve principles from owning your context window to stateless reducers, the vocabulary agent builders now share.
- [12-Factor Agents: Patterns of reliable LLM applications (AI Engineer talk)](https://www.youtube.com/watch?v=8kMaTybvDUw) - His 17-minute AI Engineer World's Fair talk, the fastest way to hear the argument in his own voice.
- [12-factor Agents: Patterns of reliable LLM applications (Show HN thread)](https://news.ycombinator.com/item?id=43699271) - The launch thread where he answered framework defenders, eval skeptics, and cost arguments point by point.
- [AI That Works](https://github.com/ai-that-works/ai-that-works) - The weekly show he runs with Vaibhav Gupta, 79 aired numbered episodes with working code for every claim.
- [A Brief History of Ralph](https://humanlayer.dev/blog/brief-history-of-ralph) - His first-person account of the viral Ralph Wiggum loop technique, his best durable blog post.

## Changes

- 2026-09-24 - Created.
- 2026-09-24 - Added the Top 5 recommended reading section.
- 2026-10-07 - Episode #77 (Building a Memory Pipeline) confirmed aired on schedule on 2026-10-06 per the show repo's episode list, replacing the "scheduled" wording in Status.
- 2026-10-15 - Episode #78 (the Software Factory Debate with Warp's CTO) confirmed aired on schedule on 2026-10-13 with #79 scheduled for 2026-10-20, and the 12-Factor Agents count moved to 26.7k stars; show repo and GitHub API fetched this run.
- 2026-10-29 - Rotation re-verification, every cited URL re-fetched and live: #78 confirmed aired 2026-10-20 (the show repo moved it off the 10-13 listing the last check recorded), #79 aired 2026-10-27, and #80 is scheduled for 2026-11-03, so the aired-episode count moved to 79; added the Pricing and Price history sections the note format mandates (the $100/user/month Pro price is unchanged).
- 2026-11-05 - Out-of-rotation accuracy check on the humanlayer open-source HITL handoff, with every cited URL re-fetched this run: confirmed the repo's own README carried from June 2026 until the pivot ("pretty much all deprecated ... try the rebuild") and the 2026-10-22 pivot commit that open-sourced the rebuilt workspace monorepo (Apache-2.0, 12.8k stars as of 2026-11-05) while moving the earlier open-source code, the HITL approval control included, to the legacy branch and the legacy-final tag; What it is, Cautions, and References updated, and Status notes #80 still flagged upcoming in the show repo after its 2026-11-03 slot.

## See also

- [Hamel Husain](../hamel-husain/index.md) - the measurement-side counterpart to his architecture-side principles
- [Simon Willison](../simon-willison/index.md) - the daily landscape feed against his single-methodology depth
- [Context management patterns](../../context-management-patterns/index.md) - the pattern stream factor 3 anticipated and feeds
- [Steve Yegge](../steve-yegge/index.md) - the other builder-voice, one that declares manifestos where Horthy ships checklists

## References

- https://github.com/humanlayer/12-factor-agents - the guide: all twelve factors, licenses, 26.7k stars and 2.0k forks as of 2026-10-15, related resources and talks
- https://humanlayer.dev/ - the product pivot, tier pricing (Starter free to 3 members, Pro $100/user/mo), BYOK, and the "team that brought you context engineering" positioning
- https://github.com/ai-that-works/ai-that-works - the weekly show: episode list #1 through #78 with dates, hosts' bios, and per-episode code
- https://news.ycombinator.com/item?id=43699271 - the April 2025 Show HN (475 points, 78 comments) with his in-thread responses to critics
- https://theouterloop.substack.com/about - his Substack exists, its topic line, and its roughly two-year launch age
- https://simonwillison.net/tags/context-engineering/ - the community record of how the term spread (Lutke tweet, Karpathy amplification), used to weigh the coiner claim
- https://hn.algolia.com/api/v1/search?query=%2212-factor+agents%22&tags=story - 2026 re-posts of the guide drawing minimal traction, evidence on current mindshare
- https://raw.githubusercontent.com/humanlayer/humanlayer/99abe673498cf8bdcd5f989aebe9406a27185b3b/README.md - the June 2026 to October 2026 repo README declaring the open-source code "pretty much all deprecated" in favor of the rebuild
- https://github.com/humanlayer/humanlayer/commit/d8197bab07 - the 2026-10-22 pivot commit: the rebuilt workspace replaces the earlier open-source code, which stays on the legacy branch and the legacy-final tag
- https://github.com/humanlayer/humanlayer - the rebuilt open-source monorepo (Apache-2.0, 12.8k stars and 1.1k forks as of 2026-11-05) and its current workspace README
