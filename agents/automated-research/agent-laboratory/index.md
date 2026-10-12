---
title: Agent Laboratory
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, paper-generation, human-in-the-loop, open-source]
readability: 3
audience_notes: >
  Engineers tracing the idea-to-paper family's human-assist ancestor and the measurements that came out of it.
  Assumes you know what an ML conference review process looks like.
---

Agent Laboratory is Samuel Schmidgall and collaborators' MIT-licensed framework that takes a human-supplied research idea through literature review, experimentation, and report writing, positioned from the start as an assistant where the human is the pilot.

**It is the idea-to-paper ancestor that measured itself most damagingly: its own evaluation had ten PhD reviewers score its generated papers 3.5 to 4.0 out of 10 against NeurIPS criteria, well below the 5.9 average its authors cite for accepted NeurIPS papers, and co-pilot mode, the human in the loop, was the only thing that moved the number.**

## What it is

A Python framework (github.com/SamuelSchmidgall/AgentLaboratory, MIT) from a January 2025 paper (arXiv 2501.04227) by Schmidgall, Yusheng Su, and eight coauthors across AMD and academic partners.
Three phases run by specialized agents: literature review over arXiv, experimentation through the mle-solver, and report writing through the paper-solver.
The mle-solver iterates code with two commands, REPLACE and EDIT, keeping a pool of top programs scored by a scoring function, with up to three repair attempts before a compile error retires a candidate.
AgentRxiv (arXiv 2503.18102, March 2025) extends it with a preprint server where autonomous labs upload, search, and build on each other's papers.

## Status

Dormant as a repository, foundational as a measurement: 5,900 stars, MIT, last pushed 2025-08-20, as of 2026-10-11.
The HN footprint is nearly absent, a 4-point and a 1-point submission with zero comments from January 2025, while the GitHub community is the second largest in this category.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=SamuelSchmidgall/AgentLaboratory&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=SamuelSchmidgall/AgentLaboratory&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=SamuelSchmidgall/AgentLaboratory&type=date&legend=top-left" />
</picture>

## Strengths

- The most useful negative result in the family: the project published its reviewers' scores against the accepted-paper average instead of only the wins.
- Co-pilot mode is measured, not assumed: human guidance lifted the average review score from 3.8 to 4.38 out of 10 in the project's own study.
- AgentRxiv is the first artifact in this category where labs share outputs, and its ablation (70.2 to 78.2 percent on MATH-500 with the server, a 73.4 to 73.8 plateau without it) grounds the sharing claim.
- Cost and runtime are published per backend: $2.33 per workflow on gpt-4o up to $13.10 on o1-preview, at 95.7 to 98.5 percent reliability.

## Cautions

- The repository has not moved since August 2025 while the rest of the category kept shipping, so treat it as an ancestor to read, not a tool to adopt.
- The generated papers' scores (3.5 to 4.0 of 10) sit far below the accepted-NeurIPS average of 5.9 the same site cites, with significance and contribution scoring lowest.
- The mle-solver's MLE-Bench medal comparison (four medals against AIDE's two) comes from the project's own evaluation with its own model choices (o1-preview for AIDE).
- AgentRxiv's headline discovery (Simultaneous Divergence Averaging) is prompt-engineering rediscovery, and the site itself links work ("All That Glitters is Not Novel") finding disguised plagiarism in AI-generated papers.

## Pricing

Free and open source under MIT; there is no paid tier, so pricing does not apply.
Costs are your own LLM API calls: the site reports $2.33 (gpt-4o) to $13.10 (o1-preview) per full workflow, and $3.11 per paper on the AgentRxiv MATH-500 runs.

## Compared to

- [Sakana AI Scientist](../sakana-ai-scientist/index.md): the fully-autonomous contemporary with the peer-review milestone; Agent Laboratory kept the human pilot and published the score gap that choice leaves.
- [AI-Researcher](../ai-researcher/index.md): the later idea-to-paper system with the larger community; Agent Laboratory has the candid evaluation, AI-Researcher has the production spin-off.
- [AIDE ML](../aide-ml/index.md): the component comparison point; Agent Laboratory's mle-solver was benchmarked against AIDE on MLE-Bench medals.

## Bottom line

**Recommended reading as the idea-to-paper family's measurement ancestor: its own numbers (4 of 10 papers, sharing beats isolation, co-pilot beats autonomous) are the baselines later systems should quote.**
Not for anyone choosing a maintained tool today: the repository has been dormant since August 2025.

## Changes

- 2026-10-11 - Created.

## See also

- [Sakana AI Scientist](../sakana-ai-scientist/index.md) - the fully-autonomous contemporary whose milestone fine print these scores contextualize
- [AI-Researcher](../ai-researcher/index.md) - the later idea-to-paper system with the largest community in the sub-family
- [AIDE ML](../aide-ml/index.md) - the MLE solver Agent Laboratory's own evaluation benchmarked head to head
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/SamuelSchmidgall/AgentLaboratory - repository, MIT license, 5,900 stars, last push 2025-08-20 (as of 2026-10-11)
- https://raw.githubusercontent.com/SamuelSchmidgall/AgentLaboratory/main/README.md - the human-assist positioning, phase structure, and the March 2025 AgentRxiv announcement (fetched 200, 2026-10-11)
- https://arxiv.org/abs/2501.04227 - the paper: authors, three stages, human feedback at each phase (fetched 200 via the arXiv API, 2026-10-11)
- https://agentlaboratory.github.io/ - mle-solver REPLACE/EDIT mechanics, MLE-Bench medal comparison, PhD-reviewer scores against the 5.9 accepted average, co-pilot gains, per-backend costs (fetched 200, 2026-10-11)
- https://agentrxiv.github.io/ - the AgentRxiv results: 70.2 to 78.2 percent on MATH-500, the no-access plateau, parallel-run gains, per-paper cost (fetched 200, 2026-10-11)
- https://hn.algolia.com/api/v1/search?query=AgentLaboratory - the thin Hacker News footprint (fetched 200, 2026-10-11)
