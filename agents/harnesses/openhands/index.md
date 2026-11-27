---
title: OpenHands
created: 2026-08-27
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, coding-agents, harnesses, open-source, agent-platforms]
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
**The docs place the old Local GUI and CLI in their Legacy section, the Local GUI explicitly deprecated**, and one unusual flex stands out: Agent Canvas can drive Claude Code, Codex, Gemini CLI, Pi, or OpenCode as ACP agents instead of its own loop ([ACP agents docs](https://docs.openhands.dev/openhands/usage/agent-canvas/acp-agents)).

## Status

**Active and venture-funded.**
Latest tagged release v1.46.0 shipped November 25, 2026 (listing and unsharing the conversations shared with a team org, a Feedback button and submission flow, and a Git Sync switch that keeps an automation's activation status local, with agent-server 1.63.1, automation 1.35.1, and extensions 0.44.0), after v1.45.0 shipped November 24, 2026 (a factory's worklogs shown newest first and factory deletion, OpenHands Projects in Canvas as an experimental view, project conversations in the sidebar with files and pull requests beside the chat, and sub-agent conversations nested under their parent, plus phone-width and keyboard-accessibility fixes), after v1.44.0 shipped November 23, 2026 (conversation mentions behind the `conversation_mentions` flag, choosing who can see an automation, a readable error when a budget is reached, viewing and editing an automation's key-value store, and a Factories sidebar entry with list and drill-in views), after v1.43.0 shipped November 20, 2026 (automations creatable from the setup wizard, a Features page for experimental user feature flags with Conversation reactions, experimental decision cards rendered in chat, and the agent's message edits shown as an experimental view), after v1.42.0 shipped November 18, 2026 (cloud picking the exact connected git provider for repositories, verify-openhands asserting every run has a non-loopback plain-HTTP origin, native webhook source validation restored in automations, and a clipboard fallback when the Clipboard API is unavailable), after v1.41.0 shipped November 16, 2026 (verify-openhands scenarios beyond the happy path with map controls and browser timezone, ACP choosing reasoning effort from what the agent reports, the Available Hooks dialog naming the workspace and user hooks files, automation dashboards grouped by tag, and UUID generation fixed on plain-HTTP non-loopback origins), after v1.40.0 shipped November 12, 2026 (improved Codex subscription authentication guidance, chat messages kept at tied history page boundaries, delayed echoes no longer deleting newer drafts, and the home model pick activating on self-hosted instances with Agent Profiles off), after v1.39.0 shipped November 11, 2026 (the automations dashboard filtering by owner with a Service accounts option, message hover timestamps moved closer to their messages, Stop hook feedback kept out of the chat, and the Paper theme printed as aged newsprint with readable warnings), after v1.38.0 shipped November 10, 2026 (conversation budgets displayed with semantic meter fills, executable plugin configuration editable from automation help, prompt and plugin presets runnable from an agent profile, a Paper theme for Agent Canvas, a resolved banner for project conversations, and an automation-aware install mode), after v1.37.0 shipped November 6, 2026 (each automation explained with a Mermaid diagram, resumed sessions placed after UTC conversation history, generated titles kept visible during startup handoff, the home page loading at the base path, and chat history scans during live updates made cheaper), alongside a `pr19394-evidence` tag published the same day, after v1.36.0 shipped November 5, 2026 (automations opening templates without the missing-integration notice, listing a script automation's files collapsed, suggesting default templates and promoting ones users set up, and setup assistance), after v1.35.0 shipped November 3, 2026 (automations storing picked Bitbucket Data Center repositories as clone URLs, each event source listing its own event types, the home view remembering and clearing the cloud repository selection, and workspace and repo metadata persisted server-side), after v1.34.0 shipped October 27, 2026 (a DigitalOcean stand-in so Managed Agents can run verification, a per-conversation Docker runtime with a Settings → Runtime page, and automation tag filtering and editing), after v1.33.0 (October 23) launched verify-openhands `--mars-web` and `--lock-to-cloud` with a DigitalOcean web build that stays signed in across restarts, closing a four-day run that took the train from v1.28.1 through v1.29.0 (October 20, full organization names in the backend selector and launchers reading public skills from the bundled extensions package), v1.30.0 and v1.31.0 (October 22, automations surfacing connection state and hiding the GitHub token field once connected, plus an MCP install dialog that picks between library options), and v1.32.0 (October 23, pinned automations stored in agent-server settings and an automation picker listing every cloneable provider's repositories), on top of v1.28.0's executable known-bugs entries and a repeatable fix proof to verify-openhands, an in-conversation modal letting the agent request a secret, a close control for the getting-started checklist, and a Bahasa Indonesia locale, which followed v1.27.1 (October 12) fixing a Docker web-bridge module copy and making warning feedback theme-aware and v1.27.0 driving the verify-openhands mock-LLM end-to-end behaviors on DeepSeek and adding `browser record` video capture, after v1.26.0 (October 8) added a verify-openhands skill with a control-openhands CLI and a daily pass mode, a suspended-workspace explanation with a switch offer, a narrowed needs-review status in automations, and a large accessibility and tablet batch; the default branch was pushed 2026-11-27 (GitHub API, as of 2026-11-27).
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

Open Source: free and self-hosted under MIT, with one shared identity, a bring-your-own LLM key, third-party agents such as Claude Code and Codex, automations, MCP and secrets, and community support.
Teams: $500/month with 10 users included (+$50/month per seat, 30-day trial) for self-hosted multi-user identity and RBAC, SAML/SSO, budgeting and usage controls, built-in OAuth integrations, best-effort email support, and a 5,000-sessions-a-month cap.
Enterprise: custom pricing for unlimited seats and organizations, an enterprise agreement, SLA-based response times, and a customer success manager, with uncapped usage.
**The SaaS Individual tier this note recorded from creation (free, BYOK or at-cost provider models, ten daily conversations) is gone from the page, which now lists self-hosted deployment on every tier**, while the docs still describe OpenHands Cloud as the managed commercial service (as of 2026-11-24).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-08-27 | Open Source, Individual, Enterprise | Baseline at note creation: local open source free; SaaS Individual free with BYOK or at-cost provider models, capped at ten daily conversations per user, with Jira and Slack integrations; Enterprise custom (SaaS or self-hosted in your VPC, SAML/SSO, unlimited conversations, priority support). | [Wayback snapshot of openhands.dev/pricing, 2026-10-19](http://web.archive.org/web/20261019165201/https://www.openhands.dev/pricing) |
| 2026-11-24 | Open Source, Teams, Enterprise | The SaaS Individual tier is gone and a self-hosted Teams tier sits at $500/month with 10 users included (+$50/month per seat, 30-day trial, 5,000 sessions a month cap) between the free Open Source tier and custom Enterprise, whose usage stays uncapped; Wayback snapshots date the restructure between October 19 (Individual still listed) and October 24 (Teams at $499/month for up to 10 users), with $500/month by November 2. | [openhands.dev/pricing](https://www.openhands.dev/pricing), [Wayback 2026-10-24](http://web.archive.org/web/20261024174630/https://www.openhands.dev/pricing), [Wayback 2026-11-02](http://web.archive.org/web/20261102034247/https://www.openhands.dev/pricing) |

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
- 2026-11-04 - Recorded the v1.35.0 release (published November 3): automations storing picked Bitbucket Data Center repositories as clone URLs, per-event-source event-type listings, the cloud repository selection remembered and clearable, and workspace and repo metadata persisted server-side; refreshed the push date to 2026-11-03.
- 2026-11-06 - Recorded the v1.36.0 release (published November 5): automations opening templates without the missing-integration notice, collapsed script-automation file listings, default-template suggestions, and setup assistance, with the `pr19394-evidence` tag published alongside; refreshed the push date to 2026-11-06.
- 2026-11-07 - Recorded the v1.37.0 release (published November 6): automations explained with a Mermaid diagram, resumed sessions ordered after UTC conversation history, generated titles kept visible during startup handoff, the home page loading at the base path, and cheaper chat history scans during live updates; refreshed the push date to 2026-11-07.
- 2026-11-13 - Recorded the v1.39.0 (published November 11: automation dashboard owner filtering with a Service accounts option, Stop hook feedback kept out of chat, and the Paper theme printed as aged newsprint) and v1.40.0 (published November 12: improved Codex subscription authentication guidance and chat draft and history-page fixes) releases; refreshed the push date to 2026-11-13.
- 2026-11-17 - Recorded the v1.41.0 release (published November 16): verify-openhands scenarios beyond the happy path with map controls and browser timezone, ACP reasoning effort read from what the agent reports, hooks files named in the Available Hooks dialog, automation dashboards grouped by tag, and the plain-HTTP UUID and MCP OAuth callback-base fixes.
- 2026-11-19 - Recorded the v1.42.0 release (published November 18): exact connected git-provider picking in cloud, a verify-openhands non-loopback plain-HTTP origin assertion per run, restored automations webhook source validation, and a clipboard fallback.
- 2026-11-21 - Recorded the v1.43.0 release (published November 20): automations creatable from the setup wizard, a Features page for experimental user feature flags with Conversation reactions, experimental decision cards rendered in chat, and the agent's message edits shown as an experimental view, against the GitHub releases API.
- 2026-11-24 - Rotation re-verification, re-fetching every cited reference (all live), found the pricing page restructured sometime between October 19 and 24 per Wayback snapshots: the SaaS Individual free tier (ten daily conversations) is gone and a self-hosted Teams tier sits at $500/month with 10 users included (+$50/month per seat, 30-day trial, 5,000 sessions a month cap) between the free Open Source tier and custom Enterprise; rewrote the Pricing section and added the Price history table with its seeded baseline row.
- 2026-11-24 - Recorded the v1.44.0 release (published November 23): conversation mentions behind the `conversation_mentions` flag, choosing who can see an automation, a readable error when a budget is reached, viewing and editing an automation's key-value store, and a Factories sidebar entry with list and drill-in views, against the GitHub releases API.
- 2026-11-24 - Extended the ACP claim to the docs' current list (Claude Code, Codex, Gemini CLI, Pi, or OpenCode) and cited the ACP agents page that grounds it.
- 2026-11-25 - Rotation re-verification, re-fetching every cited reference (all live): recorded the v1.45.0 release (published November 24: a factory's worklogs shown newest first and factory deletion, OpenHands Projects in Canvas as an experimental view, project conversations in the sidebar with files and pull requests beside the chat, sub-agent conversations nested under their parent, and phone-width and keyboard-accessibility fixes) and refreshed the push date to 2026-11-25, against the GitHub releases API.
- 2026-11-27 - Recorded the v1.46.0 release (published November 25: listing and unsharing conversations shared with a team org, a Feedback button and submission flow, and a Git Sync switch keeping automation activation status local); refreshed the push date to 2026-11-27, against the GitHub releases API.

## See also

- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the four-layer map this note slots into
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - capability rows across all profiled harnesses
- [goose](../goose/index.md) - the other big non-corporate-stewardship story, opposite side of the governance bet
- [Codex](../codex/index.md) - the closed-but-subsidized alternative in the same platform-weight class

## References

- https://github.com/OpenHands/OpenHands - repository scale, license, release cadence as of 2026-10-13
- https://docs.openhands.dev/overview/introduction - component map, Agent Canvas over Agent Server, V0 deprecation
- https://www.openhands.dev/pricing - the Open Source, Teams ($500/month, 10 users included), and Enterprise tiers, the Teams session cap, and the Wayback-dated removal of the SaaS Individual tier, as of 2026-11-24
- https://docs.openhands.dev/openhands/usage/agent-canvas/acp-agents - Agent Canvas driving Claude Code, Codex, Gemini CLI, Pi, or OpenCode through the Agent Client Protocol
- https://www.openhands.dev/blog/weve-just-raised-18-8m-to-build-the-open-standard-for-autonomous-software-development - Series A details, November 18, 2025
- https://arxiv.org/abs/2407.16741 - the platform paper grounding the code-shell-browser scope
- https://news.ycombinator.com/item?id=41215593 - the biggest community thread of the OpenDevin era (198 points)
- https://news.ycombinator.com/item?id=45975064 - the raise discussion, marked as the thin-post-rename community signal
