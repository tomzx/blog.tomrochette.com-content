---
title: Kapso
created: 2026-10-11
updated: 2026-10-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, optimization, program-synthesis, self-improving]
readability: 3
audience_notes: >
  Engineers running long optimization campaigns over ML and data systems, and researchers comparing experience-learning loops against one-shot pipelines.
  Assumes you know what an evaluation harness and a leaderboard are.
---

Kapso is Leeroo's MIT-licensed framework of long-running agents that run optimization campaigns over AI and data systems, turning a stated objective and an evaluator into a tree of coding-agent experiments whose lessons are distilled into a knowledge hub for the next campaign.

**Kapso is this category's first member whose unit of work is the campaign rather than the paper or the answer: the loop is judged by evaluator outcomes at every step, its memory is evidence-priced (a lesson stays trusted only as long as it keeps holding up), and its headline results sit on leaderboards, two of which the project runs itself.**

## What it is

A Python package (`pip install leeroo-kapso`, Python 3.10+, created 2025-12-07) by Leeroo, a YC X25 company.
It runs its inference through coding-agent CLIs with no direct-API fallback: Claude Code for ideation and implementation, Codex for research and judging, with an optional OpenAI key only for embeddings.
Four documented pillars: `.evolve()` runs tree-searched experiments toward the objective, `.learn()` and `.learn_knowledge()` mine finished campaigns and outside repositories into knowledge cards, `.research()` does web research for ideas and references, and `.deploy()` ships the result to local, Docker, or Modal infrastructure.
The technical report (arXiv 2601.21526, January 2026, by Alireza Nadafian, Alireza Mohammadshahi, and Majid Yazdani) describes a git-native experimentation engine where every attempt is a branch, a knowledge system over repositories and papers, and a cognitive memory layer distilling lessons from run logs, diffs, and evaluator feedback.
Leeroopedia, the project's hosted ML knowledge wiki, connects as an MCP server during campaigns.

## Status

Active and accelerating: 123 stars, 15 forks, created 2025-12-07, last pushed 2026-10-12, with six releases on October 11 alone taking the train from v0.6.3 to v0.7.5 (the October 12 pushes are Leeroopedia documentation commits), as of 2026-10-13.
The v0.7.0 release added cost-aware candidate selection, an estimator prices each finalized candidate before it runs, refusals and measured costs are recorded as campaign events, and the campaign stops when the next estimate would exhaust its budget, plus a `vertex_claude_code` agent that drives Claude Code on Vertex AI open-weight models; the checkpoint schema moved to version 3, so campaigns started before 0.7.0 cannot resume.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Leeroo-AI/kapso&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Leeroo-AI/kapso&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Leeroo-AI/kapso&type=date&legend=top-left" />
</picture>

The claimed results are concrete: #1 open-source on MLE-Bench, top ranking on ALE-Bench (1909 Elo against ALE Agent's 1879), RelBench wins over KumoRFM-v2 on Stanford's official leaderboard, and the IOAI 2026 AI Model Track, where the project reports a 536.07 total above all 471 human contestants and a Grand Master Trophy among the 14 founding AI participants, with IOAI's own account of the inaugural track published September 29, 2026.
**The community footprint is nearly absent: a Hacker News search for the project returns zero stories as of 2026-10-11, the 123 stars are small for the claims, and the PyPI package named `kapso` is an unrelated WhatsApp tool that shadows this one in installs, a collision the README itself warns about.**

## Strengths

- The judge is declared with the objective: every campaign carries its own evaluator, so progress is measured rather than self-declared, the Karpathy keep-or-revert property generalized to arbitrary ML and data objectives.
- The learning layer is the differentiator: lessons carry the evidence that earned them and expire when they stop holding, and outside repositories and papers fold into the same knowledge graph.
- Third-party anchoring where it exists: the RelBench results sit on Stanford's official leaderboard, and IOAI's organizers published their own review of the track the IOAI result comes from.
- It ships as a library rather than a demo: a PyPI package, documented pillars, and agent skill files for Claude Code, Codex, and OpenCode.

## Cautions

- The benchmark headline claims are self-run: the MLE-Bench and ALE-Bench numbers live in the project's own benchmark directories, and Stanford's RelBench leaderboard page states plainly that it holds self-reported results submitted in good faith, pointing to RelArena for controlled evaluation.
- 121 stars, zero Hacker News stories, and no independent replication surfaced in this run's searches, a thin footprint for results this strong.
- The loop rides on paid coding-agent subscriptions (Claude Code and Codex logins are required before anything works), and Leeroopedia adds a hosted-service account and prepaid credits to the dependency list.
- The name collision is genuine adoption friction: the unrelated `kapso` WhatsApp package on PyPI shadows this one, and every Hacker News hit for the name is the other company.
- The IOAI totals come from the company's own benchmark writeup, with IOAI's account of the track but no independent audit of the scores.

## Pricing

Free and open source under MIT; there is no paid tier, so pricing does not apply.
Costs are the coding-agent subscriptions the CLIs require (Claude Code, Codex), your compute, and an optional Leeroopedia account whose new accounts come with $20 of credit.

## Compared to

- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the keep-or-revert ancestor with one fixed metric; Kapso generalizes the measured-judge idea to campaign objectives and adds memory across campaigns.
- [ARIS](../aris/index.md): the markdown-skill ML research loop with cross-model review; Kapso is a Python framework with tree search and a knowledge graph instead of skills files.
- [DeepAnalyze](../deepanalyze/index.md): the trained 8B model carrying the data-science loop in its weights; Kapso orchestrates general coding agents and learns between runs.

## Bottom line

**Recommended for ML and data teams that want benchmark-scored optimization campaigns with a persistent, evidence-priced memory, and for researchers studying how loops learn across runs.**
Not for anyone needing independently audited headline numbers or a large user community, both absent as of 2026-10-12.

## Changes

- 2026-10-11 - Created.
- 2026-10-11 - Added the star history chart.
- 2026-10-12 - Recorded the October 11 release burst (v0.7.0 through v0.7.5): cost-aware candidate selection with budget caps and measured-cost ranking, the vertex_claude_code agent on Vertex AI open-weight models, and the schema-3 checkpoint break.
- 2026-10-13 - Harmonized the star count (the status line and the footprint line disagreed, 122 versus 121) to 123 as of 2026-10-13, and identified the October 12 pushes as Leeroopedia documentation commits.

## See also

- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the measured-judge ancestor Kapso generalizes into campaigns
- [ARIS](../aris/index.md) - the skills-based ML research loop in the same family
- [DeepAnalyze](../deepanalyze/index.md) - the trained-model data-science sibling
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/Leeroo-AI/kapso - repository, MIT license, benchmark claims, and release train (as of 2026-10-11)
- https://raw.githubusercontent.com/Leeroo-AI/kapso/main/README.md - the four pillars, CLI requirements, PyPI collision warning, and the IOAI and RelBench claims (fetched 200, 2026-10-11)
- https://arxiv.org/abs/2601.21526 - the technical report: git-native experimentation engine, knowledge system, and cognitive memory layer (fetched 200, 2026-10-11)
- https://pypi.org/pypi/leeroo-kapso/json - package version 0.7.5, MIT license, and Python requirement (fetched 200, 2026-10-12)
- https://ioai-official.org/what-happens-when-autonomous-ai-takes-on-the-same-tasks-as-the-worlds-top-young-ai-talents/ - IOAI's own account of the inaugural AI Model Track, September 29, 2026 (fetched 200, 2026-10-11)
- https://star-project.stanford.edu/relbench/leaderboard/ - the official RelBench leaderboard and its self-reported-results disclaimer (fetched 200, 2026-10-11)
- https://raw.githubusercontent.com/Leeroo-AI/kapso/main/benchmarks/ioai2026/README.md - the per-task IOAI numbers behind the 536.07 total and Grand Master Trophy (fetched 200, 2026-10-11)
- https://hn.algolia.com/api/v1/search?query=leeroo-kapso - the zero-story Hacker News footprint (fetched 200, 2026-10-11)
