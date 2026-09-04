---
title: Instructor
created: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, structured-outputs, pydantic, validation]
readability: 3
updated: 2026-08-30
audience_notes: >
  Python engineers who want typed, validated LLM outputs across multiple providers.
  Assumes working knowledge of Pydantic and of at least one provider API.

---

Instructor is an MIT-licensed Python library (with TypeScript, Go, Ruby, Elixir, and Rust ports) that returns Pydantic objects from LLM calls and re-asks the model when validation fails.
Facts below verified as of 2026-09-04.

**Its core loop, validate-then-reask with the error fed back to the model, remains the portable way to enforce rules no vendor schema constraint can express, even after native structured outputs absorbed the baseline JSON-validity problem.**

## What it is

**A thin patch over provider SDKs, not a framework.**
You wrap a client with `instructor.from_provider("openai/gpt-4o")`, pass `response_model=SomePydanticModel`, and get a typed instance back, with the same interface covering 15+ providers including Anthropic, Gemini, Ollama, vLLM, and LiteLLM.
Failed Pydantic validations trigger automatic retries (default `max_retries=3`) that send the validation error back to the model.
It also streams partial objects, iterates lists, exposes hooks for logging and monitoring, and was created by Jason Liu; it now lives under the 567-labs organization.

## Status

**Active and mainstream.**
The repository shows about 13.8k stars and 1,629 commits as of 2026-09-02, and PyPI shows release 1.16.0 on August 27, 2026 in a cadence of monthly-plus releases stretching back to 2023.
The README claims 3M+ monthly downloads and use inside OpenAI, Google, Microsoft, and AWS teams; PyPI counters with roughly 27M downloads over the last month as of 2026-08-30, so the README claim is if anything conservative.
OpenAI publicly credited Instructor as inspiration for its native SDK structured-output helpers at the August 2024 Structured Outputs launch, and the project's own README now steers agent use cases to PydanticAI, the Pydantic team's agent runtime.

## Strengths

- **Validation beyond the schema**: field validators encode business rules (age must be positive, hours in 0.5 increments) that grammar constraints cannot express.
- One `response_model` interface across hosted and local providers, which matters when you switch models or run Ollama.
- Reasking with the error message fixes semantic problems (wrong field meaning), not just syntax.
- Small enough to read and debug, which is exactly how its README positions it against LangChain and LlamaIndex.

## Cautions

- **Every retry is a full model call**, so latency and token cost scale with failure count; constrained decoding beats it for pure schema compliance.
- On OpenAI and Anthropic the library's value shrank once those APIs enforced schemas natively; it is now chiefly the cross-provider and business-rules layer.
- Adoption numbers are vendor marketing until independently verified.
- The maintainers themselves recommending PydanticAI for agents signals the scope ceiling they see for this library.

## Pricing

MIT-licensed and free.
You pay only the underlying provider's token costs, including any retry calls.

## Compared to

- Native OpenAI or Anthropic structured outputs: enforce schema at decoding time with no retries; choose them first for pure schema compliance on those providers.
- Outlines: constrained decoding for models you serve yourself, guaranteeing at generation instead of validating afterward.
- PydanticAI: the maintainer-recommended escalation when extraction grows into agents with tools, evals, and observability.

## Bottom line

**Recommended as the default extraction layer for multi-provider Python code, and as the only layer when your constraints are semantic rather than structural.**
The disagreeable part: I think most single-provider Instructor deployments written after 2025 are incidental complexity, and the minimal correct design is native structured outputs plus a thin Pydantic validation step.
Not for teams that need agents, evals, or hard latency budgets.

## See also

- [OpenAI Structured Outputs](../openai-structured-outputs/index.md) - the native feature that absorbed much of Instructor's original job
- [Anthropic structured outputs](../anthropic-structured-outputs/index.md) - the other native constraint layer Instructor sits above
- [LangChain](../langchain/index.md) - the framework alternative Instructor explicitly positions against
- [LlamaIndex](../llamaindex/index.md) - the other major framework with its own structured output tooling

## References

- https://github.com/567-labs/instructor - repo: stars, license, retry and streaming features, PydanticAI positioning (as of 2026-09-02)
- https://python.useinstructor.com/ - official docs: from_provider interface, reasking, hooks, provider list
- https://pypi.org/project/instructor/ - release cadence (1.16.0, August 2026), maintainer and authorship
- https://simonwillison.net/2024/Aug/6/openai-structured-outputs/ - independent record that OpenAI credited Instructor as inspiration for its SDK helpers
- https://platform.openai.com/docs/guides/structured-outputs - the native strict mode that changed Instructor's niche
