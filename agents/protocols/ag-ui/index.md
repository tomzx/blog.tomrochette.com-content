---
title: Agent User Interaction Protocol (AG-UI)
created: 2026-09-16
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, protocols, frontend, event-streaming]
readability: 3
audience_notes: >
  Engineers wiring an agent backend to a web or mobile frontend who want agent state, messages, and tool calls to stream without building a bespoke event layer.
  Assumes you know what SSE, MCP, and JSON events are.

---

AG-UI is an open, MIT-licensed, event-based protocol that standardizes how agent backends stream state, messages, tool calls, and human-in-the-loop controls into user-facing frontends, transport-agnostic over SSE, WebSockets, or webhooks.
Facts below verified as of 2026-09-24.

**MCP gave agents tools and A2A gave agents each other, and AG-UI is the bet that the missing layer is the one between the agent and the pixels, a bet whose SDK download counts dwarf every other protocol at this layer.**

## What it is

Agent backends emit around 16 standard event types covering streaming text, tool calls, bidirectional state synchronization, human-in-the-loop interrupts, subagent attribution, and reasoning visibility, and they accept a few simple AG-UI-compatible inputs in return.
A middleware layer lets implementations transform and intercept events, which is how integrations connect existing protocols, in-process agents, or custom backends without rewriting them.
**The protocol was born from CopilotKit's partnerships with LangChain and CrewAI, and the repository (created 2025-05-07) now lives in its own `ag-ui-protocol` organization, MIT-licensed, with TypeScript, Python, and .NET SDKs and the 1.0 specification published at /spec/1.0.**
Scaffolding an app is one command (`npx create-ag-ui-app`), and the project ships a demo suite, the AG-UI Dojo, with working examples per framework.

## Status

Very active and already the de facto standard at its layer.
The repository shows about 16,000 stars and a push on 2026-09-24 as of 2026-09-24, with dated releases landing near-daily (latest `release/2026-09-23`).
**The download signal is the strongest part: `@ag-ui/core` pulled 7.23M and `@ag-ui/client` 4.76M downloads in the last month as of 2026-09-24, numbers that beat every editor- or agent-to-agent protocol in this index, and the packages graduated from 0.0.59 to 1.0.0 on 2026-09-17.**
Integration coverage per the docs: partnership integrations with LangChain/LangGraph and CrewAI, first-party integrations with Microsoft Agent Framework, Google ADK, AWS Strands Agents, AWS Bedrock AgentCore, Mastra, Pydantic AI, Agno, LlamaIndex, and AG2, community integrations for the Claude Agent SDK, Claude Managed Agents, and Langroid, with the OpenAI Agent SDK and Cloudflare Agents marked in progress.
Microsoft adopted the protocol in its Agent Framework (November 2025), Google positioned its A2UI interface project alongside it (December 2025), and Oracle shipped an AG-UI integration for its Agent Specification (December 2025).

## Strengths

- **The framework sweep is the moat: the major agent frameworks either speak AG-UI first-party or ship community integrations, so a frontend written against it reaches most backends.**
- Transport-agnostic by design, with a middleware layer that adapts existing agents instead of forcing rewrites.
- The event vocabulary covers the hard parts of product UX (state deltas, interrupts, generative UI, serialization for history and branching), not just chat text.
- CopilotKit dogfoods it across its own frontend stack, so the protocol is exercised by a shipped product rather than maintained as a spec exercise.

## Cautions

- **Stewardship is effectively single-vendor: CopilotKit originated it, sells commercial support for it, and the neutral-foundation move that MCP, A2A, and AGENTS.md all made has not happened here.**
- Churn stays real: the SDKs only reached 1.0.0 on 2026-09-17 after months at 0.0.x, dated releases continue near-daily, and the docs keep a drafts section for changes under consideration, so pinning is a cost.
- The independent discussion footprint is thin for the adoption numbers: the Show HN launch (2025-05-13) drew 36 points and 5 comments, and the ecosystem story is told mostly in vendor blogs rather than community threads.
- Protocol fatigue is a legitimate objection: this is another acronym in a stack that already has MCP, A2A, ACP, and AHP, and Google's A2UI shows interface-level specs are still contested territory.

## Pricing

**The protocol and SDKs are free and MIT-licensed; the only paid item is optional commercial production support offered through the docs (architecture and implementation help, no public price list).**
Integration cost is the real price: a custom event-stream client or a middleware adapter per backend you want to reach.

## Compared to

- [Agent Client Protocol (ACP)](../acp/index.md): **ACP connects editors to coding agents over stdio; AG-UI connects agents to the web frontends rendering them, so for editor-hosted coding agents ACP wins and for product-facing chat or generative UI AG-UI wins.**
- [Model Context Protocol (MCP)](../mcp/index.md) and A2A: agent-to-tool and agent-to-agent respectively; the docs position AG-UI as the third complementary layer, and the three compose rather than compete.
- Google's A2UI: an open project for agent-driven interfaces, announced December 2025, which targets the generative-UI slice; AG-UI is the broader runtime protocol with the larger installed base.

## Bottom line

**Recommended for any team building a custom frontend over an agent backend: the framework coverage makes it the default choice, and its download numbers say the market already agrees.**
Not for editor-hosted coding agents, which is ACP's lane.
My disagreeable claim: AG-UI is the most adopted protocol in this index that nobody talks about, because frontend plumbing generates no discourse while it quietly becomes infrastructure.

## Changes

- 2026-09-16 - Created.
- 2026-09-18 - AG-UI shipped 1.0: SDK packages reached 1.0.0 on 2026-09-17 and the 1.0 specification is published at /spec/1.0; refreshed stars, forks, releases, and npm download figures; AWS Bedrock AgentCore moved to first-party supported.
- 2026-09-24 - Release train moved to release/2026-09-23 and download figures refreshed (core 7,230,278, client 4,764,755 in the month ending 2026-09-21).

## See also

- [Agent Client Protocol (ACP)](../acp/index.md) - the editor-to-agent counterpart that owns the coding-agent UX lane
- [Model Context Protocol (MCP)](../mcp/index.md) - the tool layer AG-UI composes with, and the governance template it has not followed
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the four-layer map where the agent-to-frontend slot sits
- [Surface Feature Matrix](../../surfaces/surface-feature-matrix/index.md) - the frontend surfaces that consume this protocol

## References

- https://github.com/ag-ui-protocol/ag-ui - repository: about 16,000 stars, MIT, created 2025-05-07, pushed 2026-09-24 (GitHub API, as of 2026-09-24)
- https://raw.githubusercontent.com/ag-ui-protocol/ag-ui/main/README.md - definition, around 16 event types, transport list, middleware, and the full integration tables
- https://docs.ag-ui.com - official docs: TypeScript, Python, and .NET SDKs, concepts (state, interrupts, subagents, generative UI), the published 1.0 specification, production support offer
- https://docs.ag-ui.com/spec/1.0 - the 1.0 specification page
- https://docs.ag-ui.com/agentic-protocols - the MCP, A2A, and AG-UI complementarity page
- https://github.com/ag-ui-protocol/ag-ui/releases - dated release series, latest `release/2026-09-23` published 2026-09-23 (GitHub API)
- https://api.npmjs.org/downloads/point/last-month/@ag-ui/core - 7,230,278 downloads 2026-08-23 to 2026-09-21
- https://api.npmjs.org/downloads/point/last-month/@ag-ui/client - 4,764,755 downloads 2026-08-23 to 2026-09-21
- https://registry.npmjs.org/@ag-ui/client - latest version 1.0.0, published 2026-09-17
- https://news.ycombinator.com/item?id=43974484 - Show HN launch, 36 points and 5 comments, 2025-05-13
- https://hn.algolia.com/api/v1/search?query=AG-UI - the footprint scan: 55 raw hits dominated by false positives, Microsoft adoption story 7 points (2025-11-20), Google A2UI and Oracle integration stories
