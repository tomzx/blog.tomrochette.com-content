---
title: AutoGPT
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, agent-platform, workflows, source-available]
readability: 3
audience_notes: >
  Engineers evaluating hosted or self-hosted platforms for running long-running AI agent workflows on schedules and triggers.
  Assumes you remember the 2023 AutoGPT phenomenon and know what a workflow block is.
---

AutoGPT is the platform, frontend plus server, that Significant Gravitas rebuilt from the 2023 autonomous-agent phenomenon: today it is a hosted and self-hostable workflow runner where you describe an agent in plain English through AutoPilot or assemble it from blocks in a visual builder, then run it on demand, on a schedule, or from a trigger.

**The star count says museum, the commit log says startup: AutoGPT is one of the few 2023 phenomena that survived by shipping a genuinely different product, and the accurate reading of its 187k stars is that they measure the meme, not the platform.**

## What it is

Four surfaces on one platform per the README: AutoPilot (chat a job into a working agent), Agents (mission control for every run, cost, and approval), Marketplace (ready-made community agents), and Build (the visual canvas).
The stack is TypeScript and Python under the `autogpt_platform` directory, deployable on their cloud at platform.agpt.co or self-hosted from the repo.
The old classic agent, Forge, and the AG Benchmark remain in the repo under MIT, but the platform is where development happens.
It positions itself as "AI agents that finish the work", with file-aware agents, scheduled and event-based triggers, and an integration block library.

## Status

Active and shipping: the repo shows 187,658 stars and was pushed 2026-10-05, the day I checked (GitHub API, as of 2026-10-05).

[![Star History Chart](https://api.star-history.com/chart?repos=Significant-Gravitas/AutoGPT&type=date&legend=top-left)](https://www.star-history.com/?repos=Significant-Gravitas%2FAutoGPT&type=date&legend=top-left)

The platform releases on a cadence: beta v0.8.2 published 2026-09-30 (AutoPilot action gating modes: Ask First, Auto, and Unsupervised), v0.8.1 on 2026-09-24, v0.8.0 on 2026-09-19, v0.7.4 on 2026-09-04, v0.7.3 on 2026-08-28.
The repo was created 2023-03-16 and the launch thread pulled 153 points with 174 comments in April 2023, at the peak of the autonomous-agent craze.
License is dual: the platform folder is Polyform Shield (source-available, not OSI open source), everything outside is MIT.
A Team plan is marked "coming soon", which tells you the company is still mid-pivot from phenomenon to business.

## Strengths

- **It is the rare zombie-brand resurrection that actually shipped**: the same repo now runs a maintained platform with a real release cadence rather than a frozen meme.
- The block-based builder plus chat-based creation covers both the control-hungry and the conversation-first users in one product.
- Scheduling, triggers, and run visibility are first-class, which is what separates an agent platform from a demo.
- Self-hosting is real and documented, so the Polyform Shield license does not lock out internal deployments.

## Cautions

- **The name is now false advertising in both directions**: people who remember AutoGPT 2023 expect an autonomous loop, and people who want an MIT platform will find Polyform Shield instead.
- The 2023 heritage invites the old critique, and the "Auto-GPT Unmasked" thread's production-pitfall skepticism still reads correctly today: hype compounds faster than reliability.
- Platform folder under Polyform Shield means a competitor cannot build on it, which limits community forks of the part that matters.
- A Team plan listed as "coming soon" with contact-sales pricing signals an enterprise motion still under construction.

## Pricing

Hosted plans are credit-based: Pro at $42.50 per month billed annually (1x usage) and Max at $272.00 per month billed annually (8.5x usage), with yearly billing saving 15 percent versus monthly (as of 2026-09-27).
A Team plan is contact-sales and marked coming soon; self-hosting the platform is free under the licenses above.
An instant demo with no signup is offered.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-27 | Pro / Max | Baseline recorded: $42.50 / $272.00 per month billed annually | https://agpt.co/pricing |

## Compared to

- [LobeHub](../lobehub/index.md): the other hosted agent-operations platform; LobeHub grew out of a chat client toward scheduling, AutoGPT grew out of an autonomous loop toward structure, and they will meet in the middle.
- [Vibe Kanban](../vibe-kanban/index.md): choose it for developer-centric parallel coding agents; choose AutoGPT for non-coding business workflows with schedules and triggers.
- [Omnara](../omnara/index.md): the open control plane that supervises agents you already run, where AutoGPT wants to own the whole build-and-run loop.

## Bottom line

Recommended for teams that want hosted, scheduled, observable agent workflows and accept a source-available license for the platform.
Not for developers who need an OSI-licensed foundation to build a product on, and not for anyone expecting the 2023 autonomous experience.
My disagreeable claim: the 187k stars are a liability now, because they attract nostalgia traffic the product cannot serve and bury the platform it became.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars scan surfaced it.
- 2026-09-30 - Recorded beta v0.8.2 (September 30, AutoPilot action gating modes) as the new latest release and refreshed star and push counts.
- 2026-10-07 - Added the Significant-Gravitas/AutoGPT star history chart to the Status section.

## See also

- [LobeHub](../lobehub/index.md) - the hosted rival converging on the same agent-operations pitch
- [Vibe Kanban](../vibe-kanban/index.md) - the developer-side counterpart for parallel agent work
- [Omnara](../omnara/index.md) - the supervise-what-you-run alternative to owning the loop
- [Assistant runtimes](../../assistant-runtimes/_index.md) - the self-hosted platform category this sits beside

## References

- https://api.github.com/repos/Significant-Gravitas/AutoGPT - GitHub API (200): 187,582 stars, pushed 2026-09-27, Python, created 2023-03-16 (as of 2026-09-27)
- https://raw.githubusercontent.com/Significant-Gravitas/AutoGPT/master/README.md - four surfaces (AutoPilot, Agents, Marketplace, Build), platform pitch (200)
- https://raw.githubusercontent.com/Significant-Gravitas/AutoGPT/master/LICENSE - Polyform Shield for autogpt_platform, MIT for the rest (200)
- https://github.com/Significant-Gravitas/AutoGPT/releases - releases (200): platform beta v0.8.1 published 2026-09-24
- https://agpt.co/pricing - Pro $42.50 and Max $272.00 per month billed annually, Team coming soon (200, 2026-09-27)
- https://docs.agpt.co - AutoGPT Platform documentation (200)
- https://agpt.co/blog/introducing-the-autogpt-platform - the platform introduction post the LICENSE points to (200)
- https://hn.algolia.com/api/v1/items/35413054 - launch thread (200): 153 points, 174 comments, 2023-04-02
- https://hn.algolia.com/api/v1/items/35562821 - "Auto-GPT Unmasked: The Hype and Hard Truths of Its Production Pitfalls" (200): 90 points, 2023-04-13 (critical source)
