---
title: AI Dev Tasks
created: 2026-10-08
updated: 2026-10-08
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, task-management, prd, prompt-pack, open-source, dormant]
readability: 3
audience_notes: >
  Engineers who met the PRD-to-task-list workflow in 2025 tutorials and want to know what it was and why the repository went quiet.
  Assumes you know what Task Master is and what a product requirements document looks like.
---

AI Dev Tasks is two Apache-2.0 markdown prompt files, `create-prd.md` and `generate-tasks.md`, that turn a feature idea into a product requirements document and the PRD into a checkbox task list an AI coding assistant works through one sub-task at a time; it was the most-starred artifact of the 2025 PRD-workflow wave and its repository has been dormant since November 2025.

**The most-starred task system of that wave was two prompt files with no state layer, and the dormancy is the market's verdict on tracking agent work in a generated checklist instead of a tool.**

## What it is

A repository holding two markdown rule files rather than software: `create-prd.md` (81 lines) makes the assistant ask three to five clarifying questions and draft a PRD, and `generate-tasks.md` (70 lines) turns the PRD into `tasks/[feature].md` with numbered parent tasks, sub-tasks, a Relevant Files section, a mandatory task 0.0 create-feature-branch, and a hard pause for the user's "Go" before sub-tasks are generated.
There is no CLI, no MCP server, no database, and no runtime state: the generated checklist is the tracker, and its checkboxes are the only record of progress.
The workflow runs in any AI IDE or CLI that can read a file (the README names Amp, Claude Code, and Windsurf alongside its Cursor origins), and the 1,708 forks show it was personalized everywhere.
It is maintained by the snarktank identity under Apache-2.0, with 65 commits in the repository's life.

## Status

Dormant.
As of 2026-10-08: 7,798 stars, 1,708 forks, 218 watchers, 3 open issues, 7 open pull requests, created 2025-04-19, last push 2025-11-05, no release ever published, Apache-2.0 throughout.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=snarktank/ai-dev-tasks&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=snarktank/ai-dev-tasks&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=snarktank/ai-dev-tasks&type=date&legend=top-left" />
</picture>

The repository's own About links its widest exposure, a demonstration on Claire Vo's [How I AI podcast](https://www.youtube.com/watch?v=fD4ktSkNCw4), and 2025 coverage ran through tutorials and video rather than Hacker News (an HN story search for the project returns zero hits as of 2026-10-08).
There is no deprecation notice or handoff: the repository simply stopped.

## Strengths

- Nothing to install: two files, any assistant, and the workflow teaches itself from the README.
- The confirmation gates (bounded clarifying questions, the "Go" pause between parent tasks and sub-tasks) are human-oversight design that predates this section's whole category.
- Task 0.0 branching and the Relevant Files sections anticipate what Task Master and spec-kit later built tooling around.
- Apache-2.0 and two files long, so every team can carry a tuned copy, which is what the fork count shows happened.

## Cautions

- There is no state layer: nothing serializes two agents on one list, survives a context reset, or answers "what is unblocked", so it is a to-do file, not a tracker.
- Dormant for eleven months with seven pull requests unmerged; any fix you need is yours to make.
- The structure lives or dies on the model following the prompt, and weaker models drop the format, which is why the community forks grew tool-specific setup instructions.
- What succeeded it is in this category: Task Master runs the same PRD-first idea as a stateful MCP server and CLI, and Backlog.md gates human review around authored task files.

## Pricing

Free and open source under Apache-2.0.
No paid tier, service, or account exists.

## Compared to

- [Task Master](../task-master/index.md): the same PRD-to-tasks pipeline with dependency state, an MCP server, and a commercial successor; choose it when the task list must be queryable state, accept that its repository is a Commons-Clause quiet one.
- [Backlog.md](../backlog-md/index.md): a tracker instead of a generator; tasks are authored and reviewed as files, not produced from a PRD, and the three review gates replace the "Go" prompt.
- [GitHub Spec Kit](../../spec-driven-development/spec-kit/index.md): versioned process templates for the same document-first loop without a task-list runtime; choose it when the spec is the product.

## Bottom line

**Recommended as the historical baseline of the PRD pipeline and a zero-dependency starter, not as a system to standardize on in 2026.**
Not for multi-agent work, long-horizon tracking, or anyone who needs the method maintained.
My disagreeable claim: ai-dev-tasks was never a tool at all, and its 7.8k stars measure how much structure 2025 wanted, not what it got.

## Changes

- 2026-10-08 - Created after the entrant sweep surfaced the dormant prompt-file original of the PRD pipeline this category tracks.

## See also

- [Task Master](../task-master/index.md) - the stateful, commercialized descendant of the same pipeline idea
- [Backlog.md](../backlog-md/index.md) - the markdown tracker where review replaces generation
- [GitHub Spec Kit](../../spec-driven-development/spec-kit/index.md) - the spec-first process layer that kept the documents and dropped the checklist
- [Ordewell](../ordewell/index.md) - the planner that interrogates the goal conversationally instead of from a written PRD

## References

- https://github.com/snarktank/ai-dev-tasks - repository: README, the two prompt files, scale, the About link to the podcast demonstration (fetched 2026-10-08)
- https://api.github.com/repos/snarktank/ai-dev-tasks - stars, forks, dates, license, push date as of 2026-10-08
- https://raw.githubusercontent.com/snarktank/ai-dev-tasks/main/README.md - the five-step workflow and the How I AI demonstration link
- https://raw.githubusercontent.com/snarktank/ai-dev-tasks/main/generate-tasks.md - parent tasks, sub-tasks, task 0.0, and the /tasks/ output contract
- https://www.youtube.com/watch?v=fD4ktSkNCw4 - the How I AI demonstration (consent shell on fetch 2026-10-08; the claim is grounded in the repository's own README link)
- https://hn.algolia.com/api/v1/search?query=%22ai-dev-tasks%22&tags=story - zero story hits as of 2026-10-08, the missing HN footprint
