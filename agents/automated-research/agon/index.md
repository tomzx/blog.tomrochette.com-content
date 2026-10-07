---
title: Agon
created: 2026-09-27
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=deepseek-v4.1-flash, llm=glm-5.3-flash, automated-research, multi-agent, autonomous-research, claude-code]
readability: 3
audience_notes: >
  Engineers and researchers studying fully autonomous research loops and their failure modes.
  Assumes you know what a coding agent, a multi-agent loop, and adversarial review are.
---

Agon is an MIT-licensed Claude Code plugin that runs producer-critic agent loops from a one-line research topic to running experiments and a paper draft, with no human-written experimental code.

**Agon's bet is that the reusable loop, not the task-specific prompt, is the unit of automation: eighteen roles and a 230 KiB prompt surface carry it across more domains than competitors several times larger, and its most useful output may be the failure taxonomy that marks where the loops stop and a human must start.**

## What it is

Agon is a research orchestrator distributed as a Claude Code plugin, written in Python and released under MIT by AutoResearch-Factory, a group led by Haizhao Yang at the University of Maryland with collaborators at the Chinese University of Hong Kong and Stanford.
A run advances a project through factories: idea, proposal, experiment, and paper.
Each factory is an adversarial producer-critic loop, where one agent creates an artifact and an independent critic on a fresh context (where possible on a different model) tries to break it before the artifact advances.
Handoffs go through files on disk, so a run is recoverable and auditable.
It runs from a separate data workspace (commonly `agon-artifacts`) through the commands `/idea-tick`, `/proposal-tick`, `/experiment-tick`, and `/deep-lit-tick`, and expects `--dangerously-skip-permissions` because the loops are meant to run unattended for hours; the author recommends a dedicated machine, container, or user account.

## Status

Active and small: 54 stars, 5 forks, 1 open issue, 76 commits, created 2026-06-18, last push 2026-09-30, as of 2026-10-03.

<a href="https://www.star-history.com/?repos=AutoResearch-Factory%2FAgon&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=AutoResearch-Factory/Agon&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=AutoResearch-Factory/Agon&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=AutoResearch-Factory/Agon&type=date&legend=top-left" />
 </picture>
</a>

The companion arXiv paper ([2606.24177](https://arxiv.org/abs/2606.24177)) was submitted 2026-06-23 and reports 444 iterations of Prompt Economy loops across more than ten scientific domains, thousands of scientist-coder-auditor iterations over three months, and a longest uninterrupted run the project page puts at 30 days.
**That adoption record is self-reported by the authors with no independent replication, and the public community footprint is essentially absent: an HN Algolia search for Agon autonomous research returns zero hits as of 2026-10-02.**

## Strengths

- A small, inspectable prompt surface: 18 roles and 230.6 KiB of prompts, against roughly 110 roles and 302.4 KiB for AI Scientist v2, 79 roles and 1,157.4 KiB for ARIS, and 78 roles and 1,297.5 KiB for AutoResearchClaw, by the paper's own count.
- Artifact-mediated handoffs make a long unattended run recoverable and auditable, which most research-agent demos do not attempt.
- The paper is unusually candid about failure modes, publishing a 22-entry taxonomy along severity, fixability, visibility, and capability locus instead of only headline results.
- Domain-agnostic by design: field knowledge enters through literature and injected skills, so the same core roles transfer across fields.
- It is an open template rather than a service, so its loops can be copied into a private pipeline today.

## Cautions

- It runs on Claude Code with permissions disabled; treat it as untrusted autonomous code and isolate it accordingly.
- 53 stars, one main repository, and no independent evaluation; the 444-iteration and ten-domain claims rest on the authors' word.
- The paper's own taxonomy concedes invisible failures (anomaly blindness, plausible false attribution, premature abandonment) that no loop catches and only a human scientist can.
- It is a research artifact, not a maintained product: no releases, no support commitment, and a plugin that tracks Claude Code's moving extension points.
- Novelty collisions are an explicit risk it manages through a deep-literature loop, which the paper concedes can still miss the 101st paper.

## Pricing

Agon is free and open source under MIT; there is no paid tier, so pricing does not apply.
Running it costs whatever the underlying model calls cost.

## Compared to

- [OpenAI Deep Research](../openai-deep-research/index.md): a productized web-research agent that writes cited reports; choose Agon when you need code-executing experiments, Deep Research when you need a fast literature answer.
- [Anthropic Claude mathematical research](../anthropic-claude-math/index.md): a bespoke Claude Code subagent loop aimed at one hard problem; Agon is the reusable harness that generalizes that pattern across fields.
- [Harmonic Aristotle](../harmonic-aristotle/index.md): a theorem prover whose output a Lean kernel checks; choose Aristotle when correctness must be machine-verified, Agon when the loop must produce and run experiments without a formal verifier.
- [Pion](../pion/index.md): agents running a real business judged by a bank account; Agon is judged by adversarial critics plus a human, a weaker but cheaper oracle.

## Bottom line

**Recommended for researchers and tool builders studying fully autonomous research loops and the failure-mode boundary, and for teams wanting an inspectable template for producer-critic pipelines.**
Not for anyone who needs a supported product, formal guarantees, or verified benchmark results.

## Changes

- 2026-09-27 - Created.
- 2026-10-07 - Added the AutoResearch-Factory/Agon star history chart to the Status section.

## See also

- [OpenAI Deep Research](../openai-deep-research/index.md) - the prose-output research loop Agon trades citations for experiments against
- [Anthropic Claude mathematical research](../anthropic-claude-math/index.md) - the bespoke subagent loop Agon generalizes into a reusable harness
- [Harmonic Aristotle](../harmonic-aristotle/index.md) - the formally verified counterpart
- [Pion](../pion/index.md) - the other column whose judge is not a machine verifier
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/AutoResearch-Factory/Agon - repository, plugin layout, commands, license, and install requirements
- https://raw.githubusercontent.com/AutoResearch-Factory/Agon/HEAD/README.md - the factory workflow, mandated Claude Code settings, and the multi-model wrapper
- https://arxiv.org/abs/2606.24177 - abstract, authors, submission date, and the 444-iteration and taxonomy summary
- https://arxiv.org/html/2606.24177v1 - design principles, architecture, prompt-surface comparison, and the failure-mode taxonomy
- https://haizhaoyang.github.io/research/autoresearch.html - project-page framing, the six principles, and the 30-day unattended run
- https://api.github.com/repos/AutoResearch-Factory/Agon - stars, forks, creation and push dates, and MIT license for the as-of status
- https://hn.algolia.com/api/v1/search?query=%22Agon%22%20autonomous%20research - the absent community footprint as of 2026-10-02
