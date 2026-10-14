---
title: EvoSkill
created: 2026-10-13
updated: 2026-10-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, skills, skill-discovery, evolution, optimization]
readability: 3
audience_notes: >
  Engineers who hold enough scored tasks to want skills mined from failures instead of hand-written, and who can run a Python CLI.
  Assumes you know what a SKILL.md and a held-out validation split are.
---

EvoSkill is Sentient Labs' Apache-2.0 skill-discovery toolkit: it runs your coding agent over a benchmark, hands the failed trajectories to a proposer, and materializes the proposed fixes as standard SKILL.md skill folders, keeping only the candidates that improve a held-out validation score.

**It is the third optimizer-family column in this category, and its difference from SkillOpt and GEPA is the unit of evolution: where they train or rewrite one text parameter, EvoSkill evolves the whole agent configuration (prompt plus skill set) and can discover skills nobody wrote.**

## What it is

A Python 3.12+ CLI (installed by script or `pip install -e .`) that wraps Claude Code, Codex, OpenCode, OpenHands, Goose, or Harbor as the executor, with any model provider behind it (Anthropic, OpenAI, OpenRouter, Fireworks, and more).
The loop runs three roles: an Executor attempts task batches with the current configuration, a Proposer reads the failed trajectories and proposes one targeted skill, and a Skill Builder writes it as a markdown folder under `.claude/skills/`.
Selection is a Pareto frontier of the top configurations, each pinned as a git branch, so the evolutionary history is a git log you can check out, and a candidate survives only when it improves the held-out score.
Apache-2.0, from Sentient Labs (the sentient-agi org), built on the March 2026 paper (arXiv 2603.02766).

## Status

Quiet since late August: 1,250 stars, 132 forks, and 21 open issues as of 2026-10-13, created 2026-03-04, pushed 2026-08-24, with the release train stalled at v1.3.0 (2026-06-16, the Fireworks provider addition).
The paper and the March 5 blog post are the whole public record, and my searches found no Hacker News story and no independent coverage of the project, so the footprint is the repository itself.
The paper's headline numbers are the authors' own runs: OfficeQA 60.6% to 67.9% exact match with Claude Code (Opus 4.5) on a 10% training subset, SealQA 26.6% to 38.7%, and a 5.3-point zero-shot transfer from SealQA skills to BrowseComp.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=sentient-agi/EvoSkill&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=sentient-agi/EvoSkill&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=sentient-agi/EvoSkill&type=date&legend=top-left" />
</picture>

## Strengths

- **Failure-driven search: proposals are grounded in recorded execution trajectories, so each candidate skill answers a demonstrated capability gap rather than a random mutation.**
- The held-out validation gate is the same discipline that makes SkillOpt trustworthy, and the git-branch frontier makes every accepted and rejected candidate inspectable.
- The output is ordinary SKILL.md folders, so induced skills install anywhere the Agent Skills standard reaches.
- Cross-model and cross-agent by construction, and the transfer result (SealQA skills improving BrowseComp without modification) is the interesting evidence that skill-level optimization produces general capabilities.

## Cautions

- **The project has been quiet for roughly seven weeks (last push 2026-08-24) with one release since June, so treat it as a research artifact that may be ending rather than a maintained tool.**
- Zero community footprint: no Hacker News thread, no independent review, and no third-party benchmark runs found as of 2026-10-13.
- You need a benchmark to run it at all; the README lists benchmark-free evolution as an open direction, so teams without scored tasks get nothing from the loop.
- The README credits the GEPA lineage through the org's own gepa-plus repository rather than the canonical gepa-ai/gepa, so the ancestry is partly self-referential.
- All accuracy gains are self-reported on two QA benchmarks, and the coding-agent framing of the README's title runs ahead of what the paper measures.

## Pricing

Free and open source under Apache-2.0.
There is no hosted tier; evolution runs consume your own model API budget across many scored rollouts, which is the whole cost.

## Compared to

- [SkillOpt](../skillopt/index.md): trains one reusable skill document against scored tasks with a strict edit budget; EvoSkill evolves the whole configuration and discovers new skills, with more freedom and less control.
- [GEPA](../gepa/index.md): the reflective optimizer over any text parameter; EvoSkill extends that feedback-driven idea to joint prompt-plus-skill mutation and adds frontier-of-configurations selection.
- [Agent Skills open standard](../agent-skills-open-standard/index.md): the format EvoSkill's output lands in; the toolkit induces folders, the standard carries them.

## Bottom line

**Recommended for teams that already hold a scored task set worth mining and want to see what skills a machine would write from their failures.**
Not for production skill maintenance (the loop is offline over a fixed dataset and the project is quiet), and not as evidence that auto-generated skills beat hand-written ones, which its benchmarks do not test.

## Changes

- 2026-10-13 - Created from the skills entrant resolution (the mapped awesome-list scan), with the zero-footprint search and the stalled release train recorded as the critical angles.

## See also

- [Skills Feature Matrix](../skills-feature-matrix/index.md) - the category comparison this note joins
- [SkillOpt](../skillopt/index.md) - the validation-gated trainer beside it in the optimizer family
- [GEPA](../gepa/index.md) - the reflective optimizer whose idea it extends
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the format its induced skills land in
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the vendor framing of the skill folders it writes

## References

- https://github.com/sentient-agi/EvoSkill - repository, Apache-2.0, 1,250 stars, 132 forks, 21 open issues, pushed 2026-08-24, install paths and supported agents (GitHub API and README, fetched 2026-10-13)
- https://arxiv.org/abs/2603.02766 - the paper: the three-role loop, the Pareto frontier, and the OfficeQA, SealQA, and BrowseComp numbers (fetched 2026-10-13)
- https://www.sentient.xyz/blog/evoskill-automated-skill-induction-from-agent-failures - the Sentient Labs post: the five-step loop, the git-branch frontier, and the Claude Code Opus 4.5 claim (March 5, 2026, fetched 2026-10-13)
- https://api.github.com/repos/sentient-agi/EvoSkill/releases/latest - v1.3.0 published 2026-06-16, the newest release as of 2026-10-13 (fetched 2026-10-13)
- https://hn.algolia.com/api/v1/search?query=EvoSkill&tags=story - the zero-hit search behind the missing-footprint statement (fetched 2026-10-13)
