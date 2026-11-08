---
title: A2UI
created: 2026-10-06
updated: 2026-11-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, protocols, generative-ui, frontend, google]
readability: 3
audience_notes: >
  Engineers building agent-driven product frontends who must pick a generative-UI format.
  Assumes you know what AG-UI, A2A, and MCP are, and what a component catalog is.
---

A2UI is Google's open, Apache-2.0 declarative format that lets agents describe rich user interfaces as data, which the client application renders from its own trusted component catalog instead of executing agent-generated code.

**A2UI owns the payload slot every other protocol in this index transports: agents speak MCP to tools, A2A to each other, and AG-UI to frontends, and A2UI is the bet for what an agent says when the answer is a UI, with Google products and Flutter's GenUI SDK already building on it.**

## What it is

A versioned specification suite published at a2ui.org (v1.0 current since 2026-11-06, with v0.9.1 and v0.9 previous and v0.8 deprecated) plus renderer libraries for Lit, Angular, Flutter, and Markdown, with React and SwiftUI on the roadmap.
An agent emits a flat, streaming list of JSON component descriptions with ID references, and the client maps each component to its own native widget, so the same payload renders on web, mobile, or desktop.
**The security model is the design's core: the client maintains a catalog of pre-approved components and the agent can only request components from that catalog, which the project summarizes as "safe like data, but expressive like code".**
Google created it and opened it on 2025-12-15, and the repository now lives in its own `a2ui-project` GitHub organization with contributions from the CopilotKit team.

## Status

**Active and adopted ahead of its spec maturity.**
The repository shows about 16,690 stars and 1,328 forks (as of 2026-10-13) with a push on 2026-11-08, roughly ten months after launch (GitHub API, as of 2026-11-08).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=a2ui-project/a2ui&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=a2ui-project/a2ui&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=a2ui-project/a2ui&type=date&legend=top-left" />
</picture>

The adoption is product-anchored: Google's Opal team is a core contributor and uses A2UI in its mini-app builder, Gemini Enterprise is integrating it, and Flutter's GenUI SDK (about 1,780 stars) uses A2UI as its declaration format between server-side agents and the app.
At the protocol layer, AG-UI documents A2UI as a supported generative-UI spec it natively carries, and A2A is a listed transport, so the two protocols above it in this index both move it.
The launch Show HN drew 164 points and 75 comments (2025-12-16), and the v1.0 specification, promoted to current on 2026-11-06, adds client-to-server action responses.
The implementation train is active on its own schedule: on 2026-10-17 the Python family split into separately versioned packages, with a2ui-core at v0.4.0 (cross-catalog `$ref` resolution), the agent SDK at v0.9.0 (breaking dependency bump), and the ADK and A2A bindings extracted into first releases (a2ui-adk v0.1.0, a2ui-a2a v0.1.0), so the agent SDK no longer depends on google-adk or the A2A SDK; on 2026-10-30 the developer CLI took its first tag (cli-v0.1.0), a typesafe component generator that emits Python client builders from catalog schemas across the 0.9, 0.9.1, and 1.0 protocol versions.
On 2026-11-02 the Python wave moved again: a2ui-core to v0.5.0 (breaking: a `DataContext` refuses a function whose `allowed_callers` is `agentOnly` before running it, as the v1.0 specification requires, and catalog-declared components without `ComponentId` or `ChildList` properties no longer infer child references), the agent SDK to v0.10.0 (breaking: v1.0 protocol messages carry the version as `'1.0'` without the `v` prefix, the file-resolve extension module was removed with the `httpx` dependency dropped, and data path assignments emit one targeted `updateDataModel` per path instead of overwriting the surface's whole data model), adding incremental streaming support for the Express inference format, and the ADK and A2A bindings to v0.2.0.
On 2026-10-26 the repository merged an MCP Apps bridge stream: a new `@a2ui/catalog-mcp` package with a `configureMcpCatalog` v1.0 entry point, an MCP Apps host bridge, and MCP App examples rendered in the Lit, Angular, and React explorers, alongside v1.0 protocol support in the Dart CLI and Python builder, so A2UI now ships tooling that treats MCP Apps as a neighbor to interoperate with rather than only a rival to position against.
On 2026-11-06 the spec hub promoted v1.0 to the current protocol version, ending the release-candidate period this note recorded since creation: the hub's table now reads v1.0 Current (which adds client-to-server RPC action responses and action IDs and renames `theme` to `surfaceProperties`, and which the project notes was previously designated as v0.10), v0.9.1 and v0.9 Previous, and v0.8 Deprecated.
The same 2026-11-05 to 11-06 wave added a user-facing a2ui agent skill and an llms.txt file for the docs site, merged the first SwiftUI renderer work (a HostedViewDriver, catalog factories, and accessibility and media-URL fixes, so SwiftUI is moving from the roadmap into the implementation tree), and redesigned the landing page; the tagged release train still ends at the 2026-11-02 Python wave, with 2026-11-04 release-prep commits for `a2ui_agent`, `a2ui_flutter`, and `a2ui_cli` not yet tagged; the 2026-11-07 and 11-08 pushes continue docs-site work (a Macros concept guide, the roadmap page rewritten as a gen-UI lifecycle loop, per-PR docs preview deployments and link checking), with nothing new tagged.

## Strengths

- **The catalog model answers the trust question that stops teams from letting agents emit UI: the agent proposes, the client's approved component set disposes.**
- Flat, streaming, ID-referenced JSON is deliberately LLM-friendly, so UIs build progressively instead of arriving as one fragile blob.
- One payload across Lit, Angular, and Flutter renderers keeps the format portable while the client keeps full styling control.
- Google ships it in its own products (Opal, Gemini Enterprise), so the spec is exercised by production surfaces rather than maintained as a paper exercise.

## Cautions

- **Spec churn is the price of admission: four versions in under a year, with v1.0 only promoted to current on 2026-11-06 after ten months of candidate status, and the README says to expect changes, so pinning is a cost.**
- No coding harness in this index speaks it; this is a product-frontend format, and its fate is tied to host adoption that has not reached the coding-agent world.
- The launch thread's recorded skepticism is about injection through generated UI and hallucinated interfaces, and the catalog constrains but does not eliminate that surface.
- Stewardship is Google-centered: unlike A2A, which Google donated to the Linux Foundation, A2UI stays in the a2ui-project organization with no foundation home.

## Pricing

Free and open, Apache-2.0, with nothing to buy.
The cost is maintaining a component catalog and renderer integration per host framework.

## Compared to

- [AG-UI](../ag-ui/index.md): **AG-UI is the transport, A2UI is the payload; AG-UI's docs list A2UI as a generative-UI spec it natively supports, so for agent-driven product UIs they compose rather than compete.**
- MCP Apps and MCP-UI: the iframe-and-resource model, where UI ships as opaque HTML in a sandbox; A2UI's native-first blueprint instead renders host components and inherits host styling, which is the sharpest line Google draws against it.
- Open-JSON-UI: OpenAI's open standardization of its internal ChatGPT-apps UI schema, platform-anchored where A2UI is cross-platform by design.

## Bottom line

**Recommended for teams building product frontends over agent backends who want rich, native-rendered UI without trusting agent-generated code.**
Not for editor-hosted coding agents, which is ACP's lane, and not for tool wiring, which is MCP's.
My disagreeable claim: A2UI will matter more to what end users see than AG-UI does, because whoever owns the payload format owns the interface, and the payload is where Google, OpenAI, and Microsoft are actually competing.

## Changes

- 2026-10-06 - Created from the 2026-10-06 entrant scan (the generative-UI payload slot), with the four-version spec churn and the single-org stewardship recorded as the central cautions.
- 2026-10-07 - Added the a2ui-project/a2ui star history chart to the Status section.
- 2026-10-10 - Recorded the Markdown renderer joining the official renderer list on the spec hub (v1.0 still candidate, v0.9.1 still current) and refreshed stars and forks as of 2026-10-10.
- 2026-10-17 - Recorded the 2026-10-17 Python package wave: a2ui-core v0.4.0 with cross-catalog `$ref` resolution, the agent SDK's breaking move to v0.9.0, and the ADK and A2A bindings extracted into first releases (a2ui-adk v0.1.0, a2ui-a2a v0.1.0); the spec hub's version table re-verified unchanged (v0.9.1 current, v1.0 candidate).
- 2026-10-22 - Rotation re-verification: every cited URL re-fetched live with no dead sources, the spec hub's version table re-confirmed (v0.9.1 current production, v1.0 release candidate), the 2026-10-17 Python package wave still the newest release set, and the launch-thread figures re-checked (164 points); the repository pushed 2026-10-22.
- 2026-10-24 - Re-verification: the repository pushed 2026-10-24 with the release train unchanged (the 2026-10-17 Python wave still the newest set) and the spec hub's version table re-confirmed (v0.9.1 current production, v1.0 release candidate).
- 2026-10-25 - Re-verification: the repository pushed 2026-10-25 with the tagged release train unchanged (the 2026-10-17 Python wave still the newest set) and the spec hub's version table re-confirmed (v0.9.1 current production, v1.0 release candidate).
- 2026-10-27 - Re-verification: the repository pushed 2026-10-26/27 with an MCP Apps bridge stream merged to main (the `@a2ui/catalog-mcp` package with a `configureMcpCatalog` v1.0 entry point, an MCP Apps host bridge, and MCP App examples in the Lit, Angular, and React explorers) plus v1.0 protocol support in the Dart CLI and Python builder, while the tagged release train stays at the 2026-10-17 Python wave and the spec hub's version table stays at v0.9.1 current with v1.0 a release candidate.
- 2026-10-31 - The tagged release train moved past the 2026-10-17 Python wave with the A2UI CLI's first release (cli-v0.1.0, 2026-10-30), a typesafe component generator that emits Python client builders from catalog schemas across protocol versions 0.9, 0.9.1, and 1.0; the spec hub's version table is unchanged (v0.9.1 current production, v1.0 release candidate).
- 2026-11-03 - The Python wave moved again on 2026-11-02: a2ui-core to v0.5.0 and the agent SDK to v0.10.0, both carrying breaking changes (the agentOnly-callable refusal the v1.0 specification requires in core; the version-string format, the file-resolve removal, and per-path `updateDataModel` emission in the SDK, which also gained incremental Express streaming), with the ADK and A2A bindings at v0.2.0; the spec hub's version table is unchanged (v0.9.1 current production, v1.0 release candidate).
- 2026-11-04 - Re-verification: the repository pushed 2026-11-04 on docs-site work (a Messages protocol concept page, preview-site header fixes, and a landing-page demo of incremental mobile chat UI generation) with the tagged release train unchanged (the 2026-11-02 Python wave still the newest set) and the spec hub's version table re-confirmed (v0.9.1 current production, v1.0 release candidate).
- 2026-11-06 - The spec hub promoted v1.0 to the current protocol version, ending the release-candidate period the note recorded since creation: the table now reads v1.0 Current (client-to-server RPC action responses and action IDs, the `theme` to `surfaceProperties` rename, previously designated as v0.10), v0.9.1 and v0.9 Previous, and v0.8 Deprecated; the same wave added an a2ui agent skill and docs llms.txt, merged the first SwiftUI renderer work, and redesigned the landing page, while the tagged release train stays at the 2026-11-02 Python wave; the What-it-is suite list, the Status section, and the churn caution moved with the promotion.
- 2026-11-08 - Re-verification: the repository pushed 2026-11-08 on docs-site work (a Macros concept guide, the roadmap page rewritten as a gen-UI lifecycle loop, per-PR docs preview deployments and link checking) with the tagged release train unchanged (the 2026-11-02 Python wave still the newest set) and the spec hub's version table re-confirmed (v1.0 current, v0.9.1 previous).

## See also

- [Agent User Interaction Protocol (AG-UI)](../ag-ui/index.md) - the event-stream transport that natively carries A2UI payloads
- [Agent2Agent Protocol (A2A)](../a2a/index.md) - the cross-organization transport A2UI messages ride to remote agents
- [Model Context Protocol (MCP)](../mcp/index.md) - whose MCP Apps extension is the iframe-based alternative for agent UI
- [Protocols Feature Matrix](../protocols-feature-matrix/index.md) - the category comparison this note joins as the eighth column

## References

- https://github.com/a2ui-project/a2ui - repository: 16,688 stars, 1,328 forks, Apache-2.0, pushed 2026-10-14 (GitHub API, as of 2026-10-13)
- https://raw.githubusercontent.com/google/A2UI/main/README.md - early-stage status, v0.9.1 production and v1.0 release candidate, the catalog security model, renderer list
- https://a2ui.org/ - spec hub: version table (v1.0 Current, v0.9.1 Previous, v0.9 Previous, v0.8 Deprecated), Google and CopilotKit contribution note, re-fetched 2026-11-06
- https://api.github.com/repos/a2ui-project/a2ui/releases - the release train: the 2026-11-02 Python wave (a2ui-core v0.5.0, agent SDK v0.10.0, a2ui-adk v0.2.0, a2ui-a2a v0.2.0) after the 2026-10-17 wave
- https://api.github.com/repos/a2ui-project/a2ui/commits?since=2026-10-25T00:00:00Z - the 2026-10-26/27 push wave: the MCP Apps bridge stream (`@a2ui/catalog-mcp`, the host bridge, the explorer examples) and the v1.0 builder support
- https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/ - launch announcement (2025-12-15): Opal, Gemini Enterprise, Flutter GenUI, and CopilotKit collaborators, and the MCP Apps and ChatKit positioning
- https://hn.algolia.com/api/v1/items/46286407 - launch thread, 164 points and 75 comments (2025-12-16), the injection and hallucination skepticism
- https://docs.ag-ui.com/concepts/generative-ui-specs - the generative-UI spec landscape (A2UI, Open-JSON-UI, MCP-UI) and AG-UI's native support for all three
- https://api.github.com/repos/flutter/genui - Flutter GenUI SDK, 1,780 stars, the Flutter-side adoption evidence (as of 2026-10-06)
