---
title: ARIS
created: 2026-10-10
updated: 2026-10-18
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, agentic-llm, machine-learning, open-source, skills]
readability: 3
audience_notes: >
  Engineers running unattended ML research loops on the coding agent they already use, and researchers comparing cross-model review against kernel or benchmark judges.
  Assumes you know what a Claude Code skill and an MCP server are.
---

ARIS (Auto-Research-In-Sleep) is wanshuiyin's MIT-licensed set of markdown-defined skills that turns Claude Code, Codex CLI, or another coding agent into an autonomous ML research loop, with a reviewer model from a different family critiquing every artifact at gated passes.

**ARIS is this category's first member whose judge is required to be a different model family: the executor drives and an independent reviewer (Codex MCP by default) demands revisions, an arrangement its technical report builds against the category's shared failure mode, the plausible unsupported success.**

## What it is

A methodology shipped as 82 markdown skills (83 in the standalone CLI bundle) with no framework and no lock-in, created 2026-03-10.
The technical report (arXiv 2605.03042, May 2026, by Ruofeng Yang, Yongcan Li, and Shuai Li) describes three layers: an execution layer with more than 65 reusable markdown skills, MCP model integrations, and a persistent research wiki; a review layer where a reviewer from a different model family critiques intermediate artifacts and requests revisions; and deployment experience from long unattended runs.
The skills cover the research arc end to end: idea discovery, experiment queues (including SSH multi-seed job queues), paper writing, citation audits, integrity forensics, and Overleaf sync.
Adapters exist for Claude Code, Codex CLI, Cursor, Trae, Antigravity, GitHub Copilot CLI, OpenClaw, and DeepSeek Harness.
Beyond the skills, the project ships a standalone Rust CLI (ARIS-Code, v0.4.28 on 2026-09-28, mid a 24-release train) and Claude Code, Codex CLI, and DeepSeek Harness plugins.

## Status

Active: 17,367 stars, 1,456 forks, created 2026-03-10, last push 2026-10-17 (a WeChat community QR-code refresh, the only commit since October 7), as of 2026-10-18.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=wanshuiyin/Auto-claude-code-research-in-sleep&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=wanshuiyin/Auto-claude-code-research-in-sleep&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=wanshuiyin/Auto-claude-code-research-in-sleep&type=date&legend=top-left" />
</picture>

**The Western discussion footprint is zero: a Hacker News search for the repository name returns no stories as of 2026-10-10, and adoption runs through a PaperWeekly feature and the Chinese-language community, the channel pattern DeepAnalyze shows; the Agon paper's own count puts ARIS at 79 roles and 1,157.4 KiB of prompts, roughly four times Agon's surface.**

## Strengths

- The cross-model rule attacks a failure the kernel columns never face: a reviewer from a different family is less likely to inherit the executor's framing, which is where the report locates unsupported claims.
- The skill set covers the whole arc, including integrity tooling (citation audit, fabrication forensics) most research loops leave to the human.
- No lock-in: the same markdown skills port across eight harnesses, so the loop survives any single vendor's churn.
- The maintenance cadence is exceptional: 24 CLI releases between May and September 2026, including a same-week bridge when codex-cli 0.154 removed the reviewer's entry point.

## Cautions

- The report's deployment claims are self-published, and no independent replication surfaced in this run's searches.
- The judge is still a model: cross-model review raises the bar but is not a kernel, a grader, or a benchmark.
- The prompt surface is large (79 roles, 1,157.4 KiB by the Agon paper's count), which makes behavior harder to inspect than Agon's 18 roles.
- The zero-story Hacker News footprint says the 17.2k stars measure attention in one language community, not broad engineering adoption.
- The loop depends on moving harness internals, as the codex-cli 0.154 breakage demonstrated.

## Pricing

Free and MIT; there is no paid tier, so pricing does not apply.
Costs are your own model subscriptions or API keys (Claude executor plus a Codex reviewer by default, with ModelScope-hosted and local-model combinations documented) and your compute.

## Compared to

- [Agon](../agon/index.md): the Claude Code plugin running producer-critic factories; ARIS is the skills-based loop whose reviewers come from other model families and which ports across harnesses.
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md): the founding keep-or-revert loop whose judge is a measured loss; ARIS's judge is another model's critique.
- [OpenResearch](../openresearch/index.md): the workspace that turns your own agents into researchers with an archived evidence tree; ARIS adds adversarial review gates to the same idea.

## Bottom line

**Recommended for ML researchers who want an unattended experiment loop with cross-model review, on the harness they already use, and for studying review-gate design against plausible unsupported successes.**
Not for anyone who needs a machine verifier behind results, a small inspectable prompt surface, or an independently replicated evaluation.

## Changes

- 2026-10-10 - Created.

## See also

- [Agon](../agon/index.md) - the producer-critic plugin that measured ARIS's prompt surface
- [Karpathy Autoresearch](../karpathy-autoresearch/index.md) - the keep-or-revert ancestor of the loop family
- [DeepAnalyze](../deepanalyze/index.md) - the other thin-Western-footprint member, judged by itself where ARIS is judged by another model
- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep - repository and README: skill set, harness adapters, executor-reviewer split, release train (fetched 200, 2026-10-10)
- https://api.github.com/repos/wanshuiyin/Auto-claude-code-research-in-sleep - stars, forks, created and pushed dates, MIT license, and topics for the as-of status (fetched 200, 2026-10-18)
- https://raw.githubusercontent.com/wanshuiyin/Auto-claude-code-research-in-sleep/main/README.md - the README source: 82 skills, adapter list, ARIS-Code v0.4.28 details, and the codex-cli 0.154 bridge note (fetched 200, 2026-10-10)
- https://arxiv.org/abs/2605.03042 - the technical report: cross-model adversarial collaboration, the plausible-unsupported-success failure mode, and the three-layer architecture (fetched 200, 2026-10-10)
- https://api.github.com/repos/wanshuiyin/Auto-claude-code-research-in-sleep/releases?per_page=5 - the release train through v0.4.28 (2026-09-28), still the latest (fetched 200, 2026-10-18)
- https://hn.algolia.com/api/v1/search?query=claude-code-research-in-sleep - the zero-story Hacker News footprint (fetched 200, 2026-10-10)
