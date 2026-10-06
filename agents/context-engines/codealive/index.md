---
title: CodeAlive
created: 2026-10-05
updated: 2026-10-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, code-search, code-graphs, mcp, saas]
readability: 3
audience_notes: >
  Engineers choosing a hosted context engine for agents on large or multi-repo
  codebases, who want the commercial options beyond Augment and Sourcegraph.
  Assumes you know what MCP, semantic search, and per-token pricing are.

---

CodeAlive is a hosted context engine that builds a code graph and hybrid retrieval index over your repositories and serves it to humans and agents over MCP and a REST API, with an AI code-review agent and a deep-research mode on top.

**CodeAlive is the cheapest on-ramp to the "index my repos for my agent" market and the only cloud entry that serves any MCP client on metered per-action pricing, and it is also the least proven tool in this category: every number on its site is vendor-run, and I found no independent coverage at all.**

## What it is

A cloud service that indexes connected repositories into a code graph (files, symbols, calls, dependencies, tests) refreshed on every push, then answers queries with hybrid retrieval, semantic search plus lexical match plus graph traversal, returning cited results.
Agents reach it through a hosted MCP endpoint (`https://mcp.codealive.ai/api/`, OAuth or API key), a local Docker MCP server that still authenticates to the cloud, or a REST API; an `npx @codealive/installer` command wires Claude Code, Cursor, VS Code, Windsurf, Cline, and Codex.
Tool API v3 (shipped 2026-07-11) exposes eleven read-only operations from search through relationship traversal to a stateless `chat` synthesis fallback, and CodeAlive 3.0 (announced 2026-07-17) added a read-only ContextResearchAgent and the vendor's own RepoContextBench.
The core is closed-source SaaS from a small London company; only the MCP server container is self-hostable, and the index stays cloud-side.

## Status

**Active and shipping, with an unverifiable user base.**
The public surfaces are current (docs, changelog, MCP v3 with a v1/v2 migration guide, all fetched 2026-10-05), and the `@codealive/installer` package sits at 1.0.8 on npm.
The adoption record is the problem: a Hacker News search returns zero stories about the product, I found no practitioner threads, no reviews, and no customer logos beyond the site's own claims, and the company's headcount is not published anywhere I could fetch.
Every performance claim (45 percent fewer tokens, about 25 times lower model cost, RepoContextBench results) is vendor-run.

## Strengths

- **Agent-agnostic by design**: one hosted index serves Claude Code, Cursor, Codex, or your own REST callers, where Augment's engine only drives Augment's own surfaces.
- The pricing is metered and public down to the action (search, chat, deep analysis, review), which makes a small-team pilot genuinely cheap instead of sales-gated.
- The integration docs understand the failure mode that kills retrieval tools: they prescribe explicit routing rules so the agent reaches for the index instead of defaulting to grep, and suggest isolating exploration in a subagent.
- Free tier includes MCP access, which is the fastest zero-cost way to test whether a hosted index helps your repo at all.

## Cautions

- **No independent evidence exists as of 2026-10-05**: zero Hacker News footprint, no third-party evaluation, and RepoContextBench is the vendor's own benchmark.
- The published tiers cap repository size (25 MB free, 100 MB Hobby and Pro, 100-500 MB Team), which sits far below the 1M-plus-LOC pitch; large monorepos are a sales conversation, not a plan.
- Your code indexes server-side by default; the "local Docker" deployment only runs the MCP client side and still sends your API key to the cloud.
- A tiny single-product company is a durability risk for infrastructure you would wire into every agent session.

## Pricing

Free ($0, 1 user, 1 workspace, 25 MB of repos, 100 chat requests per month, MCP access), Hobby ($15/month with a $15 usage balance, 1 developer, up to 100 MB), Pro ($50/month balance, 1-3 developers, deep analysis and AI code review), and Team (from $100/month balance, 5-15 developers, 100-500 MB), all as of 2026-10-05.
Usage is metered per action: search $0.02, chat $0.15, deep analysis $0.30, code review $0.50.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-05 | All tiers | Baseline: Free $0 (25 MB, 100 chats/mo), Hobby $15/mo, Pro $50/mo, Team from $100/mo; per-action $0.02 search, $0.15 chat, $0.30 deep analysis, $0.50 code review. | [codealive.ai](https://codealive.ai/en) |

## Compared to

- [Augment Code](../augment-code/index.md): a closed platform that bundles retrieval with its own harness at flat tiers plus a 40 percent service fee; CodeAlive sells the retrieval alone, metered, to any MCP client.
- [Sourcegraph code context platform](../sourcegraph-code-context/index.md): enterprise cross-repo intelligence from $16K a year; CodeAlive's free and $15 tiers cover the solo and small-team band Sourcegraph refuses.
- [Semble](../semble/index.md): local, free, per-session indexing on one machine; CodeAlive costs money but indexes multi-repo server-side and keeps graphs fresh on push.

## Bottom line

**Recommended for solo developers and small teams whose agents thrash on multi-repo exploration and who want to test a hosted index starting from zero dollars.**
Not for anyone who requires independent validation, on-prem indexing, or codebases past the published tier caps.
My disagreeable claim: CodeAlive's pricing model, the engine unbundled from the harness and metered per action, is where the context-engine market is heading, and Augment's bundled platform is the transitional form.

## Changes

- 2026-10-05 - Created from the 2026-10-05 entrant scan (the hosted agent-agnostic context-engine slot), with the vendor-only-evidence caveat recorded.

## See also

- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins as the tenth column
- [Augment Code](../augment-code/index.md) - the bundled-platform alternative whose engine never leaves its own harness
- [Sourcegraph code context platform](../sourcegraph-code-context/index.md) - the enterprise-scale version of the hosted-index bet
- [Semble](../semble/index.md) - the free local counterpart for single-repo, on-device needs

## References

- https://codealive.ai/en - homepage: positioning, tier table, per-action rates, and the vendor-run efficiency claims
- https://codealive.ai/en/pricing - the pricing page (redirects to the homepage; content live 2026-10-05)
- https://docs.codealive.ai/quickstart - installer, API keys, indexing flow, and example queries
- https://docs.codealive.ai/integrations/mcp - MCP v3 tools, hosted endpoint, OAuth and Docker deployments, migration guide
- https://codealive.ai/en/blog/codealive-3-context-engine-agent-repocontextbench - the 3.0 announcement: Tool API v3 (2026-07-11), ContextResearchAgent, RepoContextBench
- https://registry.npmjs.org/@codealive%2Finstaller - the installer package, 1.0.8
- https://hn.algolia.com/api/v1/search?query=CodeAlive&tags=story - the footprint scan: zero stories about the product (2026-10-05)
