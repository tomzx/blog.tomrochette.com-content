---
title: Trae
created: 2026-08-24
updated: 2026-09-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, surfaces, ai-editors, bytedance]
readability: 3
audience_notes: >
  Engineers weighing a cheap, capable AI IDE against the data-flow questions of a ByteDance product.
  Assumes you know what telemetry is and what a cloud agent task costs elsewhere.
---

Trae is ByteDance's AI IDE, a closed-source VS Code fork with SOLO agent mode and TraeWork cloud tasks, priced from free to $200/month.
Facts below verified as of 2026-09-18.

**Trae's September 2026 repricing roughly doubled every paid tier and erased the price edge that justified the telemetry trade, so the decision is now purely about whether your code can live inside that trade.**

## What it is

**A VS Code fork with an agent stack**: SOLO mode runs autonomous multi-step work, TraeWork runs concurrent cloud tasks (2 on the free tier up to 20 on Ultra), and autocomplete is unlimited on every paid tier.
An associated open-source project, trae-agent (MIT, about 12k stars), provides ByteDance's general-purpose agent framework separately from the IDE itself.
Enterprise sales run through BytePlus, ByteDance's enterprise arm.

## Status

**Active.**
Launched January 2025, shipping continuously since, with a free tier plus a three-run paid ladder after the September 2026 repricing and enterprise availability via BytePlus, as of 2026-09-18.
The open-source sidecar went quiet: trae-agent's last commit landed February 5, 2026, with no tagged release ever published, as of 2026-09-18.
The July 2025 telemetry analysis thread kept it in the discussion, not always favorably.

## Strengths

- **The post-reprice ladder still meters usage dollars equal to the subscription fee**: Pro at $20/month includes $20 of usage, unlimited autocomplete, and 10 concurrent cloud tasks, with 15 tasks at Pro+ and 20 plus model early access at Ultra.
- SOLO mode and TraeWork cloud tasks remain the differentiators, and concurrency is gated by tier (10 on Pro, 15 on Pro+, 20 on Ultra) rather than by a new product wall.
- The separate trae-agent framework is open source under MIT, but its February 2026 stall means it is a snapshot, not a maintained dependency.
- The free tier still includes 5,000 completions a month and 2 concurrent cloud tasks, so the trial remains real.

## Cautions

- **A 954-point independent analysis of Trae's performance and telemetry is the required pre-adoption reading**, and its existence tells you the community's trust question was serious enough to instrument the editor.
- Closed-source fork of an open editor, from a vendor whose data practices are the explicit concern of that analysis.
- Usage is metered in "Basic usage" dollars with model-dependent burn, a second meter to watch on top of the subscription.
- Enterprise path via BytePlus adds procurement friction outside ByteDance's existing footprint.

## Pricing

Free: 5,000 autocompletions a month, limited usage, 2 concurrent cloud tasks.
Pro $20/month ($20 usage, unlimited autocomplete, 10 tasks), Pro+ $60/month ($60 usage, 15 tasks), Ultra $200/month ($200 usage, 20 tasks, model early access), as of 2026-09-18.
A September 2026 repricing roughly doubled every paid tier and dropped the $3 Lite tier; as of 2026-09-16 the ladder was Lite $3 ($5 usage), Pro $10 ($20 usage, 10 tasks), Pro+ $30, Ultra $100.

## Compared to

- [Cursor](../cursor/index.md): the direct rival at matching tier prices since the reprice; pick Cursor for ecosystem and trust surface, Trae only where the telemetry question is settled.
- [Kiro](../kiro/index.md): both meter usage; Kiro brings specs and AWS gravity, Trae brings a plain VS Code fork without the spec ceremony.
- [Void](../void/index.md): the open-source fork route when trust rules out both.

## Bottom line

**Recommended for cost-tolerant work on code where the telemetry question is settled.**
Not for proprietary or regulated codebases, full stop.

## Changes

- 2026-08-24 - Created in the owner-requested Surfaces expansion, recording the ByteDance tiers, SOLO mode, and the telemetry analysis.
- 2026-08-25 - Recorded the trae-agent stall (last commit February 2026, no tagged release) and reframed the sidecar as a snapshot.
- 2026-09-18 - Recorded the September 2026 repricing: the $3 Lite tier is gone and paid tiers doubled (Pro $10 to $20, Pro+ $30 to $60, Ultra $100 to $200), with usage dollars raised to match.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [ai-tools-i-have-used](../../../ai-tools-i-have-used/index.md) - how fast cheap-editor bets rotate
- [Cursor](../cursor/index.md) - the priced-up comparison

## References

- https://www.trae.ai/ - product and download entry point
- https://www.trae.ai/pricing - tiers, usage dollars, cloud task concurrency, as of 2026-09-18
- https://github.com/bytedance/trae-agent - the MIT-licensed agent framework, last commit February 5, 2026, about 12k stars as of 2026-09-18
- https://news.ycombinator.com/item?id=44703164 - the independent performance and telemetry analysis
- https://news.ycombinator.com/item?id=42811502 - the January 2025 launch thread
