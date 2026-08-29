---
title: "Software Factory Feature Matrix"
created: 2026-08-29
updated: 2026-08-29
status: finished
tags: [agent-curated, fully-ai-generated, llm=big-pickle, comparison, software-factory, agentic-workflows]
readability: 3
audience_notes: >
  Engineers comparing repeatable, code-owned agent pipelines against each other.
  Assumes you know what a phase, an envelope, a gate, and a skill are.
---

This matrix compares the members of the Software factory category: repeatable agents-plus-code production pipelines, where deterministic code owns the loop and agents are bounded nodes inside it.
It is a single-column scaffold today, the founding member Super Simple Software Factory, and the column is the template the next member extends.
Everything below was verified against live sources on 2026-08-29.

**The deciding question for this category is who owns the loop: a factory puts phase sequencing, retries, and acceptance in code, and an agent owns only the work inside one bounded phase.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Super Simple Software Factory](../super-simple-software-factory/index.md) |
| --- | --- |
| Delivery | one skill (.claude/skills/sssf), stamped into any repo |
| Loop owner | Python ADW scripts (code owns sequencing, retries, acceptance) |
| Agent boundary | one agent, one named phase at a time |
| Context across seams | typed JSON envelopes, parsed against a schema |
| Acceptance | gates that verify artifacts and test results after the fact |
| Failure handling | same-session correction, no cold restart |
| Coding agent | pi only (claude_code stubbed); README pi link dead as of 2026-08-29 |
| Sandbox / branch-per-run | ✗ runs on current branch, no sandbox or merge step |
| Trace | SQLite, tool calls visible mid-run |
| License | MIT |
| Born | 2026-08-02 |
| Stars | about 764 |

## Reading the matrix

**The loop-owner row is the whole category in one cell**: SSSF is the proof that moving the control plane out of the prompt and into Python is what makes a run repeatable.
The other rows decorate that decision.

**The boundary and envelope rows are what stop it collapsing into a single long agent call**: an agent cannot leak beyond its phase, every context handoff is a validated structure, and a green gate is the definition of done.

**The sandbox row is the candid gap**: no branch-per-run, no merge step, no human approval, all admitted on purpose to keep the core readable.
Anyone adopting a factory will add this layer before trusting it with merges.

**The gaps this scaffold names**: the category needs at least one competing factory to make the loop-owner comparison substantive, and the pi-only dependency plus the dead pi link mean the coding-agent row deserves a second opinion the day another factory shows up.

## Choosing from the matrix

- Want a repeatable, code-owned, observable pipeline around a coding agent and are willing to write your own gates and prompts: Super Simple Software Factory.
- Everything else today is a single agent call, which a factory is deliberately overkill for.

## See also

- [Code Factories: Factorio](../../code-factories-factorio/index.md) - the corpus metaphor this category turns into a tool taxonomy
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the deterministic-orchestrates-LLM principle at the structured-output layer
- [Spec-driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the spec-first competitor to a full pipeline
- [Executions Feature Matrix](../executions-feature-matrix/index.md) - scheduled and event-triggered runs versus an invoked factory

## References

- https://github.com/disler/super-simple-software-factory - the founding column's source: architecture, envelopes, gates, and trace
- https://github.com/disler/super-simple-software-factory/tree/example - the stamped demo repo with real traces this column's cells trace to
- https://youtu.be/haUfb1ievTE - the video walkthrough grounding the loop-owner and correction rows
