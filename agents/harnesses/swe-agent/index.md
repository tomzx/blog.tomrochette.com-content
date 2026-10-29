---
title: SWE-agent
created: 2026-10-28
updated: 2026-10-28
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, swebench, research, terminal]
readability: 3
audience_notes: >
  Engineers and researchers who want the provenance of the ACI design idea and the reference
  harness behind early SWE-bench records. Assumes you know what SWE-bench is and why a
  maintenance-mode academic harness still matters to the category.
---

SWE-agent is the Princeton and Stanford research harness that introduced the agent-computer interface (ACI) idea, carried the model into a real repository through a constrained shell tool set, and became the reference agent of the early SWE-bench era.

## What it is

An open-source (MIT) Python terminal harness from the SWE-bench team, published with a NeurIPS 2024 paper arguing that interface design, not just model quality, decides agent performance.
The agent works inside a Docker-containerized copy of a repository through a yaml-governed set of tool bundles (an edit-lint flow, search, and a submit gate), and every run leaves a complete `.traj` trajectory file.
It is built and maintained by researchers from Princeton University and Stanford University, sits beside their SWE-bench, SWE-ReX, and SWE-smith projects, and carries an EnIGMA mode for offensive-security capture-the-flag work pinned to the older v0.7 line.

## Status

Maintenance-only by its own declaration, and still the category's most cited ancestor: 20,663 stars on a repository created April 2, 2024, with the default branch pushed October 26, 2026 (GitHub API, as of 2026-10-28).
The newest tagged release is v1.1.0 (May 22, 2025, a training-trajectories drop), and no release has followed in seventeen months, while the docs site and README now carry a standing banner: most development effort moved to mini-swe-agent, which "has superseded SWE-agent", and "SWE-agent is now in maintenance-only mode".
The April 2, 2024 launch thread drew 307 points and 143 comments on Hacker News, and the paper's 12.5 percent SWE-bench pass@1 was the open-source state of the art at publication.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=SWE-agent/SWE-agent&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=SWE-agent/SWE-agent&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=SWE-agent/SWE-agent&type=date&legend=top-left" />
</picture>

## Strengths

- The ACI thesis is the field's clearest statement that harness design is a first-class variable, and the paper's ablations still anchor the argument.
- Everything is yaml: model, templates, history processors, demonstration trajectories, and tool bundles, which makes run configurations reproducible and shareable.
- Model routing through litellm covers essentially every provider including local Ollama-style endpoints, with a custom cost registry for unpriced models.
- Batch mode (`run-batch`) with per-thread API-key rotation was built for benchmark evaluation, and `.traj` outputs make every run auditable.
- Prompt-caching support for Claude via a `cache_control` history processor shows unusual attention to inference cost for an academic tool.

## Cautions

- The project recommends its own replacement: the supersession banner names mini-swe-agent as the going-forward choice, and maintenance-only means no release since May 2025.
- The SWE-bench numbers it rode on are themselves contested: the SWE-Bench+ analysis found solution leakage in 32.67 percent of SWE-Agent+GPT-4's successful patches and weak tests in another 31.08 percent, dropping its measured resolution rate from 12.47 to 3.97 percent.
- The 1.0 rewrite broke the 0.7 configuration surface, and EnIGMA (the security mode) still documents the old version as its supported line.
- No subagents, no MCP, no editor integration: the loop is one model over one shell, by design.

## Pricing

Free and open source under MIT; pricing does not apply.
The cost of running it is your model API spend, which the litellm registry tracks per run.

## Compared to

Mini-SWE-agent is the same team's successor, a deliberately tiny loop with matching SWE-bench performance, and the project's own recommendation for anything new.
OpenHands is the platform-scale research agent, with a self-hostable UI and cloud, where SWE-agent stays a scriptable command-line research instrument.
Claude Code and the other commercial members of this category are production harnesses; SWE-agent is the instrument the category's evaluation culture grew up around.

## Bottom line

Recommended for research on agent-harness design and for reproducible SWE-bench batch runs where the `.traj` records and yaml configs are the point.
Not for daily production coding, where the project itself points you to mini-swe-agent or a commercial harness.

## Changes

- 2026-10-28 - Created from the cross-category handoff resolving SWE-agent/SWE-agent into the harnesses category.

## See also

- [Mini-SWE-agent](../mini-swe-agent/index.md) - the successor this project itself recommends, from the same team.
- [OpenHands](../openhands/index.md) - the platform-scale research agent that grew out of the same benchmark wave.
- [aider](../aider/index.md) - the other pre-2025 open-source harness still in the corpus, stalled for different reasons.
- [Harness Feature Matrix](../harness-feature-matrix/index.md) - the category-wide comparison this note feeds a column into.

## References

- https://api.github.com/repos/SWE-agent/SWE-agent - repository metadata: stars, license, push date, and creation date (as of 2026-10-28)
- https://github.com/SWE-agent/SWE-agent - README: the supersession banner, feature claims, EnIGMA, and the sibling projects
- https://swe-agent.com/latest/ - the documentation home: the maintenance-only banner, news, and doc structure
- https://swe-agent.com/latest/config/models/ - litellm model routing, local models, Claude prompt caching, and key rotation
- https://swe-agent.com/latest/faq/ - local model support, custom tools, multimodal configuration, and `.traj` outputs
- https://swe-agent.com/latest/usage/adding_custom_tools/ - the tool-bundle structure behind the tools row
- https://arxiv.org/abs/2405.15793 - the NeurIPS 2024 paper: the ACI thesis and the 12.5 percent SWE-bench result
- https://arxiv.org/abs/2410.06992 - SWE-Bench+: the critical analysis of SWE-Agent+GPT-4 resolution rates, leakage, and weak tests
- https://hn.algolia.com/api/v1/items/39907468 - the 307-point April 2, 2024 launch thread
