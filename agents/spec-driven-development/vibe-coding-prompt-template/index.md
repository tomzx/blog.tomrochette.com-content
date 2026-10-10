---
title: Vibe Coding Prompt Template
created: 2026-10-07
updated: 2026-10-09
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, prompts, workflow, open-source]
readability: 3
audience_notes: >
  Engineers and non-engineers choosing a spec-first workflow and wondering whether the discipline really needs a CLI.
  Assumes you know what a PRD and a tech design are.
---

Vibe Coding Prompt Template (KhazP) is an MIT-licensed pack of four copy-paste prompts that turns an idea into research findings, a PRD, and a tech design in any chat tool, then hands the artifacts to your coding assistant as instruction files before any code is written.

**It is the zero-install floor of the spec-driven movement: no CLI, no gates, no skills, just a sequence that makes you produce the spec artifacts anyway, and about 3.1k stars say that floor is where a large part of the audience actually lives.**

## What it is

Four self-contained markdown prompts, branded Vibe Workflow: Part 1 drafts a research request, Part 2 interviews you into a PRD with must-have boundaries and a Handoff Context block, Part 3 produces a technical design with stack and structure, and Part 4 generates the agent instruction files (`AGENTS.md`, `MEMORY.md`, `REVIEW-CHECKLIST.md`, plus `agent_docs/` briefs) that carry the plan into Claude Code, Cursor, Gemini, ChatGPT, or VS Code.
You paste each prompt into a fresh chat, attach the previous document, and save the result under `docs/` in your project folder.
The Part 2 prompt asks you to self-select your level, vibe-coder, developer, or in between, and tunes its questions accordingly, so the intended reader is explicitly not a staff engineer.
A small npm CLI (`npx vibeworkflow`, v0.3.0) wraps the same flow for people who want it scripted, but the README is direct that no installation is required.

## Status

Active, solo-maintained, and adopted without the front page.
As of 2026-10-09: 3,131 stars and 386 forks since creation on 2025-04-14, pushed 2026-10-04, MIT, solo author (the KhazP user account), with release v3.1.0 (2026-08-20) the newest of eight.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=KhazP/vibe-coding-prompt-template&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=KhazP/vibe-coding-prompt-template&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=KhazP/vibe-coding-prompt-template&type=date&legend=top-left" />
</picture>

**Its Hacker News footprint is two tiny threads (6 points in April 2025, 2 points in January 2026), so the 3.1k stars accumulated without any front-page moment, and the npm CLI it grew into records only 230 downloads last month (the 2026-09-08 to 2026-10-07 window), which says almost everyone uses the raw prompts.**
It entered this category's scan as a Specification Tools entry on the Engineering4AI awesome list.

## Strengths

- **Zero installation is the lowest adoption floor in this category: the whole workflow is four pastes in a chat window, which is why it out-stars several columns with far more machinery.**
- The Handoff Context blocks make each fresh chat inherit the prior decisions, the same durable-context idea BMad sells, implemented as prompt convention.
- The artifact spine (research, PRD, tech design, agent instruction files) is the same spec-before-code sequence the CLIs enforce, so graduating to one later is a lift, not a restart.
- Asking the reader to self-select their level inside the prompt is rare audience-awareness in a category that mostly writes for experts.

## Cautions

- **Nothing enforces anything: there are no gates, no review evidence, no convergence check beyond the model rereading the PRD, so the ceremony is only as strong as the human choosing to paste it.**
- Greenfield only: the flow starts from an idea in a fresh folder, with no path for the existing repos the delta-spec members serve.
- Solo maintainer, a pre-1.0 CLI, and self-reported showcase projects; independent coverage is absent this run, so the claims rest on its own README.
- The spec quality ceiling is the chat model's interviewing skill, unbenchmarkable and unversioned, and the workflow drifts every time the prompts change.

## Pricing

Free and open source under MIT.
Both the prompt pack and the npm CLI are open; no paid tier exists.

## Compared to

- [GitHub Spec Kit](../spec-kit/index.md): the movement root enforces the same sequence through a CLI and templates; choose Spec Kit when the ceremony must be structural, the prompt pack when you want to try spec-first with nothing installed.
- [OpenSpec](../openspec/index.md): the brownfield ledger versions specs across changes on a live repo; the prompt pack is the greenfield idea-stage counterpart.
- [BMad Method](../bmad-method/index.md): the full method packages the same planning conversation into roles and modules; the prompt pack is what remains when you strip the method to its interviews.

## Bottom line

**Recommended for solo and non-expert builders starting a new project who want the spec-before-code discipline without installing anything.**
Not for teams that need gates, review evidence, or brownfield support, and not for anyone whose workflow collapses without enforcement.
The disagreeable claim I will defend: four markdown files out-starring several engineered columns in this category is evidence that the movement's binding constraint is the blank page, not the enforcement, and the tools that win the next year may be the ones that ask the right questions rather than the ones that check the answers.

## Changes

- 2026-10-07 - Created from the awesome-list entrant scan, profiling KhazP/vibe-coding-prompt-template as the category's zero-install prompt-pack column.
- 2026-10-09 - Refreshed counts (npm CLI downloads down to 230 last month); the everyone-uses-the-raw-prompts conclusion stands.

## See also

- [GitHub Spec Kit](../spec-kit/index.md) - the CLI-enforced version of the same sequence
- [OpenSpec](../openspec/index.md) - the brownfield ledger alternative
- [BMad Method](../bmad-method/index.md) - the method-heavy alternative to the same planning conversation
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/KhazP/vibe-coding-prompt-template - repository: stars, forks, dates, license, releases (3,131 stars as of 2026-10-09)
- https://raw.githubusercontent.com/KhazP/vibe-coding-prompt-template/main/README.md - the five-step workflow table, artifact paths, and no-install framing
- https://raw.githubusercontent.com/KhazP/vibe-coding-prompt-template/main/part2-prd-mvp.md - the PRD prompt: audience self-selection, Handoff Context, must-have boundaries
- https://registry.npmjs.org/vibeworkflow - the CLI wrapper: v0.3.0, MIT, description
- https://api.npmjs.org/downloads/point/last-month/vibeworkflow - 230 downloads last month, fetched 2026-10-09
- https://hn.algolia.com/api/v1/search?query=vibe-coding-prompt-template&tags=story - the thin HN footprint, checked 2026-10-07
- https://github.com/Engineering4AI/awesome-spec-driven-development - the curated source that surfaced the candidate
