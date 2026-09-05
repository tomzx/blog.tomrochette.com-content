---
title: SkillOpt
created: 2026-08-30
updated: 2026-09-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, skills, self-improving-agents, research, microsoft]
readability: 3
audience_notes: >
  Engineers who maintain skill files for LLM agents and wonder whether those files can be trained instead of hand-written.
  Assumes you know what a held-out validation set and a SKILL.md are.
---

SkillOpt is a Microsoft Research text-space optimizer that trains a reusable natural-language skill document for a frozen LLM agent the way deep learning trains weights: trajectory-driven bounded edits, a textual learning rate, and a held-out validation gate, exporting a deployable `best_skill.md`.
Facts below verified as of 2026-09-05.

**SkillOpt turns the skill file into a trainable parameter, and the part that matters is not the optimization loop but the gate: an edit is kept only when it strictly improves a held-out score, which is exactly the discipline hand-written skills never get.**

## What it is

A Python package (`skillopt` on PyPI) where the target model runs scored rollout batches with the current skill, a separate optimizer model proposes bounded add, delete, and replace edits, an edit budget clips each step, and candidates are accepted only on strict validation improvement, with rejected edits feeding a negative-feedback buffer.
The deployable artifact is one compact markdown file, median around 920 tokens, consumed by the unchanged target model with zero extra inference-time calls.
The paper reports best or tied-best results across six benchmarks, seven models, and three harnesses, including runs through Codex CLI and Claude Code, with skills transferring across model scales and between harnesses.
CLI tooling, a Gradio dashboard, multiple chat backends, and v0.2.0 integration shells for Claude Code, Codex, Copilot, Devin, and OpenClaw; a nightly SkillOpt-Sleep mode harvests and consolidates behind the same gate.
MIT, from Microsoft Research Asia with university collaborators, Python 3.10+.

## Status

Research code with unusually strong product trappings: 16,697 stars, 1,571 forks, 39 open issues as of 2026-09-05, created 2026-05-08, pushed 2026-08-29.
Latest release v0.2.0 (2026-07-02) on PyPI; the arXiv paper (2605.23904) is a preprint with no peer-reviewed venue found, and all headline results are the authors' own.

## Strengths

- Validation-gated by construction, and the ablations show why: an ungated rewrite pushed one benchmark score down.
- The artifact is small, auditable markdown, so trained skills remain readable and reviewable as practitioner rules.
- Documented transfer across model scales and between Codex and Claude Code, which is what makes the artifact worth training at all.
- A working ecosystem: PyPI releases, multi-backend support, and third-party adoptions within months.

## Cautions

- The guarantee is only as good as the automatic scorer: open-ended or subjective tasks weaken the gate, which the authors acknowledge.
- Optimization is not free; training reached hundreds of millions of tokens on academic benchmarks, with community-quoted costs of a few dollars per task plus the engineering cost of a verifier and a representative held-out split.
- Single-document scope: it trains one skill file, not a skill library.
- All results are self-reported on the authors' benchmarks; no independent replication was found as of 2026-09-05.

## Pricing

Free and open source under MIT.
The costs are training-time tokens on your own API budget and the verifier engineering.

## Compared to

- [Anthropic Agent Skills](../anthropic-agent-skills/index.md): hand-authored SKILL.md folders, free to write but unvalidated; a natural workflow is hand-authoring a seed and letting SkillOpt train it against scored tasks.
- [Agent Skills open standard](../agent-skills-open-standard/index.md): the portability layer; SkillOpt's output is standard-compatible markdown, so trained artifacts slot into ordinary skill folders.
- [Ouroboros](../ouroboros/index.md): wraps whole build loops with verification gates; SkillOpt distills experience into one portable artifact, and the two address different layers of self-improvement.

## Bottom line

**Recommended for teams that already have scored tasks and a verifier, who want their skill files to earn their place empirically.**
Not for subjective domains without reliable scoring, or anyone expecting trained-skill magic without building the evaluation harness first.

## See also

- [Skills Feature Matrix](../skills-feature-matrix/index.md) - the category comparison this note joins
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the format it trains artifacts for
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the portability layer
- [Ouroboros](../ouroboros/index.md) - the loop-level counterpart in self-improvement

## References

- https://github.com/microsoft/SkillOpt - repository, method, benchmarks, license
- https://arxiv.org/abs/2605.23904 - the paper behind the method and results
- https://microsoft.github.io/SkillOpt/ - project page, ablations, and transfer numbers
- https://www.microsoft.com/en-us/research/blog/skillopt-agent-skills-as-trainable-parameters/ - the MSR blog on skills as trainable parameters
- https://github.com/microsoft/SkillOpt/releases/tag/v0.2.0 - release status and harness integrations
- https://venturebeat.com/orchestration/microsofts-open-source-skillopt-automatically-upgrades-ai-agent-skills-without-touching-model-weights - the interview with cost figures and the scorer caveat
- https://the-decoder.com/microsofts-skillopt-boosts-gpt-5-5-by-using-nothing-but-a-trained-markdown-file/ - coverage noting the acknowledged limitations
