---
title: OpenHands
created: 2026-08-27
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, open-source, agent-platforms]
readability: 3
audience_notes: >
  Engineers weighing an open, self-hostable agent platform against subscription coding harnesses.
  Assumes you know what sandboxed execution, MCP, and BYOK mean.
---

OpenHands is the open-source (MIT) AI software development platform from All Hands AI: sandboxed agent conversations with code, shell, and browser access, runnable locally, in their cloud, or in your VPC.
Facts below verified as of 2026-09-02.

**OpenHands is the field's largest open bet on the platform camp of agentic development, and its architecture has just re-centered on a server-client split that demotes the local GUI and CLI to legacy.**

## What it is

The project paper describes an open platform for AI software developers as generalist agents, built around conversations that can edit files, run commands, and drive a browser inside sandboxes.
It began as OpenDevin in March 2024 and was renamed OpenHands mid-development; the repository now lives at the `OpenHands` organization with about 85.9k stars and 11.3k forks under MIT as of 2026-09-02.
Today's component map per the docs is Agent Canvas (the open-source browser client), an Agent Server backend plus Software Agent SDK, OpenHands Cloud, Enterprise, and a Sandbox Server.
**The docs explicitly place the old Local GUI and CLI V0 under Deprecated Projects**, and one unusual flex stands out: Agent Canvas can host Claude Code, Codex, or Gemini CLI as ACP agents instead of its own loop.

## Status

**Active and venture-funded.**
Latest tagged release v1.16.0 shipped August 27, 2026, and the default branch was pushed the day of verification.
All Hands AI raised $18.8M in a Series A led by Madrona on November 18, 2025, alongside a collaboration with AMD on locally-run agents.

## Strengths

- **Breadth**: full computer use (shell, editor, browser) in sandboxed execution rather than repo-file edits only.
- Model-agnostic and locally runnable (LM Studio, Ollama, vLLM, SGLang documented), so it survives lab-side restrictions.
- The operations layer is complete: hooks, skills, plugins, MCP, cron-scheduled and event-triggered automations, CI headless mode.
- MIT client plus self-hosted server and VPC enterprise path gives real deployment sovereignty.

## Cautions

- **Platform churn is live**: the deprecated V0 surfaces mean workflows written against tutorials from 2024-2025 need migration to Canvas and the SDK.
- Community attention thinned after the rename: the OpenDevin launch drew a 198-point thread in August 2024, while the $18.8M raise announcement scored 4 points in November 2025.
- Platform breadth costs coding-specific polish; expect fewer editor-grounding conveniences than in coding-native harnesses.
- History is fragmented across two names, two org moves, and a docs split between V0 and V1, which makes searching for solutions harder than it should be.

## Pricing

Local open source: free.
SaaS Individual tier: free with BYOK or provider models at-cost, capped at ten daily conversations per user, with Jira and Slack integrations.
Enterprise: custom pricing covering SaaS or self-hosted-in-your-VPC, SAML/SSO, unlimited conversations, and priority support.

## Compared to

- [Codex](../codex/index.md): the closed-client rival with bundled subscription usage; OpenHands trades convenience for auditability and self-hosting.
- [goose](../goose/index.md): foundation-governed generalist versus company-governed platform; goose for stewardship, OpenHands for sandbox breadth and cloud automation.
- [Claude Code](../claude-code/index.md): the integrated-platform benchmark; OpenHands is where you land when its cost model or closedness disqualifies it.

## Bottom line

**Recommended for engineers who want Devin-class breadth they can audit, self-host, and point at any model, including local ones.**
Not for someone who wants a zero-migration, opinionated coding workflow today, because the platform is moving its own surface under them.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the four-layer map this note slots into
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - capability rows across all profiled harnesses
- [goose](../goose/index.md) - the other big non-corporate-stewardship story, opposite side of the governance bet
- [Codex](../codex/index.md) - the closed-but-subsidized alternative in the same platform-weight class

## References

- https://github.com/OpenHands/OpenHands - repository scale, license, release cadence as of 2026-09-02
- https://docs.openhands.dev/overview/introduction - component map, Agent Canvas over Agent Server, V0 deprecation
- https://www.openhands.dev/pricing - Free OSS, Individual free tier, Enterprise custom tiers
- https://www.openhands.dev/blog/weve-just-raised-18-8m-to-build-the-open-standard-for-autonomous-software-development - Series A details, November 18, 2025
- https://arxiv.org/abs/2407.16741 - the platform paper grounding the code-shell-browser scope
- https://news.ycombinator.com/item?id=41215593 - the biggest community thread of the OpenDevin era (198 points)
- https://news.ycombinator.com/item?id=45975064 - the raise discussion, marked as the thin-post-rename community signal
