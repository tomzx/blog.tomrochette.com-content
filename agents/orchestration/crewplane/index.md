---
title: Crewplane
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, orchestration, workflows, cli, markdown]
readability: 3
audience_notes: >
  Engineers who want their agent process versioned in the repository and auditable on disk.
  Assumes you already run at least one agent CLI and are comfortable editing Markdown and YAML front matter.
---

Crewplane is an Apache-2.0, CLI-first orchestrator that turns coding-agent CLI calls into structured, resumable Markdown workflows and keeps every run record on disk.

**Crewplane's bet is that the agent workflow, not the agent session, should be the durable artifact: define the stages in Markdown, run each stage through whichever CLI fits, and keep rendered inputs, outputs, logs, and final results as inspectable build outputs.**

## What it is

A Python 3.13+ tool (installed with `uv tool install crewplane`, pip, or npm) from crewplaneai that runs a workflow DAG described in Markdown plus YAML front matter.
Each node names a provider, so one workflow can hand off across Claude Code, Codex, Gemini CLI, GitHub Copilot CLI, Kilo Code, Pi, DeepSeek Harness, OpenCode, or any other command, and nodes run sequentially or in parallel with explicit stage artifacts between them.
Crewplane invokes provider CLIs directly rather than wrapping a vendor SDK, and it neither installs nor manages those CLIs or their credentials.
A run writes a full record under `.crewplane/`: rendered inputs, per-stage outputs and logs, manifests, and final results, so a failed later stage can resume from validated boundaries instead of replaying everything.
Optional features include a tmux dashboard, Git-backed workspace isolation, review loops with findings artifacts, and reusable workflow composition; a companion crewplane-lab publishes reproducible multi-agent experiments with the workflow, responses, telemetry, and logs.

## Status

Very early but shipping: about 41 stars and 6 forks as of 2026-10-06, created 2026-06-24, and active development through v0.3.6 on 2026-10-05 (bug-fix and change-review example workflows, review loops resuming from completed phase checkpoints) with default-branch commits through October 5.

<a href="https://www.star-history.com/?repos=crewplaneai%2Fcrewplane&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=crewplaneai/crewplane&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=crewplaneai/crewplane&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=crewplaneai/crewplane&type=date&legend=top-left" />
 </picture>
</a>

The repository is Python, passes an OpenSSF Best Practices badge, and documents an install-to-inspect path that runs a mock invoker before any real provider call.
**At roughly three months old and 41 stars, Crewplane is a cohort-of-one tool from a single vendor; its value depends on whether the Markdown-as-workflow idea outlives the project.**

## Strengths

- The whole process is versioned in the repo, which makes agent work reviewable and diffable like any other code artifact.
- Provider-agnostic and CLI-first: if a tool has a command line, Crewplane can sequence it, with no SDK lock-in.
- Resumable at validated stage boundaries, and idempotent by default (an identical rerun reuses the saved result unless `--force`).
- Every run leaves an inspectable record on disk, addressing the terminal-scrollback problem that makes multi-stage agent work hard to audit.
- A safe first run with a mock invoker, so you can validate a workflow without spending tokens.

## Cautions

- 41 stars, pre-1.0, and a single vendor; bus factor is the main risk.
- No GUI: the tmux dashboard is optional and the primary surface is the terminal.
- You install and authenticate every provider CLI yourself; Crewplane does not manage credentials or models.
- Run artifacts behave like build output, so deciding what belongs in version control is left to you.
- The per-node `cwd` defaults to the project root; worktree isolation is opt-in, so careless workflows can edit your working tree.

## Pricing

Free and open source under Apache-2.0.
No hosted tier and no per-token fee; you pay only for the provider CLIs you route stages through.

## Compared to

- [Sandcastle](../sandcastle/index.md): a TypeScript library with sandbox providers; choose Crewplane when the workflow should live in Markdown and survive failures on disk rather than in a process.
- [LoopTroop](../looptroop/index.md): a local GUI that also decomposes work into stages; choose Crewplane when you want CLI-first, repo-owned workflows instead of a council-planning GUI.
- A hand-rolled shell script plus CI: the zero-dependency option; Crewplane earns its keep once stages need provider handoffs, resumability, and an auditable record.

## Bottom line

**Recommended for teams who want their coding-agent process expressed as versioned Markdown with resumable, inspectable runs across several CLIs.**
Not for anyone who wants a visual board, and not for shops that need a mature, multi-vendor-backed tool.

## Changes

- 2026-09-27 - Created.
- 2026-10-07 - Added the crewplaneai/crewplane star history chart to the Status section.

## See also

- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [Sandcastle](../sandcastle/index.md) - the TypeScript library counterpart
- [LoopTroop](../looptroop/index.md) - the GUI workflow orchestrator
- [The Perfect Orchestrator](../the-perfect-orchestrator/index.md) - the tmux, plain-file alternative
- [OpenCode](../../harnesses/opencode/index.md) - one of the CLIs Crewplane can route stages through

## References

- https://github.com/crewplaneai/crewplane - repository, architecture, workflow syntax, license, stars, and release data
- https://raw.githubusercontent.com/crewplaneai/crewplane/master/docs/index.md - documentation map, first-project path, and the mock-validation flow
- https://github.com/crewplaneai/crewplane-lab - reproducible multi-agent comparison with workflow, responses, telemetry, and logs
- https://openorchestrators.org/players/crewplane/ - the curated directory's profile of Crewplane
- https://pypi.org/project/crewplane/ - package description and install surface
