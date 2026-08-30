---
title: "Evaluation and Review Feature Matrix"
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, evaluation, code-review, human-in-the-loop]
readability: 3
audience_notes: >
  Engineers choosing where quality control lives in their agent workflow: CI gates, dashboards, machine review, or human annotation.
  Assumes you know what an LLM-as-judge metric and a git diff are; each column links to a full note with sources.
---

This matrix compares the five members of the Evaluation and review category: the agent-driven local debugger, the pytest-style eval framework, the observability platform, the hybrid machine reviewer, and the human annotation surface.
Everything below was verified against live sources on 2026-08-30.

**The category divides on who judges: the agent itself (Workshop), a metric suite (deepeval, Phoenix), deterministic rules plus a model (OpenCodeReview), or a human (Plannotator), and mature teams run more than one column at once.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Workshop](../workshop/index.md) | [deepeval](../deepeval/index.md) | [Phoenix](../phoenix/index.md) | [OpenCodeReview](../open-code-review/index.md) | [Plannotator](../plannotator/index.md) |
| --- | --- | --- | --- | --- | --- |
| Kind | local agent debugger plus eval loop | pytest-style eval framework | observability and eval platform | hybrid machine code reviewer | visual plan and diff review UI |
| Object judged | agent traces and code behavior | LLM app outputs (agents, RAG, chat) | traces, spans, experiment outputs | git diffs and pull requests | agent plans and diffs |
| Judge | your coding agent writes and runs evals | ~50 LLM-judge metrics plus deterministic checks | LLM evals, code evaluators, human annotations | deterministic rules plus LLM agent, precision-first | human annotation |
| Deployment | local daemon plus web UI | Python/TS SDK, CLI | self-hosted server or Arize AX cloud | CLI, CI, agent plugins, MCP | local browser app plus hooks |
| CI gating | ✗ named gap in its own thread | ✓ non-zero exit on failure | ~ experiments, not gate-native | ✓ GitHub Action and GitLab CI | ✗ pre-merge local loop |
| Harness integration | skills and MCP for 5+ agents | tracing integrations | OTel auto-instrumentation, MCP server | plugins for 4 agents, delegation mode | hooks in 9 harnesses |
| Team layer | Raindrop Cloud optional | Confident AI platform | Arize AX cloud | ✗ self-hosted | encrypted links (caveat), Workspaces beta |
| License | ✓ MIT | ✓ Apache-2.0 | ~ ELv2 core, Apache clients | ✓ Apache-2.0 | ✓ Apache-2.0 or MIT |
| Maturity | pre-1.0, 4 months | mature, 3 years, v4.2 | mature, 4 years, v20.4 | young, 100 releases in 3 months | pre-1.0, fast churn |
| Pricing anchor | free, Cloud $299/mo | free, platform $200-2,000/mo | free, AX $50/mo entry | free, your tokens | free, Workspaces unpriced |

## Reading the matrix

**The CI-gating row is the buy line: deepeval and OpenCodeReview gate merges today, Workshop's absence of CI is its sharpest recorded criticism, and Plannotator deliberately serves the pre-merge loop instead.**

**The judge row is the trust line.** An agent judging itself (Workshop) closes loops fastest and has the weakest evidentiary standing; metric suites inherit judge variance; OpenCodeReview's deterministic-first design buys precision at the price of disclosed lower recall; Plannotator's human is the only judge whose judgment you do not have to calibrate.

**The license row splits the vendors: MIT and Apache-2.0 columns are safe to embed, and Phoenix's ELv2 core is the one cell that constrains what a business may do with the code.**

**Nobody here is redundant:** Workshop develops agents, deepeval gates them, Phoenix observes them, OpenCodeReview reviews their output, Plannotator steers them, and the maturity row says a realistic stack starts with the two mature columns and adds the rest as the workflow demands.

## Choosing from the matrix

- Want LLM behavior blocking merges in CI: deepeval.
- Want production-grade tracing and evaluation under your own infrastructure: Phoenix, accepting ELv2.
- Want machine review of every PR with your own keys and in-house code: OpenCodeReview, precision trade understood.
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
- https://github.com/alibaba/open-code-review - the OpenCodeReview column: hybrid architecture, benchmark
- https://github.com/backnotprop/plannotator - the Plannotator column: hooks, nine harnesses, license
- https://news.ycombinator.com/item?id=48406358 - the independent precision measurement grounding the judge-row caution
