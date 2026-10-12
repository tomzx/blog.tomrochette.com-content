---
title: CORAL
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, multi-agent, evolution, self-evolving, open-source]
readability: 3
audience_notes: >
  Engineers running coding agents against graders and comparing multi-agent evolution designs.
  Assumes you know what a git worktree and an evaluation grader are.
---

CORAL is the Human-Agent Society team's Apache-2.0 framework for multi-agent self-evolution on a codebase: a manager partitions coding agents into isolated git-worktree islands, a grader daemon scores every committed attempt, and what works is shared through persistent memory, accepted at COLM 2026.

**It is the first column in this category whose loop is an agent organization rather than a single agent or pipeline, and the only one that treats guarding the judge from the judged as a design constraint: grader state lives under .coral/private and the June 2026 release sandboxed agents so they cannot read the answer key, even through Bash.**

## What it is

A Python package installed via a curl script or uv (`coral` CLI, v0.7.21) from the April 2026 paper "CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery" (arXiv 2604.01658, Ao Qu, Han Zheng, and fifteen-plus coauthors).
Give it a codebase, a grader, and a task.yaml: the manager creates one worktree per agent, agents commit experiments, the grader daemon scores them, and attempts, notes, and reusable skills move through .coral/public while hidden grader state sits in .coral/private.
It natively drives Claude Code, OpenCode, Codex, Cursor Agent, and Kiro.
v0.6.0 added multi-island runs with migration between islands, April 2026 added rubric LLM judges for open-ended tasks (reports, memos, legal analysis), and the paper adds heartbeat-based interventions, evaluator separation, and resource and health management, claiming state-of-the-art results on math, algorithmic, and systems optimization tasks.

## Status

Active through early September: 1,063 stars, 133 forks, created 2026-03-16, last pushed 2026-09-08, with releases v0.7.19 through v0.7.21 landing between August 20 and September 6, 2026, as of 2026-10-11.
No relevant Hacker News threads surfaced in this run's search; the footprint is GitHub-native plus the project's docs and blog site.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Human-Agent-Society/CORAL&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Human-Agent-Society/CORAL&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Human-Agent-Society/CORAL&type=date&legend=top-left" />
</picture>

## Strengths

- The judge-judged separation is engineered, not assumed: Docker isolation since June 2026 keeps agents from reading grader internals, the category's only explicit anti-contamination build.
- Islands with migration give the evolution a topology: isolated populations, scoped attempts, and controlled exchange, which no other column has.
- Rubric judges extend the grader model to open-ended tasks where no metric exists.
- A COLM 2026 acceptance plus a public paper give the mechanism a peer-reviewed anchor the newer Claude-Code-native loops lack.

## Cautions

- The last push was 2026-09-08 and the release train has paused since v0.7.21, about a month before this run; nothing alarming, but worth watching.
- The state-of-the-art claims are the paper's own evaluations on its chosen tasks; no independent replication surfaced in this run's searches.
- The loop's ceiling is your grader: rubric judges reintroduce LLM judgment wherever metrics stop, so the isolation guarantee protects the metric, not the rubric.
- Running an agent organization multiplies cost: one worktree, one agent session, and one grader invocation per island, paid in your coding-agent subscriptions.

## Pricing

Free and open source under Apache-2.0; there is no paid tier, so pricing does not apply.
Costs are the coding-agent subscriptions the agents run on (Claude Code, Codex, Cursor, Kiro, OpenCode) and your compute for grading.

## Compared to

- [Kapso](../kapso/index.md): the campaign framework with evidence-priced memory; CORAL adds the population layer (islands, migration, shared notes) Kapso's tree lacks, while Kapso adds cross-campaign learning CORAL's paper does not claim.
- [OpenResearch](../openresearch/index.md): the other worktree-native member; OpenResearch archives an evidence tree for human review, CORAL grades every commit automatically.
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the single-lineage keep-or-revert ancestor; CORAL is the many-agent, shared-memory generalization with a paper behind it.

## Bottom line

**Recommended for teams that already have a grader and want to run an evolving population of coding agents against it without the agents reading the answer key.**
Not for open-ended work without a rubric you trust, and not for anyone needing an active release train this month.

## Changes

- 2026-10-11 - Created.

## See also

- [Kapso](../kapso/index.md) - the campaign-and-memory member closest in mechanism
- [OpenResearch](../openresearch/index.md) - the other worktree-native loop
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the single-lineage ancestor CORAL generalizes
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/Human-Agent-Society/CORAL - repository, Apache-2.0, 1,063 stars, COLM 2026 news, last push 2026-09-08 (as of 2026-10-11)
- https://raw.githubusercontent.com/Human-Agent-Society/CORAL/main/README.md - grader-isolation news, multi-island v0.6.0, rubric judges, supported agents, paper link (fetched 200, 2026-10-11)
- https://coral.compounding-intelligence.ai/ - the loop diagram, the .coral/public and .coral/private layout, manager and grader daemon architecture, example domains (fetched 200, 2026-10-11)
- https://arxiv.org/abs/2604.01658 - the paper: authors, autonomous multi-agent evolution framing, heartbeat interventions, evaluator separation (fetched 200 via the arXiv API, 2026-10-11)
- https://api.github.com/repos/Human-Agent-Society/CORAL/releases?per_page=3 - the v0.7.19 through v0.7.21 release dates (fetched 200, 2026-10-11)
- https://hn.algolia.com/api/v1/search?query=CORAL%20agents%20evolution - the search returning no relevant threads (fetched 200, 2026-10-11)
