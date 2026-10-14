---
title: "Evaluation and Review Feature Matrix"
created: 2026-08-30
updated: 2026-10-13
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, evaluation, code-review, human-in-the-loop]
readability: 3
audience_notes: >
  Engineers choosing where quality control lives in their agent workflow: CI gates, dashboards, machine review, or human annotation.
  Assumes you know what an LLM-as-judge metric and a git diff are; each column links to a full note with sources.
---

This matrix compares the fifteen members of the Evaluation and review category: the harness-engineering platform that judges the work loop rather than outputs (Better Harness), the browser review surface for plans, diffs, running apps, and static HTML (Crit), the pytest-style eval framework, two public harness benchmarks (the vendor-run FrontierHarness Eval and the academic HarnessTax), GitHub's open AI-code-review benchmark (ReviewBench), the typed decision-model eval library (Jevals), two observability and evaluation platforms (Langfuse and Phoenix), the desktop eval workbench where non-engineers rate outputs (Kiln), the human annotation surface, the terminal review surface, the PR walkthrough visualizer (PR Lens), the citation-fabrication gate (Verbatim Citation Gate), and the agent-driven local debugger.
The hybrid machine reviewer that used to sit here, OpenCodeReview, moved to the Code review category when this matrix was created, on 2026-08-30.

**The category divides on who judges: the agent itself (Workshop), a metric suite (deepeval), a typed decision model (Jevals), a deterministic zero-token gate ahead of an LLM judge (Verbatim Citation Gate), an observability platform's judges (Langfuse, Phoenix), a human (Crit, Plannotator, Hunk, PR Lens), a workbench seeded by human ratings (Kiln), or a fixed public benchmark's official evaluator (FrontierHarness Eval, HarnessTax, ReviewBench), and mature teams run more than one column at once.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell below traces to a source cited there or in the references.

## The matrix

| Feature | [Better Harness](../better-harness/index.md) | [Crit](../crit/index.md) | [deepeval](../deepeval/index.md) | [FrontierHarness Eval](../frontierharness-eval/index.md) | [HarnessTax](../harnesstax/index.md) | [Hunk](../hunk/index.md) | [Jevals](../jevals/index.md) | [Kiln](../kiln/index.md) | [Langfuse](../langfuse/index.md) | [Phoenix](../phoenix/index.md) | [Plannotator](../plannotator/index.md) | [PR Lens](../pr-lens/index.md) | [ReviewBench](../reviewbench/index.md) | [Verbatim Citation Gate](../verbatim-citation-gate/index.md) | [Workshop](../workshop/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | harness-engineering platform, workflow findings over collected evidence | browser review surface (local web UI launched from a Go CLI) for agent plans, branch diffs, running apps, and static HTML | pytest-style eval framework | public multi-harness benchmark, vendor-run | public benchmark study, academic | review-first terminal diff viewer (TUI) for agent-authored changesets | typed decision-model evals and guardrails library (Jev-class judges) | local-first desktop eval workbench (GUI app plus MIT library) | OSS LLM/agent observability and evaluation platform | observability and eval platform | visual plan and diff review UI | PR diff visualization: animated architecture and data-flow diagrams commented on the pull request | open AI-code-review benchmark from GitHub with a public leaderboard | two-stage citation auditor: deterministic verbatim gate plus an any-model skeptical judge | local agent debugger plus eval loop |
| Object judged | the agent work loop (goals, steps, validation, safeguards, lessons), not individual outputs | agent-authored artifacts: plan and doc files, branch and PR/MR diffs, running dev servers, and static HTML pages | LLM app outputs (agents, RAG, chat) | coding-agent harnesses on fixed tasks | model-harness pairs on SWE-bench Lite and Terminal-Bench 2.0 | agent-authored diffs: working trees, commits, PRs, and patches | agent traces (messages, tool calls, tool results) and RAG outputs | task outputs rated by humans in the app, then judge metrics and eval datasets built from those ratings | traces, sessions, dataset runs, and experiment outputs | traces, spans, experiment outputs | agent plans and diffs | nothing: the change is rendered (blast radius, data flow, payloads) for the human to judge | AI code-review agents on 219 public pull requests sampled from GitHub at large | quote-style citations in RAG answers: fabricated, frankenquote, and misattributed quotes | agent traces and code behavior |
| Judge | model analysis producing findings with acceptance checks and validation routes | the human commenting in the browser; story mode adds an LLM-authored chaptered overview that explains but renders no verdict | ~50 LLM-judge metrics plus deterministic checks | fixed 30-task suite, deterministic scoring | official benchmark evaluators, 3 attempts per task, bootstrap confidence intervals | the human reading the stream; agents annotate but render no verdict | Jev-class decision models returning a calibrated probability per typed question, one request per trace; chat LLMs as emulated fallback | LLM-as-judge and G-Eval plus deterministic code judges, seeded by the team's own ratings (Eval Builder) | managed LLM-as-judge evaluators, code evaluators, user feedback, human annotation queues | LLM evals, code evaluators, human annotations | human annotation | none: the human watching the walkthrough; diagrams annotate but render no verdict | published rubric graded by Claude Sonnet 5, with an LLM matcher for finding correspondence; golden set from human reviewers, frontier LLMs, static analysis, and author follow-up commits | stage 1 substring matching over a normalized form (zero tokens), stage 2 a default-refute LLM judge that fails closed | your coding agent writes and runs evals |
| Deployment | self-hosted npm CLI plus thin host adapters; vendor is Qoder | single local Go binary (Homebrew core, go install, Nix, Windows release), web UI bound to 127.0.0.1, zero telemetry; sharing via crit.md or self-hosted crit-web | Python/TS SDK, CLI | web leaderboard, npx runner, public repo | free web report, public GitHub Pages repo, profiling traces promised | local TUI, standalone binary or npm (hunkdiff), macOS, Linux, and Windows | Python library over remote (TypeSafe, Vercel AI Gateway) or local (Kev, Laya, Eikos) backends, CLI and MCP server | desktop app (macOS, Windows, Linux) plus local Python library and REST server; datasets as JSON in your git | cloud or self-hosted (Docker Compose locally, Kubernetes templates for production) | self-hosted server or Arize AX cloud | local browser app plus hooks | GitHub App, GitHub Action, npm CLI (own model key), agent skill; GitHub, GitLab, Bitbucket | public leaderboard site, MIT dataset and self-serve runner in the repo | pip from the repository (not on PyPI), Python library | local daemon plus web UI |
| CI gating | ? not recorded | ✗ a local pre-merge loop by design, nothing exits nonzero on failure | ✓ non-zero exit on failure | ✗ a published study, not a gate | ✗ a published study, not a gate | ✗ a local pre-merge loop by design | ~ one definition runs offline, as a monitor, and as an in-loop gate; pytest-style gating is DIY | ~ the library and REST API run evals in code, no CI gate documented | ~ experiments and evals via SDK and API, not a pytest-style gate | ~ experiments, not gate-native | ✗ pre-merge local loop | ✗ a comment on the PR, not a gate | ✗ an offline benchmark, not a gate | ~ a library call, gate it in your own CI | ✗ named gap in its own thread |
| Harness integration | 10 documented hosts (Claude Code, Codex, Cursor, Copilot CLI, Qwen Code, Pi, Kimi Code, and more) | file protocol any agent can read; installers for 14 named agents (skills, slash commands, hooks), Claude Code plugin marketplace, the /crit loop, experimental send-to-agent live threads | tracing integrations | 9 harnesses, 12 configs, agent-neutral re-run skill | 3 harnesses (Claude Code, Codex CLI, Pi) across 7 models | any agent through its generated skill file and the session comment API, with live-session control | MCP server (Cursor, Claude Code, Copilot), Claude Code PreToolUse hook, OpenAI Agents SDK, LangGraph, and Claude Agent SDK adapters | none of the coding harnesses: it evaluates your AI tasks and models across 190+ providers or Ollama | Python/JS SDKs, native OpenTelemetry, 100+ framework integrations, agent skill, CLI, MCP server | OTel auto-instrumentation, MCP server | hooks in 9 harnesses | agent skill install plus a live canvas your coding agent joins | any reviewer via the agent contract (container image, config, own model key, judge provided); GitHub pre-ran the commercial entrants | none: an in-pipeline library with a (system, user) model contract | skills and MCP for 5+ agents |
| Team layer | ~ team and organization insights over task evidence | ~ shared review URLs (crit.md or self-hosted crit-web) with per-author color coding and organization visibility; no paid team tier recorded | Confident AI platform | ✗ | ✗ | ✗ single-player local tool | ✗ no dashboard by design | ✓ the point of the GUI: PMs, subject experts, and QA rate in the app, git sync for collaboration; Team tier adds enhanced Kiln Pro | cloud RBAC, SSO and Slack on the Teams add-on, Enterprise audit logs and SCIM | Arize AX cloud | encrypted links (caveat), Workspaces waitlist | ~ free for open source, no team tier recorded | ✗ public leaderboard, no team layer | ✗ solo library | Raindrop Cloud optional |
| License | ✓ MIT | ✓ MIT | ✓ Apache-2.0 | ✗ repository unlicensed | ✗ repository unlicensed | ✓ MIT | ✓ MIT | ~ MIT library and REST server, source-available fair-code desktop app | ~ MIT core, proprietary ee/ modules, ClickHouse-owned | ~ ELv2 core, Apache clients | ✓ Apache-2.0 or MIT | ✓ MIT | ✓ MIT | ✓ MIT | ✓ MIT |
| Maturity | early, npm 0.6.6 (2026-08-31), 2,374 stars as of 2026-10-13, no independent footprint | pre-1.0 (v0.22.0, 2026-10-07), about eight months, weekly releases claimed, 1,209 stars (as of 2026-10-13) | mature, 3 years, v4.2 | new, first run 2026-08-31, 82-point HN launch | new, live 2026-09-16, 233-point HN thread (2026-10-11) | pre-1.0 (v0.24 beta, v0.23.x stable), nearly seven months, 9.6k stars (as of 2026-10-13) | alpha, 21 days old, v0.1.4, 105 stars (as of 2026-10-13) | mature, 2+ years, v1.2.0 (2026-09-29), 5.2k stars (as of 2026-10-13) | mature, 3 years, v4.58.0 | mature, 4 years, v20.21 | pre-1.0 (v0.28.x), fast churn | new, seven weeks, v0.13.0, 1.9k stars (as of 2026-10-13) | research preview, launched 2026-10-05, 52 stars (as of 2026-10-13) | new, about three months, v0.2.0, 4 stars (as of 2026-10-11) | pre-1.0, 5 months |
| Pricing anchor | free, MIT, no hosted tier | free, MIT, no paid tier recorded; story mode bills your own model tokens | free, platform $200-2,000/mo | free to read, a re-run costs harness tokens | free to read, a re-run costs model tokens | free, MIT, no paid tier recorded | free, MIT; Jev backend $0.042/M input tokens | free Individual tier, Team and Enterprise by request | free self-hosted, cloud $29-2,499/mo | free, AX $50/mo entry | free, Workspaces unpriced | free for open source, no paid tier recorded | free to read and submit, your agent's tokens are the cost | free, MIT; the judge stage bills your model | free, Cloud $299/mo |

## Reading the matrix

**The CI-gating row is the buy line: deepeval gates merges today, Workshop's absence of CI is its sharpest recorded criticism, and Crit, Plannotator, Hunk, and PR Lens deliberately serve the pre-merge loop instead.**

**The benchmark columns judge a different object than every other column: the systems that review or run the code, on public tasks, which makes them evidence for the tool-choice decision; FrontierHarness Eval and ReviewBench are the two columns with a structural conflict of interest, the first's publisher sells agent infrastructure and the second's sells the code reviewer that tops its own leaderboard, HarnessTax comes from academic authors, and ReviewBench's repository is MIT while the other two carry no license.**

**The judge row is the trust line.** An agent judging itself (Workshop) closes loops fastest and has the weakest evidentiary standing; metric suites inherit judge variance; Verbatim Citation Gate's stage 1 is the only judge here that is neither a model nor a human, a substring check that cannot be sweet-talked; Crit's, Plannotator's, Hunk's, and PR Lens's humans are the judges whose judgment you do not have to calibrate.

**The license row splits the vendors: MIT and Apache-2.0 columns are safe to embed, while Langfuse's proprietary ee/ modules and Phoenix's ELv2 core are the two cells that constrain what a business may do with the code, and Langfuse's is now held by ClickHouse, which acquired the project in January 2026.**

**Nobody here is redundant:** Workshop develops agents, deepeval gates them in CI, Jevals guards them in-loop with decision-model judges, Langfuse and Phoenix observe and evaluate them in production, Plannotator, Hunk, and PR Lens steer and explain them (browser, terminal, and the pull request itself), with Crit covering the browser slot plus the running app and forge sync, Kiln is where the team's ratings become the eval set, Verbatim Citation Gate checks the citations in their answers, FrontierHarness prices the harness choice itself, HarnessTax cross-examines that price with academic independence, ReviewBench prices the reviewer choice the same way with the vendor-conflict caveat attached, and the maturity row says a realistic stack starts with the mature columns and adds the rest as the workflow demands.
Machine review of the pull requests themselves now lives in the [Code Review Feature Matrix](../../code-review/code-review-feature-matrix/index.md).

The surfaced long tail stays in prose until something clears the bar, and the 2026-10-12 resolutions both stay out: vostride/agent-qa (904 stars as of 2026-10-12) is held on dormancy, last push 2026-08-03, no releases ever, an undetected license (fair-source by topic), and no independent discussion of its self-improving QA-agent mechanism, with admission unblocking on any push or release after 2026-08-03; px0-ai/px0 (1,851 stars as of 2026-10-12, MIT, active, a browser IDE for reviewing AI-generated code with harness handoff) judges nothing and is an environment rather than an evaluation instrument, so it resolves as surfaces-kind alongside that category's editors and review workspaces and is returned for routing there.
The 2026-10-13 resolution joins them: stanford-iris-lab/meta-harness (1,652 stars as of 2026-10-13, MIT, the code behind arXiv 2603.28052) is an outer-loop search over harness code for LLM applications, and it scores candidate harnesses only to pick the next one, so its subject is automated harness engineering rather than any judgment on agent output, which resolves it as harnesses-kind and returns it for routing there.

## Choosing from the matrix

- Want LLM behavior blocking merges in CI: deepeval.
- Want independent-ish cost and quality numbers before picking a harness: FrontierHarness Eval, vendor-run caveat attached.
- Want an independent second opinion on the harness-cost question: HarnessTax, the academic complement to FrontierHarness Eval.
- Want a shared yardstick for comparing AI code reviewers before picking one: ReviewBench, reading the publication-gate caveat first.
- Want MIT-licensed production tracing, evaluation, and prompt management in one platform: Langfuse, self-hosted or cloud, open-core edges and ClickHouse ownership accepted.
- Want production-grade tracing and evaluation under your own infrastructure: Phoenix, accepting ELv2.
- Want machine review of every pull request: the [Code Review Feature Matrix](../../code-review/code-review-feature-matrix/index.md), where OpenCodeReview moved.
- Want your annotations to steer a live agent session: Plannotator.
- Want browser line comments on plans, diffs, and the running app itself, with comments pushable to GitHub or GitLab: Crit.
- Want a fast, annotated human read of a full changeset in the terminal: Hunk, paired with a judging column since it decides nothing.
- Want the change drawn before you read the diff: PR Lens, accepting that the diagrams are interpretations, not verdicts.
- Want non-engineers building and rating the eval set in a GUI: Kiln, checking the fair-code desktop license first.
- Want fabricated RAG quotes rejected before any model call: Verbatim Citation Gate, copying the two-stage pattern even if you outgrow the four-star library.
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
- 2026-10-09 - Maturity cells refreshed: Langfuse to v4.55.0, Phoenix to v20.20.0, and the ReviewBench star count to 39 as of 2026-10-09; all other cells re-verified unchanged.
- 2026-10-10 - Maturity cells refreshed: Langfuse to v4.56.0, Hunk to 9.6k stars and nearly seven months, Jevals to its 20-day age, ReviewBench to 41 stars, and the HarnessTax thread as-of date; all other cells re-verified unchanged.
- 2026-10-10 - Extended from ten to eleven columns with Kiln, the desktop eval workbench whose GUI ratings seed the judge metrics, sorted between Jevals and Langfuse, with the intro, who-judges line, judge-row sentence, CI-gating line, redundancy paragraph, and choosing list brought along.
- 2026-10-10 - Extended from eleven to twelve columns with PR Lens, the PR walkthrough visualizer that judges nothing, sorted between Plannotator and ReviewBench, with the intro, who-judges line, CI-gating line, judge-row sentence, redundancy paragraph, and choosing list brought along.
- 2026-10-10 - Extended from twelve to thirteen columns with Verbatim Citation Gate, the deterministic citation-fabrication gate ahead of an any-model judge, sorted between ReviewBench and Workshop, with the intro, who-judges line, judge-row sentence, redundancy paragraph, and choosing list brought along.
- 2026-10-11 - Maturity cells refreshed: ReviewBench to 42 stars, Jevals to its 21-day age and 103 stars, and the HarnessTax, Hunk, Kiln, PR Lens, and Verbatim Citation Gate as-of dates; all other cells re-verified unchanged.
- 2026-10-12 - Extended from thirteen to fourteen columns with Crit, the browser review surface covering plans, branch diffs, running apps, and static HTML, sorted before deepeval as the first column, with the intro, who-judges line, CI-gating line, judge-row sentence, redundancy paragraph, and choosing list brought along.
- 2026-10-12 - Opened the long tail with the 2026-10-12 resolutions: agent-qa held on dormancy (last push 2026-08-03, no releases, admission unblocks on any push or release after that date) and px0 judged surfaces-kind and returned for routing.
- 2026-10-13 - Maturity cells refreshed: Langfuse to v4.57.0 and Phoenix to v20.21 after new releases; the pending meta-harness candidate resolved in the long tail as harnesses-kind and returned for routing; the agent-qa dormancy hold re-verified untriggered (still last push 2026-08-03, no releases); all other cells re-verified unchanged.
- 2026-10-13 - Extended from fourteen to fifteen columns with Better Harness (Qoder's workflow-level harness-engineering platform), inserted in sorted position first, all ten cells traced to the new note, intro updated.
- 2026-10-13 - Maturity cells refreshed: Langfuse to v4.58.0, Crit to 1,209 stars, Hunk to the v0.24 beta line, Jevals to 105 stars, ReviewBench to 52 stars, and the Kiln and PR Lens as-of dates; all other cells re-verified unchanged.

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
- https://github.com/Kiln-AI/Kiln - the Kiln column: repository, license split, desktop surfaces (as of 2026-10-11)
- https://kiln.tech/pricing - the Kiln column: Individual, Team, and Enterprise tiers
- https://docs.kiln.tech/docs/evaluations - the Kiln column: judge types and the Eval Builder
- https://github.com/coldteadotai/pr-lens - the PR Lens column: repository, surfaces, license (as of 2026-10-11)
- https://prlens.dev - the PR Lens column: the worked example and canvas
- https://github.com/tonydzi/verbatim-citation-gate - the Verbatim Citation Gate column: repository, two-stage design, license (as of 2026-10-11)
