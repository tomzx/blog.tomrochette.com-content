---
title: Google AI plans
created: 2026-09-26
updated: 2026-11-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, model-access, google, subscriptions, gemini]
readability: 3
audience_notes: >
  Engineers deciding which Google AI subscription pays for Antigravity, AI Studio, and the Gemini app.
  Assumes you know what a weekly rate limit and a credit top-up do to an agent loop.
---

Google AI plans are Google's consumer subscription ladder, Google AI Plus, Google AI Pro, and Google AI Ultra in 5x and 20x versions, and Pro and Ultra are how individuals raise the limits on Antigravity and AI Studio while Plus doubles access in the Gemini app, with Jules a benefit Google is winding down (its October 29, 2026 notice: sessions "until November 11, 2026", then "read-only until the end of the year", and Jules "will wind down on December 31, 2026").

**The plans sell multipliers on unpublished quotas plus a credit pool billed at API consumption rates, and Google's own free Antigravity tier is good enough that most engineers hitting a wall should check whether they need to pay at all.**

## What it is

Three consumer tiers sold through Google One: Plus (2x Gemini access versus non-subscribers, 400 GB storage), Pro (4x, 5 TB, $10 in monthly Google Cloud credits), and Ultra in 5x (5x Pro, 20 TB, $40 credits) and 20x (20x Pro, 30 TB, $100 credits) versions, as of 2026-09-26.
The plans carry the Gemini app, Google Flow, Gemini Notebook, AI Studio, Android Studio, Chrome auto browse, and expanded Antigravity limits, with Flow credits of 200 to 25,000 per month across the ladder; the table also carried expanded Jules limits through the 2026-11-15 fetch, but the 2026-11-25 and 2026-11-26 fetches hold no Jules row, and Google's October 29, 2026 notice says Jules "will wind down on December 31, 2026", read-only "until the end of the year" since November 11, 2026.
The 2026-11-26 US comparison table carries per-model access rows: in the Gemini app and in AI Studio, Carbon on Ultra only, Neon on Pro and Ultra, and Hydrogen on every tier, and under Antigravity Carbon, Neon, and Hydrogen checked on Pro and Ultra only, with no model checked on Plus, whose agent requests read Limited against Pro's Expanded.
The same table carries bundle rows the note had not recorded: Google Colab compute units of 50, 200, 1,000, and 2,000 per month from Plus to Ultra 20x, Google Flow Music credits of 3,000, 10,000, 30,000, and 30,000 per month, Google Home Premium Standard on Pro (a US$10 monthly value) and Advanced on Ultra (US$20), Google Health Premium on Pro and Ultra, and Project Genie on Ultra.
By the 2026-10-16 fetch the comparison table also rows access to Gemini 4 Argon, Google's frontier model, on every tier and an expanded token context window of one million tokens on Pro and Ultra; by the 2026-11-15 fetch the table carries separate Carbon, Argon, and Hydrogen access rows with Carbon named Google's strongest model and the Ultra headline ("Access to our Pro models" reads "includes access to Argon and Carbon" on Ultra).
Personal Google Accounts only: Workspace customers are pushed to Gemini add-ons, and organizations to Google Cloud terms with consumption-based API pricing.
The FAQ confirms the ladder's churn: the old Google AI Premium plan was renamed Google AI Plus.

## Status

Active and restructured repeatedly, with the tiers, multipliers, and storage allotments verified from Google's own pages on 2026-09-26 and re-verified unchanged on 2026-10-06, 2026-10-11, 2026-10-16, 2026-10-31, 2026-11-15, 2026-11-25, and 2026-11-26, the ladder's dollar prices still rendering client-side.
Plus is available in over 160 countries, Pro and Ultra in over 150.
The 2026 record shows a rename (AI Premium to Plus) and an Ultra split into 5x and 20x columns, both visible on the current comparison table.
**Prices are the weak point of the product surface: the marketing pages render the dollar figure client-side per region, so my US and Canada fetches returned the ladder with the price stripped, and third-party guides are the only place the US numbers appear in text.**
One exception surfaced on the 2026-11-15 US fetch: the page's savings calculator now prints Pro at $19.99/month and Ultra 5x at $99.99/month (Ultra billed monthly only) in the page text, and the 2026-11-26 fetch reads an annual Pro price of $199.99 in the same calculator.

## Strengths

- The free Antigravity tier it upgrades is substantive: unlimited tab completions and command requests, a weekly baseline quota, and access to Gemini, Claude, and open-weight models.
- The flexible AI credit pool converts a hard wall into metered overage at documented consumption pricing, with a Never/Always overage setting instead of a surprise bill.
- Ultra refreshes its quota every five hours against the free tier's weekly clock, the difference that matters for daily-driver agent work.
- The bundled Google Cloud credits ($10, $40, $100 monthly by tier) partially self-fund Ultra for anyone who also calls the Gemini API.

## Cautions

- Google publishes no quota numbers for any tier, and the Antigravity docs say limits are "correlated with the amount of work done by the agent", so one gnarly prompt can cost a day of quota.
- The AI credits purchase page sits behind Google sign-in, so credit prices are the least documented numbers in the whole stack.
- Google's own pages disagree on Plus storage: the ladder's comparison table lists it as 400 GB or 2 TB in a single cell (fetched 2026-10-16 and again 2026-10-31), beside the 400 GB card and the 2 TB figure the pages showed on 2026-09-26.
- The consumption rates your credits burn at double on January 1, 2027, when the current Gemini API promotional prices expire.
- Tier mechanics have already been changed out from under users once: the May 2026 "Antigravity bait and switch" thread drew 771 points.
- No bring-your-own-key and no organizational contract tiers on the consumer path.
- **Plus buys nothing on Antigravity: Google's plans docs group free and Plus users on one weekly quota with Gemini 4 Hydrogen only (and Gemini 3.8 Flash until November 30, 2026), so the paid Antigravity step is Pro** (read 2026-11-26).

## Pricing

Canadian storefront, fetched 2026-09-26: Google AI Plus CA$13.99/month, Google AI Pro CA$26.99/month, Ultra not listed on that page.
US dollar list prices did not render in my fetched HTML (the 2026-11-26 fetch included), while the US page's savings calculator prints Pro at $19.99/month or $199.99/year and Ultra 5x at $99.99/month; a third-party comparison table lists Plus around $8/month as the cheapest paid path and Ultra 20x at $200/month as the top individual tier (429 again on 2026-10-16, see references).
Organizations: Google Cloud terms with consumption-based API pricing, included in select Gemini Enterprise subscriptions.
Credits bill at standard Gemini Enterprise consumption rates, anchored by the Gemini API price list as of 2026-11-26: Gemini 3.8 Flash at $0.75/$3.75 per million tokens through December 31, 2026, doubling to $1.50/$7.50 in 2027; Gemini 3.1 Pro Preview at $2.00/$12.00 for prompts up to 200k tokens, $4.00/$18.00 above; and the Gemini 4 lines now anchoring the page's top (Carbon and Argon $2.00/$10.00 through November 30, 2026, then $4.00/$20.00; Hydrogen $1.50/$7.50; Neon, the model Pro steers Antigravity and AI Studio to, $3.00/$15.00, read 2026-11-26).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-08-24 | Individuals / Pro / Ultra | Baseline: Antigravity free at $0 with basic weekly rate limits, Google AI Pro and Ultra the paid paths that raise limits and add the AI credit pool | https://antigravity.google/pricing |
| 2026-09-26 | Ladder | Verified: Plus / Pro / Ultra (5x, 20x) ladder at 2x/4x/5x-Pro/20x-Pro access, AI Premium confirmed renamed to Google AI Plus, CA$13.99 Plus and CA$26.99 Pro on the Canadian storefront | https://one.google.com/about/google-ai-plans |
| 2026-11-26 | Ladder (US comparison table) | Bundle rows first recorded in this table, the calculator's list prices held: Colab compute units 50/200/1,000/2,000 per month, Flow Music credits 3,000/10,000/30,000/30,000 per month, Google Home Premium Standard on Pro (US$10/mo value) and Advanced on Ultra (US$20/mo value), Google Health Premium on Pro and Ultra, Project Genie on Ultra; calculator reads Pro $19.99/mo or $199.99/yr (the annual figure new to this table), Ultra 5x $99.99/mo | https://one.google.com/intl/en_us/about/google-ai-plans/ |

## Compared to

- [Claude plans](../claude-plans/index.md): the same multiplier-on-a-secret-quota pattern, but Google bundles harder (Flow credits, cloud credits, YouTube) and prices its entry tier lower.
- [ChatGPT plans](../chatgpt-plans/index.md): the rival ladder, which publishes per-model message ranges where Google publishes adjectives.
- [Google Antigravity](../../surfaces/antigravity/index.md): the surface these plans meter; its free tier undercuts the paid ladder for light use, which is the sharpest critique of the ladder itself.
- [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md): the API-side alternative, still the right answer for automation and CI, and the baseline your credit pool burns at.

## Bottom line

Recommended for engineers who have actually hit the free Antigravity weekly wall and want metered overage at known API rates; start at Pro, never Plus for Antigravity, and only after two genuinely capped weeks.
Not for light users, who should stay on the free tier, and not for automation-heavy workloads, which belong on the API.
My disagreeable claim: Ultra is priced for video generation more than for coding, because the 25,000 monthly Flow credits are its most concrete differentiator, so engineers buying Ultra 20x for Antigravity are mostly buying Flow.

## Changes

- 2026-09-26 - Created when the owner asked for any remaining subscription providers.
- 2026-10-16 - Rotation re-verification: ladder, multipliers, storage, and country counts unchanged with prices still stripped client-side; the comparison table now rows Gemini 4 Argon access on every tier and a one-million-token context window on Pro and Ultra, both folded into What it is; the Antigravity pricing and plans-docs pages returned client-rendered shells this run, their claims carried as dated.
- 2026-10-31 - Rotation re-verification: ladder, multipliers, storage (including the 400 GB-or-2 TB Plus cell), Argon access, cloud credits, Flow credits, and country counts unchanged with dollar prices still stripped client-side; the Canadian storefront still CA$13.99 Plus and CA$26.99 Pro with no Ultra listed; the Antigravity pages reachable again (200) this run, the Gemini API promotional rates and the 2027 doubling unchanged, and the third-party pricing table still 429.
- 2026-11-15 - Rotation re-verification: every cited source re-fetched live with the ladder, multipliers, storage (400 GB-or-2 TB Plus cell), cloud credits, Flow credits, and country counts unchanged and the Canadian storefront still CA$13.99 Plus and CA$26.99 Pro with no Ultra; the comparison table now carries separate Carbon, Argon, and Hydrogen access rows with Carbon the Ultra headline; the US page's savings calculator now prints Pro $19.99/month and Ultra 5x $99.99/month in page text; the Antigravity plans docs' quota mechanics unchanged with Gemini 4 Hydrogen added to the baseline model list; the Gemini API anchor extended (3.1 Pro Preview's >200k-prompt surcharge $4/$18, Carbon and Argon $2/$10 through November 30 then $4/$20, Hydrogen $1.50/$7.50); the HN thread still 771 points; the third-party pricing table still 429.
- 2026-11-25 - Out-of-rotation correction on the Jules turndown, every cited URL re-fetched live: the definition and What it is no longer present Jules limits as a live plan benefit, since Google's October 29, 2026 notice says Jules "will wind down on December 31, 2026", read-only "until the end of the year" after the November 11, 2026 cutoff for sessions, and the comparison table carries no Jules row in the 2026-11-25 fetch (the Antigravity and AI Studio rows present), with the notice added to References; the Gemini API pricing reference repointed to aistudio.google.com/docs/pricing after the ai.google.dev address began 301-redirecting there, the 3.1 Pro Preview, Carbon and Argon, and Hydrogen rows re-read unchanged; the third-party pricing table 429 again; no other fact re-read.
- 2026-11-26 - Full re-verification, every cited URL re-fetched live: the comparison table carries per-model access rows (Carbon on Ultra only in the Gemini app and AI Studio, Neon on Pro and Ultra, Hydrogen on every tier; Carbon, Neon, and Hydrogen on Pro and Ultra under Antigravity, none on Plus), Google Colab compute units of 50/200/1,000/2,000 per month, Google Flow Music credits of 3,000/10,000/30,000/30,000 per month, Google Home Premium (Standard on Pro, Advanced on Ultra), Google Health Premium on Pro and Ultra, and Project Genie on Ultra, folded into What it is and one Price history row; the Antigravity plans docs group free and Plus users on one weekly Hydrogen-only quota, so the definition now names Pro and Ultra, not Plus, as the Antigravity step and a Caution says why; the US savings calculator reads an annual Pro price of $199.99; Gemini 4 Neon ($3.00/$15.00) added to the consumption anchor; the Canadian storefront, country counts, Antigravity pricing page, Jules notice, and the HN thread (771 points) unchanged; the third-party pricing table 429 again.

## See also

- [Claude plans](../claude-plans/index.md) - the multiplier-based subscription this ladder most resembles, with a longer 2026 change log.
- [ChatGPT plans](../chatgpt-plans/index.md) - the OpenAI ladder at the same price points, with more published mechanics.
- [Google Antigravity](../../surfaces/antigravity/index.md) - the free-first editor and agent platform whose limits these plans raise.
- [Model Provider Feature Matrix](../../model-provider-feature-matrix/index.md) - where the subscription ends and per-token consumption pricing begins.

## References

- https://one.google.com/about/google-ai-plans - the plan ladder, comparison table (multipliers, Flow credit quotas, Antigravity rows and, through the 2026-11-15 fetch, Jules rows, now separate Carbon/Argon/Hydrogen access rows with Carbon the Ultra headline, plus Colab, Flow Music, Home Premium, Health Premium, and Project Genie rows read 2026-11-26), AI Premium rename, country counts (fetched 200, 2026-09-26, re-fetched 2026-10-11, 2026-10-16, 2026-10-31, and 2026-11-15 with ladder prices still stripped client-side; 200 again on 2026-11-25 and on 2026-11-26 with no Jules row in the table and the per-model, Colab, Flow Music, Home Premium, Health Premium, and Project Genie rows read from its HTML)
- https://one.google.com/intl/en_us/about/google-ai-plans/ - US variant: $10/$40/$100 monthly Google Cloud credits by tier, Home Premium bundle values, Ultra 5x and 20x storage tiers, a savings calculator printing Pro $19.99/month and Ultra 5x $99.99/month (monthly billing only) in page text since 2026-11-15, Pro's $199.99 annual price read 2026-11-26 (fetched 200, 2026-09-26; 200 again on 2026-10-31; re-fetched 2026-11-15 with the calculator figures visible; 200 again on 2026-11-25 and 2026-11-26)
- https://one.google.com/about/plans - Canadian storefront prices, CA$13.99 Plus and CA$26.99 Pro, no Ultra listed (fetched 200, 2026-09-26; re-fetched 2026-10-16 with both figures unchanged; re-fetched 2026-10-31 with both figures unchanged; re-fetched 2026-11-15 with both figures unchanged; re-fetched 2026-11-25 and 2026-11-26 with both figures unchanged)
- https://antigravity.google/pricing - the $0 individual tier, Pro/Ultra as the paid paths adding rate limits and the AI credit pool, Google Cloud consumption terms for organizations (fetched 200, 2026-09-26; the 2026-10-16 fetch returned a client-rendered shell, claims carried as dated; 200 again on 2026-10-31; 200 again on 2026-11-15; 200 again on 2026-11-25; 200 again on 2026-11-26)
- https://antigravity.google/docs/plans - quota mechanics: five-hour Ultra refresh, weekly free quota, credits billed at standard Gemini Enterprise consumption pricing, Never/Always overages, no BYOK (fetched 200, 2026-09-26; the 2026-10-16 fetch returned a client-rendered shell, claims carried as dated; 200 again on 2026-10-31; re-fetched 2026-11-15 with the mechanics unchanged and Gemini 4 Hydrogen added to the baseline model list; re-fetched 2026-11-25 with free and Plus users grouped on one weekly Hydrogen-only quota, Gemini 3.8 Flash on that tier until November 30, 2026, and paid Pro listing Neon, Carbon, Argon, and Hydrogen; re-fetched 2026-11-26 with the same grouping and model lists)
- https://aistudio.google.com/docs/pricing - the consumption-rate anchor: 3.8 Flash $0.75/$3.75 per million tokens until 2026-12-31 then $1.50/$7.50, 3.1 Pro Preview $2.00/$12.00 up to 200k prompts ($4.00/$18.00 above), Carbon and Argon $2.00/$10.00 through 2026-11-30 then $4.00/$20.00, Hydrogen $1.50/$7.50, Neon $3.00/$15.00 (fetched 200, 2026-09-26; re-fetched 2026-10-16 with the promotional rates and the 2027 doubling unchanged; re-fetched 2026-10-31 unchanged; re-fetched 2026-11-15 with the anchor state above; the ai.google.dev/gemini-api/docs/pricing address began 301-redirecting here and the reference was repointed on 2026-11-25, when the 3.1 Pro Preview, Carbon and Argon, and Hydrogen rows re-read unchanged; re-fetched 2026-11-26 with every row unchanged and Neon added, the price tables read from the page's embedded markup)
- https://news.ycombinator.com/item?id=48222529 - critical source: the May 2026 "Antigravity bait and switch" thread, 771 points, on tiers changing under existing users (fetched 200, 2026-09-26; re-checked 2026-10-16 at 771 points unchanged; 200 again on 2026-10-31; re-checked 2026-11-15 at 771 points unchanged; re-checked 2026-11-25 and 2026-11-26 at 771 points unchanged)
- https://codeagentswarm.com/en/guides/grok-build-pricing - third-party table naming Plus around $8/month and Ultra 20x at $200/month; 429 again 2026-10-16, again 2026-10-31, again 2026-11-15, again 2026-11-25, and again 2026-11-26, figures carried from the 2026-08-25 verification, hold loosely
- https://jules.google/docs/changelog/2026-10-29 - Jules Turndown, Google's October 29, 2026 notice: sessions until November 11, 2026, read-only until the end of the year, and Jules "will wind down on December 31, 2026", with a Jules Tools export (fetched 200, 2026-11-25; re-fetched 2026-11-26 unchanged)
