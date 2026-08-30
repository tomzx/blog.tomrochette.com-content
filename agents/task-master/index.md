---
title: Task Master
created: 2026-08-27
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, task-management, task-tracking, mcp]
readability: 3
audience_notes: >
  Engineers who used claude-task-master in 2025 or are choosing a PRD-to-tasks pipeline now and need to know what the Hamster deal changed.
  Assumes you know what an MCP server is and what a Commons Clause does to "open source".
---

Task Master (repo claude-task-master, package `task-master-ai`) is Eyal Toledano's AI task-management system that parses a PRD into dependency-chained tasks and drives agents through them; it became the engine of Hamster's commercial product in 2026 and its open-source repo has been quiet since April.
Facts below verified as of 2026-08-30.

**The most-installed task manager of the agent era chose productization over community, and its quiet repository is what a successful OSS-to-commercial handoff looks like from the outside: founders win, users keep the old binary, and the license quietly stops being open source.**

## What it is

An MCP server plus CLI that turns a product requirements document into tasks with dependencies, complexity analysis, and expansion commands (`parse-prd`, `expand`, `next`), designed to slot into Cursor, Claude Code, Windsurf, and any MCP-speaking client.
The method is PRD-first: write the document, let the system decompose it, then feed agents one dependency-ready task at a time.
Since the commercialization it is also "Taskmaster", a [Hamster](https://tryhamster.com/product/taskmaster) product (Wheel Go Fast, Inc., with Ralph Khreish), documented at [docs.task-master.dev](https://docs.task-master.dev/) and tryhamster.com.

## Status

Open-source repo quiet, commercial product alive, usage still enormous.
As of 2026-08-30: 28,037 stars and 2,628 forks (the largest raw numbers in this category), but the last push landed 2026-04-28 and the last release (0.43.1) on 2026-03-31, while npm still records 80,001 downloads last month.
The [LICENSE](https://github.com/eyaltoledano/claude-task-master/blob/main/LICENSE) is now MIT with a Commons Clause Condition v1.0 covering the whole repo and package, which prohibits selling the software and makes it non-OSI.
Development energy has visibly moved to Hamster, whose pricing sells the method as a product.

## Strengths

- The PRD-to-dependency-graph pipeline remains the most complete implementation of document-first task generation.
- Two years of community content, tutorials, and integrations exist for it, more than every rival here combined.
- MCP-native, so it drops into any modern client without glue.
- The commercial successor means the method has funding and a roadmap, unlike orphaned rivals.

## Cautions

- The open-source repo has been untouched for four months; bugs you file there are not the company's queue.
- Commons Clause means it is source-available, not open source; corporate policy reviews will notice.
- Your task graph now follows Hamster's product decisions, a lock-in beads and Backlog.md do not have.
- The free tier's terms (1 creator, 10 briefs) tell you where the paid wall sits.

## Pricing

The CLI and MCP server: free under Commons Clause terms.
Hamster the product: Free (1 creator, 10 briefs), Team at $40 per creator per month with unlimited briefs, Enterprise at $200 per creator per month with SSO and SOC 2, as of 2026-08-30.

## Compared to

- [beads](../beads/index.md): graph tracker, true MIT, no vendor; choose it when the method must outlive any company.
- [Backlog.md](../backlog-md/index.md): markdown-native with human review gates; choose it when oversight beats pipeline automation.
- [GitHub Spec Kit](../spec-kit/index.md): process templates with no runtime to buy; choose it when the spec, not the tracker, is the product.

## Bottom line

**Recommended if you are already on Task Master and happy: the binary works and npm still installs it.**
I would not standardize new work on the Commons-Clause repo while its future is a commercial product's roadmap.
For new setups, the choice is beads for multi-agent state or Backlog.md for human review, and this note exists partly as the cautionary record of the third path.

## See also

- [beads](../beads/index.md) - the MIT counterpoint with no vendor
- [Backlog.md](../backlog-md/index.md) - the review-gate counterpoint
- [GitHub Spec Kit](../spec-kit/index.md) - the spec-first layer, still vendor-neutral
- [Continue](../continue/index.md) - the other 2026 open-source-to-commercial exit this section tracks

## References

- https://github.com/eyaltoledano/claude-task-master - README and the Hamster product links
- https://api.github.com/repos/eyaltoledano/claude-task-master - stars, forks, quiet push dates as of 2026-08-30
- https://github.com/eyaltoledano/claude-task-master/releases - v0.43.1, 2026-03-31, the last release
- https://github.com/eyaltoledano/claude-task-master/blob/main/LICENSE - MIT with Commons Clause Condition v1.0
- https://tryhamster.com/pricing - Hamster Free and Team tiers as of 2026-08-30
- https://docs.task-master.dev/ - the documentation, still live
- https://api.npmjs.org/downloads/point/last-month/task-master-ai - 80,001 downloads last month
