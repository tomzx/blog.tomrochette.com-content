---
title: Greptile
created: 2026-08-24
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, code-review, code-retrieval, developer-tools]
readability: 3
audience_notes: >
  Engineers evaluating an AI code reviewer with full-codebase context, or a codebase-understanding API.
  Assumes familiarity with PR review workflows and with what graph indexes do and do not solve.

---

Greptile is an AI code review service that indexes your repositories into a graph (files, functions, dependencies) and runs a swarm of review agents over every pull request.

**Greptile's durable asset is not its graph index, which is becoming commodity, but the standards it learns from your team's own review comments, a corpus no competitor can copy overnight.**

## What it is

**It is a validation layer, deliberately not a code generator.**
The product indexes repos, then parallel agents review PRs for bugs, security issues, and multi-file logic errors, learning each team's conventions by reading GitHub/GitLab comments (learnings isolated per organization).
TREX (beta) extends review with sandboxed execution, writing and running tests per PR.
Integrations point both ways: one-click handoff of each finding to Claude Code, Cursor, Codex, or Devin, a Greptile MCP server so agents can pull learned rules and resolve comments, a Claude Code plugin that reads and resolves Greptile comments on its own, /greploop, which lets any coding agent iterate with Greptile until its issues resolve, a CLI, auto-detection of CLAUDE.md and .cursorrules, and Jira/Notion context.
Self-hosted in your own AWS or air-gapped VPC is supported, with SOC 2 and GitHub plus GitLab coverage, plus a bulk API for building your own tools on the index.
Behind it is Tabnam, Inc., a YC W24 company founded in 2023 by three Georgia Tech graduates (Daksh Gupta, Soohoon Choi, Vaishant Kameswaran).

## Status

**Active, well-funded, and shipping.**
The homepage claims 22,000+ teams and names Nvidia, Brex, Substack, PostHog, Zapier, and Retool as users (vendor claim as of 2026-10-24).
Funding: $4M seed led by Initialized Capital (June 2024), a $25M Series A led by Benchmark Capital (September 23, 2025) alongside YC and Initialized, then a $50M Series B led by Menlo Ventures announced October 19, 2026, valuing the company at $750M ($79M total raised), with Jump Trading, Wing, Operator Collective, Benchmark, YC, Browder Capital, and Initialized participating and Menlo's Deedy Das joining the board; the announcement claims Greptile now reviews and tests more than 1 percent of all pull requests opened on GitHub daily, with Nvidia, Coinbase, Decagon, and Vanta named as users.
The YC directory lists a team of about 35.
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

**Metered credits mean the reviewer's bill scales with your PR velocity, not your headcount, and since October 2026 that is literally true: Pro has no seat fees at all.**
Starter is free for one active developer with 50 credits per month; Pro dropped its $30-per-seat price for a pay-per-credit model, $1 per credit with credits shared across the whole organization and no seat fees (as of 2026-10-24).
Review depth is unchanged: Base at 1 credit, Plus at 3, and Apex at 10, selectable per review or by rule for large or high-risk PRs, so a review bills 1 to 10 credits no matter how many people work on the repo.
A startup program gives pre-Series A startups under $2M revenue 500 free credits a month for 6 months.
Free usage for qualified open source projects is advertised but, per the caution above, community reports dispute how this lands in practice.
Self-hosted enterprise and bulk API pricing are custom.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | Starter, Pro | Baseline: Starter free for one active developer (50 credits/mo), Pro $30/seat/mo with 50 credits included, extra credits $1 each, TREX reviews 3 credits; re-verified unchanged 2026-10-10. | [greptile.com](https://greptile.com/) |
| 2026-09-25 | Review depth tiers | Introduced Base (1 credit), Plus (3), and Apex (10) credits per review; Starter and Pro plan prices unchanged. | [greptile.com/blog/introducing-plus-and-apex](https://www.greptile.com/blog/introducing-plus-and-apex) |
| 2026-10 | Pro | Pro dropped the $30/seat/mo plan (50 credits included per seat): Pro is now $1 per credit with no seat fees, credits shared across the organization; Starter unchanged (free, one developer, 50 credits/mo); review-depth tiers unchanged; new startup program (500 free credits/mo for 6 months). Re-verified on the pricing page 2026-10-24. | [greptile.com/pricing](https://www.greptile.com/pricing) |

## Compared to

- [Sourcegraph code context platform](../../context-engines/sourcegraph-code-context/index.md): retrieval infrastructure priced at org level for any agent; choose Greptile when you want the reviewer and validator, not the index.
- [CodeRabbit](../coderabbit/index.md): the closest review-first rival with heavier marketing footprint; Greptile's differentiators are the learned-rules loop and self-hosting.
- [Augment Code](../../context-engines/augment-code/index.md): sells a full authoring-plus-review factory; choose Greptile when you want review independent of the tools that wrote the code.

## Bottom line

**Recommended for teams whose bottleneck is review throughput on a growing PR flood, especially with multiple coding agents authoring changes.**
Not for individuals priced out by per-credit metering or maintainers who need the OSS-free promise in writing.
My disagreeable claim: the graph index everyone credits Greptile for is the least valuable part of the product, and if a competitor shipped an identical index tomorrow with none of the learned-comment corpus, it would lose to Greptile on house-rule enforcement every time.

## Changes

- 2026-08-24 - Created among the seed notes of the Context engines category.
- 2026-08-30 - Moved into the new Code review category on category-fit grounds, with see-also links updated to its new siblings.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-10-16 - Rotation re-verification: recorded the Plus and Apex review-depth tiers (September 25, 2026, Base 1 credit, Plus 3, Apex 10) in Pricing with a Price history row, and the Claude Code plugin plus /greploop agent-iteration integration from the homepage; every cited URL re-fetched live, plan prices unchanged.
- 2026-10-24 - Rotation re-verification: recorded the $50M Series B led by Menlo Ventures (announced October 19, 2026, $750M valuation, Deedy Das joining the board) in Status, and the Pro restructure from $30/seat to $1-per-credit with no seat fees and a 500-credits startup program in Pricing with a Price history row; every cited URL re-fetched live.

## See also

- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - the category comparison this note joins
- [Sourcegraph code context platform](../../context-engines/sourcegraph-code-context/index.md) - the infra-only end of the same indexed-codebase bet
- [Semantic code search in coding tools](../../retrieval/semantic-code-search/index.md) - why graph indexes beat plain embeddings on cross-file questions
- [Tree-sitter code chunking](../../retrieval/tree-sitter-chunking/index.md) - the parsing layer Greptile's indexer builds on
- [Claude Code](../../harnesses/claude-code/index.md) - the agent most often on the receiving end of Greptile comments

## References

- https://greptile.com/ - product surface, customer list, team count, and pricing FAQ as claimed by the vendor, re-fetched 2026-10-24 (22,000+ teams still displayed)
- https://www.greptile.com/pricing - the plan table and the Base (1), Plus (3), Apex (10) credit FAQ, re-fetched 2026-10-24: Pro now $1 per credit with no seat fees, the $30/seat price gone, plus the 500-credit startup program
- https://www.greptile.com/blog/series-b - the October 19, 2026 Series B post: $50M led by Menlo Ventures, $750M valuation, participant list, Deedy Das joining the board, the 1-percent-of-GitHub-PRs claim and the Coinbase, Decagon, and Vanta customer names, fetched 2026-10-24
- https://www.greptile.com/blog/introducing-plus-and-apex - the September 25, 2026 review-depth-tier launch post, re-fetched 2026-10-24
- https://www.greptile.com/blog/series-a - $25M Series A led by Benchmark, v3 claims, 500M+ lines reviewed
- https://www.ycombinator.com/companies/greptile - YC W24 batch, founding year, founders, team size
- https://techcrunch.com/2024/06/06/greptile-raises-4m-to-build-an-ai-code-base-expert/ - $4M seed, API-first origin, customer counts at seed
- https://news.ycombinator.com/item?id=39604961 - launch thread: AST parsing, docstring embeddings, agentic search, and early criticism
- https://news.ycombinator.com/item?id=47966075 - the critical "predatory pricing" thread and OSS-billing allegations
