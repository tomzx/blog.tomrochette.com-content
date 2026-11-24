---
title: OpenCodeReview
created: 2026-08-30
updated: 2026-11-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, evaluation, code-review, ci, open-source]
readability: 3
audience_notes: >
  Teams automating code review on pull requests who want deterministic control over what an LLM reviewer sees and says.
  Assumes you know what a git diff and a CI pipeline are.
---

OpenCodeReview (`ocr`) is Alibaba's Apache-2.0 Go CLI for AI code review that combines deterministic engineering pipelines, file selection, bundling, and rule matching, with an LLM agent to produce line-precise review comments, runnable locally, in CI, or inside coding agents.

**OpenCodeReview's thesis is that a reviewer agent needs engineering around it, not just a prompt, and its own benchmark discloses the cost of that thesis: higher precision, deliberately lower recall, real defects will slip through.**

## What it is

A Go binary (npm-distributed) that reads git diffs, workspace, branch range via merge-base, single commit, or whole directories with `ocr scan`, and emits structured, line-level comments with resumable sessions and JSON output.
The deterministic side picks and filters files, bundles related files for isolated sub-agents, and matches template-engine rules; the agent side carries review-tuned prompts and a toolset distilled from production traces, with a README claim of about one ninth the tokens and higher precision than a general agent on the same model.
Deployment is unusually broad: local CLI, GitHub Action, GitLab CI, Gerrit, plugins for Claude Code, Codex, Cursor, and OpenCode, an MCP server, a VS Code extension, and a delegation mode where your own coding agent reviews while `ocr` handles selection and rules.
Apache-2.0, from Alibaba, open-sourced in May 2026 after two years of internal use at claimed tens of thousands of developers, with an OpenSSF Gold badge and a public benchmark (AACR-Bench: 200 real PRs, 10 languages).

## Status

High-velocity young: 46,915 stars, 3,406 forks, 306 open issues and PRs as of 2026-10-13, created 2026-05-18.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=alibaba/open-code-review&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=alibaba/open-code-review&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=alibaba/open-code-review&type=date&legend=top-left" />
</picture>

That is up from 23,041 stars on 2026-09-13, 29,564 on 2026-09-16, 35,673 on 2026-09-18, 37,926 on 2026-09-20, 38,670 on 2026-09-21, 40,800 on 2026-09-24, 41,702 on 2026-09-27, 42,421 on 2026-09-29, 43,189 on 2026-10-02, 43,411 on 2026-10-03, 43,529 on 2026-10-04, 43,886 on 2026-10-06, 44,113 on 2026-10-07, 44,730 on 2026-10-09, 45,649 on 2026-10-10, 45,964 on 2026-10-11, and 46,915 on 2026-10-13, roughly doubling in the month after mid-September, still with no new HN catalyst on the launch thread, which sits at the same 284 points (re-checked 2026-10-13).
At least 154 releases in five and a half months (v1.14.2 on November 23 adds a Turkish README, site docs, and VS Code localization and a rule fix for BOM-prefixed Objective-C source, after v1.14.1 on November 22 brings behavior and impact into native and delegated reviews, rejects workspace named pipes before opening them, fails the GitFlic and Gerrit example jobs when a review fails, and shows token usage in analysis reports, after v1.14.0 on November 21 adds an optional behavior-and-impact analysis pass, severity-ordered findings in review and scan output, SQL, Dhall, and Ruby review rules beside refined Rust rules and Cargo test/benchmark path exclusions, CUDA and HIP review support, a stable report header across tabs, TypeScript module extensions in review, and a fix for the GitLab CI check-mark LGTM posted on failed reviews, after v1.13.13 on November 19 links the leaderboard to AACR-Bench, reserves the complete compression-context budget, drains OAuth callback responses before closing, and lazy-loads documentation content by language, after v1.13.12 on November 18 keeps session finding-identity fields separate, bounds file_read result bytes instead of only line counts, returns non-zero on partial operational failures, and serializes lazy telemetry initialization, after v1.13.11 on November 17 added branch-filtered session listing and Move review rules while fixing session compares across path spellings, multibyte path truncation on rune boundaries, dotted MCP server names in `config set`, and rune-boundary cuts to summary comments, after v1.13.10 on November 15 defaults `--to` to HEAD when only `--from` is given, renders Markdown summaries with styled progress output in the CLI, adds `--resume` for workspace mode, and gives workspace mode access to the code on the comparison side, after v1.13.9 on November 13 records excluded files in run coverage, shows Action warnings in zero-finding PR summaries, updates vulnerable dependencies, emits [] instead of null from `session list --json`, and enforces per-request tool declarations, after v1.13.8 on November 12 added GitHub Copilot CLI integration through a plugin manifest and guide, review of both sides of a comparison, and MiniMax M3.1 Flash in model suggestions while refactoring tool bindings into task templates and removing the `--tools` CLI overrides in a breaking change, after v1.13.7 on November 10 gated PLAN_TASK on file size, made saved sessions inspectable by ID from any directory, and added Clojure and ClojureScript review rules while fixing a postinstall 404 crash and separating review tasks from the shared runtime loop, after v1.13.6 on November 5 added Starlark file review, C# review rules, and a supported-model-providers showcase page while preserving explicit false stream overrides and making the GitHub Action rewrite only the bot's own summary comment, after v1.13.5 on November 3 added HAML, Slim, ERB, EJS, Liquid, and Nunjucks template review, jsonc files, and Scala-specific rules while fixing diff-hunk matching, and v1.13.4 on November 2 fixed unnamed paths in file_read_diff errors, empty session-show JSON output, and GitHub Action runtime stability and bumped Go to 1.26.10 and Node to 24.22.1), a 284-point Hacker News front-page thread in June.
v1.13.0 moved to a minor bump for two integrations: reviews on the ChatGPT plan through the public Responses API, and an ACP service so coding agents can drive OpenCodeReview over the agent protocol.
An outside measurement has now landed: the Agent Skills Hub end-to-end eval (October 10, 2026) scored it 7 of 8 planted defects at 0.6 findings per PR in 7 minutes, among the quietest reviewers that ran, with both misses being test-only PRs it deliberately skipped, so the precision-first story held under independent testing.
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
- [CodeRabbit](../coderabbit/index.md): turnkey commercial bot with per-seat pricing; choose it for zero-wiring convenience, `ocr` for the same category at license cost zero plus wiring effort.
- [Qodo](../qodo/index.md): the open-core middle path, MIT PR-Agent to self-host or paid Qodo Merge.
- Plain agent review of `git diff`: free and fine for small diffs; `ocr`'s pitch is exactly that agents alone cut corners on large changesets, and its delegation mode is the middle path.

## Bottom line

**Recommended for teams that want self-hosted, rule-aware, line-precise automated review in CI with their own model keys, and that understand the precision-over-recall trade.**
Not for teams needing independently validated precision numbers today, or turnkey hosted review without wiring.

## Changes

- 2026-08-30 - Created as an evaluation note on Alibaba's hybrid reviewer.
- 2026-08-30 - Moved into the new Code review category, with see-also links updated to the category matrix.
- 2026-09-16 - Refreshed the growth record: 29.5k stars and 2.1k forks (up from 23k in three days), 127 releases with v1.12.3 shipping September 16.
- 2026-09-18 - The star burst continued: 35.7k stars and 2.5k forks (up roughly 21 percent in two days), 129 releases with v1.12.5 shipping September 17, still with no new HN catalyst.
- 2026-09-20 - The burst kept compounding: 37.9k stars and 2.7k forks (up roughly 6 percent in two days), 131 releases with v1.12.7 shipping September 19, still with no new HN catalyst.
- 2026-09-21 - Growth continued: 38.7k stars and 2.8k forks, v1.12.7 still latest, and the launch thread still stalled at 284 points with no new HN catalyst.
- 2026-09-24 - The burst continues: 40.8k stars and 2.9k forks (up roughly 6 percent in three days), 133 releases with v1.12.9 shipping September 22, still with no new HN catalyst.
- 2026-09-27 - The burst slows but continues: 41.7k stars and 3.0k forks (up roughly 2 percent in three days), v1.12.9 still latest, and the launch thread still at 284 points with no new HN catalyst.
- 2026-09-29 - The burst continues: 42.4k stars and 3.0k forks (up roughly 2 percent in two days), 134 releases with v1.12.10 shipping September 28 (OpenRouter as a provider, an `ocr session rm` command), still with no new HN catalyst.
- 2026-10-07 - Added the alibaba/open-code-review star history chart to the Status section.
- 2026-10-09 - Refreshed the growth ledger: 44,730 stars, v1.12.13 (October 8) as release 137, launch thread unchanged at 284 points.
- 2026-10-13 - Recorded v1.13.0 (October 13): ChatGPT-plan reviews through the public Responses API and a new ACP service, taking the ledger to 138 releases and 46,915 stars; launch thread unchanged at 284 points.
- 2026-10-18 - Recorded the Agent Skills Hub end-to-end eval (October 10): 7 of 8 planted defects at 0.6 findings per PR, among the quietest tools tested, the two misses being test-only PRs it deliberately skipped; the precision-first trade held under independent testing.
- 2026-10-20 - Recorded v1.13.2 (October 20): Nushell and PowerShell review support plus Shader Languages allowlist entries, taking the ledger past 140 releases.
- 2026-10-22 - Recorded v1.13.3 (October 22): empty review-comment batches now reported instead of silently succeeding, MCP tools/list pagination honored, CI checkout-state pollution fixed, and a NixPkgs provider directory added.
- 2026-10-27 - Rotation re-verification: every cited URL re-fetched live; v1.13.3 still the latest release with the push still October 22, the launch thread unchanged at 284 points, the AACR-Bench dataset live at 2.15k rows under Apache-2.0, the Martian benchmark site up, and the Agent Skills Hub eval table unchanged (7 of 8, 0.6 findings per PR, pr-12 the only miss); no factual drift.
- 2026-10-30 - Volatile re-verification: the push moved to October 30 with no release after v1.13.3.
- 2026-11-05 - Volatile re-verification: recorded v1.13.4 (November 2) and v1.13.5 (November 3) and counted the ledger at 143 releases; the push moved to November 5 with main active the same day.
- 2026-11-07 - Volatile re-verification: recorded v1.13.6 (November 5), the Starlark and C# review coverage, the supported-model-providers showcase page, and the Action summary-comment fix, taking the ledger to 144 releases; the push moved to November 6 with main active the same day.
- 2026-11-11 - Volatile re-verification: recorded v1.13.7 (November 10), the file-size gate on PLAN_TASK, saved sessions inspectable by ID from any directory, Clojure and ClojureScript review rules, the postinstall 404 fix, and the runtime split of review tasks from the shared loop, taking the ledger to 145 releases; the push moved to November 11 with main active the same day.
- 2026-11-13 - Volatile re-verification: recorded v1.13.8 (November 12), GitHub Copilot CLI integration (plugin manifest and guide), review of both comparison sides, MiniMax M3.1 Flash in model suggestions, tool bindings refactored into task templates, and the breaking removal of `--tools` CLI overrides, taking the ledger to 146 releases; the push moved to November 13 with main active the same day.
- 2026-11-14 - Volatile re-verification: recorded v1.13.9 (November 13), excluded files recorded in run coverage, Action warnings shown in zero-finding PR summaries, vulnerable dependencies updated, `session list --json` emitting [] instead of null, and tool declarations enforced per request, taking the ledger to 147 releases; the push moved to November 14 with main active the same day.
- 2026-11-15 - Volatile re-verification: recorded v1.13.10 (November 15), `--to` defaulting to HEAD when only `--from` is given, Markdown summaries with styled progress output in the CLI, `--resume` for workspace mode, and comparison-side code access in workspace mode, taking the ledger to 148 releases; the push and main's latest commit both moved to November 15.
- 2026-11-18 - Volatile re-verification: recorded v1.13.11 (November 17, branch-filtered session listing and Move review rules, plus session-compare, multibyte-path, dotted-MCP-name, and rune-boundary summary fixes) and v1.13.12 (November 18, finding-identity fields kept separate, file_read byte bounds, non-zero exits on partial operational failures, lazy telemetry serialization), taking the ledger to 150 releases; the push and main's latest commit both moved to November 18.
- 2026-11-20 - Volatile re-verification: recorded v1.13.13 (November 19, the AACR-Bench leaderboard linked from the pages, the complete compression-context budget reserved, OAuth callback responses drained, documentation content lazy-loaded by language), taking the ledger to 151 releases; the push and main's latest commit both moved to November 20.
- 2026-11-21 - Volatile re-verification: recorded v1.14.0 (November 21, a minor bump: the optional behavior-and-impact analysis pass, severity-ordered findings in review and scan output, SQL, Dhall, and Ruby review rules, refined Rust rules with Cargo test and benchmark path exclusions, CUDA and HIP review support, and the GitLab-CI failed-review LGTM fix), taking the ledger to 152 releases; the push and main's latest commit both moved to November 21.
- 2026-11-22 - Volatile re-verification: the push and main's latest commit both moved to November 22 (a workspace named-pipe fix); v1.14.0 still the latest release at 152 releases.
- 2026-11-24 - Volatile re-verification: recorded v1.14.1 (November 22, behavior and impact included in native and delegated reviews, workspace named pipes rejected before opening, the GitFlic and Gerrit example jobs failing when a review fails, token usage shown in analysis reports) and v1.14.2 (November 23, a Turkish README, site docs, and VS Code localization, plus a rule fix for BOM-prefixed Objective-C source), taking the ledger to 154 releases; pushed_at moved to November 23 with main's latest commit November 22 (the Turkish localization merge).

## See also

- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - the category comparison this note joins
- [Greptile](../greptile/index.md) - the hosted review alternative
- [Plannotator](../../evaluation-review/plannotator/index.md) - the human-annotation surface for the same problem
- [Hybrid Execution Feature Matrix](../../hybrid-execution/hybrid-execution-feature-matrix/index.md) - the deterministic-orchestrates-LLM principle at review scale

## References

- https://github.com/alibaba/open-code-review - repository, architecture, integrations, license, 45,964 stars as of 2026-10-11; re-queried 2026-10-30, 2026-11-05, 2026-11-07, 2026-11-11, 2026-11-13, 2026-11-14, 2026-11-15, 2026-11-18, 2026-11-20, 2026-11-21, 2026-11-22, and 2026-11-24, pushed November 20 with main active the same day (a docs translation sync), pushed November 21 with main active the same day, pushed November 22 with main active the same day (a workspace named-pipe fix), pushed November 23 with main's latest commit November 22 (the Turkish localization merge)
- https://raw.githubusercontent.com/alibaba/open-code-review/HEAD/README.md - the hybrid design, benchmark claims, and recall trade-off
- https://news.ycombinator.com/item?id=48406358 - the launch thread with the independent precision run and maintainer responses
- https://huggingface.co/datasets/Alibaba-Aone/aacr-bench - the public benchmark backing the claims
- https://registry.npmjs.org/@alibaba-group/open-code-review - distribution and release facts, re-fetched 2026-10-27 (130 versions, v1.13.3 latest)
- https://api.github.com/repos/alibaba/open-code-review/releases?per_page=3 - the release ledger's top entries: v1.14.2 (November 23, the Turkish README, site docs, and VS Code localization, plus the BOM-prefixed Objective-C rule fix), v1.14.1 (November 22, behavior and impact in native and delegated reviews, workspace named pipes rejected before opening, the GitFlic and Gerrit example jobs failing on review failure, token usage in analysis reports), v1.14.0 (November 21, the behavior-and-impact analysis pass, severity-ordered findings in review and scan output, the SQL, Dhall, and Ruby review rules, refined Rust rules with Cargo test and benchmark path exclusions, CUDA and HIP review support, and the GitLab-CI failed-review LGTM fix), v1.13.13 (November 19), v1.13.12 (November 18, 2026) with session finding-identity fields kept separate, file_read result bytes bounded, non-zero exits for partial operational failures, and lazy telemetry initialization serialized, v1.13.11 (November 17) with branch-filtered session listing, Move review rules, and the session-compare, multibyte-path, dotted-MCP-name, and rune-boundary summary fixes, v1.13.10 (November 15) with `--to` defaulting to HEAD when only `--from` is given, Markdown summaries and styled progress output in the CLI, `--resume` for workspace mode, and comparison-side code access in workspace mode, v1.13.9 (November 13) with excluded files recorded in run coverage, warnings shown in zero-finding PR summaries, vulnerable-dependency updates, `session list --json` emitting [] instead of null, and per-request tool declarations enforced, and v1.13.8 (November 12) with GitHub Copilot CLI integration, both-sides comparison review, MiniMax M3.1 Flash model suggestions, the task-template tool-binding refactor, and the breaking `--tools` removal, fetched 2026-10-22, re-fetched 2026-10-27, 2026-10-30, 2026-11-05, 2026-11-07, 2026-11-11, 2026-11-13, 2026-11-14, 2026-11-15, 2026-11-18, 2026-11-20, 2026-11-21, 2026-11-22, and 2026-11-24 (v1.14.2 latest, 154 releases)
- https://codereview.withmartian.com - the independent benchmark used for the critical precision measurement
- https://raw.githubusercontent.com/zhuyansen/agent-skills-hub/main/ops/review-runs/RESULTS.md - the Agent Skills Hub end-to-end eval (October 10, 2026): 7 of 8 planted defects, 0.6 findings per PR, 7 minutes, both misses test-only PRs it skipped, fetched 2026-10-18
