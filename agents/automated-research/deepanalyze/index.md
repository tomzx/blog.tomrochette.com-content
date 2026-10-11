---
title: DeepAnalyze
created: 2026-10-10
updated: 2026-10-10
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, agentic-llm, data-science, open-source]
readability: 3
audience_notes: >
  Engineers choosing an autonomous data-analysis loop and researchers comparing trained agentic models against prompted harnesses.
  Assumes you know what an 8B open-weights model and a code sandbox are.
---

DeepAnalyze is Renmin University of China and Tsinghua's MIT-licensed 8B-parameter agentic LLM, trained to run the data-science research loop end to end, from raw files to an analyst-grade report, with no harness beyond a code sandbox.

**DeepAnalyze is this category's first member whose loop is carried by a trained model rather than a prompted harness: the plan, act, and self-reflect structure is learned in the weights, which makes it the cheapest loop here to run and the only one with no external verifier anywhere in it.**

## What it is

DeepAnalyze-8B, released October 21, 2025 with a paper (arXiv 2510.16872, online October 19), open weights, code, and a 500,000-example instruction dataset (DataScience-Instruct-500K).
Training uses a curriculum-based agentic paradigm that mimics a data scientist's learning trajectory, with training trajectories synthesized from data sources, so the model learns to question, prepare, analyze, model, visualize, and report without workflow code.
Given structured data (databases, CSV, Excel), semi-structured files (JSON, XML, YAML), or unstructured text, it runs open-ended data research and produces analyst-grade reports.
Deployment is `vllm serve DeepAnalyze-8B` plus a WebUI or a Docker-sandboxed WebUI v2, with a hosted API available through HeyWhale key applications.
The authors are Shaolei Zhang, Ju Fan, Meihao Fan, Guoliang Li, and Xiaoyong Du (Renmin University of China with Tsinghua), and the ecosystem has widened: DA-Studio, the system behind WebUI v2, was accepted to the VLDB 2026 demonstration track, CoDA-Bench evaluates code agents on data-intensive analytical tasks, DeepPrep extends the loop to data preparation, and EvoOntology adds a self-evolving ontology layer.
It served as the official agent for the 2026 China Collegiate Computer Design Contest's Big Data track.

## Status

Active: 4,678 stars, 739 forks, created 2025-10-11, last push 2026-09-23, as of 2026-10-10.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ruc-datalab/DeepAnalyze&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ruc-datalab/DeepAnalyze&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ruc-datalab/DeepAnalyze&type=date&legend=top-left" />
</picture>

**The usage footprint is far thinner than the star count: the Hugging Face weights show 203 downloads and 93 likes as of 2026-10-10, and a Hacker News search returns zero stories, so adoption runs through the Chinese data-science community (PaperWeekly, WeChat, the collegiate contest) rather than the Western harness ecosystem.**

## Strengths

- The full loop is open and reproducible: weights, code, and training data, at a size one GPU serves.
- The paper claims it outperforms workflow-based agents built on the most advanced proprietary LLMs at data tasks.
- The ecosystem compounds beyond one repo: a benchmark (CoDA-Bench), a preparation companion (DeepPrep), a VLDB-accepted serving system (DA-Studio), and an ontology layer (EvoOntology).
- Deployment is genuinely self-hosted: vllm on your own GPU, sandboxed execution, no external service required.

## Cautions

- The headline claim is self-reported in the paper's own evaluation, and no independent replication surfaced in this run's searches.
- A single 8B model plans, executes, and judges its own work inside the sandbox, so there is no external verifier anywhere in the loop.
- The project homepage ships with its template placeholders unfilled, thin for a project of the claimed importance.
- 4,678 stars against 203 model downloads and zero Hacker News stories says the stars measure attention, not usage.

## Pricing

Free and open source: MIT-licensed code, open weights on Hugging Face, and no paid tier, so pricing does not apply.
Costs are your own GPU, or a HeyWhale-hosted API key, which is granted by application with no public prices on the fetched pages.

## Compared to

- [GPT Researcher](../gpt-researcher/index.md): the prompted web-research loop that cites the open web; DeepAnalyze is data-grounded and carried by a trained model.
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the keep-or-revert ancestor whose judge is a measured loss; DeepAnalyze's judge is itself.
- [OpenResearch](../openresearch/index.md): the workspace that turns prompted coding agents into researchers; DeepAnalyze collapses the loop into one model you can fine-tune.

## Bottom line

**Recommended for teams that want a self-hosted data-analysis agent they can fine-tune, and for researchers studying learned agentic loops against prompted ones.**
Not for audit-sensitive analysis: the loop's only judge is the model that wrote the analysis.

## Changes

- 2026-10-10 - Created.

## See also

- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the measured-judge ancestor of the loop family
- [GPT Researcher](../gpt-researcher/index.md) - the prompted research-report baseline
- [OpenResearch](../openresearch/index.md) - the workspace implementation of the loop on your own agents
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/ruc-datalab/DeepAnalyze - repository, README, task surface, deployment paths, and the ecosystem news timeline (fetched 200, 2026-10-10)
- https://api.github.com/repos/ruc-datalab/DeepAnalyze - stars, forks, created and pushed dates, and the MIT license for the as-of status (fetched 200, 2026-10-10)
- https://arxiv.org/abs/2510.16872 - the paper: title, authors, October 19 2025 online date, curriculum-based agentic training, and the frontier-workflow-agents comparison claim (fetched 200, 2026-10-10)
- https://huggingface.co/RUC-DataLab/DeepAnalyze-8B - the open weights page (fetched 200, 2026-10-10)
- https://huggingface.co/api/models/RUC-DataLab/DeepAnalyze-8B - the 203 downloads and 93 likes usage footprint (fetched 200, 2026-10-10)
- https://ruc-deepanalyze.github.io/ - the project homepage, fetched with its template placeholders unfilled (fetched 200, 2026-10-10)
- https://hn.algolia.com/api/v1/search?query=DeepAnalyze - the zero-story Hacker News footprint (fetched 200, 2026-10-10)
