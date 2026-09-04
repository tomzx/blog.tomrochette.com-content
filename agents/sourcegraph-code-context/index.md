---
title: Sourcegraph code context platform
created: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, code-search, code-retrieval, enterprise-tools, mcp]
readability: 3
audience_notes: >
  Engineers deciding how agents should retrieve context across large or multi-repo codebases.
  Assumes familiarity with MCP clients like Claude Code or Cursor and with why grep fails at scale.

---

Sourcegraph is a code intelligence platform (Code Search, Deep Search, an MCP server with the Code Finder agent) that has repositioned itself as the retrieval layer both humans and coding agents use on large codebases.
Facts below verified as of 2026-09-04.

**Sourcegraph rebuilt itself around selling search to agents rather than assistants to humans, and its own benchmark data says the value only appears above roughly 400K lines of code, which is exactly the fact its sales motion will not volunteer.**

## What it is

**The product is an indexed view of every repository, queried through four surfaces.**
Code Search does exact, deterministic search across all indexed repos, plus a public instance covering 1M+ public repositories.
Deep Search (GA October 2025) is an agentic, natural-language investigator for humans, with role-based permissions.
The MCP server gives agents keyword and semantic search, go-to-definition and find-references backed by SCIP precise code intelligence, commit history, diffs, and ownership signals, and works with Claude Code, Codex, Cursor, and Amp.
Code Finder (beta July 2026, now GA) is an agentic search tool inside the MCP server that runs its own search loop and returns files with line ranges, and Agentic Batch Changes (public beta June 2026) executes large-scale migrations across repos.
Deployment is single-tenant cloud or self-hosted, SOC 2 Type II and ISO 27001, sold by the independent company now run by CEO Dan Adler.

## Status

**Active, independent, and shipping weekly.**
Sourcegraph and Amp split into two companies on December 2, 2025, with founders Quinn Slack and Beyang Liu leaving for Amp Inc. (both stay on Sourcegraph's board) and investors Sequoia, a16z, Redpoint, Craft, and Goldcrest on both cap tables.
Version 7.0 (February 25, 2026) declared the "intelligence layer for AI coding agents" positioning and removed Cody Web and Search Notebooks, closing the Cody chapter.
SCIP moved to a community-driven open source project in March 2026, and Cloud ships weekly.
I found little independent 2026 community discussion of the post-split platform; the HN thread on the split (90 points) is mostly about Amp, so the audience for its claims is buyers, not discourse.

## Strengths

- **Precise, cross-repository navigation is the differentiator**: SCIP-backed find-references distinguishes a definition from its 47 call sites, which grep and most embeddings pipelines cannot.
- Its CodeScaleBench analysis (1,281 agent runs, 40+ large repos) names five repeatable agent failure modes and reports a +0.259 reward delta from code intelligence in the 400K-2M LOC range, with MCP-augmented agents 30% cheaper and 38% faster.
- Code Finder's own benchmark: 2.19x faster than a coding agent searching locally and 40% cheaper than an agent stepping through the MCP toolset, at comparable quality.
- Real production use: Stripe's minion agents gather code intelligence through the Sourcegraph MCP server (Stripe's own engineering blog).

## Cautions

- **The evidence is almost entirely vendor-run**: CodeScaleBench, the Code Finder benchmark, and the "cheaper model plus MCP beats a frontier model alone" claim all come from Sourcegraph's own blog and nine-task samples.
- The same vendor data shows tools slightly hurt agents below 400K LOC (a -0.080 reward delta), so most repositories are outside the product's own proven range.
- Enterprise-only pricing (from $16K) with a credits system for AI features; Code Finder was free in beta and becomes billable at GA.
- Freshness still depends on the index; local tools are always current, which matters most while an agent is mid-edit.

## Pricing

**The floor is $16K a year before any AI usage, which prices out every team the product's own data says it cannot help.**
Enterprise plan starting at $16K per year as of 2026-09-02, scaling with team size, including pooled AI credits (no monthly expiry, rollover on renewal), with volume credit buckets as an add-on and 24x5 support.
No self-serve or free private tier; the public code search is free.

## Compared to

- [Greptile](../greptile/index.md): graph index sold as a per-seat review and validation service; choose Sourcegraph when you need retrieval infrastructure for your own agents rather than a reviewer.
- [Augment Code](../augment-code/index.md): bundles its context engine with its own harness and platform; Sourcegraph serves any MCP agent you already run.
- Repomix-style packing: free and deterministic, but static snapshots with no index, navigation, or cross-repo scope.

## Bottom line

**Recommended for organizations whose codebases are past a few hundred thousand lines across many repos and who already run agent fleets that thrash on local search.**
Not for small-repo teams, solo developers, or anyone without an enterprise budget.
My disagreeable claim: below roughly 400K LOC, buying Sourcegraph for your agents means paying $16K for an index their own benchmark says slightly hurts, and that money would do more work spent on evaluation harnesses.

## See also

- [Amp](../amp/index.md) - the coding agent Sourcegraph built, then spun out, and what the split says about both bets
- [Semantic code search in coding tools](../semantic-code-search/index.md) - whether indexed retrieval survives inside editors at all
- [MCP](../mcp/index.md) - the protocol the Sourcegraph server speaks to every agent
- [Claude Code](../claude-code/index.md) - the dominant client its MCP server targets

## References

- https://sourcegraph.com/ - platform surfaces (Code Search, Deep Search, MCP, Agentic Batch Changes) and enterprise claims
- https://sourcegraph.com/pricing - Enterprise entry at $16K, credits model, support tiers
- https://sourcegraph.com/blog/why-sourcegraph-and-amp-are-becoming-independent-companies - the December 2, 2025 split, new CEO, and the agent-search-volume claim
- https://sourcegraph.com/blog/a-new-era-for-sourcegraph-the-intelligence-layer-for-ai-coding-agents-and-developers - 7.0 positioning and the Cody Web / Search Notebooks removals
- https://sourcegraph.com/changelog/code-finder-beta - Code Finder benchmark numbers and beta-to-billable credits plan
- https://sourcegraph.com/blog/why-coding-agents-fail-large-codebases - the five agent failure modes, the 400K LOC threshold, and cost/speed deltas
- https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents - customer's own account of agents using Sourcegraph MCP for retrieval
- https://news.ycombinator.com/item?id=46124649 - community discussion of the Sourcegraph/Amp split
