---
title: EvoSkill
created: 2026-10-13
updated: 2026-10-26
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
The v2 line shipped as v2.0.0 on 2026-10-26, tagged on the repo's `v2` branch while `main` stays v1: three Claude Code agents (a plain-language benchmark adaptor, a solver that attempts each task three times in its own container, and one stateful evolver session) installed by cloning the branch, requiring a macOS host and a Daytona account.
Apache-2.0, from Sentient Labs (the sentient-agi org), built on the March 2026 paper (arXiv 2603.02766).

## Status

**The v2 line shipped: v2.0.0 published 2026-10-26, tagged on the `v2` branch, while the default branch stays v1.**
The repo shows 1,250 stars and 132 forks as of 2026-10-13 and 21 open issues as of 2026-10-26, created 2026-03-04, the default branch's last commit 2026-07-06, v1.3.0 (2026-06-16, the Fireworks provider addition) still the last main-line release.
The release body is the tech report's system (arXiv 2610.25931): a benchmark adaptor turns a plain-language benchmark description, data, split, and grader into the run's frozen task list, a solver attempts each task three times in its own container, and one stateful evolver session replaces v1's Proposer and Generator, keeps every epoch's skills, and never sees validation or held-out tasks, with only the last epoch tested once.
The reported numbers are held-out pass rates of 40.4% on SpreadsheetBench v2 (+7.7 points over SkillOpt, the stronger baseline) and 51.6% on tau-bench banking (+5.4), plus a 28.0% to 49.5% self-improvement run with Claude Haiku 5.5 as both solver and evolver, and the evolver cost less per percentage point gained than either baseline's optimizer.
The requirements stay narrow at release: a macOS host, Python 3.12+ with uv, a Daytona account, and Claude access, with a local Docker backend and Linux hosts listed as not yet supported.
The paper and the March 5 blog post are otherwise the whole public record, and my searches found no Hacker News story and no independent coverage of the project, so the footprint is the repository itself.
The v1 paper's headline numbers are the authors' own runs: OfficeQA 60.6% to 67.9% exact match with Claude Code (Opus 4.5) on a 10% training subset, SealQA 26.6% to 38.7%, and a 5.3-point zero-shot transfer from SealQA skills to BrowseComp.

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

- **The release split is the trap: the default branch still serves v1 (its README and install paths describe the single-proposer loop) and v2.0.0 lives on a branch you must clone explicitly, so nothing in the repo's front door tells you which system you are installing.**
- v2's platform support is narrow at release: macOS hosts and Daytona cloud containers only, with a local Docker backend and Linux hosts planned, so Linux-first teams get nothing from v2 today.
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
Not for production skill maintenance (the loop is offline over a fixed dataset and the release line is quiet), and not as evidence that auto-generated skills beat hand-written ones, which its benchmarks do not test.

## Changes

- 2026-10-13 - Created from the skills entrant resolution (the mapped awesome-list scan), with the zero-footprint search and the stalled release train recorded as the critical angles.
- 2026-10-20 - The "quiet and possibly ending" reading reversed: the repo pushed 2026-10-20 on the v2 branch, whose commits carry "EvoSkill v2" and a tech report (arXiv 2610.25931, dated 2026-10-19) describing a stateful single-agent evolver with head-to-head gains over SkillOpt and SkillBoost; nothing tagged or merged to the default branch, so the Status and the quiet-project caution were rewritten around the unreleased-v2 reality.
- 2026-10-26 - Rotation re-verification found the v2 line released: v2.0.0 published 2026-10-26 tagged on the v2 branch (main stays v1), with the benchmark adaptor, container-per-attempt solver, and stateful evolver named in the release body, the SpreadsheetBench v2 and tau-bench banking held-out numbers, and the macOS-plus-Daytona requirements; the Status, What-it-is, and the release-surface caution were rewritten around the shipped-branch reality, and every cited URL was re-fetched live.

## See also

- [Skills Feature Matrix](../skills-feature-matrix/index.md) - the category comparison this note joins
- [SkillOpt](../skillopt/index.md) - the validation-gated trainer beside it in the optimizer family
- [GEPA](../gepa/index.md) - the reflective optimizer whose idea it extends
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the format its induced skills land in
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the vendor framing of the skill folders it writes

## References

- https://github.com/sentient-agi/EvoSkill - repository, Apache-2.0, 1,250 stars, 132 forks as of 2026-10-13, 21 open issues as of 2026-10-26, main still serving the v1 README (GitHub API and README, fetched 2026-10-13, re-fetched 2026-10-26)
- https://arxiv.org/abs/2603.02766 - the v1 paper: the three-role loop, the Pareto frontier, and the OfficeQA, SealQA, and BrowseComp numbers (fetched 2026-10-13, re-fetched 2026-10-26)
- https://arxiv.org/abs/2610.25931 - the v2 tech report: the stateful single-agent evolver, the SkillOpt and SkillBoost comparisons, and the accept-every-epoch change (fetched 2026-10-20, re-fetched 2026-10-26)
- https://github.com/sentient-agi/EvoSkill/tree/v2 - the v2 branch, now carrying the released v2.0.0 system (fetched 2026-10-20, re-fetched 2026-10-26)
- https://github.com/sentient-agi/EvoSkill/releases/tag/v2.0.0 - the release body: the three-agent v2 design, the SpreadsheetBench v2 and tau-bench banking numbers, the clone-the-branch install, and the macOS-plus-Daytona requirements (fetched 2026-10-26)
- https://www.sentient.xyz/blog/evoskill-automated-skill-induction-from-agent-failures - the Sentient Labs post: the five-step loop, the git-branch frontier, and the Claude Code Opus 4.5 claim (March 5, 2026, fetched 2026-10-13, re-fetched 2026-10-26)
- https://api.github.com/repos/sentient-agi/EvoSkill/releases/latest - v2.0.0 published 2026-10-26 on the v2 branch, the newest release; v1.3.0 (2026-06-16) still the last main-line release (fetched 2026-10-13, re-verified 2026-10-20, re-fetched 2026-10-26)
- https://hn.algolia.com/api/v1/search?query=EvoSkill&tags=story - the zero-hit search behind the missing-footprint statement (fetched 2026-10-13, re-run 2026-10-26, still no EvoSkill story)
