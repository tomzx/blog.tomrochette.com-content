---
title: MiniMax Coding Plan
created: 2026-09-26
updated: 2026-10-16
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, coding-subscription, minimax, pricing]
readability: 3
audience_notes: >
  For engineers evaluating token-metered coding subscriptions from Chinese labs.
  Assumes familiarity with quota windows, cache-discount pricing, and PAYG API billing.
---

The product sold as the MiniMax Coding Plan became the MiniMax Token Plan on June 1, 2026, a usage-based subscription on platform.minimax.io that meters the M-series models through a Subscription Key.
In October 2026 the Token Plan itself closed to new purchases, replaced by the M Plan (Go, Explore, Build) at unchanged prices, the product's third identity in five months.
**MiniMax converted a liked flat coding plan into token billing overnight, without notice, and the resulting trust deficit is still the product's largest liability.**

## What it is

MiniMax (a Hong Kong-listed Chinese AI lab) now sells the M Plan in Go, Explore, and Build tiers, Explore metered at 3x Go usage and Build at 7.5x, with quotas shared across text, image, and audio models and H3 video generation on Explore and Build, the text roster led by M3.1 Flash Preview.
Existing Token Plan (Plus/Max/Ultra) subscribers keep their plan, price, and perks while automatic renewal stays on; new buyers can only get the M Plan, and upgrading is one-way.
Usage runs through a Subscription Key separate from the pay-as-you-go API key, and Anthropic-compatible endpoints let Claude Code-style harnesss plug in directly.
Quota uses a 5-hour rolling window (non-video models) plus a weekly window (all models), with no carryover.
Credits packages at 1,000 per dollar cover overflow once subscription quota runs out.

## Status

Active at company scale but turbulent: H1 2026 revenue hit $117M (up 283% year over year), ARR passed $800M by August, and July token consumption ran 20 times January's.
The stock fell more than 80% from its HK$1,330 peak to HK$298 by September 21, 2026, and JPMorgan downgraded it in June, citing M3's lack of pricing power.
The June 2 apology and compensation package followed developer complaints after the billing switch, with a refund portal on June 3.

## Strengths

- One token pool covers code, images, and speech, which suits mixed-agent workloads other coding plans exclude.
- Credits overflow means a task does not hard-stop at the quota edge, it just starts spending Credits.
- Even the top tier ($132) undercuts Western $200 plans by more than a third, on an open-weight model family.

## Cautions

- An open GitHub issue from June 3, 2026 documents quota draining with zero API calls and an unauditable cache discount, with Plus reportedly exhausted in 4-5 hours of agent work.
- The FAQ states the plan does not support refunds and that MiniMax itself recommends pay-as-you-go for production.
- Dynamic rate limiting tightens weekday peak hours (15:00-17:30), cutting Plus to roughly 3-4 concurrent agents.
- Plus rose from $20 to $22 within three months of launch, an early sign that sticker prices here move fast.
- The plan has now been rebuilt twice since June 2026, and moving to the M Plan forfeits historical Token Plan discounts and perks (the infinity limits and the 150% weekly limit) with no path back.

## Pricing

M Plan, as of 2026-10-16: Go $22/month, Explore $55/month, Build $132/month (the Plus/Max/Ultra prices carried over under new names), with a 50%-off first-month launch offer that ran through October 14, 2026.
Token Plan (legacy, closed to new purchases): Plus $22, Max $55, Ultra $132 as last listed 2026-10-14, kept by existing subscribers at unchanged prices while auto-renewal stays on; upgrades to M Plan are one-way and prorated (Plus may move to any tier, Max to Explore or Build, Ultra to Build).
All tiers run the 5-hour and weekly windows; peak-hour dynamic rate limiting persists on the M Plan, and the 3-4/4-5/6-7 concurrent-agent figures were the Token Plan documentation's numbers.
Credits cost $5, $25, or $100 at 1,000 per dollar, valid 365 days, as last verified 2026-10-14.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-06-01 | Coding Plan -> Token Plan | Flat per-task Coding Plan replaced by usage-based Token Plan at the M3 launch, without advance notice | https://news.aibase.com/news/28699 |
| 2026-06-03 | Token Plan Plus | Observed at $20/month, $200/year | https://github.com/MiniMax-AI/MiniMax-M2.7/issues/47 |
| 2026-09-26 | Token Plan Plus/Max/Ultra | Listed at $22/$55/$132, with Plus up $2 against June | https://platform.minimax.io/docs/guides/pricing-token-plan |
| 2026-10-16 | M Plan launch | Observed: Token Plan closed to new purchases and replaced by the M Plan, tiers renamed Plus/Max/Ultra to Go/Explore/Build at unchanged $22/$55/$132 monthly, launch offer of 50% off the first month through October 14, one-way prorated upgrades (Plus to any tier, Max to Explore/Build, Ultra to Build), existing subscribers grandfathered while auto-renewal stays on | https://platform.minimax.io/docs/m-plan/monthly-offer |

## Compared to

[Kimi Code](../kimi-code/index.md) sells time-windowed quota of one lab's models and fits steady daily coders better than bursty multimodal users.
[NanoGPT](../nanogpt/index.md) has no quota windows at all, removing the mid-sprint lockout risk at the cost of per-token metering.
MiniMax's own pay-as-you-go API is the right choice for production, by the company's own documentation.

## Bottom line

Recommended for tinkerers who want cheap, broad token volume across modalities and will watch the usage bar.
Not for anyone needing auditable billing, refunds, or production reliability.
I will claim something arguable: until the quota denominator and per-call billing history are published, the usage bar is a trust position rather than a meter, and the June apology does not change that.

## Changes

- 2026-09-26 - Created.
- 2026-10-06 - Converted the Compared-to cross-references from plain-text paths into working links.
- 2026-10-16 - Second restructure recorded: the Token Plan closed to new purchases and the M Plan launched in its place (Go/Explore/Build at unchanged $22/$55/$132, a 50%-off first-month offer through October 14, one-way prorated upgrades, grandfathering while auto-renewal stays on, the text roster moved to M3.1 Flash Preview with H3 video on Explore and Build); What it is and Pricing rewritten and the price history row appended.

## See also

- [Kimi Code](../kimi-code/index.md) - the window-quota counterpart from Moonshot, with its own 2026 pricing drama.
- [NanoGPT](../nanogpt/index.md) - the no-windows gateway alternative for open-weight breadth.
- [OpenCode](../../harnesses/opencode/index.md) - a harness commonly used to instrument quota burn on plans like this.
- [Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - decide the model first, then plan versus PAYG.

## References

- https://platform.minimax.io/docs/guides/pricing-token-plan - current tiers $22/$55/$132, quota windows, agent counts, Credits packages, as of 2026-10-11 and re-fetched 2026-10-14 unchanged; on 2026-10-16 the URL rendered the M Plan overview instead, so the figures stand as the last Token Plan read.
- https://platform.minimax.io/docs/m-plan/monthly-offer - the M Plan tier prices (Go $22, Explore $55, Build $132) and the 50%-off launch offer through October 14 (fetched 200, 2026-10-16).
- https://platform.minimax.io/docs/m-plan/token-plan-notice - the keep-or-upgrade arrangement: grandfathering, one-way prorated upgrades, forfeited Token Plan perks (fetched 200, 2026-10-16).
- https://platform.minimax.io/docs/m-plan/usage-rules - the M Plan window mechanics: 5-hour non-video and weekly all-model windows, credit-pack overage, peak-hour dynamic rate limiting (fetched 200, 2026-10-16).
- https://platform.minimax.io/docs/m-plan/intro - the M Plan roster: M3.1 Flash Preview text, H3 video on Explore and Build, harness guides for Claude Code, Codex, Cursor, OpenCode, Pi, Hermes Agent, and OpenClaw (fetched 200, 2026-10-16).
- https://platform.minimax.io/docs/token-plan/faq - Subscription Key mechanics, no-refund policy, production guidance, peak-hour rate limiting (live 200 on 2026-10-16 as the legacy plan's FAQ, content not re-read this run).
- https://github.com/MiniMax-AI/MiniMax-M2.7/issues/47 - critical billing-bug report: passive quota drain, unverifiable cache discount, $20 Plus in June 2026.
- https://news.aibase.com/news/28699 - the June 2, 2026 apology, compensation package, and Coding Plan to Token Plan switch.
- https://eu.36kr.com/en/p/3993817731234817 - critical business reporting: developer backlash, JPMorgan downgrade, market value collapse, H1 2026 financials.
