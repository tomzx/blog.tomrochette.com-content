---
title: Guardrails
created: 2026-10-13
updated: 2026-10-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, structured-outputs, validation, guardrails, python]
readability: 3
audience_notes: >
  Engineers composing validation around LLM calls who need risk checks (PII, injection, toxicity) as much as schema conformance, and want to know who stands behind the framework they would import.
  Assumes you know Pydantic and what a validate-and-reask loop is.
---

Guardrails is an Apache-2.0 Python framework from Guardrails AI that wraps LLM calls in Input and Output Guards composed from installable validators, and generates schema-typed data through a validate-and-fix loop, the validator-hub member of this category's validate-and-retry family.

**Its distinct kind is the hub: 65 installable validators spanning PII, jailbreak and prompt-injection detection, toxicity, provenance, SQL, and format checks, each with its own on-fail action, which no other member of this category ships, and its 2026 is a study in platform risk, because the company joined Harvey in September after cutting off its hosted inference in August.**

## What it is

A `pip install guardrails-ai` framework, created 2023-01-29, whose two functions are risk guarding and structured generation: a `Guard` composes validators with per-validator `OnFailAction`s (exception, fix, reask, filter), and `Guard.for_pydantic(...)` turns a Pydantic class into a typed call served either by function calling or by a schema-in-prompt fallback.
It reaches 100-plus LLMs through a LiteLLM integration (OpenAI, Anthropic, Azure, Gemini, Bedrock, and custom wrappers for anything else), and a Flask-based Guardrails Server exposes composed guards over REST and an OpenAI-compatible path for callers who want the checks outside their process.
The validators are separate PyPI packages under the `guardrails-ai-*` name, installed directly since the July 2026 migration (the old `guardrails hub install` CLI and the hosted remote-inferencing service were retired with an August 25, 2026 cutoff).
It is made by Guardrails AI, the San Francisco company founded by Shreya Rajpal and Zayd Simjee, which Harvey announced it was acquiring on 2026-09-08.

## Status

Active but in transition: 7,511 stars, pushed 2026-10-09, release v0.11.0 (2026-08-14) the latest on a train that ran v0.9.x through v0.11.0 across 2026, and 101,253 PyPI downloads of the core package in the last month as of 2026-10-13 (GitHub and PyPI APIs; the vendor's own claim of 250,000-plus monthly downloads counts the separate validator packages too).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=guardrails-ai/guardrails&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=guardrails-ai/guardrails&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=guardrails-ai/guardrails&type=date&legend=top-left" />
</picture>

The project's own sunset issue is the cautionary record: the hub-install pattern it promoted since 2024 was replaced by plain PyPI packages and the hosted inference service was cut off on 2026-08-25, a migration each downstream user had to perform.
The acquisition announcement (2026-09-08) moves co-founders and team into Harvey's product and engineering organization, with the framework's know-how pointed at Harvey's agent reliability work, and the company's product surface now fronts Snowglobe, its chatbot-simulation product, whose docs shell the Guardrails documentation is served from (the docs' own llms.txt pointer 404s as of 2026-10-13).
The community footprint is thin for the framework's age: a 15-point 2024 TechCrunch story and a 2-point 2026 hub link on Hacker News, with no Show HN thread of its own that I could find, so adoption evidence is the PyPI and star record, not forum debate.

## Strengths

- **The validator hub is the category's only installable checking ecosystem: 65 validators (PII via Microsoft Presidio, jailbreak and prompt-injection detectors, toxicity, NLI provenance and hallucination checks, SQL, HTML, URL, and format rules) composed into guards with per-validator on-fail behavior, as of 2026-10-13.**
- Many validators are deterministic or small-ML checks that run locally, so the common case adds no token bill beyond the reask loops you trigger.
- The OpenAI-compatible server mode puts the validation boundary in your infrastructure rather than your code, which neither Instructor nor BAML offers.
- LiteLLM-based breadth (100-plus providers) keeps the guard layer portable across vendors, the same surface Instructor sells.

## Cautions

- **The platform behind the framework changed twice in two months, both times by the vendor: hub install retired for plain pip packages, hosted inference cut off, then the company acquired, so the maintenance question for the open-source framework under Harvey is open and unanswered.**
- The guarantee is post-hoc, the same class as Instructor: a confused model still gets paid for its failed attempts, and a validator cannot make an invalid token undrawn.
- Validator quality is self-curated, by the project's own framing (the hub applies inclusion rules only, without guarantees), so a PII or injection check is a starting point, not an audited control.
- The guarantee-mechanism spectrum in this category runs from decoding-time enforcement to no-generation architectures, and Guardrails sits at the loosest end of it.

## Pricing

Pricing does not apply: the framework and the validator packages are Apache-2.0 and free, the hosted remote-inferencing service was discontinued on 2026-08-25, and no listed prices exist for the company's remaining products (the pricing page 404s as of 2026-10-13; Harvey's commercial surface is its own products).

## Compared to

- [Instructor](../instructor/index.md): the same validate-and-reask class with a schema-first center; choose Instructor for typed extraction, Guardrails when the checks you need are risk validators someone already packaged.
- [Outlines](../outlines/index.md): the decoding-time counterpoint that makes invalid output impossible to emit, at the cost of running your own stack.
- NeMo Guardrails (NVIDIA): the conversational-systems neighbor, dialogue rails for chatbots rather than typed-output validation for code paths; the two projects' own joint post positions them as complementary.

## Bottom line

**Recommended for engineers whose binding requirement is risk validation (PII, injection, toxicity, provenance) around LLM calls on multiple providers, and who will read the post-acquisition maintenance signals before adopting.**
Not for decoding-time guarantees, and not as an audited safety control without your own evaluation of each validator.
The disagreeable claim I will defend: the validator-hub kind is the most durable layer of the validate-and-retry family, because risk checks are provider-independent and recomposed per product, yet it now belongs to a team building someone else's agent platform, and if Harvey's ownership stops the community flow, the successor that ages better is a plain Pydantic loop plus the specific validators you actually need.

## Changes

- 2026-10-13 - Created from the cross-category candidate resolution, admitted as the validate-and-retry family's validator-hub kind, with the July 2026 hub-to-PyPI migration, the August hosted-inference cutoff, and the September Harvey acquisition recorded as the governing cautions.

## See also

- [Instructor](../instructor/index.md) - the library member of the same validate-and-reask class, schema-first where Guardrails is risk-first
- [BAML](../baml/index.md) - the language-shaped repair parser, the other non-decoding guarantee in the family
- [Outlines](../outlines/index.md) - the decoding-time guarantee that removes the failure post-hoc validation only catches
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/guardrails-ai/guardrails - repository: Apache-2.0, created 2023-01-29, 7,511 stars, pushed 2026-10-09 (GitHub API, as of 2026-10-13)
- https://raw.githubusercontent.com/guardrails-ai/guardrails/main/README.md - the two functions, Guard and OnFailAction composition, the for_pydantic generation path, the Guardrails Server, and the July 2026 migration notice
- https://guardrailsai.com/hub - the Guardrails Hub: 65 validators with risk categories and infrastructure requirements (fetched 2026-10-13)
- https://www.guardrailsai.com/docs - the documentation introduction: the Input/Output Guards and structured-data functions
- https://guardrailsai.com/guardrails/docs/how-to-guides/using_llms - the LiteLLM integration: 100-plus supported LLMs and the custom-wrapper path
- https://pypi.org/pypi/guardrails-ai/json - the published package, 0.11.0 (fetched 2026-10-13)
- https://pypistats.org/api/packages/guardrails-ai/recent - 101,253 downloads of the core package in the last month (fetched 2026-10-13)
- https://github.com/guardrails-ai/guardrails/releases - the 2026 release train, v0.9.x through v0.11.0 (2026-08-14 latest) (fetched via the releases API)
- https://github.com/guardrails-ai/guardrails/issues/1560 - the project's own sunset notice: hub install retired, hosted remote inference cut off 2026-08-25, the critical source
- https://guardrailsai.com/blog/guardrails-ai-joins-harvey - the acquisition announcement (2026-09-08): co-founders joining Harvey, the 250,000-plus monthly-download claim, investor list
- https://snowglobe.so - the company's product surface after the pivot: Snowglobe chatbot simulation, the docs domain the Guardrails documentation is served from
- https://hn.algolia.com/api/v1/search?query=%22guardrails-ai%22 - the thin-footprint record: no Show HN thread of its own found, a 2-point hub link (2026-07-31) the strongest direct hit (fetched 2026-10-13)
- https://techcrunch.com/2024/02/15/guardrails-ai-builds-hub-for-genai-model-mitigations/ - the 15-point 2024 press story behind the framework's largest forum footprint (fetched 2026-10-13 via the Algolia search API)
