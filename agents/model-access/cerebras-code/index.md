---
title: Cerebras Code
created: 2026-09-26
updated: 2026-09-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, inference, coding]
readability: 3
audience_notes: >
  For developers considering a speed-first coding subscription. Assumes familiarity with tokens per second, daily token quotas, and bring-your-own-key editors.
---

Cerebras Code is a subscription from chipmaker Cerebras that sells fast inference on one open coding model at $50/month (Pro) and $200/month (Max).
**The pitch is speed, and the record shows the speed claim and the quota fine print are the two things to verify before paying.**

## What it is

A hosted coding-inference plan on Cerebras wafer-scale hardware, consumed by pointing any OpenAI-compatible editor or agent (Cline, OpenCode, Crush, Cursor) at a Cerebras API key.
It launched August 1, 2025 with Qwen3-Coder-480B advertised at up to 2,000 tokens per second and a 131k context window.
As of 2026-09-26 the product page promotes GLM 4.7 at "1,000 tokens+ per second", so the headline model has already been swapped once.

## Status

Launched August 1, 2025 and drew 449 points and 172 comments on Hacker News the same day.
Launch windows sold out repeatedly, and as of 2026-09-26 both Pro and Max are marked "sold out" on cerebras.ai/code, with a limited free trial still open.
The model changed from Qwen3-Coder to GLM 4.7 between launch and now, which shows the plan follows whichever open model is fastest rather than committing to one family.
I could not verify funding or subscriber counts.

## Strengths

- Speed is genuinely differentiated: even its harshest reviewer calls Cerebras the fastest provider of its model, bar none.
- Flat monthly pricing with published daily allowances (24M tokens Pro, 120M Max) instead of per-token anxiety.
- Bring-your-own-editor stance with OpenAI-compatible endpoints, no proprietary IDE lock-in.
- By October 2025 the original tokens-per-minute caps had been raised in response to criticism.

## Cautions

- The marketing number did not survive contact: InfoWorld measured well under 500 tokens/second and often under 100, against the "up to 2,000" claim.
- Undocumented throttles drove the experience: 300k TPM on Pro and 400k on Max produced 429 errors mid-session, and an early buyer reported a 7.5M-token daily cap hidden behind an advertised 1,000-request limit.
- 131k context is about half the model's native window and demands careful context management.
- At launch there was no prompt caching, which made agent loops expensive at the $2/1M API rate, and the usage console had defects (a Max purchase provisioning as Pro).
- Cerebras declined InfoWorld's request for comment on these issues.

## Pricing

Pro costs $50/month with up to 24M tokens/day, and Max costs $200/month with up to 120M tokens/day.
Both plans were marked sold out as of 2026-09-26; a free tier with limited tokens remains for connection testing.
The underlying API price at launch was $2 per 1M input and $2 per 1M output on Qwen3-Coder.
The current per-token table on cerebras.ai/pricing renders client-side and I could not extract it, so treat current API rates as unverified.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2025-08-01 | Pro / Max | Launched at $50/month (24M tokens/day) and $200/month (120M tokens/day) | Cerebras blog and HN thread |
| 2025-09-15 | Pro / Max | TPM caps (300k/400k) documented as the binding limit; prompt caching promised | InfoWorld review |
| 2025-10-28 | Pro / Max | Caps reported improved; Qwen3 deprecated in favor of GLM-4.6 from November | InfoWorld follow-up |
| 2026-09-26 | Pro / Max | Prices unchanged at $50/$200 but both marked sold out; model now GLM 4.7 | cerebras.ai/code |

## Compared to

- [- Chutes](../chutes/index.md) is the cheap multi-model pay-as-you-go option; choose Chutes for price and variety, Cerebras when seconds per response matter.
- [- GLM Coding Plan](../glm-coding-plan/index.md) undercuts Cerebras on quota per dollar and now serves the same GLM family; choose it for volume, Cerebras for raw tokens per second.

## Bottom line

Recommended for developers whose bottleneck is iteration latency and who code in bursts that fit the daily token allowance.
Not for heavy all-day agent runs, where the TPM throttles and 131k context cut the advertised advantage.
Claim to disagree with: at the documented throttles, Max at $200 was worse value than four Pro accounts, because 4x300k TPM beats 400k TPM.

## Changes

- 2026-09-26 - Created.

## See also

- [- Chutes](../chutes/index.md) - the low-price multi-model alternative.
- [- GLM Coding Plan](../glm-coding-plan/index.md) - the quota-heavy alternative now running the same model family.
- [- Cline](../../harnesses/cline/index.md) - the editor integration Cerebras documents first.
- [- OpenCode](../../harnesses/opencode/index.md) - a terminal harness that consumes Cerebras keys.
- [- Model provider feature matrix](../../model-provider-feature-matrix/index.md) - where Cerebras Code sits among access providers.

## References

- https://www.cerebras.ai/blog/introducing-cerebras-code - launch post: $50/$200 tiers, 24M/120M tokens/day, 2,000 tok/s claim, 131k context (fetched, HTTP 200).
- https://www.cerebras.ai/blog/qwen3-coder-480b-is-live-on-cerebras - Qwen3-Coder launch, $2/1M API rate, "20x higher coding speed" claim (fetched, HTTP 200).
- https://www.cerebras.ai/code - current product page: GLM 4.7 at 1,000+ tok/s, Pro and Max both marked "sold out" (fetched, HTTP 200, as of 2026-09-26).
- https://news.ycombinator.com/item?id=44762959 - launch-day reception: 449 points, 172 comments, top comment flags missing caching (fetched, HTTP 200).
- https://www.infoworld.com/article/4055909/ - critical review, Sep 15, 2025: disputed tok/s claims, TPM caps, 131k context, billing mixups, no vendor comment (fetched, HTTP 200).
- https://www.infoworld.com/article/4075825/how-to-vibe-code-for-free-or-almost-free.html - follow-up: caps improved, Qwen3 deprecated for GLM-4.6, "fastest bar none" (fetched, HTTP 200).
- https://www.reddit.com/r/LocalLLaMA/comments/1mfeazc/ - critical post, Aug 2, 2025: advertised 1,000 requests/day actually a 7.5M-token cap, "request" defined at ~8k tokens (retrieved, HTTP 200, via the Arctic Shift archive API).
