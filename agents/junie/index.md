---
title: Junie
created: 2026-08-22
updated: 2026-09-03
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, coding-agents, harnesses, jetbrains, byok]
readability: 3
audience_notes: >
  Engineers living in JetBrains IDEs who want an agent grounded in IDE-grade analysis.
  Assumes you know what a language server or IDE inspection is and what BYOK means.

---

Junie is JetBrains' coding agent: an LLM-agnostic CLI that also ships in JetBrains IDEs and CI, authenticating either to JetBrains or to your own model keys.
Facts below verified as of 2026-09-04.

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
The GitHub repository (installer and release channels: release, EAP, nightly, experimental) shows about 422 stars as of 2026-09-03.
In August 2026 JetBrains launched Junie Local, a free on-device build for M5 Macs that runs a bundled, tuned model entirely locally with no registration, subscription, or credits ([launch post](https://blog.jetbrains.com/junie/2026/08/junie-local-launch/)).
The client is proprietary under JetBrains AI terms; the repo is distribution, not source.

## Strengths

- **The IntelliJ analysis engine grounds edits** the way Crush uses LSPs, but from a decade of IDE inspections.
- Plan artifacts live in your repository as reviewable files, the right place for them.
- BYOK at provider rates with zero markup, including local models, from a major vendor.
- ACP means the same skills run in your IDE and your terminal.

## Cautions

- **Community footprint is small**: launch-era HN threads drew dozens of points and near-zero discussion, which is itself a signal about mindshare versus Claude Code or OpenCode.
- Cloud usage is metered in AI credits (10 per 30 days on AI Pro, 35 on AI Ultimate), so subscription-only users will exhaust quota quickly; BYOK is effectively required for cloud work, though the on-device Junie Local (August 2026) now gives Mac users a free local path (an M5 Mac with 64 GB of RAM, per JetBrains).
- Early IDE reviewers reported crashes, restarts, and fast quota burn.
- Its benchmark claims (SWE-Rebench top performer, per the site) are the vendor's own.

## Pricing

Free to start (5 AI credits, no card).
JetBrains AI Pro $8.33 per user/month (annual) and AI Ultimate $25 per user/month include the credit allowances above.
**BYOK bypasses metering at provider rates.**
Junie Local (August 2026) is free: it runs inside Junie on an M5 Mac with the bundled model downloaded locally, no account or credits at all.

## Compared to

- [Claude Code](../claude-code/index.md) and [Codex](../codex/index.md): subscription-first, single-vendor model access; Junie is the model-agnostic counter.
- [Crush](../crush/index.md): terminal-only LSP grounding; Junie adds the full IDE inspection stack.
- [OpenCode](../opencode/index.md): open client versus JetBrains' proprietary one, similar BYOK economics.

## Bottom line

**Recommended for JetBrains-first teams who want one agent across IDE, terminal, and CI on their own keys.**
Not for anyone who needs an open client or a large community ecosystem today.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - Junie as the LLM-agnostic outlier in the harness layer
- [agent-skills-that-render](../../agent-skills-that-render/index.md) - the skills layer Junie shares via ACP
- [Iterating on Agent Skills](../../iterating-on-agent-skills/index.md) - how these skill formats evolve in practice
- [Crush](../crush/index.md) - the other analysis-grounded terminal agent

## References

- https://junie.jetbrains.com/ - features, BYOK providers, plans, pricing, as of 2026-09-03
- https://blog.jetbrains.com/junie/2026/08/junie-local-launch/ - the Junie Local on-device launch, free with no credits
- https://github.com/JetBrains/junie - install channels, GitHub Action, license terms
- https://www.jetbrains.com/junie/ - the product entry point
- https://blog.jetbrains.com/junie/2025/01/meet-junie-your-coding-agent-by-jetbrains/ - the January 2025 launch and original benchmark claim
- https://devclass.com/2025/04/16/jetbrains-goes-live-with-junie-ai-agent-updates-ai-assistant-adds-free-tier/ - independent GA coverage with reviewer sentiment
