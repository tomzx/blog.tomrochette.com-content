---
title: Sepia
created: 2026-09-27
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, skills, writing, humanizer, fiction]
readability: 3
audience_notes: >
  Engineers and technical writers who ship LLM-assisted prose and want it to stop reading as machine-made.
  Assumes familiarity with SKILL.md packaging and at least one coding agent.
---

Sepia is an MIT-licensed de-AI writing skill for Claude Code, Codex, Grok Build, Antigravity, QwenPaw, and the 77+ agents the Skills CLI reaches, built on the finding that the durable AI tells are structural rather than stylistic.

**Its bet is that repairing narrative architecture (themes explained by the narrator, tidy single-track plots, emotion rendered only as bodily sensation) beats word swaps, because in the study it cites, human surface editing moved detection only from 95.5% to 93.9% macro-F1.**

## What it is

One canonical SKILL.md with thin operation wrappers, maintained by Nanako0129, exposing write, review (diagnose only), refactor (minimal edits), recreate (full rewrite), and opt-in voice profiles (built-in Hemingway and Taiwan long-form journalism voices, plus author-defined persona profiles).
Fiction gets a three-pass protocol over narrative architecture, discourse flow, and surface style.
Professional prose gets venue-matched rule files for release notes, PR replies, postmortems, tickets, technical articles, and long-form journalism.
Chinese text gets a separate calibration file across four evidence layers, including a measured corpus of about two thousand Taiwanese news articles.
Every rule traces to a research ledger in the repo that digests fifteen studies, led by StoryScope (arXiv:2604.03136, 61,608 stories, 93.2% macro-F1 from narrative features alone), with per-model fingerprints that name which vendors published guidance and which were merely consulted.
The structural finding has a professional-prose arm too: a 2026 StoryScope replication on 2,250 company blog posts against 11,250 AI mirrors separated them at 97.0 macro-F1 from structural features alone, nearly unchanged when every AI post was reworded by its own model (arXiv:2609.15369 v3; the repo's ledger still quotes the earlier revision's 98.0).
Install is `npx skills add Nanako0129/sepia -g` or a native plugin marketplace, and the repo runs CI workflows for behavioral evals and version consistency.

## Status

Active and early: 3,155 stars and 198 forks as of 2026-10-13, main unchanged since the v0.12.4 release (2026-10-15, still the latest tag) with the repo's pushed date moving to 2026-10-30 on pull-request branch activity and bot review, seven open issues as of 2026-10-31, created 2026-08-28.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Nanako0129/sepia&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Nanako0129/sepia&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Nanako0129/sepia&type=date&legend=top-left" />
</picture>

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
- Star velocity on a weeks-old repo is a distribution signal, not a quality verdict, and the zero-HN-footprint cuts both ways.

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
- 2026-10-07 - The repo resumed activity after the 09-23 quiet stretch: v0.12.3 shipped 2026-10-06 as the latest tag, and the Status figures moved to 3,007 stars and seven open issues.
- 2026-10-11 - The README's native plugin packaging list gained QwenPaw (Claude Code, Codex, Grok Build, Antigravity, and QwenPaw now ship native packaging); v0.12.3 is still the latest release and the figures refreshed to 3,079 stars.
- 2026-10-16 - v0.12.4 shipped 2026-10-15 (a professional-recreate stance fix and QwenPaw `/sepia` dispatch changes) and is now the latest release; the Status and reference lines re-dated.
- 2026-10-25 - Rotation re-verification: every cited URL re-fetched live and the zero-HN search re-run (still only unrelated sepia stories), with the repo unchanged since 2026-10-15 (v0.12.4 still latest, five open issues). The What-it-is section picked up what the README carries and the note lacked: the sixth professional-prose domain (long-form journalism), the voice profiles beyond Hemingway (a Taiwan journalism voice and author-defined personas), and the professional-prose StoryScope replication (arXiv:2609.15369), whose current v3 reports 97.0 macro-F1 where the repo's ledger quotes the pre-v3 98.0.
- 2026-10-31 - Volatile refresh: main is unchanged since v0.12.4 and the release held, while the repo's pushed date moved to 2026-10-30 on pull-request branch activity and a CodeRabbit review (no main-line change), and open issues moved to seven.

## See also

- [The Tells Are Structural](../../the-tells-are-structural/index.md) - the corpus essay that makes the same structural-tells argument sepia operationalizes
- [Agent-Native](../agent-native/index.md) - the other curated pack in this category, workflow breadth versus sepia's single-skill depth
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the packaging standard sepia targets
- [skills.sh](../skills-sh/index.md) - the registry whose CLI gives sepia its 77+ agent reach
- [SkillOpt](../skillopt/index.md) - training skill text against held-out validation, a research answer to sepia's unscored calibration

## References

- https://api.github.com/repos/Nanako0129/sepia - 3,155 stars and 198 forks as of 2026-10-13, MIT, main unchanged since 2026-10-15 with latest tag v0.12.4 and the pushed date at 2026-10-30 on non-main activity, seven open issues as of 2026-10-31 (200, re-fetched 2026-10-31)
- https://raw.githubusercontent.com/Nanako0129/sepia/main/README.md - operations, three-pass protocol, research ledger, per-platform verification limits (200, re-fetched 2026-10-25)
- https://hysenlabs.com/en/projects/nanako0129-sepia - third-party editorial review (September 10, 2026) with critical sections on calibration and wrong-tool cases (200, re-fetched 2026-10-25)
- https://arxiv.org/abs/2604.03136 - StoryScope: 61,608 stories, 93.2% macro-F1 from narrative features alone, v6 revised 2026-08-10 (200, re-fetched 2026-10-25)
- https://arxiv.org/abs/2609.15369 - SlopShape, the professional-prose replication the ledger cites: 2,250 company blog posts against 11,250 AI mirrors, 97.0 macro-F1 from 176 structural features alone and 96.1 under self-rewording (v3, 200, fetched 2026-10-25)
- https://hn.algolia.com/api/v1/search?query=sepia&tags=story - the zero-hit search behind the missing-footprint statement (200, re-run 2026-10-25, still only unrelated sepia stories)
- https://old.reddit.com/r/ClaudeAI/comments/1w2g7za/i_turned_the_storyscope_paper_into_a_deai_writing/ - the maintainer's launch thread, fetch blocked with 403 (re-tried 2026-10-25, still 403), cited for existence only
