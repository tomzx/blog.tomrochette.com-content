---
title: Hunk
created: 2026-10-06
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, evaluation, code-review, terminal, diff, human-in-the-loop]
readability: 3
audience_notes: >
  Engineers reviewing agent-authored diffs in a terminal who want the whole changeset as one readable stream with the agent's reasoning inline.
  Assumes you know what a unified diff is.
---

Hunk is a free, MIT-licensed, review-first terminal diff viewer from Modem, built to review agent-authored changesets as one multi-file stream with the agent's annotations rendered beside the code they explain.

**Hunk judges nothing itself: its whole product is making the human's read of the changeset faster, which makes it the terminal counterpart to a browser review surface like Plannotator.**

## What it is

A TUI built on OpenTUI and Pierre diffs that reviews working trees, commits, GitHub PRs, patches piped from stdin, and raw file comparisons in one scrollable stream with a sidebar.
Agents annotate inline: a session comment API (hunk session comment add and apply) drops summary, rationale, and author above the hunk it explains, and a bundled skill file (hunk skill path) teaches any agent to drive a live review session from another terminal.
Git, Jujutsu, and Sapling are first-class (native revsets per VCS), watch mode reloads as the tree changes, and Hunk doubles as a pager and git difftool.
Install paths are a standalone binary (a checksum-verified install script), npm hunkdiff, Homebrew, mise, and Nix, on macOS, Linux, and Windows; extensions are plain TypeScript; it also ships as a default tool in Omarchy.
The maker is Modem (modem.dev), the company credited in hunk.dev's footer.

## Status

Fast-growing and young: 9,515 stars and 310 forks as of 2026-10-06, created 2026-03-17, pushed 2026-10-06, v0.23.0 (2026-09-30) with 741 merged pull requests.
hunkdiff npm installs ran about 4.6k in the week of 2026-09-28 to 2026-10-04.
Endorsements from Mitchell Hashimoto and DHH are quoted on the site (the X posts themselves did not fetch this run), while the HN footprint is three stories totaling 7 points with almost no comments, the same social-channel growth pattern Plannotator recorded.

## Strengths

- One surface for the whole changeset, instead of per-file paging through a plain diff.
- Agent reasoning in context, above the hunk it explains, labeled separately from human notes.
- Live-session control: the agent steers the running review rather than dumping a diff.
- First-class Jujutsu and Sapling support, which the terminal diff incumbents lack.

## Cautions

- It renders and annotates but decides nothing: no metrics, no CI gate, no machine verdict, so pair it with a judging column from this category.
- Pre-1.0 with fast churn: 0.21 through 0.23 all landed within September 2026.
- The curl-pipe install script is the default path (checksum-verified with a GitHub fallback), worth weighing for supply-chain-sensitive teams.
- Thin independent discussion: almost nobody has publicly argued with it yet, so the endorsements are the main third-party evidence.

## Pricing

Free and open source under MIT.
No paid tier is recorded for Hunk or its maker (as of 2026-10-06).

## Compared to

- [Plannotator](../plannotator/index.md): the browser sibling, with plan review and hooks in nine harnesses; Hunk is terminal-native and PR-aware through hunk gh, but its annotations do not feed back into a live harness session the way Plannotator's do.
- delta and difftastic: the terminal diff incumbents render prettier diffs but offer no review UI, no multi-file stream, and no annotation surface, per Hunk's own comparison table.
- lumen: the closest clone by that same table, matching the review-first stream without the inline agent annotations.

## Bottom line

**Recommended for engineers whose agent loop ends in a terminal and who want one fast, annotated read of everything the agent touched.**
Not for CI gating and not for anyone expecting a machine verdict; Hunk deliberately judges nothing.

## Changes

- 2026-10-06 - Created.

## See also

- [Plannotator](../plannotator/index.md) - the browser-based sibling review surface
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category comparison this note joins
- [OpenCodeReview](../../code-review/open-code-review/index.md) - the machine-reviewed counterpart for the same diffs

## References

- https://github.com/modem-dev/hunk - repository, counts, and topics as of 2026-10-06
- https://api.github.com/repos/modem-dev/hunk/readme - features, install paths, the agent workflow, and the comparison table
- https://api.github.com/repos/modem-dev/hunk/releases - the v0.23.0 line and cadence
- https://hunk.dev - the product pitch, endorsement quotes, and the Modem attribution
- https://hunk.dev/docs/agents/comments-and-annotations/ - the session comment API behind the inline annotations
- https://hunk.dev/docs/agents/review-with-an-agent/ - the skill-file and session-command agent workflow
- https://api.npmjs.org/downloads/point/last-week/hunkdiff - the weekly npm install count
- https://hn.algolia.com/api/v1/items/48043804 - the largest HN story, 4 points and zero comments, cited as the thin-footprint signal
