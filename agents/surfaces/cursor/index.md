---
title: Cursor
created: 2026-08-23
updated: 2026-10-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, surfaces, ai-editors, anysphere]
readability: 3
audience_notes: >
  Engineers picking an AI-native editor who want to know what Cursor is now that SpaceX owns it.
  Assumes you have used an editor with an agent or a terminal harness, and know what a VS Code fork is.
---

Cursor is the AI-native editor by Anysphere: a VS Code fork grown into a platform with a CLI, cloud agents, and its own models, and since August 14, 2026 a part of SpaceX.

**Cursor stopped being an editor company in 2026: it is now a compute-distribution play, and a team that standardizes on it is buying SpaceX's GPU fleet with an IDE attached.**

## What it is

**A VS Code fork turned platform: the editor plus a CLI, cloud agents that run for hours or days, scheduled automations, a Slack integration, mobile, and Bugbot for agent code review.**
Model access spans Anthropic, Google, and xAI (whose Grok arrived through the SpaceXAI partnership), plus Cursor's own Composer models and a marketplace for team rules, skills, and plugins; the rules system covers Cursor's own project, user, and team rules and also reads AGENTS.md files from the project root and subdirectories.
OpenAI notified Anysphere on August 28, 2026 that it is winding down Cursor's direct model access, with a November 12, 2026 shutoff and no new OpenAI models during the transition.

## Status

**Active, dominant, and acquired.**
SpaceX completed the acquisition on August 14, 2026, closing a process that started with the SpaceXAI training partnership announced in April 2026, and the June 2026 announcement thread carried a $60 billion price.
The vendor-announced 2026 record includes a Gartner Magic Quadrant Leader placement (May) and an agent-security certification (August).
On August 31, 2026 the OpenAI split went public: OpenAI cited terms-of-service confidence after the acquisition, Cursor's CEO put OpenAI models at about 5% of user traffic, and Anthropic publicly committed to keep serving Claude models in Cursor.
As of 2026-10-05 the November 12, 2026 shutoff stands unrevised: OpenAI's own announcement still frames the date as proposed and no later reporting moves it, and the models docs still list OpenAI models without a removal notice.

## Strengths

- **The most complete agentic editor stack shipping**: local agent, cloud fleets, automations, review, CLI, mobile, and marketplace under one subscription.
- Composer and Grok models give it a first-party quality floor no plugin-based rival matches.
- Privacy mode carries a no-training guarantee, and enterprise controls cover SSO, audit logs, and MCP policy.
- The 2026 posts alone cover certification, analyst placement, and the acquisition, so the shipping cadence is visible from the blog index.

## Cautions

- **Ownership concentration is the caution, and it stopped being hypothetical on August 28, 2026**: the editor layer merging with the compute layer is the vertical integration antitrust language exists for, OpenAI invoked its contract's termination right within two weeks of closing, and customers have no seat at that table.
- The April 2025 support incident, where a hallucinated lockout policy triggered cancellations, remains the canonical example of AI support gone wrong.
- Usage-based billing on top of subscriptions is where teams get hurt, and the limits are opaque ("extended limits", "20x Pro") until you hit them.
- It is a fork, so upstream VS Code work lands late or never.

## Pricing

Hobby is free with limited agent requests and access to Composer.
Individual plans are $20/month (Pro, with Pro+ at 3x and Ultra at 20x agent limits).
Teams Standard is $40/user/month and Teams Premium is $120/user/month with 5x the Standard agent limits, Enterprise is custom, and on-demand usage bills in arrears on the paid tiers, as of 2026-10-05.
A Start plan for developers in India costs ₹649/month, tax inclusive, covering the first-party model pool and cloud agents.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | All tiers | Baseline: Hobby free with limited agent requests, Individual Pro $20/mo (Pro+ at 3x, Ultra at 20x limits), Teams Standard and Premium $40/user/mo, Enterprise custom, on-demand usage billed in arrears. | [cursor.com/pricing](https://cursor.com/pricing) |
| 2026-10-05 | Teams Premium | Corrected: Teams Premium is $120/user/mo with 5x the Standard agent limits, where the baseline row carried it at $40 alongside Standard; Standard stays $40/user/mo. A Start plan for India (₹649/mo) sits outside the listed ladder. | [cursor.com/docs/models-and-pricing](https://cursor.com/docs/models-and-pricing) |

## Compared to

- [VS Code + Copilot](../vscode-copilot/index.md): the default-path rival; pick VS Code for openness and price, Cursor for the integrated experience.
- [Zed](../zed/index.md): faster and cheaper with no platform ambitions; pick Zed when the editor is the product you want.
- [Windsurf](../windsurf/index.md): the cautionary tale of this market's volatility; read it before betting a team on any single AI editor.

## Bottom line

**Recommended for teams that want the strongest turnkey agentic editor and accept vendor concentration as the price.**
Not for anyone who needs an open, auditable toolchain or a predictable bill.

## Changes

- 2026-08-23 - Created in the Surfaces category seed.
- 2026-08-26 - Resolved the Grok ownership contradiction by tying Grok to the SpaceXAI partnership.
- 2026-09-02 - Recorded the OpenAI wind-down (notice August 28, 2026, model access shutoff November 12, 2026).
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-27 - Re-confirmed the November 12, 2026 OpenAI shutoff unrevised and the plan prices unchanged.
- 2026-10-05 - Corrected the Teams pricing (Premium is $120/user/mo with 5x Standard limits, not $40) per the models-and-pricing docs, added the India-only Start plan (₹649/mo), and recorded AGENTS.md support alongside Cursor's own rules; the November 12 OpenAI shutoff stands unrevised.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [ai-tools-i-have-used](../../../ai-tools-i-have-used/index.md) - how fast editor allegiances rotate in practice
- [The Shifting Bottleneck](../../../the-shifting-bottleneck/index.md) - why editor AI quality stopped being the constraint
- [Rolling Out the Unread Review](../../../rolling-out-the-unread-review/index.md) - what Bugbot-style review has to survive organizationally

## References

- https://cursor.com/pricing - tiers, limits language, privacy mode, as of 2026-10-05
- https://cursor.com/docs/models-and-pricing - plan ladder including Teams Premium $120 and the India Start plan, cloud agents, automations, and Cursor for iOS, as of 2026-10-05
- https://cursor.com/docs/rules - the rules system and AGENTS.md support in project root and subdirectories, as of 2026-10-05
- https://cursor.com/blog/joining-spacex - the August 14, 2026 acquisition completion post
- https://devops.com/openai-cuts-off-cursors-model-access-after-spacex-acquisition/ - the OpenAI wind-down, the November 12, 2026 shutoff, and the 5% traffic claim, September 2026
- https://cursor.com/docs - product surfaces and configuration
- https://news.ycombinator.com/item?id=48553224 - the June 2026 acquisition announcement thread
- https://news.ycombinator.com/item?id=43683012 - the April 2025 support-hallucination incident thread
