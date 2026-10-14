---
title: SkillSpector
created: 2026-10-12
updated: 2026-10-12
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, skills, security, supply-chain]
readability: 3
audience_notes: >
  Engineers who install third-party agent skills and want a safety verdict
  before install instead of reading every SKILL.md and script by hand.
  Assumes you know what a SKILL.md is and what prompt injection means.
---

SkillSpector is NVIDIA's Apache-2.0 security scanner for AI agent skills: point it at a git repo, URL, zip, directory, or a single SKILL.md, and it returns a 0-100 risk score with a SAFE, CAUTION, or DO NOT INSTALL recommendation before you install the thing.

**Its bet is that skills execute with implicit trust and minimal vetting, and it opens with its own research numbers: in a 31,132-skill analyzed subset, 26.1% of skills contained vulnerabilities and 5.2% showed likely malicious intent.**

## What it is

A Python 3.12+ CLI (installed with uv or pip from git, or run as a Docker image) from NVIDIA, built as two analysis stages.
Stage one is static: eleven analyzers covering 71 vulnerability patterns across 17 categories, prompt injection, data exfiltration, privilege escalation, supply chain, excessive agency, MCP tool poisoning and least privilege, plus AST behavioral checks, taint tracking, YARA signatures, and live CVE lookups against OSV.dev with an offline fallback.
Stage two is an optional LLM semantic pass (OpenAI, Anthropic, Bedrock, Gemini, Ollama, local runtimes, or NVIDIA's own build.nvidia.com endpoint) that can confirm findings and add explanations but never removes one, and disputed findings stay tagged `llm-unconfirmed` in the JSON and SARIF output.
Reports land as terminal text, JSON, Markdown, or SARIF for CI, the exit codes are a documented install-gate contract, and an MCP server mode exposes a single `scan_skill` tool so an MCP host can gate installs at runtime.
It is the security tier inside NVIDIA's SkillEvaluator and part of the Verified Skills pipeline that scans, evaluates, and signs skills before publishing them to NVIDIA's catalog, with in-session extensions for Pi and OpenCode.

## Status

Active and large: 20,139 stars, 1,770 forks, and 149 open issues as of 2026-10-13, created 2026-03-21, pushed 2026-10-13 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=NVIDIA/SkillSpector&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=NVIDIA/SkillSpector&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=NVIDIA/SkillSpector&type=date&legend=top-left" />
</picture>

The release train is active: v2.12.0 is the latest release, published 2026-09-23 with sha256-digested wheel and sdist assets, and its notes close with "Prepared by Codex on behalf of Mohit Gupta".
The Hacker News footprint is one 49-point thread with 4 comments from 2026-06-12, thin against the star count and the same stars-ahead-of-discussion pattern this section has flagged on agentmemory and Cabinet.
The project's documentation already disagrees with itself: the README counts 71 vulnerability patterns, the hosted docs guide counts 68.

## Strengths

- **Fail-closed engineering is rare in this ecosystem**: ingest caps (100 MiB per source, 10,000 zip members), coverage accounting where any excluded file blocks a SAFE verdict, and an exit-code contract built for CI gates.
- Deterministic findings are immovable: the LLM stage can confirm or dispute, but every static finding stays in the report.
- Baseline suppression lets a team accept known findings once and resurface only new ones, with evidence-bound fingerprints that reactivate when the source changes.
- The README states its own limits, including moderate static precision, no guaranteed LLM precision, and a disabled codex_cli provider whose sandbox permits host-file reads.

## Cautions

- **The pattern set is one vendor's opinion, and the 68-versus-71 count drift between the README and the docs guide shows the taxonomy is still moving.**
- The OpenCode in-session provider pins one exact OpenCode version (1.18.33 in the README, 1.18.31 in the v2.12.0 notes), so in-session semantic scans break on any other OpenCode release.
- LLM-stage scans bill your own provider, and the batch scanner's default model targeted DeepSeek, which the README expects to sunset.
- The MCP HTTP transport ships without authentication by design (loopback-only binding, credential-free https targets only), a documented but easy-to-misuse trust model.
- A clean scan inspects the artifact pre-install; it says nothing about whether the skill improves your output, which is SkillEvaluator's separate question.

## Pricing

Free and Apache-2.0, with no hosted tier of its own.
Static scans cost nothing; LLM-stage scans run on your own provider credentials and bill your tokens.

## Compared to

- [SkillMD](../skillmd/index.md): the registry that publishes lint and scanner verdicts per indexed skill; SkillSpector is the scanner you run yourself on a skill SkillMD has not reviewed.
- [skills.sh](../skills-sh/index.md): the registry whose audit columns aggregate third-party scanner output after the fact; SkillSpector is the gate run before install rather than a column read after.
- [OpenCode skills and plugins](../opencode-skills-and-plugins/index.md): the harness-side allow/deny/ask gate at load time; SkillSpector inspects content before it ever reaches a harness, so the two compose rather than compete.

## Bottom line

**Recommended for teams that install third-party skills into CI or shared images, where the exit codes and SARIF output make a pre-install scan a cheap gate, and for anyone about to run an unvetted skill against a repo with production secrets.**
Not for runtime policy enforcement (that is the harness or a control plane), for output-quality questions (that is SkillEvaluator's separate tier), or as a clean bill of health, since its static stage advertises moderate precision and the LLM stage guarantees nothing removed.

## Changes

- 2026-10-12 - Created from the daily-refresh scan resolution, with five fetched sources, the one-vendor-pattern-set caution, and the docs-versus-README pattern-count drift recorded as the critical angle.

## See also

- [SkillMD](../skillmd/index.md) - the verification-first registry, the at-scale version of the per-scan verdict SkillSpector computes
- [skills.sh](../skills-sh/index.md) - the registry whose audit columns aggregate scanner output, the market SkillSpector's verdicts feed
- [SkillOpt](../skillopt/index.md) - the other tool that operates on skill artifacts as inputs, training rather than grading
- [Anthropic Agent Skills](../anthropic-agent-skills/index.md) - the vendor framing of skills as untrusted inputs that motivates pre-install scanning
- [Agent Skills open standard](../agent-skills-open-standard/index.md) - the format whose six fields carry none of the security posture this scanner checks

## References

- https://api.github.com/repos/NVIDIA/SkillSpector - 20,139 stars, 1,770 forks, 149 open issues, Apache-2.0, created 2026-03-21, pushed 2026-10-13, docs homepage (fetched 2026-10-13)
- https://raw.githubusercontent.com/NVIDIA/SkillSpector/main/README.md - the 71-pattern taxonomy, two-stage pipeline, MCP mode, install paths, risk scoring, and the 31,132-skill research numbers (fetched 2026-10-12)
- https://docs.nvidia.com/skills/scanning-agent-skills - the hosted guide with its 68-pattern count, the triage policy, and the SkillEvaluator security-tier framing (fetched 2026-10-12)
- https://api.github.com/repos/NVIDIA/SkillSpector/releases/latest - v2.12.0 published 2026-09-23 with sha256-digested wheel and sdist assets, and the Codex-prepared release notes (fetched 2026-10-12)
- https://hn.algolia.com/api/v1/search?query=SkillSpector&tags=story - the single 49-point, 4-comment thread (2026-06-12) behind the thin-footprint statement (fetched 2026-10-12)
