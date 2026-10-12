---
title: Dexter
created: 2026-10-10
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, autonomous-agent, financial-research, open-source]
readability: 3
audience_notes: >
  Engineers exploring agentic research loops over domain data and developers studying self-validating tool agents.
  Assumes you know what an income statement and a tool-calling agent are.
---

Dexter is Virattt's open-source autonomous financial research agent that turns a financial question into a planned tool-running investigation over live market data, checks its own work, and logs every step to an inspectable scratchpad.

**Dexter is this category's first member aimed at finance rather than mathematics, proofs, or papers: its loop plans, gathers, and re-checks its own analysis against live income statements and balance sheets, and its judge is an LLM-as-judge eval suite plus the human reading the answer, the no-kernel position with a paid data terminal instead of citations.**

## What it is

A TypeScript agent built on the Bun runtime, whose README pitches it as "Claude Code, but built specifically for financial research".
The agent decomposes a question into structured research steps, selects and executes the right tools, and self-validates until it has a data-backed answer, with loop detection and step limits against runaway runs.
Data comes from the Financial Datasets API (income statements, balance sheets, cash-flow statements), with optional Exa or Tavily web search.
Models are OpenAI by default, with Anthropic, Google, xAI, OpenRouter, or local Ollama as alternatives.
Surfaces are the interactive CLI (`bun start`), a watch mode, and a WhatsApp gateway that links your phone so you chat questions to the agent.
Every run lands in a JSONL scratchpad (`.dexter/scratchpad/`) recording the query, each tool call with its arguments and result, and the agent's reasoning steps.

## Status

Active: 27,652 stars, 3,410 forks, created 2025-10-14, last push 2026-09-23, latest release v1.1.0 the same day, as of 2026-10-11.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=virattt/dexter&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=virattt/dexter&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=virattt/dexter&type=date&legend=top-left" />
</picture>

**The discussion footprint is nearly absent for a 27.6k-star repository: a Hacker News search returns two stories at one point each with zero comments as of 2026-10-10, so the stars measure feed attention rather than recorded engineering debate, and the eval accuracy numbers are the project's own LLM-as-judge output.**

## Strengths

- The artifact chain is inspectable: every tool call and reasoning step lands in a per-run JSONL scratchpad, so a run's data trail can be audited after the fact.
- An eval suite exists: a financial-question dataset scored by LLM-as-judge with LangSmith tracking, which is more measurement than most research-agent demos ship.
- Safety features are built in: loop detection and step limits bound a runaway agent.
- The model layer is swappable, including fully local inference through Ollama.

## Cautions

- No machine judge stands behind the numbers: LLM-as-judge scores the agent's own answers, and no independent benchmark or replication surfaced in this run's searches.
- The README's disclaimer restricts the project to educational and informational use and warns outputs may be incorrect or out of date.
- The README claims an MIT license, but the repository carries no license file (GitHub detects none), the same unclear legal ground as Karpathy Autoresearch.
- The loop runs on paid terminals: an OpenAI (or equivalent) key plus a Financial Datasets API key are required, with Exa optional.
- 27.6k stars against two zero-comment Hacker News stories says the audience watches rather than debates.

## Pricing

Free; the project has no paid tier of its own, so pricing does not apply.
Costs are your own API keys: OpenAI or an alternative model provider, the Financial Datasets data key, and optionally Exa or Tavily for search.

## Compared to

- [GPT Researcher](../gpt-researcher/index.md): the general cited-report baseline; Dexter is domain-bound to financial data and grounds claims in fetched statements rather than web citations.
- [DeepAnalyze](../deepanalyze/index.md): the trained 8B data-science model running its own loop; Dexter is prompted tool use over commercial financial APIs.
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the keep-or-revert ancestor whose judge is a measured loss; Dexter's judge is a model reading its own answers.

## Bottom line

**Recommended for engineers studying self-validating tool agents on domain data and for building financial research pipelines where the scratchpad audit trail matters more than verified correctness.**
Not for investment decisions, and not for anyone who needs a licensed repository or an independently evaluated judge.

## Changes

- 2026-10-10 - Created.

## See also

- [GPT Researcher](../gpt-researcher/index.md) - the general web-research loop Dexter specializes to finance
- [DeepAnalyze](../deepanalyze/index.md) - the trained-model data-analysis sibling
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the founding loop with the measured judge
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/virattt/dexter - repository, README: overview, capabilities, disclaimer, prerequisites, eval suite, WhatsApp gateway, and the MIT license claim (fetched 200, 2026-10-10)
- https://api.github.com/repos/virattt/dexter - stars, forks, created and pushed dates, TypeScript language, and the null detected license for the as-of status (fetched 200, 2026-10-11)
- https://raw.githubusercontent.com/virattt/dexter/main/README.md - the README source: tool surface, model and data keys, scratchpad layout, and eval runner (fetched 200, 2026-10-10)
- https://api.github.com/repos/virattt/dexter/releases?per_page=5 - the release train through v1.1.0 (2026-09-23) (fetched 200, 2026-10-10)
- https://hn.algolia.com/api/v1/search?query=Dexter%20financial&tags=story - the two one-point, zero-comment Hacker News stories behind the discussion-footprint claim (fetched 200, 2026-10-10)
- https://raw.githubusercontent.com/virattt/dexter/main/LICENSE - the missing license file behind the README's MIT claim (fetched 404, 2026-10-10)
