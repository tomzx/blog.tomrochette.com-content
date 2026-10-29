---
title: OpenHands
created: 2026-08-27
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, coding-agents, harnesses, open-source, agent-platforms]
readability: 3
audience_notes: >
  Engineers weighing an open, self-hostable agent platform against subscription coding harnesses.
  Assumes you know what sandboxed execution, MCP, and BYOK mean.
---

OpenHands is the open-source (MIT) AI software development platform from All Hands AI: sandboxed agent conversations with code, shell, and browser access, runnable locally, in their cloud, or in your VPC.

**OpenHands is the field's largest open bet on the platform camp of agentic development, and its architecture has just re-centered on a server-client split that demotes the local GUI and CLI to legacy.**

## What it is

The project paper describes an open platform for AI software developers as generalist agents, built around conversations that can edit files, run commands, and drive a browser inside sandboxes.
The project began as OpenDevin in March 2024 and was renamed OpenHands mid-development; the repository now lives at the `OpenHands` organization with about 90.7k stars and 12.0k forks under MIT as of 2026-10-12.
Today's component map per the docs is Agent Canvas (the open-source browser client), an Agent Server backend plus Software Agent SDK, OpenHands Cloud, Enterprise, and a Sandbox Server.
**The docs place the old Local GUI and CLI in their Legacy section, the Local GUI explicitly deprecated**, and one unusual flex stands out: Agent Canvas can host Claude Code, Codex, or Gemini CLI as ACP agents instead of its own loop.

## Status

**Active and venture-funded.**
Latest tagged release v1.34.0 shipped October 27, 2026 (a DigitalOcean stand-in so Managed Agents can run verification, a per-conversation Docker runtime with a Settings → Runtime page, and automation tag filtering and editing), after v1.33.0 (October 23) launched verify-openhands `--mars-web` and `--lock-to-cloud` with a DigitalOcean web build that stays signed in across restarts, closing a four-day run that took the train from v1.28.1 through v1.29.0 (October 20, full organization names in the backend selector and launchers reading public skills from the bundled extensions package), v1.30.0 and v1.31.0 (October 22, automations surfacing connection state and hiding the GitHub token field once connected, plus an MCP install dialog that picks between library options), and v1.32.0 (October 23, pinned automations stored in agent-server settings and an automation picker listing every cloneable provider's repositories), on top of v1.28.0's executable known-bugs entries and a repeatable fix proof to verify-openhands, an in-conversation modal letting the agent request a secret, a close control for the getting-started checklist, and a Bahasa Indonesia locale, which followed v1.27.1 (October 12) fixing a Docker web-bridge module copy and making warning feedback theme-aware and v1.27.0 driving the verify-openhands mock-LLM end-to-end behaviors on DeepSeek and adding `browser record` video capture, after v1.26.0 (October 8) added a verify-openhands skill with a control-openhands CLI and a daily pass mode, a suspended-workspace explanation with a switch offer, a narrowed needs-review status in automations, and a large accessibility and tablet batch; the default branch was pushed 2026-10-28 (GitHub API, as of 2026-10-28).
All Hands AI raised $18.8M in a Series A led by Madrona on November 18, 2025, alongside a collaboration with AMD on locally-run agents.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=OpenHands/OpenHands&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=OpenHands/OpenHands&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=OpenHands/OpenHands&type=date&legend=top-left" />
</picture>

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

## Changes

- 2026-08-27 - Created as a new-entrant harness note, recording the OpenDevin rename, the $18.8M Series A, and the Agent Canvas architecture.
- 2026-09-16 - Refreshed repository scale (about 88.1k stars, 11.6k forks) and the pushed date; v1.18.0 still the latest release.
- 2026-09-22 - Recorded the v1.22.0 release (September 22) and refreshed repository scale.
- 2026-09-24 - Recorded the v1.23.0 release (September 23) and refreshed repository scale.
- 2026-09-26 - Recorded the v1.24.0 release (September 25) and refreshed repository scale.
- 2026-10-06 - Recorded the v1.25.0 release (October 6), which added Model Router settings with a run-at-conversation-start toggle, bulk LLM profile creation, per-profile personas, Canvas App updates, automation templates with native git integrations, and optional voice dictation.
- 2026-10-07 - Added the OpenHands/OpenHands star history chart to the Status section.
- 2026-10-09 - Recorded v1.26.0 (October 8), which added the verify-openhands skill with a control-openhands CLI and a daily pass mode, a suspended-workspace explanation, a narrowed needs-review automation status, and an accessibility batch.
- 2026-10-13 - Recorded the v1.27.0 and v1.27.1 releases (both October 12), which drove the verify-openhands mock-LLM end-to-end behaviors on DeepSeek, added `browser record` video capture, and fixed a Docker web-bridge copy with theme-aware warning feedback.
- 2026-10-20 - Recorded the v1.28.0 and v1.28.1 releases (October 19): executable known-bugs entries with a repeatable fix proof in verify-openhands, an in-conversation secret-request modal, a Bahasa Indonesia locale, and an agent-server bump.
- 2026-10-24 - Recorded the train moving through v1.33.0 (October 23): verify-openhands --mars-web and --lock-to-cloud launches, pinned automations in agent-server settings, an MCP install dialog with library options, GitHub token fields hidden when connected, and skills read from the bundled extensions package.
- 2026-10-28 - Recorded the train reaching v1.34.0 (October 27): a DigitalOcean stand-in for Managed Agents verification, a per-conversation Docker runtime with a Settings → Runtime page, and automation tag filtering and editing, with the push date refreshed.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the four-layer map this note slots into
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - capability rows across all profiled harnesses
- [goose](../goose/index.md) - the other big non-corporate-stewardship story, opposite side of the governance bet
- [Codex](../codex/index.md) - the closed-but-subsidized alternative in the same platform-weight class

## References

- https://github.com/OpenHands/OpenHands - repository scale, license, release cadence as of 2026-10-13
- https://docs.openhands.dev/overview/introduction - component map, Agent Canvas over Agent Server, V0 deprecation
- https://www.openhands.dev/pricing - Free OSS, Individual free tier, Enterprise custom tiers
- https://www.openhands.dev/blog/weve-just-raised-18-8m-to-build-the-open-standard-for-autonomous-software-development - Series A details, November 18, 2025
- https://arxiv.org/abs/2407.16741 - the platform paper grounding the code-shell-browser scope
- https://news.ycombinator.com/item?id=41215593 - the biggest community thread of the OpenDevin era (198 points)
- https://news.ycombinator.com/item?id=45975064 - the raise discussion, marked as the thin-post-rename community signal
