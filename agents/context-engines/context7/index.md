---
title: Context7
created: 2026-10-07
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, documentation, mcp, developer-tools]
readability: 3
audience_notes: >
  Engineers whose coding agents hallucinate library APIs, and anyone comparing context delivery modes for agents.
  Assumes you know what an MCP server and a context window are.
---

Context7 is Upstash's hosted service that pulls up-to-date, version-specific library documentation and code examples into an LLM's prompt at question time, through an MCP server or a CLI-plus-skill install.

**Context7 is the first member of this category that indexes the world's library documentation instead of your repository: every other engine here decides which slices of your own code enter the window, while Context7 decides which slices of the public docs enter it, fresh from source rather than from the model's training data.**

## What it is

A hosted documentation platform by Upstash, the Redis and QStash company, with the MCP server and CLI open source under MIT (63,119 stars as of 2026-10-16, pushed 2026-10-23).
The pipeline crawls and version-parses library documentation, scores repository organizations for trust, and runs an LLM-based injection check over stored chunks before serving them.
Two install modes: an MCP server your agent calls natively (the `@upstash/context7-mcp` npm package, v4.4.4, about 1,027,200 downloads in the week to 2026-10-09), or a `ctx7` CLI plus an agent skill that needs no MCP at all (the CLI released through 0.8.2 on 2026-10-23, which locks concurrent token refreshes so parallel commands stop revoking a shared session; 0.8.0 had removed the deprecated `skills` and `generate` commands while `ctx7 setup` still installs the skills, and 0.8.1 preserved comments in the agent configs it rewrites).
The SDK package (@upstash/context7-sdk, 0.6.0) types a `rank` field on each search snippet so callers can interleave code and info results in the reranked order.
A prompt trigger ("use context7") or the agent's own tool call fetches the docs; only the lookup query and library name leave your machine, not your code.
A second remote endpoint, the Admin MCP server (admin.mcp.context7.com, documented 2026-10-23), lets an agent manage the account itself: teamspace members, libraries, rules and policies, usage, Docs7 sites, and Ask sites, authenticated by OAuth or a management-access API key.

## Status

Active and heavily adopted: created 2025-03-26, 63,119 stars as of 2026-10-16, npm reporting 2,508,160 downloads in the month to 2026-10-22, with several zero-day gaps in npm's counter making weekly figures unreliable, as of 2026-10-24.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=upstash/context7&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=upstash/context7&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=upstash/context7&type=date&legend=top-left" />
</picture>

The only head-to-head benchmark is Upstash's own (May 2026): across five query categories against Claude Code's WebSearch and WebFetch tools it reports an average 34.56 percent cost reduction and 36.81 percent total token reduction, driven by a roughly 99 percent cut in fresh input tokens, with the caveat that aggressive prompt caching and Haiku-handled auxiliary calls moderate the cost gap; the HN footprint is small (the largest submission reached 4 points), so the adoption case rests on the star and download curves plus this vendor-run table, unreplicated by any third party as of 2026-10-07.

## Strengths

- Attacks the failure mode every agent user knows, hallucinated or outdated APIs, at the delivery layer rather than by fine-tuning.
- Version-specific retrieval, so answers match the package version you actually pin, which repo-indexing engines and training data both miss.
- Delivery is agent-agnostic: MCP for anything that speaks it, CLI and skill for anything that does not.
- Trust scores, injection screening, and a query-only privacy boundary are documented, unusual care for a prompt-time service.

## Cautions

- The accuracy claims are vendor-run; no independent benchmark of Context7 against plain web search or training-data answers exists yet, as of 2026-10-07.
- The free tier caps at 1,000 API calls a month, and public-repo coverage is all you get below Pro, so private dependencies need the paid tier.
- Docs quality inherits the source: a library with bad docs gets bad injection, and very new or very niche packages may be absent from the index entirely.
- Sending library names and queries to a third party is a mild telemetry leak about your stack, even with code excluded.

## Pricing

Free for individuals (public repositories, 1,000 API calls per month), Pro at $10 per seat per month (private repositories, 2,000 calls per seat included, then $5 per 1,000 calls, private-repo parsing at $5 per million tokens), and Enterprise at custom per-seat pricing (published range $2.50 to $30 per user per month by teamspaces size, with SOC 2, SSO, and self-hosted deployment), as of 2026-10-22, re-verified unchanged against the live plans page.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-07 | Free, Pro, Enterprise | Introduced at Free $0, Pro $10/seat/month, Enterprise custom ($2.50 to $30/user/month published range) | https://context7.com/plans |

## Compared to

- [rtk](../rtk/index.md): the other prompt-time filter here, but rtk compresses your own command output while Context7 injects external documentation; a session can want both.
- [Augment Code](../augment-code/index.md): the platform that indexes your private code in its cloud; choose it when the missing context is yours, Context7 when it is the world's libraries.
- [Repomix](../repomix/index.md): the offline extreme, packing what you have locally into one file with no service and no freshness.

## Bottom line

**Recommended for any agent workflow that touches fast-moving libraries whose training-data knowledge has gone stale, starting free and measuring whether injected docs beat the model's defaults on your stack.**
Not for private-code context (that is what the repo-indexing members sell), and not for teams who cannot accept a per-call bill at scale.

## Changes

- 2026-10-07 - Created.
- 2026-10-11 - Recorded the MCP server package moving to v4.3.0 with weekly npm downloads passing one million (1,027,217 for the week to 2026-10-09), and refreshed the growth numbers (62,890 stars, pushed 2026-10-10).
- 2026-10-17 - Recorded the MCP server package at v4.4.2 (2026-10-15, server title and icons in the MCP handshake) and the `ctx7` CLI train through 0.8.0 (2026-10-16, deprecated `skills` and `generate` commands removed, `ctx7 setup` still installing the skills), correcting the stale v4.3.0 mention.
- 2026-10-20 - Recorded the MCP server package at v4.4.4 (2026-10-19, MCP SDK 2.3.1, list cache hints, and HTTP shutdown draining) and the `ctx7` CLI at 0.8.1 (comment-preserving config rewrites, `--api-key` stripping in setup).
- 2026-10-22 - Moved the adoption figure to the trailing-month window (2,640,895 npm downloads to 2026-10-18) after npm's counter began reporting zero days that break weekly comparisons; pricing tiers re-verified unchanged against the live plans page.
- 2026-10-24 - Recorded the new Admin MCP server (a second remote endpoint at admin.mcp.context7.com where an agent manages teamspaces, libraries, rules, usage, Docs7 sites, and Ask sites, OAuth or management-key auth, documented 2026-10-23), the `ctx7` CLI at 0.8.2 (lock-protected token refresh for concurrent commands), the SDK at 0.6.0 (typed `rank` on search snippets), and refreshed the trailing-month npm figure (2,508,160 to 2026-10-22).

## See also

- [rtk](../rtk/index.md) - the category's other prompt-time delivery layer, filtering output instead of injecting docs
- [Augment Code](../augment-code/index.md) - the private-code counterpart, indexing what Context7 deliberately ignores
- [Repomix](../repomix/index.md) - the offline, snapshot-based packing answer to the same staleness problem
- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/upstash/context7 - repository, MIT license, install modes, and the two-mode delivery story (fetched 200, 2026-10-07)
- https://api.github.com/repos/upstash/context7 - stars, created date, and push date for the as-of status (fetched 200, 2026-10-16)
- https://context7.com - the platform site, Upstash attribution, and product surface (fetched 200, 2026-10-07)
- https://context7.com/plans - the Free/Pro/Enterprise tier table, call quotas, overage rates, privacy and trust documentation, and the Enterprise seat-price range (fetched 200, 2026-10-07)
- https://registry.npmjs.org/@upstash/context7-mcp/latest - the published MCP server version 4.4.4 and MIT license (fetched 200, 2026-10-20)
- https://api.npmjs.org/downloads/point/last-month/@upstash/context7-mcp - trailing-month download volume for the adoption claim, 2,508,160 for the month to 2026-10-22 (fetched 200, 2026-10-24)
- https://raw.githubusercontent.com/upstash/context7/HEAD/docs/howto/admin-mcp.mdx - the Admin MCP server: endpoint, OAuth and management-key auth, teamspace scoping, and the tool surface (fetched 200, 2026-10-24)
- https://api.github.com/repos/upstash/context7/releases - the release train: ctx7@0.8.2 and @upstash/context7-sdk@0.6.0 published 2026-10-23 (fetched 200, 2026-10-24)
- https://upstash.com/blog/context7-vs-web-search-benchmark - the vendor's own head-to-head against Claude Code web search (May 2026): the 34.56 percent cost and 36.81 percent token reductions with their caching caveat, the only published comparison (fetched 200, 2026-10-07)
