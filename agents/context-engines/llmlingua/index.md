---
title: LLMLingua
created: 2026-10-10
updated: 2026-10-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, context-engines, compression, prompt-compression, research]
readability: 3
audience_notes: >
  Engineers weighing prompt compression against retrieval and packing for long
  natural-language contexts, who want the peer-reviewed baseline underneath this
  category's newer compression products. Assumes you know what perplexity,
  token classification, and in-context learning are.
---

LLMLingua is Microsoft Research's MIT-licensed prompt-compression toolkit, a Python library that deletes the tokens a small model judges unimportant before a large model ever reads the prompt.

**LLMLingua is the peer-reviewed ancestor of this category's compression products, and the newest independent evaluation hands back an uncomfortable verdict: its token pruning is exactly the kind that fails on code, the input this category exists to serve.**

## What it is

A family of four methods behind one `pip install llmlingua` entry point: LLMLingua (perplexity-based token pruning with a small causal LM such as GPT-2 or a sub-8GB quantized Llama-2-7B, claiming up to 20x compression with little loss), LongLLMLingua (question-aware compression plus document reordering that attacks lost-in-the-middle, claiming up to 21.4 percent better RAG performance on a quarter of the tokens), LLMLingua-2 (compression distilled from GPT-4 into a BERT-class token classifier, task-agnostic, 3x to 6x faster and better out-of-domain), and SecurityLingua (security-aware compression that exposes jailbreak intent, CoLM 2025).
It is a library for pipeline builders, not an agent tool: delivery is the Python API plus integrations written into LangChain (document compressor), LlamaIndex (node postprocessor), and Microsoft Prompt flow, with no MCP server, no proxy, and no hooks.
MIT-licensed, built by the Microsoft Research group behind the papers (Huiqiang Jiang, Chin-Yew Lin, Lili Qiu, and colleagues), running anywhere a Hugging Face model runs.

## Status

Research-mature and in maintenance: 6,746 stars and 437 forks since 2023-07-07, pushed 2026-09-10, 124 open issues, as of 2026-10-13 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=microsoft/LLMLingua&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=microsoft/LLMLingua&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=microsoft/LLMLingua&type=date&legend=top-left" />
</picture>

The PyPI package has been frozen at 0.2.2 since 2024-04-09 (14 releases total), and the GitHub release train stopped at the same version, while main keeps receiving pushes that never reach pip users.
The team's news feed has moved to KV-cache infrastructure (SCBench, RetrievalAttention, MInference), the layer underneath a prompt compressor once token pruning is done.
The launch HN thread (December 2023) drew 149 points and 47 comments, a discussion footprint most of this category's young tools would envy.

## Strengths

- The evidence base is the strongest in the category: two peer-reviewed compression papers (EMNLP 2023, ACL 2024 main and Findings) plus SecurityLingua at CoLM 2025, where every other compressor here is self-benchmarked.
- LLMLingua-2's distillation insight, formulating compression as token classification with a bidirectional encoder, is the design this category's newer products are reinventing with worse evaluation.
- The compressors are small (mBERT or XLM-RoBERTa-large, or a sub-8GB quantized 7B for the original method), so the pruning pass fits on commodity hardware.
- Distribution already exists where long prompts live, through the LangChain, LlamaIndex, and Prompt flow integrations.

## Cautions

- The independent multi-dimensional evaluation (April 2026) found code completion, few-shot, and structure-dependent tasks degrade or fail under compression, precisely the inputs coding agents would feed it; summarization and QA held up.
- The same study found end-to-end speedups above 1.3x only in narrow conditions on optimized serving stacks, and LLMLingua-1 missed requested compression rates badly enough to make API bills and quality unpredictable; only LLMLingua-2 was called practical.
- Compression here is destructive with no retrieve path: what the small model deletes is gone, so an aggressive rate silently removes the fact the answer needed.
- The package has been frozen at 0.2.2 since April 2024 while development continues without releases, so fixes do not reach pip users, and contributions require a Microsoft CLA.

## Pricing

Free and open source under MIT; there is no paid tier, so pricing does not apply.
The costs are your own hardware for the compressor model and the tokens you fail to save.

## Compared to

- [Headroom](../headroom/index.md): the productized successor surface (proxy, wrap, MCP) whose reversible compress-then-retrieve design answers LLMLingua's worst property, backed by seeded self-benchmarks instead of peer review.
- [rtk](../rtk/index.md): compresses the other channel, command output after the model call, where LLMLingua compresses the prompt before it.
- [TOON](../toon-format/index.md): the lossless extreme, re-encoding structured data exactly rather than deleting tokens approximately.

## Bottom line

**Recommended for pipeline builders compressing very long natural-language prompts (RAG chunks, transcripts, few-shot demonstrations) who will measure downstream quality at their target ratio, ideally on LLMLingua-2.**
Not for code context, which the independent evidence says does not survive token pruning, and not as an agent-loop component unless the original prompt is kept.
My disagreeable claim: the newer compression products in this category are selling LLMLingua's ideas back to practitioners with weaker evaluation, and a buyer who starts from the papers will demand the reversibility the papers never offered.

## Changes

- 2026-10-10 - Created from the 2026-10-10 Meirtz/Awesome-Context-Engineering scan (the list's LongLLMLingua entry), with the April 2026 independent evaluation recorded as the critical source.

## See also

- [Headroom](../headroom/index.md) - the agent-native compression layer built on the same token-classification idea
- [rtk](../rtk/index.md) - the output-side filter in the same token-bill fight
- [TOON](../toon-format/index.md) - the lossless packing counterpoint
- [Context Engines Feature Matrix](../context-engines-feature-matrix/index.md) - the category comparison this note joins as the fifteenth column

## References

- https://api.github.com/repos/microsoft/LLMLingua - repository stats, MIT license, and activity as of 2026-10-10
- https://raw.githubusercontent.com/microsoft/LLMLingua/main/README.md - the method family, quick-start surfaces, framework integrations, and the KV-cache news line
- https://pypi.org/pypi/llmlingua/json - the package, frozen at 0.2.2 since 2024-04-09, 14 releases
- https://arxiv.org/abs/2310.05736 - the LLMLingua paper (EMNLP 2023): coarse-to-fine compression, up to 20x with little loss
- https://arxiv.org/abs/2310.06839 - the LongLLMLingua paper (ACL 2024): long-context compression and document reordering
- https://arxiv.org/abs/2403.12968 - the LLMLingua-2 paper (ACL 2024 Findings): distillation into BERT-class token classification
- https://arxiv.org/abs/2604.02985 - the independent critical evaluation (April 2026): latency overhead, rate-adherence failures, and the code-completion degradation
- https://hn.algolia.com/api/v1/items/38689653 - the launch thread, 149 points and 47 comments, December 2023
- https://www.microsoft.com/en-us/research/project/llmlingua/ - the Microsoft Research project page and its stated insights
