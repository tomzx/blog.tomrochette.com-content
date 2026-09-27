# MEMORY

## Scheduled agent skills (user's setup, confirmed 2026-09-22)

- Three skills run hourly via a local scheduler, defined in `~/src/agents/skills/`: `review-requested-prs` (prepares PRs waiting on his review), `handle-failing-pr-ci` (fixes failing CI on his own PRs, bounded fix loop), `triage-pr-feedback` (writes reply recommendations per reviewer comment; user approves implement/decline/defer).
- `~/src/agents/.github/llmaw/flows.yml` is the event-driven GitHub label state machine (LLM-Augmented Workflows), distinct from the scheduled skills. Schedule is used for repos the user does not control; events for repos he does.
- OpenChamber scheduled tasks in the blog project: "Update principles" (monthly), "agents-section-daily-refresh" (daily 03:00 America/Toronto).
- Skill library is public: https://github.com/tomzx/agents/tree/main/skills (safe to link in articles).

## Blog conventions worth recalling

- New articles: `status: draft` until user says otherwise; AI tags `fully-ai-generated, llm=glm-5.3-flash` on agent-written pieces; `agent_sessions` gets the current session ID (available via openchamber session.list, first entry).
- Avoid the word "shape" even in headings/diagram titles; "pipeline"/"pattern" preferred.
- Article images: hand-authored SVG in `images/` next to `index.md`, presentation attributes only (no `<style>` block), muted palette with single `#2563eb` accent; see `how-much-attention-does-this-pull-request-deserve/images/routing-matrix.svg` for the established style. xmllint/rsvg-convert unavailable on this machine; validate with Python ElementTree.
- Matrix-table gotcha (2026-09-27): when extending a feature matrix by script, the `| --- |` separator row is skipped by per-cell permutation code and stays at the old width, which breaks GFM rendering; the assistant-runtimes report let it through twice. Any matrix audit must check separator AND every row's cell count equals the header's.
