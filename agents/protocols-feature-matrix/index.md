---
title: "Protocols Feature Matrix"
created: 2026-08-24
updated: 2026-08-24
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, comparison, protocols, interoperability]
readability: 3
audience_notes: >
  Engineers deciding which agent protocols to adopt or skip who need the governance, maturity, and adoption deltas at a glance.
  Assumes you know what JSON-RPC, stdio, and a repository instruction file are; each column links to a full note with sources.
---

This matrix compares the four protocols profiled in this section, A2A, ACP, AGENTS.md, and MCP, so the whole interoperability stack can be read in one table.
Everything below was verified against live sources on 2026-08-24.

**The four do not compete, they stack (repo-to-agent, editor-to-agent, agent-to-tool, agent-to-agent), and adoption falls with every step up that stack, which is why I call AGENTS.md and MCP defaults, ACP a rising bet, and A2A an enterprise convention the coding-agent world can keep ignoring.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [A2A](../a2a/index.md) | [ACP](../acp/index.md) | [AGENTS.md](../agents-md/index.md) | [MCP](../mcp/index.md) |
| --- | --- | --- | --- | --- |
| Kind | wire protocol | wire protocol | file convention | wire protocol |
| Originated by | Google (2025-04) | Zed, with JetBrains | OpenAI-led (2025-08) | Anthropic (2024-11) |
| Steward | Linux Foundation, TSC | vendor-neutral org | AAIF | AAIF |
| Spec license | Apache-2.0 | Apache-2.0 | MIT | MIT |
| Maturity | v1.0.1 (2026-05) | version 1, remote WIP | unversioned, de facto standard | dated revisions (2026-07-28) |
| What it connects | agent-to-agent | editor-to-agent | repo-to-agent | app-to-tools |
| Adoption in this section | ✗ none native | ~ growing (OpenCode, JetBrains, Zed) | ~ most, Claude Code holdout | ✓ near-universal |
| Transport or location | HTTP, gRPC, JSON-RPC | JSON-RPC over stdio | Markdown at repo root | JSON-RPC, stdio to sse |
| Official SDKs | ✓ six | ✓ five | ✗ none needed | ✓ any language |
| Criticism recorded | redundant with MCP | sprawl, flattened UX | weak efficacy evidence | tool poisoning, supply chain |

## Reading the matrix

**Governance converged faster than adoption, and every protocol went neutral only after it had already won or stalled.**
Google donated A2A to the Linux Foundation in June 2025, and Anthropic and OpenAI donated MCP and AGENTS.md to the AAIF the same day (2025-12-09).
ACP is the outlier, stewarded by Zed and JetBrains under a vendor-neutral organization with no foundation home, and it is the one compounding fastest in editors.
I read this as governance following adoption, not causing it.

**Adoption falls as the protocol climbs the stack, and the file convention beat every wire protocol to default status.**
MCP is table stakes across the harness and surface matrices; AGENTS.md counts more than 60,000 carrying projects with one glaring holdout (Claude Code); ACP rides OpenCode, JetBrains, Zed, and a Copilot CLI preview; A2A has no native speaker among this index's harnesses, only community setups near Gemini CLI.
The SDK download ratio recorded in the A2A note, 10.9M monthly versus 257M for MCP, is the gap in one number.

**The consolidations the notes record happened in opposite corners, and neither touched the other's territory.**
IBM's Agent Communication Protocol (the other ACP, the source of the name collision) merged into A2A in August 2025 under LF AI and Data.
JetBrains folded its internal Junie protocol into the Agent Client Protocol instead.
Both mergers cut the rival count in 2025 while leaving the enterprise-remote and local-editor layers separate.

**Each recorded criticism is a different species of doubt, and the pattern favors the incumbents.**
MCP is criticized for risks it creates (tool poisoning, rug pulls, a 10,000-server supply chain); AGENTS.md for whether it helps at all (an ETH Zurich study found no success-rate gain and over 20% added inference cost, against Vercel's counter-evidence); ACP for UX flattening and protocol sprawl; A2A for whether it should exist at all.
The mature protocols get attacked for their risks, the young ones for their reason to exist.

## Choosing from the matrix

- Exposing tools or data to any agent: MCP, the default with a supply-chain asterisk.
- Choosing harness and editor independently: ACP, the cheapest portability insurance in the stack.
- Any repository an agent touches: commit a short AGENTS.md, commands and conventions first.
- Delegating work across vendors or departments: A2A, provided both sides run enterprise platforms.
- Wiring sub-agents inside one framework: none of these, native primitives or MCP are simpler.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - where MCP and AGENTS.md show up as product features
- [Surface Feature Matrix](../surface-feature-matrix/index.md) - the editor side of the ACP story
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map that names the convention layer these four form
- [Gemini CLI](../gemini-cli/index.md) - the closest A2A touchpoint among the profiled harnesses

## References

- https://a2a-protocol.org/latest/ - Agent Cards, TSC membership, Apache-2.0 for the A2A column
- https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/ - IBM ACP merge into A2A for the consolidation paragraph
- https://agentclientprotocol.com - stdio model and protocol version 1 for the ACP column
- https://agents.md - format, nested scoping, and adoption count for the AGENTS.md column
- https://aaif.io/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agents-md/ - same-day AAIF donations of MCP and AGENTS.md
- https://modelcontextprotocol.io/specification/latest - spec revision 2026-07-28 for the MCP column
- https://arxiv.org/abs/2602.11988 - the efficacy critique in the AGENTS.md column
- https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks - the tool poisoning critique in the MCP column
