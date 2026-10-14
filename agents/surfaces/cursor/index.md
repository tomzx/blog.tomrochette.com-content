---
title: Cursor
created: 2026-08-23
updated: 2026-10-13
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
As of 2026-10-13 the November 12, 2026 shutoff stands unrevised: OpenAI's own announcement still frames the date as proposed and no later reporting moves it, and the models docs still list the OpenAI models without a removal notice, GPT-5.6 Sol even carrying promotional pricing through November 21, 2026 (re-verified 2026-10-13).
By 2026-10-13 the consumer plans had been restructured into X's subscription ladder (Plus, Premium, Super, Ultra), with Cursor subscriptions sold only through X Subscription Corp, the deepest merge yet of the editor into the acquirer's stack.

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

The pricing page was restructured by 2026-10-13 into an X-fused ladder: Free $0 (limited AI usage, agent and chat), Plus $8/month (Grok models only, with the social-creator feature set), Premium $30/month (4x Plus usage, cloud agents and automations, Bugbot, third-party models at API list price), Super $100/month (15x Plus), and Ultra $200/month (50x Plus), with Teams from $30/user/month and Enterprise custom, as of 2026-10-13.
The usage pool is shared across the Cursor and Grok products and refreshes weekly rather than monthly, and third-party models bill at API list price on top of the subscription from Premium up.
Subscriptions are sold only through X Subscription Corp under the SpaceXAI bundled-subscription terms.
The docs still document the earlier request-based ladder as legacy: Pro $20/month, Pro+ $60/month, Ultra $200/month, Start (India only) at ₹649/month, and Teams Standard $40 and Premium $120 per user/month, with Max Mode marked legacy-only.
On Teams and Enterprise, third-party model usage carries a new Cursor Token Rate of $0.25 per million tokens on top of model API pricing.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | All tiers | Baseline: Hobby free with limited agent requests, Individual Pro $20/mo (Pro+ at 3x, Ultra at 20x limits), Teams Standard and Premium $40/user/mo, Enterprise custom, on-demand usage billed in arrears. | [cursor.com/pricing](https://cursor.com/pricing) |
| 2026-10-05 | Teams Premium | Corrected: Teams Premium is $120/user/mo with 5x the Standard agent limits, where the baseline row carried it at $40 alongside Standard; Standard stays $40/user/mo. A Start plan for India (₹649/mo) sits outside the listed ladder. | [cursor.com/docs/models-and-pricing](https://cursor.com/docs/models-and-pricing) |
| 2026-10-13 | Consumer ladder | The pricing page was restructured into an X-fused ladder: Free $0, Plus $8 (Grok models only), Premium $30, Super $100, Ultra $200, Teams from $30/user/month, Enterprise custom, with the usage pool shared across Cursor and Grok and refreshed weekly, and sales routed through X Subscription Corp; the docs now mark the $20 Pro / $60 Pro+ / $200 Ultra request-based ladder (Start ₹649, Teams $40/$120) as legacy. | [cursor.com/pricing](https://cursor.com/pricing) |

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
- 2026-10-10 - Re-verified the plan prices unchanged and the November 12, 2026 OpenAI shutoff unrevised (the models-and-pricing docs still list the OpenAI models without a removal notice).
- 2026-10-13 - Recorded the pricing page's restructure into the X-fused ladder (Free, Plus $8 Grok-only, Premium $30, Super $100, Ultra $200, Teams from $30/user) with the shared weekly usage pool and X Subscription Corp as the sole seller, the docs marking the $20/$60/$200 request-based ladder and the $40/$120 Teams prices as legacy, and the new $0.25/M Cursor Token Rate on Teams and Enterprise third-party usage (Price history row); the November 12 OpenAI shutoff stands unrevised with the OpenAI models still listed.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [ai-tools-i-have-used](../../../ai-tools-i-have-used/index.md) - how fast editor allegiances rotate in practice
- [The Shifting Bottleneck](../../../the-shifting-bottleneck/index.md) - why editor AI quality stopped being the constraint
- [Rolling Out the Unread Review](../../../rolling-out-the-unread-review/index.md) - what Bugbot-style review has to survive organizationally

## References

- https://cursor.com/pricing - the pricing page, restructured by 2026-10-13 into the X-fused ladder (Free, Plus $8, Premium $30, Super $100, Ultra $200, Teams from $30/user, Enterprise custom) with the weekly shared usage pool and the X Subscription Corp seller statement
- https://cursor.com/docs/models-and-pricing - the legacy plan ladder (Pro $20, Pro+ $60, Ultra $200, Start ₹649, Teams Standard $40 and Premium $120), the per-model rate card, and the Cursor Token Rate, with the OpenAI models still listed without a removal notice as of 2026-10-13
- https://cursor.com/docs/rules - the rules system and AGENTS.md support in project root and subdirectories, as of 2026-10-05
- https://cursor.com/blog/joining-spacex - the August 14, 2026 acquisition completion post
- https://devops.com/openai-cuts-off-cursors-model-access-after-spacex-acquisition/ - the OpenAI wind-down, the November 12, 2026 shutoff, and the 5% traffic claim, September 2026
- https://cursor.com/docs - product surfaces and configuration
- https://news.ycombinator.com/item?id=48553224 - the June 2026 acquisition announcement thread
- https://news.ycombinator.com/item?id=43683012 - the April 2025 support-hallucination incident thread
