---
title: NanoResearch
created: 2026-10-11
updated: 2026-10-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, paper-generation, slurm, gpu, open-source]
readability: 3
audience_notes: >
  Engineers comparing idea-to-paper pipelines that run actual experiments, especially on shared GPU clusters.
  Assumes you know what a SLURM job scheduler does.
---

NanoResearch is OpenRaiser's MIT-licensed nine-stage engine that takes a research idea to a complete LaTeX paper by running the experiments itself: the pipeline submits generated code to local or SLURM GPU clusters, parses the training logs that come back, and writes every table and figure from those outputs.

**It is the idea-to-paper column that binds the manuscript to actual runs rather than sandbox simulations, and its resumable pipeline plus per-stage model routing make it the practical choice for anyone whose experiments need a GPU cluster, with the usual discount that the evidence is self-published.**

## What it is

A Python CLI (github.com/OpenRaiser/NanoResearch, MIT, Python 3.10+, v1.0 released March 2026) with a bilingual Chinese-and-English README.
The nine stages run from literature search (OpenAlex and Semantic Scholar) through experiment blueprints, code generation, GPU job submission, log parsing, figure generation, and LaTeX writing, with checkpoint-and-resume from any failed stage and a different model configurable per stage.
Execution targets are a local GPU or a SLURM cluster with auto-submission; a Claude Code mode and a Feishu bot add chat and messaging surfaces to the CLI, and an Evo self-evolving pipeline is listed as a feature section in both READMEs.
The README's core claim: every number, table, and chart in the output paper comes from the pipeline's own experiment outputs, not LLM fabrication.

## Status

Active: 1,340 stars, 92 forks, created 2026-03-17, last pushed 2026-10-09, as of 2026-10-11.
The release history is thin (a single assets release in March 2026) despite the README's v1.0 milestone, and a search for the name returns no Hacker News threads as of 2026-10-11.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=OpenRaiser/NanoResearch&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=OpenRaiser/NanoResearch&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=OpenRaiser/NanoResearch&type=date&legend=top-left" />
</picture>

## Strengths

- The evidence model is the differentiator: code goes to a GPU cluster, logs come back, and the paper binds to those logs, attacking the fabricated-results failure the citation checkers cannot see.
- Checkpoint-and-resume per stage plus per-stage model routing is engineering for the long, flaky runs actual experiments produce.
- Venue templates (NeurIPS, ICML, arXiv) and the claimed cost floor (as low as $0.5 of API credit per paper on DeepSeek) make it the cheapest member here per paper.
- Three surfaces (CLI, Claude Code mode, Feishu bot) suit both individual researchers and lab groups.

## Cautions

- The core claim is the README's: this run found no independent evaluation, no benchmark integration, and no third-party account of a NanoResearch paper's data integrity.
- A single March 2026 release asset against a v1.0 milestone suggests versioning lives in the README rather than in tagged releases.
- SLURM auto-submission runs generated code on shared infrastructure, a surface the README does not discuss sandboxing.
- The project publishes no paper of its own, so its design claims rest on documentation alone.

## Pricing

Free and open source under MIT; there is no paid tier, so pricing does not apply.
Costs are your own GPU time (local or cluster) and LLM API calls; the README claims as low as $0.5 per paper with DeepSeek.

## Compared to

- [AutoResearchClaw](../autoresearchclaw/index.md): the 23-stage rival with citation verification and human-oversight modes; NanoResearch is the GPU-cluster executor with no published citation-check layer.
- [Sakana AI Scientist](../sakana-ai-scientist/index.md): the ancestor; Sakana's experiments ran in managed sandboxes, NanoResearch's go to schedulers you administer.
- [Agent Laboratory](../agent-laboratory/index.md): the human-assist ancestor with published quality scores; NanoResearch is fully autonomous with published costs instead.

## Bottom line

**Recommended for researchers with GPU cluster access who want idea-to-paper runs where the paper's numbers come from jobs the pipeline itself submitted.**
Not for anyone needing verified data integrity: the binding-to-logs claim is self-published, and the citation layer other pipelines ship is absent here.

## Changes

- 2026-10-11 - Created.
- 2026-10-26 - Rotation re-verification: status unchanged (last push still 2026-10-09, the single assets release still the whole release train, and the name still carries no Hacker News threads); every cited URL re-fetched, all live.

## See also

- [AutoResearchClaw](../autoresearchclaw/index.md) - the stage-count rival with the citation-verification layer NanoResearch lacks
- [Sakana AI Scientist](../sakana-ai-scientist/index.md) - the sub-family ancestor
- [Agent Laboratory](../agent-laboratory/index.md) - the measurement-focused ancestor
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/OpenRaiser/NanoResearch - repository, MIT license, 1,340 stars, last push 2026-10-09 (as of 2026-10-11)
- https://raw.githubusercontent.com/OpenRaiser/NanoResearch/main/README.md - the Chinese main README: the actually-runs-experiments claim, nine stages, SLURM, Evo pipeline, Claude Code mode, Feishu bot (fetched 200, 2026-10-11)
- https://raw.githubusercontent.com/OpenRaiser/NanoResearch/main/README_en.md - the English README: v1.0 milestones, OpenAlex and Semantic Scholar search, checkpoint-and-resume, per-stage routing, the $0.5-per-paper claim (fetched 200, 2026-10-11)
- https://api.github.com/repos/OpenRaiser/NanoResearch/releases?per_page=5 - the single assets release of 2026-03-19 (fetched 200, 2026-10-11)
- https://hn.algolia.com/api/v1/search?query=NanoResearch - the search returning no threads (fetched 200, 2026-10-11)
