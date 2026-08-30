---
title: "Context Engines Feature Matrix"
created: 2026-08-24
updated: 2026-08-30
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, context-engines, code-retrieval, developer-tools]
readability: 3
audience_notes: >
  Engineers shortlisting context engines for coding agents who need the capability deltas at a glance.
  Assumes you know what MCP, code intelligence, and token budgets mean; each column links to a full note with sources.
---

This matrix compares the seven context tools profiled in this section, feature by feature, so the shortlisting step does not require reading seven notes.
Everything below was verified against live sources on 2026-08-24, with the Graphify, qmd, and rtk columns verified 2026-08-30.

**The interesting question is not which engine is best but whether a repository needs one at all: most codebases sit below the only published payback threshold in the category, and I claim most buyers of these engines are paying for an index their own vendors' data cannot justify.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [Augment Code](../augment-code/index.md) | [Graphify](../graphify/index.md) | [Greptile](../greptile/index.md) | [qmd](../qmd/index.md) | [Repomix](../repomix/index.md) | [rtk](../rtk/index.md) | [Sourcegraph](../sourcegraph-code-context/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | coding platform | local knowledge-graph CLI | review service, API | local search engine | local CLI | CLI output proxy | search platform |
| Deployment | cloud SaaS | local CLI, enterprise early access | cloud plus self-host | local CLI plus daemon | local CLI | local binary | single-tenant cloud or self-host |
| Open source | ~ harness forks OSS Pi | ✓ Apache-2.0 | ✗ | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ~ SCIP only |
| Free tier | ✗ none | ✓ CLI entirely | ✓ 50 credits, 1 dev | ✓ entirely | ✓ entirely | ✓ CLI entirely | ~ public search only |
| Index model | real-time semantic index | deterministic AST knowledge graph, no vectors | code graph (files, functions, deps) | SQLite FTS5 plus vectors, markdown chunks | none, whole-repo pack | none, per-command output filtering | indexed search plus SCIP intel |
| Index freshness | real-time | snapshot at build time | post-commit | indexed, refreshed on update | snapshot at pack time | live per command | index-dependent |
| Delivery to agents | own harness only | skill in 20+ agents, MCP, CLI | MCP, CLI, API | CLI, MCP server, SDK, plugin | CLI pack, ~ MCP | hooks rewriting commands in 16 tools | MCP server |
| Scale where it pays | large private repos | repo-scale Q&A and path tracing | PR-volume, not size | personal docs and knowledge bases | under a few hundred K tokens | long interactive sessions with noisy commands | 400K+ LOC |
| Writes code | ✓ agents and factory | ✗ graphs and queries | ~ TREX tests, beta | ✗ searches only | ✗ packs only | ✗ filters output | ~ migrations, beta |
| Pricing model | $100 flat plus usage | free core, enterprise unpriced | $30/seat plus credits | free, MIT | free, MIT | free CLI, Pro unpriced | from $16K/year |
| Enterprise orientation | ✓ SOC 2, ISO 42001 | ~ early-access platform | ✓ SOC 2, self-host | ✗ | ✗ | ~ Pro tier, on-prem option | ✓ SOC 2, ISO 27001 |

## Reading the matrix

**This is not one market: a platform, a graph CLI, a review service, a search engine, a packer CLI, an output proxy, and a search platform share a category label but sell seven different jobs.**
Augment sells the author-review-verify loop around its engine; Graphify sells structural reasoning about one codebase; Greptile sells validation on the PR stream; qmd sells local retrieval over your documents; Repomix sells one deterministic file; rtk sells cheaper command output; Sourcegraph sells retrieval to whatever agent you already run.
The Writes code row makes the split visible: only Augment ships authoring agents, while Greptile's TREX and Sourcegraph's Agentic Batch Changes stay in the verification and migration lanes, and the 2026 columns refuse the code-writing job entirely.

**I read the delivery row as the lock-in axis the marketing never names.**
Sourcegraph and Greptile speak MCP (plus API and CLI surfaces) to any agent; Repomix hands a plain file to anything that reads; Augment's Context Engine only drives Augment's own surfaces, so its documented token savings are purchasable only inside its own harness.

**The scale row is where the budget decision lives, and the only published threshold belongs to Sourcegraph.**
Its own CodeScaleBench reports a +0.259 reward delta with agents 30% cheaper and 38% faster in the 400K-2M LOC range, and a slightly negative -0.080 below 400K LOC.
Repomix inverts that curve: it pays off under a few hundred thousand tokens, then whole-window packing degrades linearly.
Augment claims the large-private-repo end but publishes no size threshold, and Greptile's value scales with PR velocity rather than repository size.

**Freshness splits real-time from snapshot, and it bites exactly when an agent is mid-edit.**
Augment indexes in real time; Greptile's graph is post-commit; Repomix is a snapshot invalidated by every edit; Sourcegraph depends on index lag it inherits from its architecture.

**Every efficiency number in this matrix is vendor-run, and the pricing floors span free to $16K.**
Augment's 33% token savings, Greptile's bug-catch multiples, and Sourcegraph's cost deltas all come from the vendors' own blogs; Augment at least publishes methodology alongside the numbers, which is the category's best practice even if no third party has replicated any of it.

## Choosing from the matrix

- Multi-repo organization past 400K LOC with agents thrashing on local search and an enterprise budget: Sourcegraph.
- Token-heavy team on one large private repo wanting a single vendor for authoring and review: Augment, after re-running its benchmark on your own repo first.
- Review throughput is the bottleneck, especially with multiple agents authoring PRs: Greptile.
- Agents re-discovering how one large codebase connects, with structure and citations preferred: Graphify, after verifying its self-published benchmarks on your repo.
- Local search over personal docs, notes, and knowledge bases for humans and agents: qmd, it is free and local.
- Small or mid repo, one-shot whole-repo questions, onboarding packs, or a CI guard on context budget: Repomix, it is free.
- Metered-API sessions dominated by noisy test, git, and search output: rtk, measuring with `rtk gain` before believing the savings.
- Code must stay on-device: Graphify and Repomix locally, qmd and rtk entirely, or Greptile and Sourcegraph self-hosted; Augment's engine stays in its cloud.

## See also

- [Context Management Patterns](../context-management-patterns/index.md) - the manual practices this category productizes
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the agents that consume what these engines deliver
- [MCP](../mcp/index.md) - the protocol behind the delivery row
- [Semantic code search in coding tools](../semantic-code-search/index.md) - whether indexed retrieval survives inside editors at all

## References

- https://www.augmentcode.com/context-engine - Context Engine mechanics and efficiency claims for the Augment column
- https://www.augmentcode.com/pricing - flat Business plan and the 40% service fee for the Augment column
- https://greptile.com/ - product surface, integrations, and per-seat credit pricing for the Greptile column
- https://github.com/yamadashy/repomix - CLI surface, output formats, token budgets, and MCP mode for the Repomix column
- https://sourcegraph.com/pricing - enterprise entry price and credits model for the Sourcegraph column
- https://sourcegraph.com/blog/why-coding-agents-fail-large-codebases - the 400K LOC threshold and the cost/speed deltas
- https://github.com/Graphify-Labs/graphify - the AST knowledge-graph architecture and license for the Graphify column
- https://github.com/tobi/qmd - the hybrid local search stack for the qmd column
- https://github.com/rtk-ai/rtk - the output-filtering strategies and agent integrations for the rtk column
