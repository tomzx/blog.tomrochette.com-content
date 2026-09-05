---
title: deepeval
created: 2026-08-30
updated: 2026-09-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation, llm-as-judge, testing, open-source]
readability: 3
audience_notes: >
  Engineers who want LLM outputs gated in CI like ordinary test failures.
  Assumes you know pytest and what an LLM-as-judge metric is.
---

deepeval is an Apache-2.0, pytest-style unit-testing framework for LLM applications that scores outputs with LLM-as-a-judge metrics, G-Eval, task completion, faithfulness, and roughly fifty more, so eval failures gate code like ordinary test failures.
Facts below verified as of 2026-09-05.

**deepeval is the category's default answer to the question where do evals live, and its answer is your existing test suite, which is exactly why the open-core line around the Confident AI platform is the decision that matters.**

## What it is

A Python SDK (3.9+) with a beta TypeScript SDK (47 of 49 metrics ported) where evals are pytest tests: `deepeval test run` exits non-zero on failure, so any CI blocks merges on regression.
Metric families cover agentic evaluation (task completion, tool correctness, plan adherence), RAG (faithfulness, contextual precision and recall), multi-turn chat, MCP, multimodal, safety (bias, toxicity, PII), and deterministic non-LLM checks, plus synthetic dataset generation and prompt optimization (GEPA, MIPROv2).
Any LLM can judge, including Ollama and vLLM local models, and tracing integrations cover OpenAI, Anthropic, LangChain, LlamaIndex, CrewAI, and Pydantic AI.
Made by Confident AI, a seed-stage San Francisco company, Apache-2.0.

## Status

The volume leader of Python eval frameworks: 18,093 stars, 1,892 forks, 559 open issues and PRs as of 2026-09-04.
Created 2023-08-10, pushed 2026-09-03, Python v4.2.1 released 2026-09-03, about 4.4 million PyPI downloads a month as of 2026-09-04.
**Three years old and commercially backed, it is the most mature column in this category, and the 560-issue backlog reads as heavy usage rather than neglect.**

## Strengths

- Native pytest and CI fit: evals are ordinary tests with a non-zero exit on failure, the integration every rival bolts on afterward.
- The largest ready-made metric library in the category, each with a self-explanation for debugging.
- Judge-model freedom including fully local judges, plus deterministic metrics for schema and exact-match checks.
- Verified traction and sustained release cadence.

## Cautions

- Most flagship metrics are LLM-as-judge: non-deterministic, prompt-sensitive, and billed to your judge key on every run.
- The open-core split is real: comparisons, regression tracking, datasets, and online evals live in the paid Confident AI platform, and `deepeval login` is "highly recommended" while auto-logging test cases to their cloud unless you opt out.
- The TypeScript SDK is explicitly not score-parity-verified against Python.
- Docs-quality criticism at launch has been addressed but 559 open issues signal friction.

## Pricing

OSS is free, Apache-2.0, fully local with your own judge key.
Confident AI platform: Free (2 seats, 5 test runs per week), Starter $200/month, Team $2,000/month, Enterprise custom with on-prem and HIPAA.

## Compared to

- [Workshop](../workshop/index.md): agent-authored evals inside a local debug loop; choose deepeval when the eval suite must gate CI.
- [Phoenix](../phoenix/index.md): observability-first with evals attached to traces; choose deepeval when test-first regression is the job, and note Phoenix's core is ELv2 while deepeval is Apache-2.0.
- promptfoo: config-driven declarative evals and red teaming, now part of OpenAI; choose it for YAML-driven cross-model comparison without Python.

## Bottom line

**Recommended for Python teams that want LLM behavior under the same merge gate as unit tests, with deliberate opt-outs configured for the cloud logging.**
Not for teams that cannot tolerate LLM-judge variance, or that need score parity across Python and TypeScript today.

## See also

- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [Phoenix](../phoenix/index.md) - the trace-attached eval alternative
- [Workshop](../workshop/index.md) - the local agent-loop alternative
- [Hamel Husain](../hamel-husain/index.md) - the methodological grounding for judge-based evals

## References

- https://github.com/confident-ai/deepeval - repository, metric list, license, adoption numbers
- https://docs.confident-ai.com/ - the metric taxonomy and integrations
- https://www.confident-ai.com/pricing - the platform tiers behind the open-core split
- https://deepeval.com/blog/introducing-deepeval-typescript - the TypeScript beta scope and parity caveat
- https://pypistats.org/api/packages/deepeval/recent - the download figures as of 2026-09-04
- https://news.ycombinator.com/item?id=37157323 - the launch thread with early criticism and maintainer response
