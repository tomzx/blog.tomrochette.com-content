---
title: Experiential
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, llm-gateway, self-hosted, model-routing]
readability: 3
audience_notes: >
  Engineers choosing a gateway in front of their model providers who want zero markup and are weighing a young YC company against incumbents.
  Assumes you know OpenAI-compatible APIs, BYOK, and per-token billing.
---

Experiential is a YC-backed, Apache-2.0 model gateway (Rust data plane, Python control plane and CLI) that serves hosted, BYOK, and local models behind one OpenAI-compatible API at zero markup, and mines your captured traffic to train routers and, on enterprise, a model you own.

**Zero markup plus traffic-trained routing is a genuinely different bargain from a percentage-fee gateway, and the price is that the product's real input is your request log.**

## What it is

Experiential Labs' gateway runs locally via `pip install experiential` and `exp`, or hosted at platform.experientiallabs.ai with an `xpl_` key and an Anthropic Messages-compatible surface alongside the OpenAI one.
The routing thesis: standardize agent traces as OTel, mine representative tasks, simulate rollouts with text world models, score with an LLM judge, and fit a nearest-neighbor router on prompt embeddings.
The team claims a compiled Rust data plane adding under 1 ms for BYOK requests, 1000+ models refreshed daily by an agent that opens PRs, and fine-tuning of a model you own via Tinker.
A `exp capture` mode records Claude Code and Codex desktop traffic while requests go straight to the provider, which requires macOS and approving a certificate.
The GitHub repo language reads Python; the Rust data plane claim comes from the team's README and launch post.

## Status

Very active and compounding fast: 9,303 stars and 231 forks as of 2026-10-06, pushed the same day, created 2026-06-24.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=experientiallabs/experiential&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=experientiallabs/experiential&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=experientiallabs/experiential&type=date&legend=top-left" />
</picture>

The Show HN launch ("We built open OpenRouter that turns usage into a better model") reached 222 points on 2026-08-27 with 47 comments, and the star count has since grown roughly an order of magnitude past the ~820 the entrant data recorded around 2026-09-21.
PyPI shows 166 releases since first upload on 2026-08-20, latest 0.7.157, requiring Python 3.12+ (as of 2026-10-06).
One hundred eighteen open issues, a Discord, and YC backing as of 2026-10-06.

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

Free plan: $0 per month, 500 hosted credits monthly after a one-time $1 card verification.
Pro is a credit ladder from $20 to $199 per month (2,000 credits at the $20 floor, scalable to 1,000,000), and above it sit self-serve Max ($200 to $1,999 per month) and Ultra ($2,000 and up) tiers with higher rate limits (Free Tier 1, Pro Tier 2, Max Tier 3, Ultra Tier 4, Tier 5 by request).
Model discounts (up to 100% off select models, for example 50% off DeepSeek V4 Flash) apply to the first 2,000 credits of usage each month, then list price.
Enterprise: custom committed credits at the lowest rate, adding SSO/SAML/SCIM, advanced RBAC, private networking, data residency, security reviews, and a model trained on your traffic.
Routed tokens stay at provider cost with 0% markup on every plan, and self-hosting the gateway is free, as of 2026-10-06.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-27 | Free / Pro / Enterprise | Baseline: Free $0 (500 credits after $1 verification), Pro introduced at $20 per month (2,000 credits), Enterprise custom committed credits | https://www.experientiallabs.ai/pricing |
| 2026-10-02 | Pro / Max / Ultra | Credit ladder documented from $20 to $199 per month (to 1,000,000 credits), with self-serve Max ($200 to $1,999) and Ultra ($2,000+) tiers and per-model discounts on the first 2,000 credits each month | https://www.experientiallabs.ai/pricing |

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

## See also

- [LiteLLM](../litellm/index.md) - the self-hosted gateway incumbent this one undercuts on markup
- [OpenRouter](../openrouter/index.md) - the hosted marketplace whose fee model experiential attacks
- [Requesty](../requesty/index.md) - the other hosted gateway, at a flat 5% markup
- [OpenCode Zen](../opencode-zen/index.md) - curated endpoints, the opposite bet to uncurated zero-markup routing
- [Ollama](../ollama/index.md) - the local runtime experiential folds into the same endpoint

## References

- https://api.github.com/repos/experientiallabs/experiential - 9,303 stars, 231 forks, Apache-2.0, pushed 2026-10-06 (fetched via the GitHub API, 2026-10-06)
- https://raw.githubusercontent.com/experientiallabs/experiential/main/README.md - architecture, capture mode, PostHog telemetry enabled by default, optimize workflow (200)
- https://hn.algolia.com/api/v1/items/49471407 - Show HN thread, 222 points, created 2026-08-27, caching objection, telemetry contradiction, rug-pull accusation (200)
- https://www.experientiallabs.ai/pricing - Free $0, Pro credit ladder $20 to $199, Max $200 to $1,999, Ultra $2,000+, 0% markup, YC backing (200, re-fetched unchanged 2026-10-06)
- https://pypi.org/pypi/experiential/json - 0.7.157, first upload 2026-08-20, 166 releases, Python 3.12+ (200, re-checked 2026-10-06)
- https://platform.experientiallabs.ai/docs - fetched with status 200 but renders as an empty JavaScript shell, so nothing citable was taken from it
