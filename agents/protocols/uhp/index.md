---
title: Unified Harness Protocol (UHP)
created: 2026-10-08
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, protocols, interoperability, agent-serving, harnesses]
readability: 3
audience_notes: >
  Engineers embedding coding-agent harnesses (Codex, Claude Code, Gemini CLI, Hermes) behind their own
  product who must decide between hand-rolling a per-harness integration and adopting a shared contract.
  Assumes you know what MCP and ACP are and what the OpenAI Responses API is.
---

UHP is an Apache-2.0, versioned HTTP specification for driving complete agent harnesses as shared infrastructure, standardizing how an application starts a task, streams progress, continues a session, cancels work, and retrieves the files a harness produced.

**UHP claims the serving lane between an application and a coding harness, the same lane the LangChain Agent Protocol opened for served agents, and its adoption bet is deliberate: a conformant server must accept the OpenAI Responses request subset, so existing Responses clients work against a UHP server unchanged.**

## What it is

An HTTP contract with three roles: a Client (a product backend, CLI, CI job, or another agent) sends work to a Server, and the Server drives one or more Harnesses, complete agent runtimes identified by stable bases such as `codex`, `claude-code`, or `hermes`.
Conformance is cumulative across three classes (Core, Extended, Full), tested by a runnable conformance suite the project publishes, and the machine-readable schema ships as OpenAPI 3.1 plus JSON Schema 2020-12.
A configured harness (base plus model, system prompt, tool restrictions, skills, and budgets) is a first-class addressable object, so a product can retune its agent without redeploying its backend.
Apache-2.0, maintained in the HarnessRouter repository under a maintainer-led, proposal-first process (UEP issues) where the specification, the reference implementation, and the conformance suite must move in the same change.

## Status

**Active and shipping fast: 2,920 stars, 296 forks, created 2026-08-09, pushed 2026-10-08, all as of 2026-10-08 (GitHub API).**

The spec is at version 2026-10-04, its fourth version in roughly eight weeks (2026-08-11, 2026-09-12, 2026-09-28, 2026-10-04), with the conformance suite itself patched as recently as 2026-10-06.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=HarnessRouter/harnessrouter&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=HarnessRouter/harnessrouter&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=HarnessRouter/harnessrouter&type=date&legend=top-left" />
</picture>

The implementations page lists three servers and one client: HarnessRouter Community Edition (the 2,920-star open-source runner putting Codex, Claude Code, and Hermes behind the contract), the hosted HarnessRouter service (sixteen harness bases with a console and billing), and SuperQode (62 stars as of 2026-10-08), a harness-engineering framework that speaks UHP both as a server and as a client, which makes it the spec's one second implementation.
The community footprint is the weak signal: the Show HN launch drew 10 points (2026-08-17) and a Hacker News search for the protocol's name returns zero stories (2026-10-08), so the 2,920 stars measure the implementing product, not the spec's reach.

## Strengths

- **Responses-API compatibility is a distribution strategy, not a detail: products with existing Responses clients, SDKs, and stream parsers gain a harness lane with no client rewrite, which is the cheapest on-ramp any serving spec in this index offers.**
- The conformance suite is the definition of conformant, and servers that pass may say so with a version and class, which most young specs never operationalize.
- The three-artifact rule (spec, reference implementation, and suite move together) is a governance discipline that keeps specification sentences enforced.
- Coding-agent-native vocabulary: harnesses, bases, configured harnesses, skills, and MCP servers are first-class objects, so the spec reads like the stack this corpus covers rather than a generic model API.

## Cautions

- **Four spec versions in eight weeks and a same-day patch to the latest one mean the draft churn this category penalizes elsewhere is present here at full intensity, so pinning is a real cost.**
- The spec lives in the repo of the company that sells the hosted HarnessRouter service, with no foundation above the maintainer's UEP process, so the steward and the commercial winner are the same party.
- The community footprint is thin: one 10-point Show HN thread, no independent coverage found, and the one second implementation sits at 62 stars.
- The lane is contested: the LangChain Agent Protocol, every cloud provider's agent-serving API, and the Responses API itself all compete for the same integration surface.

## Pricing

The specification, the conformance suite, and HarnessRouter Community Edition are free and Apache-2.0.
The hosted HarnessRouter service is separately priced by HarnessRouter with a free tier (no figures cited here), and a conformant UHP server can run wholly on your own machine with your own keys, so hosting cost is optional by design.

## Compared to

- [Agent Protocol (LangChain)](../langchain-agent-protocol/index.md): **the serving-lane neighbor; the Agent Protocol standardizes runs, threads, and schemas for agents you serve, while UHP drives complete coding harnesses you already run and is deliberately Responses-compatible so existing clients keep working.**
- [ACP](../acp/index.md): editor-to-agent over local stdio for one editor session; UHP is application-to-server over HTTP for products that embed harnesses at distance.
- [Agent Host Protocol](../agent-host-protocol/index.md): both are client-to-infrastructure specs, but AHP synchronizes live session state across many clients while UHP dispatches tasks and retrieves artifacts.

## Bottom line

**Recommended for teams embedding coding-agent harnesses in their own products who want one HTTP contract across harness vendors and can absorb draft-version churn.**
Not for editor-hosted agent sessions, which is ACP's lane, and not for agent-to-agent delegation, which is A2A's.
My disagreeable claim: the Responses API already owns this lane by gravity, so the open question is not whether UHP's wire compatibility is right but whether one name, one conformance suite, and one governance doc can claim a surface the industry is otherwise treating as an OpenAI API extension.

## Changes

- 2026-10-08 - Created from the 2026-10-08 entrant scan (the harness-serving slot), with the four-versions-in-eight-weeks churn and the vendor-repo stewardship recorded as the central cautions.

## See also

- [Agent Protocol (LangChain)](../langchain-agent-protocol/index.md) - the other serving spec in this category, and UHP's closest comparison point
- [Agent Client Protocol (ACP)](../acp/index.md) - the editor-to-agent lane UHP deliberately does not occupy
- [Protocols Feature Matrix](../protocols-feature-matrix/index.md) - the category comparison this note joins as the twelfth column
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map of the harnesses UHP exists to drive

## References

- https://github.com/HarnessRouter/harnessrouter/tree/main/protocol - the spec home: current version 2026-10-04, draft-standard status, conformance suite, governance and versioning links
- https://unifiedharnessprotocol.org/ - the official site: version history (2026-08-11, 2026-09-12, 2026-09-28, 2026-10-04) and the specification chapters
- https://github.com/HarnessRouter/harnessrouter - repository facts: 2,920 stars, 296 forks, Apache-2.0, created 2026-08-09, pushed 2026-10-08 (GitHub API, as of 2026-10-08)
- https://raw.githubusercontent.com/HarnessRouter/harnessrouter/main/protocol/IMPLEMENTATIONS.md - the implementations page: HarnessRouter CE and hosted servers, SuperQode server and client, listing criteria
- https://raw.githubusercontent.com/HarnessRouter/harnessrouter/main/protocol/versions/2026-10-04/architecture.md - the Client/Server/Harness roles, the three conformance classes, and the configured-harness object model
- https://raw.githubusercontent.com/HarnessRouter/harnessrouter/main/protocol/GOVERNANCE.md - the UEP proposal-first process and the three-artifact rule
- https://raw.githubusercontent.com/HarnessRouter/harnessrouter/main/protocol/CHANGELOG.md - the spec-churn record: the 2026-10-04 same-day patch and the conformance-suite fixes through 2026-10-06
- https://github.com/SuperagenticAI/superqode - the second implementation, 62 stars, Apache-2.0 (GitHub API, as of 2026-10-08)
- https://harnessrouter.ai - the hosted service: sixteen harness bases behind the UHP contract, commercial with a free tier
- https://hn.algolia.com/api/v1/search?query=%22Unified%20Harness%20Protocol%22&tags=story - the footprint scan: zero stories naming the protocol, found 2026-10-08
- https://hn.algolia.com/api/v1/search?query=%22HarnessRouter%22 - the Show HN launch thread at 10 points (2026-08-17)
