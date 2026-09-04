---
title: Model Context Protocol (MCP)
created: 2026-08-24
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, protocols, interoperability, agent-tools]
readability: 3
audience_notes: >
  Engineers who already use a coding agent or AI assistant and want to understand the protocol their tool integrations speak.
  Assumes familiarity with JSON-RPC style APIs and a basic client/server split.

---

MCP is an open protocol that standardizes how AI applications connect to external tools, data sources, and workflows.
Facts below verified as of 2026-09-04.

**It is the de facto standard for agent-to-tool integration, and its one-year run from launch to industry default has no precedent I can find in developer tooling.**

## What it is

The protocol defines JSON-RPC messages between hosts (LLM applications), clients (connectors inside the host), and servers that expose tools, resources, and prompts, with per-request capability negotiation.
It openly borrows its playbook from the Language Server Protocol, which solved the same N-times-M integration problem for editors and languages.
Anthropic created it (David Soria Parra and Justin Spahr-Summers), open-sourced it on 2024-11-25, and donated it to the Linux Foundation's Agentic AI Foundation (AAIF) on 2025-12-09.
**The spec and schema are MIT-licensed, and the current specification revision is 2026-07-28, grown through opt-in extensions (Tasks, Skills over MCP, MCP Apps).**

## Status

**Active and dominant.**
The specification repository shows about 9.1k stars and 4,673 commits as of 2026-09-02.
The AAIF announcement claimed more than 10,000 published MCP servers and adoption by Claude, Cursor, Microsoft Copilot, Gemini, VS Code, and ChatGPT.
In this index, [Claude Code](../claude-code/index.md), [Cursor](../cursor/index.md), [VS Code Copilot](../vscode-copilot/index.md), [Gemini CLI](../gemini-cli/index.md), and [Crush](../crush/index.md) all speak it.
Governance is now neutral, with AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, and OpenAI as AAIF platinum members.

## Strengths

- **One integration works across every major client, which is why server authors target MCP first.**
- Simple core (stateless JSON-RPC requests) that any language can implement.
- Foundation governance removes the single-vendor risk that slowed earlier standard attempts.
- The extension mechanism (long-running tasks, skills, inline apps) gives it a growth path without breaking clients.

## Cautions

- **The security model trusts tool descriptions, and that trust is attackable.**
Invariant Labs demonstrated tool poisoning (hidden instructions in descriptions exfiltrating SSH keys and configs from Cursor) and rug pulls, where a server changes its description after the user approved it.
- A 10,000-server ecosystem is a supply chain: community scans keep surfacing credential leaks and malicious packages in published servers.
- Spec revisions are date-stamped and frequent (2025-11-25, then 2026-07-28), so client and server support drifts.
- Remote-server auth and deployment remain the rough edges teams hit in production.

## Pricing

**The protocol itself is free and open (MIT spec and schema).**
Costs come from hosting remote servers and from the tokens that tool schemas and results consume, not from the protocol.

## Compared to

- [ACP](../acp/index.md): editor-to-agent for coding agents, where MCP is agent-to-tool; they compose.
- **Plain REST plus an OpenAPI spec: universal but no discovery, consent flow, or streaming semantics, so every client reimplements them.**
- Vendor plugin formats (ChatGPT apps, Claude connectors): richer one-host UX, zero portability.

## Bottom line

**Recommended as the default way to expose tools and context to agents; I would not build a bespoke integration layer in 2026 without a specific, measured reason.**
The disagreeable part: MCP's security story lags its adoption story, and teams adopting it wholesale are accepting a supply-chain risk they have mostly not priced in.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where MCP sits in the convention layer of the four-layer map
- [Agent Client Protocol](../acp/index.md) - the editor-agent counterpart in the same convention stack
- [Claude Code](../claude-code/index.md) - the harness from MCP's creator, and its heaviest consumer
- [Gemini CLI](../gemini-cli/index.md) - a non-Anthropic client showing the cross-vendor reach
- [Crush](../crush/index.md) - MCP client support across stdio, http, and sse with OAuth

## References

- https://modelcontextprotocol.io - official site: what MCP is, client ecosystem
- https://modelcontextprotocol.io/specification/latest - current spec revision 2026-07-28, JSON-RPC core, extensions
- https://github.com/modelcontextprotocol/modelcontextprotocol - spec repository, MIT license, stars and commits as of 2026-09-02
- https://www.anthropic.com/news/model-context-protocol - launch announcement (2024-11-25) and named creators
- https://aaif.io/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agents-md/ - Linux Foundation donation, member roster, 10,000+ server claim
- https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks - the tool poisoning and rug pull critique
