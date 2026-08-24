---
title: Greptile
created: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, code-review, code-retrieval, developer-tools]
readability: 3
audience_notes: >
  Engineers evaluating an AI code reviewer with full-codebase context, or a codebase-understanding API.
  Assumes familiarity with PR review workflows and with what graph indexes do and do not solve.

---

Greptile is an AI code review service that indexes your repositories into a graph (files, functions, dependencies) and runs a swarm of review agents over every pull request.
Facts below verified as of 2026-08-24.

**Greptile's durable asset is not its graph index, which is becoming commodity, but the standards it learns from your team's own review comments, a corpus no competitor can copy overnight.**

## What it is

**It is a validation layer, deliberately not a code generator.**
The product indexes repos, then parallel agents review PRs for bugs, security issues, and multi-file logic errors, learning each team's conventions by reading GitHub/GitLab comments (learnings isolated per organization).
TREX (beta) extends review with sandboxed execution, writing and running tests per PR.
Integrations point both ways: one-click handoff of each finding to Claude Code, Cursor, Codex, or Devin, a Greptile MCP server so agents can pull learned rules and resolve comments, a CLI, auto-detection of CLAUDE.md and .cursorrules, and Jira/Notion context.
Self-hosted in your own AWS or air-gapped VPC is supported, with SOC 2 and GitHub plus GitLab coverage, plus a bulk API for building your own tools on the index.
Behind it is Tabnam, Inc., a YC W24 company founded in 2023 by three Georgia Tech graduates (Daksh Gupta, Soohoon Choi, Vaishant Kameswaran).

## Status

**Active, well-funded, and shipping.**
The homepage claims 22,000+ teams and names Nvidia, Brex, Substack, PostHog, Zapier, and Retool as users (vendor claim as of 2026-08-24).
Funding: $4M seed led by Initialized Capital (June 2024), then a $25M Series A led by Benchmark Capital (September 23, 2025) alongside YC and Initialized; the YC directory lists a team of about 35.
Release cadence is real: v3 rewrite (September 2025), TREX (June 2026), v5 (August 5, 2026), with the Series A post citing 500M+ lines reviewed that September month.

## Strengths

- **The learning loop is the moat**: rules distilled from real human review comments (transaction handling, logging patterns, security whitelists) compound per team and travel nowhere else.
- Review-only focus is a defensible position when authoring agents commoditize; everything writes code, few verify it independently.
- Vendor-reported scale gives some comfort: 180,000+ bugs prevented in one month per the Series A post, with named customers willing to be quoted.
- The engineering provenance is public: the founders documented their AST-parse, docstring-embedding, agentic-search pipeline on HN at launch (it uses tree-sitter), limitations included.

## Cautions

- **Credit pricing has already drawn blood**: an April 2026 "Greptile's New Pricing Is Predatory" site hit HN, and its thread includes claims that free-tier promises to open source contributors were not honored; treat the OSS-free policy as unverified until confirmed with them.
- All quality claims (3x more critical bugs caught in v3 than v2, benchmark wins) are vendor-run with no published third-party replication.
- The index is post-commit; review-time working trees and unmerged dependencies are not what the graph sees.
- Early reliability was rough (launch-day outages and wrong-answer reports on HN in March 2024); the company has clearly iterated, but C++ templates and similar corners were weak points at launch.

## Pricing

**Metered credits mean the reviewer's bill scales with your PR velocity, not your headcount, which is either alignment or a tax depending on your merge rate.**
Starter is free for one active developer with 50 credits per month; Pro is $30 per seat per month including 50 credits per seat, with extra credits at $1 each and TREX reviews costing 3 credits (as of 2026-08-24).
Free usage for qualified open source projects and discounts for pre-Series A startups are advertised but, per the caution above, community reports dispute how this lands in practice.
Self-hosted enterprise and bulk API pricing are custom.

## Compared to

- [Sourcegraph code context platform](../sourcegraph-code-context/index.md): retrieval infrastructure priced at org level for any agent; choose Greptile when you want the reviewer and validator, not the index.
- CodeRabbit: the closest review-first rival with heavier marketing footprint; Greptile's differentiators are the learned-rules loop and self-hosting.
- [Augment Code](../augment-code/index.md): sells a full authoring-plus-review factory; choose Greptile when you want review independent of the tools that wrote the code.

## Bottom line

**Recommended for teams whose bottleneck is review throughput on a growing PR flood, especially with multiple coding agents authoring changes.**
Not for individuals priced out by per-credit metering or maintainers who need the OSS-free promise in writing.
My disagreeable claim: the graph index everyone credits Greptile for is the least valuable part of the product, and if a competitor shipped an identical index tomorrow with none of the learned-comment corpus, it would lose to Greptile on house-rule enforcement every time.

## See also

- [Sourcegraph code context platform](../sourcegraph-code-context/index.md) - the infra-only end of the same indexed-codebase bet
- [Semantic code search in coding tools](../semantic-code-search/index.md) - why graph indexes beat plain embeddings on cross-file questions
- [Tree-sitter code chunking](../tree-sitter-chunking/index.md) - the parsing layer Greptile's indexer builds on
- [Claude Code](../claude-code/index.md) - the agent most often on the receiving end of Greptile comments

## References

- https://greptile.com/ - product surface, customer list, team count, and pricing FAQ as claimed by the vendor
- https://www.greptile.com/blog/series-a - $25M Series A led by Benchmark, v3 claims, 500M+ lines reviewed
- https://www.ycombinator.com/companies/greptile - YC W24 batch, founding year, founders, team size
- https://techcrunch.com/2024/06/06/greptile-raises-4m-to-build-an-ai-code-base-expert/ - $4M seed, API-first origin, customer counts at seed
- https://news.ycombinator.com/item?id=39604961 - launch thread: AST parsing, docstring embeddings, agentic search, and early criticism
- https://news.ycombinator.com/item?id=47966075 - the critical "predatory pricing" thread and OSS-billing allegations
