---
title: Outlines
created: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, structured-outputs, constrained-decoding, open-source]
readability: 3
audience_notes: >
  Engineers running open-weight models locally or behind their own serving stack who need guaranteed structured output.
  Assumes familiarity with token-level generation and one inference backend (transformers, vLLM, llama.cpp).

---

Outlines is an Apache-2.0 Python library that guarantees LLM outputs follow a type, JSON Schema, regex, or context-free grammar by masking logits during generation instead of validating afterward.
Facts below verified as of 2026-09-02.

**It proved constrained decoding could be practical (the finite-state-machine-over-vocabulary idea dates to its 2023 paper), but the serving-engine fast lane has since been taken by XGrammar and llguidance, leaving Outlines the role of portable front-end and abstraction layer.**

## What it is

**You specify the output type, not a prompt discipline.**
A call like `model(prompt, output_type)` accepts a Python `Literal`, `int`, a Pydantic model, a regex, or an EBNF grammar, and Outlines compiles it into a logit mask that makes invalid tokens unsampleable.
It connects to transformers, llama.cpp, MLX-LM, vLLM (online and offline), SGLang, TGI, and Ollama, plus the OpenAI, Anthropic, and Gemini APIs, and its API reference now lists pluggable generation backends: outlines-core, llguidance, and xgrammar.
It began at Normal Computing (Brandon Willard and Remi Louf) and is maintained by .txt (dottxt), which sells the Dottxt API and commercially licensed libraries on top of the same research.

## Status

**Active, with an asterisk on where its own engine still runs.**
The repository shows about 15.7k stars and 1,325 commits as of 2026-09-02, and the docs claim adoption by the major serving frameworks and by companies from Amazon to Shopify (self-reported where not public).
But vLLM's current structured-outputs docs name xgrammar and guidance as its backends, and vLLM removed the old `guided_*` request fields in v0.12.0, so the engine-level default no longer runs Outlines' compiler there.
XGrammar's November 2024 benchmarks (competitor-run) measured existing solutions, Outlines included, at up to 3.5x slower mask generation on JSON schemas and more than 10x slower on context-free grammars.

## Strengths

- **One type-driven API across local, self-hosted, and hosted models**, which no single vendor feature matches.
- Coverage beyond JSON: regex and full CFGs handle SQL, code fragments, and recursive structures that vendor schema subsets reject.
- Compilation happens once per schema, so steady-state overhead is microseconds rather than retry round trips.
- The 2023 paper's indexing formulation is the foundation the entire constrained-decoding wave builds on, including the vendor implementations.

## Cautions

- **It is no longer the performance frontier**: XGrammar-2 shipped in May 2026 and powers defaults in vLLM, SGLang, and TensorRT-LLM, and vLLM deprecated the guided API Outlines rode in on.
- The benchmarks against it are vendor-run; treat the multiples as directional rather than gospel.
- Hard constraints fix structure, not truth: a schema-valid extraction can still be wrong, and constrained decoding has its own rare loop-until-`max_tokens` failure mode, as OpenAI staff described for their equivalent feature.
- The .txt commercial layer means the best-supported path is drifting toward the paid Dottxt API and enterprise libraries.

## Pricing

Apache-2.0 and free.
The adjacent money is .txt's: the Dottxt API (early access) and enterprise libraries sell the same guarantees without the self-hosting, as of 2026-09-02.

## Compared to

- XGrammar: the C++-core engine that vLLM, SGLang, and TensorRT-LLM default to; choose it (or llguidance) inside a serving engine when throughput matters.
- Instructor: validation and retries above any API; choose it when you cannot touch the serving stack or need semantic validation.
- Vendor structured outputs (OpenAI, Anthropic): the same guarantee as a platform feature; choose them when you are on those APIs anyway.

## Bottom line

**Recommended as the portability layer for type-constrained generation across mixed local and hosted models, and for anything regex- or grammar-based that vendor JSON subsets cannot express.**
The disagreeable part: I would not build a new high-throughput serving stack on Outlines' own engine in 2026; its durable value is the API and the original idea, and the engines have moved on.
Not for teams that only ever call OpenAI or Anthropic and never serve their own models.

## See also

- [OpenAI Structured Outputs](../openai-structured-outputs/index.md) - the vendor feature that industrialized the idea Outlines proved
- [Anthropic structured outputs](../anthropic-structured-outputs/index.md) - the same mechanism with a narrower schema subset
- [Instructor](../instructor/index.md) - the validate-and-retry alternative when decoding cannot be constrained

## References

- https://github.com/dottxt-ai/outlines - repo: stars, license, output types, integrations, .txt stewardship (as of 2026-09-02)
- https://dottxt-ai.github.io/outlines/latest/ - docs: features, pluggable backends, Normal Computing origin, Dottxt API
- https://arxiv.org/abs/2307.09702 - the 2023 paper introducing the FSM-vocabulary index behind guided generation
- https://docs.vllm.ai/en/latest/features/structured_outputs.html - vLLM backends (xgrammar, guidance) and removal of guided_* fields in v0.12.0
- https://blog.mlc.ai/2024/11/22/achieving-efficient-flexible-portable-structured-generation-with-xgrammar - competitor benchmarks vs Outlines and engine integration history
- https://github.com/mlc-ai/xgrammar - adoption timeline and XGrammar-2 release in May 2026
- https://simonwillison.net/2024/Aug/6/openai-structured-outputs/ - independent context on constrained-output failure modes (looping until max_tokens)
