---
title: Cursor
created: 2026-08-23
updated: 2026-09-03
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, surfaces, ai-editors, anysphere]
readability: 3
audience_notes: >
  Engineers picking an AI-native editor who want to know what Cursor is now that SpaceX owns it.
  Assumes you have used an editor with an agent or a terminal harness, and know what a VS Code fork is.
---

Cursor is the AI-native editor by Anysphere: a VS Code fork grown into a platform with a CLI, cloud agents, and its own models, and since August 14, 2026 a part of SpaceX.
Facts below verified as of 2026-09-03.

**Cursor stopped being an editor company in 2026: it is now a compute-distribution play, and a team that standardizes on it is buying SpaceX's GPU fleet with an IDE attached.**

## What it is

**A VS Code fork turned platform: the editor plus a CLI, cloud agents that run for hours or days, scheduled automations, a Slack integration, mobile, and Bugbot for agent code review.**
Model access spans Anthropic, Google, and xAI (whose Grok arrived through the SpaceXAI partnership), plus Cursor's own Composer models and a marketplace for team rules, skills, and plugins; OpenAI notified Anysphere on August 28, 2026 that it is winding down Cursor's direct model access, with a November 12, 2026 shutoff and no new OpenAI models during the transition.

## Status

**Active, dominant, and acquired.**
SpaceX completed the acquisition on August 14, 2026, closing a process that started with the SpaceXAI training partnership announced in April 2026, and the June 2026 announcement thread carried a $60 billion price.
The vendor-announced 2026 record includes a Gartner Magic Quadrant Leader placement (May) and an agent-security certification (August).
On August 31, 2026 the OpenAI split went public: OpenAI cited terms-of-service confidence after the acquisition, Cursor's CEO put OpenAI models at about 5% of user traffic, and Anthropic publicly committed to keep serving Claude models in Cursor.

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
Teams Standard and Premium are $40/user/month, Enterprise is custom, and on-demand usage bills in arrears on the paid tiers, as of 2026-09-03.

## Compared to

- [VS Code + Copilot](../vscode-copilot/index.md): the default-path rival; pick VS Code for openness and price, Cursor for the integrated experience.
- [Zed](../zed/index.md): faster and cheaper with no platform ambitions; pick Zed when the editor is the product you want.
- [Windsurf](../windsurf/index.md): the cautionary tale of this market's volatility; read it before betting a team on any single AI editor.

## Bottom line

**Recommended for teams that want the strongest turnkey agentic editor and accept vendor concentration as the price.**
Not for anyone who needs an open, auditable toolchain or a predictable bill.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [ai-tools-i-have-used](../../ai-tools-i-have-used/index.md) - how fast editor allegiances rotate in practice
- [The Shifting Bottleneck](../../the-shifting-bottleneck/index.md) - why editor AI quality stopped being the constraint
- [Rolling Out the Unread Review](../../rolling-out-the-unread-review/index.md) - what Bugbot-style review has to survive organizationally

## References

- https://cursor.com/pricing - tiers, limits language, privacy mode, as of 2026-09-03
- https://cursor.com/blog/joining-spacex - the August 14, 2026 acquisition completion post
- https://devops.com/openai-cuts-off-cursors-model-access-after-spacex-acquisition/ - the OpenAI wind-down, the November 12, 2026 shutoff, and the 5% traffic claim, September 2026
- https://cursor.com/docs - product surfaces and configuration
- https://news.ycombinator.com/item?id=48553224 - the June 2026 acquisition announcement thread
- https://news.ycombinator.com/item?id=43683012 - the April 2025 support-hallucination incident thread
