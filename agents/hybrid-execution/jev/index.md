---
title: Jev
created: 2026-09-18
updated: 2026-09-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, system-one-models, decision-models]
readability: 3
audience_notes: >
  Engineers who wire model judgments into code paths (routing, scoring, guardrails, extraction) and already know the constrained-decoding versus validate-and-retry split from this category's other notes.
  Assumes you know JSON Schema and have paid for a retry loop at least once.
---

Jev is TypeSafe AI's first "System One model": a frontier-class model that generates no text at all and answers typed questions with structured values and calibrated probabilities, positioned as the architectural inversion of everything else in this category.
Facts below verified as of 2026-09-21.

**Every other mechanism here constrains or checks a text generator; Jev removes the text generator, and if its numbers survive third-party testing, the parse-validate-retry stack the other four columns sell becomes legacy glue.**

## What it is

A closed early-access API from TypeSafe AI, a two-years-in-stealth lab founded by Diogo Almeida, whose prior work at OpenAI was the instruction-following research behind ChatGPT.
You send a state and typed questions across three primitives, Choice (pick an option, cardinality up to 255), Score (grade against a rubric), and Noul (a 0-1 truth value), and one request evaluates every question in parallel against the same state, returning typed answers with probability distributions and confidence.
The model was trained with a new method the lab calls Reinforcement Learning for Calibrated Decisions (RLCD), and the launch post claims 70-500ms end-to-end latency (40-200x faster than frontier LLM calls), $0.042 per million input tokens, and free output, with the workflow evals site claiming up to 193.6x faster and 444.6x cheaper than LLM reference calls.
The only open artifact is the MIT [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) wrapper (about 210 stars, created 2026-08-08) that gives competing LLMs the same structured-decision API for benchmarking.

## Status

Early access, opened with the launch post on 2026-09-15 to a Hacker News thread that reached 1,930 points as of 2026-09-21.
The adapter repo was pushed the day I verified, docs and the evals site both resolve, and the waitlist is draining through console.typesafe.ai.
Active and brand new; the claims below are almost entirely vendor-run.

## Strengths

- The schema guarantee is architectural rather than procedural: with no string generation, type errors and refusals are impossible to emit, which is the property decoding-time enforcement approximates and validate-and-retry only patches.
- Questions evaluate in parallel and in isolation, so a ten-question call costs little more than a one-question call and adds no context-rot across questions, a genuinely different scaling curve than one LLM call reasoning over a JSON blob.
- Every answer ships with calibrated confidence, so code can branch on certainty (auto-accept above a threshold, escalate below), which is the guardrail pattern the eval notes all build by hand.
- The decompose-and-compose philosophy (atomic questions, weighting logic in your code, change a coefficient instead of a prompt) is the same discipline the Instructor note ends up recommending, made native.

## Cautions

- The evidence is self-run: the launch post admits the workflow evals were built by its own capabilities team, benchmarked against an Astra-plus-Fable average (a bias it concedes), and measured from the founders' West Coast laptops; the HN thread's top responses note the receipts are demos, with one commenter writing they "realized the post wasn't satirical" only at the videos.
- The lab explicitly declines public benchmarks ([antibenchmaxxing](https://typesafe.ai/blog/antibenchmaxxing)), which is a defensible position that nonetheless leaves no third-party verification of the 40-200x and cannot-hallucinate claims; the "can't hallucinate" figure is admitted to be non-empirical, schema-matching being mathematically guaranteed while factual correctness is not.
- The pricing sustainability is self-admittedly unproven ("we can't prove it isn't subsidized"), and free output tokens is the kind of number that changes.
- A community "Jev-like" model appeared within a day ([jevlike](https://github.com/vinnylarouge/jevlike), 164-point thread on 2026-09-16, about 1,100 stars by 2026-09-21), and the wave it started has become an ecosystem with its own notes in this category ([Jevlike](../jevlike/index.md), [SemIf](../semif/index.md), [Kev](../kev/index.md), [NanoJev](../nanojev/index.md), and [Nimble](../nimble/index.md), alongside [Laya](../laya/index.md)), curated lists of Jev projects passed 700 stars, and browser-use's jev-ultrafast agent built on the Jev API reached about 13,000 stars in five days, which reads two ways: the mechanism may be an efficient classification architecture others can copy, and the moat, if there is one, is calibration data rather than architecture.
- No text generation, no tool calls, no local weights: it cannot replace an LLM anywhere a string is needed, only the decision layer around one.

## Pricing

$0.042 per million input tokens with output free, per the 2026-09-15 launch post, in early access with a waitlist.
No published tiers beyond that; sustainability unproven by the vendor's own admission.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-09-15 | Launch | Baseline: $0.042 per million input tokens with output free, early access with a waitlist, no other published tiers. | [System One launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev) |

## Compared to

- [Instructor](../instructor/index.md): validates a full LLM round trip and re-asks on failure; keep it when you need text generation and business rules, switch the decision layer to Jev when latency and cost dominate and the question decomposes.
- [OpenAI Structured Outputs](../openai-structured-outputs/index.md) and [Anthropic structured outputs](../anthropic-structured-outputs/index.md): schema-guaranteed decoding of a general model, slower and costlier per call but capable of anything, hallucinations included; Jev is the specialized rival for the decision slice only.
- [Outlines](../outlines/index.md): the local-weights path to the same guarantee class; the contrast is total (Jev is closed, hosted, and parallel) and the choice reduces to who owns the model.

## Bottom line

**Recommended for engineers whose agent or product makes many small judgments in code paths where 100ms and $0.04 per million tokens changes what is buildable (routing, scoring, moderation, guardrails), and who can tolerate early-access risk.**
Not for anything needing generated text, tool calls, or self-hosting.
The disagreeable claim I will defend: this category's four existing members all exist to coerce text generators into decisions, and a model born at the decision layer makes that coercion look like what it is, an expensive workaround; the open question, and it is the only one that matters, is whether anyone but TypeSafe can confirm the numbers.

## Changes

- 2026-09-18 - Created from the owner-prompted entrant resolution after the 2026-09-15 launch slipped between entrant-scan windows.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-21 - Recorded the open-model ecosystem wave around the Jev contract (Laya promoted to its own note, jevlike at about 1,100 stars, the 13,000-star jev-ultrafast agent), and refreshed thread and adapter counts.
- 2026-09-21 - Linked the owner-prompted open-alternatives coverage: Jevlike, SemIf, Kev, NanoJev, and Nimble joined this category as their own notes.

## See also

- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category compared, where Jev's column makes the guarantee-mechanism row three-way
- [Instructor](../instructor/index.md) - the validate-and-retry incumbent for the same decision workloads
- [Outlines](../outlines/index.md) - the self-hosted path to the same no-invalid-token guarantee
- [Laya](../laya/index.md) - the open-weights rival that answers the same typed questions on your own hardware
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - where the text-generating model you keep alongside Jev gets chosen

## References

- https://typesafe.ai/blog/introducing-system-one-models-and-jev - the launch post: claims, RLCD, primitives, pricing, admitted nuances
- https://docs.typesafe.ai/ - the three primitives (Choice, Score, Noul), parallel evaluation, decompose-and-compose patterns
- https://evals.typesafe.ai/ - the workflow evals site behind the 193.6x/444.6x claims
- https://github.com/typesafe-ai/system-one-adapter-python - the MIT adapter, the only open artifact (stars, dates via the GitHub API)
- https://news.ycombinator.com/item?id=49717558 - the launch thread (1,930 points as of 2026-09-21), its skepticism the critical source
- https://github.com/vinnylarouge/jevlike - the community reverse-engineering of a Jev-like model within a day
- https://typesafe.ai/blog/antibenchmaxxing - the lab's stated reasons for declining public benchmarks
