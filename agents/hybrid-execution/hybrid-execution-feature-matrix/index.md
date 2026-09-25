---
title: "Hybrid Execution Feature Matrix"
created: 2026-08-24
updated: 2026-09-25
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, hybrid-execution, structured-outputs, constrained-decoding]
readability: 3
audience_notes: >
  Engineers choosing a structured-output mechanism who need the capability deltas at a glance.
  Assumes you know JSON Schema and have called at least one provider API; each column links to a full note.
---

This matrix compares the thirteen hybrid-execution notes profiled in this section, feature by feature: two vendor API features that constrain decoding, two libraries that validate or mask their way to typed output, eight decision-model implementations of the no-generation contract (TypeSafe's closed Jev plus the seven open answers the community shipped in Jev's launch week: CUA-S1, Jevlike, Kev, Laya, NanoJev, Nimble, and SemIf), and one independent benchmark that measures all of them (JevBench).

**These thirteen are less competitors than mechanisms on one spectrum, and the decision that matters is where the schema guarantee lives, in sampling, in post-hoc checks, or in the architecture itself: I would take decoding-time enforcement everywhere it exists, treat most single-provider Instructor deployments written after 2025 as incidental complexity, and no longer take the architectural class purely on faith, because the launch week put seven independently inspectable open brackets next to Jev's closed claim and the week after produced the first outside scoreboard for all of them.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Anthropic structured outputs](../anthropic-structured-outputs/index.md) | [CUA-S1](../cua-s1/index.md) | [Instructor](../instructor/index.md) | [Jev](../jev/index.md) | [JevBench](../jevbench/index.md) | [Jevlike](../jevlike/index.md) | [Kev](../kev/index.md) | [Laya](../laya/index.md) | [NanoJev](../nanojev/index.md) | [Nimble](../nimble/index.md) | [OpenAI Structured Outputs](../openai-structured-outputs/index.md) | [Outlines](../outlines/index.md) | [SemIf](../semif/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | API feature | open-weights research model | Python library | closed model | benchmark harness (MIT) | open-weights starter (community reverse-engineering) | open-weights LoRA family on Qwen3.5 | open-weights model family | open-weights 0.6B game-task model | open-weights 9B LoRA fine-tune | API feature | Python library | MIT research project over frozen open models |
| Guarantee mechanism | grammar-constrained decoding | architectural no-generation scoring with calibrated probabilities | validate plus reask | no text generation at all | measures intelligence, calibration, speed, and cost across the other columns, enforces nothing itself | single-pass option-attention scoring, no text generation | LoRA-plus-pointer-head scoring with question isolation, no generated answers | non-autoregressive scoring over typed questions, router-dispatched checkpoints | set-attention probability heads over candidates, zero output-token decoding | logit readout of enum and boolean fields, no generated JSON | token masking at decode | logit masking | direct logit readout of declared options from frozen checkpoints |
| API surface | REST, 7+ SDKs | Python source plus HF weights, Cua Driver handoff | Python, 5 ports | REST, MIT Python adapter | CLI harness over each system's own endpoint, 534 public decisions plus a 109-item held-out hard tier, frozen per-task artifacts | Python training CLI plus in-repo checkpoints (vision variant included) | local `POST /v1/systemone` server the TypeSafe SDK targets unchanged, web playground and a browser Spaces demo | pip package (0.3.6), HF checkpoints, community MLX and CoreML runtimes | Python serve script (`POST /api/evaluate`), HF weights and dataset | MLX `ParallelScorer` on Apple Silicon, CUDA path, HF weights | REST, SDK parse helpers | Python | Python runners plus a browser WebGPU demo, MLX community backend |
| Open source | ✗ | ✓ MIT code and weights | ✓ MIT | ✗ (adapter only) | ✓ MIT harness, datasets, and scoring code | ✓ MIT code and in-repo checkpoints | ✓ Apache-2.0 code and weights | ✓ Apache-2.0 code and weights | ✓ MIT code, weights untagged on HF | ~ Apache-2.0 weights, repo code unlicensed | ✗ | ✓ Apache-2.0 | ✓ MIT code (models are third-party open weights) |
| Provider breadth | ✗ Claude models only | ✗ one specialist model, self-hosted | ✓ 15+ providers | ✗ TypeSafe only | ✓ runs against hosted and self-hosted systems alike (48 ranked rows) | ✗ trains its own tiny scorer | ✗ self-hosted only | ✗ self-hosted only | ✗ self-hosted only | ✗ self-hosted only | ✗ OpenAI only | ✓ local engines plus hosted APIs | ✗ runs your own frozen open models |
| Local models | ✗ | ✓ runs on a laptop (2.8 MB) | ✓ via Ollama and vLLM | ✗ | ~ evaluates local endpoints, ships no model of its own | ✓ trains and runs on your machine | ✓ the point (your GPU; MLX backend now shipped for Apple Silicon) | ✓ the point (T4 to Apple Silicon) | ✓ CUDA machine | ✓ Mac (MLX) or CUDA | ✗ | ✓ core use case | ✓ the point (browser demo runs client-side) |
| Strict tool calls | ✓ strict: true | ~ form-element actions only, no tool-call surface | ~ reask only | ✗ no tool-call surface | ✗ typed questions only, no tool-call surface | ✗ scores text and image options, no tool-call surface | ✗ no tool-call surface | ✗ no tool-call surface | ✗ no tool-call surface | ✗ flat enum and boolean fields only | ✓ strict mode | ? | ✗ |
| Beyond-schema constraints | ✗ narrow subset | ~ calibrated abstention and auto-accept thresholds | ✓ Pydantic rules | ~ confidence thresholds in caller code | ✓ scores calibration (ECE plus fidelity to gold distributions) for every entrant rather than providing it | ~ ECE and shuffled-context control shipped; 192-byte default context | ~ calibrated confidence with published gap tables (8.2% confident-wrong at 0.9+ on new sources) | ~ choice/score/noul vocabulary, calibrated only after temperature fitting | ✗ no calibration shipped (plain SFT, RLCD on the roadmap) | ~ temperature fitted 2026-09-22 (same answers, shifted probabilities); suite still showed Jev better calibrated on 11 of 13 subsets | ✗ strict subset | ✓ regex and CFGs | ~ not-calibrated core scores with per-row provenance (timing, revision, prompt hash); community temperature-calibration PRs landed 2026-09-22 |
| Retry behavior | ✗ none, guaranteed | ✗ none, nothing generated | ✓ reask, default 3 | ✗ none, guaranteed | ✗ none, nothing generated (it scores other systems) | ✗ none, nothing generated | ✗ none, nothing generated | ✗ none, nothing generated | ✗ none, nothing generated | ✗ none, nothing generated | ✗ none, guaranteed | ✗ none, guaranteed | ✗ none, nothing generated |
| Maintenance status | GA since Feb 2026 | research artifact, first checkpoint 2026-09-18 | active since 2023 | early access since Sep 2026 | active, v1.4 sealed-decision re-scoring shipped 2026-09-24 (created 2026-09-19) | dormant since launch day (one day of commits, 2026-09-16) | active, eight days old, two releases | days old, launched 2026-09-18 | days old, pushed 2026-09-21 | days old, temperature refit 2026-09-22 | default since Aug 2024 | active, engines moved on | days old and active (pushed 2026-09-23) |
| Cost implications | injected prompt tokens | free, 2.8 MB on your hardware, your planner still bills | retries bill full calls | $0.042/MTok in, output free (subsidy unproven) | free harness, publishes cost per 1,000 decisions for every ranked system | free, your own training run | free weights, about $475 to reproduce the family's training | free, your hardware, three checkpoints to keep warm | free, your own GPU | free weights, your hardware (106 ms per example on an H100, 444 ms on an M5 Pro) | compile latency, loop risk | free, microseconds overhead | free, your GPU (1.023 s median for 21 criteria on a 3090) |

## Reading the matrix

**The guarantee-mechanism row is the distinction that carries the most weight, and every other row is downstream of it.**
OpenAI, Anthropic, and Outlines enforce the schema while the tokens are being sampled, so an invalid token is never drawn in the first place.
Instructor inspects the finished output and re-asks when Pydantic rejects it.
Jev and the seven open implementations below it sit at the end of the spectrum the other four approach: with no text generation there is nothing to constrain and nothing to validate, which is why their rows guarantee retries and type errors away the same way the decoding-time options do.
The difference among the eight is verifiability, scope, and evidence, not mechanism: Jev's numbers began as vendor claims behind a closed API, and the JevBench board is the first outside reading of them (Jev first on both boards, 74.4 on the v1.2 readout and 63.3 on the sealed v1.4 revision, which dropped SemIf from 73.1 to 47.7, from one runner whose methodology its own thread contests), CUA-S1 is a 2.8 MB MIT checkpoint anyone can re-run (its card now adds a 196-decision real eval and a Jev head-to-head, all still vendor-run), Laya is an Apache-2.0 multilingual family whose benchmark comparisons are likewise self-run, and the launch-week wave adds a dormancy spectrum from Kev's pre-registered locked-test harness down to Jevlike's single day of commits and NanoJev's unreplicated game benchmarks.
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
- Want a self-hosted contract drop-in for code written against Jev's SDK: Kev, whose locked-test eval discipline is the strongest in the wave, budgeting for its calibration gap and the missing MLX backend.
- Want to experience the contract locally before trusting anyone's numbers: SemIf, the only column whose browser demo runs client-side with no backend, reading its explicit not-calibrated warning first.
- Shopping the wave by evidence rather than stars: Nimble hosts the only human-labeled head-to-head with Jev (76.0 versus 74.8 macro), NanoJev ships the most complete but unreplicated pipeline, and Jevlike is the dormant one-day starter whose value is historical.
- Want the systems measured rather than described: JevBench, the one column that scores every other one on frozen items with per-task artifacts, read with its thread's methodology objections and one-runner caveats attached.

## Changes

- 2026-08-24 - Created with four columns and category rows including the guarantee-mechanism comparison.
- 2026-09-18 - Extended from four to five columns with Jev, the first member that is a model rather than a mechanism around one, and updated the intro, reading, and choosing sections for the third guarantee class.
- 2026-09-20 - Extended from five to six columns with CUA-S1, the open-weights counterpart to Jev's no-generation contract, and updated the intro, thesis, guarantee-spectrum reading, and choosing sections.
- 2026-09-21 - Extended from six to seven columns with Laya, the open-weights multilingual decision-model family, inserted alphabetically between Jev and OpenAI Structured Outputs, and updated the intro, thesis, spectrum reading, choosing bullets, and the CUA-S1 evidence framing after its model-card expansion.
- 2026-09-21 - Extended from seven to twelve columns with the launch-week open wave (Jevlike, Kev, NanoJev, Nimble, SemIf, all inserted alphabetically), rewrote the intro and thesis for the seven-open-brackets framing, extended the spectrum reading with the dormancy-and-evidence spread, and added four choosing bullets for the wave.
- 2026-09-22 - Extended from twelve to thirteen columns with JevBench, the category's first independent benchmark, inserted alphabetically between Jev and Jevlike, updated the kev (MLX shipped, thread cleared the bar), nimble (temperature fitted 2026-09-22), and semif (calibration PRs) cells, and added a choosing bullet for the scoreboard column.
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-25 - JevBench's sealed-decision v1.4 re-scoring updated the spectrum reading (Jev first on both boards, SemIf 73.1 to 47.7), and the JevBench, Kev, and SemIf maintenance cells moved to the 2026-09-24 re-scoring and later pushes.

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
- https://github.com/vinnylarouge/jevlike - the Jevlike column: MIT, one day of commits, the option-attention starter (GitHub API, as of 2026-09-21)
- https://news.ycombinator.com/item?id=49731282 - the 166-point Jevlike thread behind its dormant-since-launch status cell
- https://github.com/jaredpalmer/kev - the Kev column: Apache-2.0, the SDK-compatible server, releases and author standing (GitHub API, as of 2026-09-21)
- https://raw.githubusercontent.com/jaredpalmer/kev/main/PLAN.md - the pre-registered eval discipline behind Kev's beyond-schema and cost cells
- https://github.com/TianyuCodings/NanoJev - the NanoJev column: MIT code, weights and dataset on Hugging Face (GitHub API, as of 2026-09-21)
- https://github.com/bespokelabsai/nimble - the Nimble column: stars and pushed date, with the missing license behind its partial open-source cell (GitHub API, as of 2026-09-21)
- https://raw.githubusercontent.com/bespokelabsai/nimble/main/docs/PUBLIC_BENCHMARKS.md - the human-labeled Jev head-to-head behind the Nimble evidence framing
- https://github.com/TheoLeeCJ/SemIf - the SemIf column: MIT, the rename from OpenJev, and the frozen-model method (GitHub API, as of 2026-09-21)
- https://news.ycombinator.com/item?id=49752041 - the OpenJev thread behind SemIf's community-footprint status (720 points as of 2026-09-22)
- https://github.com/fstandhartinger/jevbench - the JevBench column: MIT harness, 48-row board, frozen artifacts (GitHub API and README, as of 2026-09-22)
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/RESULTS-v1.2.md - the per-axis scores grounding the JevBench column and the spectrum-reading update
- https://news.ycombinator.com/item?id=49800574 - the 92-point JevBench thread and its methodology objections behind the contested scoreboard framing
- https://simonwillison.net/2024/Aug/6/openai-structured-outputs/ - independent record of failure modes and of Instructor's influence
