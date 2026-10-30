---
title: Ray Amjad
created: 2026-09-24
updated: 2026-10-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, youtube, claude-code, agentic-coding, verification]
readability: 3
audience_notes: >
  Engineers who follow Claude Code releases closely and want each new feature explained and pressure-tested within days.
  Assumes you already use coding agents daily and know what hooks, subagents, and CLAUDE.md are.
---

Ray Amjad is an engineer-educator (ex-YC technical founder, Cambridge physics) whose YouTube channel turns each Claude Code and Codex release into a worked explanation with a verification-first argument attached.

**He is the fastest way to understand a Claude Code feature drop in depth, and the only channel in this batch that states it has never accepted a sponsor, with the boundary that his videos are also the top of a cohort funnel and his own products are his demos.**

## What it is

A YouTube channel (50K subscribers as of 2026-10-04) run by Ray Amjad, who builds agent-first software under his holding company 21 Dreams (AgentStack, Impello AI, and the open-source HyperWhisper).
Coverage is Claude Code centric: hooks, forked and nested subagents, output styles, dynamic workflows, and the monitor tool, each explained with a working demo within days of release, plus concept videos on loop engineering and verification.
Every description states that he has never accepted a sponsor and that his own products keep the channel running.
The funnel is agenticcoding.school: a two-week cohort (the newest video descriptions title it "My Agent-Era Engineer Cohort", the September run's name; the October run page titled it "The Software Factory Engineer" with 190 lessons for the 2026-10-26 to 2026-11-06 dates, and the September run carried 237 lessons), evergreen Claude Code and Codex classes, company training, and consulting.

## Status

Active and growing as of 2026-10-29.
The channel was created 2019-08-09 and shows 50K subscribers; the RSS feed (refetched 2026-10-29) shows 19 uploads between 2026-04-09 and 2026-10-26, still two to three per month with bursts around Anthropic releases.
The newest upload is "Anthropic's New Subagent Rules Will Change How You Build" (2026-10-26, on Anthropic's guidance for when to fold subagents back into the main loop), after "Karpathy Is Right: Your Attention Is the New Bottleneck" (2026-10-20), "Your Prompts Are Too SMALL for Claude Code" (2026-10-18), and "The S TIER Claude Code Mods" (2026-10-12).
Reach is concentrated and rising: "How to Use Jev + Claude Code" (2026-09-18, retitled from "Jev + Claude Code = The Cheapest Agentic Coding Loop Yet") passed 150,259 views within a week and 172,522 as of 2026-10-29, the Opus 5 output-styles video passed 102,888, and typical uploads run 10,000 to 46,000.
His cohort page claims 4,000+ engineers taught and 5,000+ hours in Claude Code and Codex, self-reported figures I found nowhere else.

## Strengths

- Depth per release is his edge: he reads the change, surfaces the undocumented details (for example the function-hooks environment variable when hooks shipped disabled by default), and demos edge cases in one video.
- The verification thesis is a real argument rather than a mood: generation is solved so the bottleneck moved, prefer a verifier over an instruction, and merge gates that scale with blast radius.
- He watches adjacent experiments (cmux peer sessions, Codex managed threads, Anthropic observer agents) and connects them into patterns before they are mainstream.
- With no sponsor reads, there is no advertiser incentive to stretch a claim, though the cautions below show where his incentive actually sits.

## Cautions

- Every video ends in the cohort pitch: the channel is a content layer for agenticcoding.school, so the free material is the introduction, not the product.
- His products are his demos: videos touching AgentStack, Impello, or HyperWhisper blur the line between coverage and advertisement for his own stack.
- The credentials (4,000+ taught, 5,000+ hours, "most in-depth Claude Code content on YouTube") are self-reported and unverified by any third party I could find.
- The third-party footprint is thin: zero Hacker News threads mention him as of 2026-09-24, so nothing he claims has yet been publicly criticized or corrected, which cuts both ways.

## Compared to

- [IndyDevDan](../indydevdan/index.md): both sell cohort courses and coin vocabulary, but Ray is Claude Code release first and verification first while Dan is harness first, model-stacking first, and weekly.
- [Caleb Writes Code](../caleb-writes-code/index.md): both cover Claude Code updates fast, but Caleb compresses to short illustrated explainers while Ray goes deep on one feature with a setup you can copy.
- [Boris Cherny](../boris-cherny/index.md): Boris is the Claude Code creator speaking from inside the tool; Ray is the most dedicated outside analyst of the same surface.

## Bottom line

**Recommended for engineers who want every Claude Code release explained with depth and a verifier-first mental model, and who can discount the course funnel.**
Not for someone who wants vendor-agnostic coverage, or who minds that the demos showcase his own products.

## Pricing

The videos are free and he states he has never accepted a sponsor; revenue comes from agenticcoding.school (paid cohort, evergreen classes, company training, and consulting) and his own products (Impello AI, AgentStack, HyperWhisper). No prices are published on the public pages fetched for this note.

## Top 5 recommended reading

- [How to Use Jev + Claude Code](https://www.youtube.com/watch?v=ScvXFi4MUSc) - His biggest video (171,845 views as of 2026-10-22, retitled from "Jev + Claude Code = The Cheapest Agentic Coding Loop Yet") and the best single tour of his current thinking: skill selection, feedback loops, adversarial testing, and code review on the newest cheap model.
- [Anthropic Just Dropped the Biggest Claude Code Update Yet](https://www.youtube.com/watch?v=B-YQANvDOq0) - The hooks release explained with the undocumented enable flag, a secret redactor, and deploy gating, the video to copy settings from.
- [Claude Code Just Made Subagents Feel Obsolete](https://www.youtube.com/watch?v=oqp6D-ugtX4) - His argument against in-process subagents, using cmux peer sessions and stacked pull requests as the alternative architecture.
- [Loop Engineering: The Future of AI Coding?](https://www.youtube.com/watch?v=2-0lxK2wgJ8) - The concept video that frames inner and outer loops and Slack as a memory layer, his vocabulary at its most useful.
- [Anthropic Just Dropped the Update Everyone's Obsessed With: Dynamic Workflows](https://www.youtube.com/watch?v=c0gVowvMR-g) - Dynamic workflows demoed with his own workflow-creator skill, including when not to reach for them.

## Changes

- 2026-09-24 - Created.
- 2026-10-05 - The RSS feed serves again after its 2026-10-04 outage and reconfirms no upload newer than "Jev + Claude Code = The Cheapest Agentic Coding Loop Yet" (2026-09-18); Status and the reference line updated to match.
- 2026-10-22 - Full re-verification, rotation: all cited URLs refetched and live; the RSS feed shows three new uploads (2026-10-12, 2026-10-18, 2026-10-20) with "Karpathy Is Right: Your Attention Is the New Bottleneck" now newest, the Jev video retitled to "How to Use Jev + Claude Code", and the cohort renamed to "The Software Factory Engineer" (190 lessons, 2026-10-26 to 2026-11-06 run); Status, What-it-is, Top 5, and References updated to match.
- 2026-10-29 - A fourth upload since the rotation: "Anthropic's New Subagent Rules Will Change How You Build" (2026-10-26) is now newest, making 19 uploads between April 9 and October 26; the Jev video passed 172,522 views and the newest video descriptions are back to the "My Agent-Era Engineer Cohort" title; RSS feed fetched this run; added the Pricing section the note format mandates.

## See also

- [IndyDevDan](../indydevdan/index.md) - the weekly harness-first counterpart covering overlapping releases
- [Caleb Writes Code](../caleb-writes-code/index.md) - the faster, shallower Claude Code news layer
- [Claude Code](../../harnesses/claude-code/index.md) - the tool nearly every video dissects
- [Context management patterns](../../context-management-patterns/index.md) - the section essay behind the context-engineering chapters he teaches

## References

- https://www.youtube.com/@RAmjad - the channel: identity and 50K subscribers as of 2026-10-04
- https://www.youtube.com/feeds/videos.xml?channel_id=UCLA7cJBnqr0nLF2bQBD9uUg - the RSS feed that grounds cadence, titles, dates, view counts, the no-sponsor statement, and the 2019-08-09 channel creation (it 404ed on 2026-10-04, serves again since 2026-10-05, and was refetched 2026-10-22, where it showed three new uploads through 2026-10-20)
- https://www.rayamjad.com/ - the personal site: 21 Dreams studio, consulting, and company registration
- https://github.com/ray-amjad - the GitHub profile (Tokyo) whose pinned repos match the video-description links, closing the identity loop
- https://www.agenticcoding.school/cohort - the cohort page: positioning claims, syllabus, products, and the commercial model
- https://hn.algolia.com/api/v1/search?query=%22ray%20amjad%22&hitsPerPage=8 - zero Hacker News hits for the name, the thin third-party footprint
