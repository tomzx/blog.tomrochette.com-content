---
title: BAML
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, structured-outputs, dsl, validation, agents]
readability: 3
audience_notes: >
  Engineers choosing a typed-output mechanism who want to know where a language-level approach sits
  against Instructor, Outlines, and the decision-model wave. Assumes you know JSON Schema and what
  validate-and-retry means.
---

BAML is an Apache-2.0, Rust-implemented programming language for agent code from Boundary, where an LLM call is a native function whose prompt is the body and whose return type is the schema, now grown into a full toolchain (CLI, LSP, tests, binaries, generated SDKs) positioned as "the programming language for agents".

**Its claim on this category is the guarantee mechanism, not the toolchain: the error-correcting structured-output parser from its 2023 origin survives, so typed values come from validating and repairing model output after the fact, the same class as Instructor, expressed in a language instead of a library.**

## What it is

A TypeScript-flavored language with runtime types and no `any` ("opne" fails before runtime when a status field says open or closed), typed error sets, exhaustive pattern matching, Go-style green threads without function coloring, filesystem-based namespaces with no imports, and tests and testsets as code, including quorum runners that rerun nondeterministic calls and require a majority of passes.
The toolchain: `brew install baml`, then `baml init`, `baml agent install` (a version-matched BAML skill for Claude Code and Codex), `baml run` (any function becomes a CLI), `baml describe` (AST-aware discovery for agents), `baml test`, `baml pack` (standalone binaries, 12.1 MB against Bun's 63.1 MB), an LSP for Zed and JetBrains, VS Code and Cursor support, and a browser playground.
`baml generate` emits typed Python and TypeScript SDKs, so an existing application calls BAML functions through Pydantic v2 models; `baml-py` and the `@boundaryml/baml` npm package carry the runtime.
Boundary, a Seattle company, also runs Agent Tries BAML, thousands of simulated agents measuring how hard the language is for agents to use, with a public arena comparing skill versions.

## Status

**Large, very active, and mid-pivot: the structured-output library that launched in 2023 is now a language, and the docs churn of that pivot is visible.**
9,392 stars, 498 forks, and 398 open issues, created 2023-10-06, pushed 2026-10-12, as of 2026-10-11 (GitHub API).
The `baml-language` release train runs nightlies on a 0.21.1 alpha after 0.21.0 (2026-10-08), and the project is pre-1.0 by its own statement.
The npm runtime moved 1,053,321 downloads in the month ending 2026-10-10, the category's largest distribution after the vendor APIs themselves.
The community footprint is thinner than the numbers suggest: the 2024 Show HN drew 18 points, a July 2026 thread on the language repositioning drew 8, and the former clients documentation path (docs.boundaryml.com/clients) returns 404 as of 2026-10-11, a casualty of the pivot.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=BoundaryML/baml&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=BoundaryML/baml&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=BoundaryML/baml&type=date&theme=dark&legend=top-left" />
</picture>

## Strengths

- **The language is the validation story**: with runtime types and no unchecked casts, an invalid state cannot compile, which moves part of the correctness burden from prompt engineering to the type checker.
- LLM calls compose with ordinary code as first-class functions, so the same function is testable, traceable, and packable, and the generated Python and TypeScript SDKs keep adoption incremental.
- `baml describe` and the installed agent skill are agent-first tooling done properly: an agent reads resolved definitions and call sites instead of grepping whole files.
- The Agent Tries BAML arena is the only published agent-usability harness any member of this category runs against its own interface.

## Cautions

- **Pre-1.0 with a recent identity change**: the language pivot orphaned the older documentation (the clients page 404s), so provider coverage that was once documented, including local-model clients, is not verifiable at a stable URL this run.
- The guarantee is still post-hoc: the parser repairs imperfect output, but a confused model can still loop inside technically valid responses, the same failure the decoding-time columns eliminate.
- One company stewards the language, the hosted playground, the skill, and the eval arena, with 398 open issues against a single-vendor maintenance surface.
- No package manager yet, by the project's own statement, so reusable code distribution and its supply-chain questions are still being designed.

## Pricing

Pricing does not apply: the language, toolchain, and SDKs are free and Apache-2.0.
Boundary sells nothing at a listed price as of 2026-10-11 and offers a free 45-minute onboarding session through an early-access program; your model providers bill the calls.

## Compared to

- [Instructor](../instructor/index.md): the same validate-and-recover class, as a Python library in your process; BAML is the language-shaped version, with the repair parser baked into the runtime and typed errors from the compiler.
- [Outlines](../outlines/index.md): Outlines constrains decoding so an invalid token is never drawn; BAML lets the model speak and repairs the result, which is the cheaper integration and the weaker guarantee.
- [Atomic Agents](../atomic-agents/index.md): the framework answer to composing many typed calls in Python; BAML composes them in one language with one toolchain instead.

## Bottom line

**Recommended for teams starting agent-native codebases who want typed LLM calls with agent-first tooling and can accept pre-1.0 churn on a single vendor's language.**
Not for anyone who needs decoding-time guarantees (Outlines or the vendor strict modes), a battle-tested library inside an existing Python service (Instructor), or a stable documented provider matrix today.
My disagreeable claim: BAML is the strongest bet in this category that the structured-output library era ends in absorption, that validation stops being something you import and becomes a property of the language your agents write.

## Changes

- 2026-10-11 - Created after the resolution scan flagged it as the structured-output peer of Instructor and Outlines, with the post-hoc parser guarantee and the pivot's documentation churn recorded as the central cautions.

## See also

- [Instructor](../instructor/index.md) - the library member of the same validate-and-recover class
- [Outlines](../outlines/index.md) - the decoding-time counterpoint that removes the failure BAML repairs
- [Atomic Agents](../atomic-agents/index.md) - the framework layer built on Instructor
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/BoundaryML/baml - repository facts: 9,392 stars, 498 forks, Apache-2.0, Rust, created 2023-10-06, pushed 2026-10-12 (GitHub API, as of 2026-10-11)
- https://raw.githubusercontent.com/BoundaryML/baml/main/README.md - the positioning, runtime types, toolchain list, and install commands (fetched 2026-10-11)
- https://boundaryml.com/explore.md - the language tour: runtime types, typed errors, green threads, LLM calls as functions, the error-correcting parser, testsets and quorums, the supply-chain statement, and the Agent Tries BAML arena
- https://boundaryml.com/quickstart - the toolchain walkthrough: brew install, baml init, agent skill install for Claude Code and Codex, LSP and playground
- https://api.github.com/repos/BoundaryML/baml/releases - baml-language 0.21.0 (2026-10-08) and the nightly train
- https://api.npmjs.org/downloads/point/last-month/@boundaryml/baml - 1,053,321 downloads in the month ending 2026-10-10
- https://hn.algolia.com/api/v1/search?query=BAML%20boundary&tags=story - the footprint scan: an 18-point 2024 Show HN and an 8-point July 2026 repositioning thread
