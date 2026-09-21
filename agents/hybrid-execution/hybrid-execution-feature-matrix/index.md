---
title: "Hybrid Execution Feature Matrix"
created: 2026-08-24
updated: 2026-09-21
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, hybrid-execution, structured-outputs, constrained-decoding]
readability: 3
audience_notes: >
  Engineers choosing a structured-output mechanism who need the capability deltas at a glance.
  Assumes you know JSON Schema and have called at least one provider API; each column links to a full note.
---

This matrix compares the seven hybrid-execution notes profiled in this section, feature by feature: two vendor API features that constrain decoding, two libraries that validate or mask their way to typed output, and three models that skip text generation entirely, TypeSafe's closed Jev, Cua's open-weights CUA-S1 research checkpoint, and ConvAI Innovations' open-weights, multilingual Laya family.
Everything below was verified against the refreshed member notes and live sources on 2026-09-21.

**These seven are less competitors than mechanisms on one spectrum, and the decision that matters is where the schema guarantee lives, in sampling, in post-hoc checks, or in the architecture itself: I would take decoding-time enforcement everywhere it exists, treat most single-provider Instructor deployments written after 2025 as incidental complexity, and no longer take the architectural class purely on faith, because CUA-S1 and Laya put two independently inspectable open-weights brackets next to Jev's closed claim.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Anthropic structured outputs](../anthropic-structured-outputs/index.md) | [CUA-S1](../cua-s1/index.md) | [Instructor](../instructor/index.md) | [Jev](../jev/index.md) | [Laya](../laya/index.md) | [OpenAI Structured Outputs](../openai-structured-outputs/index.md) | [Outlines](../outlines/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | API feature | open-weights research model | Python library | closed model | open-weights model family | API feature | Python library |
| Guarantee mechanism | grammar-constrained decoding | architectural no-generation scoring with calibrated probabilities | validate plus reask | no text generation at all | non-autoregressive scoring over typed questions, router-dispatched checkpoints | token masking at decode | logit masking |
| API surface | REST, 7+ SDKs | Python source plus HF weights, Cua Driver handoff | Python, 5 ports | REST, MIT Python adapter | pip package (0.3.4), HF checkpoints, community MLX and CoreML runtimes | REST, SDK parse helpers | Python |
| Open source | ✗ | ✓ MIT code and weights | ✓ MIT | ✗ (adapter only) | ✓ Apache-2.0 code and weights | ✗ | ✓ Apache-2.0 |
| Provider breadth | ✗ Claude models only | ✗ one specialist model, self-hosted | ✓ 15+ providers | ✗ TypeSafe only | ✗ self-hosted only | ✗ OpenAI only | ✓ local engines plus hosted APIs |
| Local models | ✗ | ✓ runs on a laptop (2.8 MB) | ✓ via Ollama and vLLM | ✗ | ✓ the point (T4 to Apple Silicon) | ✗ | ✓ core use case |
| Strict tool calls | ✓ strict: true | ~ form-element actions only, no tool-call surface | ~ reask only | ✗ no tool-call surface | ✗ no tool-call surface | ✓ strict mode | ? |
| Beyond-schema constraints | ✗ narrow subset | ~ calibrated abstention and auto-accept thresholds | ✓ Pydantic rules | ~ confidence thresholds in caller code | ~ choice/score/noul vocabulary, calibrated only after temperature fitting | ✗ strict subset | ✓ regex and CFGs |
| Retry behavior | ✗ none, guaranteed | ✗ none, nothing generated | ✓ reask, default 3 | ✗ none, guaranteed | ✗ none, nothing generated | ✗ none, guaranteed | ✗ none, guaranteed |
| Maintenance status | GA since Feb 2026 | research artifact, first checkpoint 2026-09-18 | active since 2023 | early access since Sep 2026 | days old, launched 2026-09-18 | default since Aug 2024 | active, engines moved on |
| Cost implications | injected prompt tokens | free, 2.8 MB on your hardware, your planner still bills | retries bill full calls | $0.042/MTok in, output free (subsidy unproven) | free, your hardware, three checkpoints to keep warm | compile latency, loop risk | free, microseconds overhead |

## Reading the matrix

**The guarantee-mechanism row is the distinction that carries the most weight, and every other row is downstream of it.**
OpenAI, Anthropic, and Outlines enforce the schema while the tokens are being sampled, so an invalid token is never drawn in the first place.
Instructor inspects the finished output and re-asks when Pydantic rejects it.
Jev, CUA-S1, and Laya sit at the end of the spectrum the other four approach: with no text generation there is nothing to constrain and nothing to validate, which is why their rows guarantee retries and type errors away the same way the decoding-time options do.
The difference among the three is verifiability and scope, not mechanism: Jev's numbers are vendor claims behind a closed API, CUA-S1 is a 2.8 MB MIT checkpoint anyone can re-run (its card now adds a 196-decision real eval and a Jev head-to-head, all still vendor-run), and Laya is an Apache-2.0 multilingual family whose benchmark comparisons are likewise self-run.
In plain words: one approach makes the mistake impossible to emit, the other catches the mistake after you have paid for it, and the last two never draw a token in the first place.

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
Both vendors guarantee tool arguments at sampling time, Instructor can only validate and re-ask, nothing in the Outlines note grounds tool-call guarantees at all, and CUA-S1 scores form elements rather than tool calls.

**Costs follow the mechanism as well.**
The decoding-time options bill injected prompts (286 to 675 tokens per request on Anthropic) or first-request compilation (OpenAI) but nothing per failure.
Instructor pays a full model round trip per failed validation, which is the price of enforcing rules the grammar cannot express.
Outlines compiles once per schema and then runs at microseconds of overhead, at the cost of running your own stack.
CUA-S1 is free beyond your own hardware, but the general planning model above it still bills every request.

## Choosing from the matrix

- Already committed to OpenAI or Anthropic and need schema-valid JSON or tool arguments: use the native feature first and add nothing.
- Constraints are semantic (business rules, field meanings) or the stack spans providers: Instructor, layered over native strict mode where it exists.
- Serving your own models, or needing regex, CFG, or recursive structures the vendor subsets reject: Outlines as the front end.
- Running a high-throughput serving stack: prefer the engine's own backend (xgrammar in vLLM) over Outlines' engine.
- Agent loops where one malformed tool call wrecks a run: a vendor with strict tool use beats any library.
- Zero tolerance for retry latency: any decoding-time option, budgeting for Anthropic's injected tokens and OpenAI's compile latency.
- Many small decisions in latency- or cost-sensitive code paths (routing, scoring, guardrails) and no need for generated text: Jev is the hosted column priced and timed for that job, pending third-party confirmation of its claims.
- Want that same no-generation contract inspectable, or work on form-automation research: CUA-S1, a 2.8 MB MIT checkpoint you can re-run, with its vendor-run, single-profile evidence attached.
- Need the decision layer self-hosted and multilingual: Laya, accepting 1k-token states, a fine-tuning step for best accuracy, and self-run benchmarks in exchange for Apache-2.0 weights and local runtimes.

## Changes

- 2026-08-24 - Created with four columns and category rows including the guarantee-mechanism comparison.
- 2026-09-18 - Extended from four to five columns with Jev, the first member that is a model rather than a mechanism around one, and updated the intro, reading, and choosing sections for the third guarantee class.
- 2026-09-20 - Extended from five to six columns with CUA-S1, the open-weights counterpart to Jev's no-generation contract, and updated the intro, thesis, guarantee-spectrum reading, and choosing sections.
- 2026-09-21 - Extended from six to seven columns with Laya, the open-weights multilingual decision-model family, inserted alphabetically between Jev and OpenAI Structured Outputs, and updated the intro, thesis, spectrum reading, choosing bullets, and the CUA-S1 evidence framing after its model-card expansion.

## See also

- [Harness Feature Matrix](../../harnesses/harness-feature-matrix/index.md) - the same treatment for terminal coding agents
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the model side of the decision, since the mechanism choice follows the model choice
- [MCP](../../protocols/mcp/index.md) - the tool ecosystem whose calls get schema guarantees
- [LangChain](../../retrieval/langchain/index.md) - the framework layer that wraps these features alongside its own output parsers

## References

- https://platform.openai.com/docs/guides/structured-outputs - strict mode, API surfaces, JSON-mode comparison for the OpenAI column
- https://docs.claude.com/en/docs/build-with-claude/structured-outputs - schema subset, complexity limits, injected-token costs for the Anthropic column
- https://docs.claude.com/en/docs/agents-and-tools/tool-use/strict-tool-use - sampling-time guarantees behind the strict-tool-calls row
- https://github.com/567-labs/instructor - license, reask retries, provider list for the Instructor column
- https://dottxt-ai.github.io/outlines/latest/ - output types, integrations, pluggable backends for the Outlines column
- https://typesafe.ai/blog/introducing-system-one-models-and-jev - primitives, pricing, and claims behind the Jev column
- https://docs.typesafe.ai/ - the Choice, Score, and Noul surfaces behind the Jev column
- https://news.ycombinator.com/item?id=49717558 - the launch thread and its skepticism behind the Jev column's early-access status
- https://github.com/trycua/cua - the host repository (24,749 stars, MIT) and CUA-S1 component behind the new column (GitHub API, as of 2026-09-20)
- https://huggingface.co/cua-ai/cua-s1-forms - the MIT weights grounding the CUA-S1 open-source and local-model cells
- https://huggingface.co/cua-ai/cua-s1-forms/raw/main/cua-s1-forms.json - the checkpoint metrics grounding the CUA-S1 calibrated-probabilities and synthetic-only cells
- https://news.ycombinator.com/item?id=49767564 - the 2026-09-19 launch thread grounding the CUA-S1 research-artifact status
- https://docs.vllm.ai/en/latest/features/structured_outputs.html - vLLM backend names behind the maintenance-status row
- https://github.com/NandhaKishorM/laya - the Laya column: Apache-2.0 license, checkpoint table, Router, PyPI package (GitHub API and PyPI, as of 2026-09-21)
- https://huggingface.co/convaiinnovations/laya - the Laya model card: the self-critical limits section, post-temperature ECE, and where-Jev-leads tables behind the Laya cells
- https://news.ycombinator.com/item?id=49765348 - the Laya launch thread criticisms behind the context-limit and calibration cells
- https://simonwillison.net/2024/Aug/6/openai-structured-outputs/ - independent record of failure modes and of Instructor's influence
