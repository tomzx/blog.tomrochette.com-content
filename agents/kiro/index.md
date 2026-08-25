---
title: Kiro
created: 2026-08-24
updated: 2026-08-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, surfaces, ai-editors, aws]
readability: 3
audience_notes: >
  Engineers in the AWS orbit evaluating the spec-driven agentic IDE.
  Assumes you know what a spec is and what subscription credits meter.
---

Kiro is AWS's agentic IDE: spec-driven by default, with a CLI, web, mobile, and a multi-agent Crew, metered in credits from a 50-credit free tier to a $200/month Power plan.
Facts below verified as of 2026-08-25.

**Kiro is the only major IDE vendor that treats specs, requirements, and design documents as the primary artifact rather than chat, and that bet either matches how your team already works or will feel like bureaucracy.**

## What it is

**Two modes organize everything: vibe mode for direct iteration and spec mode, where Kiro generates requirements and design docs you edit before implementation proceeds.**
Agent hooks trigger on file changes or schedules, and a subscription covers the IDE, the CLI, Kiro on the web, mobile, Crew (parallel agents), and ACP-compatible IDEs, an unusually wide surface list.
The default model router is Auto, mixing frontier and specialist models, with explicit choices spanning GPT-5.6, Claude Opus 5 and Sonnet 5, DeepSeek, MiniMax, GLM-5, and Qwen3 Coder Next.

## Status

**Active and enterprise-ready.**
The vendor changelog shows weekly releases, latest 2.19.1 on August 21, 2026; pricing, GovCloud availability, and enterprise billing through AWS are all shipped.
The public issue tracker (kirodotdev/Kiro, about 4.2k stars as of 2026-08-25) has been quiet since June 22, 2026, so release evidence now lives on kiro.dev, not the repository.
Its spec workflow has been influential enough that community projects port it to other harnesses.

## Strengths

- **Specs as first-class artifacts** turn agent work into reviewable documents, the same pull-based review pattern this blog argues for elsewhere.
- One subscription spans IDE, CLI, web, mobile, Crew, and ACP-compatible editors.
- Free tier includes Claude Sonnet 4.5 and open-weight models, a genuine trial rather than a teaser.
- Enterprise identity, billing, and GovCloud come from AWS machinery that orgs already run.

## Cautions

- **Credits are the trap**: 1,000 credits on Pro sounds large until spec tasks, refinements, and agent hooks each meter fractions of a credit at model-specific multipliers, and add-ons cost $0.04 per credit.
- Terms explicitly forbid routing subscription usage through third-party automation harnesses, so your Kiro credits stay in Kiro surfaces.
- An August 2025 writeup documented arbitrary code execution via indirect prompt injection in the IDE.
- The client is closed; the GitHub repository is feedback and docs, not source.

## Pricing

Free: $0 with 50 credits, open-weight models plus Claude Sonnet 4.5.
Pro $20 (1,000 credits), Pro+ $40 (2,000), Pro Max $100 (5,000), Power $200 (10,000), add-on credits at $0.04 each, enterprise via AWS with SSO and overage controls, GovCloud priced about 20% higher, as of 2026-08-25.

## Compared to

- [Cursor](../cursor/index.md): chat-first versus spec-first; pick Kiro when requirements artifacts matter to your team.
- [JetBrains IDEs](../jetbrains/index.md): deep analysis versus spec workflow; both sell credits.
- [VS Code + Copilot](../vscode-copilot/index.md): the neutral host; Kiro is an opinionated environment with AWS gravity.

## Bottom line

**Recommended for spec-disciplined teams, especially those already buying through AWS.**
Not for credit-averse solo engineers or anyone who wants an open client.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the surface layer this note belongs to
- [Send Implementation, Not Issue](../../send-implementation-not-issue/index.md) - why generated specs plus implementation beats bare tickets
- [OpenCode](../opencode/index.md) - the open harness alternative, also ACP-reachable

## References

- https://kiro.dev/ - product surfaces, modes, hooks
- https://kiro.dev/pricing/ - tiers, credits, model multipliers, enterprise and GovCloud terms, as of 2026-08-25
- https://kiro.dev/changelog/ - the weekly release cadence, 2.19.1 on August 21, 2026, as of 2026-08-25
- https://github.com/kirodotdev/Kiro - issue tracker, quiet since June 22, 2026, about 4.2k stars as of 2026-08-25
- https://news.ycombinator.com/item?id=45044061 - the prompt-injection code execution writeup
- https://news.ycombinator.com/item?id=44654560 - the spec-workflow port that shows Kiro's influence
