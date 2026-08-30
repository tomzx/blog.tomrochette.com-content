---
title: OpenCodeReview
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation, code-review, ci, open-source]
readability: 3
audience_notes: >
  Teams automating code review on pull requests who want deterministic control over what an LLM reviewer sees and says.
  Assumes you know what a git diff and a CI pipeline are.
---

OpenCodeReview (`ocr`) is Alibaba's Apache-2.0 Go CLI for AI code review that combines deterministic engineering pipelines, file selection, bundling, and rule matching, with an LLM agent to produce line-precise review comments, runnable locally, in CI, or inside coding agents.
Facts below verified as of 2026-08-30.

**OpenCodeReview's thesis is that a reviewer agent needs engineering around it, not just a prompt, and its own benchmark discloses the cost of that thesis: higher precision, deliberately lower recall, real defects will slip through.**

## What it is

A Go binary (npm-distributed) that reads git diffs, workspace, branch range via merge-base, single commit, or whole directories with `ocr scan`, and emits structured, line-level comments with resumable sessions and JSON output.
The deterministic side picks and filters files, bundles related files for isolated sub-agents, and matches template-engine rules; the agent side carries review-tuned prompts and a toolset distilled from production traces, with a README claim of about one ninth the tokens and higher precision than a general agent on the same model.
Deployment is unusually broad: local CLI, GitHub Action, GitLab CI, Gerrit, plugins for Claude Code, Codex, Cursor, and OpenCode, an MCP server, a VS Code extension, and a delegation mode where your own coding agent reviews while `ocr` handles selection and rules.
Apache-2.0, from Alibaba, open-sourced in May 2026 after two years of internal use at claimed tens of thousands of developers, with an OpenSSF Gold badge and a public benchmark (AACR-Bench: 200 real PRs, 10 languages).

## Status

High-velocity young: 21,636 stars, 1,599 forks, 150 open issues and PRs as of 2026-08-30, created 2026-05-18.
114 releases in three and a half months (v1.11.0 on 2026-08-28), a 284-point Hacker News front-page thread in June.
**Adoption outran polish visibly: GPT-5.x compatibility broke at launch and was fixed, and the lead has said parts of the codebase are not yet fully polished.**

## Strengths

- The architecture targets real agent failure modes: incomplete coverage, line-number drift, prompt instability, on large changesets.
- Ships a public benchmark and transparently discloses its recall disadvantage, which is better evidence behavior than most of the category.
- One tool covers local, CI, plugin, and delegation deployments with model choice and BYO keys.
- Rules cover roughly 47 languages and file types, from NPE and thread-safety to XSS and SQL injection.

## Cautions

- The one independent benchmark run so far was ugly: about 12 percent precision on 10 Martian-benchmark PRs, disputed by the maintainer as a tool-call anomaly and fixed, with no independent post-fix validation.
- Recall is deliberately lower than a general agent; teams wanting maximum defect-finding should know that is not this tool's bet.
- Rule docs originated in Chinese with community translations later mainlined, and the docs site is a client-rendered SPA that resisted verification.
- Alibaba-priority dependency on a single dominant contributor.

## Pricing

Free and open source under Apache-2.0, no paid tiers.
Costs are your own LLM API calls, or zero in delegation mode where your existing agent does the judging.

## Compared to

- [Greptile](../greptile/index.md): hosted, codebase-indexed review; choose OpenCodeReview when code must stay in-house and you want model and token control.
- CodeRabbit: turnkey commercial bot with per-seat pricing; choose it for zero-wiring convenience, `ocr` for the same category at license cost zero plus wiring effort.
- Plain agent review of `git diff`: free and fine for small diffs; `ocr`'s pitch is exactly that agents alone cut corners on large changesets, and its delegation mode is the middle path.

## Bottom line

**Recommended for teams that want self-hosted, rule-aware, line-precise automated review in CI with their own model keys, and that understand the precision-over-recall trade.**
Not for teams needing independently validated precision numbers today, or turnkey hosted review without wiring.

## See also

- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [Greptile](../greptile/index.md) - the hosted review alternative
- [Plannotator](../plannotator/index.md) - the human-annotation surface for the same problem
- [Hybrid Execution Feature Matrix](../hybrid-execution-feature-matrix/index.md) - the deterministic-orchestrates-LLM principle at review scale

## References

- https://github.com/alibaba/open-code-review - repository, architecture, integrations, license
- https://raw.githubusercontent.com/alibaba/open-code-review/HEAD/README.md - the hybrid design, benchmark claims, and recall trade-off
- https://news.ycombinator.com/item?id=48406358 - the launch thread with the independent precision run and maintainer responses
- https://huggingface.co/datasets/Alibaba-Aone/aacr-bench - the public benchmark backing the claims
- https://registry.npmjs.org/@alibaba-group/open-code-review - distribution and release facts
- https://codereview.withmartian.com - the independent benchmark used for the critical precision measurement
