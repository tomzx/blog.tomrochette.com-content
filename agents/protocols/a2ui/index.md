---
title: A2UI
created: 2026-10-06
updated: 2026-10-07
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

A versioned specification suite published at a2ui.org (v0.8 legacy, v0.9 stable, v0.9.1 current production, v1.0 release candidate) plus renderer libraries for Lit, Angular, and Flutter, with React and SwiftUI on the roadmap.
An agent emits a flat, streaming list of JSON component descriptions with ID references, and the client maps each component to its own native widget, so the same payload renders on web, mobile, or desktop.
**The security model is the design's core: the client maintains a catalog of pre-approved components and the agent can only request components from that catalog, which the project summarizes as "safe like data, but expressive like code".**
Google created it and opened it on 2025-12-15, and the repository now lives in its own `a2ui-project` GitHub organization with contributions from the CopilotKit team.

## Status

**Active and adopted ahead of its spec maturity.**
The repository shows about 16,600 stars and 1,322 forks with a push on 2026-10-06, roughly ten months after launch, all as of 2026-10-06 (GitHub API).

[![Star History Chart](https://api.star-history.com/chart?repos=a2ui-project/a2ui&type=date&legend=top-left)](https://www.star-history.com/?repos=a2ui-project%2Fa2ui&type=date&legend=top-left)

The adoption is product-anchored: Google's Opal team is a core contributor and uses A2UI in its mini-app builder, Gemini Enterprise is integrating it, and Flutter's GenUI SDK (about 1,780 stars) uses A2UI as its declaration format between server-side agents and the app.
At the protocol layer, AG-UI documents A2UI as a supported generative-UI spec it natively carries, and A2A is a listed transport, so the two protocols above it in this index both move it.
The launch Show HN drew 164 points and 75 comments (2025-12-16), and the v1.0 specification is a release candidate that adds client-to-server action responses.

## Strengths

- **The catalog model answers the trust question that stops teams from letting agents emit UI: the agent proposes, the client's approved component set disposes.**
- Flat, streaming, ID-referenced JSON is deliberately LLM-friendly, so UIs build progressively instead of arriving as one fragile blob.
- One payload across Lit, Angular, and Flutter renderers keeps the format portable while the client keeps full styling control.
- Google ships it in its own products (Opal, Gemini Enterprise), so the spec is exercised by production surfaces rather than maintained as a paper exercise.

## Cautions

- **Spec churn is the price of admission: four versions in under a year, v1.0 still a release candidate, and the README says to expect changes, so pinning is a cost.**
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

## See also

- [Agent User Interaction Protocol (AG-UI)](../ag-ui/index.md) - the event-stream transport that natively carries A2UI payloads
- [Agent2Agent Protocol (A2A)](../a2a/index.md) - the cross-organization transport A2UI messages ride to remote agents
- [Model Context Protocol (MCP)](../mcp/index.md) - whose MCP Apps extension is the iframe-based alternative for agent UI
- [Protocols Feature Matrix](../protocols-feature-matrix/index.md) - the category comparison this note joins as the eighth column

## References

- https://github.com/a2ui-project/a2ui - repository: 16,597 stars, 1,322 forks, Apache-2.0, pushed 2026-10-06 (GitHub API, as of 2026-10-06)
- https://raw.githubusercontent.com/google/A2UI/main/README.md - early-stage status, v0.9.1 production and v1.0 release candidate, the catalog security model, renderer list
- https://a2ui.org/ - spec hub: version table (v1.0 Candidate, v0.9.1 Current, v0.9 Stable, v0.8 Legacy), Google and CopilotKit contribution note
- https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/ - launch announcement (2025-12-15): Opal, Gemini Enterprise, Flutter GenUI, and CopilotKit collaborators, and the MCP Apps and ChatKit positioning
- https://hn.algolia.com/api/v1/items/46286407 - launch thread, 164 points and 75 comments (2025-12-16), the injection and hallucination skepticism
- https://docs.ag-ui.com/concepts/generative-ui-specs - the generative-UI spec landscape (A2UI, Open-JSON-UI, MCP-UI) and AG-UI's native support for all three
- https://api.github.com/repos/flutter/genui - Flutter GenUI SDK, 1,780 stars, the Flutter-side adoption evidence (as of 2026-10-06)
