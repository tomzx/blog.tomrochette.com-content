---
title: Intent-Router
created: 2026-10-10
updated: 2026-10-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, intent-specs, clarification, skills]
readability: 3
audience_notes: >
  Engineers who get better spec adherence from agents by fixing the request itself, without adopting a full spec workflow.
  Assumes you know what spec-driven development is and have used a coding-agent skill.
---

Intent-Router is a single MIT skill that compiles a vague request into a typed IntentSpec contract, asking only what the repository cannot answer, then checks the delivered work against that spec one constraint at a time.

**The mechanism is the convergence gate plus the cross-session artifact: it probes the repo before interrupting you, refuses to emit while the intent is underspecified, writes the settled contract to `.intent/<intent>.intent.yaml` with evidence pointers, and writes the delivery check back into the same file so the next session starts from what was decided instead of zero.**

## What it is

An installable skill (`npx skills add angel291592/Intent-Router`) that runs as parse, resolve, typecheck, emit: it looks up what it can (deps, routes, git history, docs, ticket systems), asks the one question no file holds, calls out contradictions and disproved premises, and refuses to emit while anything material stays open.
The emitted IntentSpec is machine-readable YAML whose state records whether it is still waiting on a question, settled, or carried out, and a later session reads it before probing anything, so an answered question is never asked twice.
When the work is handed off, the skill checks the result against the spec constraint by constraint and records the outcome in the artifact.
The README positions it against plan modes (which prefer looking up over verifying premises), spec-kit (which asks you to buy its whole workflow), Kiro's specs (three files and an IDE), and Jev and Laya (typed decisions one layer down, the input layer this skill feeds).

## Status

Climbing back after the collapse: 239 stars and 51 forks as of 2026-10-14, created 2026-09-22, pushed 2026-10-20, with five releases (v1.4.0 on 2026-10-16, v1.3.0 on 2026-10-09, v1.0.0 on 2026-09-23); v1.4.0 trimmed the skill description to fit a 500-character harness cap after its second half, including the negative predicates that keep auto-invocation off unnecessary work, was being truncated in at least one harness, and added a DeepSeek Harness eval channel plus a cross-session contract test case.
**The GitHub API read 1,017 stars and 124 forks on 2026-10-11, 158 and 46 on 2026-10-13, and 239 and 51 on 2026-10-14: the collapse fork counts cannot take organically was followed by a one-day climb the same kind of engagement produces, which reads as a purge of inauthentic stars followed by continued re-inflation, and the nineteen-day adoption-curve claim this note published stays retracted.**
Engagement from freshly created accounts is still arriving (a fork and a star land on 2026-10-13 alone), so the inflation appears ongoing, and the independent footprint is still empty: a Hacker News search returns no thread about it as of 2026-10-13.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=angel291592/Intent-Router&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=angel291592/Intent-Router&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=angel291592/Intent-Router&type=date&theme=dark&legend=top-left" />
</picture>

## Strengths

- The delivery check is the part most spec tools skip: checking built work against the spec it came from, one constraint at a time, is where spec drift actually gets caught.
- It respects the reader before the writer: probing the repo, tickets, and docs first means the human sees one question instead of an interview.
- The cross-session YAML artifact with evidence pointers makes intent durable across agents and teammates without a platform.
- Zero install surface beyond a skill: no workflow to adopt, no daemon, no IDE, and it runs prompt-only at its L0 backend.

## Cautions

- The evidence is self-published and small: the delivery report of 2026-09-24 compares 5 bare runs against 3 skill runs (mean 5.0 versus 6.0 of 6) in one harness on one model, and the report discloses that the bare arm needed the skill explicitly denied because an installer test had left a copy in user-level skills.
- Three weeks old with a solo maintainer: the IntentSpec format and the four-state model can still move under you.
- The star story inverted: the 1,017 stars of 2026-10-11 fell to 158 by 2026-10-13 and climbed back to 239 by 2026-10-14 in an apparent purge-then-refill of inauthentic engagement, so the social signal is now evidence against the project, and there is no independent replication of the delivery numbers.
- It is upstream of typed decision models (Jev, Laya), so teams already running those need to decide which layer owns the clarification step.

## Pricing

Does not apply: MIT, free, no paid tier recorded as of 2026-10-10.

## Compared to

- [GitHub Spec Kit](../spec-kit/index.md): the full constitution-plus-workflow ceremony; choose Spec Kit when the whole team adopts the process, Intent-Router when you want the contract without the ceremony.
- [cc-sdd](../cc-sdd/index.md): a 17-skill SDD workflow installed per agent; cc-sdd covers the full spec-design-tasks pipeline, Intent-Router covers only the front door and the delivery check.
- [Superpowers](../superpowers/index.md): the mandatory skill suite with brainstorming from session start; Superpowers enforces a method, Intent-Router is opt-in per request.

## Bottom line

**Recommended for agent users whose requests arrive vague and whose follow-up sessions start from zero: the typed artifact plus the delivery check is a cheap upgrade to any harness.**
Not for teams needing enforced process (that is Superpowers), and not for anyone who requires third-party-validated numbers before adopting a three-week-old skill.

## Changes

- 2026-10-10 - Created from the spec-driven-development resolution pass, choosing this category over task management because the artifact is a spec contract with a delivery check, not a task record.
- 2026-10-13 - Recorded the engagement collapse (1,017 stars and 124 forks on 2026-10-11 to 158 and 46 on 2026-10-13, a drop forks cannot take organically), retracted the nineteen-day adoption-curve claim, and moved the caution from momentum to deflation.
- 2026-10-14 - Recorded the re-inflation (158 to 239 stars and 46 to 51 forks in one day, fresh-account engagement continuing), extending the 10-13 collapse reading from a one-time purge to a purge-then-refill pattern.
- 2026-10-17 - Recorded the v1.4.0 release (2026-10-16: the description trimmed to fit a 500-character harness cap whose truncation was dropping the skill's negative predicates, a DeepSeek Harness eval channel, and a cross-session contract test case).

## See also

- [GitHub Spec Kit](../spec-kit/index.md) - the full-workflow contrast on the same shelf
- [Superpowers](../superpowers/index.md) - the mandatory-workflow skill suite this is the opt-in opposite of
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins
- [Jev](../../hybrid-execution/jev/index.md) - the typed decision layer this positions itself upstream of

## References

- https://github.com/angel291592/Intent-Router - repository: README, pipeline, comparison table, license
- https://api.github.com/repos/angel291592/Intent-Router - stars, forks, issues, creation and push dates, the 1,017-to-158-to-239 readings, as of 2026-10-14
- https://api.github.com/repos/angel291592/Intent-Router/releases - v1.4.0 published 2026-10-16 and the release train
- https://raw.githubusercontent.com/angel291592/Intent-Router/main/README.md - the convergence design, artifact model, and prior-art comparison
- https://raw.githubusercontent.com/angel291592/Intent-Router/main/evals/reports/2026-09-24-delivery-opencode.md - the self-published delivery report behind the numbers and the contamination check
- https://hn.algolia.com/api/v1/search?query=Intent-Router&hitsPerPage=5 - the no-thread community-footprint check as of 2026-10-11
