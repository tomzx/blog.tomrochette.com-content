---
title: SuperGrok
created: 2026-09-26
updated: 2026-10-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, grok, subscriptions, xai]
readability: 3
audience_notes: >
  Engineers deciding whether an xAI consumer subscription is the right way to pay for Grok in chat and in the Grok Build coding agent.
  Assumes you know what a rate limit and a per-token API bill look like.
---

The consumer subscription this note tracks under the SuperGrok name is the ladder for Grok sold by X Subscription Corp under the SpaceX Super Intelligence LLC (SpaceXSI) brand, which doubled as the way engineers pay for the Grok Build coding agent until a mid-October 2026 restructure replaced the SuperGrok tiers with a Plus/Premium/Super/Ultra lineup that bundles X Premium features and Cursor.

**One subscription, one weekly pool, with the API just moved outside it: your Grok chat, Imagine, Voice, Bot, and Cursor runs share the bucket while API calls bill separately at standard rates, so the plan you buy for coding is also the plan you spend by chatting, but the API escape hatch no longer drains it.**

## What it is

A five-step consumer ladder sold through X Subscription Corp: Free, Plus $8, Premium $30, Super $100, and Ultra $200 per month, with Teams from $30 per user and Enterprise custom. Until the October 2026 restructure the ladder was Free, SuperGrok Lite ($10, announced in testing), SuperGrok ($30), SuperGrok Plus ($100), and SuperGrok Heavy ($300), and the SuperGrok plan names have since left the pricing page.
The tiers meter the Grok products (chat, Imagine image and video generation, Voice, and Grok Bot; Grok Build is included per tier with limits from the same pool) and bundle X Premium features (checkmark, reduced ads, creator tools) and Cursor (agent, cloud agents, code hosting via Origin, Bugbot reviews), with third-party Cursor models billed at API list prices outside the pool.
Above the ladder sits the pay-per-token API: paid plans include Grok API access, but per the pricing FAQ as of 2026-10-29 API usage is billed separately at standard model rates and does not draw from the plan's usage pool, and every tier's dollar figure is published on the page.

## Status

Active and still being restructured: Lite was announced on 2026-03-25 at $10 per month while in testing with selected users, SuperGrok Plus surfaced between a July 2026 tier guide and the 2026-09-26 page check, and by the 2026-10-14 fetch the whole ladder had been rebuilt into Plus/Premium/Super/Ultra with the SuperGrok names gone.
The defining mechanic moved again by 2026-10-29: the pricing page's FAQ now states the shared pool covers Chat, Imagine, Voice, and Bot within Grok, and answers the API question the other way from before, API usage is billed separately at standard model rates and does not draw from the plan's usage pool.
That puts the official page at odds with Warp's subscription doc (last updated 2026-10-20), which still states that Grok chat, Grok Build, and API access all draw down the same weekly pool and that requests from Warp appear under the API label against that pool, so the third-party-harness story now rests on the older wording.
**The ladder is converging on one fuzzy weekly pool instead of countable messages, and the pool's own boundaries are still moving underneath it.**

## Strengths

- The weekly pool is flexible rather than siloed, so a coding-heavy week can spend the budget on Grok Build and a research-heavy week on DeepSearch and chat.
- Grok Build is included from Free upward, which makes the $0 tier a working entry point to a frontier coding agent, with paid tiers raising its limits from the same pool.
- The API escape hatch is cheap for a frontier lab: grok-4.6 and grok-4.7 bill $2.00 input and $6.00 output per million tokens under 200k prompt, with cached input at $0.50, as of 2026-10-29 (re-verified unchanged), and per the current FAQ it no longer drains the subscription pool.
- The subscription travels outside xAI's own apps per Warp's documentation, though the pool treatment of those requests is now stated differently by Warp (API in the pool, October 20) and by xAI's own FAQ (API billed separately, October 29).
- Plus at $8 per month now matches ChatGPT Go as the cheapest paid on-ramp in this category, and every tier's dollar figure is on the official card.

## Cautions

- No quota is published anywhere: no messages, no tokens, no pool size, so the only way to size a plan is to burn a month and read the usage indicator.
- The shared pool cuts both ways: an afternoon of video generation or idle chat quietly deletes tomorrow's coding budget.
- The ladder has been rebuilt twice in 2026 (Lite announced in March, the full rebrand by mid-October), so a tier bought this month may not carry its name at renewal even though every price is now published.
- Coding is the ladder's weakest argument: the critical guide I fetched concludes Claude and ChatGPT lead on coding help and recommends SuperGrok for live X data and image work, not for code.
- Imagine, the media product the higher tiers are priced around, is the surface under active lawsuits, a US congressional inquiry, and EU, UK, and Canada probes, per the same critical guide.
- A subscription connected through a third-party harness carries no zero-data-retention guarantee from that harness, since retention on xAI's side is governed by your own xAI account.

## Pricing

Free: $0, limited usage, Grok Build included with limits.
Plus: $8/month, the shared AI usage pool across Grok and Cursor, the Premium checkmark, and reduced timeline ads on X.
Premium: $30/month, 4x the Plus pool, the latest Grok models, faster chat responses, image and video generation, and through Cursor the agent, cloud agents and automations, code hosting via Origin, and Bugbot AI code reviews.
Super: $100/month, 15x the Plus pool and priority model access at peak times.
Ultra: $200/month, 50x the Plus pool and earliest access to products and models.
Teams from $30 per user per month and Enterprise custom (all re-verified unchanged 2026-10-29; the former SuperGrok Lite $10, SuperGrok $30, Plus $100, and Heavy $300 ladder is gone, and existing SuperGrok subscribers keep their old plans per the October 2026 restructuring).
API escape hatch, included on paid plans but billed separately at standard model rates without drawing from the pool (per the pricing FAQ, 2026-10-29): grok-4.6 and grok-4.7 at $2.00/$6.00 per 1M tokens under 200k prompt ($4.00/$12.00 above), $0.50 cached input; grok-build-0.1 at $1.00/$2.00 ($2.00/$4.00 above 200k); Grok 4.7 Fast at 2x rates (1.5x long-context), exclusive to Cursor and Grok Build and excluded from Grok Build's free tier; a US regional endpoint bills 1.1x (all re-verified on the API pricing page as of 2026-10-29).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-01-24 | SuperGrok / Heavy | Baseline: SuperGrok $30/month and Heavy $300/month, no Lite or Plus tier; the July 2026 update describes these two anchor prices as unchanged | https://aitoolanalysis.com/supergrok-subscription-price-2026/ |
| 2026-03-25 | SuperGrok Lite | Announced at $10/month by Musk on X, in testing with selected users, global rollout promised later in the year | https://www.businesstoday.in/technology/story/xai-makes-grok-affordable-with-new-supergrok-lite-plan-check-price-and-what-it-offers-522462-2026-03-26 |
| 2026-09-26 | SuperGrok Plus | Observed at $100/month on the official pricing page, absent from the 2026-07-06 complete tier guide, so added in the July to September window | https://x.ai/pricing |
| 2026-10-14 | Ladder | Restructure: the SuperGrok ladder (Free, Lite $10 in testing, SuperGrok $30, Plus $100, Heavy $300) replaced by Free, Plus $8, Premium $30, Super $100, and Ultra $200 monthly, with Teams from $30 per user; X Premium features and Cursor now bundle into every tier, the SuperGrok plan names left the cards, and the shared weekly pool mechanic carried over | https://x.ai/pricing |
| 2026-10-29 (observed) | Pool terms | The pricing FAQ removed API usage from the shared weekly pool: the pool now covers Chat, Imagine, Voice, and Bot within Grok, while paid plans include Grok API access billed separately at standard model rates that does not draw from the pool; Warp's subscription doc (updated 2026-10-20) still describes API access as drawing the same pool | https://x.ai/pricing |

## Compared to

- [Claude plans](../claude-plans/index.md): the $20 to $200 Anthropic ladder that runs Claude Code; it matches the Super tier at the $100 rung and carries the stronger coding reputation, while publishing no more about its quotas than xAI does.
- [ChatGPT plans](../chatgpt-plans/index.md): the rival consumer ladder at $20 to $200, which publishes per-model message ranges, a discipline xAI has not adopted.
- The [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md): the per-token path, and the reason the shared pool matters less if your coding runs on the API anyway.

## Bottom line

Recommended for engineers already inside the Grok and X ecosystem who want one bill across chat and Grok Build and can tolerate an unpublished weekly pool.
Not for coding-first engineers choosing a primary agent subscription, where Claude plans or the GLM Coding Plan buy more verified coding throughput per dollar.
My disagreeable claim: Super at $100 is still a media-creator tier wearing an engineer's price tag, because on a shared pool the extra $70 over Premium mostly buys priority model access at peak times, not more code.

## Changes

- 2026-09-26 - Created when the owner asked for any remaining subscription providers.
- 2026-10-14 - Ladder restructure recorded: x.ai/pricing replaced the SuperGrok-named tiers (Lite $10 testing, SuperGrok $30, Plus $100, Heavy $300) with Free, Plus $8, Premium $30, Super $100, and Ultra $200 monthly plus Teams from $30 per user, bundling X Premium features and Cursor into every tier with every dollar figure now published and the shared weekly pool carried over; the Warp pool documentation claim re-based onto the page's own FAQ, the API rates re-verified unchanged, and the price history row appended.
- 2026-10-29 - Rotation re-verification with a pool-terms change and a seller rebrand: the pricing FAQ now scopes the shared weekly pool to Chat, Imagine, Voice, and Bot and states API usage is billed separately at standard rates without drawing from the pool (the opposite of the 10-14 FAQ reading), Warp's doc (updated 2026-10-20) still claims API in the pool, and the seller now brands as SpaceX Super Intelligence LLC (SpaceXSI) with the ladder prices unchanged; every cited URL re-fetched live this run, price history row appended.

## See also

- [Claude plans](../claude-plans/index.md) - the incumbent subscription this ladder prices against, rung for rung.
- [ChatGPT plans](../chatgpt-plans/index.md) - the other big-lab consumer ladder, facing the same unpublished-quota problem.
- [Grok Build](../../harnesses/grok-build/index.md) - the harness these subscriptions meter, including the wire-level privacy analysis of its default path.
- [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md) - xAI's API-side row, where the $2/$6 escape hatch lives.

## References

- https://x.ai/pricing - the plan cards after the mid-October restructure: Free $0, Plus $8, Premium $30, Super $100, Ultra $200, Teams from $30 per user, X features and Cursor bundled, the shared weekly pool FAQ, and Grok Build rows per tier (fetched 200 on 2026-09-26 reading SuperGrok $30 and Plus $100, re-verified 2026-10-06 and 2026-10-11, re-fetched 2026-10-14 reading the new ladder; re-fetched 2026-10-29 under the SpaceXSI brand with prices unchanged and the FAQ now scoping the pool to Chat, Imagine, Voice, and Bot with API billed separately outside the pool)
- https://docs.warp.dev/agents/inference/grok-subscription - the one weekly pool shared across Grok chat, Grok Build, and API access, pause-on-empty behavior, third-party-harness ZDR caveat (fetched 200, page updated 2026-09-24; re-fetched 2026-10-29, page updated 2026-10-20 and still stating chat, Build, and API access all draw the same pool, now diverging from xAI's own FAQ)
- https://docs.x.ai/developers/pricing - API escape hatch: grok-4.6/4.7 at $2/$6 under 200k prompt, $0.50 cached, $4/$12 above, grok-build-0.1 at $1/$2, Grok 4.7 Fast exclusivity, the US regional endpoint at 1.1x (fetched 200, re-verified 2026-10-06 and 2026-10-14; re-fetched 2026-10-29 under SpaceXSI branding with grok-4.5 and grok-4.3 rows added to the table and the cited rates unchanged)
- https://www.businesstoday.in/technology/story/xai-makes-grok-affordable-with-new-supergrok-lite-plan-check-price-and-what-it-offers-522462-2026-03-26 - Lite announcement: $10/month, testing phase with selected users, 480p 6-second video, 2x chats, one agent (fetched 200, 2026-09-26; re-fetched 2026-10-29, unchanged)
- https://aitoolanalysis.com/supergrok-subscription-price-2026/ - critical guide: full tier table including Heavy $300, the coding-benchmarks caveat, and the safety litigation section (fetched 200, updated 2026-07-06; re-fetched 2026-10-29, updated October 21 with the October 12 The X Subscription cutover and the keep-or-switch guidance for existing SuperGrok subscribers)
- https://codeagentswarm.com/en/guides/grok-build-pricing - independent Grok Build plan-table guide, attempted four times this run and rate-limited (429) on every attempt, so nothing here is cited from it
