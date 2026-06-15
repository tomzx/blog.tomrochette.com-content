---
title: "Developer Trust Profiles: Earned Scrutiny for Automated Code Review"
created: 2026-06-15
type: post
status: finished
tags: [ai, software-engineering, code-review, agents, developer-tools, fully-ai-generated, llm=glm-5.2]
readability: 3
---

When you automate code review, the obvious design is to treat every pull request identically.
Same checks, same threshold, same outcome, regardless of author.
This obvious design is wrong.

A reviewer that applies the same scrutiny to a developer who has shipped two hundred clean PRs and to a stranger on their first contribution is either too strict for the first or too lax for the second.
It is a blunt instrument, and bluntness is the enemy of autonomy.
The more you rely on automated approval to unblock work, the more you need a mechanism that varies scrutiny by evidence.

I built that mechanism as a pair of skills in my agent library, [developer-trust-profile](https://github.com/tomzx/agents/blob/main/skills/developer-trust-profile/SKILL.md) and [initialize-developer-trust-profile](https://github.com/tomzx/agents/blob/main/skills/initialize-developer-trust-profile/SKILL.md).
This is the idea behind them, and why I believe it is the missing primitive for autonomous code review.

## The problem with a reviewer that has no memory

Most automated review tools are stateless.
They look at a diff, run their checks, and emit a verdict.
Next PR, they start over, as if they had never seen the author before.

This is not how any experienced human reviewer works.
When a trusted colleague opens a PR, you skim it, confirm the tests pass, and approve.
When someone with a history of breaking the build opens one, you read every line.
You already know who tends to forget tests, who mixes unrelated refactors into a single commit, who writes the clearest descriptions.
That knowledge is not bias to be eliminated; it is signal, accumulated over hundreds of reviews, that tells you where to spend your attention.

A stateless automated reviewer throws all of that signal away.
It re-derives, badly and from scratch, what a human reviewer simply remembers.
The result is a system that either approves indiscriminately (unsafe) or applies maximum suspicion to everyone (slow, and corrosive to trust).

The trust profile is the answer to a direct question: how does an automated reviewer remember?

## What a trust profile stores

Each developer gets a single file, `~/.developer-trust/{github_username}.md`, and the whole directory is a git repository.
The file accumulates observations across every review.

Four trust levels exist, and each one maps to a different *behavior*, not just a different label:

| Level | Meaning | Effect on the automated reviewer |
|-------|---------|----------------------------------|
| `trusted` | Consistently clean, high-quality PRs | Standard checks, lean toward approval on borderline cases |
| `neutral` | Unknown or mixed track record | Standard checks, default behavior |
| `cautious` | History of issues, missed edge cases, unclear PRs | Stricter interpretation, flag marginal cases as failures |
| `always_reject` | Persistent quality or policy issues | Skip entirely, never auto-approve, require manual review |

Beyond the level, the profile keeps a running overview, lists of strengths and weaknesses observed across PRs, recurring PR patterns, and a full review history table with dates, repos, outcomes, and a one-line note per review.

Crucially, it is plain markdown in a git repo.
That makes the system's memory auditable, diffable, and portable.
You can see the exact review that tipped an author from `neutral` to `cautious`, and the reasoning behind it.
For a mechanism that gates code into production, that paper trail is not a nicety; it is a requirement.

## How earned trust changes review behavior

The levels are not decorative.
They modify how the automated reviewer interprets its own checks.

The reviewer I run, [quick-pr-review](https://github.com/tomzx/agents/blob/main/skills/quick-pr-review/SKILL.md), evaluates a fixed set of gates: significant public interface changes, security-sensitive code, new dependencies, reversibility, passing CI, alignment with the linked issue's acceptance criteria.
For a `neutral` author, each gate is binary.
For a `trusted` author, a borderline call (is this small new export a "significant" public interface change?) leans toward passing.
For a `cautious` author, that same borderline call is treated as a failure.

This is differential scrutiny, and it is the whole point.
The checks are identical; the threshold moves with evidence.
A trusted author gets unblocked faster because the reviewer stops re-litigating cases it has effectively already won.
A cautious author gets caught earlier, before a recurring weakness reaches production again.

And then there is `always_reject`, the hard stop.
When an author sits at that level, the reviewer does not fetch the diff, does not post a comment, does not approve.
It reports that the PR was skipped and that a human needs to look.
This is the system saying: I have enough evidence to know I should not be making this decision.

## The loop closes

The profile is not a static config file that a human maintains by hand.
It is both consumed and produced by the review pipeline.

Before a review, `quick-pr-review` reads the author's profile to set its thresholds.
After the review, it writes back: it appends a row to the history, merges new observations into the strengths and weaknesses, and reconsiders the trust level if the accumulated evidence warrants it.
Each profile update is committed to the local git repo with a message like `Update alice trust profile (approved: acme/api#42)`.

This makes the system a slow learner rather than a judge.
A single review does not move the trust level, unless it is egregious.
Trust degrades through recurring patterns observed across many PRs, and the level only shifts when the weight of evidence demands it.
That hysteresis is deliberate.
It prevents one bad day from branding a developer, and it prevents one lucky PR from buying unwarranted autonomy.

## Bootstrapping without survivorship bias

The hardest part of any reputation system is the cold start.
A new contributor, or a contributor new to the system, starts at `neutral` with an empty file.
That is safe but unhelpful; you want a profile grounded in reality, not a blank slate that takes months to fill.

The [initialize](https://github.com/tomzx/agents/blob/main/skills/initialize-developer-trust-profile/SKILL.md) skill bootstraps a profile from history by scanning the author's last N pull requests across every repository the token can see.
The detail that separates this from a naive implementation is that it samples both merged *and* rejected PRs.

Sampling only merged PRs is survivorship bias in its purest form.
It would make every developer look good, because the failures were quietly closed and forgotten.
By pulling closed-without-merge PRs as well, and by deriving the outcome from actual review data (was there a changes-requested that was never superseded?) rather than assuming merge equals approval, the bootstrap produces a profile that reflects how a developer actually works, not just their wins.

Processed oldest-first, each historical PR feeds into the same update pipeline as a live review, so a freshly initialized profile looks exactly like one that was built up review by review over time.

## Honest limitations

The design has real trade-offs, and they are worth naming.

Profiles live on the reviewer's machine and are not shared.
This is a feature (no global reputation database, no public scoring of humans) and a cost (each reviewer builds a different picture, and the memory does not transfer).
For a single operator running their own agents, that is the right trade.
For an organization, you would want a shared, access-controlled store, and the design does not pretend otherwise.

There is a risk that a reputation ossifies.
The skills mitigate this by removing observations that recent evidence contradicts and by reconsidering the level on every update.
But any system that summarizes a human into a label can lock them in.
The fix is transparency (everything is in a diffable file) and a human who can edit the file when the summary is wrong.

There is also a gaming risk.
Once authors know a trust system exists, they can optimize for it.
On balance this is fine: optimizing for clean, well-tested, well-scoped PRs that reference their issues is exactly the behavior you wanted anyway.
The system fails safe, because the worst case is that people produce better PRs.

## Why this matters more in the age of LLM-authored code

I have written elsewhere about why human review of LLM-generated code is a poor use of attention (see [The Future of Code Review](https://blog.tomrochette.com/the-future-of-code-review)).
The short version is that the human's leverage has moved upstream, to specifying the problem, while machines verify compliance.

But that argument has a gap.
Even after you accept automated review, you are left with a follow-up question: should the automated reviewer treat every author identically?
The answer is no, and for a reason that is sharper now than it was five years ago.

In an LLM-heavy workflow, the "author" of a PR is increasingly a human paired with a model, or an agent operating on a human's behalf.
The trust profile stops measuring just a developer's coding skill and starts measuring something more valuable: the quality of a human's oversight of their tools.
Two developers can submit PRs that an LLM wrote.
One vets the output carefully, keeps PRs atomic, links the spec, and ships reversible changes.
The other rubber-stamps whatever the model produced, mixes concerns, and breaks public interfaces.
A stateless reviewer cannot tell them apart.
A reviewer with a trust profile can, and it calibrates its scrutiny accordingly.

Seen this way, the trust profile is the layer beneath the automated reviewer: the checks define what "good" looks like, and the profile decides how much to trust that a given author is delivering it.

But that framing also points at the profile's eventual obsolescence, which is the goal.

## A bridge, not a destination

There is a sense in which the trust profile is a mechanism I want to make obsolete.

The ideal end state is not a finely calibrated reputation system that perfectly sorts developers into tiers.
The ideal end state is that there is nothing to sort.
Every contributor, senior engineer or new hire, funnels their work through agents that enforce the same standards: atomic PRs, tests that pass, interfaces that do not break, changes that are reversible and tied to a spec.
The output converges into something homogeneous, and by the time it reaches the code stage it is, for all practical purposes, perfect.
Authorship stops carrying signal, because every author is producing the same uniform quality through the same disciplined pipeline.

In that world the reviewer's checks still run, but they never flag anything, because the problems were engineered out upstream rather than caught downstream.
And the trust profile, with nothing left to differentiate, collapses: everyone sits at `trusted`, the level never moves, and the file stops being worth reading.

That is the honest framing for the trust profile.
It is not the destination; it is the bridge.
Today's reality is heterogeneous, a mix of careful and careless, hand-written and agent-generated, vetted and rubber-stamped, and the profile does useful work precisely because that variance exists.
As the variance shrinks, so does the profile's job, until the most successful outcome is that no one, me included, needs it anymore.
