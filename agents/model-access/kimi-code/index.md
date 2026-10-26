---
title: Kimi Code
created: 2026-09-26
updated: 2026-10-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, coding-subscription, moonshot-ai, pricing]
readability: 3
audience_notes: >
  For engineers comparing first-party coding subscriptions and their quota mechanics.
  Assumes familiarity with Claude Code-style agentic CLIs and per-token API pricing.
---

Kimi Code is Moonshot AI's developer coding subscription, selling the K-series models through a CLI, desktop app, and VS Code extension under a membership quota.
**The same membership is sold at a yen ladder on kimi.com and a dollar ladder on kimi.ai, and the entry tiers do not convert between them.**

## What it is

Moonshot AI sells Kimi Code as the developer service inside a Kimi membership, with CLI, desktop, IDE, and third-party requests drawing on one shared quota.
Third-party harnesses connect through OpenAI-compatible and Anthropic-compatible endpoints on api.kimi.com.
Model access is tiered: K2.7 Code for every paying member, K3 at full 1M context from the mid tier up, with RMB-billed Extra Usage as overflow.

## Status

Active and restructuring quickly: K3 shipped into Kimi Code on July 17, 2026, by late September a restructure had renamed tiers and dropped the weekly quota window for new members, and in October 2026 a second restructure renamed both ladders (Plus/Pro/Max/Ultra internationally, Go/Plus/Pro/Max in China, a fifth China tier, Ultra, added later that month) with the musical tiers kept on as legacy plans.
Moonshot launched Kimi K3.1 Pro on 2026-10-23, a 3T-class 1M-context multimodal flagship positioned as the K3 successor, listed on the API platform at $2/$10 per million tokens with a $4/$20 highspeed variant and cache reads at $0.20, and states the open weights will be released by November 4, 2026 (as of 2026-10-25).
The same launch started the K2 retirement clock: from October 31, 2026 the K2 series closes to newly registered platform users, with full retirement planned by the end of December 2026, and K3.1 Pro had not reached either membership ladder by 2026-10-25 (it surfaced on both sites only as a blog link).
The CLI is published on GitHub under MoonshotAI, with third-party coverage putting it at 3.2k stars in July 2026.
Independent guides multiplied through 2026, which I read as genuine adoption.

## Strengths

- The $19 entry ($15 billed annually) undercuts Claude Pro and Cursor Pro while including a 1M-context frontier-class model at the mid tier.
- The yen ladder starts at ¥49 per month, well below the $19 international entry at any recent exchange rate.
- Anthropic-compatible endpoints mean Claude Code and OpenCode work without new tooling.

## Cautions

- Coding quota shares one pool with chat, Deep Research, and other Kimi features, so non-coding usage drains your coding allowance.
- The plan ladder moved twice in 2026 and gained a China-only Ultra tier in October, so quota rules at signup may not persist.
- A February 2026 checkout experiment offered personalized first months between $0.99 and $11.99, so two subscribers on one tier can pay different prices.
- One four-month user quit, reporting that higher tiers bought less inference per dollar, not more.
- The entry tier's model sits under a retirement clock: K2.7 Code, the model every paying member codes on, is K2-series, and Moonshot cuts the whole series off from new platform users on 2026-10-31 with full retirement planned by end of December 2026, so the cheapest ladder rungs should expect a forced model swap.

## Pricing

On kimi.ai (as of 2026-10-25, re-verified unchanged from the 2026-10-21 read): Plus $19, Pro $39, Max $99, Ultra $199 per month, annual effective $15/$31/$79/$159; the former musical tiers (Moderato, Allegretto, Allegro, Vivace) are legacy plans at unchanged prices.
On kimi.com (as of 2026-10-25, re-verified unchanged from the 2026-10-21 read, when the ladder read five tiers): Go ¥49, Plus ¥99, Pro ¥199, Max ¥699, Ultra ¥1,399 per month, annual equivalents ¥39/¥79/¥159/¥559/¥1,119; the former musical tiers (Andante, Moderato, Allegretto, Allegro) are legacy plans at unchanged monthly prices, with annual billing added.
On both ladders, Go has no coding quota, Plus and above include Kimi Code under a rolling 5-hour limit with no weekly limit, legacy plans keep both the 5-hour and weekly windows, and Pro and above unlock K3 at 1M context.
The monthly pool is credits shared across every Kimi feature, and Kimi Code additionally runs under its own usage limit (a rolling 5-hour rate window for new members, the weekly window having been removed; the membership help page still phrases it as a 5-hour/weekly limit because legacy plans keep the weekly window, per the membership docs re-fetched 2026-10-11) that applies only to Kimi Code.
Extra Usage is pay-as-you-go overflow with a ¥25 minimum top-up, generally non-refundable.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-07-17 | Moderato to Vivace | Listed $19/$39/$99/$199 with time-limited promos at $15/$31/$79/$159; Kimi and Kimi Code separation announced | https://www.digitalapplied.com/blog/kimi-code-k3-hands-on-setup-plans-cache-2026 |
| 2026-09-26 | Same tiers | Promos became standard annual pricing; new plans released at unchanged prices, weekly window dropped for new members | https://www.kimi.ai/help/membership/membership-pricing |
| 2026-10-12 | Both ladders | Tier rename: international Moderato/Allegretto/Allegro/Vivace became Plus/Pro/Max/Ultra and China Andante/Moderato/Allegretto/Allegro became Go/Plus/Pro/Max at unchanged monthly prices, musical tiers designated legacy, annual billing added on both ladders | https://www.kimi.ai/help/membership/membership-pricing |
| 2026-10-19 | China ladder | Fifth tier added: Ultra at ¥1,399/month (¥13,428/year, ¥1,119 monthly equivalent with annual billing), present by the help page's screenshot captured that day; the other four tiers and the international ladder unchanged | https://www.kimi.com/en/help/membership/membership-pricing |
| 2026-10-19 | API (OpenRouter) | kimi-k3's sixteenth recorded move: the aggregator listing's input leg dropped from $0.304 to $0.239 per million tokens (output $11.936 and cache reads $0.21 held), with the input floor moving to Wafer at $0.238/$16.00, the output floor collapsing to Relace at $0.80/$3.00 on a wholesale reprice from $0.27/$14.00, InferenceNet matching the listing, and the roster at 26 endpoints | https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints |
| 2026-10-21 | API (OpenRouter) | The listing held at $0.239/$11.936 while the endpoints recomposed: the Relace outlier re-priced to $0.30/$12.00 and the output floor moved to Wafer's second endpoint at $0.36/$11.90, with Sail Research's output leg down to $5.50, new hosts Parasail and Modal widening the roster to 28, and kimi-k2.7-code holding at $0.67/$3.35 | https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints |
| 2026-10-23 | API (Moonshot) | Kimi K3.1 Pro listed at $2/$10 per million tokens (cache reads $0.20, 1M context) with a kimi-k3.1-pro-highspeed variant at $4/$20, while K3 held at $3/$15 and the K2-series coders at $0.95/$4 | https://platform.moonshot.ai/docs/pricing |
| 2026-10-24 | API (OpenRouter) | The listing's seventeenth recorded move: the main listing's output leg fell from $11.936 to $10.80 per million tokens (input $0.239 and cache reads $0.21 held) with InferenceNet following it down, Relace took the input floor at $0.2023/$7.70 (from $0.30/$12.00), Wafer's cheapest-input endpoint moved to $0.213/$24.00, Morph's input leg rose to $1.358/$14.90, the output floor held at $1.20/$5.50 on Sail Research, the roster held at 29 endpoints, and kimi-k2.7-code's listing held at $0.67/$3.35 with its cache-read leg down to $0.15 (from $0.18) | https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints |
| 2026-10-25 | API (OpenRouter) | The listing held at $0.239/$10.80 (cache reads $0.21) while the endpoints recomposed into the eighteenth recorded move: the input floor fell to Relace at $0.19/$8.94 (cache reads $0.19, from $0.2023/$7.70), Wafer's cheapest input moved to $0.20/$16.00 (from $0.213/$24.00), and Morph's input leg fell to $0.90 (from $1.358), with the output floor held at $1.20/$5.50 on Sail Research, the roster at 29 endpoints, and a new moonshotai/kimi-k3.1-pro listing at $2/$10 (cache reads $0.20) beside them | https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints |

## Compared to

[MiniMax Coding Plan](../minimax-coding-plan/index.md) meters tokens across modalities instead of time windows, cheaper at the top end but carrying 2026 billing-change baggage.
[NanoGPT](../nanogpt/index.md) fits when open-weight breadth matters more than one lab's flagship.
Claude Code or Cursor remain the picks when reliability per hour beats price per hour.

## Bottom line

Recommended for cost-sensitive daily coders who want K3's 1M context at $15 to $39 per month and accept quota churn.
Not for teams needing contract-stable plan terms after two restructures in one year.
I will claim something arguable: the ¥49 China-market ladder proves this product profits at roughly a third of the international price, which makes $19 a regional tax, not a cost.

## Changes

- 2026-09-26 - Created.
- 2026-10-06 - Converted the Compared-to cross-references from plain-text paths into working links.
- 2026-10-06 - Pricing re-verified on both membership pages; the help docs now state that Kimi Code carries its own usage limit (a rolling 5-hour rate window, the weekly window removed for new members) on top of the shared monthly credit pool, and both ladder as-of dates moved to 2026-10-06.
- 2026-10-12 - Second restructure of the year: both membership ladders renamed (international Moderato/Allegretto/Allegro/Vivace to Plus/Pro/Max/Ultra, China Andante/Moderato/Allegretto/Allegro to Go/Plus/Pro/Max) at unchanged monthly prices, the musical tiers designated legacy with their 5-hour-plus-weekly windows retained, annual billing added on both ladders, and the rolling-5-hour, no-weekly-limit rule confirmed for new Kimi Code plans; price history row appended.
- 2026-10-14 - Both ladders re-verified unchanged two days after the rename, and the pay-per-token API listing for kimi-k3 recorded in the references for the first time (InferenceNet $0.73/$10.00, Wafer $0.72/$24.00, Morph $0.75/$14.90, official $3/$15), with the day-by-day API price history kept in the harnesses note.
- 2026-10-14 - Re-recorded the pay-per-token reference after the listing churned within the day: the main listing moved to $0.70/$15.00 (cache reads $0.32) and the endpoint floor to $0.56/$14.00 on Relace, with InferenceNet matching the main listing; the move-by-move history stays in the harnesses note.
- 2026-10-16 - Re-recorded the pay-per-token reference after the listing's fifteenth recorded move: the main listing closed the day at $0.304/$11.936 (cache reads $0.21) after the output leg rose intraday from an earlier $11.588 reading, with InferenceNet matching, Relace's endpoint at $0.35/$14.00, Morph at $1.00/$14.90, and Wafer's two endpoints at $0.294/$28.00 and $0.36/$17.50; the move-by-move history stays in the harnesses note.
- 2026-10-17 - Re-recorded the pay-per-token reference after the listing churned again within the day: the main listing held at $0.304/$11.936 (cache reads $0.21) on InferenceNet, the input floor moved to Relace at $0.27/$14.23 (cache reads $0.05), and Sail Research's new fp4 endpoint took the output floor at $0.504/$8.10 as the roster widened to 26 endpoints; the move-by-move history stays in the harnesses note.
- 2026-10-21 - Defect pass over the price history: recorded the two API moves the section-root pass caught and this note lacked, the sixteenth move on 2026-10-19 (listing input leg $0.304 to $0.239, output $11.936 and cache $0.21 held, input floor to Wafer $0.238/$16.00, output floor collapsing to Relace $0.80/$3.00) and the 2026-10-21 recomposition (Relace re-priced to $0.30/$12.00, output floor to Wafer's second endpoint $0.36/$11.90, Sail Research's output leg $5.50, roster to 28 with Parasail and Modal joining), both fetched and appended as Price history rows.
- 2026-10-21 - The China ladder gained a fifth tier, Ultra at ¥1,399/month (¥13,428/year, ¥1,119 monthly equivalent with annual), present by the help page's 2026-10-19 capture, with the other four tiers and the international ladder unchanged; Price history row appended and both ladder as-of dates moved to 2026-10-21.
- 2026-10-24 - Re-recorded the pay-per-token reference after the listing's seventeenth recorded move: the main listing's output leg fell from $11.936 to $10.80 (input $0.239 and cache reads $0.21 held) with InferenceNet following, Relace took the input floor at $0.2023/$7.70, Wafer's cheapest input moved to $0.213/$24.00, Morph's input leg rose to $1.358, and the output floor held at $1.20/$5.50 on Sail Research at 29 endpoints, with kimi-k2.7-code's cache-read leg down to $0.15; the move-by-move history stays in the harnesses note.
- 2026-10-25 - Moonshot launched Kimi K3.1 Pro (2026-10-23, $2/$10 per million tokens, cache reads $0.20, 1M context, open weights promised by November 4) and started the K2 retirement clock (the series closes to new platform users 2026-10-31, full retirement planned by end of December 2026, which puts the entry tiers' K2.7 Code model on notice); recorded in Status and Cautions, with the K3.1 Pro platform price appended to Price history.
- 2026-10-25 - Re-recorded the pay-per-token reference after the listing's eighteenth recorded move: the main listing held at $0.239/$10.80 while the input floor fell to Relace at $0.19/$8.94, Wafer's cheapest input moved to $0.20/$16.00, and Morph's input leg fell to $0.90 at 29 endpoints, with kimi-k3.1-pro listed at $2/$10 beside them; the move-by-move history stays in the harnesses note.

## See also

- [MiniMax Coding Plan](../minimax-coding-plan/index.md) - the other first-party Chinese coding plan, token-metered where Kimi is window-metered.
- [NanoGPT](../nanogpt/index.md) - the gateway alternative when model breadth beats model loyalty.
- [OpenCode](../../harnesses/opencode/index.md) - a harness that drives Kimi Code's Anthropic-compatible endpoint.
- [Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - pick the model before the plan.

## References

- https://www.kimi.com/code/en - official product page; surfaces and the K3 1M-context claim.
- https://www.kimi.com/code/docs/en/kimi-code/membership.html - membership docs; new ladder (Go/Plus/Pro), weekly window removal, Extra Usage terms.
- https://www.kimi.ai/help/membership/membership-pricing - dollar pricing $19/$39/$99/$199 monthly, $15/$31/$79/$159 annual, as of 2026-10-12, when the ladder read Plus/Pro/Max/Ultra with the musical tiers designated legacy (fetched, HTTP 200; re-fetched 2026-10-14 and 2026-10-21 unchanged; re-fetched 2026-10-25 with every price unchanged).
- https://www.kimi.com/en/help/membership/membership-pricing - yen pricing ¥49/¥99/¥199/¥699/¥1,399 monthly and shared credit pool rules, as of 2026-10-21, when the ladder read Go/Plus/Pro/Max/Ultra at the four original monthly prices with annual billing added (fetched, HTTP 200; re-fetched 2026-10-14 at four tiers, the Ultra tier absent; re-fetched 2026-10-25 with every price unchanged).
- https://platform.kimi.ai/docs/models - the model-list page: K3.1 Pro described as the first K3.1-series model, a 3T-class 1M-context multimodal flagship, plus the K2 retirement statement (from 2026-10-31 the K2 series closes to newly registered users, existing users unaffected, full retirement planned by end of December 2026) (fetched 2026-10-25).
- https://platform.moonshot.ai/docs/pricing - the API platform price table: kimi-k3.1-pro $2/$10 per million tokens with cache reads $0.20 and a $4/$20 highspeed variant, kimi-k3 $3/$15, kimi-k2.7-code and kimi-k2.6 $0.95/$4, under a dismissible K3.1 Pro launch banner that carries the retire-all-K2 notice (fetched 2026-10-25; re-fetched 2026-10-26 with the table unchanged).
- https://platform.moonshot.ai/docs/guide/kimi-k3-1-pro-quickstart - the K3.1 Pro quickstart: the open-weights commitment ("weights will be released by Nov 4") with the capability-release policy statement around it (fetched 2026-10-25).
- https://www.digitalapplied.com/blog/kimi-code-k3-hands-on-setup-plans-cache-2026 - July 17, 2026 snapshot of listed vs promo prices and the separation banner.
- https://aihackers.net/value/deals/kimi-haggle/ - documented February 2026 first-month offers of $0.99 to $11.99, marked historical.
- https://www.noemititarenco.com/blog/kimi-code-plan-after-4-months-of-use-honest-review/ - skeptical four-month user review and cancellation rationale.
- https://openrouter.ai/api/v1/models - the aggregator listing behind the endpoint floor readings: kimi-k3 at $0.239/$10.80 per million tokens (cache reads $0.21) and kimi-k2.7-code at $0.67/$3.35 (cache reads $0.15, down from the $0.18 read 2026-10-21) (fetched 2026-10-21; re-fetched 2026-10-23 with both listings then unchanged; re-fetched 2026-10-24 with the kimi-k3 output leg at $10.80 and the k2.7-code cache leg at $0.15; re-fetched 2026-10-25 with both listings unchanged and moonshotai/kimi-k3.1-pro present at $2/$10, cache reads $0.20, canonical slug kimi-k3.1-pro-20261023).
- https://openrouter.ai/api/v1/models/moonshotai/kimi-k3/endpoints - the pay-per-token API listing for the K3 model the ladder gates, 29 endpoints as of 2026-10-25: main listing $0.239/$10.80 per million tokens (cache reads $0.21) matched on InferenceNet's fp4 row, cheapest input $0.19/$8.94 on Relace (cache reads $0.19), Wafer's two endpoints at $0.20/$16.00 and $0.36/$11.90, cheapest output $1.20/$5.50 on Sail Research's fp4 rows, an InferenceNet row still at $0.239/$11.936, Morph at $0.90/$14.90, and Moonshot's own endpoint at $3/$15 (fetched 2026-10-21; re-fetched 2026-10-23 with every price and floor unchanged and the roster grown to 29 endpoints; re-fetched 2026-10-24 with the output-leg drop, the Relace and Wafer input moves, and Morph's input rise; re-fetched 2026-10-25 with the listing held and the Relace, Wafer, and Morph input moves recorded; the per-move history of this churning listing is tracked in the harnesses note for the CLI).
