---
title: Verbatim Citation Gate
created: 2026-10-10
updated: 2026-10-25
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation-review, citations, hallucination, guardrails, rag]
readability: 3
audience_notes: >
  Engineers building RAG or research agents whose failure mode is fabricated quotes, and who want a gate that costs no tokens.
  Assumes you know what grounded citation checking tries to do and what an LLM judge is.
---

Verbatim Citation Gate is an MIT two-stage citation auditor that catches fabricated RAG quotes deterministically before any model call, then hands only quotes that actually exist to a skeptical LLM judge.

**The mechanism is the order of the checks: a zero-dependency, zero-token verbatim gate rejects fabricated, stitched ("frankenquote"), and misattributed quotes for free, so the expensive judge only ever sees quotes the sources contain, and the judge itself starts at "unsupported" and fails closed when its output does not parse.**

## What it is

A pip-installable Python package (from the repository, not yet on PyPI) with stage one in `gate.py`: pure `re` plus substring matching over a normalized form (case, smart quotes, dashes, and whitespace folded, numbers and percent preserved), returning `not_found` or `misattributed` with no network and no model.
Stage two in `judge.py` takes any `(system, user) -> str` callable, so it wires to Claude, GPT, Gemini, Mistral, Cohere, or a local Qwen without adapters, and returns `supports`, `partial`, `unrelated`, or `contradicts`.
The judge's prompt encodes three rules: default-refute (the verdict starts at unsupported and ties break against the claim), outside knowledge is inadmissible (a claim can be true and still unsupported by this source), and full-strength support or the verdict caps at `partial`.
Each named failure mode has its own test, including `test_audit_fabrication_never_calls_judge`, which proves a fabricated quote costs zero model calls.
The docs page describes the maintainer as the Palo Alto AI Research Lab, a self-styled name; the repository itself belongs to a personal GitHub account (tonydzi), and no GitHub organization of that lab name exists as of 2026-10-11.

## Status

Active but barely adopted: 4 stars, 3 forks, and 5 open issues as of 2026-10-13, created 2026-07-24, pushed 2026-10-24, with four releases (v0.3.1 on 2026-10-24, v0.3.0 on 2026-10-16, v0.2.0 on 2026-08-25, v0.1.0 on 2026-08-04) and CI running a tests workflow.
v0.3.1 (2026-10-24) released the three gate fixes that had sat on main since 2026-10-19 (whole-word quote matching, a balanced-JSON verdict parser, and a pytest source-path fix), and the package is still absent from PyPI as of 2026-10-25.
v0.3.0 adds a `span_gate` that applies the same fail-closed treatment to citations given as character offsets, rejecting unresolvable spans instead of silently clipping them, and it is the project's first outside contribution (PR 12, closing issue 9).
A Hacker News search returns zero threads as of 2026-10-11, so the adoption signal here is still thin: a solo project with a clean mechanism whose first independent involvement arrived through that October contribution.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=tonydzi/verbatim-citation-gate&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=tonydzi/verbatim-citation-gate&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=tonydzi/verbatim-citation-gate&type=date&legend=top-left" />
</picture>

## Strengths

- The free first stage is an effective filter: three quote-failure classes (fabricated, frankenquote, misattributed) each get a named test, and the contiguous-match design is what makes stitched quotes fail.
- Fail-closed judge: an unparseable judge response never counts as support, which is the right default for a verification component.
- The smallest possible judge contract (`(system, user) -> str`) means the gate outlives any vendor SDK.
- Misattribution is surfaced as its own verdict rather than collapsed into not-found, because the two failures need different fixes upstream.

## Cautions

- Near-zero adoption: 4 stars and zero discussion as of 2026-10-11, with the October v0.3.0 contribution the only outside involvement on record, so treat it as a promising pattern to copy, not a dependency to trust.
- Exact-verbatim matching misses legitimate paraphrase and cross-sentence citations by design, so it fits quote-style citation systems only.
- The distribution is a git URL install with no PyPI package (still absent as of 2026-10-25), and the release train ran twice in August then resumed in October with v0.3.0 and v0.3.1.
- The "Palo Alto AI Research Lab" branding on the docs is uncorroborated by any organization, funding, or publication record a reader can check.

## Pricing

Does not apply: MIT-licensed, free, stage one costs zero tokens and stage two costs whatever model you attach.

## Compared to

- [deepeval](../deepeval/index.md): its faithfulness metrics judge grounding with an LLM on every check; choose Verbatim Citation Gate to make the deterministic substring check absorb the obvious fabrications first, and keep deepeval for everything non-verbatim.
- [Jevals](../jevals/index.md): typed decision-model judges that calibrate per question; Jevals is the general judge layer, this gate is the free pre-filter that shrinks what any judge sees.
- [Phoenix](../phoenix/index.md): RAG evals and tracing at platform scale; run the platform for visibility and bolt this gate onto the citation path where fabrication actually hurts.

## Bottom line

**Recommended as a pattern and a small library for quote-citing pipelines: adopt the two-stage order (deterministic verbatim check, then skeptical judge) even if you reimplement it.**
Not for paraphrase-tolerant citation systems, and not as a battle-tested dependency until someone other than the author has run it.

## Changes

- 2026-10-10 - Created from the evaluation-review resolution pass as the differentiated judge mechanism: the deterministic zero-token citation-fabrication gate ahead of an LLM judge.
- 2026-10-17 - Recorded the v0.3.0 release (2026-10-16): offset-span citations under the same fail-closed gate, and the project's first outside contribution (PR 12), with the release-pause caution updated.
- 2026-10-21 - Recorded the unreleased post-v0.3.0 fixes on main (2026-10-19) and re-verified the PyPI absence; the newest release is still v0.3.0.
- 2026-10-25 - Recorded the v0.3.1 release (2026-10-24), which shipped the three gate fixes previously tracked as unreleased on main; the PyPI absence re-verified.

- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).

## See also

- [deepeval](../deepeval/index.md) - the LLM-judged faithfulness metrics this gate pre-filters
- [Jevals](../jevals/index.md) - the typed-judge layer in the same category
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [Rethinking Code Review in the Age of LLMs](../../../rethinking-code-review-in-the-age-of-llms/index.md) - the corpus argument for cheap deterministic checks ahead of model judgment

## References

- https://github.com/tonydzi/verbatim-citation-gate - repository: README, two-stage design, test names, license
- https://api.github.com/repos/tonydzi/verbatim-citation-gate - stars, forks, issues, creation and push dates as of 2026-10-11
- https://api.github.com/repos/tonydzi/verbatim-citation-gate/releases - v0.2.0 (2026-08-25) and v0.1.0 (2026-08-04)
- https://api.github.com/repos/tonydzi/verbatim-citation-gate/releases/tags/v0.3.0 - v0.3.0 (2026-10-16): the span_gate release notes and the first outside contribution (PR 12)
- https://tonydzi.github.io/verbatim-citation-gate/ - the docs page: two-stage diagram, known limits, and the self-styled lab attribution
- https://hn.algolia.com/api/v1/search?query=verbatim-citation-gate&hitsPerPage=3 - the zero-thread community-footprint check as of 2026-10-11
