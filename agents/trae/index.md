---
title: Trae
created: 2026-08-24
updated: 2026-08-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, surfaces, ai-editors, bytedance]
readability: 3
audience_notes: >
  Engineers weighing a cheap, capable AI IDE against the data-flow questions of a ByteDance product.
  Assumes you know what telemetry is and what a cloud agent task costs elsewhere.
---

Trae is ByteDance's AI IDE, a closed-source VS Code fork with SOLO agent mode and TraeWork cloud tasks, priced from free to $100/month.
Facts below verified as of 2026-08-25.

**Trae undercuts every Western rival on price while shipping comparable agent features, and the decision is entirely about whether your code can live inside that trade.**

## What it is

**A VS Code fork with an agent stack**: SOLO mode runs autonomous multi-step work, TraeWork runs concurrent cloud tasks (2 on the free tier up to 20 on Ultra), and autocomplete is unlimited on every paid tier.
An associated open-source project, trae-agent (MIT, about 12k stars), provides ByteDance's general-purpose agent framework separately from the IDE itself.
Enterprise sales run through BytePlus, ByteDance's enterprise arm.

## Status

**Active.**
Launched January 2025, shipping continuously since, with a four-tier consumer pricing ladder and enterprise availability via BytePlus, as of 2026-08-25.
The open-source sidecar went quiet: trae-agent's last commit landed February 5, 2026, with no tagged release ever published, as of 2026-08-25.
The July 2025 telemetry analysis thread kept it in the discussion, not always favorably.

## Strengths

- **The price floor is unmatched**: Lite at $3/month with $5 of usage and unlimited autocomplete, Pro at $10/month with $20 of usage and 10 concurrent cloud tasks.
- SOLO mode and cloud task concurrency arrive at price points where rivals offer none.
- The separate trae-agent framework is open source under MIT, but its February 2026 stall means it is a snapshot, not a maintained dependency.
- Free tier includes SOLO mode and 2 cloud tasks, so the trial is the real product.

## Cautions

- **A 954-point independent analysis of Trae's performance and telemetry is the required pre-adoption reading**, and its existence tells you the community's trust question was serious enough to instrument the editor.
- Closed-source fork of an open editor, from a vendor whose data practices are the explicit concern of that analysis.
- Usage is metered in "Basic usage" dollars with model-dependent burn, a second meter to watch on top of the subscription.
- Enterprise path via BytePlus adds procurement friction outside ByteDance's existing footprint.

## Pricing

Free: 5,000 autocompletions a month, SOLO mode, 2 concurrent cloud tasks.
Lite $3/month ($5 usage), Pro $10/month ($20 usage, 10 tasks), Pro+ $30/month (3.5x Pro usage, 15 tasks), Ultra $100/month (20x usage, 20 tasks, model early access), as of 2026-08-25.

## Compared to

- [Cursor](../cursor/index.md): the direct rival at 2-3x the price; pick Cursor for ecosystem and trust surface, Trae for budget.
- [Kiro](../kiro/index.md): both credit-metered; Kiro brings specs, Trae brings raw price.
- [Void](../void/index.md): the open-source fork route when trust rules out both.

## Bottom line

**Recommended for cost-sensitive work on code where the telemetry question is settled.**
Not for proprietary or regulated codebases, full stop.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [ai-tools-i-have-used](../../ai-tools-i-have-used/index.md) - how fast cheap-editor bets rotate
- [Cursor](../cursor/index.md) - the priced-up comparison

## References

- https://www.trae.ai/ - product and download entry point
- https://www.trae.ai/pricing - tiers, usage dollars, cloud task concurrency, as of 2026-08-25
- https://github.com/bytedance/trae-agent - the MIT-licensed agent framework, last commit February 5, 2026, about 12k stars as of 2026-08-25
- https://news.ycombinator.com/item?id=44703164 - the independent performance and telemetry analysis
- https://news.ycombinator.com/item?id=42811502 - the January 2025 launch thread
