---
title: Sakana AI Scientist
created: 2026-10-11
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, sakana-ai, paper-generation, open-source]
readability: 3
audience_notes: >
  Engineers tracing where the idea-to-paper pipeline family came from and what its peer-review milestone actually was.
  Assumes you know what an ML conference workshop is.
---

The AI Scientist is Sakana AI's end-to-end research pipeline that generates hypotheses, runs experiments, and writes papers, and its second version produced the first fully AI-generated manuscript to pass a peer-review process, at an ICLR 2025 workshop.

**The AI Scientist is the ancestor this category's idea-to-paper columns measure themselves against, and its famous first is smaller than remembered: one of three curated papers cleared a workshop's average acceptance threshold, was withdrawn from publication by design, and the authors' own internal reviews found none of the three at main-conference bar.**

## What it is

Version 1 (August 2024, arXiv 2408.06292) was the first system to generate full scientific manuscripts end to end, template-based and ML-focused.
Version 2 (April 2025, arXiv 2504.08066, by Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, and David Ha, a Sakana AI with UBC and Oxford collaboration) removed the templates, generalized across ML domains, and added progressive agentic tree search managed by a dedicated experiment-manager agent, plus a vision-language-model feedback loop on figures.
Both versions are open code on your own GPUs and API keys (OpenAI by default, Gemini and others supported in v2), under a custom Sakana license that GitHub records as NOASSERTION.

## Status

Dormant as repositories, foundational as influence: v2 at 7,294 stars and v1 at 14,692, both last pushed 2025-12-19, as of 2026-10-11.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=SakanaAI/AI-Scientist-v2,SakanaAI/AI-Scientist&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=SakanaAI/AI-Scientist-v2,SakanaAI/AI-Scientist&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=SakanaAI/AI-Scientist-v2,SakanaAI/AI-Scientist&type=date&legend=top-left" />
</picture>

The lineage anchors the category: AutoResearchClaw measures its headline 54.7 percent improvement against AI Scientist v2, and the Agon paper counts AI Scientist v2's prompt surface (about 110 roles and 302.4 KiB) in its cross-system comparison.
The March 12, 2025 first-publication experiment: three v2 manuscripts went through double-blind review at ICLR 2025's ICBINB workshop with the organizers' cooperation, one averaged 6.33 (scores of 6, 7, 6), above the workshop's acceptance threshold, and all three were withdrawn before publication per a protocol agreed in advance.
**The v2 forum footprint stayed small: the first-publication story drew two to three points across several Hacker News posts as of 2026-10-11, against the 203-point, 132-comment thread v1's 2024 launch drew.**

## Strengths

- The first demonstration that the complete loop (hypothesis, code, experiments, figures, manuscript) can clear a standard peer-review process, however scoped.
- v2's tree search with an experiment manager is the mechanism the newer idea-to-paper columns build on or benchmark against.
- Unusually candid self-critique: Sakana's own post documents the human curation step, the withdrawal, the citation errors, and the internal verdict that no paper met conference bar.
- Everything is public: the code, the three papers, and the humans' reviews sit in repositories anyone can judge.

## Cautions

- The milestone was a workshop, not a conference: workshop acceptance rates run 60 to 70 percent, and humans picked which three of the generated papers to submit, a selection step inside the fully-autonomous claim.
- The accepted paper was never published: withdrawn by design, so the result is a review score, not a publication record.
- Both repositories are dormant since December 2025 and neither carries a standard open-source license, which limits reuse beyond reading.
- The system executes LLM-written code with web access, a risk the README itself flags for sandboxing.
- v1's launch-thread attention never returned for v2: the peer-review milestone got a fraction of the 2024 coverage.

## Pricing

Free to run; the project has no paid tier, so pricing does not apply.
Costs are your own GPU time and LLM API keys.

## Compared to

- [AutoResearchClaw](../autoresearchclaw/index.md): the 23-stage pipeline that benchmarks itself against AI Scientist v2 and adds citation verification and human-oversight modes; choose it for structured deliverables, AI Scientist for the original tree-search loop.
- [Agon](../agon/index.md): the producer-critic plugin whose paper measured AI Scientist v2's prompt surface in its cross-system comparison.
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the contemporary loop whose judge is a measured loss; AI Scientist's judge is review scores, which is why its milestones need more fine print.

## Bottom line

**Recommended reading as the idea-to-paper family's founding artifact and as a case study in running an AI-science milestone with the fine print attached.**
Not for anyone choosing a maintained tool today: both repositories are dormant and the license is custom.

## Changes

- 2026-10-11 - Created.
- 2026-10-11 - Added the star history chart.

## See also

- [AutoResearchClaw](../autoresearchclaw/index.md) - the pipeline that benchmarks its improvement against AI Scientist v2
- [Agon](../agon/index.md) - the paper that measured v2's prompt surface
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the measured-judge counterpart in the same loop family
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/SakanaAI/AI-Scientist-v2 - the v2 repository, stars, license status, and last push date (as of 2026-10-11)
- https://raw.githubusercontent.com/SakanaAI/AI-Scientist-v2/main/README.md - the v1-versus-v2 comparison, tree-search description, and code-execution caution (fetched 200, 2026-10-11)
- https://arxiv.org/abs/2504.08066 - the v2 paper: authors, the ICLR workshop experiment, and the tree-search method (fetched 200, 2026-10-11)
- https://sakana.ai/ai-scientist-first-publication/ - the first-publication experiment: review scores, withdrawal protocol, human curation, and internal reviews (fetched 200, 2026-10-11)
- https://api.github.com/repos/SakanaAI/AI-Scientist - the v1 repository's star count and push date for the status line (as of 2026-10-11)
- https://hn.algolia.com/api/v1/search?query=AI%20Scientist%20Sakana&tags=story - the v1 203-point launch thread and v2's thin discussion footprint (fetched 200, 2026-10-11)
