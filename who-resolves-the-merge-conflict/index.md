---
title: "Who Resolves the Merge Conflict? Why the Bot and the Author Are Not Interchangeable"
created: 2026-07-06
type: post
status: finished
tags: [software-engineering, pull-request, git, automation, llm, github-actions, productivity, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader works on a repository that receives pull requests from humans and from LLM agents, runs an auto-merge lane or wants to, and is comfortable with git rebase, merge conflicts, and branch protection. Clean rebases are assumed solved and out of scope; the only question is who resolves a real conflict.
---

A pull request falls behind main and conflicts.
Who resolves the conflict, the bot or the author?
**The answer depends on whether the conflict is mechanical or semantic, and treating the two as the same job is what makes every flat policy, "the bot rebases everything" or "the author handles it," wrong.**

The clean rebase is settled and out of scope; automate it on every push to main.
The live question is the conflict, and the conflict is not one thing.
Resolving a conflict means deciding what the code should now say, and that decision is a claim about what the author meant.
Someone has to make it, and the interesting question is who can back it with intent they actually hold.
**That depends entirely on whether the conflict has a unique correct answer an oracle can check, or whether its correctness lives only in the author's head.**

## Why the Question Got Loud

For most of git's history the conflict question was quiet.
A contributor resolved their own conflicts, or the maintainer did, and the round trip was short because the people involved shared a mental model of the code.
Two things broke that equilibrium.

The first is auto-merge.
Once low-risk changes land on green without a human clicking merge, a PR that cannot merge cleanly becomes the thing that stalls the whole lane.
A human can absorb a conflicted PR by glancing and clicking; an automated merge pipeline cannot.
**Auto-merge makes conflict resolution a prerequisite of the lane, and that turns "who resolves" from a courtesy into a load-bearing question.**

The second is the model-authored pull request.
When the author is a model, the conflict round trip behaves differently at both ends.
The bot never sleeps, so a resolve request adds no latency the way it does for a human.
But the bot also has no private knowledge of what the code was meant to do, so its resolution is a guess about intent dressed up as a fix.
This is the plausibility problem, and it lands hardest exactly where the conflict is hardest.

So the modern repository has a lane that wants every PR mergeable on green, and a growing share of PRs whose intent lives only in the code a model produced, with no description, linked issue, or spec that states it independently.
When the intent is encoded somewhere, a conflict has an oracle to check a resolution against.
When it is not, there is nothing to verify the resolution by, and that, not the absence of an author to interrogate, is the actual problem.
**The old default, the contributor resolves, is too slow for the merge lane, and the bot is too confident to stand in as the oracle, so the live question is not who authored the PR but whether the intent exists outside someone's head.**

## The Conflict Has a Gradient

Conflicts are not all the same, and the gradient is what lets you route them accurately.

At one end is the mechanical conflict: an import added in both branches, a trailing comma, two functions inserted at adjacent positions, a formatting drift the formatter can settle.
Resolve it and there is exactly one answer any reasonable developer would accept, and a test suite that passes before will pass after.
At the other end is the semantic conflict: two people changed the same logic for different reasons, and the correct resolution depends on which reason was right.
**The mechanical conflict has a unique correct answer that a test can falsify; the semantic conflict has no correct answer without the intent that motivated the change.**

The mechanical conflict is therefore still logistics, just logistics that needs an oracle.
Resolve it, run the suite, and if the suite passes the resolution is, by construction, the one the project already trusted.
This is the test acting as the independent oracle the model cannot be, the same role it plays in closing the bug gap when a fix claims to be done.
A conflict whose wrongness a test can catch is a conflict the bot may resolve, because the test, not the model, is signing off.

The semantic conflict is a different animal.
Nothing external is left to disagree with the model's plausible stitch, because the definition of "correct" is the intent, and the intent is precisely what the model does not have.
**A bot that resolves a semantic conflict is making an intent claim it cannot source, and the harder the disagreement, the more likely the claim is a confident fabrication.**

## Where the Intent Lives

The semantic conflict splits once more, and it splits on a cleaner axis than who wrote the PR: whether the intent is encoded anywhere a resolver can read it.

Intent can live in two places.
It can be encoded, written down in the PR description, a linked issue, an acceptance criterion, a failing test, anything a human authored to state what the change was supposed to do.
Or it can be tacit, held in someone's head and never written down, surfacing only if you ask.
**A conflict is safe for the bot to resolve when the intent is encoded and the encoded source covers the disputed region, because then the resolution has an oracle.**
It is not safe when the intent is tacit, because then nothing external can falsify the bot's stitch, and the stitch will look right whether or not it is.

Author type matters, but only as a proxy for where the intent lives, and the proxy is worth stating because it inverts the naive assumption.

When the PR is human-authored, the human's own description is an independent statement of intent.
If the description covers the conflict, the bot may resolve against it, and the description, not the model, is the oracle.
If the description is thin or silent on the disputed region, the intent is effectively tacit, and the only defensible move is to ask the human who holds it.

When the PR is bot-authored, the trap is that the bot's description is not an independent oracle.
It was written by the same model that wrote the code, or a sibling of it, so checking the resolution against the description is checking the model against its own narration, which provides no real verification.
The only trustworthy intent source for a bot-authored PR is something a human wrote upstream: the issue, the spec, the prompt, an acceptance test.
When that upstream source exists and covers the conflict, the bot may re-derive against it, and the re-derivation is checkable.
When it does not exist, the intent was never encoded by anyone, and the bot's resolution is a guess about intent no one ever wrote down.

This is the refinement the flat "maintainer picks a default" framing misses.
A single repository-wide default is too coarse, because the right default is a function of whether the PR carries an encoded, independent intent source, and that varies PR by PR, not repository by repository.
**The PR that links a human-authored issue with acceptance criteria is safe for bot resolution regardless of who wrote the code; the PR that arrives as code and a self-description is not safe regardless of who wrote the code.**

## The Label Is the Right Mechanism, the Default Is the Question

Given the split, the mechanism worth reaching for is the one the question already points at: a label on the PR that decides who resolves a conflict.
Labels are already how a modern triage layer expresses every other routing decision, and conflict resolution is no different in kind.
The label should express the thing that actually varies, which is not "is this PR rebased" but "who is allowed to resolve a semantic conflict on it."

For a mechanical conflict there is no decision worth encoding: the bot resolves, the test gates, and a `conflict: auto-resolved` note is enough audit trail.
The label earns its keep at the semantic tier.
Something like `conflict: author-resolves` versus `conflict: bot-may-resolve`, defaulted per repository by the maintainers and overridable per PR, is the right shape, and it is the shape the question proposes.

The interesting work is in the default, and the sound default routes on intent availability, not on author type.
A PR that links a human-authored issue or spec, with acceptance criteria that cover the change, defaults to `bot-may-resolve`, because the resolution has an oracle.
A PR that arrives as code alone, with no independent statement of intent, defaults to `author-resolves`, because nothing can falsify the bot's stitch.
The maintainer's real choice is not "auto or manual."
It is "what do we assume about a PR whose intent source we cannot verify," and the conservative answer, treat it as unencoded and ask the author, costs a little latency where the bot could have handled it, while the permissive answer, resolve and trust the model, costs intent claims that are silently wrong.
**Between losing a little speed and shipping a confidently wrong merge, the speed is the cheaper loss, so the default for a PR with no verifiable intent source should be `author-resolves`.**

This makes the highest-leverage change a documentation change, not a tooling one.
Require, in the pull request template, a linked issue or a short intent statement that covers the change, and ask whether the PR was model-assisted.
The linked issue turns an unencoded PR into an encoded one; the model-assisted flag tells you whether the PR's own description can serve as an oracle or whether you need the upstream source.
Both shrink the "no verifiable intent" bucket, and shrinking that bucket is what lets the auto-merge lane actually run.

## What to Do on Monday

First, surface the conflict instead of hiding it.
Add [eps1lon/actions-label-merge-conflict](https://github.com/eps1lon/actions-label-merge-conflict) so any PR that falls behind main gets a `merge-conflict` label the moment it conflicts, and loses it the moment it merges again.
Your auto-merge lane can now filter `-label:merge-conflict` and only act on work that is actually ready, and the author gets an automated nudge that a real decision is needed without you being the one to say it.

Second, classify the conflict before you route it.
Mechanical conflicts, imports, formatting, adjacent non-overlapping edits, the bot resolves behind the test gate, and the test is the oracle that makes the resolution trustworthy.
If the suite fails, the resolution is wrong by definition and the bot escalates rather than ships.

Third, route the semantic conflict by whether an independent intent source exists.
If the PR links a human-authored issue or spec that covers the disputed region, let the bot resolve and check the result against that source, with an encoded test that must pass on the resolved tree.
If the PR carries no such source, post the conflict as a comment and drop the PR to `author-resolves` until someone provides the intent or resolves it by hand.

Fourth, choose the conservative default for the case where you cannot tell.
When a PR arrives with no linked issue and no intent statement, default to `author-resolves`, because the cost of a confidently wrong merge is higher than the cost of a round trip, and the round trip at least asks the question the silent resolution skips.

Fifth, make the routing signal cheap to produce.
Require a linked issue or a short intent statement in the pull request template, and ask whether the PR was model-assisted.
The link is what turns an unencoded PR into an encoded one, and the model-assisted flag is what tells you whether the PR's own description can count as the oracle.

Do not write a policy that says "the bot resolves everything" or "the author resolves everything."
Both are the original mistake in policy form.
**Gate the mechanical conflict behind a test, defer the semantic conflict to an independent intent source when one exists, and defer to the author when one does not.**

## See also

- [Triaging Open Source Pull Requests](../triaging-open-source-pull-requests/index.md) - the upstream layer this refines: labeling merge conflicts and routing by risk is the triage move, and conflict-tier routing is what makes the auto-merge lane inside that layer safe
- [The Merge Gate](../the-merge-gate/index.md) - the case for gating on the properties of a change rather than on the existence of a PR, which is the same principle applied here to "is this a mechanical conflict or a semantic one"
- [The Acceptance Gap: Why an LLM Solution Is Not a Shipped Solution](../the-acceptance-gap/index.md) - why a conflict resolution is a mini-acceptance gap: the mechanical tier wants a check (verification), and the semantic tier wants the author's reaction (validation)
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - the plausibility problem in full, the reason a bot resolving a semantic conflict is making a claim about intent it cannot source
