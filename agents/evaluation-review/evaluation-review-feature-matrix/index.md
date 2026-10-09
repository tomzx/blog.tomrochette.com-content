---
title: "Evaluation and Review Feature Matrix"
created: 2026-08-30
updated: 2026-10-08
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, evaluation, code-review, human-in-the-loop]
readability: 3
audience_notes: >
  Engineers choosing where quality control lives in their agent workflow: CI gates, dashboards, machine review, or human annotation.
  Assumes you know what an LLM-as-judge metric and a git diff are; each column links to a full note with sources.
---

This matrix compares the ten members of the Evaluation and review category: the pytest-style eval framework, two public harness benchmarks (the vendor-run FrontierHarness Eval and the academic HarnessTax), GitHub's open AI-code-review benchmark (ReviewBench), the typed decision-model eval library (Jevals), two observability and evaluation platforms (Langfuse and Phoenix), the human annotation surface, the terminal review surface, and the agent-driven local debugger.
The hybrid machine reviewer that used to sit here, OpenCodeReview, moved to the Code review category when this matrix was created, on 2026-08-30.

**The category divides on who judges: the agent itself (Workshop), a metric suite (deepeval), a typed decision model (Jevals), an observability platform's judges (Langfuse, Phoenix), a human (Plannotator, Hunk), or a fixed public benchmark's official evaluator (FrontierHarness Eval, HarnessTax, ReviewBench), and mature teams run more than one column at once.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [deepeval](../deepeval/index.md) | [FrontierHarness Eval](../frontierharness-eval/index.md) | [HarnessTax](../harnesstax/index.md) | [Hunk](../hunk/index.md) | [Jevals](../jevals/index.md) | [Langfuse](../langfuse/index.md) | [Phoenix](../phoenix/index.md) | [Plannotator](../plannotator/index.md) | [ReviewBench](../reviewbench/index.md) | [Workshop](../workshop/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | pytest-style eval framework | public multi-harness benchmark, vendor-run | public benchmark study, academic | review-first terminal diff viewer (TUI) for agent-authored changesets | typed decision-model evals and guardrails library (Jev-class judges) | OSS LLM/agent observability and evaluation platform | observability and eval platform | visual plan and diff review UI | open AI-code-review benchmark from GitHub with a public leaderboard | local agent debugger plus eval loop |
| Object judged | LLM app outputs (agents, RAG, chat) | coding-agent harnesses on fixed tasks | model-harness pairs on SWE-bench Lite and Terminal-Bench 2.0 | agent-authored diffs: working trees, commits, PRs, and patches | agent traces (messages, tool calls, tool results) and RAG outputs | traces, sessions, dataset runs, and experiment outputs | traces, spans, experiment outputs | agent plans and diffs | AI code-review agents on 219 public pull requests sampled from GitHub at large | agent traces and code behavior |
| Judge | ~50 LLM-judge metrics plus deterministic checks | fixed 30-task suite, deterministic scoring | official benchmark evaluators, 3 attempts per task, bootstrap confidence intervals | the human reading the stream; agents annotate but render no verdict | Jev-class decision models returning a calibrated probability per typed question, one request per trace; chat LLMs as emulated fallback | managed LLM-as-judge evaluators, code evaluators, user feedback, human annotation queues | LLM evals, code evaluators, human annotations | human annotation | published rubric graded by Claude Sonnet 5, with an LLM matcher for finding correspondence; golden set from human reviewers, frontier LLMs, static analysis, and author follow-up commits | your coding agent writes and runs evals |
| Deployment | Python/TS SDK, CLI | web leaderboard, npx runner, public repo | free web report, public GitHub Pages repo, profiling traces promised | local TUI, standalone binary or npm (hunkdiff), macOS, Linux, and Windows | Python library over remote (TypeSafe, Vercel AI Gateway) or local (Kev, Laya, Eikos) backends, CLI and MCP server | cloud or self-hosted (Docker Compose locally, Kubernetes templates for production) | self-hosted server or Arize AX cloud | local browser app plus hooks | public leaderboard site, MIT dataset and self-serve runner in the repo | local daemon plus web UI |
| CI gating | ✓ non-zero exit on failure | ✗ a published study, not a gate | ✗ a published study, not a gate | ✗ a local pre-merge loop by design | ~ one definition runs offline, as a monitor, and as an in-loop gate; pytest-style gating is DIY | ~ experiments and evals via SDK and API, not a pytest-style gate | ~ experiments, not gate-native | ✗ pre-merge local loop | ✗ an offline benchmark, not a gate | ✗ named gap in its own thread |
| Harness integration | tracing integrations | 9 harnesses, 12 configs, agent-neutral re-run skill | 3 harnesses (Claude Code, Codex CLI, Pi) across 7 models | any agent through its generated skill file and the session comment API, with live-session control | MCP server (Cursor, Claude Code, Copilot), Claude Code PreToolUse hook, OpenAI Agents SDK, LangGraph, and Claude Agent SDK adapters | Python/JS SDKs, native OpenTelemetry, 100+ framework integrations, agent skill, CLI, MCP server | OTel auto-instrumentation, MCP server | hooks in 9 harnesses | any reviewer via the agent contract (container image, config, own model key, judge provided); GitHub pre-ran the commercial entrants | skills and MCP for 5+ agents |
| Team layer | Confident AI platform | ✗ | ✗ | ✗ single-player local tool | ✗ no dashboard by design | cloud RBAC, SSO and Slack on the Teams add-on, Enterprise audit logs and SCIM | Arize AX cloud | encrypted links (caveat), Workspaces waitlist | ✗ public leaderboard, no team layer | Raindrop Cloud optional |
| License | ✓ Apache-2.0 | ✗ repository unlicensed | ✗ repository unlicensed | ✓ MIT | ✓ MIT | ~ MIT core, proprietary ee/ modules, ClickHouse-owned | ~ ELv2 core, Apache clients | ✓ Apache-2.0 or MIT | ✓ MIT | ✓ MIT |
| Maturity | mature, 3 years, v4.2 | new, first run 2026-08-31, 82-point HN launch | new, live 2026-09-16, 233-point HN thread (2026-10-07) | pre-1.0 (v0.23.x), six months, 9.5k stars (as of 2026-10-07) | alpha, 17 days old, v0.1.4, 102 stars (as of 2026-10-07) | mature, 3 years, v4.54.0 | mature, 4 years, v20.19 | pre-1.0 (v0.28.x), fast churn | research preview, launched 2026-10-05, 26 stars (as of 2026-10-07) | pre-1.0, 5 months |
| Pricing anchor | free, platform $200-2,000/mo | free to read, a re-run costs harness tokens | free to read, a re-run costs model tokens | free, MIT, no paid tier recorded | free, MIT; Jev backend $0.042/M input tokens | free self-hosted, cloud $29-2,499/mo | free, AX $50/mo entry | free, Workspaces unpriced | free to read and submit, your agent's tokens are the cost | free, Cloud $299/mo |

## Reading the matrix

**The CI-gating row is the buy line: deepeval gates merges today, Workshop's absence of CI is its sharpest recorded criticism, and Plannotator and Hunk deliberately serve the pre-merge loop instead.**

**The benchmark columns judge a different object than every other column: the systems that review or run the code, on public tasks, which makes them evidence for the tool-choice decision; FrontierHarness Eval and ReviewBench are the two columns with a structural conflict of interest, the first's publisher sells agent infrastructure and the second's sells the code reviewer that tops its own leaderboard, HarnessTax comes from academic authors, and ReviewBench's repository is MIT while the other two carry no license.**

**The judge row is the trust line.** An agent judging itself (Workshop) closes loops fastest and has the weakest evidentiary standing; metric suites inherit judge variance; Plannotator's and Hunk's humans are the only judges whose judgment you do not have to calibrate.

**The license row splits the vendors: MIT and Apache-2.0 columns are safe to embed, while Langfuse's proprietary ee/ modules and Phoenix's ELv2 core are the two cells that constrain what a business may do with the code, and Langfuse's is now held by ClickHouse, which acquired the project in January 2026.**

**Nobody here is redundant:** Workshop develops agents, deepeval gates them in CI, Jevals guards them in-loop with decision-model judges, Langfuse and Phoenix observe and evaluate them in production, Plannotator and Hunk steer them (browser and terminal), FrontierHarness prices the harness choice itself, HarnessTax cross-examines that price with academic independence, ReviewBench prices the reviewer choice the same way with the vendor-conflict caveat attached, and the maturity row says a realistic stack starts with the mature columns and adds the rest as the workflow demands.
Machine review of the pull requests themselves now lives in the [Code Review Feature Matrix](../../code-review/code-review-feature-matrix/index.md).

## Choosing from the matrix

- Want LLM behavior blocking merges in CI: deepeval.
- Want independent-ish cost and quality numbers before picking a harness: FrontierHarness Eval, vendor-run caveat attached.
- Want an independent second opinion on the harness-cost question: HarnessTax, the academic complement to FrontierHarness Eval.
- Want a shared yardstick for comparing AI code reviewers before picking one: ReviewBench, reading the publication-gate caveat first.
- Want MIT-licensed production tracing, evaluation, and prompt management in one platform: Langfuse, self-hosted or cloud, open-core edges and ClickHouse ownership accepted.
- Want production-grade tracing and evaluation under your own infrastructure: Phoenix, accepting ELv2.
- Want machine review of every pull request: the [Code Review Feature Matrix](../../code-review/code-review-feature-matrix/index.md), where OpenCodeReview moved.
- Want your annotations to steer a live agent session: Plannotator.
- Want a fast, annotated human read of a full changeset in the terminal: Hunk, paired with a judging column since it decides nothing.
- Want the trace-to-fix loop while developing an agent locally: Workshop.
- Want allow/escalate/block guardrails inside the agent loop at decision-model cost: Jevals, calibrated on your own labels first.

## Changes

- 2026-08-30 - Created with five columns on the who-judges axis, reduced to four the same day when the OpenCodeReview column was removed.
- 2026-09-05 - Extended to five columns with FrontierHarness Eval.
- 2026-09-07 - FrontierHarness Eval cell corrected to 82 points.
- 2026-09-13 - Corrected the intro sentence that tied the OpenCodeReview category move to the re-verification date; the move happened on 2026-08-30.
- 2026-09-16 - Phoenix maturity cell moved to v20.12 after the 2026-09-14 release.
- 2026-09-16 - Extended to six columns with Langfuse.
- 2026-09-18 - Phoenix maturity cell moved to v20.14 and Langfuse's to v4.38.0 after new releases.
- 2026-09-18 - Extended to seven columns with HarnessTax.
- 2026-09-20 - Refreshed the HarnessTax maturity cell to the thread's 229-point total; the deepeval and Phoenix download corrections live in their notes, no matrix cells carried them.
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-25 - Maturity cells refreshed: HarnessTax thread 232 points, Langfuse v4.45.2, Phoenix v20.16.
- 2026-09-29 - HarnessTax maturity cell refreshed to the thread's 233-point total; all other cells re-verified unchanged.
- 2026-10-02 - Maturity cells refreshed: Langfuse to v4.49.0, Phoenix to v20.19, and the HarnessTax thread as-of date; all other cells re-verified unchanged.
- 2026-10-03 - Maturity cell refreshed: Langfuse to v4.50.0; all other cells re-verified unchanged.
- 2026-10-06 - Maturity cells refreshed: Langfuse to v4.51.0, Plannotator to the v0.28.x line, and the HarnessTax thread as-of date; all other cells re-verified unchanged.
- 2026-10-06 - Extended from seven to eight columns with Jevals, sorted between HarnessTax and Langfuse, adding the typed decision-model judge to the who-judges axis; all other cells re-verified unchanged.
- 2026-10-06 - Extended from eight to nine columns with Hunk, the review-first terminal diff viewer that judges nothing itself, sorted between HarnessTax and Jevals, with the intro, who-judges line, judge-row sentence, CI-gating line, redundancy paragraph, and choosing list brought along.
- 2026-10-07 - Maturity cells refreshed: Langfuse to v4.53.0, Jevals to its 17-day age, and the Hunk, HarnessTax, and Jevals as-of dates moved; all other cells re-verified unchanged.
- 2026-10-07 - Extended from nine to ten columns with ReviewBench, GitHub's open AI-code-review benchmark, sorted between Plannotator and Workshop, with the intro, who-judges line, benchmark paragraph, redundancy sentence, and choosing list brought along.
- 2026-10-08 - Maturity cell refreshed: Langfuse to v4.54.0; all other cells re-verified unchanged.

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
- https://harnesstax.github.io/ - the HarnessTax column: findings, methodology, and the harness-tax framing
- https://github.com/HarnessTax/HarnessTax.github.io - the HarnessTax column: public repository and the unlicensed caveat
- https://github.com/Arize-ai/phoenix - the Phoenix column: OTel basis, ELv2, scale
- https://github.com/backnotprop/plannotator - the Plannotator column: hooks, nine harnesses, license
- https://github.com/langfuse/langfuse - the Langfuse column: repository, license split, adoption numbers
- https://raw.githubusercontent.com/langfuse/langfuse/main/LICENSE - the Langfuse column: MIT core with the proprietary ee/ carve-out and the ClickHouse copyright
- https://langfuse.com/pricing - the Langfuse column: cloud tiers, billable units, and self-hosting
