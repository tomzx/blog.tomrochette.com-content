---
title: "Hybrid Execution Feature Matrix"
created: 2026-08-24
updated: 2026-10-06
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, comparison, hybrid-execution, structured-outputs, constrained-decoding]
readability: 3
audience_notes: >
  Engineers choosing a structured-output mechanism who need the capability deltas at a glance.
  Assumes you know JSON Schema and have called at least one provider API; each column links to a full note.
---

This matrix compares the sixteen hybrid-execution notes profiled in this section, feature by feature: two vendor API features that constrain decoding, two libraries that validate or mask their way to typed output, ten decision-model implementations of the no-generation contract (TypeSafe's closed Jev, the seven open answers the community shipped in Jev's launch week, CUA-S1, Jevlike, Kev, Laya, NanoJev, Nimble, and SemIf, plus the second-generation lines Jeff and Jeeves), the local runtime that packages most of them (Ollaya), and one independent benchmark that measures all of them (JevBench).

**These sixteen are less competitors than mechanisms on one spectrum, and the decision that matters is where the schema guarantee lives, in sampling, in post-hoc checks, or in the architecture itself: I would take decoding-time enforcement everywhere it exists, treat most single-provider Instructor deployments written after 2025 as incidental complexity, and no longer take the architectural class purely on faith, because the launch week put seven independently inspectable open brackets next to Jev's closed claim, the weeks since produced the first outside scoreboard for all of them plus a second generation of fork lines and a reasoning entrant, and Ollaya now packages the open side into one installable runtime.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Anthropic structured outputs](../anthropic-structured-outputs/index.md) | [CUA-S1](../cua-s1/index.md) | [Instructor](../instructor/index.md) | [Jeeves](../jeeves/index.md) | [Jeff](../jeff/index.md) | [Jev](../jev/index.md) | [JevBench](../jevbench/index.md) | [Jevlike](../jevlike/index.md) | [Kev](../kev/index.md) | [Laya](../laya/index.md) | [NanoJev](../nanojev/index.md) | [Nimble](../nimble/index.md) | [Ollaya](../ollaya/index.md) | [OpenAI Structured Outputs](../openai-structured-outputs/index.md) | [Outlines](../outlines/index.md) | [SemIf](../semif/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | API feature | open-weights research model family | Python library | open-weights reasoning decision model (PostHog) | open-weights fine-tuned family (AutoJev fork line, now a v1.3 base plus adapters) | closed model | benchmark harness (MIT) | open-weights starter (community reverse-engineering) | open-weights fine-tune family (three LoRA adapters on Qwen3.5 plus a full-weights 27B on Qwen3.8) | open-weights model family | open-weights 0.6B game-task model | open-weights 9B LoRA fine-tune | local runtime and model hub for decision models | API feature | Python library | MIT research project over frozen open models |
| Guarantee mechanism | grammar-constrained decoding | architectural no-generation scoring with calibrated probabilities | validate plus reask | LoRA-plus-pointer-head scoring after a short diffusion-drafted reasoning chain, no answer tokens | trained option readout with a fitted temperature, no text generation | no text generation at all | measures intelligence, calibration, speed, and cost across the other columns, enforces nothing itself | single-pass option-attention scoring, no text generation | LoRA-plus-pointer-head scoring with question isolation, no generated answers | non-autoregressive scoring over typed questions, router-dispatched checkpoints | set-attention probability heads over candidates, zero output-token decoding | logit readout of enum and boolean fields, no generated JSON | serves each family's own calibrated probabilities over a wire-identical TypeSafe API, enforces nothing itself | token masking at decode | logit masking | direct logit readout of declared options from frozen checkpoints |
| API surface | REST, 7+ SDKs | Python source plus HF weights, Cua Driver handoff | Python, 5 ports | Jev-compatible local server (noul, choice, score), HF weights, CUDA and MPS inference | local `/v1/systemone` server in Jev's request format, the v1.3 base plus fifteen adapters with GGUF exports, MLX on Apple Silicon | REST, MIT Python adapter | CLI harness over each system's own endpoint, 534 public decisions plus a 109-item held-out hard tier, frozen per-task artifacts | Python training CLI plus in-repo checkpoints (vision variant included) | local `POST /v1/systemone` server the TypeSafe SDK targets unchanged, web playground, a browser Spaces demo, and the kev-1.0 family release (2026-10-01) | pip package (0.3.28), HF checkpoints, community MLX and CoreML runtimes | Python serve script (`POST /api/evaluate`), HF weights and dataset | MLX `ParallelScorer` on Apple Silicon, CUDA path, HF weights | `/v1/systemone`, `/v1/decisions`, and `/v1/models`; desktop app, CLI, and Docker; the TypeSafe SDK 0.7.1 targets it unchanged | REST, SDK parse helpers | Python | Python runners plus a browser WebGPU demo, MLX community backend |
| Open source | ✗ | ✓ MIT code and weights | ✓ MIT | ✓ MIT code, Apache-2.0 weights | ✓ MIT code, Apache-2.0 weights | ✗ (adapter only) | ✓ MIT harness, datasets, and scoring code | ✓ MIT code and in-repo checkpoints | ✓ Apache-2.0 code and weights | ✓ Apache-2.0 code and weights | ✓ MIT code, weights untagged on HF | ~ Apache-2.0 weights, repo code unlicensed | ✓ Apache-2.0 runtime, authors' weights pinned and mirrored | ✗ | ✓ Apache-2.0 | ✓ MIT code (models are third-party open weights) |
| Provider breadth | ✗ Claude models only | ✗ one specialist model, self-hosted | ✓ 15+ providers | ✗ self-hosted only | ✗ self-hosted only | ✗ TypeSafe only | ✓ runs against hosted and self-hosted systems alike (48 ranked rows) | ✗ trains its own tiny scorer | ✗ self-hosted only | ✗ self-hosted only | ✗ self-hosted only | ✗ self-hosted only | ✓ runs 16 open families locally | ✗ OpenAI only | ✓ local engines plus hosted APIs | ✗ runs your own frozen open models |
| Local models | ✗ | ✓ forms checkpoint runs on a laptop (2.8 MB); the 4B LoRA line wants a GPU | ✓ via Ollama and vLLM | ✓ an H100 in fp8, or a 48 GB Mac with reduced caches | ✓ the point (22 ms on an RTX PRO 6000, 28 ms on an M4 Max via MLX) | ✗ | ~ evaluates local endpoints, ships no model of its own | ✓ trains and runs on your machine | ✓ the point (your GPU; MLX backend now shipped for Apple Silicon) | ✓ the point (T4 to Apple Silicon) | ✓ CUDA machine | ✓ Mac (MLX) or CUDA | ✓ the point (CPU to RTX 5090, MLX for laya and nli) | ✗ | ✓ core use case | ✓ the point (browser demo runs client-side) |
| Strict tool calls | ✓ strict: true | ~ form-element actions only, no tool-call surface | ~ reask only | ✗ no tool-call surface | ✗ no tool-call surface | ✗ no tool-call surface | ✗ typed questions only, no tool-call surface | ✗ scores text and image options, no tool-call surface | ✗ no tool-call surface | ✗ no tool-call surface | ✗ no tool-call surface | ✗ flat enum and boolean fields only | ✗ typed questions only, no tool-call surface | ✓ strict mode | ? | ✗ |
| Beyond-schema constraints | ✗ narrow subset | ~ calibrated abstention and auto-accept thresholds | ✓ Pydantic rules | ~ unknowable-question discipline (0.055 answered at p 0.9+ against Jev's 0.090) plus published ECE, all self-run | ~ fitted-temperature calibration; 26-option ceiling (the server refuses longer questions) | ~ confidence thresholds in caller code | ✓ scores calibration (ECE plus fidelity to gold distributions) for every entrant rather than providing it | ~ ECE and shuffled-context control shipped; 192-byte default context | ~ calibrated confidence with published gap tables (8.2% confident-wrong at 0.9+ on new sources) | ~ choice/score/noul vocabulary, calibrated only after temperature fitting | ✗ no calibration shipped (plain SFT, RLCD on the roadmap) | ~ temperature fitted 2026-09-22 (same answers, shifted probabilities); suite still showed Jev better calibrated on 11 of 13 subsets | ~ each model ships its author's fitted temperature, refittable in a Modelfile; parity-checked against the authors' code | ✗ strict subset | ✓ regex and CFGs | ~ not-calibrated core scores with per-row provenance (timing, revision, prompt hash); community temperature-calibration PRs landed 2026-09-22 |
| Retry behavior | ✗ none, guaranteed | ✗ none, nothing generated | ✓ reask, default 3 | ✗ none, nothing generated | ✗ none, nothing generated | ✗ none, guaranteed | ✗ none, nothing generated (it scores other systems) | ✗ none, nothing generated | ✗ none, nothing generated | ✗ none, nothing generated | ✗ none, nothing generated | ✗ none, nothing generated | ✗ none, nothing generated | ✗ none, guaranteed | ✗ none, guaranteed | ✗ none, nothing generated |
| Maintenance status | GA since Feb 2026 | research artifact, four checkpoints by 2026-10-06 (first 2026-09-18) | active since 2023 | seven days old (created 2026-09-29), one company, unlisted on the JevBench board | eight days old, v1.3 adapter-first base plus Jeff-Code (2026-10-05) | early access since Sep 2026 | active, v1.4.2.2 board current, v1.5 method published 2026-09-29 (created 2026-09-19) | dormant since launch day (one day of commits, 2026-09-16) | active, nineteen days old, three releases (Kev 1.0 family release 2026-10-01) | eighteen days old, launched 2026-09-18 | nineteen days old, pushed 2026-09-21 | eighteen days old, temperature refit 2026-09-22 | beta, thirteen days old, pushed 2026-10-05 | default since Aug 2024 | active, engines moved on | three weeks old and active (pushed 2026-09-23) |
| Cost implications | injected prompt tokens | free, 2.8 MB on your hardware, your planner still bills | retries bill full calls | free weights, your GPU, and a 3.3 s median thinking budget per request on an H100 | free weights, your own GPU (training data not released) | $0.042/MTok in, output free (subsidy unproven) | free harness, publishes cost per 1,000 decisions for every ranked system | free, your own training run | free weights, about $475 to reproduce the small family's training plus a data-centre GPU for the 27B | free, your hardware, three checkpoints to keep warm | free, your own GPU | free weights, your hardware (106 ms per example on an H100, 444 ms on an M5 Pro) | free, your hardware, no metering | compile latency, loop risk | free, microseconds overhead | free, your GPU (1.023 s median for 21 criteria on a 3090) |

## Reading the matrix

**The guarantee-mechanism row is the distinction that carries the most weight, and every other row is downstream of it.**
OpenAI, Anthropic, and Outlines enforce the schema while the tokens are being sampled, so an invalid token is never drawn in the first place.
Instructor inspects the finished output and re-asks when Pydantic rejects it.
Jev, the nine open implementations, and the runtime that packages them sit at the end of the spectrum the other four approach: with no text generation there is nothing to constrain and nothing to validate, which is why their rows guarantee retries and type errors away the same way the decoding-time options do.
The difference among the ten is verifiability, scope, and evidence, not mechanism: Jev's numbers began as vendor claims behind a closed API, and the JevBench board is the first outside reading of them (Jev led the v1.2 board at 74.4 and the initial sealed v1.4 revision at 63.3, which dropped SemIf from 73.1 to 47.7, before v1.4.2's eleven additions moved decider-4b v2, 64.1, half a point ahead and the v1.4.2.1 Plumb-4B, 65.8, and v1.4.2.2 Imajev-4B, 67.4, point releases took the top spot on consecutive days, from one runner whose methodology its own thread contests), CUA-S1 grew from a 2.8 MB MIT checkpoint anyone can re-run into a four-checkpoint family (its card now adds a 196-decision eval over actual forms and a Jev head-to-head, all still vendor-run), Laya is an Apache-2.0 multilingual family whose benchmark comparisons are likewise self-run, the launch-week wave adds a dormancy spectrum from Kev's pre-registered locked-test harness down to Jevlike's single day of commits and NanoJev's unreplicated game benchmarks, the second generation arrived as Jeff's AutoJev-fork fine-tunes, whose benchmark table matches Jev's published overall while conceding every reasoning benchmark to it, and Jeeves's reasoning-then-deciding 9B, which beats the same published numbers on its own tests at ten times the latency, while Ollaya packages the open side into one installable runtime whose core feature is parity-checking every model against its author's code.
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
- Want a self-hosted contract drop-in for code written against Jev's SDK: Kev, whose locked-test eval discipline is the strongest in the wave and whose 1.0 release now spans 0.8B to 27B, budgeting for its calibration gap and, above 8k tokens, for the 80 GB GPU the 27B wants.
- Want a small fine-tunable Jev-format student trained on one workstation GPU: Jeff, whose benchmark table concedes every reasoning benchmark to Jev while matching its published classification overall.
- Want accuracy back without abandoning the contract: Jeeves, accepting a 3.3 s median thinking budget, self-run numbers, and an unboarded checkpoint.
- Want the whole open wave runnable locally behind one TypeSafe-shaped API: Ollaya, reading its self-run accuracy tables as directional and its parity checks against the authors' code as the feature worth trusting.
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
- 2026-09-26 - JevBench's v1.4.2 additions (eleven systems, a v1.4.3 roster pending) updated the spectrum reading, where decider-4b v2 (64.1) now sits half a point ahead of Jev (63.3), and the JevBench maintenance cell moved to the 2026-09-24 additions.
- 2026-09-27 - JevBench's v1.4.2.1 point release (Plumb-4B 65.8, the new #1) updated the spectrum reading again, and the JevBench maintenance cell moved to the 2026-09-27 point release.
- 2026-09-29 - Extended from thirteen to fourteen columns with Jeff, the AutoJev-fork fine-tune family that clears the wave's evidence bar (471-point launch thread), inserted alphabetically between Instructor and Jev, and updated the intro, thesis, spectrum reading, and choosing sections; the JevBench maintenance cell moved to the v1.4.2.2 point release (Imajev-4B 67.4, the new #1), the Kev cell moved to twelve days old, and the Laya API-surface cell moved to PyPI 0.3.21.
- 2026-10-02 - Moved the Kev cells for the Kev 1.0 family release and the new 27B flagship (kind now names the full-weights 27B, the API-surface cell records kev-1.0, maintenance moves to sixteen days old and three releases, cost adds the data-centre GPU) and the Laya API-surface cell to PyPI 0.3.23; the JevBench text board itself is unchanged since v1.4.2.2.
- 2026-10-02 - Moved the JevBench maintenance cell to the frozen v1.5 method publication of 2026-09-29 (equal-axis, equal-type headline amendment), with the v1.4.2.2 board still current and no v1.5 results published.
- 2026-10-03 - Moved the Laya API-surface cell to PyPI 0.3.24 and pointed the SemIf reference at the repository's canonical SemIf-OpenJev name (the /SemIf URL redirects); every other cell is unchanged.
- 2026-10-04 - Moved the Laya API-surface cell to PyPI 0.3.26 (0.3.25 and 0.3.26 shipped October 3) and the Kev maintenance cell to seventeen days old; every other cell is unchanged.
- 2026-10-06 - Extended from fourteen to sixteen columns with Jeeves, the reasoning-then-deciding 9B from PostHog, and Ollaya, the local runtime that packages the open families behind the TypeSafe API, both inserted alphabetically, and updated the intro, thesis, spectrum reading, and choosing sections.
- 2026-10-06 - Moved the CUA-S1 kind, local-models, and maintenance cells to the four-checkpoint family, the Jeff maintenance and API-surface cells to the v1.3 adapter-first base plus Jeff-Code, the Kev maintenance cell to twenty days old, and the Laya API-surface cell to PyPI 0.3.28.
- 2026-10-06 - Corrected the maintenance-row ages (Jeff eight days and Ollaya thirteen, not three weeks; Kev nineteen, not twenty) and refreshed the stale day counts for Jeeves, Laya, NanoJev, Nimble, and SemIf.

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
- https://github.com/firelex/jeff - the Jeff column: MIT code, Apache-2.0 weights, the benchmark table and speed claims, the AutoJev lineage (GitHub API and README, as of 2026-09-29)
- https://raw.githubusercontent.com/firelex/jeff/main/README.md - the v1.3 adapter-first base, the fifteen adapters, and the Jeff-Code paired-run table behind the Jeff maintenance and API-surface cells (fetched 2026-10-06)
- https://github.com/PostHog/jeeves - the Jeeves column: MIT code, Apache-2.0 weights, the benchmark tables and latency trade (GitHub API and README, as of 2026-10-06)
- https://news.ycombinator.com/item?id=49891290 - the 242-point Jeeves launch thread grounding its evidence framing
- https://ollaya.dev/ - the Ollaya column: the TypeSafe-compatible API surface, family list, and the Ollama comparison behind its cells
- https://github.com/ollaya-dev/ollaya - the Ollaya repository: Apache-2.0, created 2026-09-23, 1,207 stars (GitHub API, as of 2026-10-06)
- https://news.ycombinator.com/item?id=49848269 - the 618-point Ollaya launch thread
- https://news.ycombinator.com/item?id=49883844 - the 471-point Jeff launch thread grounding the Jeff column's evidence framing
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
- https://github.com/TheoLeeCJ/SemIf-OpenJev - the SemIf column: MIT, the rename from OpenJev, and the frozen-model method (GitHub API, as of 2026-10-03; the /SemIf URL redirects here)
- https://news.ycombinator.com/item?id=49752041 - the OpenJev thread behind SemIf's community-footprint status (720 points as of 2026-09-22)
- https://github.com/fstandhartinger/jevbench - the JevBench column: MIT harness, 48-row board, frozen artifacts (GitHub API and README, as of 2026-09-22)
- https://raw.githubusercontent.com/fstandhartinger/jevbench/main/RESULTS-v1.2.md - the per-axis scores grounding the JevBench column and the spectrum-reading update
- https://news.ycombinator.com/item?id=49800574 - the 92-point JevBench thread and its methodology objections behind the contested scoreboard framing
- https://simonwillison.net/2024/Aug/6/openai-structured-outputs/ - independent record of failure modes and of Instructor's influence
