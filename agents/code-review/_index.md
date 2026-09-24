---
showArticleList: false
title: Code review
created: 2026-09-24
visible: true
status: in progress
tags: [agents, code-review]
readability: 3
---

Where machines judge pull requests: the review bots, the open-source reviewers, and the one that pivoted into agent infrastructure.

- [CodeRabbit](coderabbit/index.md) - the commercial anchor, $143M Series C at a $1.5B valuation, free forever on public repos, with a disclosed RCE history in its file.
- [Ellipsis](ellipsis/index.md) - the 2024 review bot that pivoted to managed agent infrastructure in July 2026, review now one configurable use case.
- [Graphite Diamond](graphite-diamond/index.md) - the deprecated Diamond reviewer, now Graphite Agent inside Cursor since the December 2025 acquisition.
- [Greptile](greptile/index.md) - AI code review running a swarm of agents over a graph index of your repositories, learned house rules included.
- [Kodus](kodus/index.md) - the AGPL-3.0 open-source reviewer with BYOK and zero token markup, self-hosted or on Kodus Cloud.
- [OpenCodeReview](open-code-review/index.md) - Alibaba's hybrid reviewer where deterministic pipelines pick and rule-check what the LLM agent judges, precision over recall.
- [Qodo](qodo/index.md) - the open-core reviewer, MIT PR-Agent you can self-host or paid Qodo Merge, both sides covered by Kudelski's exploit research.
- [Sourcery](sourcery/index.md) - the MIT-lineage static-analysis tool turned proprietary AI reviewer, free for open source and $12 for private repos.

Its members are compared on shared rows in the [Code Review Feature Matrix](code-review-feature-matrix/index.md).

## Changes

- 2026-08-24 - Added Greptile.
- 2026-08-30 - Added CodeRabbit.
- 2026-08-30 - Added Ellipsis.
- 2026-08-30 - Added Graphite Diamond.
- 2026-08-30 - Added Kodus.
- 2026-08-30 - Added OpenCodeReview.
- 2026-08-30 - Added Qodo.
- 2026-08-30 - Added Sourcery.
