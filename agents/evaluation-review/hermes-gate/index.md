---
title: HermesGate
created: 2026-10-16
updated: 2026-10-23
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation-review, ci, quality-gate, deterministic]
readability: 3
audience_notes: >
  Engineers who gate coding-agent output in CI and want a repeatable pass or fail that names exactly which bytes and tool versions were checked.
  Assumes you know what a CI check and a content hash are.
---

HermesGate is Hermes Labs' Apache-2.0 receipt-bound quality gate for coding agents: it runs a repository's own declared checks, binds the PASS to an exact content digest and the tool versions that produced it, and reuses that receipt only while the bytes still match.

**Its judged object is the completion claim, not the code: where every other judge in this category scores outputs, HermesGate scores whether "the checks passed" means anything, turning an agent's unverifiable done into a receipt a human, a hook, or a boundary command can verify.**

## What it is

A Python 3.11+ CLI (`pip install hermes-gate`) with no daemon and no runtime dependencies beyond Git, from Hermes Labs, an agentic-infrastructure vendor whose tagline is "assurance, not theater".
`hermes-gate init` detects repository-native commands (Ruff, pytest, npm, lint, typecheck, build) and writes a reviewable `.hermes/gate.toml` profile, a checksum-bound standard-library runner, and a CI workflow, wrapping the repo's own tools rather than installing or replacing them.
Three completion workflows cover `fast` (changed paths, seconds), `full` (the whole local test contract), and `review` (one bounded semantic review after fast passes), each emitting one terminal JSON state from PASS, FAIL, NOT_APPLICABLE, NOT_CONFIGURED, REVIEW_UNAVAILABLE, PARKED, or ERROR, and `boundary commit|push|pr-create|pr-ready` verifies receipts before a Git operation without performing one.
The `review` mode is the only model-touching path: it consumes CodeRabbit agent-mode JSONL or any local reviewer command emitting a completion claim against the exact diff digest, and unparseable, timed-out, or unavailable review output is never relabeled PASS.
Distribution is PyPI, a pinned GitHub Action (`hermes-labs-ai/hermes-gate@v0.1.7`), and a self-contained Claude Code plugin wiring SessionStart, Stop, and PreToolUse (Bash) hooks, all of which fail open; a hidden `delegate-judge` command adapts the same engine as the quality gate for NousResearch's Hermes Agent.

## Status

Early and near-invisible: 3 stars, 1 fork, and 89 commits as of 2026-10-16, created 2026-08-10, pushed 2026-10-15, PyPI 0.1.7 matching the v0.1.7 action.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=hermes-labs-ai/hermes-gate&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=hermes-labs-ai/hermes-gate&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=hermes-labs-ai/hermes-gate&type=date&legend=top-left" />
</picture>

The provenance untidiness resolved after verification: as of 2026-10-23 the vendor-org repository (hermes-labs-ai/hermes-gate) redirects to the personal one (roli-lpci/hermes-gate), so the twin repositories seen at creation are now one repository, while the README's badges, action pin, and catalog table still point at the org path through the redirect.
A Hacker News search returns no threads, and the vendor's own curated catalog still does not list HermesGate, though the org's site hosts the project pages.
**The zero-community footprint is the adoption signal here: the pattern is worth copying, and nothing independent has validated the implementation.**

## Strengths

- The receipt is the mechanism this category lacked: a PASS names the exact content digest, selected paths, checks, and command versions, so "it passed" is checkable later and a stale receipt cannot masquerade as a fresh one.
- Deterministic by default: fast and full never call a model, which makes the gate's verdict reproducible in a way no LLM judge here is.
- The fail mode is split correctly: adopted-repo boundaries fail closed on a missing profile, while advisory hooks fail open so a malformed payload never blocks a session.
- The self-description is disciplined about epistemics: a PASS explicitly does not prove correctness, security, mergeability, or that a reviewer examined every line.

## Cautions

- Near-zero adoption: 3 stars, no discussion anywhere, and absent from the vendor's own catalog page, so the receipt semantics have no third-party validation.
- The review mode's default providers (CodeRabbit, a bundled Claude adapter) send your diff to third parties when enabled, and the README's PASS boundary is easy to skim past.
- The twin-repository arrangement that weakened provenance at creation collapsed before this re-verification: the org path now redirects to the personal repository, leaving one canonical repo, but the README still pins badges and the GitHub Action to the org path.
- Solo-vendor tool from a small consultancy, pre-1.0, with the profile format and JSON states still free to move.

## Pricing

Free and open source under Apache-2.0, fully local, with the judge stage billing whatever reviewer or model you attach.
No hosted tier is recorded; the vendor sells reliability services separately.

## Compared to

- [Verbatim Citation Gate](../verbatim-citation-gate/index.md): the same deterministic-first pattern on a different object, citations versus completion claims, and both refuse to spend model tokens before the cheap check has spoken.
- [deepeval](../deepeval/index.md): the eval suite as CI gate; deepeval judges model outputs against metrics, HermesGate attests that the repository's own checks ran on exact bytes.
- [Better Harness](../better-harness/index.md): scores the work loop continuously from evidence; HermesGate binds one completion event to one verifiable receipt.

## Bottom line

**Recommended as a pattern for anyone building agent completion gates: the receipt-bound, digest-checked PASS is the right primitive, and the implementation is small enough to read in an afternoon.**
Not as a trusted dependency today: with three stars and no independent validation, copy the design before you install the package.

## Changes

- 2026-10-16 - Created from the awesome-agent-observability scan, admitted as the category's first receipt-bound completion gate.
- 2026-10-23 - Updated the provenance record: the hermes-labs-ai org repository now redirects to roli-lpci/hermes-gate, collapsing the twin-repository arrangement noted at creation; every cited URL re-fetched in rotation, all live.

## See also

- [Verbatim Citation Gate](../verbatim-citation-gate/index.md) - the deterministic-first sibling on citations
- [deepeval](../deepeval/index.md) - the CI-gating eval framework
- [Better Harness](../better-harness/index.md) - the workflow-level findings loop
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/roli-lpci/hermes-gate - the list-linked repository: README, CLI, workflows, review contract, and plugin
- https://github.com/hermes-labs-ai/hermes-gate - the vendor-org repository path the badges and GitHub Action point at, now redirecting to roli-lpci/hermes-gate (checked 2026-10-23)
- https://pypi.org/project/hermes-gate/ - the published package, 0.1.7, authored by Hermes Labs
- https://raw.githubusercontent.com/roli-lpci/hermes-gate/main/CHANGELOG.md - release history, including the reused-review fix
- https://raw.githubusercontent.com/roli-lpci/hermes-gate/main/llms.txt - the project's self-description and docs index
- https://hermes-labs.ai/open-source - the vendor's curated catalog, which does not yet list HermesGate
