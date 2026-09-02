---
title: Agent Host Protocol
created: 2026-08-30
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.3, protocols, agent-sessions, state-synchronization, microsoft, open-source]
readability: 3
audience_notes: >
  Engineers building clients, harnesses, or integrations on top of AI coding-agent sessions who must decide whether to adopt Microsoft's session-state protocol.
  Assumes you know what MCP and ACP are and what an agent session is.
---

The Agent Host Protocol (AHP) is Microsoft's MIT-licensed wire protocol for a standalone sessions server that gives any number of clients one synchronized view of AI agent sessions, built on immutable state, pure reducers, and write-ahead reconciliation.
Facts below verified as of 2026-09-02.

**AHP claims the one lane the protocol stack left empty, the session itself: MCP covers agent-to-tool, ACP covers editor-to-agent, A2A covers agent-to-agent, and AHP turns a live agent session into a shared resource any client can attach to, with the reference host shipping inside VS Code.**

## What it is

A protocol specification plus client SDKs in six languages: Rust (`ahp` on crates.io), TypeScript (`@microsoft/agent-host-protocol` on npm), Kotlin (Maven Central), Go, Swift (SwiftPM), and .NET (NuGet), each released independently on its own SemVer track.
The core abstraction is the channel, a URI-identified subscribable resource (`ahp-root://`, `ahp-session:/<uuid>`, `ahp-chat:/<uuid>`, plus terminal and changeset channels) that holds either an immutable state tree or a stateless pub/sub topic.
Clients apply actions optimistically, then reconcile when the host's echo returns stamped with a monotonic sequence number; the docs place AHP in the lineage of LSP and DAP.
It is agent-agnostic by design, describing client-facing session state without binding clients to a runtime, and an MCP channel exists with MCP relay and LSP relay planned.
MIT licensed, TypeScript, under the `microsoft` GitHub org, created 2026-03-12.

## Status

**Active and shipping: 296 stars, 86 forks, 47 open issues as of 2026-09-02, with commits landing the day before verification and spec v0.9.0 tagged 2026-08-28 alongside matching client releases.**
Adoption is real where it counts: the `ahp` crate records about 194,000 downloads and the npm package about 83,000 in the month before verification, both as of 2026-09-02.
A member of the VS Code team stated publicly in June 2026 that the team is rebuilding its agent infrastructure on AHP, and the reference host lives at `src/vs/platform/agentHost/node` in the `microsoft/vscode` repository.
Pre-1.0 in the exact sense: the spec sits at v0.9.0 and wire churn is expected.

## Strengths

- **Distribution no rival spec has: the reference host ships inside VS Code, the editor a large fraction of working engineers already run.**
- A six-language SDK surface published to six package registries, which is more than most protocol projects ever reach.
- A clean core model (immutable state, pure reducers, one totally ordered envelope stream) that ordinary clients can implement.
- The docs carry a doctrine page on AHP and ACP, so the boundary with the closest neighbor protocol is stated by the project itself rather than left to inference.

## Cautions

- Microsoft-controlled: the spec lives in the `microsoft` org with repo-first governance and no foundation, so neutrality is unproven.
- A v0.9.0 spec means breaking changes; conformance work between the TypeScript and .NET clients was literally in flight in August 2026.
- The crates.io download figure includes CI rebuilds, so read it as an upper bound (the same skepticism this corpus applies to vendor benchmarks).
- It is a fifth protocol to track, and the sprawl criticism recorded against ACP applies here too.

## Pricing

Free and open under MIT, nothing to buy.
The costs are implementing or operating a host, plus tracking spec churn until 1.0.

## Compared to

- [ACP](../acp/index.md): both sit in editor-to-agent territory, but ACP drives one agent from one client over stdio while AHP hosts many clients on one synchronized session through a server; choose ACP for harness portability inside your editor, AHP when several surfaces must share a live session.
- [MCP](../mcp/index.md): agent-to-tool and complementary by design; AHP's docs treat MCP as a channel to relay, not a competitor.
- [A2A](../a2a/index.md): cross-organization delegation between opaque agents; AHP is single-organization client-to-host and about live shared state rather than task delegation.

## Bottom line

**Recommended for tool builders who want a client attached to VS Code agent sessions today, with pre-1.0 churn priced in; not for cross-org delegation or tool integration, where A2A and MCP remain the answers.**
The disagreeable part: I think AHP will matter more to daily coding work than A2A ever will, because whoever owns the host owns the session, and most engineers already run theirs (VS Code).

## See also

- [Protocols Feature Matrix](../protocols-feature-matrix/index.md) - the category comparison this note joins, now with its own AHP column
- [MCP](../mcp/index.md) - the agent-to-tool layer AHP relays as a channel
- [ACP](../acp/index.md) - the closest lane neighbor, and the subject of AHP's own doctrine page
- [A2A](../a2a/index.md) - the cross-org layer, and the Ask HN thread where the VS Code team announced the AHP bet
- [VS Code + Copilot](../vscode-copilot/index.md) - the surface whose built-in agent host is the protocol's reference implementation

## References

- https://github.com/microsoft/agent-host-protocol - repository, six-language SDK table, VS Code reference host pointer, MIT license
- https://microsoft.github.io/agent-host-protocol/ - docs home: problem framing, host broadcast model, optimistic-apply reconciliation
- https://microsoft.github.io/agent-host-protocol/guide/what-is-ahp - channel abstraction, URI schemes, agent-agnostic stance, planned MCP and LSP relay
- https://microsoft.github.io/agent-host-protocol/specification/overview - RFC 2119 conventions and the x- extension rule
- https://registry.npmjs.org/@microsoft%2Fagent-host-protocol - TypeScript client, 10 versions, latest 0.9.0
- https://api.npmjs.org/downloads/point/last-month/@microsoft/agent-host-protocol - 83,361 downloads 2026-07-31 to 2026-08-29
- https://crates.io/api/v1/crates/ahp - Rust client, 193,943 downloads and repository pointer as of 2026-09-02
- https://hn.algolia.com/api/v1/items/48582679 - the Ask HN A2A thread containing the VS Code team's AHP announcement comment (2026-06-18)
- https://github.com/microsoft/vscode/tree/main/src/vs/platform/agentHost/node - the reference host implementation inside the VS Code tree
