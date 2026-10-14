---
title: Kiln
created: 2026-10-10
updated: 2026-10-11
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation-review, evals, fine-tuning, desktop-app]
readability: 3
audience_notes: >
  Engineers and mixed teams (PMs, subject experts, QA) who need to build and rate eval sets without writing code first.
  Assumes you know what an LLM-as-judge metric is and what a golden dataset is for.
---

Kiln is a free desktop app plus an MIT Python library that runs the AI development loop, with evals as the anchor: build judge metrics and datasets in a GUI, rate outputs with non-engineers, then optimize prompts, fine-tune, and generate synthetic data against the same dataset.

**The mechanism this category lacked is the GUI workbench where the whole team rates outputs: deepeval gates in code and Langfuse watches in production, while Kiln is the local-first desktop where a PM rates responses and the same ratings become eval datasets, fine-tuning sets, and optimization targets.**

## What it is

A desktop app for macOS, Windows, and Linux with a one-click installer, plus the MIT-licensed `kiln-ai` Python library and REST server that run the same tasks in notebooks and production (PyPI at 1.2.0, matching the v1.2.0 release of 2026-09-29).
The docs describe judge types across LLM-as-judge, G-Eval, and deterministic code judges for rule-checkable properties, plus RAG Q&A evals and tool-use evals, and the Eval Builder compresses six manual eval-building steps into one interactive flow.
It is local-first: datasets are open JSON on your disk, synced through a git repo you own, with your own API keys or fully offline through Ollama, and the README claims 190+ models tested across providers.
The maker is Chesterfield Laboratories Inc, and the desktop app is source-available under the fair-code model while the library is MIT.

## Status

Active and mature for this category: 5,191 stars, 394 forks, and 56 open issues as of 2026-10-13, created 2024-07-23, pushed 2026-10-14, with the v1.2.0 release published 2026-09-29.
The release train is steady (v1.1.3 on 2026-09-16, v1.1.1 on 2026-08-20), and PyPI tracks the same 1.2.0 version.
The community footprint is thin for the star count: a Hacker News search returns four hits about Kiln, all small (10, 6, 3, and 2 points, the newest from 2025-08-06), so adoption evidence rests on the stars and the installer base rather than independent technical discussion.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Kiln-AI/Kiln&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Kiln-AI/Kiln&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Kiln-AI/Kiln&type=date&legend=top-left" />
</picture>

## Strengths

- Non-engineers can build and rate evals: the GUI exists so PMs, subject experts, and QA rate outputs and add data without a terminal, which no other column in this category offers.
- One dataset flows through the whole loop: the same rated examples drive evals, prompt optimization, fine-tuning, and synthetic data, so a quality regression found in one stage is reusable in the others.
- Git-native and local: datasets are plain JSON in a repo you control, and the app syncs to Git automatically, which keeps the eval set auditable and vendor-portable.
- Auto-Optimize searches prompts, models, tools, skills, subagents, and parameters against your eval dimensions instead of only scoring them.

## Cautions

- The desktop app is source-available fair-code, not open source: you can read and run it, but the license is not OSI-approved, so embedders should check the terms on the `app/` directory before redistributing.
- The headline AI features (Kiln Pro assistant, auto-generated evals, Auto-Optimize) run on the vendor's servers: the free tier is rate limited with standard models, and the enhanced tiers are request-access, so the "local-first" boundary covers your data but not the optimization brain.
- Independent discussion is scarce: four small Hacker News threads in two years is a thin record for a 5.2k-star project, so treat the adoption figure as installer curiosity until you find practitioners writing about production use.
- Scope breadth is a caution as much as a strength: evals, RAG, agents, fine-tuning, synthetic data, and MCP in one app means every one of those surfaces has shallower depth than a dedicated tool.

## Pricing

Individual is free: the MIT library, the source-available desktop app, local datasets with git sync, rate-limited Kiln Pro on standard models, and community support.
Team adds enhanced Kiln Pro models with higher limits, automatic agent optimization, priority access, and email support, priced by request access.
Enterprise adds SSO/SAML, SLA, and procurement support, custom by contact.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-10 | Individual | Recorded at $0, free, rate-limited Kiln Pro included | https://kiln.tech/pricing |
| 2026-10-10 | Team | Recorded as unpriced, request access | https://kiln.tech/pricing |
| 2026-10-10 | Enterprise | Recorded as unpriced, custom by contact | https://kiln.tech/pricing |

## Compared to

- [deepeval](../deepeval/index.md): the code-first framework with roughly fifty judge metrics that gates merges in CI; choose deepeval when the eval suite must live in pytest, Kiln when the team building the evals does not write code.
- [Langfuse](../langfuse/index.md): the observability platform that evaluates traces in production; choose Langfuse for live traffic and regression dashboards, Kiln for building the rated datasets those dashboards need.
- [Workshop](../workshop/index.md): the local debugger where your coding agent writes and runs its own evals; choose Workshop when the agent maintains the suite, Kiln when humans curate it.

## Bottom line

**Recommended for teams whose eval bottleneck is human rating rather than code: the GUI workbench plus git-native datasets is a mechanism the rest of this category does not offer.**
Not for CI gating (deepeval's job), production observability (Langfuse's and Phoenix's), or anyone who needs an OSI-approved desktop license, since the app is fair-code.

## Changes

- 2026-10-10 - Created from the evaluation-review resolution pass, profiling the desktop evals workbench as the category's first GUI column where non-engineers rate outputs.

## See also

- [deepeval](../deepeval/index.md) - the code-first framework this note's GUI contrasts with
- [Langfuse](../langfuse/index.md) - the production side of the same eval lifecycle
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [ReviewBench](../reviewbench/index.md) - the benchmark for judging the judged, a different object than Kiln's datasets

## References

- https://github.com/Kiln-AI/Kiln - repository: README, install paths, license split, model claims
- https://api.github.com/repos/Kiln-AI/Kiln - stars, forks, issues, creation and push dates as of 2026-10-11
- https://api.github.com/repos/Kiln-AI/Kiln/releases - v1.2.0 published 2026-09-29 and the release train
- https://docs.kiln.tech/docs/evaluations - judge types (LLM judges, G-Eval, code judges), Eval Builder, RAG and tool-use evals
- https://kiln.tech/pricing - Individual/Team/Enterprise tiers, Kiln Pro scope, and the local-data claims
- https://pypi.org/pypi/kiln-ai/json - library version 1.2.0 matching the GitHub release
- https://faircode.io - the fair-code model the desktop app's license follows
- https://hn.algolia.com/api/v1/search?query=Kiln%20AI%20evals&tags=story - the thin community-footprint check, four small threads, as of 2026-10-11
