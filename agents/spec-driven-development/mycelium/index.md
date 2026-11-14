---
title: Mycelium
created: 2026-10-16
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, spec-driven-development, product-discovery, claude-code-plugin]
readability: 3
audience_notes: >
  Engineers building agent-built products who want discovery enforced in the harness,
  not suggested in a prompt.
  Assumes you know what a Claude Code plugin and a spec contract are.
---

Mycelium is a MIT Claude Code plugin that structurally gates implementation on a discovery contract: the agent cannot create a new source file until four questions (what is the problem, who has it, what are you assuming, what would show you wrong) are answered into YAML the repo keeps.

**The gate is hooks, not prose: it holds the agent's first source file until the brief exists, and the brief grades its own evidence (`validated: false`, `strength: speculation`), so the spec records how much is known, not only what is planned.**

## What it is

A plugin installed through Claude Code's marketplace (`/plugin marketplace add haabe/mycelium`) from Håvard Bartnes (haabe), with the files and skills documented as porting to OpenCode, Codex, and Cursor.
`/mycelium:start` sets up the `.claude/` state and asks the four questions once per repo, writing `.claude/canvas/purpose.yml` and `jobs-to-be-done.yml`, a decision log at `.claude/harness/decision-log.md`, and delivery diamonds at `.claude/diamonds/active.yml`.
Sixty-three optional skills carry the method above the gate, grouped across six layers from purpose (L0) to market (L5) and named for their theories: Jobs To Be Done, Wardley maps, Cynefin, DORA, Opportunity Solution Trees.
The standing cost is about six thousand tokens of context per session, always on.

## Status

Active and shipping fast: 47 stars, 5 forks, created 2026-04-07, pushed 2026-11-13, as of 2026-11-14 (GitHub API).
Pre-1.0 by the author's own framing, with schema and skill names moving between minor versions, and the release train runs in hours: v0.337.1 (2026-11-13) is the newest, a self-audit of the plugin and the steward's dogfood project that fixed three things found wrong (the session-start, session-end, and reflexion-reconcile counters now count corrections the way the prompt line does, where one session read 244 corrections at start and 447 in memory from the same file; a correction written as a dated heading or dated bullet now answers a reflexion, with the ledger naming the counter its baseline was taken with; and pages that said what is no longer so, a 45-skills claim against the 63 skills that exist among them), following v0.337.0 (2026-11-12), the twenty design rulings the maintainer made by interview over his upstream-candidate triage built as changes (a team-only exposure is its own trial at L3, a service check can be scoped to one exposure, viability asks "should we build it" pointing at /mycelium:harms-check, a blind second view runs by default after /mycelium:wardley-map and can only raise concerns, never pass anything, "make compliance the cheapest option" is a design principle, and handoff, user-interview, and launch-tier skills write take-away files the person will use later), following v0.336.0 (2026-11-12), the second and third triage releases shipped together (a Monitor command's changes are compared at turn end, the gate's own preflight run no longer spends the session's background checks, and the closing path reads door-opened diamonds), following v0.335.0 (2026-11-12), the first release from a triage of 85 open entries in the maintainer's own upstream-candidates list and the material one for the gate, because the hooks now run on the Python 3.9 a stock Mac ships (31 hook files used 3.11-only forms and seven modules failed to import there, with the fire logs discarding their errors, so on stock macOS the gates silently did not run at all, which a CI test now checks by importing all 68 hook modules under any Python older than 3.10), beside atomic writes for the background session checks that could lose their pending marker and shell-safety rules that read commands instead of quoted text, replayed over 11,134 of the steward's real commands, following v0.334.1 (2026-11-06), a docs-only release whose eighth `/mycelium:xai-check` measured the 0.311.0 citation requirement at 284 of 284 `Next:` lines citing a source and ran the first blind-prediction faithfulness audit (a fresh reviewer predicted the proposed action in 8 of 10 lines), following v0.334.0 (2026-11-06) declaring the `scenario_gap` field on an opportunity with `validate_canvas` counting the gaps, and v0.333.0 (2026-11-06) moving scored keys into dated notes with the instrument, purpose-hash, and related checks fixed to read the result, on top of v0.332.0 (2026-10-31) shipping a native Agent Plugins 1.0 manifest so the folder loads as it ships on Mistral Vibe, whose plugin loader binds no hooks a plugin ships, meaning v0.328.3's workaround had loaded the skills while none of the gates ran there, and the discovery, release, and scale-lock gates now run on Vibe for the first time, of a train that ran v0.323 through v0.337 across October 13 to November 12.
The adoption record is small and mostly first-hand: three of the steward's own projects, a three-person test cohort in May, and one stranger on record whose Lisp-interpreter canvas is public.

**The independent footprint is empty, and that is this note's critical angle: a Hacker News search returns only the maintainer's own Show HN (2026-07-04, 1 point, 0 comments) plus an earlier post he says missed the Show HN tag, with no third-party coverage anywhere, so at 47 stars this admission rides the HermesGate-at-3-stars precedent rather than any membership floor.**

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=haabe/mycelium&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=haabe/mycelium&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=haabe/mycelium&type=date&legend=top-left" />
</picture>

## Strengths

- **The gate is structural**: harness hooks hold the agent's first new source file until the brief exists, which no advisory prompt convention can promise, and a repo that already has a dozen source files is asked once, ever.
- **The artifact grades its own evidence**: `validated` and `strength` fields, with the public vibe-rant canvas marking its own idea at 0.15 confidence, give the spec an epistemic state the other members' artifacts lack.
- The steward publishes his failures: the killed macOS file-viewer receipt, and the stated falsifier that you should uninstall it and say so if the brief never once changes what you build across three projects.
- Leaving is clean: uninstall leaves the canvas as plain YAML that reads without the plugin, skip acks exist for untracked work, and the agent cannot write either without asking.

## Cautions

- The four questions run once per repo, by the author's own admission: nothing brings you back in November to check the assumptions you wrote in August, so it buys one good discovery pass unless you supply the loop.
- **Zero independent coverage**: one self-published Show HN thread, no write-ups anywhere, and an adoption record that is nearly all the steward's own, the profile that has kept thinner records out of other categories.
- The gate leaks by design: scaffolder and clone commands still write files past it, hand-committed code is unchecked unless setup adds the git check, and code declared prototype is free.
- Pre-1.0 churn is explicit, Claude Code turns auto-update on only for its own marketplaces by default, and the always-on token cost shows up on long sessions.

## Pricing

Does not apply: MIT, free, no paid tier.
The author states that if a business case exists underneath all this it is still worth giving away, and that he is not looking hard for one.

## Compared to

- [Intent-Router](../intent-router/index.md): the nearest gate-kind member, and the difference is the scope of the contract; Intent-Router compiles one request into a typed spec and checks the delivery against it, Mycelium compiles the product's purpose into an evidence-graded brief and holds the first file on it, so choose Intent-Router for per-request clarification and Mycelium for repo-level discovery discipline.
- [OpenSpec](../openspec/index.md): the brownfield spec-writing member; OpenSpec's delta proposals govern change to code that exists, Mycelium's canvas governs whether the thing should exist at all.
- [BMad Method](../bmad-method/index.md): the sized-ceremony method; BMad runs a team process with roles and retrospectives, Mycelium is one solo founder's gate with 63 skills you may never invoke.

## Bottom line

**Recommended for solo builders starting agent-built products who want the discovery questions structurally in the agent's way, at the price of ten minutes up front and about six thousand tokens a session.**
Not for teams needing a stable interface (pre-1.0, schema moves between minors), throughput work with the decision already made (the author routes you elsewhere himself), or anyone who requires independent validation before adopting.

## Changes

- 2026-10-16 - Created from the awesome-claude-code addition the cross-category scanner flagged, admitted under the Intent-Router gate-kind precedent (a spec contract is spec-driven even when tracker-adjacent), with the zero-coverage record as the critical angle.
- 2026-10-21 - Recorded the v0.328.1 and v0.328.2 releases (both 2026-10-20): the OpenCode 2.x plugin port now guards `write` as well as `edit`, extending the structural gate past Claude Code.
- 2026-10-23 - Recorded the v0.328.3 through v0.328.5 releases (2026-10-21 to 23): a Mistral Vibe page after the Vibe port measured as loading nothing, diamond skills that stop for the person's own judgment before showing analysis, and a session-start hook naming the next canvas-health advisory.
- 2026-10-25 - Recorded the v0.329.x and v0.330.x releases (2026-10-23 to 24): review cadences became data with an adaptive corrections-audit cadence, and the canvas gate now refuses a subagent's writes to the canvas and diamonds files on Claude Code, closing the enforcement gap the founder's own audit found.
- 2026-10-31 - Recorded the v0.331.0 release (2026-10-28: the release and scale-lock gates read each safety skill's own assessment record, so a Privacy, Service Quality, or Explainability pass without every principle judged with evidence refuses the next release).
- 2026-11-01 - Recorded the v0.332.0 release (2026-10-31: a native Agent Plugins 1.0 manifest, so the Mistral Vibe port loads the plugin as shipped and the gates run there for the first time; Vibe binds no hooks a plugin ships, so the earlier workaround loaded the skills only).
- 2026-11-07 - Recorded the v0.333.0 through v0.334.1 releases (all 2026-11-06: scored keys moved into dated notes with the reading checks fixed, the `scenario_gap` field declared and counted, and the eighth xai-check measuring 0.311.0's citation requirement at 284 of 284 Next lines alongside the first blind-prediction faithfulness audit).
- 2026-11-12 - Recorded the v0.335.0 release (2026-11-12: the hooks run on the Python 3.9 a stock Mac ships, where 3.11-only forms had seven modules failing import with the fire logs discarding their errors and the gates silently not running, now checked in CI by importing all 68 hook modules under an older Python, beside atomic session-check writes and shell-safety rules that read commands instead of quoted text).
- 2026-11-13 - Recorded the v0.336.0 and v0.337.0 releases (both 2026-11-12: the second and third upstream-candidate triage releases shipped together, with Monitor-command changes compared at turn end and the gate's own preflight no longer spending background checks, then the twenty design rulings from the maintainer's interview built as changes, including a team-only exposure its own L3 trial, a default blind second view after wardley-map that can only raise concerns, and handoff take-away files).
- 2026-11-14 - Recorded the v0.337.1 release (2026-11-13: a self-audit of the plugin and the dogfood project whose correction counters in session start, session end, and reflexion reconciliation now count entries the way the prompt line does, a dated-heading or dated-bullet correction now answers a reflexion with the ledger naming its counter baseline, and the stale pages fixed, the 45-skills claim against 63 among them).

## See also

- [Intent-Router](../intent-router/index.md) - the nearest gate-kind member, request-scoped where Mycelium is product-scoped
- [OpenSpec](../openspec/index.md) - the brownfield spec ledger, change-scoped where Mycelium is existence-scoped
- [BMad Method](../bmad-method/index.md) - the team-sized method this solo gate contrasts with
- [Spec Driven Development Feature Matrix](../spec-driven-development-feature-matrix/index.md) - the category comparison this note joins
- [HermesGate](../../evaluation-review/hermes-gate/index.md) - the 3-star gate whose admission precedent this note rides

## References

- https://api.github.com/repos/haabe/mycelium - 47 stars, 5 forks, MIT, topics including spec-driven-development, created 2026-04-07 (47 stars as of 2026-10-23), pushed 2026-11-13, as of 2026-11-14
- https://raw.githubusercontent.com/haabe/mycelium/main/README.md - the gate design, artifact model, token cost, falsifier, six layers, porting, and when-to-use-something-else routing
- https://raw.githubusercontent.com/haabe/mycelium/main/docs/get-started.md - install, the four questions, artifact paths, gate behavior, and the skip-ack files
- https://raw.githubusercontent.com/haabe/mycelium/main/docs/skills/README.md - the 63-skill index, layer model, and theory attributions
- https://api.github.com/repos/haabe/mycelium/releases - the release train through v0.337.1 (2026-11-13), fetched 2026-11-14
- https://github.com/haabe/vibe-rant - the steward's public canvas repository (0 stars, 1 commit)
- https://raw.githubusercontent.com/haabe/vibe-rant/main/.claude/canvas/purpose.yml - the evidence fields (`validated: false`, `strength: speculation`) in the published artifact
- https://raw.githubusercontent.com/dagfinndybvig/minilisp/main/.claude/canvas/gist.yml - the one stranger's public canvas, grounding the third-party-use record
- https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/main/README.md - the listing entry naming the steward and the four-question gate
- https://hn.algolia.com/api/v1/search?query=mycelium%20claude&hitsPerPage=8 - the footprint check: only the maintainer's Show HN at 1 point and 0 comments, the zero-coverage record
