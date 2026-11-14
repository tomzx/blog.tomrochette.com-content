---
title: Kapso
created: 2026-10-11
updated: 2026-11-14
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
Four documented pillars, renamed in the v0.8.0 redesign: `.build()` runs a brief-driven campaign of candidates implemented on their own branches, measured, and kept or refined, `.learn()` mines a finished campaign into evidence-priced lesson cards, the `experience` subcommands and `.load_experience()` serve a build exactly what it loads (your bank, the hosted Leeroopedia gate, a shared team bank, or a corpus ingested from a repository, a researched question, or since v0.9.0 a paper), and `.deploy()` turns a solution into running software on local, Docker, Modal, BentoCloud, or LangGraph Platform targets.
Four harnesses ship bundled (predictive modelling and competitive programming from the redesign, plus agent-engineering and data-engineering, which v0.9.3 moved in from examples where only a repository clone reached them), the examples carry a trading harness, and a Kapso plugin installs the setup, objective, harness, and review skills into Claude Code or Codex in one line.
The technical report (arXiv 2601.21526, January 2026, by Alireza Nadafian, Alireza Mohammadshahi, and Majid Yazdani) describes a git-native experimentation engine where every attempt is a branch, a knowledge system over repositories and papers, and a cognitive memory layer distilling lessons from run logs, diffs, and evaluator feedback.
Leeroopedia, the project's hosted ML knowledge wiki, connects as an MCP server during campaigns.

## Status

Active and accelerating: 125 stars as of 2026-10-15, 18 forks, created 2025-12-07, last pushed 2026-11-13, with the release train at v0.9.3 (November 12, on PyPI): the two patch trains added `kapso compare` (two finished or running campaigns side by side, state, iterations, time, spend, and the delivered and best score after each candidate, printed as Markdown, a file, or JSON, with a winner named only when the two scores mean the same thing, the same direction and a registered evaluator, and a warning when neither campaign registered one), made budget-aware fidelity follow a minimize problem's direction (before the fix the validate grant, the promotion margin, and the reserve went by the higher score, so on a lower-is-better problem the worst probe was the one promoted), bundled the `data-engineering` and `agent-engineering` harnesses into the package beside `predictive-modelling` and `competitive-programming` (name-loadable from any install, both revised on the way in), and cut the six task examples down to setup-only documentation, with v0.9.1 (November 10) the patch release after v0.9.0's rebrand-and-polish (November 6, four days after v0.8.0's breaking redesign): a running campaign now takes notes (`kapso inbox note` files a note into the campaign from the CLI or the plugin), two full-size examples replace the small ones (dbt models on Snowflake carrying a seventeen-ticket backlog, and harness optimization for a customer-support agent on a local model), the ten-language README set lives under docs/translations with a CI check keeping it in step with the English one, and the knowledge-graph hybrid-query and embedding-provider fixes landed, while v0.9.0 was the rebrand-and-polish release itself: the positioning reset to "an engine that runs experiments, deploys the best solution, and learns from every run" told in four parts (smart experimentation, learning loop, deployment, domain adaptation) across the README, docs, package metadata, and CLI help, new `kapso experience search` and `show` shell queries plus `experience add --paper` ingestion from an external contributor, a `notify:` config sending one JSON event when a build pauses for a person, hits budget, fails, or completes, `kapso deploy --branch` to deploy any attempt the trace shows, and the checkpoint schema bumped to version 7, so campaigns recorded by 0.8.0 cannot resume, with no migration by design while the project is pre-1.0; main's November 11-13 commits carried the v0.9.2 and v0.9.3 trains and the post-release `kapso report --json` and README-walkthrough-video commits, as of 2026-11-14.
The v0.8.0 redesign (November 1) renamed the verbs (`kapso evolve` became `kapso build --brief`, `kapso watch --tree` became `kapso trace`, `kapso deploy` takes `--target` instead of `--strategy`), added the `harness`, `experience`, `report`, and `inbox` subcommands, replaced the modes with one packaged configuration with `--config` overrides, and rebuilt the Python API around `kapso.build()` returning a `Solution` carrying score, branch, diff, and explain, so pre-0.8 scripts and configs need remapping.
The v0.7.0 release added cost-aware candidate selection, an estimator prices each finalized candidate before it runs, refusals and measured costs are recorded as campaign events, and the campaign stops when the next estimate would exhaust its budget, plus a `vertex_claude_code` agent that drives Claude Code on Vertex AI open-weight models; the checkpoint schema moved to version 3, so campaigns started before 0.7.0 cannot resume. v0.7.7 (October 15) made a failed bank-connect leave the origin as it found it, and v0.7.8 (October 16) kept the session clone when a branch push is rejected instead of deleting the candidate's only copy of its work.
v0.7.9 changed how repository memory updates: the model now returns a patch of the sections it changed or added, with an explicit `removed_sections` list, instead of rewriting the whole book from a truncated view, so large repositories stop losing sections; a patch that removes a core section or names an unknown one is rejected into the repair loop. v0.7.10 fixed `kapso inbox` listing a relaunched campaign twice.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Leeroo-AI/kapso&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Leeroo-AI/kapso&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Leeroo-AI/kapso&type=date&legend=top-left" />
</picture>

The claimed results are concrete: #1 open-source on MLE-Bench, top ranking on ALE-Bench (1909 Elo against ALE Agent's 1879), first place on all three official RelBench leaderboards (classification 81.2 AUROC, regression 0.2476 NMAE, recommendations 18.4 MAP), and the IOAI 2026 AI Model Track, where the project reports a 536.07 total above all 471 human contestants and a Grand Master Trophy among the 14 founding AI participants, with IOAI's own account of the inaugural track published September 29, 2026.
**The community footprint is nearly absent: a Hacker News search for the project returns zero stories as of 2026-10-11, the 125 stars are small for the claims, and the PyPI package named `kapso` is an unrelated WhatsApp tool that shadows this one in installs, a collision the README itself warns about.**

## Strengths

- The judge is declared with the objective: every campaign carries its own evaluator, so progress is measured rather than self-declared, the Karpathy keep-or-revert property generalized to arbitrary ML and data objectives.
- The learning layer is the differentiator: lessons carry the evidence that earned them and expire when they stop holding, and outside repositories and papers fold into the same knowledge graph.
- Third-party anchoring where it exists: the RelBench results sit on Stanford's official leaderboard, and IOAI's organizers published their own review of the track the IOAI result comes from.
- It ships as a library rather than a demo: a PyPI package, documented pillars, and agent skill files for Claude Code, Codex, and OpenCode.

## Cautions

- The benchmark headline claims are self-run: the MLE-Bench and ALE-Bench numbers live in the project's own benchmark directories, and Stanford's RelBench leaderboard page states plainly that it holds self-reported results submitted in good faith, pointing to RelArena for controlled evaluation.
- 125 stars as of 2026-10-15, zero Hacker News stories, and no independent replication surfaced in this run's searches, a thin footprint for results this strong.
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
- 2026-10-19 - Recorded the October 18 releases: v0.7.9's patch-based repository-memory update (sections stop disappearing on large repositories) and v0.7.10's kapso inbox dedup, with PyPI at 0.7.10.
- 2026-11-05 - Recorded the v0.8.0 breaking redesign (verbs renamed, modes replaced by one configuration, Python API rebuilt around `kapso.build()`), rewrote the pillar descriptions to the renamed surfaces, noted the two shipped harnesses and the plugin install line, harmonized the cautions' star figure with the Status line, and recorded main's November 3-4 resume fixes.
- 2026-11-07 - Recorded the v0.9.0 release (November 6): the four-part rebrand across every public surface, the experience search, show, and paper-ingest commands from an external contributor, the notify webhook, `deploy --branch`, and the checkpoint-schema-7 break that strands 0.8.0 campaigns; moved the deploy targets to Docker, Modal, BentoCloud, and LangGraph Platform; and updated the RelBench claim to first place on all three official leaderboards.
- 2026-11-11 - Volatile re-verification: recorded the v0.9.1 patch release (November 10): campaign notes through `kapso inbox note`, the two full-size examples (dbt models on Snowflake, support-agent harness optimization on a local model) replacing the small ones, the ten-language README set under docs/translations with a CI step check, and the knowledge-graph hybrid-query and embedding-provider fixes.
- 2026-11-14 - Volatile re-verification: recorded the v0.9.2 and v0.9.3 releases (November 11-12): the campaign-compare command with its scoring-direction and evaluator-match guard, the minimize-direction fidelity fix that stops the worst probe winning on lower-is-better problems, the agent-engineering and data-engineering harnesses bundling into the package, the setup-only task-example rewrite, and the post-release `kapso report --json` and walkthrough-video commits.

## See also

- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the measured-judge ancestor Kapso generalizes into campaigns
- [ARIS](../aris/index.md) - the skills-based ML research loop in the same family
- [DeepAnalyze](../deepanalyze/index.md) - the trained-model data-science sibling
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/Leeroo-AI/kapso - repository, MIT license, benchmark claims, and release train (as of 2026-11-06)
- https://api.github.com/repos/Leeroo-AI/kapso/releases - the v0.7.7 (2026-10-15) through v0.7.10 (2026-10-18) release bodies behind the durability and memory-patch descriptions (fetched 200, 2026-10-29)
- https://api.github.com/repos/Leeroo-AI/kapso/releases/latest - v0.9.0 (2026-11-06), the rebrand-and-polish release: experience search, show, and --paper, the notify webhook, deploy --branch, and the checkpoint-schema-7 break (fetched 200, 2026-11-07)
- https://api.github.com/repos/Leeroo-AI/kapso/releases?per_page=5 - v0.9.3 (2026-11-12) the latest release above v0.9.2 (2026-11-11) and v0.9.1 (2026-11-10) (fetched 200, 2026-11-14)
- https://api.github.com/repos/Leeroo-AI/kapso/releases/tags/v0.9.2 - the v0.9.2 notes: campaign compare, the fidelity direction fix, the setup-only example rewrite (fetched 200, 2026-11-14)
- https://api.github.com/repos/Leeroo-AI/kapso/releases/tags/v0.9.3 - the v0.9.3 notes: the bundled data-engineering and agent-engineering harnesses, their revisions, and the upgrade note (fetched 200, 2026-11-14)
- https://api.github.com/repos/Leeroo-AI/kapso/commits?since=2026-11-10T00:00:00Z&per_page=30 - the November 11-13 v0.9.2 and v0.9.3 trains behind this refresh, plus the post-release report-json and walkthrough-video commits (fetched 200, 2026-11-14)
- https://raw.githubusercontent.com/Leeroo-AI/kapso/main/README.md - the four-part pillar table, CLI requirements, PyPI collision warning, the ten-language translations, the deploy targets, and the IOAI, RelBench, and MLE-Bench claims (fetched 200, 2026-11-07)
- https://arxiv.org/abs/2601.21526 - the technical report: git-native experimentation engine, knowledge system, and cognitive memory layer (fetched 200, 2026-10-11)
- https://pypi.org/pypi/leeroo-kapso/json - package version 0.9.0 published 2026-11-06, MIT license, and Python 3.10+ requirement (fetched 200, 2026-11-07)
- https://ioai-official.org/what-happens-when-autonomous-ai-takes-on-the-same-tasks-as-the-worlds-top-young-ai-talents/ - IOAI's own account of the inaugural AI Model Track, September 29, 2026 (fetched 200, 2026-10-11)
- https://star-project.stanford.edu/relbench/leaderboard/ - the official RelBench leaderboard and its self-reported-results disclaimer (fetched 200, 2026-10-11)
- https://raw.githubusercontent.com/Leeroo-AI/kapso/main/benchmarks/ioai2026/README.md - the per-task IOAI numbers behind the 536.07 total and Grand Master Trophy (fetched 200, 2026-10-11)
- https://hn.algolia.com/api/v1/search?query=leeroo-kapso - the zero-story Hacker News footprint (fetched 200, 2026-10-11)
