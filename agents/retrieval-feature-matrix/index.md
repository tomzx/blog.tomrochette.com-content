---
title: "Retrieval Feature Matrix"
created: 2026-08-24
updated: 2026-08-26
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, comparison, retrieval, rag, code-retrieval]
readability: 3
audience_notes: >
  Engineers choosing between retrieval frameworks, shipped semantic search, and chunking strategies for agentic coding.
  Assumes you know what embeddings, vector stores, and RAG mean; each column links to a full note with sources.
---

This matrix compares the four retrieval entries profiled in this section, two frameworks and two patterns, feature by feature, so the shortlisting step does not require reading four notes.
Everything below was verified against live sources on 2026-08-24.

**Both frameworks are pivoting away from retrieval as their business, both patterns are being demoted by the tools that ship them, and I read that as evidence that the agent loop, not the index, is now the retrieval layer, a claim the enterprise platform bets are still arguing.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [LlamaIndex](../llamaindex/index.md) | [LangChain](../langchain/index.md) | [Semantic code search](../semantic-code-search/index.md) | [Tree-sitter chunking](../tree-sitter-chunking/index.md) |
| --- | --- | --- | --- | --- |
| Kind | retrieval framework | agent framework | shipped capability | parsing technique |
| Open source license | ✓ MIT | ✓ MIT | ~ tool-dependent | ✓ MIT parsers |
| Primary language | Python | Python | ~ varies by tool | C11 core |
| Code-specific focus | ~ general data, code capable | ~ generic text RAG | ✓ code only | ✓ code only |
| AST-aware code splitting | ✓ CodeSplitter | ✗ separators only | ? chunkers undisclosed | ✓ the technique |
| Hosted or commercial arm | ✓ LlamaParse SaaS | ✓ LangSmith SaaS | ~ plan-gated indexes | ~ Chonkie sells one |
| Positioning drift in the notes | ~ pivot to document OCR | ~ climb to agent platform | ~ demoted to optional | ~ outsourced to Chonkie |
| Maintenance status | ✓ active, 51.8k stars | ✓ active, 144.9k stars | ~ active but demoted | ✓ mature, pervasive |
| Displacement signal in the notes | ~ agentic search eats indexed RAG | ~ retrieval commoditized | ✓ pioneers shipped grep loops | ~ ranked below truncation |
| What it replaces in a coding-agent stack | hand-rolled retrievers | hand-rolled agent loops | grep-only lookups | line-count chunking |

## Reading the matrix

**The two frameworks are the healthiest entries and the least committed to retrieval: the giants of the category are both diversifying away from the job you would hire them for.**
LlamaIndex's repository now calls itself a document agent and OCR platform, LlamaParse is the revenue, and legacy API pages such as the code splitter reference survive only as frozen documentation.
LangChain repositioned as an agent engineering platform with its own terminal coding agent, and my own call in its note is to stop picking it purely for RAG.

**The pattern columns carry the shipped verdict: semantic indexes are being demoted inside the tools that pioneered them, and the chunking strategy called most exact is ranked last by the practitioners who documented their pipeline.**
Cursor's retrieval docs lead with Instant Grep and an Explore subagent, Continue deprecated its `@Codebase` embeddings provider, and VS Code ships a no-index fallback.
Continue's custom code RAG guide ranks truncation and fixed-length chunking above AST chunking because a 16k-token embedding model fits most whole files.

**The context-management-patterns essay argues that harness-native features beat bespoke RAG below a few hundred thousand lines of code, and this matrix is that claim's evidence table.**
Every drift row points the same direction, and the essay's Sourcegraph data (a negative reward delta below 400K LOC from the vendor's own benchmark) sets the threshold.
The live counterargument sits in the commercial-arm row: Devin Desktop doubles down on a RAG context engine and VS Code moved its index to the GitHub platform, so indexed retrieval may survive as an enterprise service even as local indexes disappear.

**Code-specific machinery is thinnest exactly where you would buy it: the biggest framework offers separator-based splitting only, and the deepest AST chunking route now runs through a third-party commercial chunker.**
LangChain's text splitters catalog has no AST chunker at all.
LlamaIndex's newer Chunker node parser wraps Chonkie rather than reimplementing chunking, which tells you where maintainers think the effort should live.

## Choosing from the matrix

- Ingestion-heavy document RAG across many formats: LlamaIndex, pricing LlamaParse only if you want the maintained parsing.
- Multi-provider agent systems that also need retrieval: LangChain plus LangSmith, accepting generic text splitters.
- Want concept lookup in an editor today: use the shipped semantic search where present, but keep a grep-first workflow; do not design around the index existing.
- Building your own code RAG: start with truncation and fixed-length chunking, and adopt tree-sitter chunking only when measurements on your corpus earn the complexity.
- Repo below a few hundred thousand lines: skip the category and learn compaction, subagents, and memory files first.
- Past that threshold: build on framework machinery or a dedicated chunker, and deliver the index to your harness via MCP.

## See also

- [Context Management Patterns](../context-management-patterns/index.md) - the size-threshold argument this matrix leans on
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the terminal agents that consume all of this retrieval
- [Surface Feature Matrix](../surface-feature-matrix/index.md) - the editors shipping or dropping these indexes
- [Aider](../aider/index.md) - the no-embeddings counterexample via graph-ranked repo maps

## References

- https://github.com/run-llama/llama_index - repository scale, MIT license, and the document-agent and OCR pivot wording for the LlamaIndex column
- https://www.llamaindex.ai/pricing - LlamaParse tiers grounding the commercial-arm row
- https://github.com/langchain-ai/langchain - repository scale, MIT license, and agent-platform positioning for the LangChain column
- https://python.langchain.com/api_reference/text_splitters/text_splitters/code_splitter.html - separator-based code splitting only, grounding the AST row
- https://cursor.com/docs/context/codebase-indexing - Instant Grep first and encrypted chunks for the semantic search column
- https://docs.continue.dev/reference/deprecated-codebase - the deprecated local embeddings pipeline for the displacement row
- https://docs.continue.dev/guides/custom-code-rag - the chunking strategy ranking (truncate, fixed-length, AST) for the tree-sitter column
- https://tree-sitter.github.io/tree-sitter/ - parser properties (incremental, error-robust, C11) for the technique column
