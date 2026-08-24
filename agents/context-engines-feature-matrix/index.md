---
title: "Context Engines Feature Matrix"
created: 2026-08-24
updated: 2026-08-24
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, comparison, context-engines, code-retrieval, developer-tools]
readability: 3
audience_notes: >
  Engineers shortlisting context engines for coding agents who need the capability deltas at a glance.
  Assumes you know what MCP, code intelligence, and token budgets mean; each column links to a full note with sources.
---

This matrix compares the four context engines profiled in this section, feature by feature, so the shortlisting step does not require reading four notes.
Everything below was verified against live sources on 2026-08-24.

**The interesting question is not which engine is best but whether a repository needs one at all: most codebases sit below the only published payback threshold in the category, and I claim most buyers of these engines are paying for an index their own vendors' data cannot justify.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [Augment Code](../augment-code/index.md) | [Greptile](../greptile/index.md) | [Repomix](../repomix/index.md) | [Sourcegraph](../sourcegraph-code-context/index.md) |
| --- | --- | --- | --- | --- |
| Kind | coding platform | review service, API | local CLI | search platform |
| Deployment | cloud SaaS | cloud plus self-host | local CLI | single-tenant cloud or self-host |
| Open source | ~ harness forks OSS Pi | ✗ | ✓ MIT | ~ SCIP only |
| Free tier | ✗ none | ✓ 50 credits, 1 dev | ✓ entirely | ~ public search only |
| Index model | real-time semantic index | code graph (files, functions, deps) | none, whole-repo pack | indexed search plus SCIP intel |
| Index freshness | real-time | post-commit | snapshot at pack time | index-dependent |
| Delivery to agents | own harness only | MCP, CLI, API | CLI pack, ~ MCP | MCP server |
| Scale where it pays | large private repos | PR-volume, not size | under a few hundred K tokens | 400K+ LOC |
| Writes code | ✓ agents and factory | ~ TREX tests, beta | ✗ packs only | ~ migrations, beta |
| Pricing model | $100 flat plus usage | $30/seat plus credits | free, MIT | from $16K/year |
| Enterprise orientation | ✓ SOC 2, ISO 42001 | ✓ SOC 2, self-host | ✗ | ✓ SOC 2, ISO 27001 |

## Reading the matrix

**This is not one market: a platform, a review service, a packer CLI, and a search platform share a category label but sell four different jobs.**
Augment sells the author-review-verify loop around its engine; Greptile sells validation on the PR stream; Repomix sells one deterministic file; Sourcegraph sells retrieval to whatever agent you already run.
The Writes code row makes the split visible: only Augment ships authoring agents, while Greptile's TREX and Sourcegraph's Agentic Batch Changes stay in the verification and migration lanes.

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
- Small or mid repo, one-shot whole-repo questions, onboarding packs, or a CI guard on context budget: Repomix, it is free.
- Code must stay on-device: Repomix locally, or Greptile and Sourcegraph self-hosted; Augment's engine stays in its cloud.

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
