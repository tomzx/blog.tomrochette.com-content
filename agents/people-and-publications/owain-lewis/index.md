---
title: Owain Lewis
created: 2026-09-24
updated: 2026-10-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, youtube, agentic-coding, software-factory, claude-code]
readability: 3
audience_notes: >
  Engineers who want working agent infrastructure they can clone rather than just watch, built by a practicing engineering director.
  Assumes you already run Claude Code or Codex and can read Go and Rust.
---

Owain Lewis is a UK-based AI engineer and engineering director whose YouTube channel walks through the agent infrastructure he builds and open sources.

**He is the category's build-and-ship voice: every video is a working system (a software factory, a coding agent, a personal agent gateway) with the repo linked in the description, which makes him the member to clone from, and the boundary is that his scope is one-person and consultancy scale.**

## What it is

A YouTube channel (19K subscribers as of 2026-10-04) run by Owain Lewis, who describes himself as a principal AI engineer and engineering director with 20 years in software, now running his own AI consultancy.
Coverage is practical agentic engineering: agent loops, nested subagents, software factories, coding agents built from scratch, and Claude Code and Codex workflows.
Each video pairs with open source he maintains: Machinist (factory infrastructure, 455 stars), blueprint (agent skills, 403 stars), Push (a coding-agent gateway, 196 stars), Neo (a minimal multi-agent harness, 144 stars), and a youtube-tutorials companion repo.
Uploads run about weekly, and descriptions read like engineering writeups that state token costs, failure modes, and when he would not use his own build.

## Status

Active and steady at modest scale as of 2026-10-29.
The channel was created 2014-07-20 and shows 19K subscribers; the latest upload is "How Anthropic Reviews 30,000 Claude Code Changes a Day" (2026-10-26, 12,788 views within three days), a breakdown of the Claude Code team's layered review process that doubles as a demo of his Software Factory plugin, the 19th upload between 2026-05-15 and 2026-10-26, roughly one per week, reconfirmed against the RSS feed, after "My COMPLETE Workflow for Building Production AI Agents" (2026-10-12, about 21,561 views as of 2026-10-29).
The 2026-10-05 DevOps-agent upload reached 12,947 views and the 2026-09-28 "JEV Explained" sat at 10,555, while the 2026-09-21 "Inside OpenAI's Agentic Software Factory" climbed to 24,153 (all as of 2026-10-24).
Reach concentrates in the factory videos: "I Built an Agentic Software Factory" (2026-07-25) is his biggest recent at 82,379 views, while most uploads land between 3,000 and 30,000.
Trajectory is upward without a breakout, and his roughly 1.2K combined GitHub stars across the pinned repos carry more durable weight than the sub count suggests.

## Strengths

- Every claim comes with a repo: the factories, agents, and gateways he demonstrates are runnable open source, not concept demos.
- Descriptions carry the numbers creators usually cut: around $2 of API spend in two days on the DeepSeek harness test, and explicit statements of when a build is the wrong tool.
- His testing surfaces findings the vendors announce differently: he nested Claude Code subagents roughly 30 levels deep after the announced cap was five, and showed Codex's max_depth guardrail as the fix.
- The weekly cadence follows one coherent thread (factory thinking applied to a single engineer's workflow), so older videos stay usable instead of expiring.

## Cautions

- The funnel has graduated from email capture to paid membership: descriptions now point at his $67/month Skool community ("work with me"), the newest video carries a Google Cloud sponsorship, and the aiengineer.co email capture persists in older descriptions, so treat the free-skills funnel as the business model it is.
- The scope is one-person consultancy scale: his factory runs his backlog, not a regulated enterprise codebase, so transplant the patterns rather than the numbers.
- No critical community filter exists: Hacker News has zero threads on his channel content (searched again 2026-10-24), so his techniques have not been stress-tested in public argument.
- View counts are modest, so the community surface for catching errors in his techniques is thin.

## Pricing

The videos are free to watch (as of 2026-10-24).
The funnel around them is paid: his "AI Engineer" Skool community lists at $67/month (150 members as of 2026-10-24), the aiengineer.co starter resources remain a free email capture, and the newest video adds sponsor revenue (Google Cloud).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-24 | AI Engineer Skool community | Baseline: videos free; community listed at $67/month with 150 members; free resources still behind the aiengineer.co email capture. | https://www.skool.com/aiengineer/about |

## Compared to

- [IndyDevDan](../indydevdan/index.md): both build software factories in public, but Dan publishes weekly concept frameworks with louder packaging while Owain publishes quieter end-to-end builds you clone directly.
- [AI Jason](../ai-jason/index.md): both walk through complete working workflows, but Jason's builds target everyday app use cases while Owain's target the engineering loop itself.
- [Caleb Writes Code](../caleb-writes-code/index.md): use Caleb for same-week release explainers and Owain when you want to see a system built and open sourced around one.

## Bottom line

**Recommended for engineers who learn by cloning: his value is the linked repos and the stated tradeoffs, not the watching.**
Not for someone who wants model-release news, enterprise-scale case studies, or a large community already testing the techniques.

## Top 5 recommended reading

- [Agent Loops: Complete Guide (Claude Code + Codex)](https://www.youtube.com/watch?v=RVEaDvh6f5A) - The most complete single artifact of his method: manager and worker loops over GitHub issues, including the guardrails and evals most people skip.
- [I Built an Agentic Software Factory with Codex and Claude Code](https://www.youtube.com/watch?v=AbpyqAfxZ8c) - His biggest recent video (82,379 views as of 2026-10-24) and the clearest statement of the factory pattern, ticket to pull request with worktree isolation plus the limits he states himself.
- [Build Your Own Coding Agent Like Pi (With 1 Prompt)](https://www.youtube.com/watch?v=QER-0DaC-Gk) - Demystifies harness engineering by building a working coding agent in one Go file, then names what a minimal agent still lacks.
- [I Built A Self-Improving AI Software Factory](https://www.youtube.com/watch?v=ZDOTYfJBuLw) - Shows the measurement layer (run data, evals, model comparison) that turns a factory from a demo into a system that improves.
- [Claude Code's New Subagent Feature](https://www.youtube.com/watch?v=ZdXsRn9w0VE) - The nested-subagent video with the 30-level finding and the orchestrator, worker, sub-worker pattern he uses day to day.

## Changes

- 2026-09-24 - Created.
- 2026-10-02 - Status recency refreshed: 16 uploads between May 15 and September 28, 2026, the latest "JEV Explained (Real Use Cases)" (2026-09-28).
- 2026-10-05 - The RSS feed serves again after its 2026-10-04 outage and reconfirms no upload newer than "JEV Explained (Real Use Cases)" (2026-09-28); the reference line updated to match.
- 2026-10-06 - New upload "I Built A Claude DevOps Agent To Run My Software Factory" (2026-10-05) became the latest, making 17 uploads between May 15 and October 5, 2026; Status and the reference line updated (feed fetched this run).
- 2026-10-24 - New upload "My COMPLETE Workflow for Building Production AI Agents" (2026-10-12) became the latest, making 18 uploads between May 15 and October 12, 2026; the funnel shift to the $67/month Skool community and the first Google Cloud sponsorship recorded in Cautions, and the Pricing and Price history sections added (Skool page, feeds, and searches fetched this run).
- 2026-10-29 - New upload "How Anthropic Reviews 30,000 Claude Code Changes a Day" (2026-10-26) became the latest, making 19 uploads between May 15 and October 26, 2026; RSS feed fetched this run.

## See also

- [IndyDevDan](../indydevdan/index.md) - the louder weekly counterpart building the same factory concepts
- [Machinist](../../software-factory/machinist/index.md) - the software factory infrastructure he demonstrates on the channel
- [AI Jason](../ai-jason/index.md) - the other complete-workflow builder in this category
- [Pi](../../harnesses/pi/index.md) - the open coding agent his Neo build and factory videos build around

## References

- https://www.youtube.com/@owainlewis - the channel: identity and 19K subscribers as of 2026-10-04
- https://www.youtube.com/feeds/videos.xml?channel_id=UC08YjBHjjPFu8T1KbHGomnQ - the RSS feed that grounds cadence, titles, dates, view counts, and the 2014-07-20 channel creation through the 2026-10-12 upload (uploads-tab fetches still render as JavaScript shells)
- https://www.skool.com/aiengineer/about - the $67/month Skool community the newest descriptions funnel to: pricing, member count, and what the membership includes
- https://github.com/owainlewis - the GitHub profile linking this channel, with bio, location, and pinned repo star counts
- https://owainlewis.com - the personal site: positioning, newsletter, and community links
- https://aiengineer.co/start - the free starter pack and email funnel behind the older video descriptions, now sharing description space with the Skool community link
- https://hn.algolia.com/api/v1/search?query=%22owain%20lewis%22&hitsPerPage=8 - zero Hacker News hits for the name, the missing critical coverage
- https://hn.algolia.com/api/v1/search?query=owainlewis&hitsPerPage=5 - 82 hits with the oldest visible from 2014 to 2015 (Forth links, awesome lists, early startups), grounding his long engineering history and the absence of current channel discussion
