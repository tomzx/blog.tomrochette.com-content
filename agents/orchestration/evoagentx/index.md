---
title: EvoAgentX
created: 2026-10-10
updated: 2026-10-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, python, self-evolving, workflow-optimization]
readability: 3
audience_notes: >
  Engineers and researchers choosing a multi-agent workflow framework who care about whether the framework improves its own workflows.
  Assumes you know what a workflow graph and a prompt optimizer are.
---

EvoAgentX is a research team's MIT Python framework that generates multi-agent workflows from a natural-language goal and then evolves them with published optimization algorithms: TextGrad, AFlow, MIPRO, and EvoPrompt.

**Its bet is that workflow quality is an optimization problem: prompts, tool configurations, and workflow topology are the search space, which makes it the one column in this category whose orchestration is itself under optimization rather than fixed at design time.**

## What it is

A five-layer platform (basic components, agent, workflow, evolving, evaluation) per the July 2025 arXiv paper: a `WorkFlowGenerator` turns a goal into a structured workflow graph, an `AgentManager` instantiates the agents, and a `WorkFlow` executes the graph, while the evolving layer iteratively refines prompts, tool configurations, and topology against a dataset and metric.
It ships toolkits for code interpreters (Python, Docker), search, filesystem, databases, image analysis, browser automation, and MCP tools, plus memory modules and human-in-the-loop interceptors that pause a workflow for approval or input as first-class workflow nodes.
Models connect through OpenAI, Qwen, LiteLLM, SiliconFlow, and OpenRouter, covering Claude, DeepSeek, and Kimi alongside the native providers.
MIT per the LICENSE file (GitHub's license detection reports NOASSERTION), by Yingxu Wang, Siwei Liu, Jinyuan Fang, and Zaiqiao Meng of Glasgow, with the repository since moved from the EvoAgentX org to ANative-Lab (the paper's and README's old links redirect).

## Status

Active but quiet: 3,370 stars and 315 forks as of 2026-10-10 on a repository created 2025-04-15, with the release train stopped at v0.1.4 (2026-06-28) and the default branch silent from 2026-08-27 until a three-commit maintenance return on 2026-10-22 (pytest fixes and new evolution examples), while the community talk series kept running through June 2026 (GitHub API, as of 2026-10-27).
The framework paper (arXiv 2507.03616, July 2025, revised September) and the team's self-evolving-agents survey (arXiv 2508.07407, August 2025) are the grounding publications.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ANative-Lab/EvoAgentX&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ANative-Lab/EvoAgentX&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ANative-Lab/EvoAgentX&type=date&legend=top-left" />
</picture>

**The evaluation record is self-published and small: the headline gains (a 7.44 percent HotPotQA F1 rise, 10 percent on MBPP pass@1 and MATH, up to 20 percent on GAIA) rest on 50 validation and 100 test examples, and the project's entire Hacker News presence is self-posted stories that never cleared 5 points.**

## Strengths

- The evolution engine is the differentiator: four published optimizers over prompts and graph topology with the benchmark harnesses (HotPotQA, MBPP, MATH) already wired in, which no other framework column here ships as the core.
- Auto-construction lowers the floor: a goal in, a workflow graph out, then optimization against your own dataset.
- HITL interceptors and approval gates are workflow nodes, so human oversight survives the optimization loop.
- The team's survey of self-evolving agents is a real map of the field the framework sits in, rare grounding for a repo in this category.

## Cautions

- Six weeks without a push as of this check, and both the README's links and the paper's code URL still point at the pre-move EvoAgentX org, a maintenance smell.
- The results tables are self-measured on tiny samples with no independent reproduction in the sources.
- Research-first abstractions in the CAMEL mold: Python workflows over LLM APIs, with nothing for coding sessions, worktrees, or review, so it serves this category's framework wing, not its parallel-agent core.

## Pricing

Free and open source under MIT.
Your model API bills are the only cost; optimization multiplies them, since each evolution round re-runs the workflow against the validation set.

## Compared to

- [CAMEL](../camel/index.md): the role-playing research lineage; choose CAMEL to study agent societies, EvoAgentX to optimize a workflow against a metric.
- [LangGraph](../langgraph/index.md): the production graph runtime with durable execution; choose LangGraph to ship, EvoAgentX to search the workflow design space before you do.
- [Raven](../raven/index.md): the DAG host whose Evolver evaluates candidate harness changes; the adjacent instinct pointed at a different object, Raven's own harness versus your workflow.

## Bottom line

**Recommended for researchers and workflow engineers who have a dataset, a metric, and tolerance for a quiet repository, and want automated prompt and topology search instead of hand-tuning.**
Not for coding-session orchestration, and not for anyone who needs an actively shipping dependency today.
My disagreeable claim: **the framework family's next differentiator is not another agent abstraction but the optimizer loop, and EvoAgentX is the only column already shipping it as the product's core rather than a side tool.**

## Changes

- 2026-10-10 - Created from the automated-research scan's referral of the project as orchestration-class.
- 2026-10-27 - Re-verified in rotation: all cited sources re-fetched and live (repo, README, license, both arXiv papers, HN search); no claims changed, the 2026-10-22 maintenance return still the newest activity, and the category index one-liner corrected to match.

## See also

- [CAMEL](../camel/index.md) - the other research-first framework column in the family
- [LangGraph](../langgraph/index.md) - the production graph runtime this category builds on
- [Raven](../raven/index.md) - the DAG-planning host with the adjacent self-evolution instinct
- [Orchestration Feature Matrix](../orchestration-feature-matrix/index.md) - the category comparison this note joins
- [The Agentic Development Environment Landscape](../../the-agentic-development-environment-landscape/index.md) - the tracker this category extends

## References

- https://api.github.com/repos/ANative-Lab/EvoAgentX - stars, forks, dates, language, and the NOASSERTION license detection, as of 2026-10-10
- https://raw.githubusercontent.com/ANative-Lab/EvoAgentX/main/README.md - the workflow generation model, evolution algorithms, tools, HITL, and self-reported results
- https://raw.githubusercontent.com/ANative-Lab/EvoAgentX/main/LICENSE - the MIT grant plus the AFlow and LiveCodeBench third-party notices
- https://arxiv.org/abs/2507.03616 - the framework paper's five-layer architecture, integrated optimizers, and benchmark claims
- https://arxiv.org/abs/2508.07407 - the team's survey grounding the self-evolving-agents field the framework sits in
- https://hn.algolia.com/api/v1/search?query=EvoAgentX&hitsPerPage=5 - the self-posted-only HN footprint, queried 2026-10-10
