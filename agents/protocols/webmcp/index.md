---
title: WebMCP
created: 2026-10-06
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, protocols, browser, w3c, agent-tools]
readability: 3
audience_notes: >
  Web engineers deciding whether to expose their application's features as callable tools for AI agents,
  and agent engineers tracking where browser-native tool discovery is heading.
  Assumes you know what MCP and a JSON Schema are.
---

WebMCP is a W3C Community Group draft specification, edited by Microsoft and Google engineers, that lets a web page expose its features as structured, callable tools through a `document.modelContext` browser API, so the page itself acts like an MCP server implemented in client-side script.

**WebMCP inverts agent actuation the way AGENTS.md inverted repo instructions: the site declares what it can do instead of the agent reverse-engineering the interface, and since August 2026 the supply side went default-on across much of commerce through Shopify and Cloudflare while the demand side is still essentially one browser's agent, which is the bet's actual state.**

## What it is

A Draft Community Group Report (dated 2026-10-08, revised from the 2026-10-02 draft) from the W3C Web Machine Learning Community Group, first announced 2026-02-10, with editors from Microsoft and Google.
The API surface is `document.modelContext` with `registerTool()`, `getTools()`, and `executeTool()`: a tool carries a name, a natural-language description, and a JSON Schema input, and pages register tools imperatively in JavaScript.
**The spec's own framing places it in this index's stack: "Web pages that use WebMCP can be thought of as Model Context Protocol servers that implement tools in client-side script instead of on the backend", with the browser mediating every call under a `tools` Permissions Policy that defaults to same-origin only.**
Chrome ships it behind a public origin trial (Chrome 149 through 156) plus a local flag, and Angular offers experimental support.

## Status

**Active and past the flag stage, with one browser shipping and one agent consuming.**
The repository shows 4,499 stars and 123 open issues with a push on 2026-10-08, all as of 2026-10-09 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=webmachinelearning/webmcp&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=webmachinelearning/webmcp&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=webmachinelearning/webmcp&type=date&legend=top-left" />
</picture>

The Chrome origin trial opened with Chrome 149 (Intent to Experiment filed 2026-05-15), Puppeteer added native WebMCP support in v24.41.0, and Google's Chrome team presented the API alongside its agent browser work at I/O 2026.
In August 2026 the supply side jumped: Shopify switched WebMCP on for every Liquid storefront (catalog, cart, checkout, and policy tools) and Cloudflare made it available to any Cloudflare-fronted site with no code change.
The demand side did not move with it: Gemini in Chrome remains the main agent actually calling the tools, Microsoft co-authored the spec but Edge's 147 release notes list no WebMCP support, and Firefox and Safari have given no public signal.

## Strengths

- **The browser stays in the middle of every call: the API is gated behind the `tools` permissions policy with a same-origin default allowlist, and pages get `ToolActivatedEvent` and `ToolCancelEvent` visibility into what agents invoke.**
- **The imperative path stayed small through the churn: a tool is a name, a natural-language description, and a JSON Schema input, and pages register tools imperatively in JavaScript.**
- Multi-vendor authorship inside a standards body (Microsoft and Google together) rather than a single company's repo-first spec.
- Chrome ships the adoption machinery: origin trial, demos, an inspector extension, security guidance, and evals, not just a proposal page.

## Cautions

- **One browser ships it and one agent consumes it: a storefront that enables WebMCP today is writing against Chrome's roadmap, not a standard.**
- The API renamed itself mid-year (`window.agent`, then `navigator.modelContext`, now `document.modelContext`, deprecated in Chromium 150), the spec is a Community Group draft, not a W3C standard-track document, and the 2026-10-08 revision removed the declarative form-annotation API "for now" (issue #338), so a page that adopted the form path has no standard to lean on.
- The spec's own security section catalogs tool poisoning, output injection, over-parameterization privacy leakage, and same-origin violations as open risks, with mitigations still marked as approaches rather than solved problems.
- The supply-and-demand mismatch is the practical trap: millions of pages gained tool surfaces in a week, while the population of agents able to call them stayed near one.

## Pricing

Free, an open specification with nothing to buy.
The cost is designing, implementing, and maintaining a tool surface per site, plus tracking a draft that has already renamed its central API.

## Compared to

- [MCP](../mcp/index.md): **server-side tool exposure for agents you operate; WebMCP is the browser-tab cousin for sites you visit, and the spec explicitly models a page as an MCP server in client-side script.**
- llms.txt: the identity-file bet versus the capability bet, a static description of who you are against callable tools; Google's John Mueller called llms.txt "purely speculative for now" and pointed developers at WebMCP.
- [AG-UI](../ag-ui/index.md): streams agent events into a frontend you build, while WebMCP exposes tools from a site you visit, so they meet at the browser from opposite directions.

## Bottom line

**Recommended for web platforms and commerce sites that want to be agent-actionable before the standard settles, and for agent builders who need a structured alternative to DOM actuation in Chromium.**
Not for anything requiring a stable, cross-browser API today, and not (yet) for reaching users outside Chrome.
My disagreeable claim: the Shopify-and-Cloudflare default-on wave matters less than it looks, because tool supply without agent demand is inventory nobody buys, and the protocol's fate rides on whether Firefox, Safari, and OpenAI ever join.

## Changes

- 2026-10-06 - Created from the 2026-10-06 entrant scan (the browser-native tool-exposure slot), with the one-browser-one-agent adoption split recorded as the central caution.
- 2026-10-07 - Added the webmachinelearning/webmcp star history chart to the Status section.
- 2026-10-09 - The draft report was revised on 2026-10-08 and removed the declarative form-annotation API "for now" (issue #338), so the API description moved to the imperative-only path, the declarative on-ramp bullet became the imperative-path bullet, the browser-mediation bullet was re-grounded in the permissions policy and tool events after `SubmitEvent.agentInvoked` left the draft, and the removal joined the churn caution; stars and open issues refreshed as of 2026-10-09.

## See also

- [Model Context Protocol (MCP)](../mcp/index.md) - the server-side protocol the spec names as its model
- [Agent User Interaction Protocol (AG-UI)](../ag-ui/index.md) - the frontend-facing lane on the other side of the browser
- [Protocols Feature Matrix](../protocols-feature-matrix/index.md) - the category comparison this note joins as the ninth column
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - the map of where browser agents sit among the harnesses

## References

- https://webmachinelearning.github.io/webmcp/ - the Draft Community Group Report (2026-10-08 revision): `document.modelContext` API, permissions policy, and the full security considerations section
- https://github.com/webmachinelearning/webmcp - repository: 4,499 stars, 123 open issues, pushed 2026-10-08 (GitHub API, as of 2026-10-09)
- https://github.com/webmachinelearning/webmcp/commit/14ae813cc4e9 - the 2026-10-08 commit "Remove declarative API from the spec for now (#338)" behind the revision
- https://developer.chrome.com/docs/ai/webmcp - Chrome implementation: origin trial from Chrome 149, imperative and declarative APIs, `tools` permissions policy defaults, Angular experimental support (page updated 2026-10-01)
- https://nohacks.co/blog/what-is-webmcp - practitioner record: the 2026-02-10 announcement, the navigator-to-document rename, the August Shopify and Cloudflare default-on wave, and the browser-support table
- https://zylos.ai/research/2026-04-30-webmcp-browser-native-ai-agent-interaction/ - independent analysis: Puppeteer v24.41.0 native support and the experimental state of the spec's security sections as of April 2026
- https://www.infoq.com/news/2026/06/webmcp-web-agent-standard-chrome/ - the Chrome team's I/O 2026 announcement context
