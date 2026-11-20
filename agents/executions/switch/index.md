---
title: Switch
created: 2026-11-19
updated: 2026-11-20
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, executions, chat-bridge, self-hosted]
readability: 3
audience_notes: >
  Engineers deciding whether AI teammates should live in the chat app their team already uses, and who can install a desktop Console or run a small server for them.
  Assumes you know what an agent harness, MCP, and source-available licensing are.
---

Switch is a SandboxAQ-backed open-source platform that turns channels in Slack, Teams, Discord, Telegram, and Mattermost into shared rooms where your team and any agent harness work side by side, self-hosted through a desktop Console or your own server.

**It is the chat-bridge member with the widest trigger surface, five chat platforms beside Centaur's Slack and Airut's email-and-Slack, and the loosest agent lock-in, any harness that speaks the protocol: Claude Code, Codex, Antigravity, Cursor, OpenCode, or one you built on LangChain or Google ADK.**

## What it is

A room is a channel your team already uses, and the agents you connect join it as named teammates with an owner, instructions, and connectors (Google Workspace, Atlassian, GitHub, Datadog, Airtable), seeing only the rooms they belong to.
You install Switch Console, the desktop app, pick a provider per agent under your own account, and let switch-buddy, the built-in assistant, create your first agents and rooms; for a team you run the server on your own hardware, and connecting Microsoft Teams needs a Microsoft 365 admin plus a server reachable over the internet.
The repo ships no agents and no models, and its docs are themselves served over MCP so an agent can walk you through the setup.
It is built by SandboxAQ (the license copyright reads SB Technology, Inc. dba SandboxAQ), licensed Apache-2.0 as limited by the Commons Clause, and it sits beside two commercial siblings, Switch Trust (agent scanning and guardrails) and Switch ROI (cost and value reporting), with a hosted Switch Cloud marked coming soon.

## Status

**Active, institutionally backed, and the largest chat-bridge in this category by stars, with an independent footprint of one thread.**
4,587 stars, 364 forks, and 718 open issues and pull requests as of 2026-11-20 (GitHub API), repository created 2026-07-16 and pushed 2026-11-20.
The release train is dense for a project this age: switch-core 0.32.1 and Switch Console 0.41.1 (both published 2026-11-18) top the stable line, with a canary cut (Console 0.42.0-canary.1, 2026-11-18) and dev builds of main publishing daily.
The README carries a #1 Product of the Day Product Hunt badge, and the vendor's case study names Mount Sinai West's physician-led MSW Lab as a design partner, in alpha and built around the Trust product line rather than Rooms.
The community footprint on Hacker News is one self-submitted thread (2026-08-27, 1 point, zero comments) linking the repository, so the stars carry no visible independent discussion anywhere.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=sandbox-quantum/switch&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=sandbox-quantum/switch&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=sandbox-quantum/switch&type=date&legend=top-left" />
</picture>

## Strengths

- **The trigger surface is the whole team's chat app, on five platforms, and the room is shared state**: people and agents work from the same conversation, decisions, and documents, with no new tool to learn and no bot-per-vendor sprawl.
- Any harness that speaks the protocol can join, so a team's Claude Code, Codex, Cursor, and homegrown LangChain agents share one room surface, and switching agents or models does not strand the context.
- The governance model is built into the repo: every agent has an owner who controls who can use it, an agent sees only the rooms it belongs to, and workspace admins gate connectors and access.
- The onboarding floor is a desktop app: Console manages the server, switch-buddy does the setup, and the docs' quickstart promises a first run with no coding and no server knowledge.

## Cautions

- **The community footprint is one 1-point self-submitted Hacker News thread with zero comments as of 2026-11-19**: the stars are the only independent signal, every adoption claim is the vendor's own, and the flagship case study is a design partner in alpha on the Trust product, not Rooms.
- The license is Apache-2.0 limited by the Commons Clause, extended in the repo's own license text to derivatives, so self-hosting and internal use are free but selling hosting or consulting built on it is not; it is not plain open-source, whatever the site's "Free & Open Source" label says.
- Switch ships no sandbox of its own: the containment layer is the separate Switch Trust product, so the repo's protection story is permissions and approvals, not the containers Airut runs or the network policy Centaur enforces.
- Console telemetry is opt-out (on by default, disclosed on first run, no free text or code in the payload), the server's is off by default, and every Switch Cloud badge reads coming soon, so the hosted tier the pitch leans on does not exist yet.
- The docs moved from docs.flintai.dev to docs.switchagents.ai, so coverage under the earlier flintai domain is this same product's history, one project not two, and the docs name the Trust repository family as the development line rather than the released product.

## Pricing

No public price list as of 2026-11-19.
The Rooms stack is free to self-host under the Commons-Clause-limited license, and your costs are your hardware, your agent providers under your own plans, and the chat platforms you connect.
Switch Trust and Switch ROI are free-to-start SaaS signups (no card) with a book-a-demo path and unpublished paid tiers, and Switch Cloud is marked coming soon.

## Compared to

- [Centaur](../centaur/index.md): the same chat-to-agent thesis at team scale, one Slack thread to one Kubernetes sandbox with credentials injected at a per-sandbox proxy; Switch runs agents on your machines under your accounts, spans five chat platforms, and asks for a desktop app instead of a cluster.
- [Airut](../airut/index.md): the single-operator gateway that starts sandboxed Claude Code tasks from email or Slack and continues sessions by reply; Switch is multi-platform and harness-agnostic but brings no container or egress allowlist of its own.
- [n8n](../n8n/index.md): the general canvas where chat and webhook triggers drive workflows you assemble from 1,500+ integrations; Switch is purpose-built for people-plus-agents rooms and carries no integration canvas.

## Bottom line

**Recommended for a team that wants AI teammates in the Slack or Teams it already runs, wants more than one vendor's harness in those rooms, and will accept a young, vendor-led project whose guardrails are a separate product.**
Not for anyone needing proven independent adoption, a shipped hosted tier, or an unambiguously open-source license.
My disagreeable claim: Switch is Centaur's mass-market mirror image, the same chat-to-agent thesis with a desktop app instead of Kubernetes and five platforms instead of one, and its 4,587 stars against Centaur's 1,422 measure a launch, not a body of evidence, because both projects' independent records reduce to self-submitted, zero-comment threads.

## Changes

- 2026-11-19 - Created from the 2026-11-19 cross-category scan admission, routed to executions on the centaur/airut chat-bridge line.
- 2026-11-20 - Refreshed the repository counters after the 2026-11-20 push (358 to 364 forks, 719 to 718 open issues and pull requests); the release record re-confirmed (the stable line still switch-core 0.32.1 and Switch Console 0.41.1 of 2026-11-18, dev builds of main publishing daily).

## See also

- [Centaur](../centaur/index.md) - the team-scale sibling with the same chat trigger and the sandbox architecture Switch leaves to its Trust product
- [Airut](../airut/index.md) - the single-operator chat-bridge that ships the containment Switch does not
- [n8n](../n8n/index.md) - the general canvas alternative for chat and webhook triggers
- [Claude Code](../../harnesses/claude-code/index.md) - the harness the README leads with when it describes rooms

## References

- https://api.github.com/repos/sandbox-quantum/switch - counters (4,587 stars as of 2026-11-19, the creation baseline; 364 forks, 718 open issues and pull requests, created 2026-07-16, pushed 2026-11-20; re-verified 2026-11-20)
- https://raw.githubusercontent.com/sandbox-quantum/switch/main/README.md - the rooms model, the five chat platforms, the any-agent claim, Console and switch-buddy onboarding, connectors, the telemetry disclosure, and the Product Hunt badge (fetched 2026-11-19)
- https://raw.githubusercontent.com/sandbox-quantum/switch/main/LICENSE - Apache-2.0 as limited by the Commons Clause, extended to derivatives, copyright SB Technology, Inc. dba SandboxAQ (fetched 2026-11-19)
- https://api.github.com/repos/sandbox-quantum/switch/releases?per_page=5 - the release train: switch-core 0.32.1 and Switch Console 0.41.1 (both 2026-11-18), canary 0.42.0-canary.1 (2026-11-18), dev builds of main daily (fetched 2026-11-19)
- https://www.switchagents.ai/ - the Switch AI product family (Rooms, Trust, ROI), the SandboxAQ branding, and the Dr. Jeffrey Bander quote (fetched 2026-11-19)
- https://docs.switchagents.ai/switch-rooms/getting-started - the rooms-and-agents model, the per-agent owner rule, and the recorded move from docs.flintai.dev (fetched 2026-11-19)
- https://docs.switchagents.ai/switch-rooms/getting-started/quickstart.md - the Console quickstart, the per-agent provider choice under your own account, and the Teams admin requirement (fetched 2026-11-19)
- https://www.switchagents.ai/case-studies/case-study-mount-sinai - the Mount Sinai West case study: MSW Lab as design partner, in alpha, on the Trust product line (fetched 2026-11-19)
- https://hn.algolia.com/api/v1/search?query=switchagents&tags=story - the coverage search finding one 1-point thread and no other discussion (fetched 2026-11-19)
- https://hn.algolia.com/api/v1/items/49468269 - the single thread, "Project Switch: Agents and humans work side-by-side" (2026-08-27, 1 point, zero comments) (fetched 2026-11-19)
- https://www.switchagents.ai/get-started - the free-to-start Rooms and Trust/ROI signup paths and the demo path behind the unpublished paid tiers (fetched 2026-11-19)
