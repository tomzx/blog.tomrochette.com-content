---
title: Anthropic structured outputs
created: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, structured-outputs, anthropic, tool-calling]
readability: 3
audience_notes: >
  Engineers building extraction or agent tooling on Claude models through the Messages API.
  Assumes you know JSON Schema and have called the Anthropic API before.

---

Anthropic structured outputs is the Claude API feature that constrains responses and tool inputs to a JSON Schema via grammar-constrained decoding, split into JSON outputs (`output_config.format`) and strict tool use (`strict: true` on tools).
Facts below verified as of 2026-08-30.

**Anthropic arrived more than a year after OpenAI (public beta November 2025, GA February 2026), and the gap still shows in the schema subset and complexity limits, but strict tool use targets the failure that hurts agents most: malformed tool arguments mid-loop.**

## What it is

**Two independent halves that compose in one request.**
JSON outputs put a `json_schema` in `output_config.format` so Claude's text response is guaranteed schema-valid, with `messages.parse()` helpers over Pydantic models and Zod schemas in the Python and TypeScript SDKs.
Strict tool use adds `strict: true` to a tool definition so tool names and inputs are grammar-validated at sampling time.
Before the native feature, the documented workaround was forcing a tool via `tool_choice` and reading its arguments, and every model older than Sonnet 4.5 still has to work that way.

## Status

**Active, GA since February 4, 2026.**
The beta (header `structured-outputs-2025-11-13`) launched November 14, 2025 on Sonnet 4.5 and Opus 4.1, Haiku 4.5 followed on December 4, 2025, and GA brought Sonnet 4.5, Opus 4.5, and Haiku 4.5 to the platform and Bedrock with support for more complex schemas.
Current docs list the feature across the opus-5, sonnet-5, mythos-5, and fable-5 families plus their 4.5-generation predecessors, with Microsoft Foundry limited to Anthropic-hosted deployments.
Independent tooling tracked it immediately: Simon Willison's llm-anthropic plugin added support within a day of the beta and kept the tool-call workaround for older models.

## Strengths

- **Strict tool use guarantees type-correct function arguments every call**, removing the validate-and-retry machinery from the agent loop.
- Compiled grammars are cached server-side for 24 hours from last use, so repeated schemas skip first-request latency.
- The Python, TypeScript, Ruby, and PHP SDKs transform schemas that exceed the supported subset (dropping `minimum`, moving constraints into field descriptions) while still validating the full rule set client-side.
- Batch processing takes 50% off, same as the rest of the Batch API.

## Cautions

- **The schema subset is narrower than Pydantic users assume**: no recursive schemas, no numeric or string-length constraints, `minItems` only 0 or 1, regex without lookaround or backreferences, and `additionalProperties` must be false.
- Hard per-request complexity limits: 20 strict tools, 24 optional parameters, 16 union-typed parameters, and a 180-second grammar compilation timeout that returns a 400.
- Enum capitalization is explicitly not guaranteed, so enum values differing only by case can silently collide.
- Requests carry an injected structured-outputs system prompt (billed like any other), and changing `output_config.format` invalidates the conversation's prompt cache.
- Refusals return HTTP 200 with `stop_reason: "refusal"` and non-schema output you must handle yourself, and the computer and browser toolsets reject `strict: true`.

## Pricing

**No feature surcharge, but the meter runs in the small print.**
You pay normal per-model token rates plus the injected prompt tokens; the tool-use docs quantify the tool-use system prompt alone at roughly 286 to 675 input tokens per request depending on model and `tool_choice` (for example 286 for Opus 5 with `auto`, 675 for Opus 4.7) as of 2026-08-24.
Batch discounts structured output requests by 50%.

## Compared to

- OpenAI Structured Outputs: the older, broader implementation of the same idea; choose it when you need ecosystem maturity or a larger supported-model surface.
- Instructor: the library route (Pydantic validation plus re-ask retries over plain tool use), still useful for business rules and for Claude models without native support.
- Forced tool use via `tool_choice`: the zero-infrastructure fallback on older models, at the cost of retries when the model drifts off schema.

## Bottom line

**Recommended for Claude-based agents whose tool arguments must never fail to parse, which I consider the highest-value use of the feature.**
The disagreeable part: I think strict tool use matters more here than JSON outputs, because response formatting was always solvable with retries while a malformed call in the middle of an agent loop was not.
Not for schemas that lean on numeric constraints, recursion, or dozens of optional fields, where the grammar limits and complexity caps will fight you.

## See also

- [OpenAI Structured Outputs](../openai-structured-outputs/index.md) - the older vendor implementation this is measured against
- [Claude Code](../claude-code/index.md) - Anthropic's own harness, whose tool loop is the prime beneficiary of strict tool use
- [Model Context Protocol](../mcp/index.md) - the tool ecosystem whose calls get schema guarantees
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where this sits under the harness layer

## References

- https://docs.claude.com/en/docs/build-with-claude/structured-outputs - primary docs: output_config.format, schema limitations, complexity limits, token costs, failure modes
- https://docs.claude.com/en/docs/agents-and-tools/tool-use/strict-tool-use - strict tool use: grammar-constrained sampling guarantees and PHI caching caveats
- https://claude.com/blog/structured-outputs-on-the-claude-developer-platform - launch timeline: beta Nov 2025, Haiku Dec 2025, GA Feb 2026 with more complex schemas
- https://docs.claude.com/en/docs/build-with-claude/tool-use - tool_use round trip, tool_choice forcing, per-model tool-use system prompt token table
- https://simonwillison.net/2025/Nov/15/llm-anthropic-022/ - independent tooling adoption and the tool-call workaround it replaced
