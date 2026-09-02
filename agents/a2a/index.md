---
title: Agent2Agent Protocol (A2A)
created: 2026-08-24
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, protocols, interoperability, multi-agent]
readability: 3
audience_notes: >
  Engineers and architects evaluating how agents built on different frameworks should discover and delegate work to each other.
  Assumes familiarity with MCP and with enterprise platform integration patterns.

---

A2A is an open protocol for communication and interoperability between independent, opaque AI agents.
Facts below verified as of 2026-09-02.

**It is the enterprise answer to agent interoperability: adoption is real at the platform layer and nearly invisible in startup and coding-agent usage, and that split is the story.**

## What it is

A client agent delegates tasks to remote agents discovered through Agent Cards, over bindings to JSON and HTTP, gRPC, or JSON-RPC, with polling, streaming, and webhooks for long-running tasks.
Agents stay opaque: no shared memory, tools, or internal state crosses the boundary.
**Google created and open-sourced it in April 2025, donated it to the Linux Foundation in June 2025, and a technical steering committee from AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP, and ServiceNow now governs it, Apache-2.0.**
IBM's rival Agent Communication Protocol merged into A2A in August 2025, consolidating the agent-to-agent space.

## Status

**Active, spec-stable, unevenly adopted.**
v1.0.0 shipped 2026-03-12 and v1.0.1 on 2026-05-26 (latest as of 2026-09-02), with breaking wire changes from 0.3 but backward-compatible Agent Cards.
The repository shows about 25.6k stars as of 2026-09-02, and the launch coalition of 50+ partners passed 100 supporting companies by donation time.
Support concentrates in enterprise suites (Gemini Enterprise, Agentforce, watsonx Orchestrate, SAP Joule, Azure AI Foundry).
No coding harness in this index speaks it natively; the closest touchpoint is [Gemini CLI](../gemini-cli/index.md), where community setups attach remote A2A agents.

## Strengths

- **Solves discovery, delegation, and long-running tasks across trust boundaries, which plain REST leaves to every integrator.**
- Web-aligned core: an interaction can begin with a single HTTP request and scale through existing load balancers, gateways, and observability.
- Six official SDKs (Python, Go, JavaScript, Java, .NET, Rust) under genuinely neutral governance.
- Signed Agent Cards give cryptographic identity verification before any interaction.

## Cautions

- **The usage gap with MCP is the signal**: an A2A ecosystem developer reported roughly 10.9M monthly a2a-sdk downloads versus about 257M for the MCP SDK (pypistats, mid-June 2026).
- Critics argue MCP already covers the ground by treating agents as tools, and a June 2026 Ask HN thread (45 comments) found thin startup usage plus concrete complaints about identity assumptions and gRPC friction.
- v1.0 broke wire compatibility with v0.3, so early adopters are mid-migration.
- Prompt injection across agent boundaries remains unsolved at the protocol level.

## Pricing

**Free and open, Apache-2.0, with nothing to buy.**
Google monetizes the surrounding platforms (Gemini Enterprise, ADK), not the protocol.

## Compared to

- [MCP](../mcp/index.md): **agent-to-tool, complementary by design; the official framing is MCP inside agents, A2A between agents**.
- [ACP](../acp/index.md): editor-to-agent for coding agents, local-first; A2A is organization-to-organization and remote-first.
- REST plus an OpenAPI spec: adequate for one-to-one integrations, with no discovery or task lifecycle.

## Bottom line

**Recommended when agents from different vendors or departments must delegate work across a boundary; not for wiring up your own sub-agents, where native primitives or MCP are simpler.**
The disagreeable part: I expect A2A to stay an enterprise convention, and if autonomous agents on the open web ever emerge they will speak MCP or plain HTTP first, not A2A.

## See also

- [Model Context Protocol](../mcp/index.md) - the complementary agent-to-tool layer it is always paired with
- [Agent Client Protocol](../acp/index.md) - the coding-agent corner of the interoperability stack
- [AGENTS.md](../agents-md/index.md) - the third convention in the Linux Foundation-adjacent stack
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - why the harness layer mostly ignores A2A today
- [Gemini CLI](../gemini-cli/index.md) - Google's harness, the closest contact point in the index

## References

- https://a2a-protocol.org/latest/ - official site: Agent Cards, MCP complementarity, TSC membership, Apache-2.0
- https://github.com/a2aproject/A2A - repository, stars as of 2026-09-02, SDK list
- https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ - launch announcement (2025-04-09), 50+ partners
- https://developers.googleblog.com/en/google-cloud-donates-a2a-to-linux-foundation/ - Linux Foundation donation (2025-06-23), founding members
- https://github.com/a2aproject/A2A/releases - v1.0.0 (2026-03-12) and v1.0.1 (2026-05-26) release notes
- https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/ - IBM ACP merge and TSC composition
- https://blog.fka.dev/blog/2025-04-15-why-googles-a2a-protocol-doesnt-make-sense/ - the MCP-redundancy critique
- https://news.ycombinator.com/item?id=48582679 - Ask HN usage thread: thin startup adoption, the download-ratio report
