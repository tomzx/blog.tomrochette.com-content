---
title: Agent Network Protocol (ANP)
created: 2026-10-05
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, protocols, interoperability, decentralized-identity, multi-agent]
readability: 3
audience_notes: >
  Engineers tracking agent-to-agent interoperability who want to know whether the
  decentralized, open-web alternative to A2A is worth watching.
  Assumes you know what A2A and MCP are and what a DID is at a handshake level.

---

ANP (Agent Network Protocol) is an open-source protocol suite for connecting agents on the open web, built on DID-based identity, description and discovery documents, and end-to-end encrypted messaging profiles.

**ANP is the only protocol in this index betting that agent-to-agent interconnection should be decentralized and web-native rather than mediated by enterprise platforms, and after two years it has the spec depth to show for it and almost none of the adoption, and I read that mismatch as the bet's unproven state.**

## What it is

A versioned specification suite published at agent-network-protocol.com: a technical white paper, an agent description protocol, an agent discovery protocol, the DID:WBA identity method (a did:web derivative), and a nine-part messaging profile ladder (core binding, discovery, direct and group messaging, direct and group end-to-end encryption, attachments, federation, mentions), with an agent communication meta-protocol and an agent payment protocol still in draft.
Apache-2.0, driven by a community working group with bilingual English and Chinese documentation, currently at spec version 1.2 (1.0 and 1.1 archived).
Working code exists around the spec: the `anp` implementation repository, an open DID server, npm packages under the `@agent-network-protocol` scope, and an `mcp2anp` bridge that turns MCP tools into ANP-advertised services.

## Status

**Active but unanswered by the market.**
The main repository (created 2024-10-23) shows 1,439 stars, 105 forks, and a push on 2026-10-01, with the companion `anp` repo at 350 stars and the spec hub serving ANP 1.2, all as of 2026-10-06 (GitHub API and the spec site).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=agent-network-protocol/AgentNetworkProtocol&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=agent-network-protocol/AgentNetworkProtocol&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=agent-network-protocol/AgentNetworkProtocol&type=date&legend=top-left" />
</picture>

The community footprint is the weak signal: the only Hacker News stories are 2 points (2025-08) and 1 point (2025-11), and the only third-party comparative coverage I found is a 2026-02 survey published by the OSSA project, which scores ANP under 1 percent production use while promoting its own contract layer, so even the comparative source is self-interested.
No enterprise platform ships ANP support; adoption evidence is confined to the project's own examples, SDKs, and bridge tools.

## Strengths

- **DID-based identity is a genuinely different answer to the trust problem**: A2A verifies agent identity with signed Agent Cards inside enterprise trust, while DID:WBA wants cross-domain verification with no platform in the middle.
- The messaging profile ladder is the most complete transport-and-encryption story in the category on paper, ending in federated, end-to-end encrypted group messaging that no rival spec even attempts.
- The `mcp2anp` bridge is a pragmatic on-ramp: an MCP server's tools can be advertised as ANP services, so adoption does not require abandoning MCP.
- Versioned, archived specifications (1.0, 1.1, 1.2) show specification discipline most community protocols never reach.

## Cautions

- **Adoption is near zero, and the parts that would make it matter have not moved**: no harness, surface, or platform in this index speaks it, and its discussion footprint is three stories totaling 4 points.
- The complexity budget is large: DID resolution, namespace specifications, nine messaging profiles, and two draft protocols are a lot of machinery for a network that does not exist yet.
- The README carries a disclaimer that the project has issued no digital currency, an unusual line that hints at impersonation noise around the identity technology.
- Governance is a single community working group with no foundation and no corporate backer on the order of A2A's eight-company steering committee.

## Pricing

Free and open under Apache-2.0, with nothing to buy.
The cost is specification and implementation tracking across a broad, still-moving suite.

## Compared to

- [A2A](../a2a/index.md): the enterprise, platform-mediated counterpart; A2A has the coalition, the SDKs, and the production deployments, ANP has the decentralization. Choose A2A where platforms support it.
- [MCP](../mcp/index.md): agent-to-tool rather than agent-to-agent, and the bridge makes them compose rather than compete.
- [ACP](../acp/index.md): editor-to-agent over local stdio, a different lane entirely from open-web discovery.

## Bottom line

**Recommended for researchers and builders prototyping open-web agent discovery, where ANP is the only developed option in this index.**
Not for production engineering teams today: use A2A where your platforms already speak it and MCP for tools.
My disagreeable claim: if autonomous agents on the open web ever emerge, ANP's DID-and-discovery design is a more likely base than A2A, but the probability that they emerge on either spec is the number to discount.

## Changes

- 2026-10-05 - Created from the 2026-10-05 entrant scan (the decentralized agent-interop slot), with the thin adoption footprint recorded as the central caution.
- 2026-10-07 - Added the agent-network-protocol/AgentNetworkProtocol star history chart to the Status section.

## See also

- [Protocols Feature Matrix](../protocols-feature-matrix/index.md) - the category comparison this note joins as the seventh column
- [A2A](../a2a/index.md) - the enterprise counterpart whose adoption gap ANP inherits in worse form
- [Model Context Protocol](../mcp/index.md) - the tool layer the mcp2anp bridge advertises into ANP
- [Agent Client Protocol](../acp/index.md) - the local editor-to-agent lane ANP does not touch

## References

- https://github.com/agent-network-protocol/AgentNetworkProtocol - repository, 1,439 stars, Apache-2.0, activity as of 2026-10-06 (GitHub API)
- https://raw.githubusercontent.com/agent-network-protocol/AgentNetworkProtocol/master/README.md - vision, protocol-suite framing, the digital-currency disclaimer
- https://agent-network-protocol.com/ - spec hub: ANP 1.2 latest, 1.0 and 1.1 archived, core protocols and messaging profiles
- https://agent-network-protocol.com/specs/1.2/white-paper - the ANP 1.2 technical white paper
- https://api.github.com/orgs/agent-network-protocol/repos - the companion implementations (anp 350 stars, open-did-server, mcp2anp, anp-open-sdk), fetched 2026-10-06
- https://hn.algolia.com/api/v1/search?query=%22Agent%20Network%20Protocol%22&tags=story - the footprint scan: stories at 2, 1, and 1 points (2025-08 to 2026-01)
- https://openstandardagents.org/research/agent-communication-protocol-survey/ - the only third-party comparative coverage found, itself published by a competing project (2026-02-20)
