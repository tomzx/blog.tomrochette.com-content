---
title: Shreya Shankar
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, evals, data-systems, llm-practitioner, academic]
readability: 3
audience_notes: >
  Engineers building LLM pipelines over messy, document-heavy data who want measurement discipline with peer-review provenance.
  Assumes you know what an eval is and have shipped at least one LLM feature whose quality surprised you.
---

Shreya Shankar is a UC Berkeley computer science researcher in the EPIC Data Lab, advised by Aditya Parameswaran, who joins Carnegie Mellon University as an assistant professor in 2027 and publishes and teaches on making LLM systems measurable.

**She is the voice that turns agent and pipeline reliability from opinion into benchmarks and peer-reviewed systems: when you want measurement discipline grounded in review rather than vendor decks, start here, with the caveat that the cadence is academic and the center of gravity is data systems, not coding agents.**

## What it is

A personal site and blog, a stack of open-source research systems, and a growing set of benchmarks, all built on her PhD work on LLM-powered data processing.
The flagship is DocETL (github.com/ucbepic/docetl), a system for complex document processing with semantic operators and agentic query rewrites, which her homepage reports at 3.7k+ GitHub stars with real use by public defenders and climate scientists as of 2026-09-24.
With Hamel Husain she co-teaches and co-writes the evals material, including the free Maven mini-book Beyond Naive RAG.
The newest instrument is Data Agent Bench (DAB), the first benchmark for data agents on realistic multi-database tasks.

## Status

Active and ascending, in a transition year.
Her homepage announces the move to Carnegie Mellon's CSD (and, by courtesy, HCII) in 2027, where she is starting the Full Stack Data Lab.
The award record is stacking up fast: Best of SIGMOD 2026, a CHI 2026 Best Paper (RAG Without the Lag), and a UIST 2025 Best Paper Honorable Mention, plus two more papers at VLDB 2026.
DAB appears at EMNLP in October 2026 with over 50 submissions already; the repo leaderboard shows entries dated through 2026-09-13, and the repo sits at 172 stars and 57 forks as of 2026-09-24.
The blog is slow, with the latest post on May 21, 2026, but she gave the Weaviate Podcast #135 on data agents in April 2026, covering DocETL, semantic operators, and why context management may be the new data management.

## Strengths

- Peer-review provenance: the claims come with SIGMOD, VLDB, CHI, and UIST awards behind them, which is rare in an evals discourse dominated by vendor content.
- She ships instruments, not just arguments: DocETL and DAB are runnable artifacts with public leaderboards and submission traces you can audit.
- The evals framework she teaches with Hamel has been pressure-tested on thousands of course students, not only her own projects.
- She engages critics directly: In Defense of AI Evals names the anti-evals posts making the rounds and answers them on the merits rather than strawmanning them.

## Cautions

- Cadence is academic: a few blog posts a year, with most substance in papers, course material, and code.
- The examples lean toward document processing and data analysis, so coding-agent practitioners must translate.
- The evals lane she anchors has a live skeptical current (the anti-evals posts by swyx and others she rebuts), and reasonable people disagree about how much rigor a small team needs.
- A practical note for an AI-maintained section like this one: her homepage states she receives dozens of AI-generated emails a week and never responds to any of them.

## Compared to

- [Hamel Husain](../hamel-husain/index.md): her frequent co-author and co-teacher; he is the practitioner-consultant voice, she supplies the formal grounding and the systems. Choose Hamel for the consulting-grade how-to, Shreya for the reviewed why and the data-systems layer.
- [Lilian Weng](../lilian-weng/index.md): both are rigorous researcher voices, but Weng surveys the model-and-agent research frontier while Shankar works the data-and-measurement layer underneath it.
- [Nathan Lambert](../nathan-lambert/index.md): Lambert explains how models are post-trained, Shankar explains whether your pipeline over them actually works; read Lambert for the model layer, Shankar for the application layer.

## Bottom line

Recommended for engineers whose LLM work runs over messy real-world data and who want an evals method with peer-review provenance and runnable benchmarks.
Not for someone hunting a daily news feed on coding-agent tools or quick prompt tricks.

## Top 5 recommended reading

- [In Defense of AI Evals, for Everyone](https://www.sh-reya.com/blog/in-defense-ai-evals/) - her defining statement on what evals are, when lighter rigor is fine, and why the anti-evals backlash misfires.
- [Data Flywheels for LLM Applications](https://www.sh-reya.com/blog/ai-engineering-flywheel/) - the three-part evaluation, monitoring, and continual-improvement framework for turning production traces into improvement.
- [On the Consumption of AI-Generated Content at Scale](https://www.sh-reya.com/blog/consumption-ai-scale/) - her most original recent essay, on signal degradation and verification erosion in an AI-saturated information diet.
- [DocETL](https://www.docetl.org/) - the flagship system that operationalizes her research on semantic operators and agentic query rewrites for document processing.
- [Data Agent Benchmark (DAB)](https://github.com/ucbepic/DataAgentBench) - the benchmark and public leaderboard that measures whether data agents can handle realistic multi-database work.

## Changes

- 2026-09-24 - Created.

## See also

- [Hamel Husain](../hamel-husain/index.md) - her co-teacher and co-author on the evals course and FAQ, the practitioner half of the partnership
- [Lilian Weng](../lilian-weng/index.md) - the other academic-depth voice in this category, working the model and agent frontier
- [Phoenix](../../evaluation-review/phoenix/index.md) - tracing and evaluation tooling that operationalizes the measurement discipline she teaches
- [LlamaIndex](../../retrieval/llamaindex/index.md) - the RAG framework layer her Beyond Naive RAG material critiques and improves

## References

- https://www.sh-reya.com/ - homepage: the CMU 2027 move, the Full Stack Data Lab, DocETL adoption, and the paper awards
- https://www.sh-reya.com/blog - the blog index and posting cadence
- https://www.sh-reya.com/blog/in-defense-ai-evals/ - the definition of evals and the rebuttal to the anti-evals wave
- https://www.sh-reya.com/blog/ai-engineering-flywheel/ - the data flywheel framework
- https://www.sh-reya.com/blog/consumption-ai-scale/ - the signal-degradation and verification-erosion essay
- https://www.docetl.org/ - the DocETL project site and its paper record
- https://github.com/ucbepic/DataAgentBench - DAB repo, leaderboard entries, and submission activity as of 2026-09-24
- https://maven.com/p/945082/beyond-naive-rag-practical-advanced-methods - the free mini-book with Hamel Husain, and her positioning as an applied evals researcher
- https://hn.algolia.com/api/v1/search?query=%22shreya%20shankar%22&hitsPerPage=8 - HN footprint: the Weaviate Podcast episode on data agents, her 2022 ML engineering essay, and Hamel naming her a frequent collaborator
