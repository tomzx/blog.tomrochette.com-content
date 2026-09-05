---
title: LlamaIndex
created: 2026-08-24
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, rag, retrieval, frameworks]
readability: 3
audience_notes: >
  Engineers choosing a framework for a RAG pipeline over documents or a codebase.
  Assumes hands-on familiarity with embeddings, vector stores, and chunking.

---

LlamaIndex is an MIT-licensed data framework for building retrieval pipelines and document agents over private data, now the open source arm of a company whose commercial product is the LlamaParse document platform.
Facts below verified as of 2026-09-05.

**It remains the deepest off-the-shelf retrieval toolkit, but its maker has pivoted to enterprise document OCR, so the framework you build on is no longer the business you are buying from.**

## What it is

The framework provides data connectors, node parsers, indices (vector, property graph, keyword), retrievers, rerankers, query engines, agents, and event-driven workflows, with over 300 integration packages on LlamaHub.
**Code retrieval is a first-class case: the `CodeSplitter` node parser chunks source by tree-sitter language, and a newer `Chunker` node parser delegates to the Chonkie chunking library.**
The company, LlamaIndex (run-llama), sells LlamaParse: a closed platform spanning Parse (agentic OCR, 130+ formats), Extract, Index, Split, and deployed Agents, usable with or without the framework.

## Status

Active and heavily used.
The `run-llama/llama_index` repository shows 52.0k stars, 8.1k forks, 7,928 commits, and 193 open issues as of 2026-09-05.
**The strategic signal is the pivot: the repository now describes itself as "the leading document agent and OCR platform", and the docs split between the legacy `docs.llamaindex.ai` site and the new `developers.llamaindex.ai` home, where some legacy API pages (the code splitter reference among them) no longer resolve.**

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
LlamaParse as of 2026-09-02: Free at 10k credits/month, Starter $50/month with 40k credits, Pro $500/month with 400k credits, Enterprise custom, with 1,000 credits = $1.25 and pay-as-you-go above plan inclusion.
**You can use the OSS framework forever without LlamaParse; you just stop receiving the maintained parsing and managed index parts.**

## Compared to

- [LangChain](../langchain/index.md): wider agent platform with its own coding agent; choose it for orchestration-heavy systems, LlamaIndex for retrieval-heavy ones.
- A hand-rolled stack: Continue's custom code RAG guide (LanceDB plus a code embedding model plus an MCP server) replaces most of what a framework buys, in a few hundred lines you fully control.
- Raw provider SDKs: for a single-provider, single-corpus app, the abstraction tax is real and the HN thread above documents it.

## Bottom line

**Recommended for document-heavy RAG where ingestion variety and retrieval experiments matter, and for teams that want research-grade retrievers pre-built.**
I would not start a new code-search product on LlamaIndex in 2026: the coding tools that actually shipped retrieval built it by hand or stripped it back out, and I think the framework era of RAG is closing as agentic search eats indexed retrieval.
That claim is arguable, which is the point.

## See also

- [LangChain](../langchain/index.md) - the other giant framework, now with a real coding-agent entry
- [Aider](../aider/index.md) - shipping retrieval without embeddings, via a graph-ranked repo map
- [VS Code Copilot](../vscode-copilot/index.md) - semantic code indexing as shipped by a mainstream tool
- [The Importance of Context When Interacting with LLMs](../../the-importance-of-context-when-interacting-with-llms/index.md) - why retrieval quality dominates raw model choice

## References

- https://github.com/run-llama/llama_index - repository scale (52.0k stars), MIT license, pivot to "document agent and OCR platform", as of 2026-09-02
- https://docs.llamaindex.ai/en/stable/ - framework documentation structure: RAG pipeline, agents, workflows, LlamaCloud
- https://developers.llamaindex.ai/python/framework/module_guides/loading/node_parsers/modules/ - CodeSplitter (tree-sitter) and Chunker (Chonkie) node parsers
- https://www.llamaindex.ai/pricing - LlamaParse tiers, credit pricing, VPC and compliance options, as of 2026-09-02
- https://news.ycombinator.com/item?id=40739982 - critical framework-RAG discussion naming LlamaIndex, with the LangChain CEO response
- https://news.ycombinator.com/item?id=44225930 - Chonkie launch with benchmark claims against LlamaIndex and LangChain chunking
