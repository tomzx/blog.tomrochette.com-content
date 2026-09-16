---
title: "Evaluation and Review Feature Matrix"
created: 2026-08-30
updated: 2026-09-16
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, evaluation, code-review, human-in-the-loop]
readability: 3
audience_notes: >
  Engineers choosing where quality control lives in their agent workflow: CI gates, dashboards, machine review, or human annotation.
  Assumes you know what an LLM-as-judge metric and a git diff are; each column links to a full note with sources.
---

This matrix compares the six members of the Evaluation and review category: the pytest-style eval framework, the public multi-harness benchmark, two observability and evaluation platforms (Langfuse and Phoenix), the human annotation surface, and the agent-driven local debugger.
Everything below was re-verified against live sources on 2026-09-16.
The hybrid machine reviewer that used to sit here, OpenCodeReview, moved to the Code review category when this matrix was created, on 2026-08-30.

**The category divides on who judges: the agent itself (Workshop), a metric suite (deepeval), an observability platform's judges (Langfuse, Phoenix), or a human (Plannotator), and mature teams run more than one column at once.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [deepeval](../deepeval/index.md) | [FrontierHarness Eval](../frontierharness-eval/index.md) | [Langfuse](../langfuse/index.md) | [Phoenix](../phoenix/index.md) | [Plannotator](../plannotator/index.md) | [Workshop](../workshop/index.md) |
| --- | --- | --- | --- | --- | --- | --- |
| Kind | pytest-style eval framework | public multi-harness benchmark | OSS LLM/agent observability and evaluation platform | observability and eval platform | visual plan and diff review UI | local agent debugger plus eval loop |
| Object judged | LLM app outputs (agents, RAG, chat) | coding-agent harnesses on fixed tasks | traces, sessions, dataset runs, and experiment outputs | traces, spans, experiment outputs | agent plans and diffs | agent traces and code behavior |
| Judge | ~50 LLM-judge metrics plus deterministic checks | fixed 30-task suite, deterministic scoring | managed LLM-as-judge evaluators, code evaluators, user feedback, human annotation queues | LLM evals, code evaluators, human annotations | human annotation | your coding agent writes and runs evals |
| Deployment | Python/TS SDK, CLI | web leaderboard, npx runner, public repo | cloud or self-hosted (Docker Compose locally, Kubernetes templates for production) | self-hosted server or Arize AX cloud | local browser app plus hooks | local daemon plus web UI |
| CI gating | ✓ non-zero exit on failure | ✗ a published study, not a gate | ~ experiments and evals via SDK and API, not a pytest-style gate | ~ experiments, not gate-native | ✗ pre-merge local loop | ✗ named gap in its own thread |
| Harness integration | tracing integrations | 9 harnesses, 12 configs, agent-neutral re-run skill | Python/JS SDKs, native OpenTelemetry, 100+ framework integrations, agent skill, CLI, MCP server | OTel auto-instrumentation, MCP server | hooks in 9 harnesses | skills and MCP for 5+ agents |
| Team layer | Confident AI platform | ✗ | cloud RBAC, SSO and Slack on the Teams add-on, Enterprise audit logs and SCIM | Arize AX cloud | encrypted links (caveat), Workspaces waitlist | Raindrop Cloud optional |
| License | ✓ Apache-2.0 | ✗ repository unlicensed | ~ MIT core, proprietary ee/ modules, ClickHouse-owned | ~ ELv2 core, Apache clients | ✓ Apache-2.0 or MIT | ✓ MIT |
| Maturity | mature, 3 years, v4.2 | new, first run 2026-08-31, 82-point HN launch | mature, 3 years, v4.36.1 | mature, 4 years, v20.12 | pre-1.0 (v0.27.x), fast churn | pre-1.0, 4 months |
| Pricing anchor | free, platform $200-2,000/mo | free to read, a re-run costs harness tokens | free self-hosted, cloud $29-2,499/mo | free, AX $50/mo entry | free, Workspaces unpriced | free, Cloud $299/mo |

## Reading the matrix

**The CI-gating row is the buy line: deepeval gates merges today, Workshop's absence of CI is its sharpest recorded criticism, and Plannotator deliberately serves the pre-merge loop instead.**

**The FrontierHarness column judges a different object than every other column: the harnesses themselves, on public tasks, which makes it evidence for the tool-choice decision and the one column here with a structural conflict of interest, since its publisher sells agent infrastructure and its repository carries no license.**

**The judge row is the trust line.** An agent judging itself (Workshop) closes loops fastest and has the weakest evidentiary standing; metric suites inherit judge variance; Plannotator's human is the only judge whose judgment you do not have to calibrate.

**The license row splits the vendors: MIT and Apache-2.0 columns are safe to embed, while Langfuse's proprietary ee/ modules and Phoenix's ELv2 core are the two cells that constrain what a business may do with the code, and Langfuse's is now held by ClickHouse, which acquired the project in January 2026.**

**Nobody here is redundant:** Workshop develops agents, deepeval gates them, Langfuse and Phoenix observe and evaluate them in production, Plannotator steers them, FrontierHarness prices the harness choice itself, and the maturity row says a realistic stack starts with the mature columns and adds the rest as the workflow demands.
Machine review of the pull requests themselves now lives in the [Code Review Feature Matrix](../../code-review/code-review-feature-matrix/index.md).

## Choosing from the matrix

- Want LLM behavior blocking merges in CI: deepeval.
- Want independent-ish cost and quality numbers before picking a harness: FrontierHarness Eval, vendor-run caveat attached.
- Want MIT-licensed production tracing, evaluation, and prompt management in one platform: Langfuse, self-hosted or cloud, open-core edges and ClickHouse ownership accepted.
- Want production-grade tracing and evaluation under your own infrastructure: Phoenix, accepting ELv2.
- Want machine review of every pull request: the [Code Review Feature Matrix](../../code-review/code-review-feature-matrix/index.md), where OpenCodeReview moved.
- Want your annotations to steer a live agent session: Plannotator.
- Want the trace-to-fix loop while developing an agent locally: Workshop.

## Changes

- 2026-08-30 - Created with five columns on the who-judges axis, reduced to four the same day when the OpenCodeReview column was removed.
- 2026-09-05 - Extended to five columns with FrontierHarness Eval.
- 2026-09-07 - FrontierHarness Eval cell corrected to 82 points.
- 2026-09-13 - Corrected the intro sentence that tied the OpenCodeReview category move to the re-verification date; the move happened on 2026-08-30.
- 2026-09-16 - Phoenix maturity cell moved to v20.12 after the 2026-09-14 release.
- 2026-09-16 - Extended to six columns with Langfuse.

## See also

- [Retrieval Feature Matrix](../../retrieval/retrieval-feature-matrix/index.md) - the RAG patterns these tools evaluate
- [Memory Feature Matrix](../../memory/memory-feature-matrix/index.md) - the state these tools help verify
- [Hamel Husain](../../people-and-publications/hamel-husain/index.md) - the eval-driven method grounding the category
- [Executions Feature Matrix](../../executions/executions-feature-matrix/index.md) - the scheduled runs whose output gets judged

## References

- https://github.com/raindrop-ai/workshop - the Workshop column: loop, install, license
- https://github.com/confident-ai/deepeval - the deepeval column: metrics, pytest fit, license
- https://frontierharness.org - the FrontierHarness column: results, task count, cost spread
- https://github.com/frontier-harness-eval/eval - the FrontierHarness column: public artifacts and the unlicensed caveat
- https://runta.com/blog/introducing-frontierharness-eval/ - the FrontierHarness column: evaluation design and publisher context
- https://github.com/Arize-ai/phoenix - the Phoenix column: OTel basis, ELv2, scale
- https://github.com/backnotprop/plannotator - the Plannotator column: hooks, nine harnesses, license
- https://github.com/langfuse/langfuse - the Langfuse column: repository, license split, adoption numbers
- https://raw.githubusercontent.com/langfuse/langfuse/main/LICENSE - the Langfuse column: MIT core with the proprietary ee/ carve-out and the ClickHouse copyright
- https://langfuse.com/pricing - the Langfuse column: cloud tiers, billable units, and self-hosting
