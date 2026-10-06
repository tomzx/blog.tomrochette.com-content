---
title: Delta
created: 2026-10-04
updated: 2026-10-06
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surfaces, agentic-development-environments, version-control, code-review, multiplayer]
readability: 3
audience_notes: >
  Engineers whose review workflow is straining under agent-generated diffs, who want to know what Zed Industries' Delta actually replaces and what it costs in trust.
  Assumes you know what a pull request, a worktree, and a CRDT are.
---

Delta is Zed Industries' multiplayer environment for coding with agents, in public beta since 2026-09-16, where the unit of work is a thread (a conversation bundled with its own worktree copy) and pull requests are replaced by review inside the thread.

**Delta is the first serious attempt to make the conversation that produced the code the reviewable artifact itself, and its bet is credible precisely because its maker runs its own development on it, but the same design moves your code and your agent transcripts onto Zed's servers, which is a trade many teams will refuse.**

## What it is

A desktop app (macOS, Linux, Windows), a web client, and a mobile browser view, built by Zed Industries on DeltaDB, the version-control layer the company announced on 2026-06-11.
DeltaDB records every operation between commits as a delta with a stable identity, keeps conversation messages and the edits they produced side by side, and stores conflict-free replicated worktrees, so a commit remains the checkpoint you push while the work between checkpoints becomes addressable history.
Your repository stays a normal Git repository: commits, branches, and remotes work as before, and teammates who never open Delta see a normal Git clone.
Threads run in parallel, each with its own Delta worktree, are revertible to any earlier point (conversation and files rewind together), and are shareable, so a reviewer joins the thread, sees the same worktrees, and can ask the same agent why a decision was made.
Zed disabled pull requests on Delta's own repository at launch and reports building it entirely inside Delta, 33 people landing 570 changes to main as of the beta announcement.

## Status

**Active and early: public beta since 2026-09-16, free during beta, closed source.**
The DeltaDB announcement (2026-06-11) drew a 529-point Hacker News thread, and the public-beta announcement (2026-09-16, "Replace PRs with Delta") drew 154 points with 102 comments as of 2026-10-04, a comment count that signals argument rather than drive-by attention.
Shipping cadence is visible on the Delta blog: a harness-eval piece on 2026-09-24 and a planning-in-Delta piece on 2026-10-01.
DeltaDB itself has no public release; the open-source release thread commenters ask about has not shipped.
The beta requires signing in and accepting beta terms, and the product is the founder-led bet of one vendor whose editor is the adjacent product.

## Strengths

- **The thread is a durable artifact, not a log: conversation and edits are recorded together, revert together, and can be handed to a reviewer with the original agent's context attached.**
- Review happens where the work happened: review subthreads get isolated copies of the parent worktrees, so reviewers can explore and fix without disturbing the source thread.
- The Git exit is preserved: a repository used through Delta remains a normal Git repository, so adoption is per-thread rather than all-or-nothing.
- Every surface is covered, desktop, web, mobile browser, and cloud runners, which no other agentic environment in this category ships at beta quality.

## Cautions

- **Your repository contents and your agent conversations are stored on Zed's servers (Cloudflare R2, Durable Objects, KV, and D1), account deletion is email-only, and the docs themselves state that Delete Locally does not remove server copies, exactly the combination the beta thread's privacy commenters flagged.**
- Untracked files Git does not ignore are imported into DeltaDB too, so the upload surface is wider than the commits you would have pushed.
- No merge gating or CI enforcement: the thread's sharpest technical criticism is that landing stays a skill the agent executes rather than a check the remote enforces, and the announcement defers CI-style verification to the roadmap.
- Closed client and closed DeltaDB: you cannot audit either, and the harness coupling (their editor, their agent runner) was the second-most common objection in the thread.
- The replace-GitHub framing outruns the product: Git storage in DeltaDB and content-based builds are future work, and a reviewer who wants a distilled summary rather than a colleague's 100-turn transcript will not find one here.

## Pricing

Free during the public beta, with paid plans promised for individuals and teams and a stated permanent free version.
The published ladder shares accounts and credits with Zed: Personal at $0/month (bring your own keys or external agents) and Pro at $10/month ($5 of tokens included, Zed-hosted models, usage-based beyond), as of 2026-10-06 (re-verified, unchanged).

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-04 | Personal, Pro | Baseline observed at beta: Personal $0/month (BYOK or external agents), Pro $10/month with $5 of tokens included, accounts and credits shared with Zed; free during beta with paid plans promised. | [delta.dev/pricing](https://delta.dev/pricing) |

## Compared to

- [Zed](../zed/index.md): the editor that coexists with it; Delta is the collaboration layer beside the editor, sold on the same account, so the choice is not editor versus environment but whether the thread layer earns its server-side storage.
- [OpenChamber](../openchamber/index.md): the open, local-first session cockpit; OpenChamber keeps code and conversations on your machine under MIT, Delta trades that ownership for multiplayer review and hosted history.
- [Cursor](../cursor/index.md): the platform rival that kept pull requests; Cursor's cloud agents land as PRs into your existing forge, Delta asks the team to move review itself into threads.

## Bottom line

**Recommended for small teams whose review bottleneck is missing context, working on code they are willing to place on Zed's servers during a beta.**
Not for proprietary or regulated code with strict egress rules, and not for anyone who needs merge gating enforced by the remote today.
The disagreeable claim I will defend: the durable idea here is not replacing GitHub, it is making a thread revertible, because conversation-plus-edits-as-one-history is the first review primitive that matches how agents actually work, and the GitHub-replacement rhetoric only raises the odds competitors ship the revertible part without the lock-in.

## Changes

- 2026-10-04 - Created from the entrant scan after the 2026-09-16 public beta cleared the bar (DeltaDB thread at 529 points, beta thread at 154 with 102 comments, six sources fetched including the vendor's own data-storage doc conceding the deletion caveats).

## See also

- [Zed](../zed/index.md) - the editor from the same vendor, whose plans and credits Delta shares
- [OpenChamber](../openchamber/index.md) - the open-source, local-first answer to the same parallel-sessions problem
- [Cursor](../cursor/index.md) - the platform rival that kept the pull-request workflow Delta removes
- [Rolling Out the Unread Review](../../../rolling-out-the-unread-review/index.md) - what a review process change like this has to survive organizationally

## References

- https://delta.dev/ - the product site: threads pitch, surfaces, early-adopter quotes
- https://zed.dev/blog/delta-public-beta - the 2026-09-16 public beta announcement: PRs disabled on its own repo, 33 people and 570 changes, free during beta, replace-GitHub framing
- https://zed.dev/blog/introducing-deltadb - the 2026-06-11 DeltaDB announcement: deltas with stable identities, message-and-edit pairing, CRDT worktrees
- https://delta.dev/docs/concepts/core-concepts - threads, projects, and Delta worktrees, and the Git-compatibility guarantee
- https://delta.dev/docs/privacy-and-security/data-storage - what is stored server-side, the Cloudflare backend, email-only deletion, and what Delete Locally does not remove
- https://delta.dev/pricing - Personal $0 and Pro $10/month, accounts and credits shared with Zed, as of 2026-10-06
- https://news.ycombinator.com/item?id=49727245 - the beta thread (154 points, 102 comments as of 2026-10-04): the merge-gating, privacy-upload, and why-not-a-PR criticisms, plus positive beta-user reports
