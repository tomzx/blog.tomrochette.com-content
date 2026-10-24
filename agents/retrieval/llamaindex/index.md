---
title: LlamaIndex
created: 2026-08-24
updated: 2026-10-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, rag, retrieval, frameworks]
readability: 3
audience_notes: >
  Engineers choosing a framework for a RAG pipeline over documents or a codebase.
  Assumes hands-on familiarity with embeddings, vector stores, and chunking.

---

LlamaIndex is an MIT-licensed data framework for building retrieval pipelines and document agents over private data, now the open source arm of a company whose commercial product is the LlamaParse document platform.

**It remains the deepest off-the-shelf retrieval toolkit, but its maker has pivoted to enterprise document OCR, so the framework you build on is no longer the business you are buying from.**

## What it is

The framework provides data connectors, node parsers, indices (vector, property graph, keyword), retrievers, rerankers, query engines, agents, and event-driven workflows, with over 300 integration packages on LlamaHub.
**Code retrieval is a first-class case: the `CodeSplitter` node parser chunks source by tree-sitter language, and a newer `Chunker` node parser delegates to the [Chonkie](../chonkie/index.md) chunking library.**
The company, LlamaIndex (run-llama), sells LlamaParse: a closed platform spanning Parse (agentic OCR, 130+ formats), Extract, Index, Split, and deployed Agents, usable with or without the framework.
In February 2026 the same team also open-sourced [LiteParse](https://github.com/run-llama/liteparse), an Apache-2.0 Rust document parser that reached 12.8k stars by 2026-10-03.

## Status

Active and heavily used.
The `run-llama/llama_index` repository shows 52.5k stars and 8.3k forks as of 2026-10-13, pushed 2026-10-23 with 1,051 open issues counting pull requests (GitHub API, as of 2026-10-24), with 7,956 commits as of 2026-10-10.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=run-llama/llama_index&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=run-llama/llama_index&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=run-llama/llama_index&type=date&legend=top-left" />
</picture>

**The strategic signal is the pivot, and it deepened: the README's NOTE block now states the current focus is "the best AI-powered engine for document parsing and extraction", with LlamaParse the enterprise platform for agentic OCR and LiteParse the free parser, and ParseBench and ExtractBench added as the team's open parsing benchmarks.**

## Strengths

- **The broadest ingestion-to-query surface in open source RAG**: readers, vector stores, embeddings, and LLM providers are all pluggable.
- Retrieval research ideas ship as usable modules: sentence-window parsing, auto-merging retrievers, hybrid BM25, reciprocal rank fusion, property graph indexes.
- Tree-sitter code chunking is built in, which most general RAG stacks lack.
- MCP support lets LlamaIndex tools and retrievers serve agentic clients directly.

## Cautions

- **The framework is not the revenue**: LlamaParse is, so roadmap priority can drift toward document OCR rather than retrieval fundamentals.
- Community criticism of framework RAG is persistent: the 480-point Octomind thread describes "5 layers of abstraction" for small changes, naming both LangChain and LlamaIndex, and Chonkie's launch claims rivals' chunkers install 80-170MB and chunk up to 33x slower (vendor benchmarks, unverified).
- Docs churn: the README itself warns it lags the documentation, and the dual docs domains make citations rot quickly.
- LlamaParse is a closed SaaS; data leaves your tenant unless you pay for VPC or hybrid deployment.

## Pricing

Framework: free, MIT.
LlamaParse as of 2026-10-13: Free at 10k credits/month, Starter $50/month with 40k credits, Pro $500/month with 400k credits plus a limited-time one-time bonus of 800k credits listed at $1,000 for business-email domains, Enterprise custom, with 1,000 credits = $1.25 and pay-as-you-go above plan inclusion.
**You can use the OSS framework forever without LlamaParse; you just stop receiving the maintained parsing and managed index parts.**

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-18 | LlamaParse | Baseline: framework free (MIT); LlamaParse Free (10k credits/mo), Starter $50/mo (40k), Pro $500/mo (400k), Enterprise custom, credits at $1.25 per 1,000. | [llamaindex.ai/pricing](https://www.llamaindex.ai/pricing) |

## Compared to

- [LangChain](../langchain/index.md): wider agent platform with its own coding agent; choose it for orchestration-heavy systems, LlamaIndex for retrieval-heavy ones.
- A hand-rolled stack: Continue's custom code RAG guide (LanceDB plus a code embedding model plus an MCP server) replaces most of what a framework buys, in a few hundred lines you fully control.
- Raw provider SDKs: for a single-provider, single-corpus app, the abstraction tax is genuine and the HN thread above documents it.

## Bottom line

**Recommended for document-heavy RAG where ingestion variety and retrieval experiments matter, and for teams that want research-grade retrievers pre-built.**
I would not start a new code-search product on LlamaIndex in 2026: the coding tools that actually shipped retrieval built it by hand or stripped it back out, and I think the framework era of RAG is closing as agentic search eats indexed retrieval.
That claim is arguable, which is the point.

## Changes

- 2026-08-24 - Created among the four retrieval notes of the research index seeding run.
- 2026-09-06 - Added the LiteParse sentence and repository reference after folding the LiteParse candidate into the note.
- 2026-09-16 - Linked the new Chonkie note at the existing Chunker mention.
- 2026-09-18 - Refreshed volatile facts for the 2026-09-18 verification: 52.2k stars, 8.2k forks, 216 open issues (802 counting pull requests), 7,938 commits, and LiteParse at 12,325 stars, LlamaParse pricing re-confirmed unchanged.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-25 - Refreshed volatile facts: 231 open issues (858 counting pull requests), 7,943 commits, and LiteParse at 12,611 stars; LlamaParse pricing re-confirmed unchanged.
- 2026-10-07 - Added the run-llama/llama_index star history chart to the Status section.
- 2026-10-10 - Corrected the pivot wording: the README's NOTE block now states the focus is an AI-powered document parsing and extraction engine with LlamaParse the enterprise platform, LiteParse the free parser, and ParseBench and ExtractBench as open parsing benchmarks, replacing the "document agent and OCR platform" phrasing, and refreshed the repository numbers (52.5k stars, 270 open issues, 7,956 commits).
- 2026-10-11 - Reworded banned-term words out of the prose and refreshed the volatile numbers (271 open issues, 902 counting pull requests, LiteParse 12,824 stars); LlamaParse pricing re-verified unchanged.
- 2026-10-13 - Recorded the LlamaParse Pro plan's limited-time one-time bonus (800k credits listed at $1,000, business-email domains only) on tier prices otherwise unchanged.
- 2026-10-22 - Refreshed the repository activity (pushed 2026-10-21, 1,020 open issues counting pull requests).
- 2026-10-24 - Refreshed the repository activity (pushed 2026-10-23, 1,051 open issues counting pull requests).

## See also

- [LangChain](../langchain/index.md) - the other giant framework, now with a shipped coding-agent entry
- [Aider](../../harnesses/aider/index.md) - shipping retrieval without embeddings, via a graph-ranked repo map
- [VS Code Copilot](../../surfaces/vscode-copilot/index.md) - semantic code indexing as shipped by a mainstream tool
- [The Importance of Context When Interacting with LLMs](../../../the-importance-of-context-when-interacting-with-llms/index.md) - why retrieval quality dominates raw model choice

## References

- https://github.com/run-llama/llama_index - repository scale (52.5k stars), MIT license, the README's parsing-engine focus note and ParseBench and ExtractBench benchmarks, pushed 2026-10-23 (GitHub API, as of 2026-10-24; README re-verified unchanged 2026-10-22)
- https://github.com/run-llama/liteparse - the open-source Rust parser sibling, 12,824 stars, Apache-2.0, pushed 2026-10-09 (GitHub API, as of 2026-10-11)
- https://docs.llamaindex.ai/en/stable/ - framework documentation structure: RAG pipeline, agents, workflows, LlamaCloud
- https://developers.llamaindex.ai/python/framework/module_guides/loading/node_parsers/modules/ - CodeSplitter (tree-sitter) and Chunker (Chonkie) node parsers
- https://www.llamaindex.ai/pricing - LlamaParse tiers, credit pricing, the Pro plan's limited-time one-time 800k-credit bonus, VPC and compliance options, as of 2026-10-13 (tier prices unchanged since 2026-09-18)
- https://news.ycombinator.com/item?id=40739982 - critical framework-RAG discussion naming LlamaIndex, with the LangChain CEO response
- https://news.ycombinator.com/item?id=44225930 - Chonkie launch with benchmark claims against LlamaIndex and LangChain chunking
