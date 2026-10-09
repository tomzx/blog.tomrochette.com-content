---
title: tool-eval-bench
created: 2026-10-08
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, hybrid-execution, tool-calling, benchmarking, structured-outputs, open-source]
readability: 3
audience_notes: >
  Engineers running their own serving stack (vLLM, SGLang, llama.cpp, LiteLLM) whose agents depend on tool calls, and anyone comparing this category's measurement layer.
  Assumes you know what a tool call and a deterministic mock are.
---

tool-eval-bench is an MIT benchmark harness that audits how well an LLM serving stack actually calls tools, running 69 deterministic multi-turn scenarios plus 23 opt-in Hard Mode ones against any OpenAI-compatible endpoint, with a second track that scores Jev-class decision-model probabilities over the same `/v1/systemone` surface the rest of this category speaks.

**It is the first member aimed at the tool-calling half of this category's contract rather than the decision half, and its distinguishing property is determinism: mock tools with seeded payload noise, a fixed in-prompt date, and a full conversation trace per scenario, so a failing scenario is a bug report you can replay rather than a vibe.**

## What it is

A Python CLI (installed from git with `uv tool install`, or Docker) that drives scenarios through OpenAI-compatible `/v1/chat/completions` endpoints on vLLM, SGLang, LiteLLM, llama.cpp, NInfer, and TensorFold, plus hosted Gemini and Anthropic.
Each scenario observes one assistant conversation with mock tools, 12 universal tools or 52 in the large-toolset scenarios, and payloads carry deliberate noise so a model that can only read clean fixtures does not pass.
Every scenario is scored by a deterministic evaluator as PASS (2), PARTIAL (1), or FAIL (0), the loop runs to an 8-turn default limit, and multi-trial runs report Pass@k and Pass^k; throughput, long-context retrieval, and accuracy benchmarks run against the same endpoint.
The lineage is a credited extension of ToolCall-15, positioned by the project's own related-work table against BFCL, ToolBench, API-Bank, and PinchBench as the local-first, multi-turn, deterministic option.
The decision-model track (`--decision`) measures how accurate a `/v1/systemone` endpoint's probabilities are and whether high confidence is trustworthy, aborting with a message rather than scoring zeros when the surface is missing.

## Status

Active, six months old, and steadily released: created 2026-04-17, v2.7.0 published 2026-09-21 (v2.5.0 and v2.6.0 in August), pushed 2026-10-07, with 378 stars and 50 forks as of 2026-10-08.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=SeraphimSerapis/tool-eval-bench&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=SeraphimSerapis/tool-eval-bench&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=SeraphimSerapis/tool-eval-bench&type=date&legend=top-left" />
</picture>

The community footprint is thin and stated plainly: no Hacker News story of its own as of 2026-10-08 (two comment mentions, June and July, via the Algolia search API), so adoption evidence is the star and release record, not forum debate.
The engineering inside is unusually disciplined for that footprint: the repository carries 3,125 tests at an 85 percent branch-coverage gate, AST-enforced architecture boundaries, and a self-published August 2026 quality review that names its own weak point ("The problem is not quality. It is approachability.").

## Strengths

- **Determinism is the design center: seeded runs (`--seed`), mock tools with reproducible noise, a fixed in-prompt date, and per-scenario traces, so results are auditable and re-runnable in a way model-judged evals are not.**
- It measures the half of this category no other scoreboard touches: whether a serving stack picks the right tool, passes the right parameters, chains calls across turns, and holds safety boundaries (Category K includes prompt-injection resistance), where JevBench and the Decision Index score decision models only.
- The `/v1/systemone` decision track extends the same audit to this category's contract, scoring probability accuracy and confidence trustworthiness, and it refuses to silently zero a missing surface.
- The self-audit culture is visible: the August 2026 quality review documents what was measured and what is wrong, alongside CI running Python 3.11 through 3.13 with varying seeds.

## Cautions

- **The README states its own limits: difficulty tiers are author estimates, not calibrated rankings, localization coverage is German-focused, and it measures single-assistant conversations, not independent agents, delegation, or handoffs.**
- There is no standing leaderboard: results are per-run artifacts, so it audits your stack rather than ranking the field, and nothing here lets you compare hosted vendors without running them yourself.
- Self-graded end to end: the evaluators are the author's deterministic functions, and the thin community footprint means the scenario design has had no public stress-testing.
- Coverage breadth costs depth per backend: 69 scenarios is small next to BFCL's 1,700-plus tests, a trade the related-work table owns.

## Pricing

Free and open source under MIT; pricing does not apply.
The costs are your endpoint's tokens per scenario and your time, multiplied on multi-trial runs.

## Compared to

- [JevBench](../jevbench/index.md): the other in-category benchmark; JevBench ranks decision models on a standing public board, tool-eval-bench audits one endpoint's tool calling on demand and adds the decision-model accuracy track without a ranking.
- [Decision Index](../decision-index/index.md): breadth over decision models with a frozen public suite; tool-eval-bench is depth over tool calls with per-scenario traces and no board.
- BFCL (Berkeley's Function Calling Leaderboard): the large-scale function-calling eval for hosted APIs; per the project's own comparison, tool-eval-bench targets self-hosted stacks with multi-turn orchestration and deterministic mock tools instead.

## Bottom line

**Recommended as a pre-deployment audit for engineers whose agents put tool calls through their own serving stack, run with `--seed` and read scenario by scenario rather than as one number.**
Not as a public scoreboard for shopping hosted vendors, and not for end-to-end agent task completion, which it deliberately does not measure.
The disagreeable claim I will defend: this category spent September learning to measure decisions and has no measurement at all for the tool calls wrapped around them, and a deterministic, trace-first auditor is worth more to a serving-stack owner than another leaderboard row.

## Changes

- 2026-10-08 - Created from the entrant scan (the structured-output and tool-calling sweep), the category's third benchmark member.

## See also

- [JevBench](../jevbench/index.md) - the standing decision-model scoreboard beside this on-demand audit
- [Decision Index](../decision-index/index.md) - the breadth scoreboard for the decision-model half
- [Jev](../jev/index.md) - the contract whose `/v1/systemone` surface this benchmark's decision track reads
- [OpenAI Structured Outputs](../openai-structured-outputs/index.md) - the vendor strict mode whose tool-call guarantee this audits the failure side of
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/SeraphimSerapis/tool-eval-bench - repository: MIT, created 2026-04-17, 378 stars, 50 forks, pushed 2026-10-07 (GitHub API, as of 2026-10-08)
- https://raw.githubusercontent.com/SeraphimSerapis/tool-eval-bench/main/README.md - the 69-plus-23 scenario design, backends, pass/partial/fail scoring, install paths, and the stated limitations
- https://raw.githubusercontent.com/SeraphimSerapis/tool-eval-bench/main/docs/methodology.md - the 3-tier scoring rationale, the 12 and 52-tool sets, the 8-turn loop, and deterministic noise
- https://raw.githubusercontent.com/SeraphimSerapis/tool-eval-bench/main/docs/decision-models.md - the `/v1/systemone` decision-model track and its missing-surface abort behavior
- https://raw.githubusercontent.com/SeraphimSerapis/tool-eval-bench/main/docs/quality-review-2026-08.md - the author's August 2026 quality review: test counts, coverage gate, and the approachability finding (the critical source)
- https://raw.githubusercontent.com/SeraphimSerapis/tool-eval-bench/main/docs/related-work.md - the BFCL, ToolBench, API-Bank, ToolCall-15, and PinchBench comparison table grounding the lineage claims
- https://raw.githubusercontent.com/SeraphimSerapis/tool-eval-bench/main/docs/backends.md - the served-stack adapter coverage (fetched 200, 2026-10-08)
- https://api.github.com/repos/SeraphimSerapis/tool-eval-bench/releases - v2.5.0 through v2.7.0, 2026-08-05 to 2026-09-21 (fetched 2026-10-08)
- https://hn.algolia.com/api/v1/search?query=%22tool-eval-bench%22 - the thin-footprint record: no story, two comment mentions (fetched 2026-10-08)
