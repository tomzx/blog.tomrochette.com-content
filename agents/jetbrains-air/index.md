---
title: JetBrains Air
created: 2026-09-12
updated: 2026-09-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, parallel-agents, jetbrains, agentic-development-environment]
readability: 3
audience_notes: >
  Engineers with a JetBrains AI subscription deciding whether to run parallel agent tasks in Air instead of a third-party orchestrator.
  Assumes you know what a git worktree and a container-isolated task are.
---

JetBrains Air is a standalone desktop (and organization-web) application from JetBrains that runs Codex, Claude Agent, Gemini CLI, and Junie as independent parallel task loops, each isolated in a git worktree, Docker container, or cloud environment.
Facts below verified as of 2026-09-12.

**Air is JetBrains conceding that the agentic workflow layer is a product category distinct from the IDE: it is a task orchestrator that belongs next to Conductor and Superset rather than in Surfaces, because the IDE stays a separate application by JetBrains' own design, and the orchestrator itself is sold as a subscription feature rather than a product.**

## What it is

A standalone desktop app for macOS, Windows, and Linux, plus a web version at air.jetbrains.cloud that is currently organization-only, tagged "Multitask with agents, stay in control" and called an Agentic Development Environment.
Each task picks one of four run environments: local workspace (no isolation), git worktree, Docker container, or JetBrains-managed cloud, with changes landing on an `air/<task>` branch for review and apply.
Workspaces scope sessions, git state, and tools to a single project, and review is language-aware, with IntelliJ-powered Java and Kotlin code intelligence since July 2026.
Built-in agents are Codex, Claude Agent, Gemini CLI, and Junie, and any ACP-compatible agent can be added (GitHub Copilot, OpenCode, and 17 more at introduction, including local models via Ollama).
**The division of labor is JetBrains' own FAQ line: "Air handles the agent-powered development; your IDE handles the rest", with an Open In IDE action bridging the two.**

## Status

Active, public preview.
The latest release is 262.579.32 (2026-08-19) as of 2026-09-12, on a roughly monthly cadence since January 2026.
Milestones: Codex support January 19, Gemini CLI and Junie with the Agent Review chain March 5, public preview March 9, Linux June 2, Windows June 29, ACP agents and Java/Kotlin intelligence July 15.
Cloud execution, called tech preview at launch, has since shipped as documented cloud tasks, automations, and the org web version, governed through JetBrains Central Console.
**The community footprint is thin: Algolia lists exactly three "JetBrains Air" stories (26 points with 1 comment, 6 points, and 3 points), the June submission links to a Google-ads-tagged air.dev URL, and the December 2025 story about JetBrains abandoning Fleet for Air drew 3 points and 1 comment, a signal in a market where peers launch to 100+ point threads.**

## Strengths

- The isolation menu is the deepest in the category: worktree, Docker, or cloud per task, with `.air/worktree.json` and `.air/docker.json` for setup, teardown, and environment.
- One JetBrains AI Pro or Ultimate subscription unlocks all four agent families, the only bundled deal in this category.
- Agent Review, one agent reviewing another's diff, is built in and configurable per review.
- Organization governance is real: admins set agent, cloud, and credit policy in JetBrains Central Console, which no peer at this table offers.

## Cautions

- Preview churn with sharp edges: Claude Agent in Docker refuses subscription credentials and requires Anthropic API billing, BYOK works only for local tasks, and Gemini CLI is temporarily unavailable for cloud tasks (docs as of 2026-09-10).
- Cloud tasks always spend JetBrains AI credits, the metering the [Junie](../junie/index.md) note already found thin for subscription-only users.
- The web version and org features require a JetBrains Central Console organization, and JetBrains AI Free and AI Enterprise are not supported at all.
- Proprietary client, vendor-run cloud, and a community footprint that is a fraction of any peer's, so there is no exit path and little independent signal on quality.

## Pricing

No standalone price: sign in with a JetBrains AI Pro or Ultimate subscription and all supported agents are included at no additional cost, as of 2026-09-12.
AI Free and AI Enterprise are explicitly not supported, and trials cannot be activated from Air.
BYOK keys (Anthropic, OpenAI, Google) take priority when configured, and you can also bring your own Codex (ChatGPT Plus, Pro, or Team) and Gemini subscriptions.
The exception that defines the model: cloud tasks always run agents on JetBrains AI credits, whatever you connected locally.

## Compared to

- [Conductor](../conductor/index.md): the polished closed-source Mac orchestrator with Vercel cloud sandboxes; choose Conductor for four-harness breadth and founder velocity, Air for subscription economics and IntelliJ-grade code intelligence.
- [Superset](../superset/index.md): source-available, agent-agnostic, free local core; choose Superset to avoid vendor metering entirely, Air when the AI Pro seat is already paid.
- [Happy Coder](../happy-coder/index.md): the pure thin client for phone access to sessions you already run; Air is the opposite bet, a first-party stack from isolation to org policy.

## Bottom line

**Recommended for JetBrains-first engineers and teams already paying for AI Pro or Ultimate who want parallel agent tasks with real isolation choices and organization governance.**
Not for open-client requirements, AI Free or AI Enterprise subscribers, or anyone unwilling to route cloud work through JetBrains credits.
My disagreeable claim: the isolation-plus-oversight bundle Air sells is now table stakes that Conductor, Superset, and Emdash all ship on your own subscriptions, so Air's real product is the subscription tie-in rather than the orchestrator, and I expect the orchestrator to be judged against that bar.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [JetBrains IDEs](../jetbrains/index.md) - the IDE-family sibling in Surfaces, deliberately a different category from Air
- [Junie](../junie/index.md) - the bundled JetBrains agent Air drives alongside its rivals
- [Six Months with OpenChamber](../../six-months-with-openchamber/index.md) - scheduled sessions, the non-interactive complement to Air's parallel dispatch

## References

- https://air.dev/ - product claims, supported agents, isolation options, FAQ, and pricing terms, as of 2026-09-12
- https://air.dev/changelog - version 262.579.32 (2026-08-19), platform dates, ACP support, and feature history
- https://www.jetbrains.com/help/air/execution-environments.html - the four run environments and the isolation model, as of 2026-08-18
- https://www.jetbrains.com/help/air/supported-agents.html - the agent and provider-account matrix, as of 2026-08-25
- https://www.jetbrains.com/help/air/cloud-tasks.html - cloud tasks, the org web version, lifecycle, and credits, as of 2026-08-20
- https://www.jetbrains.com/help/air/set-up.html - desktop platforms, org setup, and Central Console governance, as of 2026-09-10
- https://blog.jetbrains.com/air/2026/03/air-launches-as-public-preview-a-new-wave-of-dev-tooling-built-on-26-years-of-experience/ - the March 2026 public-preview announcement by Nik Tkachev
- https://hn.algolia.com/api/v1/search?query=%22JetBrains+Air%22&tags=story - the three HN stories and their thin footprint, queried 2026-09-12
- https://hn.algolia.com/api/v1/items/46350939 - the Fleet-abandonment story (2025-12-22, 3 points, 1 comment)
