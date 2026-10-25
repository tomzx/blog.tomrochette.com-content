---
title: slop-grader
created: 2026-10-21
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation-review, jev, decision-models, linting, writing-quality]
readability: 3
audience_notes: >
  Engineers who want repeatable, rule-based grading of AI-written documents and diffs without paying chat-model prices per check.
  Assumes you know what a linter and an LLM judge are.
---

slop-grader is a free, MIT-licensed TypeScript CLI that grades text files against Markdown-authored rulesets using Jev, the typed decision model, asking one semantic question per line per rule in parallel instead of asking a chat model to skim the whole document.

**It is Jevals' mechanism pointed at documents: the judge never generates text, so exhaustive coverage (every rule against every line) costs cents, and the output is a report any agent can turn into a fix plan.**

## What it is

An npm CLI (`@lukstei/slop-grader`, Node 18+) from lukstei, with rules written in plain Markdown under `# Line Rules` and `# Document Rules` sections or in JSON, validated offline with `--check`.
Line rules ask one yes/no question per line (banned words, empty adverbs, swallowed errors, hardcoded secrets); document rules score qualitative rubrics (narrative arc, root-cause depth, commit intent) in a single request.
Lines are batched to the model's token budget (up to 255 lines per call) with up to ten lines of surrounding context, and every batch response is verified for complete answer-to-question parity, halting on dropped questions rather than reporting unchecked lines as clean.
Evaluations cache by line hash, so re-running an edited document bills only the changed lines.
Providers are TypeSafe's Jev endpoint or OpenRouter (jev-1.13 by default), and the intended loop is two steps: grade, then paste the report into any AI agent to plan and apply the fixes.
Five built-in rulesets ship (no-ai-slop, article-scores, tech-docs, and English and German grammar), plus a companion agent skill for authoring custom rulesets.

## Status

New and shipping fast: 35 stars and 2 forks as of 2026-10-21, created 2026-09-20, pushed 2026-10-18, with seventeen GitHub releases in the first month and npm at 0.4.0 (2026-10-18) after fifteen published versions.
Adoption is early but measurable: 2,727 npm downloads in the first month, 180 in the week of 2026-10-12 to 2026-10-18.
**The independent footprint is one Show HN thread (2026-09-21, 3 points, zero comments) and no third-party coverage anywhere, so every performance claim on record comes from the author's own README.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=lukstei/slop-grader&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=lukstei/slop-grader&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=lukstei/slop-grader&type=date&legend=top-left" />
</picture>

## Strengths

- Exhaustive by construction: every rule meets every line, so nothing is skimmed, which is the documented failure mode of single-prompt document review.
- The judge is typed and cheap: Jev probabilities cost thousandths of a cent per question, which is what makes thousand-check runs routine (the README grades a 300-line article against 42 rules for about 7.6 cents).
- Rules are Markdown you can read, version, and validate offline, and the project's own guidance is one pattern per rule, which keeps failures attributable to a named rule ID.
- Cache-by-line turns the grader into an editing-loop companion rather than a one-shot audit.

## Cautions

- The judge is the same small-model class as every Jev consumer: its precision on nuanced rules is unmeasured by anyone except the author, and the 0.8 confidence threshold is global, not per rule.
- Zero independent evaluation: no benchmark, no third-party writeup, one unremarked Show HN thread, so the cost and coverage figures rest entirely on the README's self-run examples.
- The GitHub Action and pull-request comment surfaces are still roadmap items, so CI use today means wrapping the JSON output yourself.
- Solo maintainer, one month old, fifteen npm versions: ruleset syntax and CLI flags have moved repeatedly and will keep moving.

## Pricing

The CLI is free and MIT.
Grading bills your own provider key: the README's own examples price a 16-line document against 53 rules at about $0.0053 and a 300-line article against 42 rules at about $0.076, with unchanged lines free on re-runs through the cache.
The Jev backend's per-token price is tracked in the [Jevals](../jevals/index.md) note, which uses the same backend.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-21 | Jev/OpenRouter usage | Baseline: CLI free (MIT); grading bills your provider key, README examples about $0.0053 per 16-line document against 53 rules and about $0.076 per 300-line article against 42 rules. | https://raw.githubusercontent.com/lukstei/slop-grader/main/README.md |

## Compared to

- [Jevals](../jevals/index.md): the same Jev judge packaged as a Python evals-and-guardrails library over agent traces; slop-grader is the document-and-diff grader with a report-and-fix-plan loop, Jevals the in-loop gate.
- [Verbatim Citation Gate](../verbatim-citation-gate/index.md): the other cheap-first judge on text, deterministic for quotes where slop-grader is decision-model for rules; both refuse to pay generative prices per check.
- [deepeval](../deepeval/index.md): the pytest-style framework with judge metrics gating LLM app outputs in CI; choose it when the suite must block merges, slop-grader for authored rulesets over documents and diffs.

## Bottom line

**Recommended for writers and reviewers who want a repeatable, exhaustive ruleset grade over AI-written text and diffs at near-zero cost, with an agent closing the loop on the findings.**
Not as a validated quality gate yet: one month old, one maintainer, and no independent measurement of the judge's accuracy exists.

## Changes

- 2026-10-21 - Created from the skills-worker handoff, admitted as the second Jev-based member after Jevals.

- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).

## See also

- [Jevals](../jevals/index.md) - the Jev library sibling judging traces instead of documents
- [Jev](../../hybrid-execution/jev/index.md) - the decision model every check runs on
- [Verbatim Citation Gate](../verbatim-citation-gate/index.md) - the deterministic-first citation judge
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/lukstei/slop-grader - repository, description, MIT license, stars and dates as of 2026-10-21
- https://raw.githubusercontent.com/lukstei/slop-grader/main/README.md - the two-step loop, batching and context padding, caching, cost examples, and the built-in rulesets
- https://raw.githubusercontent.com/lukstei/slop-grader/main/docs/CHANGELOG.md - release history from v0.1.x to v0.4.0
- https://registry.npmjs.org/@lukstei/slop-grader - package: 0.4.0 (2026-10-18), fifteen published versions
- https://api.npmjs.org/downloads/point/last-month/@lukstei/slop-grader - 2,727 downloads in the first month; the weekly point read 180 for 2026-10-12 to 2026-10-18
- https://hn.algolia.com/api/v1/search?query=slop-grader&hitsPerPage=5 - the single Show HN thread (2026-09-21, 3 points, zero comments), the thin-footprint evidence
