---
title: PR Lens
created: 2026-10-10
updated: 2026-10-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation-review, code-review, visualization, pull-requests]
readability: 3
audience_notes: >
  Reviewers drowning in agent-authored pull requests who want to understand a change before reading the diff.
  Assumes you know what a GitHub App and an architecture diagram are; it judges nothing itself.
---

PR Lens draws every pull request as animated architecture and data-flow diagrams, posted as a comment inside the pull request itself, so a reviewer sees what changed before reading a line of code.

**The open-source core is a review surface, not a reviewer: the diagrams carry no verdict, the human still judges the change, and that puts it next to Hunk and Plannotator as the third column here whose job is making the human's judgment faster, though the vendor's hosted App now adds model-authored findings on top of the drawing.**

## What it is

An MIT tool from the coldtea organization (prlens.dev) with four delivery surfaces: a GitHub App that comments on every push, a GitHub Action, an npm CLI (`@coldtea/pr-lens-cli`, 0.13.2 published 2026-10-17) that renders a diff into a schema-valid graph with your own model key, and an agent skill installed with `npx skills add coldteadotai/pr-lens`.
The renderer is custom rather than Mermaid, and draws a blast-radius view (green new, amber changed, red removed components against the surrounding system), step-by-step data-flow animations, payload panels on every arrow, folding sections for zoom, and a full-size interactive canvas with walkthroughs.
Your coding agent can also connect to the canvas live: questions in the terminal come back as annotated diagram steps.
The hosted App's comment now goes beyond the drawing: the product site's setup flow says the App posts the diagrams plus a code review that flags bugs and security problems ranked by risk, with autofix and agent prompts, while the Action, CLI, and skill draw only (the site tells would-be Action users the code review "only comes with" the hosted App).
The README documents none of that, only the drawing surfaces plus GitLab and Bitbucket support alongside GitHub, so the judging layer lives in the closed hosted tier, not this MIT repository.

## Status

New and moving fast: 1,954 stars and 71 forks as of 2026-10-13, created 2026-08-20, pushed 2026-10-25, with v0.13.1 published 2026-10-17 as the newest release and the v0.13 train now two deep.
Reaching 1.9k stars in seven weeks is strong adoption for a review tool, though the independent footprint is small: a Hacker News search finds three Show HN threads (6 points on 2026-08-27, 4 points on 2026-10-05, 4 points on 2026-09-17), none above single digits.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=coldteadotai/pr-lens&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=coldteadotai/pr-lens&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=coldteadotai/pr-lens&type=date&legend=top-left" />
</picture>

## Strengths

- The blast-radius view answers the first reviewer question (what does this touch) in one image instead of twelve file diffs.
- Payload panels and walkthroughs turn a diff into a reviewable narrative, which is exactly what agent-authored pull requests need.
- Four surfaces (App, Action, CLI, skill) mean it fits a human review flow, a CI flow, or an agent flow without new infrastructure.
- Free for open source and MIT, with the CLI using your own model key, so the cost model stays visible.

## Cautions

- The diagrams are model-generated interpretations: nothing in the fetched material verifies that a drawn call or payload matches the code, so a confident diagram can mislead exactly like a confident summary.
- The hosted App's review findings are the same class of model output with the stakes raised: bug and security claims, ranked by risk, from a vendor model with no published accuracy measurement, and they exist only in the closed hosted tier, not the MIT repository.
- The MIT core judges nothing, so its reviewer speed comes with zero defect detection; the hosted App's findings fill that slot only behind the vendor's hosted service.
- The project is seven weeks old with a v0.x train, so comment format, canvas URLs, and CLI flags should be expected to move.
- The community footprint is single-digit Hacker News threads; the star curve has not yet converted into public discussion of accuracy in practice.

## Pricing

Free for open source, MIT-licensed, with the CLI and skill running on your own model key.
No paid tier is recorded in the fetched material as of 2026-10-11.

## Compared to

- [Hunk](../hunk/index.md): the terminal diff viewer for agent changesets; choose Hunk when you review in the terminal, PR Lens when review happens on the pull request itself and diagrams beat diffs.
- [Plannotator](../plannotator/index.md): the annotation surface that steers a live agent; both make humans faster without judging, Plannotator mid-task and PR Lens at review time.
- [CodeRabbit](../../code-review/coderabbit/index.md): the commercial anchor that actually judges; pair a judging reviewer with PR Lens rather than choosing one as a substitute for the other.

## Bottom line

**Recommended for teams reviewing large agent-authored pull requests who want comprehension help without adopting another judge.**
Not for defect detection from the open-source core (it renders, not judges), and not where diagram accuracy must be guaranteed, since nothing verifies the model's reading of the diff.

## Changes

- 2026-10-10 - Created from the code-review resolution pass and placed in this category rather than code review, because the diagrams judge nothing: it joins Hunk and Plannotator as a human-review surface.
- 2026-10-18 - Recorded the v0.13.1 release (2026-10-17), the npm CLI at 0.13.2, and the refreshed activity line.
- 2026-10-25 - Rotation re-verification: every cited URL re-fetched and live; recorded that the hosted GitHub App now posts model-authored review findings (risk-ranked bug and security flags with autofix prompts) alongside the diagrams, a capability the MIT Action, CLI, and skill do not carry, and refreshed the activity line.

- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart light-source markup (the light source carried the dark-theme parameter; it now points at the default chart).

## See also

- [Hunk](../hunk/index.md) - the terminal sibling that also judges nothing
- [Plannotator](../plannotator/index.md) - the mid-task annotation surface
- [ReviewBench](../reviewbench/index.md) - the benchmark for the judging tools this note deliberately is not
- [Code Review Feature Matrix](../../code-review/code-review-feature-matrix/index.md) - where the judging reviewers live

## References

- https://github.com/coldteadotai/pr-lens - repository: README, surfaces, license, renderer claims
- https://api.github.com/repos/coldteadotai/pr-lens - stars, forks, issues, creation and push dates as of 2026-10-11
- https://api.github.com/repos/coldteadotai/pr-lens/releases - v0.13.1 published 2026-10-17 and the release train
- https://prlens.dev - product site: the worked example, the canvas, and the hosted App's diagrams-plus-code-review setup flow (as of 2026-10-25)
- https://registry.npmjs.org/@coldtea/pr-lens-cli - CLI version 0.13.2 published 2026-10-17 and its own-model-key description
- https://hn.algolia.com/api/v1/search?query=prlens&hitsPerPage=5 - the three Show HN threads and their point counts, as of 2026-10-11
