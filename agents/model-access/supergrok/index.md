---
title: SuperGrok
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, grok, subscriptions, xai]
readability: 3
audience_notes: >
  Engineers deciding whether an xAI consumer subscription is the right way to pay for Grok in chat and in the Grok Build coding agent.
  Assumes you know what a rate limit and a per-token API bill look like.
---

SuperGrok is xAI's (SpaceXAI LLC's) consumer subscription ladder for Grok, running from a free tier to $300 per month, which now doubles as the way engineers pay for the Grok Build coding agent.

**One subscription, one weekly pool: your Grok chat, your Grok Build runs, and your API calls all drain the same weekly bucket, so the plan you buy for coding is also the plan you spend by chatting.**

## What it is

A five-step consumer ladder sold by xAI for its Grok products on web, iOS, and Android: Free, SuperGrok Lite, SuperGrok, SuperGrok Plus, and SuperGrok Heavy, with Business and Enterprise seats above.
The tiers meter chat, Imagine image and video generation, Voice, Grok Bot, and Grok Build, xAI's open-source terminal coding agent, which carries its own row on the official plan comparison for every tier from Free to Enterprise, and the API pricing page separately refers to "Grok Build's free tier".
Above the ladder sits the pay-per-token API, billed separately from any subscription.
The official pricing page lists dollar figures only for Free, SuperGrok, and Plus; Lite and Heavy show as plan columns without public prices on the web card, so their numbers come from press coverage and third-party guides.

## Status

Active and still being restructured: Lite was announced on 2026-03-25 at $10 per month while in testing with selected users, and SuperGrok Plus is absent from a complete tier guide dated 2026-07-06 yet present on the official page on 2026-09-26.
The defining mechanic is recent and explicit: integration documentation states that every paid Grok subscription gets one weekly usage pool shared across Grok chat, Grok Build, and API access, and that paid usage pauses when the pool empties until the reset time shown in the Usage tab.
Third-party harnesses can spend the same pool: Warp connects over OAuth and routes Grok models through your xAI account, with its requests labeled API in xAI's usage dashboard.
**The ladder is converging on one fuzzy weekly pool instead of countable messages, while the tier list itself is still moving underneath it.**

## Strengths

- The weekly pool is flexible rather than siloed, so a coding-heavy week can spend the budget on Grok Build and a research-heavy week on DeepSearch and chat.
- Grok Build is included from Free upward, which makes the $0 tier a working entry point to a frontier coding agent, with paid tiers raising its limits from the same pool.
- The API escape hatch is cheap for a frontier lab: grok-4.6 and grok-4.7 bill $2.00 input and $6.00 output per million tokens under 200k prompt, with cached input at $0.50, as of 2026-09-26.
- The subscription travels outside xAI's own apps, since Warp and similar tools authenticate against it directly.
- Lite at $10 per month would be the cheapest paid on-ramp of any frontier-lab subscription in this category, once it ships generally.

## Cautions

- No quota is published anywhere: no messages, no tokens, no pool size, so the only way to size a plan is to burn a month and read the Usage tab.
- The shared pool cuts both ways: an afternoon of video generation or idle chat quietly deletes tomorrow's coding budget.
- Lite is not confirmed as generally available, announced as a test with selected users in March 2026, and Heavy's $300 figure rests on third-party guides because the official web card does not expose it.
- Coding is the ladder's weakest argument: the critical guide I fetched concludes Claude and ChatGPT lead on coding help and recommends SuperGrok for live X data and image work, not for code.
- Imagine, the media product the higher tiers are priced around, is the surface under active lawsuits, a US congressional inquiry, and EU, UK, and Canada probes, per the same critical guide.
- A subscription connected through a third-party harness carries no zero-data-retention guarantee from that harness, since retention on xAI's side is governed by your own xAI account.

## Pricing

Free: $0, limited usage, Grok Build included with limits.
SuperGrok Lite: $10/month, announced 2026-03-25, basic creation tools, 480p video up to 6 seconds, 2x longer chats than Free, one AI agent, in testing at announcement.
SuperGrok: $30/month, Grok 4.6, higher rate limits across all features, image and video generation.
SuperGrok Plus: $100/month, everything in SuperGrok plus 1080p video, significantly higher usage across Chat, Imagine, Voice, and Build, priority access at peak times.
SuperGrok Heavy: $300/month per third-party guides as of 2026-07-06, the multi-agent Grok 4 Heavy tier.
API escape hatch, billed separately: grok-4.6 and grok-4.7 at $2.00/$6.00 per 1M tokens under 200k prompt ($4.00/$12.00 above), $0.50 cached input; grok-build-0.1 at $1.00/$2.00; Grok 4.7 Fast at 2x rates, exclusive to Cursor and Grok Build and excluded from Grok Build's free tier.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-01-24 | SuperGrok / Heavy | Baseline: SuperGrok $30/month and Heavy $300/month, no Lite or Plus tier; the July 2026 update describes these two anchor prices as unchanged | https://aitoolanalysis.com/supergrok-subscription-price-2026/ |
| 2026-03-25 | SuperGrok Lite | Announced at $10/month by Musk on X, in testing with selected users, global rollout promised later in the year | https://www.businesstoday.in/technology/story/xai-makes-grok-affordable-with-new-supergrok-lite-plan-check-price-and-what-it-offers-522462-2026-03-26 |
| 2026-09-26 | SuperGrok Plus | Observed at $100/month on the official pricing page, absent from the 2026-07-06 complete tier guide, so added in the July to September window | https://x.ai/pricing |

## Compared to

- [Claude plans](../claude-plans/index.md): the $20 to $200 Anthropic ladder that runs Claude Code; it matches SuperGrok at the $100 rung and carries the stronger coding reputation, while publishing no more about its quotas than xAI does.
- [ChatGPT plans](../chatgpt-plans/index.md): the rival consumer ladder at $20 to $200, which publishes per-model message ranges, a discipline xAI has not adopted.
- The [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md): the per-token path, and the reason the shared pool matters less if your coding runs on the API anyway.

## Bottom line

Recommended for engineers already inside the Grok and X ecosystem who want one bill across chat and Grok Build and can tolerate an unpublished weekly pool.
Not for coding-first engineers choosing a primary agent subscription, where Claude plans or the GLM Coding Plan buy more verified coding throughput per dollar.
My disagreeable claim: SuperGrok Plus at $100 is a media-creator tier wearing an engineer's price tag, because on a shared pool the extra $70 mostly buys 1080p video and peak-hour priority, not more code.

## Changes

- 2026-09-26 - Created when the owner asked for any remaining subscription providers.

## See also

- [Claude plans](../claude-plans/index.md) - the incumbent subscription this ladder prices against, rung for rung.
- [ChatGPT plans](../chatgpt-plans/index.md) - the other big-lab consumer ladder, facing the same unpublished-quota problem.
- [Grok Build](../../harnesses/grok-build/index.md) - the harness these subscriptions meter, including the wire-level privacy analysis of its default path.
- [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md) - xAI's API-side row, where the $2/$6 escape hatch lives.

## References

- https://x.ai/pricing - official plan cards (Free $0, SuperGrok $30, Plus $100) and the plan comparison carrying Lite, Heavy, and Grok Build rows (fetched 200, 2026-09-26)
- https://docs.warp.dev/agents/inference/grok-subscription - the one weekly pool shared across Grok chat, Grok Build, and API access, pause-on-empty behavior, third-party-harness ZDR caveat (fetched 200, page updated 2026-09-24)
- https://docs.x.ai/developers/pricing - API escape hatch: grok-4.6/4.7 at $2/$6 under 200k prompt, $0.50 cached, $4/$12 above, grok-build-0.1 at $1/$2, Grok 4.7 Fast exclusivity (fetched 200, 2026-09-26)
- https://www.businesstoday.in/technology/story/xai-makes-grok-affordable-with-new-supergrok-lite-plan-check-price-and-what-it-offers-522462-2026-03-26 - Lite announcement: $10/month, testing phase with selected users, 480p 6-second video, 2x chats, one agent (fetched 200, 2026-09-26)
- https://aitoolanalysis.com/supergrok-subscription-price-2026/ - critical guide: full tier table including Heavy $300, the coding-benchmarks caveat, and the safety litigation section (fetched 200, updated 2026-07-06)
- https://codeagentswarm.com/en/guides/grok-build-pricing - independent Grok Build plan-table guide, attempted four times this run and rate-limited (429) on every attempt, so nothing here is cited from it
