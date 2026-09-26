---
title: Google AI plans
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, google, subscriptions, gemini]
readability: 3
audience_notes: >
  Engineers deciding which Google AI subscription pays for Antigravity, AI Studio, and the Gemini app.
  Assumes you know what a weekly rate limit and a credit top-up do to an agent loop.
---

Google AI plans are Google's consumer subscription ladder, Google AI Plus, Google AI Pro, and Google AI Ultra in 5x and 20x versions, and from Plus upward they are how individuals raise the limits on Antigravity, AI Studio, Jules, and the Gemini app.

**The plans sell multipliers on unpublished quotas plus a credit pool billed at API consumption rates, and Google's own free Antigravity tier is good enough that most engineers hitting a wall should check whether they need to pay at all.**

## What it is

Three consumer tiers sold through Google One: Plus (2x Gemini access versus non-subscribers, 400 GB storage), Pro (4x, 5 TB, $10 in monthly Google Cloud credits), and Ultra in 5x (5x Pro, 20 TB, $40 credits) and 20x (20x Pro, 30 TB, $100 credits) versions, as of 2026-09-26.
The plans carry the Gemini app, Google Flow, Gemini Notebook, AI Studio, Android Studio, Chrome auto browse, and expanded Antigravity and Jules limits, with Flow credits of 200 to 25,000 per month across the ladder.
Personal Google Accounts only: Workspace customers are pushed to Gemini add-ons, and organizations to Google Cloud terms with consumption-based API pricing.
The FAQ confirms the ladder's churn: the old Google AI Premium plan was renamed Google AI Plus.

## Status

Active and restructured repeatedly, with the tiers, multipliers, and storage allotments verified from Google's own pages on 2026-09-26.
Plus is available in over 160 countries, Pro and Ultra in over 150.
The 2026 record shows a rename (AI Premium to Plus) and an Ultra split into 5x and 20x columns, both visible on the current comparison table.
**Prices are the weak point of the product surface: the marketing pages render the dollar figure client-side per region, so my US and Canada fetches returned the ladder with the price stripped, and third-party guides are the only place the US numbers appear in text.**

## Strengths

- The free Antigravity tier it upgrades is real: unlimited tab completions and command requests, a weekly baseline quota, and access to Gemini, Claude, and open-weight models.
- The flexible AI credit pool converts a hard wall into metered overage at documented consumption pricing, with a Never/Always overage setting instead of a surprise bill.
- Ultra refreshes its quota every five hours against the free tier's weekly clock, the difference that matters for daily-driver agent work.
- The bundled Google Cloud credits ($10, $40, $100 monthly by tier) partially self-fund Ultra for anyone who also calls the Gemini API.

## Cautions

- Google publishes no quota numbers for any tier, and the Antigravity docs say limits are "correlated with the amount of work done by the agent", so one gnarly prompt can cost a day of quota.
- The AI credits purchase page sits behind Google sign-in, so credit prices are the least documented numbers in the whole stack.
- Google's own pages disagree on Plus storage, 400 GB on the AI plans page versus 2 TB on the Canadian plans page, both fetched 2026-09-26.
- The consumption rates your credits burn at double on January 1, 2027, when the current Gemini API promotional prices expire.
- Tier mechanics have already been changed out from under users once: the May 2026 "Antigravity bait and switch" thread drew 771 points.
- No bring-your-own-key and no organizational contract tiers on the consumer path.

## Pricing

Canadian storefront, fetched 2026-09-26: Google AI Plus CA$13.99/month, Google AI Pro CA$26.99/month, Ultra not listed on that page.
US dollar list prices did not render in my fetched HTML; a third-party comparison table lists Plus around $8/month as the cheapest paid path and Ultra 20x at $200/month as the top individual tier (blocked fetch, see references).
Organizations: Google Cloud terms with consumption-based API pricing, included in select Gemini Enterprise subscriptions.
Credits bill at standard Gemini Enterprise consumption rates, anchored by the Gemini API price list: Gemini 3.8 Flash at $0.75/$3.75 per million tokens through December 31, 2026, doubling in 2027, and Gemini 3.1 Pro at $2.00/$12.00.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-08-24 | Individuals / Pro / Ultra | Baseline: Antigravity free at $0 with basic weekly rate limits, Google AI Pro and Ultra the paid paths that raise limits and add the AI credit pool | https://antigravity.google/pricing |
| 2026-09-26 | Ladder | Verified: Plus / Pro / Ultra (5x, 20x) ladder at 2x/4x/5x-Pro/20x-Pro access, AI Premium confirmed renamed to Google AI Plus, CA$13.99 Plus and CA$26.99 Pro on the Canadian storefront | https://one.google.com/about/google-ai-plans |

## Compared to

- [Claude plans](../claude-plans/index.md): the same multiplier-on-a-secret-quota pattern, but Google bundles harder (Flow credits, cloud credits, YouTube) and prices its entry tier lower.
- [ChatGPT plans](../chatgpt-plans/index.md): the rival ladder, which publishes per-model message ranges where Google publishes adjectives.
- [Google Antigravity](../../surfaces/antigravity/index.md): the surface these plans meter; its free tier undercuts the paid ladder for light use, which is the sharpest critique of the ladder itself.
- [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md): the API-side alternative, still the right answer for automation and CI, and the baseline your credit pool burns at.

## Bottom line

Recommended for engineers who have actually hit the free Antigravity weekly wall and want metered overage at known API rates; start at Pro, and only after two real capped weeks.
Not for light users, who should stay on the free tier, and not for automation-heavy workloads, which belong on the API.
My disagreeable claim: Ultra is priced for video generation more than for coding, because the 25,000 monthly Flow credits are its most concrete differentiator, so engineers buying Ultra 20x for Antigravity are mostly buying Flow.

## Changes

- 2026-09-26 - Created when the owner asked for any remaining subscription providers.

## See also

- [Claude plans](../claude-plans/index.md) - the multiplier-based subscription this ladder most resembles, with a longer 2026 change log.
- [ChatGPT plans](../chatgpt-plans/index.md) - the OpenAI ladder at the same price points, with more published mechanics.
- [Google Antigravity](../../surfaces/antigravity/index.md) - the free-first editor and agent platform whose limits these plans raise.
- [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md) - where the subscription ends and per-token consumption pricing begins.

## References

- https://one.google.com/about/google-ai-plans - the plan ladder, comparison table (multipliers, Flow credit quotas, Antigravity and Jules rows), AI Premium rename, country counts (fetched 200, 2026-09-26)
- https://one.google.com/intl/en_us/about/google-ai-plans/ - US variant: $10/$40/$100 monthly Google Cloud credits by tier, Home Premium bundle values, Ultra 5x and 20x storage tiers (fetched 200, 2026-09-26)
- https://one.google.com/about/plans - Canadian storefront prices, CA$13.99 Plus and CA$26.99 Pro, no Ultra listed (fetched 200, 2026-09-26)
- https://antigravity.google/pricing - the $0 individual tier, Pro/Ultra as the paid paths adding rate limits and the AI credit pool, Google Cloud consumption terms for organizations (fetched 200, 2026-09-26)
- https://antigravity.google/docs/plans - quota mechanics: five-hour Ultra refresh, weekly free quota, credits billed at standard Gemini Enterprise consumption pricing, Never/Always overages, no BYOK (fetched 200, 2026-09-26)
- https://ai.google.dev/gemini-api/docs/pricing - the consumption-rate anchor: 3.8 Flash $0.75/$3.75 per million tokens until 2026-12-31 then doubled, 3.1 Pro $2.00/$12.00 (fetched 200, 2026-09-26)
- https://news.ycombinator.com/item?id=48222529 - critical source: the May 2026 "Antigravity bait and switch" thread, 771 points, on tiers changing under existing users (fetched 200, 2026-09-26)
- https://codeagentswarm.com/en/guides/grok-build-pricing - third-party table naming Plus around $8/month and Ultra 20x at $200/month; fetched 429 this run, figures carried from the 2026-08-25 verification, hold loosely
