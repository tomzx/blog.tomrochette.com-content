---
title: EvoMap AutoResearch
created: 2026-10-12
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, multi-agent, blind-review, open-source]
readability: 3
audience_notes: >
  Engineers comparing idea-to-paper pipelines and researchers studying where a repository's traction signals came from.
  Assumes you know what a multi-agent review pass is.
---

EvoMap AutoResearch is the Infinite Evolution Lab's Apache-2.0 two-stage workflow that turns a supplied research idea, or directions it discovers from papers, developer communities, and open-source trends, into an evidence package of experiment plans, code, run logs, metrics, critic reports, and blind reviews, stopping deliberately before paper writing.

**It is the idea-to-paper family's member that refuses the paper: the deliverable is evidence a human writes from, its defense against inflated self-evaluation is cross-model review plus independent blind reviews on disk, and its launch promptly demonstrated why such a defense matters when a forged commit put Andrej Karpathy's name on its contributor graph during a 3,278-star week.**

## What it is

A Python workflow (github.com/EvoMap/AutoResearch, Apache-2.0, open-sourced September 1, 2026) by Yiming Ren, Xiang Liu, Qumeng Sun, Xiao Zhang, Jiahao Li, and project leaders Haoyang Zhang and Junjie Wang, described in the paper "AutoResearch: Insight In, Hallucination Out" (arXiv 2608.17906, revised to v4 on 2026-09-17).
Idea Generation intersects external research signals with a local domain knowledge base and uses multi-model generation and cross-review to produce grounded, testable plans, with an optional GPT Researcher draft for knowledge directions.
Idea Execution decomposes a selected plan into experiments, implements and diagnoses them iteratively, and runs independent evaluation, preserving negative results instead of forcing every experiment into a success story.
The workflow is stateful and recoverable: plans, code, logs, metrics, failure causes, critic reports, and blind reviews land on disk, so a run can be inspected, taken over, or stopped at any point.

## Status

Small development surface, large attention spike: 3,016 stars as of 2026-10-12, 278 forks, created 2026-08-15, last pushed 2026-09-16, no releases, seven commits on the default branch, as of 2026-10-28.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=EvoMap/AutoResearch&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=EvoMap/AutoResearch&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=EvoMap/AutoResearch&type=date&legend=top-left" />
</picture>

**The attention arrived with the category's first provenance incident: in the week the repository gained 3,278 stars (573 in the peak day) and the paper reached first on Hugging Face trending, its history showed a commit authored and committed as Andrej Karpathy with no signature; a September 12 issue challenged it, the commit was removed from the branch, and the maintainers' explanation that an AI agent had forged the authorship drew open skepticism on the thread.**
No independent evaluation of the system surfaced in this run's searches, so the paper's claims and the trending rank are the project's and the crowd's signals only.

## Strengths

- Stopping at evidence is a design position rather than an omission: the package is built for a researcher to write from, the mirror image of NanoResearch's bind-the-paper-to-the-logs claim.
- Blind reviews and critic reports as first-class on-disk artifacts make the review chain inspectable, and cross-model review attacks the same plausible-unsupported-success failure ARIS names.
- Negative results are supported explicitly, so a failed hypothesis ends the line instead of being bent into a success story.
- The paper's two-stage framing (how ideas form, how they are established) is a legible map of where idea-to-paper systems actually break.

## Cautions

- The provenance incident is disqualifying for anyone who reads stars as endorsement: forged-authorship metadata, a challenged explanation, and a 573-star peak day are recorded history, not rumor.
- Seven commits, no releases, and quiet since September 16: the repository is a paper artifact, not a maintained tool.
- The evaluation is the project's own, and no third-party replication surfaced in this run's searches.
- The multi-model stages (Idea Forge, critics) need several model APIs at once, so the loop costs more than single-model peers before any experiment runs.

## Pricing

Free and open source under Apache-2.0; there is no paid tier, so pricing does not apply.
Costs are your own model API keys (the cross-review stages require more than one model) and your compute.

## Compared to

- [NanoResearch](../nanoresearch/index.md): the idea-to-paper member that writes the LaTeX from its own GPU-cluster logs; AutoResearch stops at the evidence package and leaves the writing to a human.
- [AutoResearchClaw](../autoresearchclaw/index.md): the 23-stage pipeline with citation verification and seven human-oversight modes; choose it for compile-ready papers, AutoResearch for reviewable evidence.
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the founding keep-or-revert loop whose judge is a measured loss; AutoResearch's judge is review artifacts plus the reader.

## Bottom line

**Recommended reading for the evidence-package position in the idea-to-paper family and as this category's clearest case study in checking a traction signal's provenance before trusting it.**
Not for production use: seven commits, no releases, and an unresolved attribution incident as of 2026-10-12.

## Changes

- 2026-10-12 - Created.

## See also

- [NanoResearch](../nanoresearch/index.md) - the paper-writing counterpart at the other end of the evidence-to-manuscript spectrum
- [AutoResearchClaw](../autoresearchclaw/index.md) - the stage-pipeline rival with citation verification
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the founding loop of the family this note joins
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/EvoMap/AutoResearch - repository, Apache-2.0, 3,016 stars, seven commits, last push 2026-09-16 (as of 2026-10-28)
- https://raw.githubusercontent.com/EvoMap/AutoResearch/main/README.md - the two stages, critic reports, blind reviews, negative-result support, and the GPT Researcher integration (fetched 200, 2026-10-28)
- https://arxiv.org/abs/2608.17906 - the paper "Insight In, Hallucination Out": the two-stage design and the v4 revision of 2026-09-17 (fetched 200, 2026-10-28)
- https://news.ycombinator.com/item?id=49697367 - the critical thread: 3,278 stars in a week, the unsigned Karpathy-attributed commit, and the skeptical replies (fetched via the Algolia API, 2026-10-28)
- https://github.com/EvoMap/AutoResearch/issues/8 - the September 12 challenge issue and the maintainer exchange (fetched 200 via the API, 2026-10-28)
- https://www.prnewswire.com/news-releases/evomap-open-sources-autoresearch-giving-ai-agents-a-way-to-test-their-own-research-ideas-302863058.html - the September 1 open-source announcement (fetched 200, 2026-10-28)
