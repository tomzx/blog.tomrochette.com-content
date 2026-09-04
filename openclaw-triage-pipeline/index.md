---

title: "The Bot Reads the Queue First: How OpenClaw Processes Thousands of Issues and Pull Requests"
created: 2026-07-26
type: post
status: finished
tags: [open-source, software-engineering, github, automation, llm, ai, triage, code-review, agents, openclaw, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader maintains or co-maintains a public GitHub repository, has watched an issue or pull request backlog grow past what one person can read, and understands labels, GitHub Actions, and what an LLM coding agent is. No introduction to what a pull request or a triage bot is.
agent_sessions:
  - ses_0e49f60a2ffe091GR3mG0gyHAd
  - ses_05e60ba69ffeVBjFhys7fcMWw3
---

A popular open source repository does not drown in code.
It drowns in input.
**The inflow of issues and pull requests scales with the project's popularity, and the maintainer's reading bandwidth does not scale with anything at all, and every project that gets popular enough eventually hits the wall where the queue stops being a list and starts being a force of nature.**

[OpenClaw](https://github.com/openclaw/openclaw), the self-hosted AI assistant, hit that wall early.
By the middle of 2026 its tracker held well over a thousand open issues, and a single forty-eight hour window in early July produced more than seventy new ones.
That is a rate at which the conventional response, "we will read them as they come in," stops being a plan and starts being a lie.
At that volume a human maintainer does not triage the queue.
The queue triages the maintainer, and it wins.

The interesting thing about OpenClaw is not that it got popular.
The interesting thing is what it built in response.
What it built is a processing pipeline that has removed the human from the critical path of intake almost entirely.
**Maintainers do not read raw issues; they read bot verdicts, and the bot verdicts are produced by a conservative, lane-separated automation system called ClawSweeper that turns an unreadable flood into a sorted, labeled, rated, proof-gated work queue.**

This article is a walkthrough of that pipeline, read from the inside.
It is structured the way the queue itself is structured: by what happens to an issue or pull request from the moment it arrives to the moment a human (or the bot) acts on it.
Every architectural claim below is checked against the ClawSweeper source at commit `f2fc64e0bc743bbd6742b36e4e164cbf91c0b31a` (2026-07-02), cited in the references.
The throughline is a single design observation.
When the volume crosses a threshold, the only scalable architecture is one in which the bottleneck, the human reviewer, never touches an item that a machine could have sorted first.

## The Composition of the Inflow

Before the pipeline, the inflow.
The OpenClaw tracker is not a uniform stream of bug reports.
It is a mixture of bugs, regressions, feature requests, RFCs, integration reports from a dozen messaging channels, plugin authoring questions, and a long tail of drive-by pull requests from contributors who will never open a second one.
A sample of a hundred open issues returns thirty different label combinations, and that variety is the first thing the pipeline has to absorb.
A one-line feature request and a five-paragraph regression report with a stack trace are not the same kind of work, and they should not reach the same reviewer at the same speed.

The volume is also contributor-heavy.
Most open pull requests are not authored by maintainers.
They come from accounts that appear once or twice, they touch a single plugin, and they arrive without proof that the change actually works.
**A contributor-heavy queue is structurally different from a maintainer-heavy one, because it shifts the bottleneck from "writing the code" to "verifying the code someone else wrote," and verification at volume is exactly the job a bot pipeline is built to absorb.**

So the pipeline has two intake problems, and it solves them with two parallel flows that share an architecture but apply different vocabularies: an issue flow and a pull request flow.
Both pass through the same lanes, and the lanes are where the real design lives.

## The Four Lanes That Carry Every Item

ClawSweeper is split into four operational lanes, and their separation is the structural part of the design.
They are, in source order: review, apply, repair, and commit review.

The **review lane** is where the model does its work, and it owns the scheduler that decides what gets read and how often.
The scheduler tiers cadence because reviewer attention is not uniform, and pretending every item deserves the same read is the mistake that bankrupts the queue.
Items with target-side activity since the last review are checked hourly.
Items created in the last seven days without new activity are checked daily, as are pull requests outside the hot window and issues under thirty days old.
Older, inactive issues drop to a weekly cadence, because the answer to a year-old issue is unlikely to change between Monday and Tuesday.
A five-minute hot-intake sweep catches the newest queue edge so a fresh bug report does not wait an hour for its first read.
**Cadence is tiered because reviewer attention is not, and the scheduler is the stage that admits this asymmetry instead of pretending every item deserves the same read.**

For each item the scheduler hands it, the review lane assembles a context shard (the title, body, comment thread, and a snapshot of repository state on `main`) and hands that shard to Codex running the internal model at high reasoning, the default service tier, and a hard ten-minute per-item timeout.
The model runs with no GitHub write token, over a read-only checkout, and the review fails outright if Codex leaves tracked or untracked changes behind.
The output is a structured markdown report with one of three verdicts: keep open, close because of a specific reason, or insufficient evidence.
The review lane never closes anything itself.
It only writes proposals, which land as durable files under `records/<repo-slug>/items/<number>.md` on the `state` branch of a separate state repository, where a human could, in principle, read every one before any action is taken.

The **apply lane** is the only stage that closes items, and it is deliberately dumb.
It wakes every fifteen minutes, reads the proposals the review lane wrote, and for each one it re-fetches live GitHub state and re-validates: have new comments arrived, has a maintainer added a label, has a referencing pull request opened, has the snapshot drifted?
If anything has shifted, the proposal is discarded and the scheduler reconsiders the item on a later pass.
Only if the proposal is still consistent with the live state does the apply lane close the item, reuse the review's comment as the close explanation, and move the report to `records/<repo-slug>/closed/<number>.md`.
Apply is capped at five fresh closes per checkpoint to stay within a single GitHub App token lifetime, so a saturated run stops and waits for the next tick instead of self-dispatching indefinitely.

**The single most important design choice in the entire pipeline is that the stage that decides what to close and the stage that executes the close are different processes with different privileges.**
The model reasons without write access.
The apply lane enforces without reasoning.
Neither can run away with the queue on its own, because each one's correctness depends on the other's output, rechecked under fresh conditions.

The **repair lane** is where the pipeline can write code, and it is gated behind explicit maintainer opt-in (covered below, because it inverts the read-only posture of the other lanes).
The **commit review lane** reviews main-branch commits rather than issues or PRs; it is manual-only in production, and it never closes items, writes comments, or fixes code.

## How an Issue Is Processed

Walk a single issue through the pipeline and the architecture becomes concrete.

A user files a bug.
Within the scheduler's tiered cadence it enters the review lane.
Codex reads the title, the body, the comments so far, and the relevant slice of `main`, and it writes a report.
The report does not just say "keep open" or "close."
It also stamps the issue with a fixed vocabulary of labels, and this vocabulary is what makes the backlog sortable instead of merely long.

The labels fall into four axes, and the axes are the real product of the review.

The **triage state axis** tells the system where the item sits in its own lifecycle.
`clawsweeper:no-new-fix-pr` means the bot has scanned and found no open fix.
`clawsweeper:source-repro` means the bug is reproducible from source inspection alone, with no live run needed.
`clawsweeper:linked-pr-open` means a fix PR exists and is still open.
`clawsweeper:queueable-fix` means the item is actionable enough to be auto-queued for work.
These labels let a maintainer filter the backlog down to "things I can act on right now" in one click, instead of reading a thousand bodies to find them.

The **routing axis** tells the system whose desk the item belongs on.
`clawsweeper:needs-maintainer-review` is the default for anything that survived the bot's first pass.
`clawsweeper:needs-product-decision` routes to whoever owns roadmap.
`clawsweeper:needs-security-review` routes to the security owners.
`clawsweeper:needs-live-repro` means the bot could not reproduce from source and a real run is needed.
`clawsweeper:needs-info` means the reporter left out something required and the item is waiting on them.
**Routing labels are the stage that converts a flat backlog into a partitioned one, and a partitioned backlog is the precondition for an ownership table actually working, because you cannot route to an owner until you can name the owner the item belongs to.**

The **impact axis** records what kind of damage the issue describes.
`impact:session-state`, `impact:message-loss`, `impact:auth-provider`, `impact:crash-loop`, `impact:security`, `impact:data-loss`, `impact:other`.
This is a closed list, not free text, and the closure is what makes it filterable.
A maintainer who wants to see every issue that could be losing user messages types one label and gets the complete set.
That query would be impossible against raw bodies.

The **rating axis** is the part that looks whimsical and is not.
Issues get one of `issue-rating: 🦞 diamond lobster`, `🐚 platinum hermit`, `🦐 gold shrimp`, `🦪 silver shellfish`, or `🌊 off-metric tidepool`.
The shellfish scale is a severity heuristic the bot assigns from the combination of impact, reproducibility, and reach.
The joke naming is a deliberate choice: memorable labels get used, and a label that gets used is a label that actually sorts the queue.
A `diamond lobster` is the rating that says "read this first."
A `tidepool` is the rating that says "this is real but off the critical path."

Layered on top are the older, human-facing labels: `bug`, `enhancement`, `regression`, `P1` through `P3`, `maturity:stable`.
The bot applies or confirms these too, so that the surface a human maintainer sees when they opens the tracker is already classified along every dimension the project cares about, without anyone having read the issue by hand.

If the verdict is "close," the proposal waits in the apply lane's queue.
If the verdict is "keep open," the item sits with its labels until the scheduler revisits it, and the labels do the work of making it findable in the meantime.
The bot also syncs a single marker-backed review comment per item, edited in place rather than reposted, so a maintainer who opens any single issue sees the bot's reading of it before they read the body themselves.

## How a Feature Request Is Processed

A bug asks "does this behavior exist, and is it wrong?"
A feature request asks "should this behavior exist?"
The review lane runs the same Codex pass over both, but the verdict it produces diverges in ways that show the pipeline is not one-size-fits-all.

The clearest divergence is on the routing axis.
A bug that survives the first pass carries `clawsweeper:needs-maintainer-review` and usually stops there.
A feature request carries `clawsweeper:needs-product-decision` on top of it, because the question for a feature is never "is this real" but "do we want this," and that question has a different owner than "is this code correct."
Three feature requests in the openclaw sample, a screen-sharing capability, a multi-agent collaboration RFC, and an auto-discovery proposal, all carry both labels, and the product-decision route is the one a bug almost never picks up.
**The same review produces a different routing label for a different input type, and that is the mechanism by which a flat issue tracker gets partitioned into the queues of different humans.**

The other axes apply conditionally, not uniformly, and checking this against the same three feature requests corrects the tempting simplification.
It is tempting to say a feature has nothing to reproduce, so the repro axis is silent, but the auto-discovery feature carries `clawsweeper:source-repro` because it touches behavior already present in the codebase.
It is tempting to say a feature is lower priority than an active bug, so it always lands the `off-metric tidepool` rating, but the same auto-discovery feature carries `issue-rating: 🦞 diamond lobster`, the top rating, because its reach and security surface are large.
The precise statement is narrower: the repro, impact, and rating axes still fire for a feature, but they fire based on what the feature touches, while the product-decision route fires for the feature category itself.

The close surface does narrow.
A feature request cannot be closed as `implemented_on_main` unless the feature was already built, at which point it is no longer a request, and it cannot be closed as `cannot_reproduce`, because there is no observed behavior to fail to reproduce.
What remains available are the `clawhub` close (the feature belongs in a plugin or skill, not core), the `duplicate_or_superseded` close, the `incoherent` close, and the `stale_insufficient_info` close after sixty days.
A maintainer asking "what should we build" reads a different, smaller close menu than one asking "what is broken."

Finally, feature requests are the input type that can leave the triage pipeline entirely and enter the repair lane.
Reviewed issues that clearly fit the repository's `VISION.md`, are small enough for one focused pull request, and have a clear repair structure can be dispatched to Codex to open a guarded implementation PR, labeled `clawsweeper:autogenerated`.
In `openclaw/openclaw` itself this lane is separately gated as a strict-bug or vision-fit path; in sibling repositories under the same organization it runs on viable reviewed issues more generally.
**A bug that clears triage waits for a human to fix it; a feature that clears triage can, under narrow conditions, be built by the same system that triaged it.**
That path is covered in the next section.

## How a Pull Request Is Processed

Pull requests pass through the same review and apply lanes, but the vocabulary the bot applies is different, because the questions you ask of code are different from the questions you ask of a bug report.

A pull request arrives, usually from a non-maintainer.
The scheduler tiers it the same way.
The review lane reads the diff, the linked issue, the body, and the relevant tests, and it stamps the PR with a parallel set of axes.

The **size axis** comes first, because size is the cheapest signal and the one that decides everything downstream.
`size: XS`, `size: S`, `size: M`, `size: L`, `size: XL`.
A five-thousand-line diff cannot actually be reviewed by a human; it can only be rubber-stamped, and the size label is what surfaces that fact before anyone wastes an hour pretending otherwise.
**Size is the label that protects the bottleneck, because the one thing you cannot do at scale is spend deep attention on a diff that was never reviewable to begin with.**

The **proof axis** is the one that makes the contributor-heavy queue survivable.
`proof: sufficient` means the PR carries enough evidence (tests, logs, or a screenshot) to support its claim.
`proof: supplied` means evidence was attached but not yet judged sufficient.
`proof: 📸 screenshot` marks the specific kind of proof.
PRs without proof sit in `status: 📣 needs proof` and do not advance until the contributor provides it.
This is the single largest filter in the pull request flow, because most drive-by PRs arrive with code and no demonstration that the code works.
Asking the bot to gate on proof shifts the verification burden back onto the author where it belongs.

The **merge-risk axis** records what breaks if this lands.
`merge-risk: 🚨 compatibility` for changes that touch shipped contracts.
`merge-risk: 🚨 security-boundary` for auth, sandboxing, or secrets.
`merge-risk: 🚨 message-delivery` for the channel paths that carry user messages.
`merge-risk: 🚨 auth-provider`, `merge-risk: 🚨 automation`, `merge-risk: 🚨 session-state`.
A PR can carry more than one, and the combination is what tells a maintainer how carefully to read.
A `size: S` PR with `merge-risk: 🚨 security-boundary` is small but dangerous, and that is a different reading from a `size: XL` PR with no risk flags.
The labels make the difference visible before the diff is opened.

The **rating axis** reappears on PRs with its own vocabulary: `rating: 🧂 unranked krab`, `rating: 🐚 platinum hermit`, `rating: 🦞 diamond lobster`, `rating: 🦐 gold shrimp`, `rating: 🦪 silver shellfish`.
The naming overlaps with the issue scale on purpose, because the underlying question is the same: how much does this deserve attention, and how risky is it if it lands.

Finally the **status axis** is the workflow state machine that decides what happens next.
`status: 📣 needs proof` blocks until evidence arrives.
`status: ⏳ waiting on author` means the bot or a reviewer has asked for changes and the ball is in the contributor's court.
`status: 👀 ready for maintainer look` is the state that says the PR has cleared every cheap gate a machine can apply and is now, for the first time, worth a human's time.

**The cumulative effect of these axes is that a maintainer opening the pull request list sees a sorted, ranked, risk-tagged queue instead of a chronological one, and the only PRs that reach `ready for maintainer look` are the ones that have already passed every cheap check the bot could run.**
That is the entire point of the pipeline.
The human reads the output of triage, never the raw inflow.

## The Repair Lane: Where the Bot Writes Code

Everything above is read-only.
The review lane reasons without a write token, the apply lane closes but does not reason, and the commit review lane never writes anything at all.
The repair lane inverts that posture: it is where ClawSweeper writes code, pushes branches, and can merge.
**The discipline of the design is not that the bot cannot write code; it is that code-writing lives in exactly one lane, and that lane opens only when a maintainer explicitly asks for it.**

The lane starts from maintainer intent.
A maintainer with write permission comments `@clawsweeper autofix` to opt a PR into a bounded review-and-fix loop without merging, or `@clawsweeper automerge` to opt it into the same loop plus a guarded merge.
The router validates the commenter's repository permission before anything runs, and security-sensitive findings require the explicit opt-in; the bot will not repair them on its own.
Issue implementation uses `@clawsweeper implement issue`, which is gated further: ClawSweeper refuses if an open PR already mentions the issue, a generated branch is already open, the issue is paused, or security blockers remain.

Inside the lane, the same separation that protects review and apply protects repair.
Codex handles the code repair and the local validation loop.
Deterministic executor steps own every GitHub mutation: branch push, label update, and the final merge gate.
Codex never pushes directly.
Before a contributor branch push, the lane waits ninety seconds by default, re-fetches the live PR head, and requeues rather than pushing if that head changed during the wait, so two repair attempts never collide on the same branch.
Automerge waits for an exact-head review, required checks, mergeability, security state, and maintainer stop or approve state before the final merge, and it can be halted at any point with `@clawsweeper stop`, which adds `clawsweeper:human-review` and makes older repair comments ineligible to continue.

**The boundary that matters is not "the bot does not write code," it is that the bot writes code only inside a bounded loop that a maintainer opened, on a head it re-checked immediately before pushing, with every mutation owned by a deterministic executor rather than the model itself.**
That is the same pattern as review and apply, applied to writes instead of closes: the model proposes, a guarded executor disposes, and neither runs unsupervised on the other's output.

## The Restraint That Makes It Credible

Restraint shows up first in the close rules, and the close rules are a closed list in source, not a model judgment.
The `RepositoryCloseReason` type in `src/repository-profiles.ts` enumerates exactly ten: `implemented_on_main`, `mostly_implemented_on_main`, `cannot_reproduce`, `clawhub` (better suited to a plugin or skill), `duplicate_or_superseded`, `low_signal_unmergeable_pr`, `unconfirmed_product_direction` (default-off), `not_actionable_in_repo`, `incoherent`, and `stale_insufficient_info` (the sixty-day stale case).
Everything else stays open, including reproducible bugs, valid feature requests, partial reproductions, and real but un-prioritized work.
**Closure of the list is what makes it auditable: a close either maps to one of these names, with evidence, or it does not happen.**

Layered on top are hard exclusions that override the rules.
Maintainer-authored items are excluded from automated closes unless the close reason is verified `implemented_on_main`, the one case where ownership yields to a proven-shipped fix.
Protected labels block close proposals entirely.
Open pull requests with GitHub closing references (such as `Fixes #123`) block close on the referenced issue until the PR resolves.
Open same-author issue and PR pairs block one-sided closes, so a contributor's PR and its matching issue live or die together.
The apply lane re-validation throws away any proposal whose underlying item has changed since the review, which is the guard against acting on a stale snapshot.

The throughput limits are themselves restraint.
Apply is capped at five fresh closes per checkpoint.
The worker budget tops out at thirty-two concurrent Codex workers across the whole system, with scheduled normal review getting up to twelve shards when quiet and manual backfill up to twenty-two.
Exact event reviews lease at most twenty concurrent reviews and admit up to sixteen active per target repository.
These numbers say, in code, that the system would rather leave an item open than spend a review it cannot afford.

A secondary write-up ([Apidog, April 2026](https://apidog.com/blog/clawsweeper-openclaw-github-triage-bot/)) reported a close rate of roughly one tenth of one percent on a weekly pass, around four closes against nearly three and a half thousand reviewed issues.
That figure is not in the ClawSweeper source and I could not verify it independently, but it is consistent with the posture the close rules and caps enforce, and it is the right mental model: the pipeline optimizes for "never close something a contributor would defend if asked," not for inbox zero.

## The Boundaries That Actually Hold

Earlier I claimed ClawSweeper does not write code, does not set priority, and does not learn from past closes.
Reading the source showed all three claims to be false or overstated, and the corrected picture is worth stating plainly because the real boundaries are more interesting than the false ones.

The review lane does not write code, does close anything, or mutate GitHub state: it is proposal-only, read-only, and fails if Codex leaves a dirty tree.
That boundary holds, and it is the one that makes unsupervised review safe to run over attacker-controlled issue and PR text.
The commit review lane is even stricter: it never closes items, writes comments, or fixes code, and it runs only on manual dispatch in production.

But the repair lane does write code, as covered above, gated behind maintainer opt-in.
The bot does apply priority and advisory labels (`P1` through `P3`, the `impact:*` set, the routing labels) from structured review conclusions, though the source is explicit that these are advisory and do not trigger repair, merge, or close behavior.
And review is not memoryless: it pulls prior ClawSweeper reports, linked closing PRs, and gitcrawl cluster context as advisory input, and the repair lane resumes the same logical Codex thread across planning and execution.
**The accurate framing is not "the bot refuses to do these things," it is that each lane owns exactly the mutation its contract permits, and every mutation is rechecked against live state immediately before it happens.**
A bot at scale should own exactly one decision per lane and re-validate at the boundary, and that is the discipline the source actually encodes.

## Why the Architecture Generalizes

You do not have to run OpenClaw, or build AI assistants, to borrow this design.
**The architecture is portable because the problem it solves is universal.**
Any tracker at sufficient volume has the same structure: a mixed inflow, a scarce bottleneck of human attention, and a long tail of items that could have been sorted by a machine but are instead being sorted, slowly and expensively, by a tired maintainer.

The valuable parts are not the prompts, which are tied to OpenClaw's domain, and not the shellfish labels, which are a stylistic choice.
The valuable parts are the structural moves, and they work regardless of what your project actually ships.

**Separate the decision from the execution.**
Run the model without write access, and run the apply step without reasoning.
**The separation is what makes the system auditable and what stops either stage from running away.**

Narrow the autonomous action to a closed list of cases.
Do not let the model decide what counts as closeable on the fly.
Write the rules down, make them few, and make "everything else stays open" the default.

Tier the cadence.
Hot items get revisited often, cold items rarely.
Treating every issue as equally deserving of attention is the mistake that bankrupts the queue.

Gate on the cheapest signal first.
On pull requests, size and proof are cheaper than correctness, and they filter the bulk of the inflow before a single diff is read.

Keep code-writing, if you do it at all, in its own lane behind explicit opt-in, with the model separated from the push.
Letting an LLM propose a fix is cheap; letting an LLM push to a branch unattended is the failure mode the repair lane's executor separation exists to prevent.

Optimize for precision, not throughput.
A bot that closes one percent of the right things is more valuable than one that closes fifty percent of the wrong things, because the wrong closes cost you the contributors you cannot afford to lose.

## What to Do Next

You will not build OpenClaw's pipeline in a week, and you should not try.
The move is to steal the structure and apply it one slice at a time, to whatever is costing you the most attention right now.

Start with the labels.
Write down the four axes that would make your backlog sortable if every item had them: state, routing, impact, severity.
Apply them by hand for a month, until you can feel which questions a machine could answer and which still need you.
A label vocabulary that has not been used by humans is not ready to be applied by a bot.

Add the cheap gates first.
A size labeler, a path-based labeler, a conflict marker, a stale closer.
Each one is an automated answer to a cheap question, and each one is a slice of attention you stop spending by hand.

Then, and only then, wire in the review lane, in shadow mode.
Have it post its summary as a comment without applying any labels, and read along with it for a month until you trust its routing and severity calls.
When you trust the labels, turn them on.
When you trust the close proposals, add an apply lane, and let it run on the narrowest possible close rules, closing at most a handful per day until trust accumulates.

Leave code-writing for last, and only if you need it.
If you do build a repair lane, separate the model from the push the way review is separated from apply, and gate it behind an explicit maintainer command so it never runs on its own.

The end state is not a maintainer who reads everything.
It is a maintainer who has built a pipeline good enough that almost nothing reaches them unsorted, and what does reach them is exactly the work that was worth a human's time.
**The goal of triage automation is not to replace the maintainer; it is to make sure the maintainer is never the thing standing between the queue and the project's future.**

## See also

- [Peter Steinberger | OpenClaw Creator](https://www.youtube.com/watch?v=82YaJw-_t10) - a video interview with the OpenClaw creator, where the triage pipeline and maintainer-attention problem are discussed firsthand
- [Read the Commits, Not the Manual](../learnings-from-openclaw/index.md) - the companion reading of OpenClaw's git history, where the same maintainer-attention bottleneck shows up in the commit patterns and contribution rules
- [The Pull Request Queue Outgrew You](../triaging-open-source-pull-requests/index.md) - the general case for a triage layer between the inflow and the human reviewer, which the OpenClaw pipeline is a working, production-scale implementation of
- [The Merge Gate](../the-merge-gate/index.md) - the argument for gating on blast radius rather than on the existence of a pull request, which is the principle behind the merge-risk axis
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - why a machine-checked constraint outperforms a tired human scan, the premise behind letting the review lane run unsupervised
- [The Codebase Gardener](../the-codebase-gardener/index.md) - the case for encoding standards where work passes through them, which is what the label vocabulary does for the backlog

## References

- [openclaw/clawsweeper source](https://github.com/openclaw/clawsweeper) at commit `f2fc64e0bc743bbd6742b36e4e164cbf91c0b31a` (2026-07-02) - the canonical source for every architectural claim in this article; the four-lane structure, the ten `RepositoryCloseReason` values, the worker caps, and the repair-lane gating were read directly from `README.md`, `src/repository-profiles.ts`, `config/automation-limits.json`, `docs/scheduler.md`, `docs/work-lane.md`, and `docs/repair/README.md` at this commit
- [ClawSweeper README](https://github.com/openclaw/clawsweeper/blob/main/README.md) - the operator-facing overview of the four lanes, the scheduler cadences, and the token safety model
- [ClawSweeper scheduler docs](https://github.com/openclaw/clawsweeper/blob/main/docs/scheduler.md) - the cadence tiers (hourly for active items, daily for recent, weekly for older) and the shard limits
- [ClawSweeper repair docs](https://github.com/openclaw/clawsweeper/tree/main/docs/repair) - the `autofix`/`automerge`/`implement issue` opt-in contract and the deterministic-executor separation
- [OpenClaw on GitHub](https://github.com/openclaw/openclaw) - the repository whose issue and pull request tracker supplied the label vocabularies, bot comments, and volume samples cited throughout
- [Apidog, "ClawSweeper: How OpenClaw's Codex Bot Triages 7,000 GitHub Issues"](https://apidog.com/blog/clawsweeper-openclaw-github-triage-bot/) - a secondary write-up; the only claim in this article taken from it rather than the source is the 0.1% close-rate figure, which is attributed inline and flagged as unverified
- [Wikipedia, "Theory of Constraints"](https://en.wikipedia.org/wiki/Theory_of_constraints) - Goldratt's framing for why you protect the bottleneck rather than adding effort elsewhere, the basis for reading the entire pipeline as reviewer-time conservation
