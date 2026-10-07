---
title: Sepia
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, skills, writing, humanizer, fiction]
readability: 3
audience_notes: >
  Engineers and technical writers who ship LLM-assisted prose and want it to stop reading as machine-made.
  Assumes familiarity with SKILL.md packaging and at least one coding agent.
---

Sepia is an MIT-licensed de-AI writing skill for Claude Code, Codex, Grok Build, Antigravity, and the 77+ agents the Skills CLI reaches, built on the finding that the durable AI tells are structural rather than stylistic.

**Its bet is that repairing narrative architecture (themes explained by the narrator, tidy single-track plots, emotion rendered only as bodily sensation) beats word swaps, because in the study it cites, human surface editing moved detection only from 95.5% to 93.9% macro-F1.**

## What it is

One canonical SKILL.md with thin operation wrappers, maintained by Nanako0129, exposing write, review (diagnose only), refactor (minimal edits), recreate (full rewrite), and an opt-in Hemingway voice profile.
Fiction gets a three-pass protocol over narrative architecture, discourse flow, and surface style.
Professional prose gets venue-matched rule files for release notes, PR replies, postmortems, tickets, and technical articles.
Chinese text gets a separate calibration file across four evidence layers, including a measured corpus of about two thousand Taiwanese news articles.
Every rule traces to a research ledger in the repo that digests fifteen studies, led by StoryScope (arXiv:2604.03136, 61,608 stories, 93.2% macro-F1 from narrative features alone), with per-model fingerprints that name which vendors published guidance and which were merely consulted.
Install is `npx skills add Nanako0129/sepia -g` or a native plugin marketplace, and the repo runs CI workflows for behavioral evals and version consistency.

## Status

Active and early: 2,992 stars and 193 forks as of 2026-10-06, repo pushed 2026-09-23, eleven open issues, created 2026-08-28.

[![Star History Chart](https://api.star-history.com/chart?repos=Nanako0129/sepia&type=date&legend=top-left)](https://www.star-history.com/?repos=Nanako0129%2Fsepia&type=date&legend=top-left)

The growth is fast but young: the entrant data had it near 1,444 stars about five days after launch, and it has roughly doubled since.
There is no Hacker News thread under its name (my searches returned only unrelated sepia stories) and no mainstream coverage as of 2026-09-27, so the audience is GitHub plus the third-party registries that mirror and review it.
A third-party snapshot service recorded 2,860 stars on 2026-09-26, one day before this note's count, so the trajectory held through the week.
Maintenance is funded by a Patreon link, not a company.

## Strengths

- **Every rule carries provenance: the ledger separates measured findings from consulted-vendor guidance instead of inventing entries where no guidance exists.**
- The review operation diagnoses without editing, so the skill doubles as an audit surface rather than a rewrite button.
- Cross-harness by construction: one Agent Skills standard file, with native packaging only for the command surfaces that need it.
- The README states its own verification limits (installs verified, per-platform behavior not exercised), which is rarer than it should be in this ecosystem.

## Cautions

- **The output depends on judgment calls the skill does not fully specify: there is no rollback path when a refactor overshoots and no score telling you whether the chosen moves stayed inside the human distribution.**
- The voice-skills interface rests on one blind review experiment on one specimen, which the README itself flags as a worked example, not measured evidence.
- Applying every rule produces its own fingerprint, so calibration reduces to a 3-5 moves guideline with no enforcement.
- Per-model fingerprint tables age fast, tied to named model versions that a new model generation stales.
- Star velocity on a month-old repo is a distribution signal, not a quality verdict, and the zero-HN-footprint cuts both ways.

## Pricing

Free.
MIT licensed, no paid tier, no account; the maintainer's stated costs are model quota for evals and literature surveys, funded through Patreon, as of 2026-09-27.

## Compared to

- Agent-Native: Builder.io's pack is workflow breadth plus an app funnel; sepia is one deep skill with a research ledger.
- Anthropic Agent Skills: the vendor format sepia conforms to; sepia is a pack on that format, not a competing format.
- blader/humanizer: the popular surface-level pass; sepia runs that as its third pass and claims the two architecture passes before it are the actual fix.

## Bottom line

Recommended for writers who already run a surface pass and still get flagged, and for teams standardizing postmortems, PR replies, and release notes.
Not for regulated or brand-locked prose, where the venue's fixed register looks machine-made precisely because it is standardized.
My disagreeable claim: most humanizer installs, sepia included, are plausibly wasted context, because the only test that settles the question (running real work twice, with and without the skill, then diffing the outputs) is one almost nobody runs.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars candidates were processed.
- 2026-10-07 - Added the Nanako0129/sepia star history chart to the Status section.

## See also

- [The Tells Are Structural](../../the-tells-are-structural/index.md) - the corpus essay that makes the same structural-tells argument sepia operationalizes
- [Agent-Native](../agent-native/index.md) - the other curated pack in this category, workflow breadth versus sepia's single-skill depth
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the packaging standard sepia targets
- [skills.sh](../skills-sh/index.md) - the registry whose CLI gives sepia its 77+ agent reach
- [SkillOpt](../skillopt/index.md) - training skill text against held-out validation, a research answer to sepia's unscored calibration

## References

- https://api.github.com/repos/Nanako0129/sepia - 2,992 stars, 193 forks, MIT, pushed 2026-09-23 (200, fetched 2026-10-06)
- https://raw.githubusercontent.com/Nanako0129/sepia/main/README.md - operations, three-pass protocol, research ledger, per-platform verification limits (200)
- https://hysenlabs.com/en/projects/nanako0129-sepia - third-party editorial review (September 10, 2026) with critical sections on calibration and wrong-tool cases (200)
- https://arxiv.org/abs/2604.03136 - StoryScope: 61,608 stories, 93.2% macro-F1 from narrative features alone, v6 revised 2026-08-10 (200)
- https://hn.algolia.com/api/v1/search?query=sepia&tags=story - the zero-hit search behind the missing-footprint statement (200, fetched 2026-09-27)
- https://old.reddit.com/r/ClaudeAI/comments/1w2g7za/i_turned_the_storyscope_paper_into_a_deai_writing/ - the maintainer's launch thread, fetch blocked with 403 in this run, cited for existence only
