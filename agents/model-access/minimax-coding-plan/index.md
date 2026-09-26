---
title: MiniMax Coding Plan
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, coding-subscription, minimax, pricing]
readability: 3
audience_notes: >
  For engineers evaluating token-metered coding subscriptions from Chinese labs.
  Assumes familiarity with quota windows, cache-discount pricing, and PAYG API billing.
---

The product sold as the MiniMax Coding Plan became the MiniMax Token Plan on June 1, 2026, a usage-based subscription on platform.minimax.io that meters the M-series models through a Subscription Key.
**MiniMax converted a liked flat coding plan into token billing overnight, without notice, and the resulting trust deficit is still the product's largest liability.**

## What it is

MiniMax (a Hong Kong-listed Chinese AI lab) sells Plus, Max, and Ultra tiers, with quotas shared across text, image, and speech models including M3 and M2.7.
Usage runs through a Subscription Key separate from the pay-as-you-go API key, and Anthropic-compatible endpoints let Claude Code-style harnesss plug in directly.
Quota uses a 5-hour rolling window plus a weekly window, with no carryover.
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

## Pricing

As of 2026-09-26: Plus $22/month, Max $55/month, Ultra $132/month, all with 5-hour rolling and weekly windows.
Typical peak-hour capacity is 3-4 (Plus), 4-5 (Max), and 6-7 (Ultra) agents.
Credits cost $5, $25, or $100 at 1,000 per dollar, valid 365 days, and a 10% referral discount applies at checkout.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-06-01 | Coding Plan -> Token Plan | Flat per-task Coding Plan replaced by usage-based Token Plan at the M3 launch, without advance notice | https://news.aibase.com/news/28699 |
| 2026-06-03 | Token Plan Plus | Observed at $20/month, $200/year | https://github.com/MiniMax-AI/MiniMax-M2.7/issues/47 |
| 2026-09-26 | Token Plan Plus/Max/Ultra | Listed at $22/$55/$132, with Plus up $2 against June | https://platform.minimax.io/docs/guides/pricing-token-plan |

## Compared to

Kimi Code (../kimi-code/index.md) sells time-windowed quota of one lab's models and fits steady daily coders better than bursty multimodal users.
NanoGPT (../nanogpt/index.md) has no quota windows at all, removing the mid-sprint lockout risk at the cost of per-token metering.
MiniMax's own pay-as-you-go API is the right choice for production, by the company's own documentation.

## Bottom line

Recommended for tinkerers who want cheap, broad token volume across modalities and will watch the usage bar.
Not for anyone needing auditable billing, refunds, or production reliability.
I will claim something arguable: until the quota denominator and per-call billing history are published, the usage bar is a trust position rather than a meter, and the June apology does not change that.

## Changes

- 2026-09-26 - Created.

## See also

- [Kimi Code](../kimi-code/index.md) - the window-quota counterpart from Moonshot, with its own 2026 pricing drama.
- [NanoGPT](../nanogpt/index.md) - the no-windows gateway alternative for open-weight breadth.
- [OpenCode](../../harnesses/opencode/index.md) - a harness commonly used to instrument quota burn on plans like this.
- [Model selection for coding tasks](../../model-selection-for-coding-tasks/index.md) - decide the model first, then plan versus PAYG.

## References

- https://platform.minimax.io/docs/guides/pricing-token-plan - current tiers $22/$55/$132, quota windows, agent counts, Credits packages, as of 2026-09-26.
- https://platform.minimax.io/docs/token-plan/faq - Subscription Key mechanics, no-refund policy, production guidance, peak-hour rate limiting.
- https://github.com/MiniMax-AI/MiniMax-M2.7/issues/47 - critical billing-bug report: passive quota drain, unverifiable cache discount, $20 Plus in June 2026.
- https://news.aibase.com/news/28699 - the June 2, 2026 apology, compensation package, and Coding Plan to Token Plan switch.
- https://eu.36kr.com/en/p/3993817731234817 - critical business reporting: developer backlash, JPMorgan downgrade, market value collapse, H1 2026 financials.
