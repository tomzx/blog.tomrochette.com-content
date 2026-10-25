---
title: Google Antigravity
created: 2026-08-24
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, surfaces, ai-editors, google]
readability: 3
audience_notes: >
  Engineers evaluating Google's agent platform now that it replaced Gemini CLI for individuals.
  Assumes you know the editor-plus-agent pattern and what a rate-limited free tier means.
---

Google Antigravity is Google's agentic development platform: the Antigravity 2.0 desktop command center, an IDE, a CLI, and an SDK, free to use with weekly rate limits.

**Antigravity is the most generous free agent platform from any major lab right now, and its first year of security incidents is the checklist of what to verify before you point it at anything that matters.**

## What it is

Four surfaces share one platform: **Antigravity 2.0, a command center for multiple local agents in parallel with Projects and scheduled messages; the Antigravity IDE; the Antigravity CLI; and an SDK for prototyping custom agents in Python.**
Since June 18, 2026 it is also the only Google terminal agent for individuals, having absorbed Gemini CLI's former audience.
IDE extensions, custom agents, and remote control shipped in the August 2026 releases, on a cadence of roughly weekly blog-documented changes.

## Status

**Active and shipping fast.**
Launched November 2025, rebuilt as 2.0 at I/O on May 19, 2026, with Gemini 3.7 Flash landing August 13, 2026 and Gemini 3.8 Flash on September 1, 2026.
Enterprise access went live through Google Cloud and Gemini Enterprise subscriptions in August 2026.

## Strengths

- **The free individual tier is real**: unlimited tab completions and command requests with weekly rate limits, now carrying Gemini 3.8 Flash beside Claude Sonnet 4.6 and Opus 4.6 (thinking) and GPT-OSS 120B, the last three still dated for November 2, 2026 removal, while Gemini 3.1 Pro and the 3.6 to 3.7 Flash pair moved to Enterprise-only in the models docs (re-verified 2026-10-16).
- Paid tiers pulled further ahead of the free list: Gemini 4 Argon (announced October 13, 2026, in the App, CLI, and IDE extensions but not the Antigravity IDE itself) and Claude Sonnet 5.5 and Opus 5.5 (thinking) are Pro and Ultra models, with the Claude pair on non-trial Pro only.
- The SDK runs agents on local models with no API key: on-device through LiteRT (Gemma 4 26B) or against OpenAI-compatible local servers such as Ollama, LM Studio, and vLLM.
- Multi-agent parallel management in the 2.0 desktop app matches what Cursor and OpenChamber charge for.
- The SDK makes the harness a platform primitive, not just a product.
- Enterprise path runs on Google Cloud terms with consumption pricing, familiar territory for org buyers.

## Cautions

- **The incident record is the caution**: a November 2025 finding showed exfiltration via indirect prompt injection, December 2025 brought a report of Antigravity deleting an entire drive's contents, February 2026 brought waves of account bans, and a May 2026 thread with 771 points alleges a bait and switch on tiers.
- Weekly (not daily) free-tier limits means a heavy Tuesday can idle you until Monday.
- Account bans lock the whole Google identity, not just the product.
- The terms are exposure too: a September 2026 HN thread (338 points) discusses the clause covering use of the service in connection with products Google does not provide, under which third-party harness usage can get the whole Google account suspended, though the Antigravity team's Varun Mohan clarified inside that thread that the clause concerns the Antigravity account rather than the whole Google identity, with a rewording promised.
- The client is closed; trust rests on Google's incident response, which the bans thread suggests is blunt.
- The plans state there is no BYOK or bring-your-own-endpoint support, so the product surfaces run only on Google's quotas and model list; the SDK's local-model support is the one escape hatch.

## Pricing

Individuals: $0/month with basic weekly rate limits.
Google AI Pro and AI Ultra raise limits and add a flexible AI credit pool.
Organizations: Google Cloud terms with consumption-based API pricing via the Gemini Enterprise Agent Platform, included in select Gemini Enterprise subscriptions, Standard and Plus from $30/seat/month or pay-as-you-go with a $0 seat fee, as of 2026-10-16 (re-verified, unchanged).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-08-24 | Individuals | Free at launch, $0/month with basic weekly rate limits | https://antigravity.google/pricing |
| 2026-10-05 | Gemini Enterprise Standard/Plus | First observed org-side prices: Standard/Plus from $30 USD per seat per month, or pay-as-you-go with a $0 seat fee and consumption-based API pricing; Individuals unchanged at $0/month. | https://antigravity.google/pricing |

## Compared to

- [Cursor](../cursor/index.md): the commercial benchmark; Antigravity's free tier undercuts it, Cursor's polish and ecosystem still lead.
- [OpenChamber](../openchamber/index.md): the open alternative for multi-agent management on your own model keys.
- [Gemini CLI](../../harnesses/gemini-cli/index.md): the product Antigravity replaced for individuals; read its note for the transition terms.

## Bottom line

**Recommended for engineers who want a capable multi-agent platform at $0 and can live with Google account coupling.**
Not for proprietary-code environments that cannot absorb prompt-injection class incidents or blunt moderation.

## Changes

- 2026-08-24 - Created in the owner-requested Surfaces expansion.
- 2026-09-16 - Added the September 2026 terms-of-service thread (337 points) to Cautions and References, on third-party harness usage risking Google account suspension.
- 2026-09-25 - Added the Price history table the pricing rule requires, seeded with the $0/month individuals baseline.
- 2026-09-26 - Linked the Google AI plans note in the Model access category, where the paid Pro/Ultra ladder behind the credit pool is tracked.
- 2026-10-05 - Recorded the org-side prices the pricing page now exposes: Gemini Enterprise Standard/Plus from $30/seat/month or pay-as-you-go at a $0 seat fee; the individual $0 tier unchanged.
- 2026-10-07 - Recorded the models-docs lineup change: Claude Sonnet 5.5 and Opus 5.5 (thinking) joined as paid-tier models while the Claude Sonnet and Opus 4.6 pair and gpt-oss-120b carry a November 2, 2026 removal date, and added the SDK's local-model paths (LiteRT on-device or OpenAI-compatible servers) against the plans' explicit no-BYOK statement; prices unchanged.
- 2026-10-16 - Rotation re-verification, all cited URLs re-fetched live: recorded Gemini 4 Argon joining the paid tiers (October 13, App, CLI, and IDE extensions, not the Antigravity IDE) and Gemini 3.1 Pro plus the 3.6 to 3.7 Flash pair moving to Enterprise-only in the models docs, and added the vendor's in-thread clarification that the September ToS clause concerns the Antigravity account rather than the whole Google identity; prices unchanged.
- 2026-10-25 - Rotation re-verification, all eleven cited URLs re-fetched live: the pricing page, the models table (Argon on Pro, Ultra, and Enterprise; the November 2, 2026 removal dates on the Claude 4.6 pair and GPT-OSS-120b), the no-BYOK plans statement, the SDK local-models page, the Gemini CLI transition post, and all four threads (launch 1088, exfiltration 768, bait-and-switch 771, ToS 338) stand; prices unchanged.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where Antigravity sits across the surface and harness layers
- [Gemini CLI](../../harnesses/gemini-cli/index.md) - the consumer shutdown that funneled users here
- [Google AI plans](../../model-access/google-ai-plans/index.md) - the paid ladder behind the credit pool this note's free tier sits under
- [Attention Engineering](../../../attention-engineering/index.md) - why grounding-heavy agents change what you verify

## References

- https://antigravity.google/ - product family, 2.0 command center, IDE, CLI, SDK, re-verified 2026-10-25
- https://antigravity.google/pricing - tiers, model lists, weekly limits, enterprise terms, re-verified 2026-10-25 (unchanged from the 2026-10-06 reading)
- https://antigravity.google/docs/models - the model availability table: Gemini 4 Argon on Pro, Ultra, and Enterprise (App, CLI, and extensions, not the IDE), 3.8 Flash and the Claude 4.6 pair and GPT-OSS 120B on the free column with the November 2, 2026 removal dates, and 3.1 Pro plus 3.6/3.7 Flash Enterprise-only, re-verified 2026-10-25
- https://antigravity.google/blog/gemini-4-argon-in-google-antigravity - the October 13, 2026 Argon rollout post: Pro and Ultra subscribers, desktop app and CLI first, Gemini Enterprise and API for business, re-verified 2026-10-25
- https://antigravity.google/docs/plans/ - the free tier's weekly quota, the five-hour refresh on paid tiers, and the explicit no-BYOK statement, re-verified 2026-10-25 (unchanged)
- https://antigravity.google/docs/sdk/local-models/ - the SDK's LiteRT on-device path (Gemma 4 26B) and OpenAI-compatible local-server path (Ollama, LM Studio, vLLM), re-verified 2026-10-25 (unchanged)
- https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ - the Gemini CLI transition and June 18, 2026 cutoff
- https://news.ycombinator.com/item?id=45967814 - the November 2025 launch thread
- https://news.ycombinator.com/item?id=46048996 - the exfiltration-via-prompt-injection finding
- https://news.ycombinator.com/item?id=48222529 - the May 2026 bait-and-switch thread
- https://news.ycombinator.com/item?id=49548452 - the September 2026 terms-of-service thread, 338 points
