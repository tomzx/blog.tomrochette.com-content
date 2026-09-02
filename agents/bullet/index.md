---
title: Bullet
created: 2026-08-30
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, model-routing, benchmarks]
readability: 3
audience_notes: >
  Engineers comparing closed-source coding agents who know what SWE-bench Verified,
  model routing, and BYOK mean, and who care about latency more than feature depth.
---

Bullet is a closed-source coding agent (desktop app plus npm CLI) from a YC S26 startup whose entire pitch is latency: route simple tasks to fast models, search instead of embedding the repo, run tool calls in parallel, and kill stuck loops.
Facts below verified as of 2026-09-02.

**Bullet is the first harness to compete on speed rather than capability, and its benchmark write-up is the most transparent vendor self-report in the category, which makes the closed source the only thing standing between it and a serious look.**

## What it is

Built by a YC S26 team (the site says "Backed by Y Combinator") whose founders' note describes the origin as frustration waiting on Claude Code at their previous company.
The loop has three moves: route straightforward work to fast models and escalate only hard tasks, acquire context through targeted file reads (08% of the repo, by its own example) instead of embedding it, and execute independent tool calls in parallel while intercepting duplicates and stuck loops.
It runs GPT-5.6 Sol underneath, per its benchmark page.
Distribution is a desktop app (macOS, Linux, Windows) plus a Node 18+ CLI (`@trybullet/cli`, `npm install -g`, then `bullet`).
It is closed source: the npm package is marked UNLICENSED, its declared repository URL is dead, and only a releases-only GitHub repository is public.

## Status

v1.4.16 as of 2026-09-02, with that desktop build published to the releases repository on September 2, 2026.
The CLI shipped on npm on August 7, 2026 and did 654 downloads in the last week and 3,813 in the last month as of 2026-09-02 (the npm API's windows end August 29).
Its Launch HN on August 13, 2026 reached 121 points (item 49283063), ten days after a quiet 9-point Show HN.
Traction is real but early: thousands of installs, not millions, with YC backing as the deliberately stated signal behind it.

## Strengths

- **The benchmark disclosure sets the category standard**: 479 of 500 SWE-bench Verified (95.8%) in a single attempt, graded by the official Docker harness, at $0.73 mean cost and 119 seconds mean time, with all 500 patches and logs published.
- Latency as the design target is measured, not vibes: two thirds of the 500 tasks finished inside two minutes.
- Zero-friction trial: free, no API key required to start.

## Cautions

- **Closed source with a dead repo link in its npm metadata**, so you cannot audit the loop that reports its own numbers.
- The benchmark is self-reported; the production-harness-versus-mini-swe-agent comparison against Vals model rows is not independently reproduced.
- Monetization is unstated ("Free to use. No subscriptions."), which means the pricing story does not exist yet.
- Launch-thread top reactions were skepticism that YC funded another agent, plus onboarding bypass tricks users found in the app.

## Pricing

Free access today, explicitly with no subscriptions, as of 2026-09-02.

## Compared to

- [Claude Code](../claude-code/index.md): the incumbent it was built against; maturity and ecosystem versus raw latency.
- [Codex](../codex/index.md): an open Apache-2.0 client with subscription economics behind it, the opposite of Bullet's closed-and-free stance.
- [Amp](../amp/index.md): also closed and usage-billed but with documented plugins and orbs; Bullet is free while it works out how to charge.

## Bottom line

**Recommended for impatient engineers on strong machines who want a free second-opinion agent and will actually read the published patches.**
Not for teams that require auditable clients, and not for anyone betting on a pricing model that does not exist yet.
I think speed is the wrong axis for buying a coding agent, and a 119-second mean on a benchmark says nothing about the 40-minute debugging session you actually need it for.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where a latency-first entrant sits in the field
- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the routing logic Bullet automates away
- [Claude Code](../claude-code/index.md) - the harness its founders were waiting on
- [Codex](../codex/index.md) - the open-client alternative with subscription usage

## References

- https://www.codewithbullet.com - product surface, YC badge, CLI install, free access as of 2026-09-02
- https://www.codewithbullet.com/blog/benchmark-results.html - the SWE-bench Verified run: 479/500, 119 s mean, $0.73 per instance
- https://registry.npmjs.org/@trybullet%2Fcli - CLI version, UNLICENSED marker, and dead repository URL
- https://api.npmjs.org/downloads/point/last-month/@trybullet/cli - 3,813 monthly downloads as of 2026-09-02
- https://github.com/trybullet/bullet-releases - desktop release channel, v1.4.16 published September 2, 2026
- https://news.ycombinator.com/item?id=49283063 - 121-point Launch HN with YC S26 in the title and community skepticism
- https://news.ycombinator.com/item?id=49173799 - the earlier 9-point Show HN ten days prior
