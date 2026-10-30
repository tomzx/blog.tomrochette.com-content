---
title: Amp
created: 2026-08-22
updated: 2026-10-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, coding-agents, harnesses, remote-execution, developer-tools]
readability: 3
audience_notes: >
  Engineers delegating long-running tasks to agents that keep working after the laptop closes.
  Assumes you have run a terminal agent and understand metered usage billing.

---

Amp is the coding agent from Amp Frontier Corporation ([spun out of Sourcegraph on December 2, 2025](https://ampcode.com/news/amp-frontier-corporation)): a CLI plus web and phone surfaces, with threads that run on remote machines called orbs.

**Amp's orbs are the most direct answer in the field to "the agent should keep working when I close my laptop", and the product is priced exactly like something that believes its own value.**

## What it is

The `amp` CLI runs the agent loop locally; threads can be handed to **orbs, remote machines that keep executing after you disconnect**, and picked up from any device.
Four modes (low, medium, high, ultra) trade speed against reasoning, with the oracle as a second-opinion model, the librarian for cross-repository GitHub search, subagents, schedules the agent sets itself, and a plugin system that can gate tool calls.
AGENTS.md is the guidance convention, and a linked ChatGPT subscription can supply GPT-5.6 usage.

## Status

**Active and independent.**
Amp was built inside Sourcegraph, was made free in October 2025, launched subscriptions, and spun out as a profitable separate company in December 2025 with a twenty-person founding team.
Shipping cadence in August and September 2026 is weekly (voice control via Puck and an iOS and macOS app in late August, a desktop orb client and Fable 5.1 powering ultra in early September, a customizable Dial and sooner steering on September 8-10, runners that serve many directories on September 17, runner-created worktrees and workspace-shared runners on September 22-24, and the Mac app acting as a runner on September 24, as of 2026-09-26).
On September 13, 2026 the [Free Agent announcement](https://ampcode.com/news/free-agent) made Amp free to use with your own compute, subscriptions, or keys, removed BYOK token fees for everyone outside Enterprise, and opened early access to nine more BYOK providers (OpenRouter, Bedrock, Google Cloud Agent Platform, Azure Foundry, Vercel AI Gateway, Cloudflare AI Gateway, Ollama Cloud, OpenCode Go, custom endpoints).
The cadence ran through September's end and into October: Opus 5.5 took over the medium setting on September 28, Plaid Speed claimed 6x faster inference for GPT-6 Astra on September 29, multiple separate Puck conversations arrived on October 6, and on October 10 the [Use Your Claude Plan announcement](https://ampcode.com/news/use-your-claude-plan) made Claude Pro and Max plans usable in Amp for everyone at no extra cost, a mode that runs the Claude Agent SDK under the hood rather than Amp's own agent ([news index](https://ampcode.com/news)), the newest items as of 2026-10-10, with the pricing page re-verified unchanged on 2026-10-11.
October's train has kept running since: Amp now follows up on your GitHub pull requests and orders files intelligently for faster reviews (both October 12), Puck works in other agents via MCP (October 13), a runner's macOS desktop is visible and usable from your session (October 16), issues can be mentioned or assigned to Amp in Linear and it works them in a thread (October 19), and the featured October 22 [Self-Hosted Orbs announcement](https://ampcode.com/news/self-hosted-orbs) opened running orbs on your own infrastructure through an `amp orb provider` dispatch program (free for individuals and teams, with Enterprise billing at standard orb pricing starting October 29), and the train ran on through late October: an Android app carrying threads, orbs, and Puck (October 27), personal self-hosted orb providers that any individual can attach without a workspace admin (October 28), charts, timelines, and mockups rendered in the thread (Visualize This, October 29), and [macOS Satellites](https://ampcode.com/news/macos-satellites) that attach a cloud Mac to a Linux orb for Xcode builds and simulator runs (October 29, beta with a waitlist), the newest items as of 2026-10-30, with the tier page re-verified unchanged on 2026-10-30 (the Individual and Teams tiers advertise using your own domains for portals).

## Strengths

- **Remote execution is the product, not a bolt-on**: orbs, runners, phone control, and thread sharing compose into actual delegated work.
- The oracle and librarian are direct answers to "the model should check itself and read other repos".
- Willingness to delete features keeps the surface small; the manual reads like a tool its builders use.
- BYOK works on usage billing, including Anthropic keys (with the data-retention caveat their [manual](https://ampcode.com/manual/) documents for Fable-class models).

## Cautions

- Closed source; you are trusting a startup's harness with your repository and its metering.
- Expensive by [community report](https://news.ycombinator.com/item?id=46124649): **usage-billed teams describe spending over $1,000/month per person**, and pay-as-you-go users describe watching budgets evaporate before they can judge the tool.
- A free Hobby tier returned in September 2026, reversing the paid-only stretch that followed the October 2025 free period; it has no included orb time, only pay-as-you-go orbs or your own runners.
- Tool calls do not ask approval by default; the permission model is opt-in via plugins, which is a real decision to make consciously.

## Pricing

Hobby: free tier with all product features, pay-as-you-go orb time or your own runners, and no Amp token fees on BYOK or linked subscriptions.
Individual $20/month: 45,000 orb minutes (750 hours) of Megawatt orb time, with a Gigawatt step-up behind the same toggle; a linked ChatGPT subscription still powers the low, medium, and high Dial settings instead of Amp credits.
Teams cost nothing extra beyond members' tiers and pool credits with SAML/OIDC SSO; Enterprise is custom, pooled credits only.
Since the September 13, 2026 Free Agent change there is no monthly fee to use Amp at all on your own compute, runners, subscriptions, or keys (you can still buy inference through Amp with no markup), and the zero and minimal data retention policy is now contractually extended to every tier.
All tiers re-verified unchanged on 2026-10-30.
The one new metered product is macOS Satellites (October 29 beta): satellite time bills at mac.medium $2/hour or mac.large $4/hour, drawn from included orb time first and then Amp credits.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-08-22 | Individual | Baseline at note creation: Hobby free, Individual $20/mo for 45,000 Megawatt orb minutes, Teams and Enterprise pooling. | [ampcode.com/pricing](https://ampcode.com/pricing/) |
| 2026-09-13 | All tiers | Free Agent change: no monthly fee to use Amp on your own compute, runners, subscriptions, or keys; Amp-sold inference stays at no markup, zero and minimal retention extended to every tier. | [ampcode.com/pricing](https://ampcode.com/pricing/) |
| 2026-10-22 | Self-hosted orbs | Introduced free for individuals and teams; Enterprise workspaces move to standard orb pricing starting October 29, 2026, free for every workspace until then. | [Self-Hosted Orbs announcement](https://ampcode.com/news/self-hosted-orbs) |
| 2026-10-29 | macOS Satellites | Introduced in beta at mac.medium $2/hour (6 CPU, 14 GB) and mac.large $4/hour (12 CPU, 28 GB), drawn from included orb time first, then Amp credits. | [macOS Satellites announcement](https://ampcode.com/news/macos-satellites) |

## Compared to

- [Claude Code](../claude-code/index.md) and [Codex](../codex/index.md): subscription platforms whose cloud forms are bounded by session caps; **Amp's orbs are the more aggressive delegation model**.
- [OpenCode](../opencode/index.md): the local, open, cheap end of the same decision.

## Bottom line

**Recommended for engineers whose bottleneck is supervision of long-running parallel work and whose budget is real.**
If orbs fit your loop, I think the premium buys itself back in supervision time.
Not for open-source-only teams or anyone metering their own tokens.

## Changes

- 2026-08-22 - Created in the Harnesses category seed, recording the December 2025 Sourcegraph spinout and subscription tiers.
- 2026-08-22 - Removed type: post per a section-wide owner rules change.
- 2026-08-24 - Recorded the widened linked-subscription set (X Premium+/SuperGrok and SpaceX AI alongside ChatGPT).
- 2026-08-26 - Added a first-person line in Bottom line per writing rules.
- 2026-08-27 - Canonicalized the spinout link and reference to ampcode.com/news/amp-frontier-corporation.
- 2026-09-02 - Updated linked subscriptions after the pricing page dropped SpaceX AI.
- 2026-09-08 - Folded in September news (desktop orb client, Fable 5.1 powering ultra, iOS and macOS app).
- 2026-09-12 - Recorded the pricing restructure (new free Hobby tier, Individual $20 with 45,000 orb minutes, seat-free Teams).
- 2026-09-13 - Recorded the Free Agent announcement: free with your own compute or subscriptions, BYOK token fees dropped outside Enterprise, and nine more BYOK providers in early access.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-26 - Folded in late September shipping news: runner-created worktrees, workspace-shared runners, and the Mac app acting as a runner; pricing re-verified unchanged.
- 2026-10-02 - Recorded the September 28-29 news (Opus 5.5 powering medium, Plaid Speed 6x inference for GPT-6 Astra) and re-verified the pricing page unchanged.
- 2026-10-08 - Recorded the October 6 Many, Many Pucks news (multiple separate Puck conversations), re-verified the pricing page unchanged, and moved the newest-item as-of date.
- 2026-10-10 - Recorded the October 10 Use Your Claude Plan announcement, which made Claude Pro and Max plans usable in Amp for everyone at no extra cost through a mode running the Claude Agent SDK under the hood.
- 2026-10-17 - Recorded the October 12-16 news: GitHub pull-request follow-ups, Jev-powered intelligent file ordering, Puck in other agents via MCP, and runner desktop viewing, and moved the newest-item as-of date.
- 2026-10-25 - Rotation re-verification, every cited reference live; recorded the October 19 Linear issue assignment and the October 22 Self-Hosted Orbs announcement (free for individuals and teams, Enterprise orb pricing from October 29) with its Price history row, re-verified the tier page unchanged, and noted the custom portal domains now advertised on Individual and Teams.
- 2026-10-30 - Rotation re-verification, every cited reference live except the Use Your Claude Plan announcement, whose URL now serves the pricing page: recorded the October 27-29 news (Amp on Android, personal self-hosted orb providers, thread visualization, and macOS Satellites in beta) with the satellites' Price history row, and re-verified the tier page unchanged.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - Amp as the remote-execution bet in the harness layer
- [Managing Many Concurrent LLM Agent Sessions](../../../managing-many-llm-agent-sessions/index.md) - the supervision pattern orbs exist for
- [Scaling the LLM Agent Company](../../../scaling-the-llm-agent-company/index.md) - where delegated agents point at company scale
- [The Codebase Gardener](../../../the-codebase-gardener/index.md) - the human role left when agents run this far

## References

- https://ampcode.com/ - product overview, orbs, news cadence as of 2026-10-30
- https://ampcode.com/pricing/ - Hobby, Megawatt, Gigawatt, teams, enterprise, linked subscriptions, as of 2026-10-30 (re-verified unchanged)
- https://ampcode.com/news/macos-satellites - the October 29, 2026 announcement attaching cloud Macs to orbs, with the mac.medium and mac.large rates
- https://ampcode.com/news/self-hosted-orbs - the October 22, 2026 announcement opening orb self-hosting
- https://ampcode.com/news/free-agent - the September 13, 2026 free-with-your-own-compute and expanded-BYOK announcement
- https://ampcode.com/news/use-your-claude-plan - the October 10, 2026 Claude Plan mode announcement and its Claude Agent SDK note (the URL now serves the pricing page, verified 2026-10-30)
- https://ampcode.com/news/amp-frontier-corporation - the December 2, 2025 spinout announcement
- https://ampcode.com/manual/ - modes, oracle, librarian, skills, plugins, permissions
- https://news.ycombinator.com/item?id=46124649 - spinout discussion with praise and cost complaints
