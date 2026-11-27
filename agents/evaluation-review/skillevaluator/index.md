---
title: SkillEvaluator
created: 2026-11-24
updated: 2026-11-27
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.4, evaluation, agent-skills, ci, quality-gate, live-evaluation]
readability: 3
audience_notes: >
  Engineers who author agent skills or plugins and want a gate that says whether a skill is well-formed, safe, loads in each harness, and actually helps an agent.
  Assumes you know what a SKILL.md folder is, what an LLM-as-a-judge score is, and what a Docker sandbox is.
---

SkillEvaluator is NVIDIA's Apache-2.0 multi-tier framework that evaluates AI agent skills and plugins, from keyless static quality gates and a harness-load check up to a live agent trial run with and without the skill, and it ships CI templates that gate every skill change on the static tiers.

**Its bet is that scanning a skill cannot tell you whether the skill helps an agent, so the tiers climb from free deterministic checks to a paired live trial whose difference, Skill Lift, is the only answer to the deployment question; the authors' own study found the structural and judged scores barely correlate (Spearman 0.14).**

## What it is

A Python 3.12 to 3.14 CLI (`pip install skillevaluator`, or `uv tool install`) from NVIDIA, running a three-tier pipeline over a skill folder, a plugin, or another capability package.
Tier 1 validation needs no model key: a quality score out of 100 with a passing threshold of 70 by default, schema, version, PII, license, Unicode, and script linting, plus Harness Check, which predicts from versioned profiles whether Claude Code, Codex, Copilot CLI, Hermes, OpenClaw, and OpenCode will load, degrade, or drop the skill.
Security and code-integrity checks in Tier 1 run through SkillSpector, Gitleaks, Bandit, optional Semgrep, and opt-in pip-audit, and the README counts 500-plus static rules and detection patterns across 11 CI checks.
Tier 2 deduplication uses embeddings and chat to find guidance that repeats inside a skill or overlaps a catalog.
Tier 3, the live evaluation, takes a reviewed dataset, runs a supported agent (Claude Code, Codex, or OpenCode, with Hermes experimental) in a Harbor sandbox once with and once without the skill, grades both arms, and reports Skill Lift.
`skillevaluator validate` runs the tiers together: Tier 1 always gates the exit code, Tier 2 gates unless `--no-block-on-dedup` is set, and Tier 3 gates only with `--block-on-agent-eval`.
`skillevaluator ci init` wires a GitHub repository through a setup pull request, GitLab takes a copied CI template, and `npx skills add NVIDIA/SkillEvaluator` installs the agent skill.
It is part of NVIDIA's Verified Skills pipeline and the NVIDIA/skills catalog, and its README declares the support level Experimental: community-supported, best effort, no SLA.

## Status

Active, young, and heavily starred: 4,453 stars and 565 forks as of 2026-11-24, 38 open issues and pull requests, Apache-2.0, repository created 2026-06-24 and pushed 2026-11-26 (repository-level; the default branch's latest commit is 2026-11-25, requiring SkillSpector 2.13.7 or newer, PR 901, adding PR comments on the stable channel, PR 899, and Tier 1 and Tier 2 artifact scanning and reporting, PR 897).
The published train is v1.2.1 (2026-11-25, the verified 1.2.1 CI bundle with matching scanner, workflow, and CLI pins, a locked Tier 2 CI container with credential-free build verification, and Tier 3 paired-case lift estimates with a 95% bootstrap interval and pass^k beside pass@k on multi-attempt runs) after v1.2.0 (2026-11-24, reviewed hook approvals, a GitHub Actions annotations report format, and more reliable agent evaluation) after v1.0.1 (2026-11-18, its first 1.0-series release, carrying Harness Check, a NeMo Gym backend, and improved agent-assisted evaluation and repository CI), a day after v1.0.0 (2026-11-17, marked superseded) and five days after v0.9.0 (2026-11-13), after v0.8.0 (2026-11-06) and v0.7.0 through v0.7.2 (2026-11-02 to 2026-11-04), with PyPI tracking 1.2.1.
The 1.1-series tags stayed unreleased: release-preparation commits for v1.1.0, v1.1.1, and v1.2.0 landed on 2026-11-23 (a GitHub Actions annotations report format, operator host and hook URL allowlists), and v1.2.0 then published to GitHub Releases and PyPI on 2026-11-24, after the note's same-day read, with the v1.1.0 and v1.1.1 tags carrying no GitHub release or PyPI publish as of 2026-11-25.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=NVIDIA/SkillEvaluator&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=NVIDIA/SkillEvaluator&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=NVIDIA/SkillEvaluator&type=date&legend=top-left" />
</picture>

The paper behind it (arXiv 2608.20614, submitted 2026-08-20, with versions accepted at the Agent Skills '26 workshop at ACM CAIS 2026 and orally at a KDD 2026 workshop on enterprise AI agents) reports 947 scored paired cases from 58 production skills on four harnesses: mean composite Skill Lift 0.2134 with a 95 percent confidence interval of 0.1967 to 0.2301, positive in 72.8 percent of paired cases.
**The footprint outside NVIDIA is thin: Hacker News holds one 5-point, zero-comment submission of the paper (2026-08-30) and no thread on the tool, so the stars rest on the vendor's channels, and the adoption evidence is the vendor's own account of partner pilots (OpenClaw's ClawHub Evals tab and Nous Research's Hermes Agent install flow).**

## Strengths

- The question ladder is well ordered: safe and well-formed, then loadable, then distinct, then useful, with each tier runnable alone and the validation and loadability checks free.
- Harness Check prices a failure nothing else here measures: a specification-valid skill that one loader silently drops, predicted in about a second with no key.
- The live tier is a paired experiment under one prompt, model, task inputs, and grading criteria, so Skill Lift isolates the skill the way FrontierHarness Eval isolates the harness.
- Fail-closed defaults: a missing, timed-out, or crashed scanner leaves its check INCOMPLETE and `validate` exits non-zero instead of passing quietly.
- Reusable CI templates for GitHub and GitLab, the GitHub one wired by a guided `ci init` setup pull request, so there is no evaluation code to maintain.

## Cautions

- **The headline numbers are the vendor scoring its own catalog: the launch post's 300-plus verified skills ran on NVIDIA-generated tasks, 85 percent of them in a single attempt, and the post reports no confidence intervals.**
- Discoverability and Efficiency are scored against the skill itself, so they cannot read low without it (baselines of 42 and 43 of 100); the post says so, and their lifts of 40 and 35 points mean the skill activated, not that unaided behavior improved.
- The authors' study found structural and LLM-judge scores barely correlate (Spearman 0.14), so a green Tier 1 says nothing about Skill Lift; the answer lives in Tier 3, which bills model tokens and needs Docker and a reviewed dataset.
- Harness Check predicts from versioned profiles, each finding naming the harness version it was verified against, so it goes stale as harnesses release, and by default it never fails a run.
- Support is Experimental, the 1.0 line is six days old as of 2026-11-24, and main's release-preparation commits already sit two minor versions ahead of the published train.
- Tier 3 results depend on pinned agent versions (Claude Code 2.1.292, Codex 0.161.0, OpenCode 1.19.5 per the docs fetched 2026-11-24), and the default NVIDIA Build path runs OpenCode, so a lift measured here is a pairing, not a skill property.

## Pricing

Free and Apache-2.0, with no hosted tier of its own; the keyless Tier 1 and Harness Check cost nothing to run.
Tier 2 and Tier 3 bill your provider: eligible NVIDIA Developer Program members get free prototyping on NVIDIA-hosted endpoints subject to access terms and rate limits, and the docs warn that model and managed-sandbox usage can incur charges.

## Compared to

- [SkillSpector](../../skills/skillspector/index.md): the security scanner that is SkillEvaluator's Tier 1 security check and a member of the skills category; run SkillSpector alone for a pre-install verdict on a third-party skill, SkillEvaluator when you author the skill and also want its quality, loadability, and effect measured.
- [Harbor](../harbor/index.md): the neutral runner that executes the Tier 3 sandboxes; choose Harbor directly when you bring your own tasks and grading, SkillEvaluator when the object is a skill and the paired design is the point.
- [agent-qa](../agent-qa/index.md): a QA agent judging the app on screen from plain-English journeys; SkillEvaluator judges the skill artifact and its effect on an agent's task results, not the user interface.
- [deepeval](../deepeval/index.md): a pytest-style framework where you write the metrics; SkillEvaluator ships its rubric for one artifact type, so it needs no eval code but says nothing outside that rubric.

## Bottom line

**Recommended for teams that ship skills or plugins through CI and want every change checked for quality, safety, and harness loadability for free, with a paired live trial available when a skill's value is in dispute.**
Not for anyone who wants an independent verdict on a skill, since the publisher scores its own catalog, or a stable interface, given Experimental support and a six-day-old 1.0 line.
My disagreeable claim: Harness Check will matter to more teams than Skill Lift, because a skill a loader silently drops scores zero everywhere and costs nothing to detect, while the lift measurement needs a model key, Docker, and a reviewed dataset before it says anything.

## Changes

- 2026-11-24 - Created from the coordinator's automated-research handoff, admitted as the category's skill-and-plugin evaluation gate beside the app-level acceptance harness.
- 2026-11-25 - Recorded the v1.2.0 release (published to GitHub Releases and PyPI 2026-11-24, after the note's same-day read: reviewed hook approvals, GitHub Actions annotations, and more reliable agent evaluation; the v1.1.0 and v1.1.1 tags stay unreleased) and refreshed the activity line (the default branch's latest commit 2026-11-25).
- 2026-11-27 - Recorded the v1.2.1 release (2026-11-25: the verified CI bundle with matching pins, a locked Tier 2 CI container, and Tier 3 paired-case lift estimates with a 95% bootstrap interval) and refreshed the activity line (the default branch's latest commit 2026-11-25).

## See also

- [Harbor](../harbor/index.md) - the neutral benchmark runner that executes the live tier's sandboxed trials
- [SkillSpector](../../skills/skillspector/index.md) - the security scanner inside Tier 1, profiled in the skills category
- [Anthropic Agent Skills](../../skills/anthropic-agent-skills/index.md) - the vendor framing of skills as untrusted inputs that motivates gating them before install
- [agent-qa](../agent-qa/index.md) - the other vendor-run evaluation in the category, judging the app surface instead of the skill
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/NVIDIA/SkillEvaluator - repository: README, the three-tier pipeline, the gate rules, CI templates, the Experimental support level, and NVIDIA Verified Skills membership (fetched 2026-11-24)
- https://api.github.com/repos/NVIDIA/SkillEvaluator - 4,453 stars and 565 forks as of 2026-11-24, 38 open issues and pull requests, Apache-2.0, created 2026-06-24, pushed 2026-11-23
- https://api.github.com/repos/NVIDIA/SkillEvaluator/releases - the release train: v1.2.0 (2026-11-24), v1.0.1 (2026-11-18), v1.0.0 (2026-11-17, superseded), v0.9.0 (2026-11-13), back to v0.1.0 (2026-08-05), and main's 2026-11-23 release-preparation commits for v1.1.0, v1.1.1, and v1.2.0
- https://pypi.org/pypi/skillevaluator/json - 1.0.1 published 2026-11-18, Python 3.12 to 3.14
- https://docs.nvidia.com/skills/skillevaluator/ - the documentation hub: the tiers, Apache-2.0, the Experimental support statement, and NVIDIA Verified Skills
- https://docs.nvidia.com/skills/skillevaluator/tier1-reference - the Tier 1 checks, the 70 passing threshold, the gate rules (Tier 1 always gates, Tier 3 advisory by default), and the INCOMPLETE rule for missing or crashed scanners
- https://docs.nvidia.com/skills/skillevaluator/harness-check - Harness Check: six harnesses, versioned profiles, no pass or fail change by default
- https://docs.nvidia.com/skills/skillevaluator/tier3-live-evaluation - the live tier: a reviewed dataset, with-and-without runs in Docker, the Skill Lift report, and the NeMo Gym backend note
- https://docs.nvidia.com/skills/skillevaluator/agents-and-sandboxes - the supported agents and their pinned versions
- https://docs.nvidia.com/skills/skillevaluator/cli-onboarding - the GitHub `ci init` wizard (setup pull request, admin access) and the GitLab template path
- https://arxiv.org/abs/2608.20614 - the ACES paper: 947 paired cases, mean composite Skill Lift 0.2134, and the structural-versus-judge Spearman of 0.14
- https://developer.nvidia.com/blog/evaluating-ai-agent-skill-performance-with-nvidia-skillevaluator/ - the launch post (2026-08-19): the 300-plus verified skills, the five scored dimensions, the single-attempt and missing-confidence-interval limitations, and the partner pilots
- https://hn.algolia.com/api/v1/search?query=Evaluating%20Skills%2C%20Not%20Just%20Agents&tags=story - the 5-point, zero-comment paper submission (2026-08-30), the thin-footprint signal
