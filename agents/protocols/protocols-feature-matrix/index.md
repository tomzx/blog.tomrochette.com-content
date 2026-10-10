---
title: "Protocols Feature Matrix"
created: 2026-08-24
updated: 2026-10-09
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, protocols, interoperability]
readability: 3
audience_notes: >
  Engineers deciding which agent protocols to adopt or skip who need the governance, maturity, and adoption deltas at a glance.
  Assumes you know what JSON-RPC, stdio, and a repository instruction file are; each column links to a full note with sources.
---

This matrix compares the twelve protocols profiled in this section, A2UI, ACP, Agent Host Protocol, ANP, Agent Protocol (LangChain), AG-UI, A2A, AGENTS.md, llms.txt, MCP, Unified Harness Protocol (UHP), and WebMCP, so the whole interoperability stack can be read in one table.

**The twelve do not compete, they stack (repo-to-agent, editor-to-agent, agent-to-frontend, agent-to-tool, agent-to-agent, client-to-session, app-to-agent serving, open-web identity and discovery, site content discovery, UI payload, browser tool exposure), and adoption falls with every step up that stack, which is why I call AGENTS.md and MCP defaults, ACP a rising bet, AG-UI the quiet winner by raw download volume, AHP a bet underwritten by VS Code's own distribution, A2UI the payload format the frontend layer is converging on, the Agent Protocol the serving API waiting for a second implementation, UHP the Responses-compatible draft claiming the harness side of that same serving lane, llms.txt the docs-side convention search refuses to honor, WebMCP the browser bet only one browser ships, A2A an enterprise convention the coding-agent world can keep ignoring, and ANP the decentralized open-web bet the market has not bought yet.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

|  Feature  |  [A2A](../a2a/index.md)  |  [A2UI](../a2ui/index.md)  |  [ACP](../acp/index.md)  |  [AG-UI](../ag-ui/index.md)  |  [Agent Host Protocol](../agent-host-protocol/index.md)  |  [Agent Protocol (LangChain)](../langchain-agent-protocol/index.md)  |  [AGENTS.md](../agents-md/index.md)  |  [ANP](../anp/index.md)  |  [llms.txt](../llms-txt/index.md)  |  [MCP](../mcp/index.md)  |  [Unified Harness Protocol (UHP)](../uhp/index.md)  |  [WebMCP](../webmcp/index.md)  |
|  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |  ---  |
|  Kind  |  wire protocol  |  declarative UI payload format  |  wire protocol  |  wire protocol  |  wire protocol  |  REST/OpenAPI serving spec  |  file convention  |  wire protocol suite  |  file convention  |  wire protocol  |  HTTP serving spec  |  browser API standard  |
|  Originated by  |  Google (2025-04)  |  Google (2025-12)  |  Zed, with JetBrains  |  CopilotKit (2025-05)  |  Microsoft (2026-03)  |  LangChain (2024-11)  |  OpenAI-led (2025-08)  |  community working group (2024-10)  |  Jeremy Howard, Answer.AI (2024-09)  |  Anthropic (2024-11)  |  HarnessRouter (2026-08)  |  Microsoft and Google engineers, W3C Web ML CG (2026-02)  |
|  Steward  |  AAIF (2026-08), TSC  |  Google, a2ui-project org, no foundation  |  vendor-neutral org  |  CopilotKit, no foundation  |  Microsoft, no foundation  |  LangChain, no foundation  |  AAIF  |  community working group, no foundation  |  Answer.AI author-driven, no foundation  |  AAIF  |  HarnessRouter, no foundation (maintainer-led UEP process)  |  W3C Web Machine Learning Community Group  |
|  Spec license  |  Apache-2.0  |  Apache-2.0  |  Apache-2.0  |  MIT  |  MIT  |  MIT  |  MIT  |  Apache-2.0  |  none stated  |  MIT  |  Apache-2.0  |  W3C CG terms  |
|  Maturity  |  v1.0.1 (2026-05)  |  v0.9.1 production, v1.0 release candidate  |  version 1, v2 draft, remote WIP  |  packages 1.0.2 (2026-10-05), spec 1.0  |  v1.0.0 (2026-10-02)  |  OpenAPI 0.1.6, active  |  unversioned, de facto standard  |  specs 1.2 latest (1.0, 1.1 archived), two drafts open  |  v2 (2026-08), v1 (2024-09)  |  dated revisions (2026-07-28)  |  draft standard 2026-10-04 (fourth version since 2026-08)  |  CG draft (2026-10-08), Chrome origin trial 149 to 156  |
|  What it connects  |  agent-to-agent  |  agent-to-frontend UI payload  |  editor-to-agent  |  agent-to-frontend  |  client-to-session  |  app-to-agent serving  |  repo-to-agent  |  agent-to-agent, open-web  |  site-to-agent content discovery  |  app-to-tools  |  app-to-harness serving  |  site-to-agent tool exposure  |
|  Adoption in this section  |  ~ via the official CLI and skill (2026-10-01), none native  |  ✗ none native (carried by AG-UI and A2A transports)  |  ~ growing (OpenCode, JetBrains, Zed)  |  ✗ none native (CopilotKit ecosystem outside this index)  |  ~ VS Code reference host  |  ✗ none native (LangChain ecosystem only)  |  ~ most; Claude Code shipped native support 2026-09-18  |  ✗ none native (MCP bridge exists)  |  ~ docs surfaces in this index serve it; required by none  |  ✓ near-universal  |  ✗ none native (harnesses are the driven party)  |  ✗ none native (browser lane outside this index)  |
|  Transport or location  |  HTTP, gRPC, JSON-RPC  |  streaming JSONL component list over A2A or AG-UI  |  JSON-RPC over stdio  |  SSE, WebSockets, webhooks  |  URI channels on a standalone sessions server  |  REST over HTTPS, runs, threads, and agents endpoints  |  Markdown at repo root  |  HTTPS, DID documents, messaging profiles  |  Markdown at site or path root, HTTP Link headers  |  JSON-RPC, stdio to sse  |  HTTPS, SSE streaming, Responses-compatible request body  |  document.modelContext browser API, no wire transport  |
|  Official SDKs  |  ✓ six  |  ✓ Lit, Angular, and Flutter renderers, Python and TS packages  |  ✓ five  |  ✓ three first-party, seven community  |  ✓ six  |  ✓ Python server stubs and TS bindings  |  ✗ none needed  |  ~ community SDKs and an MCP bridge  |  ✓ Python and JavaScript tooling, community generators  |  ✓ any language  |  ~ OpenAPI 3.1 schema plus a runnable conformance suite, no first-party SDKs  |  ✗ none needed (web platform API)  |
|  Criticism recorded  |  redundant with MCP  |  spec churn, Google stewardship, injection through generated UI  |  sprawl, flattened UX  |  single-vendor origin, pre-1.0 churn  |  more sprawl, one vendor's governance  |  one company stewards spec and commercial superset, missing community footprint, name collision with the 2023 spec  |  weak efficacy evidence  |  near-zero adoption, complexity  |  search engines ignore it, author-driven governance, adjacent conventions fragment  |  tool poisoning, supply chain  |  four spec versions in eight weeks, one vendor's repo-first governance, thin community footprint  |  one browser ships it, mid-year API rename and October removal of the declarative path, open security risks  |

## Reading the matrix

**Governance converged faster than adoption, and every protocol that went neutral did so only after it had already won or stalled.**
Google donated A2A to the Linux Foundation in June 2025, Anthropic and OpenAI donated MCP and AGENTS.md to the AAIF the same day (2025-12-09), and A2A itself joined the AAIF as a Growth Stage project on 2026-08-27, so three of the twelve now sit in the same foundation.
ACP is stewarded by Zed and JetBrains under a vendor-neutral organization with no foundation home, AHP stays inside the `microsoft` org with repo-first governance, AG-UI remains closest to its corporate parent, CopilotKit, which also sells commercial support for it, ANP has no governance above its working group, the Agent Protocol is stewarded by the same LangChain that sells its commercial superset, UHP is maintained in the HarnessRouter repository under the maintainer's own UEP process while the same vendor sells the hosted implementation, llms.txt remains author-driven at Answer.AI with no conformance process, and A2UI stays with Google's a2ui-project organization, while WebMCP is the one newer column with a neutral home in the W3C Community Group process, so the stack now has eight non-foundation columns, and ACP remains the one compounding fastest in editors.
I read this as governance following adoption, not causing it.

**Adoption falls as the protocol climbs the stack, and the file convention beat every wire protocol to default status.**
MCP is table stakes across the harness and surface matrices; AGENTS.md counts more than 60,000 carrying projects, and its one glaring holdout closed on 2026-09-18 when Claude Code shipped native support in 2.1.277; ACP rides OpenCode, JetBrains, Zed, and a Copilot CLI preview; A2A has no native speaker among this index's harnesses, only community setups near Gemini CLI plus the official CLI and agent skill the project shipped on 2026-10-01; AHP is just over six months old with 396 stars and a fresh 1.0.0 spec (2026-10-02) as of 2026-10-09, and its reference host ships inside VS Code while the VS Code team has said publicly it is rebuilding its agent infrastructure on the protocol.
The SDK download ratio recorded in the A2A note, about 11.4M monthly versus about 235M for MCP as of 2026-10-07, is the gap in one number, and AHP's roughly 878k combined downloads (about 283.1k crates plus 595.4k npm) show the same order-of-magnitude distance from the top.
The Agent Protocol sits with the young serving specs: 684 stars, active through 2026-10-07, with LangGraph Platform as its one commercial implementation and no independent adopter in this index.
UHP is the newest serving bet: the spec ships inside HarnessRouter's 2,941-star repository (as of 2026-10-09), the hosted service and SuperQode's 62-star framework are the recorded implementations, and its discussion footprint is one 10-point Show HN thread with zero stories naming the protocol itself.
llms.txt splits the file-convention lane with AGENTS.md: thousands of sites and the docs of tools in this index serve it (Anthropic's and OpenAI's developer docs confirmed live this run), coding agents fetch it, and the search crawlers its SEO adopters hoped for still ignore it.
AG-UI is the anomaly that proves the rule: none of this index's harnesses or surfaces speak it natively, yet its SDKs moved about 15.9M combined npm downloads in the month ending 2026-10-07, because the frontend layer is where end-user products live even though coding tools never touch it.
A2UI is the newest layer to fill in: launched in December 2025, it passed 16,600 stars in ten months and is carried by Google's own Opal and Gemini Enterprise plus Flutter's GenUI SDK, adoption that outruns its release-candidate spec.
WebMCP sits at the browser edge: 4,499 stars, a Chrome origin trial, and Shopify and Cloudflare turning it default-on across much of commerce in August 2026, while Gemini in Chrome remains the only agent consuming those tools at scale.
ANP sits below even A2A: 1.4k stars after two years and Hacker News stories at 2 and 1 points are the footprint of a protocol whose network effect has not started.

**The consolidations the notes record happened in opposite corners, and neither touched the other's territory.**
IBM's Agent Communication Protocol (the other ACP, the source of the name collision) merged into A2A in August 2025 under LF AI and Data.
JetBrains folded its internal Junie protocol into the Agent Client Protocol instead.
Both mergers cut the rival count in 2025 while leaving the enterprise-remote and local-editor layers separate.

**Each recorded criticism is a different species of doubt, and the pattern favors the incumbents.**
MCP is criticized for risks it creates (tool poisoning, rug pulls, a 10,000-server supply chain); AGENTS.md for whether it helps at all (an ETH Zurich study found no success-rate gain and over 20% added inference cost, against Vercel's counter-evidence); ACP for UX flattening and protocol sprawl; AHP for being a fifth protocol to track under one vendor's governance; A2A for whether it should exist at all; AG-UI for provenance and maturity, a CopilotKit-originated stack that only graduated to 1.0.0 packages on 2026-09-17 and whose adoption story lives in vendor blogs; A2UI for spec churn and Google stewardship, four versions in under a year with no foundation home; WebMCP for shipping in one browser under a draft that renamed its central API mid-year; ANP for building infrastructure for a network that does not exist yet; the Agent Protocol for a community footprint that has not started and one company holding both spec and commercial superset; UHP for four versions in eight weeks under the stewarding vendor's own repository; and llms.txt for being ignored by the search crawlers its SEO adopters expected and governed by nobody but its author.
The mature protocols get attacked for their risks, the young ones for their reason to exist or their provenance.

## Choosing from the matrix

- Exposing tools or data to any agent: MCP, the default with a supply-chain asterisk.
- Choosing harness and editor independently: ACP, the cheapest portability insurance in the stack.
- Streaming an agent into a product frontend: AG-UI, accepting CopilotKit's stewardship and dated-release churn (1.0.0 only landed 2026-09-17).
- Rendering agent-generated UI natively and safely in your own product: A2UI, pinned to v0.9.1 until the v1.0 candidate lands.
- Making a public website's features callable by browser agents: WebMCP, accepting Chrome-only reach and draft-status churn today.
- Serving your own agents behind a conventional runs-and-threads API: the Agent Protocol, accepting LangChain stewardship and a thin adopter base.
- Driving complete coding-agent harnesses from your own product over HTTP: UHP, accepting draft-version churn and HarnessRouter stewardship while the conformance suite keeps implementations verifiable.
- Making a docs surface readable by agents: publish llms.txt with the v2 link headers, and expect nothing from search crawlers.
- Any repository an agent touches: commit a short AGENTS.md, commands and conventions first.
- Delegating work across vendors or departments: A2A, provided both sides run enterprise platforms.
- Betting on open-web agent discovery before platforms mediate everything: ANP, as a research bet, not a production choice.
- Attaching a second client to a live agent session: AHP, provided v1.0.0's short track record and Microsoft's stewardship are acceptable.
- Wiring sub-agents inside one framework: none of these, native primitives or MCP are simpler.

## Changes

- 2026-08-24 - Created with the stacking thesis and recorded protocol consolidations.
- 2026-09-16 - Extended from five to six columns with AG-UI, re-sorted alphabetically, and updated the governance, adoption, criticism, and choosing prose for the agent-to-frontend layer.
- 2026-09-18 - AG-UI maturity cell updated to 1.0.0 packages and a published 1.0 specification, and stars and download figures refreshed in the AG-UI and AHP prose.
- 2026-09-21 - AGENTS.md adoption cell updated after Claude Code shipped native support in 2.1.277 (2026-09-18), ending the holdout the cell recorded; AG-UI and AHP download and star figures refreshed in the prose.
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-24 - Re-verification: refreshed star and download figures in the AG-UI and AHP prose (AG-UI about 12.0M combined monthly downloads, AHP 363 stars and roughly 369k combined downloads).
- 2026-09-25 - Re-sorted the columns by member title (ACP and Agent Host Protocol precede A2A under the case-insensitive title ordering the other matrices use); no cell content changed.
- 2026-09-27 - Re-verification: refreshed the AG-UI and AHP figures in the prose (AG-UI about 12.9M combined monthly downloads, AHP 368 stars and roughly 410k combined downloads); no cells changed.
- 2026-09-29 - Re-verification: refreshed the AG-UI and AHP figures in the prose (AG-UI about 12.3M combined monthly downloads, AHP 375 stars and roughly 433k combined downloads); no cells changed.
- 2026-09-29 - Re-sorted the columns to the section-wide case-insensitive title sort (A2A, ACP, AG-UI, Agent Host Protocol, AGENTS.md, MCP), correcting the 2026-09-25 arrangement that had placed ACP and Agent Host Protocol ahead of A2A and AG-UI; the category page list was brought to the same order in the same run; no cell content changed.
- 2026-10-02 - Re-verification: refreshed the AG-UI and AHP figures in the prose (AG-UI about 13.1M combined monthly downloads, AHP 382 stars and roughly 597k combined downloads); no cells changed.
- 2026-10-03 - AHP maturity cell moved to v1.0.0 (2026-10-02) and the AG-UI maturity cell to packages 1.0.1 (2026-09-29), with star and download figures refreshed in the prose (AG-UI about 14.6M combined monthly downloads, AHP 384 stars and roughly 681k combined downloads).
- 2026-10-05 - Extended from six to seven columns with ANP (the community DID-based agent-interop suite), inserted in sorted position between AGENTS.md and MCP and traced to the new note; the intro, reading, and choosing sections updated for the seventh protocol; AG-UI and AHP figures refreshed in the prose (AG-UI about 15.0M combined monthly downloads, AHP 386 stars and roughly 733k combined downloads).
- 2026-10-06 - Extended from seven to nine columns with A2UI (Google's declarative generative-UI payload format) and WebMCP (the W3C browser tool-exposure draft), inserted in sorted positions and traced to the new notes; the A2A adoption cell moved to record the official CLI and agent skill (2026-10-01) and the AG-UI maturity cell to packages 1.0.2 (2026-10-05); the intro, governance, adoption, criticism, and choosing sections updated for the two new protocols; AG-UI and AHP figures refreshed in the prose (AG-UI about 14.8M combined monthly downloads, AHP 390 stars and roughly 823k combined downloads).
- 2026-10-07 - Extended from nine to eleven columns with Agent Protocol (LangChain) (the REST/OpenAPI serving spec) and llms.txt (the site-content-discovery convention, now at v2), inserted in sorted positions and traced to the new notes; the AHP figures in the prose refreshed to 392 stars and roughly 848k combined downloads, the A2A-versus-MCP download ratio to about 11.4M versus about 235M as of 2026-10-07, and the WebMCP star count to 4,478; the intro, governance, adoption, criticism, and choosing sections updated for the two new members.
- 2026-10-08 - Extended from eleven to twelve columns with Unified Harness Protocol (UHP) (the Responses-compatible harness-serving draft), inserted in sorted position between MCP and WebMCP and traced to the new note; the intro, governance, adoption, criticism, and choosing sections updated for the twelfth protocol; figures refreshed in the prose (AHP 392 stars and roughly 852k combined downloads, the Agent Protocol active through 2026-10-07, WebMCP 4,487 stars).
- 2026-10-09 - Re-sorted the columns alphabetically by member title, case-insensitive, moving A2A from the founding first position to its title-sorted place; no cell content changed.
- 2026-10-09 - WebMCP's maturity cell moved to the draft revision of 2026-10-08 and its criticism cell records the same-day removal of the declarative path; the intro's protocol-name list was brought to the column order and its eleven count corrected to twelve; figures refreshed in the prose (AG-UI about 15.9M combined downloads in the month ending 2026-10-07, AHP 396 stars and roughly 878k combined downloads, WebMCP 4,499 stars, HarnessRouter 2,941 stars); no membership change.

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
- https://github.com/ag-ui-protocol/ag-ui - repository facts (16,403 stars, MIT, created 2025-05-07, pushed 2026-10-08) for the AG-UI column (GitHub API, as of 2026-10-09)
- https://raw.githubusercontent.com/ag-ui-protocol/ag-ui/main/README.md - origin by CopilotKit, around 16 event types, transports, and integration tables for the AG-UI column
- https://docs.ag-ui.com - TypeScript, Python, and .NET SDKs and the published 1.0 specification for the AG-UI column
- https://api.npmjs.org/downloads/point/last-month/@ag-ui/core - 9,710,636 downloads in the month ending 2026-10-07 for the adoption paragraph
- https://api.npmjs.org/downloads/point/last-month/@ag-ui/client - 6,175,767 downloads in the month ending 2026-10-07 for the adoption paragraph
- https://github.com/langchain-ai/agent-protocol - repository facts (684 stars, MIT, created 2024-11-12, pushed 2026-10-02) for the Agent Protocol column (GitHub API, as of 2026-10-07)
- https://raw.githubusercontent.com/langchain-ai/agent-protocol/main/README.md - purpose, LangGraph Platform superset, and implementations for the Agent Protocol column
- https://langchain-ai.github.io/agent-protocol/openapi.json - the OpenAPI document (v0.1.6, agents, threads, and runs endpoints) for the Agent Protocol maturity and transport cells
- https://github.com/a2ui-project/a2ui - repository facts (16,603 stars, Apache-2.0, pushed 2026-10-07) for the A2UI column (GitHub API, as of 2026-10-07)
- https://a2ui.org/ - the spec version table (v1.0 Candidate, v0.9.1 Current, v0.9 Stable, v0.8 Legacy) for the A2UI maturity cell
- https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/ - the A2UI launch and partner list for the adoption paragraph
- https://webmachinelearning.github.io/webmcp/ - the Draft Community Group Report (2026-10-08 revision) behind the WebMCP column
- https://developer.chrome.com/docs/ai/webmcp - the Chrome origin trial status for the WebMCP maturity cell
- https://nohacks.co/blog/what-is-webmcp - the Shopify and Cloudflare default-on record and browser-support table for the WebMCP adoption and criticism cells
- https://llmstxt.org/ - the llms.txt spec site (author, published 2024-09-03, modified 2026-08-10) for the llms.txt column
- https://llmstxt.org/changes.html - the v2 changes (August 2026) behind the llms.txt maturity cell
- https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/ - the Google dismissal behind the llms.txt criticism cell
- https://docs.anthropic.com/llms.txt - the served-file adoption evidence for the llms.txt adoption cell
- https://agents.md - format, nested scoping, and adoption count for the AGENTS.md column
- https://github.com/agent-network-protocol/AgentNetworkProtocol - repository facts (1,441 stars, Apache-2.0, created 2024-10-23, pushed 2026-10-01) for the ANP column (GitHub API, as of 2026-10-07)
- https://agent-network-protocol.com/ - the ANP spec hub (ANP 1.2 latest, 1.0 and 1.1 archived, messaging profiles) for the ANP column
- https://hn.algolia.com/api/v1/search?query=%22Agent%20Network%20Protocol%22&tags=story - the adoption-footprint scan behind the ANP column's criticism cell
- https://aaif.io/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agents-md/ - same-day AAIF donations of MCP and AGENTS.md
- https://modelcontextprotocol.io/specification/latest - spec revision 2026-07-28 for the MCP column
- https://arxiv.org/abs/2602.11988 - the efficacy critique in the AGENTS.md column
- https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks - the tool poisoning critique in the MCP column
