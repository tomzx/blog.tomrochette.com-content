---
title: "Hybrid Execution Feature Matrix"
created: 2026-08-24
updated: 2026-08-24
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, comparison, hybrid-execution, structured-outputs, constrained-decoding]
readability: 3
audience_notes: >
  Engineers choosing a structured-output mechanism who need the capability deltas at a glance.
  Assumes you know JSON Schema and have called at least one provider API; each column links to a full note.
---

This matrix compares the four hybrid-execution notes profiled in this section, feature by feature: two vendor API features that constrain decoding and two libraries that validate or mask their way to typed output.
Everything below was verified against live sources on 2026-08-24.

**These four are less competitors than two mechanisms wearing four badges, and the decision that matters is whether the schema is enforced while tokens are sampled or checked after the fact: I would take decoding-time enforcement everywhere it exists, which leaves the libraries the portability and business-rules work, and makes most single-provider Instructor deployments written after 2025 incidental complexity.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Anthropic structured outputs](../anthropic-structured-outputs/index.md) | [Instructor](../instructor/index.md) | [OpenAI Structured Outputs](../openai-structured-outputs/index.md) | [Outlines](../outlines/index.md) |
| --- | --- | --- | --- | --- |
| Kind | API feature | Python library | API feature | Python library |
| Guarantee mechanism | grammar-constrained decoding | validate plus reask | token masking at decode | logit masking |
| API surface | REST, 4 SDKs | Python, 5 ports | REST, SDK parse helpers | Python |
| Open source | ✗ | ✓ MIT | ✗ | ✓ Apache-2.0 |
| Provider breadth | ✗ Claude models only | ✓ 15+ providers | ✗ OpenAI only | ✓ local engines plus hosted APIs |
| Local models | ✗ | ✓ via Ollama and vLLM | ✗ | ✓ core use case |
| Strict tool calls | ✓ strict: true | ~ reask only | ✓ strict mode | ? |
| Beyond-schema constraints | ✗ narrow subset | ✓ Pydantic rules | ✗ strict subset | ✓ regex and CFGs |
| Retry behavior | ✗ none, guaranteed | ✓ reask, default 3 | ✗ none, guaranteed | ✗ none, guaranteed |
| Maintenance status | GA since Feb 2026 | active since 2023 | default since Aug 2024 | active, engines moved on |
| Cost implications | injected prompt tokens | retries bill full calls | compile latency, loop risk | free, microseconds overhead |

## Reading the matrix

**The guarantee-mechanism row is the distinction that carries the most weight, and every other row is downstream of it.**
OpenAI, Anthropic, and Outlines enforce the schema while the tokens are being sampled, so an invalid token is never drawn in the first place.
Instructor inspects the finished output and re-asks when Pydantic rejects it.
In plain words: one approach makes the mistake impossible to emit, the other catches the mistake after you have paid for it.

**A decoding-time guarantee changes the failure mode rather than removing it.**
OpenAI staff described a confused model looping in technically valid output until `max_tokens`, and you pay for every token of it.
Anthropic refusals come back as HTTP 200 with non-schema text you must handle yourself.
The retry loop leaves your code; error handling does not.

**Given the mechanism, the library columns survive only in the niches the vendors cannot reach.**
Instructor's remaining value is the cross-provider surface (15+ providers, Ollama and vLLM included) and business rules no grammar expresses.
Outlines' is regex, CFG, and recursive coverage, plus one type-driven API across local engines and hosted APIs.
The Instructor note itself argues the minimal correct design on a single vendor is native strict mode plus a thin Pydantic validation step, and I agree.

**Strict tool calls are the sharpest vendor win, because a malformed call in the middle of an agent loop is the failure retries never fixed well.**
The Anthropic note calls this the highest-value use of the feature.
Both vendors guarantee tool arguments at sampling time, Instructor can only validate and re-ask, and nothing in the Outlines note grounds tool-call guarantees at all.

**Costs follow the mechanism as well.**
The decoding-time options bill injected prompts (286 to 675 tokens per request on Anthropic) or first-request compilation (OpenAI) but nothing per failure.
Instructor pays a full model round trip per failed validation, which is the price of enforcing rules the grammar cannot express.
Outlines compiles once per schema and then runs at microseconds of overhead, at the cost of running your own stack.

## Choosing from the matrix

- Already committed to OpenAI or Anthropic and need schema-valid JSON or tool arguments: use the native feature first and add nothing.
- Constraints are semantic (business rules, field meanings) or the stack spans providers: Instructor, layered over native strict mode where it exists.
- Serving your own models, or needing regex, CFG, or recursive structures the vendor subsets reject: Outlines as the front end.
- Running a high-throughput serving stack: prefer the engine's own backend (xgrammar in vLLM) over Outlines' engine.
- Agent loops where one malformed tool call wrecks a run: a vendor with strict tool use beats any library.
- Zero tolerance for retry latency: any decoding-time option, budgeting for Anthropic's injected tokens and OpenAI's compile latency.

## See also

- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the same treatment for terminal coding agents
- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the model side of the decision, since the mechanism choice follows the model choice
- [MCP](../mcp/index.md) - the tool ecosystem whose calls get schema guarantees
- [LangChain](../langchain/index.md) - the framework layer that wraps these features alongside its own output parsers

## References

- https://platform.openai.com/docs/guides/structured-outputs - strict mode, API surfaces, JSON-mode comparison for the OpenAI column
- https://docs.claude.com/en/docs/build-with-claude/structured-outputs - schema subset, complexity limits, injected-token costs for the Anthropic column
- https://docs.claude.com/en/docs/agents-and-tools/tool-use/strict-tool-use - sampling-time guarantees behind the strict-tool-calls row
- https://github.com/567-labs/instructor - license, reask retries, provider list for the Instructor column
- https://dottxt-ai.github.io/outlines/latest/ - output types, integrations, pluggable backends for the Outlines column
- https://docs.vllm.ai/en/latest/features/structured_outputs.html - vLLM backend names behind the maintenance-status row
- https://simonwillison.net/2024/Aug/6/openai-structured-outputs/ - independent record of failure modes and of Instructor's influence
