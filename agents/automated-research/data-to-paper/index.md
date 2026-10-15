---
title: data-to-paper
created: 2026-10-15
updated: 2026-10-15
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, research-agent, traceability, open-source]
readability: 3
audience_notes: >
  Engineers comparing automated research loops on how verifiable their outputs are, and anyone building data-analysis agents that need audit trails.
  Assumes you know what an LLM agent pipeline is.
---

data-to-paper is the Technion Kishony lab's MIT-licensed pipeline that takes an annotated dataset and walks interacting LLM and rule-based agents through the full research path to a manuscript whose every number can be traced back to the code line that produced it.

**Its judging mechanism is the artifact itself: data-chaining programmatically links every result, method, and dataset reference in the manuscript back through the analysis code to the data, which makes verification a property of the document rather than a review pass.**

## What it is

A Python package (`pip install data-to-paper`, MIT) from Tal Ifargan, Lukas Hafner, Maor Kern, Ori Alcalay, and Roy Kishony at Technion's Kishony lab, published in NEJM AI in December 2024 after an April 2024 arXiv preprint.
In autopilot mode it raises hypotheses, plans the research, writes and debugs analysis code, generates and interprets results, and writes a complete paper from annotated data alone.
In copilot mode a human oversees every step through the Copilot App: reviewing, rewinding to prior stages, replaying recorded runs, and tracking API costs.
Rule-based agents hold the pipeline's structure while LLM agents write the code and prose, and standard statistical packages are overridden with coding guardrails to catch common LLM analysis errors.

## Status

Dormant but installable: 829 stars, created 2023-06-17, last push 2025-07-19, which is also the day PyPI took v1.1.22, the package's thirteenth release, as of 2026-10-15.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Technion-Kishony-lab/data-to-paper&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Technion-Kishony-lab/data-to-paper&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Technion-Kishony-lab/data-to-paper&type=date&legend=top-left" />
</picture>

The May 2024 Show HN thread reached 139 points with 15 top-level comments, the strongest community-tier launch footprint in this category's records, and a December 2024 follow-up thread marked the NEJM AI publication.

## Strengths

- Data-chaining is a mechanism no other member ships: the manuscript's numbers, methods, and data references are programmatically linked, so any claim click-traces to the exact code and data that produced it.
- NEJM AI peer review is external validation most of this category's community tier never gets; FutureHouse Robin's Nature paper is the only stronger credential here.
- The paper grades itself honestly: simple goals recapitulated peer-reviewed publications without major errors in about 80 to 90 percent of autonomous runs, and the authors call the research novelty "relatively limited".
- Copilot mode records oversight in the loop itself, with rewinds and replays that make a run auditable after the fact.

## Cautions

- Dormant since July 2025 with no release since, so the pipeline targets 2024-era models and has not followed the harness ecosystem's moves.
- Complexity is the wall, by the authors' own reading: accuracy held only for simple goals, and human co-piloting "becomes critical" as the research question grows.
- The launch thread's sharpest reply names the statistical hazard: raising hypotheses from the same data the manuscript then publishes is automated p-hacking unless confirmatory data follows, and the framework's open-goal mode does exactly that.
- The scope is data analysis, not discovery: public-health, social-network, and clinical datasets, with recapitulation rather than novelty as the demonstrated product.

## Pricing

Free and open source under MIT; there is no paid tier, so pricing does not apply.
Costs are your own LLM API keys, with per-run cost tracking built in.

## Compared to

- [Agent Laboratory](../agent-laboratory/index.md): the other human-assisted academic ancestor; Agent Laboratory is paper-first from a supplied idea, data-to-paper is data-first and traces every number it prints.
- [AiScientist](../aiscientist/index.md): reproduction as the unit of work on PaperBench; data-to-paper recapitulates publications from raw data instead of re-running a published pipeline.
- [Mole](../mole/index.md): the other enforcement-first member; mole polices a run's budget and quotes while it runs, data-to-paper chains a manuscript's content after it is written.

## Bottom line

**Recommended for engineers building data-analysis agents that need audit trails: the data-chaining mechanism is worth stealing even where the 2024-era pipeline is not.**
Not for novelty-seeking discovery runs, which the authors themselves score as the framework's weak output.

## Changes

- 2026-10-15 - Created.

## See also

- [Agent Laboratory](../agent-laboratory/index.md) - the other academic ancestor this note sits beside in the lineage
- [AiScientist](../aiscientist/index.md) - the reproduction-track neighbor with File-as-Bus coordination
- [Mole](../mole/index.md) - the enforcement-first sibling at the deep-research tier
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/Technion-Kishony-lab/data-to-paper - repository, MIT license, features, example datasets, and the NEJM AI citation (fetched 200, 2026-10-15)
- https://api.github.com/repos/Technion-Kishony-lab/data-to-paper - 829 stars, created 2023-06-17, last push 2025-07-19, MIT, for the as-of status (fetched 200, 2026-10-15)
- https://raw.githubusercontent.com/Technion-Kishony-lab/data-to-paper/main/README.md - the data-chaining description, autopilot and copilot modes, coding guardrails, and the example manuscripts (fetched 200, 2026-10-15)
- https://pypi.org/pypi/data-to-paper/json - package version 1.1.22 uploaded 2025-07-19, thirteen releases in the train (fetched 200, 2026-10-15)
- https://arxiv.org/abs/2404.17605 - the preprint abstract: the 80 to 90 percent recapitulation figure, the limited-novelty admission, and the co-piloting caveat (fetched 200, 2026-10-15)
- https://doi.org/10.1056/AIoa2400555 - the NEJM AI paper of record (Ifargan, Hafner, Kern, Alcalay, Kishony); the page returned 403 to this run's fetch (Cloudflare), so publication facts are grounded in the repository's citation and the preprint (recorded 403, 2026-10-15)
- https://hn.algolia.com/api/v1/items/40331850 - the 139-point Show HN thread: the p-hacking critique, the paper-mill concern, and the authors' responsibility disclaimer (fetched 200, 2026-10-15)
