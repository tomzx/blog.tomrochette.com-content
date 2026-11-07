---
title: Experiential
created: 2026-09-27
updated: 2026-11-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, llm-gateway, self-hosted, model-routing]
readability: 3
audience_notes: >
  Engineers choosing a gateway in front of their model providers who want zero markup and are weighing a young YC company against incumbents.
  Assumes you know OpenAI-compatible APIs, BYOK, and per-token billing.
---

Experiential is a YC-backed, Apache-2.0 model gateway (Rust data plane, Python control plane and CLI) that serves hosted, BYOK, and local models behind one OpenAI-compatible API at zero markup, and mines your captured traffic to train routers and, on enterprise, a model you own.

**Zero markup plus traffic-trained routing is a genuinely different bargain from a percentage-fee gateway, and the price is that the product's actual input is your request log.**

## What it is

Experiential Labs' gateway runs locally via `pip install experiential` and `exp`, or hosted at platform.experientiallabs.ai with an `xpl_` key and an Anthropic Messages-compatible surface alongside the OpenAI one.
The routing thesis: standardize agent traces as OTel, mine representative tasks, simulate rollouts with text world models, score with an LLM judge, and fit a nearest-neighbor router on prompt embeddings.
The team claims a compiled Rust data plane adding under 1 ms for BYOK requests, 1000+ models refreshed daily by an agent that opens PRs, and fine-tuning of a model you own via Tinker.
A `exp capture` mode records Claude Code and Codex desktop traffic while requests go straight to the provider, which requires macOS and approving a certificate.
The GitHub repo language reads Python; the Rust data plane claim comes from the team's README and launch post.

## Status

Very active and compounding fast: 9,469 stars and 233 forks as of 2026-10-07, pushed the same day, created 2026-06-24.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=experientiallabs/experiential&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=experientiallabs/experiential&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=experientiallabs/experiential&type=date&legend=top-left" />
</picture>

The Show HN launch ("We built open OpenRouter that turns usage into a better model") reached 222 points on 2026-08-27 with 47 comments, and the star count has since grown roughly an order of magnitude past the ~820 the entrant data recorded around 2026-09-21.
PyPI shows 236 releases since first upload on 2026-08-20, latest 0.7.234, requiring Python 3.12+ (as of 2026-11-07).
One hundred forty-three open issues, a Discord, and YC backing as of 2026-10-07.
On 2026-10-10 the GitHub repository and the experientiallabs org both return 404 on the API and the web while the product site, its pricing page, and the PyPI package stay live (the package README still links the dead repo paths), so the repository is private, renamed, or removed as of this date; the 404 state persisted through the 2026-10-12, 2026-10-14, and 2026-10-16 re-checks with the site and package still live; the star count above stands at its last verification, and the site's own badge reads 9.9k.
By 2026-10-24 the repository and org were live again on both the API and the web, with the repo pushed that day and the pricing page's GitHub badge linking it again, so the removal or privacy spell ended and the 404 stretch ran from 2026-10-10 through at least 2026-10-16; the repo stayed in active push through 2026-11-07, with the v0.7.226 GitHub release published 2026-11-01, v0.7.228 on 2026-11-03, and v0.7.233 (2026-11-06) and v0.7.234 (2026-11-07) gateway-fix releases.

## Strengths

- **Credits bill at provider list price with 0% markup on routed tokens at every tier, so the gateway does not tax usage.**
- Budgets, hard caps, model allowlists, and per-agent attribution are enforced at the gateway on every request, in the free tier.
- Zero-data-retention routing and a no-training provider policy are selectable, not enterprise-gated.
- Self-hosting is one command (`uvx --from experiential exp run`), and aggregate telemetry has a documented disable path.
- The router work is unusually principled for the category, with published simulation methodology and benchmark deltas on RouterBench and TauBench.

## Cautions

- **The founder told Hacker News telemetry is off by default while the README says PostHog telemetry is enabled by default, and that contradiction was never reconciled in the thread.**
- The HN thread also drew an explicit rug-pull accusation over that default, plus the objection that a two-month, small-team build lowers the project's value.
- `exp capture` is certificate-installing interception software on your own machine, experimental, and macOS-only.
- Router switches can forfeit provider prompt-cache discounts, the thread's sharpest technical objection, and semantic caching is explicitly not planned.
- The dashboard shown in the README is the hosted platform, not something the open repo gives you, as one commenter discovered.
- 0.7.x with 159 releases in six weeks and 110 open issues is churn, not stability.

## Pricing

Free: $0 per month with no monthly credits (the 500-credit grant is gone as of 2026-10-29): a $1 card check (refunded) unlocks the core set, which is GPT-6 Luna, DeepSeek V4.1 Flash, and the CClef decision endpoint carrying no per-token charge within shared limits of 10 requests/min, 250K tokens/min, and 1M tokens/day (Jev remains zero-fee for existing accounts only), while new accounts also share 60 requests/min and 1M tokens/min across all other models with no daily cap.
Pro: $20 per month with 2,000 included credits (1 credit = 1¢), BYOK with zero data retention from this tier up, and per the 2026-11-01 plan table 100 requests/min, 1M tokens/min, and a 10M-token daily ceiling, where the same page's FAQ still carries the 2026-10-29 figures.
Max: $200 per month with 20,000 credits and a per-plan discount table (Claude Haiku 5.5, DeepSeek V4 Flash, and Qwen3.8 27B at 75% off), and per the 2026-11-01 plan table 1,000 requests/min, 10M tokens/min, and a 100M-token daily ceiling, against the page's own bill example still stating 6,000 requests/min, 100M tokens/min, and 36B tokens a day.
Ultra: $2,000 per month with 200,000 credits and Claude Haiku 5.5, DeepSeek V4 Flash, and Qwen3.8 27B at $0 with Kimi K3 45% off, and per the 2026-11-01 plan table 10,000 requests/min, 100M tokens/min, and a 1B-token daily ceiling, against the FAQ's retained 10,000 requests/min, 150M tokens/min, and 54B tokens a day.
The 2026-11-07 page still leads with "your AI bill is the plan price" and one key (959 models), now states paid-plan usage as multiples of Free's daily usage (Pro 10x, Max 100x, Ultra 1,000x) with the rate table restating the credit grants as dollar amounts ($20/$200/$2,000 included), keeps the per-plan discount section the 2026-10-29 rebuild restored (its rows render client-side, so the figures stand as the 2026-10-29 read), and holds the plan comparison table's rate rows at the 2026-11-01 cuts while its FAQ and bill example keep the older figures.
Enterprise: custom committed credits at the lowest rate, adding private networking, data residency, SSO, and security reviews.
Routed tokens stay at provider cost with 0% markup on every plan, and self-hosting the gateway is free, as of 2026-10-07 for the markup claim and 2026-11-01 for the page read.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-27 | Free / Pro / Enterprise | Baseline: Free $0 (500 credits after $1 verification), Pro introduced at $20 per month (2,000 credits), Enterprise custom committed credits | https://www.experientiallabs.ai/pricing |
| 2026-10-02 | Pro / Max / Ultra | Credit ladder documented from $20 to $199 per month (to 1,000,000 credits), with self-serve Max ($200 to $1,999) and Ultra ($2,000+) tiers and per-model discounts on the first 2,000 credits each month | https://www.experientiallabs.ai/pricing |
| 2026-10-07 | Page structure | Page rebuilt into Free/Pro/Enterprise cards with Pro/Max/Ultra as a segmented credit selector (2,000 to 1,000,000 credits/month); Free $0 and the Pro $20 floor re-verified, higher-rung dollar figures no longer in the static page, rate-limit tiers enumerated and SOC 1 added | https://www.experientiallabs.ai/pricing |
| 2026-10-10 | Per-model discounts | Discount schedule revised: GLM-5.3 Flash moved from 7.5% to 2.5% off, the first-2,000-credit free-usage set named as unlimited DeepSeek V4.1 Flash, GPT-6 Luna, Claude Haiku 5.5, and Jev, Kimi K3 11.25% and DeepSeek V4 Flash 50% unchanged, and a flat 1¢-per-credit statement added; plan prices unchanged | https://www.experientiallabs.ai/pricing |
| 2026-10-11 | Per-model discounts | Discount schedule expanded again: new 5% band for the GPT-4.1 family, GPT-4o, and the GPT-5 line, Qwen3.8 Max at 3.75%, the 2.5% band widened beyond GLM-5.3 Flash to Claude Fable 5 and 5.1, Claude Sonnet 5, Qwen3.8 2.4T A95B, Qwen3.8 Flash, and Tencent Hy4 Preview, a 1.25% band added for the older Claude models, and the flat 1¢-per-credit row added to the plan comparison table; plan prices unchanged | https://www.experientiallabs.ai/pricing |
| 2026-10-14 | Per-model discounts | Discount schedule revised again: GLM-5.3 moved to its own 7.5% line, GPT-4o dropped from the 5% band (now the GPT-4.1 family plus GPT-5 through GPT-5.4 Nano), and the plan table caps discounts at up to 25% (Free) and 50%/75%/45% (Pro/Max/Ultra); plan prices unchanged | https://www.experientiallabs.ai/pricing |
| 2026-10-24 | All plans | Page rebuilt into flat plan prices: Free $0, Pro $20, Max $200, Ultra $2,000 with fixed monthly credit grants (500/2,000/20,000/200,000 credits at 1¢), DeepSeek V4.1 Flash, GPT-6 Luna, and Jev at no per-token charge on every plan, Max at 75% off and Ultra at $0 for DeepSeek V4 Flash and Qwen3.8 27B with Kimi K3 45% off on Ultra, annual billing added, and the credit ladder, the first-2,000-credit cap, and the band schedule removed from the page | https://www.experientiallabs.ai/pricing |
| 2026-10-29 (observed) | Free / all plans | Free lost its 500-credit grant (now no monthly credits, core set metered at 10 RPM, 250K TPM, 1M tokens/day, new accounts sharing 60 RPM and 1M TPM over other models), paid plans gained daily token ceilings (Pro 9B, Max 36B, Ultra 54B), the zero-fee core set swapped Jev for the CClef decision endpoint (Jev grandfathered), a per-plan discount table returned (Claude Haiku 5.5 added at 75%-off-to-$0, GLM 5.3, Claude Sonnet 5.5, and older-Claude bands new to the table), and the model count moved to 943; plan prices unchanged at $0/$20/$200/$2,000 | https://www.experientiallabs.ai/pricing |
| 2026-11-01 (observed) | Paid plan rate table | The plan comparison table's rate rows cut sharply: Pro to 100 requests/min, 1M tokens/min, 10M tokens/day (from 1,500/25M/9B), Max to 1,000/min, 10M/min, 100M/day (from 6,000/100M/36B), Ultra to 10,000/min, 100M/min, 1B/day (from 10,000/150M/54B), while the same page's FAQ and bill example still state the older figures; plan prices, credit grants, and the discount section unchanged, and the one-key model count moved to 958 (from 943) | https://www.experientiallabs.ai/pricing |

## Compared to

- LiteLLM: the dominant self-hosted gateway, deeper enterprise controls but a weekly minor-line cadence and a March 2026 supply-chain incident; experiential is younger, lighter, and margin-free.
- OpenRouter: the hosted marketplace experiential name-checks, charging a 5.5% credit fee where experiential bills at list price; OpenRouter has the maturity and the catalog depth.
- Requesty: the other hosted gateway, at a flat 5% markup; experiential undercuts it on price and matches it on residency talking points.

## Bottom line

Recommended for cost-sensitive teams that want gateway controls and attribution without a usage tax, and that are comfortable feeding traces to a five-week-old platform.
Not for anyone who needs an audited, stable gateway today, or who cannot accept a telemetry contradiction in the project's own materials.
My disagreeable claim: the traffic-trained router is the demo rather than the product, most adopters will use this as a free OpenRouter substitute and never train anything, and that outcome is fine.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars candidates were processed.
- 2026-10-02 - Pricing page expanded: Pro became a credit ladder from $20 to $199 per month and self-serve Max ($200 to $1,999) and Ultra ($2,000+) tiers appeared above it, with model discounts on the first 2,000 credits each month; price history row appended, plus refreshed adoption numbers (7,592 stars, PyPI 0.7.141).
- 2026-10-03 - Adoption refresh: 8,032 stars, PyPI at 0.7.147 (156 releases), GitHub releases at v0.7.147, and pricing re-checked unchanged on the vendor page (Free $0, Pro $20-$199 ladder, Max $200-$1,999, Ultra $2,000+).
- 2026-10-07 - Added the experientiallabs/experiential star history chart to the Status section.
- 2026-10-07 - Pricing page restructured into Free/Pro/Enterprise cards with the Pro/Max/Ultra rungs as a segmented credit selector (2,000 to 1,000,000 credits/month), the higher-rung dollar figures no longer present in the static page (kept dated to the 2026-10-02 verification), per-tier rate limits enumerated, SOC 1 added, and per-model discounts published per model; price history row appended, plus refreshed adoption numbers (9,469 stars, PyPI 0.7.166 at 175 releases, 143 open issues).
- 2026-10-10 - Pricing re-check: the per-model discount schedule moved (GLM-5.3 Flash 7.5% to 2.5% off, the first-2,000-credit free set now named, a flat 1¢-per-credit statement added) with plan prices unchanged, and the GitHub repository and org found returning 404 while the product site and the PyPI package stay live; price history row appended.
- 2026-10-11 - Pricing re-check: the per-model discount schedule expanded again (new 5% band for the GPT-4.1 family and GPT-5 line, 3.75% Qwen3.8 Max, the 2.5% band widened to five more models, a 1.25% band for older Claude models, and the 1¢-per-credit row added to the plan table) with plan prices unchanged, the repository and org 404 state persisted through this re-check, and PyPI advanced to 0.7.178 at 186 releases; price history row appended.
- 2026-10-14 - Pricing re-check: the per-model discount schedule revised again (GLM-5.3 to its own 7.5% line, GPT-4o out of the 5% band, tier discount caps of 25%/50%/75%/45% added to the plan table) with plan prices unchanged, the repository and org 404 persisted through a fourth re-check, and PyPI advanced to 0.7.185 at 189 releases; price history row appended.
- 2026-10-24 - The repository and org returned to public access after the 404 stretch (live on both the API and the web, repo pushed 2026-10-24), and PyPI advanced to 0.7.218 at 221 releases.
- 2026-10-24 - Pricing page rebuilt into flat plan prices (Free $0, Pro $20, Max $200, Ultra $2,000 with fixed monthly credit grants, the three zero-per-token models on every plan, the credit ladder, first-2,000-credit cap, and band schedule gone); the Pricing section rewritten to the new page and a price history row appended.
- 2026-10-28 - PyPI advanced to 0.7.222 at 225 releases (GitHub release v0.7.221 published 2026-10-27) and the repo pushed 2026-10-28; the flat-plan pricing page re-checked unchanged.
- 2026-10-29 - Pricing page rebuilt again on top of the flat plans: Free dropped its 500-credit grant (now no credits, core models metered at 10 RPM, 250K TPM, and 1M tokens/day, with new accounts sharing 60 RPM and 1M TPM over other models), paid plans gained 9B/36B/54B daily token ceilings, the zero-fee core set swapped Jev for the CClef decision endpoint (Jev kept for existing accounts), a per-plan discount table returned to the page with Claude Haiku 5.5, GLM 5.3, Claude Sonnet 5.5, and the older-Claude band added, and the one-key model count moved from 961 to 943; plan prices held at $0/$20/$200/$2,000; price history row appended, and PyPI advanced to 0.7.223 at 226 releases with the repo pushed 2026-10-29.
- 2026-11-01 - Pricing-page rate rows moved again: the plan comparison table now reads Pro 100 requests/min, 1M tokens/min, 10M tokens/day, Max 1,000/min, 10M/min, 100M/day, and Ultra 10,000/min, 100M/min, 1B/day, a sharp cut against both the 10-29 table and the page's own FAQ and bill example, which still carry the 9B/36B/54B ceilings and higher per-minute figures; the one-key model count moved to 958; price history row appended, PyPI advanced to 0.7.225 at 228 releases with the v0.7.225 GitHub release published 2026-10-31 and the repo pushed 2026-11-01.

## See also

- [LiteLLM](../litellm/index.md) - the self-hosted gateway incumbent this one undercuts on markup
- [OpenRouter](../openrouter/index.md) - the hosted marketplace whose fee model experiential attacks
- [Requesty](../requesty/index.md) - the other hosted gateway, at a flat 5% markup
- [OpenCode Zen](../opencode-zen/index.md) - curated endpoints, the opposite bet to uncurated zero-markup routing
- [Ollama](../ollama/index.md) - the local runtime experiential folds into the same endpoint

## References

- https://api.github.com/repos/experientiallabs/experiential - 9,469 stars, 233 forks, Apache-2.0, pushed 2026-10-07 (fetched via the GitHub API, 2026-10-07; re-fetched 2026-10-24 with the repository and org live again after the 404 stretch, pushed 2026-10-24; re-fetched 2026-10-25, pushed 2026-10-25; re-fetched 2026-10-26, pushed 2026-10-25 unchanged with the v0.7.220 GitHub release published 2026-10-25; re-fetched 2026-10-28, pushed 2026-10-28; re-fetched 2026-10-29, pushed 2026-10-29; re-fetched 2026-11-01, pushed 2026-11-01; re-fetched 2026-11-04, pushed 2026-11-04; re-fetched 2026-11-07, pushed 2026-11-07).
- https://api.github.com/repos/experientiallabs/experiential/releases - the v0.7.234 release of 2026-11-07 (dropped Postgres connections returning a retryable 503, a max_tokens-cut reasoning turn settling as length, exp-gateway-native 0.3.181) and v0.7.233 of 2026-11-06 (Responses WebSocket capture expiry fix, exp-gateway-native 0.3.179), the two releases after the 2026-11-03 v0.7.228 fleet-lane release (fetched 200, 2026-11-07).
- https://raw.githubusercontent.com/experientiallabs/experiential/main/README.md - architecture, capture mode, PostHog telemetry enabled by default, optimize workflow (200)
- https://hn.algolia.com/api/v1/items/49471407 - Show HN thread, 222 points, created 2026-08-27, caching objection, telemetry contradiction, rug-pull accusation (200)
- https://www.experientiallabs.ai/pricing - Free $0, Pro credit ladder $20 to $199, Max $200 to $1,999, Ultra $2,000+ (dated 2026-10-02), page restructured 2026-10-07 into Free/Pro/Enterprise cards with the rungs as a credit selector, 0% markup, YC backing (200, re-fetched 2026-10-07, 2026-10-11, and 2026-10-14 with the discount schedule revised on the last two; fetched 2026-10-24 rebuilt into flat plan prices, Free/Pro/Max/Ultra at $0/$20/$200/$2,000 with fixed credit grants and the three zero-per-token models on every plan; re-fetched 2026-10-28 with the flat-plan state unchanged; re-fetched 2026-10-29 with the Free credit grant removed, daily token ceilings added, the CClef core swap, and a per-plan discount table returned; re-fetched 2026-11-01 with the plan table's rate rows cut to 10M/100M/1B tokens a day against the FAQ's retained 9B/36B/54B, the discount section present with client-side rows, and the model count at 958; re-fetched 2026-11-04 with the rate rows and the FAQ-vs-bill-example disagreement unchanged, the discount section present, and the model count at 959; re-fetched 2026-11-07 with plan prices and the rate rows unchanged, the usage lines restated as 10x/100x/1,000x Free's daily usage with the credits shown as dollar amounts in the table, the FAQ-vs-bill-example disagreement persisting, and the model count still 959)
- https://pypi.org/pypi/experiential/json - 0.7.166, first upload 2026-08-20, 175 releases, Python 3.12+ (200, re-checked 2026-10-07, 2026-10-11, 2026-10-12, and 2026-10-14, reading 0.7.178 at 186 releases on 10-11/10-12 and 0.7.185 at 189 releases on 10-14; re-checked 2026-10-24 reading 0.7.218 at 221 releases; re-checked 2026-10-25 reading 0.7.220 at 223 releases; re-checked 2026-10-26, 0.7.220 at 223 releases unchanged; re-checked 2026-10-28 reading 0.7.222 at 225 releases; re-checked 2026-10-29 reading 0.7.223 at 226 releases; re-checked 2026-11-01 reading 0.7.225 at 228 releases; re-checked 2026-11-04 reading 0.7.231 at 233 releases; re-checked 2026-11-07 reading 0.7.234 at 236 releases, uploaded 2026-11-07)
- https://platform.experientiallabs.ai/docs - fetched with status 200 but renders as an empty JavaScript shell, so nothing citable was taken from it
