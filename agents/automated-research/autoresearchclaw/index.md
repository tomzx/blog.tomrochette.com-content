---
title: AutoResearchClaw
created: 2026-10-10
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, agentic-llm, open-source, paper-generation]
readability: 3
audience_notes: >
  Engineers evaluating idea-to-paper research pipelines and researchers studying failure handling and citation integrity in autonomous agents.
  Assumes you know what a multi-agent pipeline and a BibTeX file are.
---

AutoResearchClaw is the MIT-licensed 23-stage pipeline from the aiming-lab organization that turns a one-line research idea into a compile-ready paper, with sandbox experiments, multi-agent debate, a four-layer citation-verification layer, and seven human-in-the-loop modes.

**AutoResearchClaw is the idea-to-paper pipeline that treats failure and fabrication as first-class problems: its executor heals through Pivot/Refine loops, its citations pass arXiv, CrossRef, DataCite, and LLM checks before delivery, and its 54.7 percent win over AI Scientist v2 is measured on its own ARC-Bench, a self-run benchmark the README has since widened from 25 to 55 topics.**

## What it is

A Python pipeline (created 2026-03-15) run from the `researchclaw` CLI, standalone, through an OpenClaw bridge to Discord, Telegram, Lark, or WeChat, or on any ACP-compatible agent backend (Claude Code, Codex CLI, Copilot CLI, Gemini CLI, Kimi CLI).
The arXiv paper (2605.20025, v2, by 36 authors led by Jiaqi Liu and Shi Qiu) presents five mechanisms: structured multi-agent debate, a self-healing executor with a Pivot/Refine decision loop, verifiable result reporting against fabricated numbers and hallucinated citations, human-in-the-loop collaboration across seven intervention modes, and cross-run evolution that converts past failures into future safeguards.
Deliverables per run: a paper draft, conference-ready LaTeX (NeurIPS, ICML, ICLR templates), a BibTeX file with references pulled from OpenAlex, Semantic Scholar, and arXiv, a verification report, sandbox experiment code and metrics, charts, multi-agent reviews, and evolution lessons.
MetaClaw adds cross-run learning (pipeline failures become structured lessons injected into later runs), and the skills library loads 20 preloaded skills plus community contributions.
The companion ARC-Bench dataset ships on Hugging Face under the AIMING-Lab-UNC account, widened at v0.5.0 (May 2026) to 55 topics across machine learning, high-energy physics, quantum, biology, and statistics.

## Status

Dormant since August: 14,618 stars as of 2026-10-11, 1,711 forks, created 2026-03-15, last push 2026-08-19, latest release v0.5.0 on 2026-05-20, as of 2026-10-25.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=aiming-lab/AutoResearchClaw&type=date&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=aiming-lab/AutoResearchClaw&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=aiming-lab/AutoResearchClaw&type=date&legend=top-left" />
</picture>

**The repository has gone quiet while attention held: no commits in over nine weeks and no release in five months as of 2026-10-25, a Hacker News footprint of two stories at two and one points with zero comments, and the eight showcase papers are self-published, so the 14.6k stars currently measure attention the repository is no longer feeding.**

## Strengths

- Citation integrity is a design point, not an afterthought: the four-layer check (arXiv, CrossRef, DataCite, LLM) kills fabricated references before delivery, the failure class the no-kernel columns are most exposed to.
- Failure handling is architectural: Pivot/Refine turns failed experiments into information, and MetaClaw accumulates them into reusable skills.
- The seven-mode human-oversight ladder (full-auto through step-by-step) is the widest in this category, an answer to the trust problem rather than a denial of it.
- ARC-Bench gives the loop a rubric-scored eval set spanning five domains instead of a single ML sandbox.

## Cautions

- The 54.7 percent improvement over AI Scientist v2 is self-reported on the project's own benchmark, with no independent replication surfaced in this run's searches.
- Development is quiet: last push 2026-08-19 and last release 2026-05-20, which is a poor sign for a 23-stage pipeline whose stages depend on external APIs and agent backends.
- The two zero-comment Hacker News stories say there is no practitioner debate to check the claims against.
- A 23-stage pipeline is heavy to adopt and heavier to fork: the runtime surface (LLM providers, Docker, LaTeX, five agent backends) is wide.

## Pricing

Free and MIT; there is no paid tier, so pricing does not apply.
Costs are your own LLM API keys and compute (a Docker executor with GPU, MPS, or CPU auto-detection).

## Compared to

- [Agon](../agon/index.md): the other idea-to-paper column; Agon is a Claude Code plugin with adversarial critics and a failure taxonomy, AutoResearchClaw a standalone pipeline whose added layer is citation verification and a human-oversight ladder.
- [ARIS](../aris/index.md): the markdown-skill loop ported across harnesses with cross-model review gates; AutoResearchClaw is a fixed 23-stage pipeline you run rather than a method you install.
- [GPT Researcher](../gpt-researcher/index.md): the cited-report baseline with no experiments; AutoResearchClaw runs sandbox experiments and ships LaTeX.

## Bottom line

**Recommended for studying how an autonomous pipeline can make citation fabrication and silent failure first-class problems, and for teams that want idea-to-paper runs with explicit human-oversight modes.**
Not for anyone who needs an actively maintained tool (eight weeks without a commit) or independently verified benchmark claims.

## Changes

- 2026-10-10 - Created.
- 2026-10-25 - Rotation re-verification: corrected the paper's author list to the arXiv v2 count of 36, led by Jiaqi Liu and Shi Qiu (the note had named only the first eight), confirmed dormancy (push still 2026-08-19, release still v0.5.0), and re-fetched every cited URL, all live.

## See also

- [Agon](../agon/index.md) - the producer-critic idea-to-paper column and the Agon paper's comparator
- [ARIS](../aris/index.md) - the skills-based cross-model loop in the same family
- [GPT Researcher](../gpt-researcher/index.md) - the cited-report baseline AutoResearchClaw extends to experiments
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/aiming-lab/AutoResearchClaw - repository and README: 23-stage pipeline, deliverables, OpenClaw and ACP-backend support, release news (fetched 200, 2026-10-25)
- https://api.github.com/repos/aiming-lab/AutoResearchClaw - stars, forks, created and pushed dates, MIT license, and topics for the as-of status (fetched 200, 2026-10-25)
- https://raw.githubusercontent.com/aiming-lab/AutoResearchClaw/main/README.md - the README source: stage outputs, citation-verification layers, HITL system, ARC-Bench v0.5.0 widening, and the 36-author citation block (fetched 200, 2026-10-25)
- https://arxiv.org/abs/2605.20025 - the paper, v2: five mechanisms, the 54.7 percent AI Scientist v2 comparison on ARC-Bench, the seven intervention modes, and the full author list (fetched 200, 2026-10-25)
- https://api.github.com/repos/aiming-lab/AutoResearchClaw/releases?per_page=5 - the release train through v0.5.0 (2026-05-20), still the latest (fetched 200, 2026-10-25)
- https://hn.algolia.com/api/v1/search?query=AutoResearchClaw - the two zero-comment Hacker News stories behind the discussion-footprint claim (fetched 200, 2026-10-25)
- https://huggingface.co/datasets/AIMING-Lab-UNC/ARC-Bench - the ARC-Bench dataset page under the AIMING-Lab-UNC account (fetched 200, 2026-10-25)
