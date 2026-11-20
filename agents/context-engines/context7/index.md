---
title: Context7
created: 2026-10-07
updated: 2026-11-20
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

A hosted documentation platform by Upstash, the Redis and QStash company, with the MCP server and CLI open source under MIT (63,119 stars as of 2026-10-16, pushed 2026-11-19).
The pipeline crawls and version-parses library documentation, scores repository organizations for trust, and runs an LLM-based injection check over stored chunks before serving them.
Two install modes: an MCP server your agent calls natively (the `@upstash/context7-mcp` npm package, v4.7.3 as of 2026-11-19, about 1,027,200 downloads in the week to 2026-10-09), or a `ctx7` CLI plus an agent skill that needs no MCP at all (0.9.0 on 2026-11-03 added `ctx7 search <query>`, a cross-library search that needs no library ID, with `--library`, `--library-version`, `--language`, and `--json` narrowing, and taught setup and remove to handle the OpenCode 2.x config layout; the 0.8.x train locked concurrent token refreshes so parallel commands stop revoking a shared session, removed the deprecated `skills` and `generate` commands while `ctx7 setup` still installs the skills, and preserved comments in the agent configs it rewrites).
The SDK package (@upstash/context7-sdk, 0.7.1 since 2026-11-16, which also reads a JSON response through a mixed-case Content-Type header where 0.7.0 threw a TypeError) types a `rank` field on each search snippet so callers can interleave code and info results in the reranked order, and its `searchLibrary` call now returns an empty list instead of throwing when nothing matches, labeling the trust score "Source Reputation" like the MCP server.
A prompt trigger ("use context7") or the agent's own tool call fetches the docs; only the lookup query and library name leave your machine, not your code.
A second remote endpoint, the Admin MCP server (admin.mcp.context7.com, documented 2026-10-23), lets an agent manage the account itself: teamspace members, libraries, rules and policies, usage, Docs7 sites, and Ask sites, authenticated by OAuth or a management-access API key.

## Status

Active and heavily adopted: created 2025-03-26, 63,119 stars as of 2026-10-16, npm reporting 4,034,314 downloads summed for 2026-10-20 to 2026-11-20, with three zero-day gaps in npm's counter making weekly figures unreliable, as of 2026-11-20.
Release 4.5.0 (2026-11-03) shipped the research-preview mode for the MCP server, with a `submit-docs-feedback` tool that scores the documentation `query-docs` returned, listed only when the preview flag is on, in the same batch as admin-surface hardening that puts library imports behind the admin key.
Releases 4.5.1 and ctx7 0.10.0 (both 2026-11-06) shipped the follow-ups: the MCP server keeps the teamspace library-filter notice in resolve-library-id results even when no library matches, while the CLI released the Pi and T3 Code setup options it had carried unreleased (Pi written to `~/.pi/agent/mcp.json` with the Context7 rule added to its context file and the skill to `~/.agents/skills`) and extended the comment-preserving config rewrites to JSONC files such as `.vscode/mcp.json` and `.cursor/mcp.json`, with CRLF-safe AGENTS.md and GEMINI.md edits.
Releases 4.6.0 and ctx7 0.11.0 (both 2026-11-09) added the `query-code` MCP tool and the `ctx7 code` command, which search and read a library's source code at the version its docs describe (grep with ripgrep's options plus definition, references, outline, read, and list operations; part of the research preview, listed only with the flag on), and released the `get-upgrade-guide` tool the 2026-11-05 work had held back; the docs' on-prem changelog now carries 2.0.0 upgrade notes (2026-11-10).
The 2026-11-12 wave released the next tranche across five packages: @upstash/context7-mcp@4.7.0 paginates `get-upgrade-guide` (a long guide arrives in pages, page 1 carrying everything needed to migrate, and a guide is served only once complete so its pages always fit together), @upstash/context7-sdk@0.7.0 made `searchLibrary` return an empty list instead of a 404, and ctx7@0.11.1 repointed the CLI's help examples to `/reactjs/react.dev` after `/facebook/react` began redirecting.
The 2026-11-16 wave released the next tranche across the same packages: @upstash/context7-mcp@4.7.1 widens the source-indexing wait rule (`ctx7 code` and `query-code` now say to call again for up to three minutes while a library's first index runs, instead of at most twice) and renames the research preview to experimental tools with each signed-in user choosing them from the dashboard, @upstash/context7-sdk@0.7.1 ships the mixed-case Content-Type fix, and ctx7@0.12.0 adds the `ctx7 get-upgrade-guide` CLI counterpart of the MCP tool (a guide printed between two versions, with `--page` and `--json`, exiting with code 75 while the guide is being prepared) plus a fix for `ctx7 login` and `ctx7 whoami` hanging on a stalled endpoint.
ctx7@0.12.1 (2026-11-16) reads the deployment URL from `CONTEXT7_BASE_URL` when `--base-url` is not passed, so on-premise users set it once instead of per command, with `--base-url` still winning and a custom URL from either source turning off the update check and telemetry. The 2026-11-17 release wave corrected this run's earlier docs-only reading of that day's main commits: @upstash/context7-mcp@4.7.3 replaced the experimental `query-code` tool with `grep-code`, `glob-code`, `read-code`, and `find-symbol`, which take the parameters of the Grep, Glob, and Read tools coding agents already have, so agents search the library instead of the local project (a dashboard choice that turned query-code on now turns the four on), @upstash/context7-mcp@4.7.2 serves that dashboard choice without a per-request lookup, and ctx7@0.12.2 together with the new @upstash/context7-opencode plugin package (0.2.2) restored the rules and skills that `ctx7 setup` and the plugins install to their pre-code-tools text, with no query-code, `ctx7 code`, or `get-upgrade-guide` guidance and the MCP server describing its experimental tools only to users who opted in; the README's tool list now names only `resolve-library-id` and `query-docs`, and main's newest commit (2026-11-18) is a docs piece comparing Google Drive connection methods.
A 2026-11-19 docs change landed after that day's fetch: the experimental-tools doc now says **source code search is turned off for now and the dashboard does not offer it**, so the four grep-class code tools shipped in 4.7.3 are not currently selectable, while documentation feedback and upgrade guides remain the two experimental tools a user can turn on; main's unreleased 2026-11-20 batch goes further on delivery (the `context7-mcp` skill served over the MCP skills extension), tooling (resolve-library-id taking the library version as its own input and stopping listing versions), and CLI hygiene (terminal control characters stripped from API content), all awaiting their release wave.

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

Free for individuals (public repositories, 1,000 API calls per month), Pro at $10 per seat per month (private repositories, 2,000 calls per seat included, then $5 per 1,000 calls, private-repo parsing at $5 per million tokens), and Enterprise at custom per-seat pricing (published range $2.50 to $30 per user per month by teamspaces size, with SOC 2, SSO, and self-hosted deployment), as of 2026-11-07, re-verified unchanged against the live plans page.

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
- 2026-10-31 - Full rotation re-verification: every cited URL re-fetched and intact; recorded main's unreleased research-preview work (a research-preview flag and a docs feedback tool for the MCP server, committed 2026-10-30, with library imports now gated on the admin key), and refreshed the trailing-month npm figure (2,607,063 to 2026-10-29); pricing tiers re-verified unchanged against the live plans page.
- 2026-11-05 - Recorded the 2026-11-03 releases: @upstash/context7-mcp@4.5.0 shipping the research-preview mode with its `submit-docs-feedback` tool, and ctx7@0.9.0 adding cross-library `ctx7 search` and OpenCode 2.x config handling; refreshed the trailing-month npm figure (2,769,609 summed for 2026-10-06 to 2026-11-05); pricing tiers re-verified unchanged against the live plans page.
- 2026-11-06 - Recorded main's unreleased post-release work (2026-11-05 to 2026-11-06: SAML 2.0 SSO documented for on-premise, the ctx7 CLI setup gaining Pi and T3 Code as supported agents, and the new `get-upgrade-guide` research-preview tool held back until its libraries are prepared); the trailing-month npm figure keeps its 2026-11-05 as-of date.
- 2026-11-07 - Recorded the 2026-11-06 releases releasing that work: @upstash/context7-mcp@4.5.1 (the teamspace library-filter notice kept in resolve-library-id results when no library matches) and ctx7@0.10.0 (Pi and T3 Code setup and remove, comment-preserving rewrites extended to JSONC configs, CRLF-safe AGENTS.md and GEMINI.md edits); refreshed the trailing-month npm figure (3,176,334 summed for 2026-10-08 to 2026-11-07, six zero days); pricing tiers re-verified unchanged against the live plans page.
- 2026-11-11 - Recorded the 2026-11-09 releases: @upstash/context7-mcp@4.6.0 and ctx7@0.11.0 adding the research-preview `query-code` tool and `ctx7 code` command (source-code search and read at the documented version, ripgrep-style grep plus definition, references, outline, read, and list) and releasing the `get-upgrade-guide` tool, with the on-prem changelog carrying 2.0.0 upgrade notes (2026-11-10); refreshed the trailing-month npm figure (3,061,330 summed for 2026-10-12 to 2026-11-11, six zero days).
- 2026-11-16 - Recorded the 2026-11-12 release wave: @upstash/context7-mcp@4.7.0 paginating the `get-upgrade-guide` research-preview tool (page 1 carries the migration essentials and a guide is served only once complete so its pages fit together), @upstash/context7-sdk@0.7.0 (`searchLibrary` returning an empty list instead of a 404, the trust score labeled Source Reputation), and ctx7@0.11.1 (help examples moved to /reactjs/react.dev after /facebook/react began redirecting); refreshed the trailing-month npm figure (3,336,230 summed for 2026-10-17 to 2026-11-16, three zero days); the 2026-11-13 main commits resolved as docs-only and the 2026-11-16 pushed signal as later pushes of a default branch newest-committed 2026-11-14, per the standing rulings.
- 2026-11-17 - Recorded the 2026-11-16 release wave: @upstash/context7-mcp@4.7.1 (the code tools now say to call again for up to three minutes while a library's first index runs, and the research preview renamed experimental tools with a per-user dashboard choice), @upstash/context7-sdk@0.7.1 (the mixed-case Content-Type fix shipped), ctx7@0.12.0 (the `ctx7 get-upgrade-guide` CLI counterpart with `--page`, `--json`, and exit code 75 while the guide is prepared, plus the stalled-endpoint login/whoami fix), ctx7@0.12.1 (the deployment URL read from `CONTEXT7_BASE_URL`, custom URLs turning off the update check and telemetry), and mcpb-v4.7.1; the 2026-11-17 main commits resolved as docs-only; refreshed the trailing-month npm figure (3,267,015 summed for 2026-10-18 to 2026-11-17, four zero days).
- 2026-11-19 - Corrected the 2026-11-17 docs-only summary: the same-day 2026-11-17 release wave shipped @upstash/context7-mcp@4.7.3 replacing the experimental `query-code` tool with `grep-code`, `glob-code`, `read-code`, and `find-symbol` (the parameters of the agents' own Grep, Glob, and Read tools, aimed at the library), @upstash/context7-mcp@4.7.2 (the dashboard choice served without a per-request lookup), and ctx7@0.12.2 plus the new @upstash/context7-opencode@0.2.2 plugin package restoring the rules and skills to their pre-code-tools text with experimental tools described only to opted-in users; the 2026-11-19 pushed signal re-fired the check; refreshed the trailing-month npm figure (3,814,469 summed 2026-10-19 to 2026-11-18, three zero days) and the MCP package version (4.7.3).
- 2026-11-20 - Recorded the 2026-11-19 docs change that landed after the same day's fetch: the experimental-tools doc states source code search is turned off for now and the dashboard does not offer it, so the grep-code/glob-code/read-code/find-symbol set shipped in 4.7.3 is not currently selectable (documentation feedback and upgrade guides remain the two turnable experimental tools); recorded main's unreleased 2026-11-20 batch (the context7-mcp skill served over the MCP skills extension, resolve-library-id taking the version as its own input and stopping listing versions, and terminal control characters stripped from CLI API content); refreshed the trailing-month npm figure (4,034,314 summed 2026-10-20 to 2026-11-20, three zero days).

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
- https://registry.npmjs.org/@upstash/context7-mcp/latest - the published MCP server version 4.7.3 and MIT license (re-fetched 2026-11-19)
- https://api.npmjs.org/downloads/range/2026-10-20:2026-11-20/@upstash/context7-mcp - trailing-month download volume for the adoption claim, 4,034,314 summed for 2026-10-20 to 2026-11-20, three zero days in the window (fetched 2026-11-20)
- https://raw.githubusercontent.com/upstash/context7/HEAD/docs/howto/admin-mcp.mdx - the Admin MCP server: endpoint, OAuth and management-key auth, teamspace scoping, and the tool surface (fetched 200, 2026-10-24)
- https://api.github.com/repos/upstash/context7/releases - the release train: the 2026-11-16 wave (mcpb-v4.7.1, ctx7@0.12.1, ctx7@0.12.0, @upstash/context7-sdk@0.7.1, @upstash/context7-mcp@4.7.1) after the 2026-11-12 wave (@upstash/context7-mcp@4.7.0, @upstash/context7-sdk@0.7.0, @upstash/context7-tools-ai-sdk@1.0.4, ctx7@0.11.1, mcpb-v4.7.0), and the 2026-11-17 wave (@upstash/context7-mcp@4.7.2 and @4.7.3, ctx7@0.12.2, @upstash/context7-opencode@0.2.2, mcpb-v4.7.2, mcpb-v4.7.3) (re-fetched 2026-11-19)
- https://upstash.com/blog/context7-vs-web-search-benchmark - the vendor's own head-to-head against Claude Code web search (May 2026): the 34.56 percent cost and 36.81 percent token reductions with their caching caveat, the only published comparison (fetched 200, 2026-10-07)
