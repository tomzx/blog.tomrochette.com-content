---
title: Agent Protocol (LangChain)
created: 2026-10-07
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, protocols, interoperability, agent-serving, rest-apis]
readability: 3
audience_notes: >
  Engineers deploying LLM agents behind a production API who must decide between rolling their own
  run/thread endpoints and adopting a shared serving spec.
  Assumes you know what MCP and A2A are and what an OpenAPI document is.

---

The Agent Protocol is LangChain's open, MIT-licensed REST/OpenAPI specification for the server-side API that applications call to run LLM agents in production, organized around Agents, Threads, and Runs resources.

**MCP connects agents to tools and A2A connects agents to each other, and this spec claims the boring lane in between: the deployment API your app calls to create, stream, wait on, and cancel an agent run, with LangGraph Platform already shipping the first commercial superset of it.**

## What it is

The OpenAPI document (v0.1.6 as of 2026-10-07) defines endpoints for agent listing and schemas, thread CRUD plus history and copy, and run execution with search, stream, wait, and cancel, so any conforming server exposes the same serving surface.
A companion streaming specification adds primitives with a CDDL schema and generated Python and TypeScript bindings for live agent execution.
The repository ships a Python server stub generated from the spec (FastAPI and Pydantic v2), an open-source LangGraph.js implementation using in-memory storage, and self-hosted async-subagent server examples in the deepagents projects.
MIT licensed, stewarded in the `langchain-ai` GitHub organization (repository created 2024-11-12, not a fork), with the README framing it as framework-agnostic: any agent can sit behind the API.

## Status

**Active and implementation-backed, with a thin independent footprint.**
The repository shows 684 stars, 65 forks, and a push on 2026-10-07, all as of 2026-10-08 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=langchain-ai/agent-protocol&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=langchain-ai/agent-protocol&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=langchain-ai/agent-protocol&type=date&legend=top-left" />
</picture>

The spec is exercised by shipping software: LangGraph Platform implements a superset of it commercially, and the open-source LangGraph.js API and deepagents example servers implement it directly.
The community footprint is the weak signal: an Algolia scan found no dedicated Hacker News launch thread for this spec (2026-10-07), and its 684 stars sit far below every wire protocol in this index.
The name is a collision hazard: a different "Agent Protocol" (agentprotocol.ai, from the 2023 e2b and AI Engineer Foundation effort, Show HN July 2023) standardized CLI agent invocation and shows up in the same search results.

## Strengths

- **It specifies exactly the layer teams otherwise hand-roll: runs, threads, streaming, cancellation, with search and schemas, so the spec reads like the API you were about to write anyway.**
- Implementation-first stewardship: server stubs, an in-memory reference implementation, and self-hosted examples ship in the repository rather than as promises.
- Streaming is specified, not hand-waved, with a CDDL schema and generated bindings for Python and TypeScript.
- Framework-agnostic ambition: the endpoints describe serving resources, not LangChain internals, so a non-LangChain agent can conform.

## Cautions

- **Steward and commercial winner are the same company**: LangChain both stewards the spec and sells LangGraph Platform as a superset implementation, and there is no foundation or third-party governance.
- The community footprint is missing as of 2026-10-07: no dedicated launch discussion on Hacker News and adoption evidence confined to LangChain's own ecosystem, which is itself a signal about reach.
- The spec is at 0.1.6, pre-1.0, so endpoint stability is unproven.
- Its lane overlaps A2A's remote-invocation story and every cloud provider's agent-serving API, so the second independent implementation everyone waits for has not arrived.

## Pricing

The specification and the repository tooling are free and MIT-licensed.
LangGraph Platform, the commercial superset implementation, is separately priced by LangChain, and self-hosted alternatives (the LangGraph.js API, the example servers) exist for the spec itself.

## Compared to

- [A2A](../a2a/index.md): peer-agent delegation with Agent Cards across trust boundaries; the Agent Protocol is one application calling one agent's serving API, closer to a deployment contract than an inter-agent fabric.
- [Agent Host Protocol](../agent-host-protocol/index.md): both are client-to-agent-infrastructure specs, but AHP synchronizes live session state across many clients while the Agent Protocol standardizes the run lifecycle endpoints of a hosted agent.
- The 2023 agentprotocol.ai spec: same name, different target, that one standardized CLI agent invocation and has been quiet, so check which one a tool means before integrating.

## Bottom line

**Recommended for teams deploying agents who want a conventional runs-and-threads API boundary without inventing one, accepting LangChain stewardship and a pre-1.0 spec.**
Not for agent-to-agent delegation, where A2A remains the answer.
My disagreeable claim: this lane matters more than the protocol-sprawl critics admit, because every production deployment invents these endpoints anyway, and the argument is only over whether one spec or five win them.

## Changes

- 2026-10-07 - Created from the 2026-10-07 entrant scan (the serving-API slot), with the single-company stewardship and the missing community footprint recorded as the central cautions.

## See also

- [Agent2Agent Protocol (A2A)](../a2a/index.md) - the agent-to-agent layer this serving spec is adjacent to and often confused with
- [Agent Host Protocol](../agent-host-protocol/index.md) - the other client-to-infrastructure spec in this index, on the session-state side
- [Model Context Protocol (MCP)](../mcp/index.md) - the tool layer a served agent consumes downstream
- [Protocols Feature Matrix](../protocols-feature-matrix/index.md) - the category comparison this note joins as the tenth column

## References

- https://github.com/langchain-ai/agent-protocol - repository: 684 stars, 65 forks, MIT, created 2024-11-12, pushed 2026-10-07 (GitHub API, as of 2026-10-08)
- https://raw.githubusercontent.com/langchain-ai/agent-protocol/main/README.md - purpose, endpoint rationale, streaming spec, server stubs, implementations, and the LangGraph Platform superset claim
- https://langchain-ai.github.io/agent-protocol/openapi.json - the OpenAPI document: title Agent Protocol, version 0.1.6, agents, threads, and runs endpoints as of 2026-10-07
- https://langchain-ai.github.io/agent-protocol/api.html - the docs home the repository lists as its homepage
- https://www.langchain.com/pricing-langgraph-platform - the commercial LangGraph Platform page (fetches 200; renders client-side), the superset implementation
- https://hn.algolia.com/api/v1/search?query=langchain%20agent%20protocol&hitsPerPage=6 - the footprint scan: no dedicated launch thread for the LangChain spec, found 2026-10-07
- https://hn.algolia.com/api/v1/search?query=%22agent%20protocol%22&tags=story - the name-collision record: Show HN Agent Protocol (2023-07-24) and related stories for the older agentprotocol.ai spec
