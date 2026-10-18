---
title: Junie
created: 2026-08-22
updated: 2026-10-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, coding-agents, harnesses, jetbrains, byok]
readability: 3
audience_notes: >
  Engineers living in JetBrains IDEs who want an agent grounded in IDE-grade analysis.
  Assumes you know what a language server or IDE inspection is and what BYOK means.

---

Junie is JetBrains' coding agent: an LLM-agnostic CLI that also ships in JetBrains IDEs and CI, authenticating either to JetBrains or to your own model keys.

**Junie quietly became the most vendor-flexible of the major agents (any provider, any local model, zero markup on keys), and its thin independent community, not its capability, is the actual adoption risk.**

## What it is

The `junie` CLI runs from the terminal, in any IDE, in GitHub Actions (via `/install-github-action`), and in GitLab CI/CD.
Junie plans before it edits: advanced plan mode writes structured requirements, design, and delivery stages into `.junie/plans` files you can edit and commit, with live prompting to steer mid-task and human-in-the-loop execution allowlists.
**Guidelines and Agent Skills are shared across the CLI and the IDEs via ACP, which JetBrains co-created.**
Remote control lets you start work on your laptop and review the PR from your phone.
BYOK covers Anthropic, OpenAI, Google, xAI, OpenRouter, Copilot, and local models.

## Status

**Active.**
Junie started as an IDE agent in January 2025 (53.6% on SWE-bench Verified at announcement), went GA in April 2025, and the LLM-agnostic CLI followed into beta and beyond.
The GitHub repository (installer and release channels: release, EAP, nightly, experimental) shows 478 stars as of 2026-10-15.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=JetBrains/junie&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=JetBrains/junie&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=JetBrains/junie&type=date&legend=top-left" />
</picture>

In August 2026 JetBrains launched Junie Local, a free on-device build for M5 Macs that runs a bundled, tuned model entirely locally with no registration, subscription, or credits ([launch post](https://blog.jetbrains.com/junie/2026/08/junie-local-launch/)).
In October 2026 Junie Local widened past the Mac: it runs on NVIDIA RTX Spark machines (Windows on Arm) from day one of that platform, Windows support on RTX cards with at least 24 GB of VRAM moved from experimental to stable, and the local model is now a choice of Qwen3.6-27B or the merged Qwen3.8-3.6-27B-blend ([RTX Spark post](https://blog.jetbrains.com/junie/2026/10/junie-local-rtx-spark/)).
The client is proprietary under JetBrains AI terms; the repo is distribution, not source.

## Strengths

- **The IntelliJ analysis engine grounds edits** the way Crush uses LSPs, but from a decade of IDE inspections.
- Plan artifacts live in your repository as reviewable files, the right place for them.
- BYOK at provider rates with zero markup, including local models, from a major vendor.
- ACP means the same skills run in your IDE and your terminal.

## Cautions

- **Community footprint is small**: launch-era HN threads drew dozens of points and near-zero discussion, which is itself a signal about mindshare versus Claude Code or OpenCode.
- Cloud usage is metered in AI credits (10 per 30 days on AI Pro, 35 on AI Ultimate), so subscription-only users will exhaust quota quickly; BYOK is effectively required for cloud work, though the on-device Junie Local (August 2026, widened to NVIDIA RTX Spark and stable Windows in October 2026) now gives Mac and RTX users a free local path (an M5 Mac with 64 GB of RAM, or a 24 GB RTX card, per JetBrains).
- Early IDE reviewers reported crashes, restarts, and fast quota burn.
- Its benchmark claims (SWE-Rebench top performer, per the site) are the vendor's own.

## Pricing

Free to start (5 AI credits, no card).
JetBrains AI Pro $8.33 per user/month (annual) and AI Ultimate $25 per user/month include the credit allowances above.
**BYOK bypasses metering at provider rates.**
Junie Local is free: it runs inside Junie on an M5 Mac, an NVIDIA RTX Spark, or a Windows PC with a 24 GB RTX card, with the bundled model downloaded locally, no account or credits at all.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-09 | AI Pro, AI Ultimate | Baseline: free start (5 credits, no card), AI Pro $8.33/user/mo annual, AI Ultimate $25/user/mo, credit-metered; BYOK at provider rates; Junie Local free since August 2026. | [junie.jetbrains.com](https://junie.jetbrains.com/) |

## Compared to

- [Claude Code](../claude-code/index.md) and [Codex](../codex/index.md): subscription-first, single-vendor model access; Junie is the model-agnostic counter.
- [Crush](../crush/index.md): terminal-only LSP grounding; Junie adds the full IDE inspection stack.
- [OpenCode](../opencode/index.md): open client versus JetBrains' proprietary one, similar BYOK economics.

## Bottom line

**Recommended for JetBrains-first teams who want one agent across IDE, terminal, and CI on their own keys.**
Not for anyone who needs an open client or a large community ecosystem today.

## Changes

- 2026-08-22 - Created as one of the eight seed notes of the Harnesses category.
- 2026-08-23 - Style conformance pass: bolded each section's key insight, split a combined sentence into one per line, and named the vague referent.
- 2026-09-02 - Recorded the Junie Local on-device Mac launch.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-10-07 - Added the JetBrains/junie star history chart to the Status section.
- 2026-10-18 - Recorded Junie Local widening past the Mac: NVIDIA RTX Spark support from day one of that platform and Windows support stable on 24 GB RTX cards, with a Qwen3.6-27B or Qwen3.8-3.6-27B-blend model choice, and refreshed the home-page reference annotation and the Pricing section's Local line.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - Junie as the LLM-agnostic outlier in the harness layer
- [agent-skills-that-render](../../../agent-skills-that-render/index.md) - the skills layer Junie shares via ACP
- [Iterating on Agent Skills](../../../iterating-on-agent-skills/index.md) - how these skill formats evolve in practice
- [Crush](../crush/index.md) - the other analysis-grounded terminal agent

## References

- https://junie.jetbrains.com/ - features and BYOK providers, re-fetched 2026-10-18 (the page now leads with the free-to-start Junie CLI and Junie Local framing; the plan prices were last confirmed on the page 2026-10-06)
- https://blog.jetbrains.com/junie/2026/08/junie-local-launch/ - the Junie Local on-device launch, free with no credits
- https://blog.jetbrains.com/junie/2026/10/junie-local-rtx-spark/ - the October 2026 widening: NVIDIA RTX Spark support and stable Windows on 24 GB RTX cards
- https://github.com/JetBrains/junie - install channels, GitHub Action, license terms, 475 stars as of 2026-10-11
- https://www.jetbrains.com/junie/ - the product entry point
- https://blog.jetbrains.com/junie/2025/01/meet-junie-your-coding-agent-by-jetbrains/ - the January 2025 launch and original benchmark claim
- https://www.devclass.com/ai-ml/2025/04/16/jetbrains-goes-live-with-junie-ai-agent-updates-ai-assistant-adds-free-tier/1620745 - independent GA coverage with reviewer sentiment
