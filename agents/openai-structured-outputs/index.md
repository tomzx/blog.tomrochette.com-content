---
title: OpenAI Structured Outputs
created: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, structured-outputs, openai, json-schema]
readability: 3
audience_notes: >
  Engineers who call OpenAI models from code and need guaranteed JSON for tools or pipelines.
  Assumes familiarity with the Responses or Chat Completions API and basic JSON Schema.

---

OpenAI Structured Outputs is an API capability that guarantees model responses adhere to a JSON Schema you supply, enforced by constraining decoding rather than by prompting.
Facts below verified as of 2026-08-30.

**It is the strongest output guarantee available from a major vendor: schema adherence is enforced at generation time, so the classic parse-validate-retry loop collapses into a single call for anything your schema can express.**

## What it is

**Two API surfaces expose the same constraint mechanism.**
You can pass `text.format` with `type: json_schema` and `strict: true` on the Responses API (or `response_format` on Chat Completions) to structure the model's reply, or you can set `strict: true` on function and tool definitions to guarantee tool-call arguments match their schemas.
The SDKs wrap both with Pydantic (Python) and Zod (TypeScript) helpers, so `client.responses.parse()` returns a typed, parsed object directly.
The feature shipped in August 2024 with gpt-4o-2024-08-06 and later models; the older JSON mode (`json_object`) only guarantees valid JSON, not schema adherence, and the docs recommend Structured Outputs over it wherever possible.

## Status

**Active, and effectively the default way to get JSON out of OpenAI.**
It works across the Responses, Chat Completions, Assistants, Fine-tuning, and Batch APIs, and current guide examples target the gpt-5.6 model family.
Independent tooling built on it (SDK parse helpers, LLM schema layers) has been standard in the ecosystem since late 2024.

## Strengths

- **Generation-time enforcement**: invalid tokens are masked, so schema violations become structurally impossible instead of merely unlikely.
- Safety refusals surface in a dedicated `refusal` field, making them programmatically detectable instead of a broken parse.
- First-party SDK parsing helpers mean Pydantic or Zod types flow end to end with no hand-written schema JSON.
- Function calling gets the same guarantee, so tool arguments and response bodies are covered by one mechanism.

## Cautions

- **Strict mode accepts only a subset of JSON Schema**: objects must set `additionalProperties: false`, and every key must be listed in `required`, so truly optional fields need nullable-union workarounds.
- The first request with a new schema pays preprocessing latency while OpenAI compiles it into a grammar (per OpenAI staff comments at launch).
- The same staff described the failure mode as rarer but worse: a confused model can loop emitting technically valid output until `max_tokens`, and you pay for every token of it.
- Output keys follow schema ordering, which surprises engineers who expect JSON's unordered keys.

## Pricing

**No separate line item for the feature.**
Requests bill at the chosen model's token rates; for example gpt-5.6-luna lists at $0.20/1M input and $1.20/1M output (standard tier) as of 2026-08-24.
Batch API use cuts those rates by 50% for offline extraction jobs.

## Compared to

- Anthropic structured outputs: the same constrained-decoding idea, but only GA since February 2026 with a narrower schema subset; OpenAI's surface is older and more battle-tested.
- Instructor: a library that adds Pydantic validation and retries across many providers; on OpenAI it now layers business-rule validation on top of the native guarantee rather than replacing it.
- vLLM structured outputs: the equivalent guarantee for models you serve yourself, with xgrammar or guidance backends.

## Bottom line

**Recommended as the default for any OpenAI-backed pipeline that consumes JSON; I would not run schema-critical extraction through prompts plus hope in 2026.**
The disagreeable part: I think the schema subset restrictions are a feature rather than a limitation, because they force schemas a grammar can enforce cheaply, and most "optional field" pain is schema design debt.
Not for schemas that genuinely need numeric ranges, pervasive optional keys, or recursion, where client-side validation plus retries still wins.

## See also

- [Anthropic structured outputs](../anthropic-structured-outputs/index.md) - the other major vendor's constrained-decoding take, and where it lags
- [Instructor](../instructor/index.md) - the library route when you need validation beyond what the schema subset expresses
- [Model Context Protocol](../mcp/index.md) - the tool ecosystem whose calls this guarantee protects
- [LangChain](../langchain/index.md) - the framework layer that wraps this feature alongside its own output parsers
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where structured outputs sit under the harness layer

## References

- https://platform.openai.com/docs/guides/structured-outputs - primary guide: strict mode, text.format vs function calling, JSON mode comparison, model support
- https://cookbook.openai.com/examples/structured_outputs_intro - official cookbook: refusal handling and the Pydantic parse helper
- https://platform.openai.com/docs/pricing - per-model token rates, no structured-outputs surcharge, batch discounts (as of 2026-08-24)
- https://simonwillison.net/2024/Aug/6/openai-structured-outputs/ - independent launch analysis with schema-subset limits and OpenAI staff quotes on latency and loop failures
- https://docs.claude.com/en/docs/build-with-claude/structured-outputs - cross-vendor comparison point for mechanism and schema limits
