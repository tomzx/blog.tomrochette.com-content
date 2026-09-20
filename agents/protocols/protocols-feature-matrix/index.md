---
title: "Protocols Feature Matrix"
created: 2026-08-24
updated: 2026-09-18
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, protocols, interoperability]
readability: 3
audience_notes: >
  Engineers deciding which agent protocols to adopt or skip who need the governance, maturity, and adoption deltas at a glance.
  Assumes you know what JSON-RPC, stdio, and a repository instruction file are; each column links to a full note with sources.
---

This matrix compares the six protocols profiled in this section, A2A, ACP, AG-UI, Agent Host Protocol, AGENTS.md, and MCP, so the whole interoperability stack can be read in one table.
Everything below was re-verified against live sources on 2026-09-20.

**The six do not compete, they stack (repo-to-agent, editor-to-agent, agent-to-frontend, agent-to-tool, agent-to-agent, client-to-session), and adoption falls with every step up that stack, which is why I call AGENTS.md and MCP defaults, ACP a rising bet, AG-UI the quiet winner by raw download volume, AHP a bet underwritten by VS Code's own distribution, and A2A an enterprise convention the coding-agent world can keep ignoring.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [A2A](../a2a/index.md) | [ACP](../acp/index.md) | [AG-UI](../ag-ui/index.md) | [Agent Host Protocol](../agent-host-protocol/index.md) | [AGENTS.md](../agents-md/index.md) | [MCP](../mcp/index.md) |
| --- | --- | --- | --- | --- | --- | --- |
| Kind | wire protocol | wire protocol | wire protocol | wire protocol | file convention | wire protocol |
| Originated by | Google (2025-04) | Zed, with JetBrains | CopilotKit (2025-05) | Microsoft (2026-03) | OpenAI-led (2025-08) | Anthropic (2024-11) |
| Steward | AAIF (2026-08), TSC | vendor-neutral org | CopilotKit, no foundation | Microsoft, no foundation | AAIF | AAIF |
| Spec license | Apache-2.0 | Apache-2.0 | MIT | MIT | MIT | MIT |
| Maturity | v1.0.1 (2026-05) | version 1, v2 draft, remote WIP | packages 1.0.0 (2026-09-17), spec 1.0 | v0.9.0 (2026-08-28) | unversioned, de facto standard | dated revisions (2026-07-28) |
| What it connects | agent-to-agent | editor-to-agent | agent-to-frontend | client-to-session | repo-to-agent | app-to-tools |
| Adoption in this section | ✗ none native | ~ growing (OpenCode, JetBrains, Zed) | ✗ none native (CopilotKit ecosystem outside this index) | ~ VS Code reference host | ~ most, Claude Code holdout | ✓ near-universal |
| Transport or location | HTTP, gRPC, JSON-RPC | JSON-RPC over stdio | SSE, WebSockets, webhooks | URI channels on a standalone sessions server | Markdown at repo root | JSON-RPC, stdio to sse |
| Official SDKs | ✓ six | ✓ five | ✓ three (TypeScript, Python, .NET) | ✓ six | ✗ none needed | ✓ any language |
| Criticism recorded | redundant with MCP | sprawl, flattened UX | single-vendor origin, pre-1.0 churn | more sprawl, one vendor's governance | weak efficacy evidence | tool poisoning, supply chain |

## Reading the matrix

**Governance converged faster than adoption, and every protocol that went neutral did so only after it had already won or stalled.**
Google donated A2A to the Linux Foundation in June 2025, Anthropic and OpenAI donated MCP and AGENTS.md to the AAIF the same day (2025-12-09), and A2A itself joined the AAIF as a Growth Stage project on 2026-08-27, so three of the six now sit in the same foundation.
ACP is stewarded by Zed and JetBrains under a vendor-neutral organization with no foundation home, AHP stays inside the `microsoft` org with repo-first governance, and AG-UI, the newest column, is the one still closest to its corporate parent, CopilotKit, which also sells commercial support for it, so the stack now has three non-foundation columns, and ACP remains the one compounding fastest in editors.
I read this as governance following adoption, not causing it.

**Adoption falls as the protocol climbs the stack, and the file convention beat every wire protocol to default status.**
MCP is table stakes across the harness and surface matrices; AGENTS.md counts more than 60,000 carrying projects with one glaring holdout (Claude Code); ACP rides OpenCode, JetBrains, Zed, and a Copilot CLI preview; A2A has no native speaker among this index's harnesses, only community setups near Gemini CLI; AHP is just over six months old with 346 stars as of 2026-09-20, but its reference host ships inside VS Code and the VS Code team has said publicly it is rebuilding its agent infrastructure on the protocol.
The SDK download ratio recorded in the A2A note, 10.9M monthly versus 257M for MCP, is the gap in one number, and AHP's roughly 337k combined downloads (about 234k crates plus 103k npm, the npm curve spiking mid-September) show the same order-of-magnitude distance from the top.
AG-UI is the anomaly that proves the rule: none of this index's harnesses or surfaces speak it natively, yet its SDKs moved about 12.5M combined npm downloads in the last month as of 2026-09-18, because the frontend layer is where end-user products live even though coding tools never touch it.

**The consolidations the notes record happened in opposite corners, and neither touched the other's territory.**
IBM's Agent Communication Protocol (the other ACP, the source of the name collision) merged into A2A in August 2025 under LF AI and Data.
JetBrains folded its internal Junie protocol into the Agent Client Protocol instead.
Both mergers cut the rival count in 2025 while leaving the enterprise-remote and local-editor layers separate.

**Each recorded criticism is a different species of doubt, and the pattern favors the incumbents.**
MCP is criticized for risks it creates (tool poisoning, rug pulls, a 10,000-server supply chain); AGENTS.md for whether it helps at all (an ETH Zurich study found no success-rate gain and over 20% added inference cost, against Vercel's counter-evidence); ACP for UX flattening and protocol sprawl; AHP for being a fifth protocol to track under one vendor's governance; A2A for whether it should exist at all; AG-UI for provenance and maturity, a CopilotKit-originated stack that only graduated to 1.0.0 packages on 2026-09-17 and whose adoption story lives in vendor blogs.
The mature protocols get attacked for their risks, the young ones for their reason to exist or their provenance.

## Choosing from the matrix

- Exposing tools or data to any agent: MCP, the default with a supply-chain asterisk.
- Choosing harness and editor independently: ACP, the cheapest portability insurance in the stack.
- Streaming an agent into a product frontend: AG-UI, accepting CopilotKit's stewardship and dated-release churn (1.0.0 only landed 2026-09-17).
- Any repository an agent touches: commit a short AGENTS.md, commands and conventions first.
- Delegating work across vendors or departments: A2A, provided both sides run enterprise platforms.
- Attaching a second client to a live agent session: AHP, provided v0.9.0 churn and Microsoft's stewardship are acceptable.
- Wiring sub-agents inside one framework: none of these, native primitives or MCP are simpler.

## Changes

- 2026-08-24 - Created with the stacking thesis and recorded protocol consolidations.
- 2026-09-16 - Extended from five to six columns with AG-UI, re-sorted alphabetically, and updated the governance, adoption, criticism, and choosing prose for the agent-to-frontend layer.
- 2026-09-18 - AG-UI maturity cell updated to 1.0.0 packages and a published 1.0 specification, and stars and download figures refreshed in the AG-UI and AHP prose.

## See also

- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - where MCP and AGENTS.md show up as product features
- [Surface Feature Matrix](../../surfaces/surface-feature-matrix/index.md) - the editor side of the ACP story
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map that names the convention layer these protocols form
- [Gemini CLI](../../harnesses/gemini-cli/index.md) - the closest A2A touchpoint among the profiled harnesses

## References

- https://a2a-protocol.org/latest/ - Agent Cards, TSC membership, Apache-2.0 for the A2A column
- https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/ - the A2A-AAIF acceptance (2026-08-27) behind the updated Steward cell
- https://lfaidata.foundation/communityblog/2025/08/29/acp-joins-forces-with-a2a-under-the-linux-foundations-lf-ai-data/ - IBM ACP merge into A2A for the consolidation paragraph
- https://agentclientprotocol.com - stdio model and protocol version 1 for the ACP column
- https://github.com/ag-ui-protocol/ag-ui - repository facts (15,940 stars, MIT, created 2025-05-07, pushed 2026-09-18) for the AG-UI column (GitHub API, as of 2026-09-18)
- https://raw.githubusercontent.com/ag-ui-protocol/ag-ui/main/README.md - origin by CopilotKit, around 16 event types, transports, and integration tables for the AG-UI column
- https://docs.ag-ui.com - TypeScript, Python, and .NET SDKs and the published 1.0 specification for the AG-UI column
- https://api.npmjs.org/downloads/point/last-month/@ag-ui/core - 7,497,024 downloads for the adoption paragraph
- https://api.npmjs.org/downloads/point/last-month/@ag-ui/client - 5,030,868 downloads for the adoption paragraph
- https://agents.md - format, nested scoping, and adoption count for the AGENTS.md column
- https://aaif.io/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agents-md/ - same-day AAIF donations of MCP and AGENTS.md
- https://modelcontextprotocol.io/specification/latest - spec revision 2026-07-28 for the MCP column
- https://arxiv.org/abs/2602.11988 - the efficacy critique in the AGENTS.md column
- https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks - the tool poisoning critique in the MCP column
