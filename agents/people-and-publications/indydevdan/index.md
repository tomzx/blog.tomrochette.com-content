---
title: IndyDevDan
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, youtube, agentic-engineering, claude-code, harness-engineering]
readability: 3
audience_notes: >
  Engineers who want a conceptual stack (prompt, context, harness, factory) that organizes agentic coding, taught weekly in video form.
  Assumes you already use Claude Code or a similar agent and can judge hype on your own.
---

IndyDevDan (Dan, GitHub disler) runs the YouTube channel that named and normalized "agentic engineering," publishing weekly videos plus the open source repos behind them and the Tactical Agentic Coding course they sell.
Facts below verified as of 2026-09-24.

**He is the category's vocabulary engine on its most consistent weekly cadence, mapping prompt, context, and harness engineering into frameworks engineers actually reuse, with the boundary that the framing always climbs toward his course and the titles shout.**

## What it is

A YouTube channel (149K subscribers as of 2026-09-24, created 2020-12-23) run by Dan, a 15+ year engineer whose GitHub bio reads "Betting the next 10 years of my career on AGENTIC software."
Videos fall into three lanes: concept frameworks (the core four of context, model, prompt, and tools, the operating-level model, software factories, agent swarms, model fusion), release-adjacent builds (fixing Opus 5's verbosity with system prompts, benchmark re-rankings), and devlogs that ship a real repo such as a self-compacting Pi agent.
Every video pairs with open source under github.com/disler, including claude-code-hooks-mastery (3.9K stars), pi-vs-claude-code (1.7K stars), and super-simple-software-factory (887 stars).
The commercial engine is agenticengineer.com, which sells Principled AI Coding (phase 1) and Tactical Agentic Coding (phase 2).

## Status

Active and metronomic as of 2026-09-24.
Uploads run weekly, every Monday at 13:00 UTC, and the RSS feed shows 15 consecutive Mondays from 2026-06-15 to 2026-09-21 with no gaps.
Recent videos land between 12,700 and 127,800 views, with "FORGET Loop Engineering" at 127,800 and the agent-swarms takeaways at 79,785.
Hacker News mentions him in six comment threads between 2025-04 and 2026-09, the only channel of this batch with third-party discussion at all.

## Strengths

- The frameworks are the product and they are reusable: the core four, the leverage-versus-control trade across operating levels, and the factory-as-leverage argument give engineers a shared map.
- He ships the repos: claude-code-hooks-mastery, the multi-agent observability app, and super-simple-software-factory are widely starred, so the videos come with working code.
- Benchmark coverage is contrarian in a useful way: he argues an index is a proxy of a proxy, picks five benchmarks including alignment and hallucination behavior, and re-ranks models on cost and speed rather than score alone.
- Hacker News users who dislike the style still credit the substance: "Despite his sensationalism, he does quick reviews of new CC features that you just have to see to understand," and his git-status command gets attributed in the wild.

## Cautions

- The titles are engineered for the algorithm ("Intelligence EXPLOSION", "BANNED", "ZERO HYPE"), and the site's founder letter runs on evolve-or-die survival pressure, so strip the framing before adopting the technique.
- Every video funnels to Tactical Agentic Coding, so treat the free content as the course syllabus in reverse: concepts resolve to the paid product.
- Maximalist claims ("There is no wall, there are no limits") are branding, and the swarm and factory videos demo on toy codebases at his own scale.
- The hype cadence means his "this changes everything" of three months ago is often quietly superseded, so watch the repos for what he actually keeps using.

## Compared to

- [Owain Lewis](../owain-lewis/index.md): both build software factories in public, but Dan publishes weekly frameworks with louder packaging while Owain publishes quieter end-to-end builds you clone directly.
- [Ray Amjad](../ray-amjad/index.md): both sell cohorts and explain Claude Code releases, but Ray goes feature-deep and verification-first while Dan goes concept-wide and harness-first.
- [AI Jason](../ai-jason/index.md): both are the category's workflow-builder video voices, but Jason optimizes for usable app workflows while Dan optimizes for engineering worldview.

## Bottom line

**Recommended for engineers who want a weekly conceptual map of agentic coding and will take the frameworks while skipping the shouting.**
Not for someone allergic to hype framing, or who wants vendor-neutral depth without a course funnel.

## Top 5 recommended reading

- [My Super Simple Software Factory (For Agentic Engineers)](https://www.youtube.com/watch?v=haUfb1ievTE) - The clearest single statement of his factory thesis, agents plus code with deterministic gate checks, given away free with the repo.
- [FORGET Loop Engineering. Agentic Engineering is about THIS](https://www.youtube.com/watch?v=VQy50fuxI34) - His most-watched recent video (127,800 views), arguing loops are a rebrand and AI developer workflows are the actual unit of leverage.
- [FIXING Opus 5: PROOF that Prompt Engineering IS NOT DEAD](https://www.youtube.com/watch?v=S_QdQ1G4GlU) - The system-prompt-as-law method (positive and negative patterns, aliases, hard boundaries) applied to a real model's real failure modes.
- [Agentic Engineering Operating Level: WHERE to FOCUS your AGENTS?](https://www.youtube.com/watch?v=rPWCYB62wvI) - His best framework video: five operating levels and the rule for choosing leverage versus control.
- [Are Agent Swarms USEFUL? OpenAI's GPT-6 Astra SWARM Takeaways](https://www.youtube.com/watch?v=S2sjyokoxeE) - Turns the OpenAI swarm incident into engineering rules (mailboxes, kill switches, sandboxes) and runs three real swarms with costs shown.

## Changes

- 2026-09-24 - Created.

## See also

- [Super Simple Software Factory](../../software-factory/super-simple-software-factory/index.md) - the repo behind his factory videos, with its own research note
- [Pi](../../harnesses/pi/index.md) - the open harness his pi-vs-claude-code and devlog builds center on
- [Ray Amjad](../ray-amjad/index.md) - the Claude Code release deep-dive peer covering the same beat differently
- [Owain Lewis](../owain-lewis/index.md) - the quieter factory builder in the same batch
- [Claude Code](../../harnesses/claude-code/index.md) - the harness most of his repos extend

## References

- https://www.youtube.com/@indydevdan - the channel: identity and 149K subscribers as of 2026-09-24
- https://www.youtube.com/feeds/videos.xml?channel_id=UC_x36zCEGilGpB1m-V4gmjg - the RSS feed grounding the weekly Monday cadence, titles, dates, view counts, and the 2020-12-23 channel creation
- https://agenticengineer.com/ - the course site: both paid phases, the founder letter's rhetoric, and the blog
- https://github.com/disler - the GitHub profile confirming the IndyDevDan identity, follower count, and repo star counts
- https://hn.algolia.com/api/v1/search?query=indydevdan&hitsPerPage=8 - the Hacker News record: the sensationalism critique, the command attribution, and the prompting-series recommendation
