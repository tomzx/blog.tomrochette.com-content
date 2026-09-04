---
title: "Evaluation and Review Feature Matrix"
created: 2026-08-30
updated: 2026-09-04
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, evaluation, code-review, human-in-the-loop]
readability: 3
audience_notes: >
  Engineers choosing where quality control lives in their agent workflow: CI gates, dashboards, machine review, or human annotation.
  Assumes you know what an LLM-as-judge metric and a git diff are; each column links to a full note with sources.
---

This matrix compares the four members of the Evaluation and review category: the agent-driven local debugger, the pytest-style eval framework, the observability platform, and the human annotation surface.
Everything below was re-verified against live sources on 2026-09-04.
The hybrid machine reviewer that used to sit here, OpenCodeReview, moved to the Code review category the same day.

**The category divides on who judges: the agent itself (Workshop), a metric suite (deepeval, Phoenix), or a human (Plannotator), and mature teams run more than one column at once.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [deepeval](../deepeval/index.md) | [Phoenix](../phoenix/index.md) | [Plannotator](../plannotator/index.md) | [Workshop](../workshop/index.md) |
| --- | --- | --- | --- | --- |
| Kind | pytest-style eval framework | observability and eval platform | visual plan and diff review UI | local agent debugger plus eval loop |
| Object judged | LLM app outputs (agents, RAG, chat) | traces, spans, experiment outputs | agent plans and diffs | agent traces and code behavior |
| Judge | ~50 LLM-judge metrics plus deterministic checks | LLM evals, code evaluators, human annotations | human annotation | your coding agent writes and runs evals |
| Deployment | Python/TS SDK, CLI | self-hosted server or Arize AX cloud | local browser app plus hooks | local daemon plus web UI |
| CI gating | ✓ non-zero exit on failure | ~ experiments, not gate-native | ✗ pre-merge local loop | ✗ named gap in its own thread |
| Harness integration | tracing integrations | OTel auto-instrumentation, MCP server | hooks in 9 harnesses | skills and MCP for 5+ agents |
| Team layer | Confident AI platform | Arize AX cloud | encrypted links (caveat), Workspaces beta | Raindrop Cloud optional |
| License | ✓ Apache-2.0 | ~ ELv2 core, Apache clients | ✓ Apache-2.0 or MIT | ✓ MIT |
| Maturity | mature, 3 years, v4.2 | mature, 4 years, v20.7 | pre-1.0 (v0.27.x), fast churn | pre-1.0, 4 months |
| Pricing anchor | free, platform $200-2,000/mo | free, AX $50/mo entry | free, Workspaces unpriced | free, Cloud $299/mo |

## Reading the matrix

**The CI-gating row is the buy line: deepeval gates merges today, Workshop's absence of CI is its sharpest recorded criticism, and Plannotator deliberately serves the pre-merge loop instead.**

**The judge row is the trust line.** An agent judging itself (Workshop) closes loops fastest and has the weakest evidentiary standing; metric suites inherit judge variance; Plannotator's human is the only judge whose judgment you do not have to calibrate.

**The license row splits the vendors: MIT and Apache-2.0 columns are safe to embed, and Phoenix's ELv2 core is the one cell that constrains what a business may do with the code.**

**Nobody here is redundant:** Workshop develops agents, deepeval gates them, Phoenix observes them, Plannotator steers them, and the maturity row says a realistic stack starts with the two mature columns and adds the rest as the workflow demands.
Machine review of the pull requests themselves now lives in the [Code Review Feature Matrix](../code-review-feature-matrix/index.md).

## Choosing from the matrix

- Want LLM behavior blocking merges in CI: deepeval.
- Want production-grade tracing and evaluation under your own infrastructure: Phoenix, accepting ELv2.
- Want machine review of every pull request: the [Code Review Feature Matrix](../code-review-feature-matrix/index.md), where OpenCodeReview moved.
- Want your annotations to steer a live agent session: Plannotator.
- Want the trace-to-fix loop while developing an agent locally: Workshop.

## See also

- [Retrieval Feature Matrix](../retrieval-feature-matrix/index.md) - the RAG patterns these tools evaluate
- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the state these tools help verify
- [Hamel Husain](../hamel-husain/index.md) - the eval-driven method grounding the category
- [Executions Feature Matrix](../executions-feature-matrix/index.md) - the scheduled runs whose output gets judged

## References

- https://github.com/raindrop-ai/workshop - the Workshop column: loop, install, license
- https://github.com/confident-ai/deepeval - the deepeval column: metrics, pytest fit, license
- https://github.com/Arize-ai/phoenix - the Phoenix column: OTel basis, ELv2, scale
- https://github.com/backnotprop/plannotator - the Plannotator column: hooks, nine harnesses, license
