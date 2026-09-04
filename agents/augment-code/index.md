---
title: Augment Code
created: 2026-08-24
updated: 2026-09-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, context-engines, coding-agents, enterprise-tools]
readability: 3
audience_notes: >
  Engineers and eng leaders evaluating a context-engine-backed coding platform against harness subscriptions.
  Assumes familiarity with token economics (cache reads, service fees) and with SWE-bench style evaluation.

---

Augment Code is an AI coding platform whose core is the Context Engine, a real-time semantic index of the codebase that feeds its Auggie CLI agent and the Cosmos agent orchestration platform.
Facts below verified as of 2026-09-04.

**Augment makes the strongest documented claim in the context-engine space, that retrieval quality cuts agent token spend by a third at matched quality, and every number behind it is vendor-run, so buyer-side replication is the actual missing feature.**

## What it is

**The retrieval layer is the product; everything else is a container for it.**
The Context Engine indexes code, dependencies, docs, and commit history, and retrieves "the slice the task touches" before the model spends tokens exploring, with permission-aware access.
Auggie CLI is the terminal agent; its v2 (2026) is a fork of the open-source Pi harness with the Context Engine plugged in as an extension that registers a single `codebase-retrieval` tool.
Cosmos (launched June 3, 2026) runs fleets of "Expert" agents on triggers (PR opened, alert fired, cron), with the Prism model router, sandboxed VMs, a self-hosted daemon option, and YAML-as-code review of the whole factory.
Everything is closed-source SaaS with SOC 2 Type II, ISO 42001, zero data retention options, and a no-training-on-your-code commitment; enterprise logos include Adobe, MongoDB, and Webflow.

## Status

**Active and shipping fast, with a trust deficit from the 2025 pricing reset.**
Blog cadence runs multiple posts per month through August 28, 2026 (Cosmos launch, GPT-5.6 Sol as default in July, the Auggie harness rebuild, further PR-to-merge loop optimization).
The October 20, 2025 pricing change triggered a community revolt; the company's own Reddit response admitted 22.5% of users were consuming 20x what they paid, and the HN thread documents broken grandfathering promises.
There is no free tier as of 2026-09-02.
I could not verify funding history from primary sources in this run (the company pages do not state it and Wikipedia has no article), which is itself a signal: the public record for this company is mostly its own marketing.

## Strengths

- **Benchmark transparency is above the field's average**: the Terminal Bench 2.0 and SWE-bench Pro runs publish token categories and methodology (Harbor framework, five attempts per task), claiming 33% lower spend at equal pass rate vs Claude Code on Opus 4.7, and 41% lower on private-repo internal evals.
- The harness rebuild post is unusually concrete engineering: tool-surface narrowing to one bash and three file tools, proactive compaction on a cheaper model, and a measured 53% cheaper per SWE-bench Pro task ($1.27 vs $2.70) at matched pass rate.
- Flat, no-per-seat pricing now comes in two tiers (Standard $20/month, Business $100/month, each up to 50 seats, plan structure as of 2026-09-04), a rare anti-seat-model move.
- Model-agnostic by design, with Prism routing claimed to add 20-30% savings on top.

## Cautions

- **All efficiency claims are vendor-run against a baseline the vendor picks**; no independent replication of the Context Engine numbers exists in sources I could verify.
- The usage fee structure quietly stacks: LLM usage at provider list price plus a 40% service fee on LLM spend, plus compute, on top of the plan.
- The October 2025 pricing episode and its "inference games" framing in community discussion is a live lesson in how fast plan economics can change.
- The 2026 marketing has drifted toward unfalsifiable factory metrics (customer anecdotes of "10-15x faster" delivery) that dilute the good benchmark work.

## Pricing

**The flat plans are an entry point, not a ceiling: at their own published usage rates, a 50-seat team's real bill is dominated by tokens and the 40% service fee on them.**
Standard is $20/month flat for up to 50 seats including $20/month of usage, and Business is $100/month flat with $100/month of usage (LLM at provider list price, 40% service fee on LLM usage, plus compute), with pooled top-ups valid 12 months (plan structure as of 2026-09-04).
Enterprise is custom (unlimited users, data residency, CMEK, SIEM, dedicated support).
No free tier; trials get community support only.

## Compared to

- [Sourcegraph code context platform](../sourcegraph-code-context/index.md): retrieval sold as infrastructure to any MCP agent; Augment's engine only drives Augment's own surfaces, but goes deeper into the harness loop.
- [Claude Code](../claude-code/index.md): the subscription harness Augment benchmarks against; cheaper per task if Augment's numbers replicate, but you live in their walled garden.
- [Greptile](../greptile/index.md): validation-only and per-seat; Augment wants the whole author-review-verify loop.

## Bottom line

**Recommended for token-heavy teams on large private codebases who will re-run the benchmark on their own repos before believing it.**
Not for solo developers, OSS work, or anyone who cannot absorb a 40% service fee on top of model spend.
My disagreeable claim: if the Context Engine numbers are even half right, harness choice matters less than retrieval quality, and flat-rate subscription harnesses are selling expensive exploration that a good index eliminates, which would make Augment's pricing model the eventual default and their competitors' margins the casualty.

## See also

- [Sourcegraph code context platform](../sourcegraph-code-context/index.md) - the infrastructure-only version of the same retrieval bet
- [Greptile](../greptile/index.md) - the validation-layer counterpart with the inverse business model
- [Claude Code](../claude-code/index.md) - the baseline every context-engine benchmark measures against
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where context engines sit in the four-layer map

## References

- https://www.augmentcode.com/context-engine - Context Engine mechanics and headline efficiency claims
- https://www.augmentcode.com/blog/auggie-beats-claude-code-on-cost-and-quality - Terminal Bench 2.0 and SWE-bench Pro token/cost tables and methodology
- https://www.augmentcode.com/blog/auggie-cli-harness-rebuild-53-percent-cheaper - Pi fork, tool-surface narrowing, compaction, per-task cost table
- https://www.augmentcode.com/pricing - Business $100 flat plan, 40% service fee, usage mechanics
- https://www.augmentcode.com/blog/cosmos-the-platform-for-ai-native-engineering-teams - Cosmos launch, Experts, Prism, compliance stack
- https://docs.augmentcode.com/introduction - current product surfaces (Cosmos, Auggie CLI, IDE extensions)
- https://news.ycombinator.com/item?id=45586110 - October 2025 pricing backlash thread with the 22.5%/20x admission
