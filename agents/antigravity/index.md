---
title: Google Antigravity
created: 2026-08-24
updated: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, surfaces, ai-editors, google]
readability: 3
audience_notes: >
  Engineers evaluating Google's agent platform now that it replaced Gemini CLI for individuals.
  Assumes you know the editor-plus-agent pattern and what a rate-limited free tier means.
---

Google Antigravity is Google's agentic development platform: the Antigravity 2.0 desktop command center, an IDE, a CLI, and an SDK, free to use with weekly rate limits.
Facts below verified as of 2026-08-30.

**Antigravity is the most generous free agent platform from any major lab right now, and its first year of security incidents is the checklist of what to verify before you point it at anything that matters.**

## What it is

Four surfaces share one platform: **Antigravity 2.0, a command center for multiple local agents in parallel with Projects and scheduled messages; the Antigravity IDE; the Antigravity CLI; and an SDK for prototyping custom agents in Python.**
Since June 18, 2026 it is also the only Google terminal agent for individuals, having absorbed Gemini CLI's former audience.
IDE extensions, custom agents, and remote control shipped in the August 2026 releases, on a cadence of roughly weekly blog-documented changes.

## Status

**Active and shipping fast.**
Launched November 2025, rebuilt as 2.0 at I/O on May 19, 2026, with Gemini 3.7 Flash landing August 13, 2026.
Enterprise access went live through Google Cloud and Gemini Enterprise subscriptions in August 2026.

## Strengths

- **The free individual tier is real**: unlimited tab completions and command requests against Gemini 3.5 Flash, Gemini 3.1 Pro, Gemini 3 Flash, Claude Sonnet and Opus 4.6, and gpt-oss-120b, with weekly rate limits.
- Multi-agent parallel management in the 2.0 desktop app matches what Cursor and OpenChamber charge for.
- The SDK makes the harness a platform primitive, not just a product.
- Enterprise path runs on Google Cloud terms with consumption pricing, familiar territory for org buyers.

## Cautions

- **The incident record is the caution**: a November 2025 finding showed exfiltration via indirect prompt injection, December 2025 brought a report of Antigravity deleting an entire drive's contents, February 2026 brought waves of account bans, and a May 2026 thread with 771 points alleges a bait and switch on tiers.
- Weekly (not daily) free-tier limits means a heavy Tuesday can idle you until Monday.
- Account bans lock the whole Google identity, not just the product.
- The client is closed; trust rests on Google's incident response, which the bans thread suggests is blunt.

## Pricing

Individuals: $0/month with basic weekly rate limits.
Google AI Pro and AI Ultra raise limits and add a flexible AI credit pool.
Organizations: Google Cloud terms with consumption-based API pricing via the Gemini Enterprise Agent Platform, included in select Gemini Enterprise subscriptions, as of 2026-08-24.

## Compared to

- [Cursor](../cursor/index.md): the commercial benchmark; Antigravity's free tier undercuts it, Cursor's polish and ecosystem still lead.
- [OpenChamber](../openchamber/index.md): the open alternative for multi-agent management on your own model keys.
- [Gemini CLI](../gemini-cli/index.md): the product Antigravity replaced for individuals; read its note for the transition terms.

## Bottom line

**Recommended for engineers who want a capable multi-agent platform at $0 and can live with Google account coupling.**
Not for proprietary-code environments that cannot absorb prompt-injection class incidents or blunt moderation.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where Antigravity sits across the surface and harness layers
- [Gemini CLI](../gemini-cli/index.md) - the consumer shutdown that funneled users here
- [Attention Engineering](../../attention-engineering/index.md) - why grounding-heavy agents change what you verify

## References

- https://antigravity.google/ - product family, 2.0 command center, IDE, CLI, SDK
- https://antigravity.google/pricing - tiers, model lists, weekly limits, enterprise terms, as of 2026-08-24
- https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ - the Gemini CLI transition and June 18, 2026 cutoff
- https://news.ycombinator.com/item?id=45967814 - the November 2025 launch thread
- https://news.ycombinator.com/item?id=46048996 - the exfiltration-via-prompt-injection finding
- https://news.ycombinator.com/item?id=48222529 - the May 2026 bait-and-switch thread
