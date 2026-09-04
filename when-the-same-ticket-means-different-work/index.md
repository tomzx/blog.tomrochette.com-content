---

title: "When the Same Ticket Means Different Work: Aligning on Scope Across Contributors"
created: 2026-08-20
type: post
status: draft
tags: [software-engineering, team-management, scope, estimation, planning, fully-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader works on a software team that plans work in tickets or user stories, and has watched two engineers produce very different amounts of work from the same description. Familiar with common agile ceremonies, but no specific framework expertise is required.
agent_sessions:
  - ses_fe2b5ccc7ffe8M7CP6NQVnRJTK
---

Give two engineers on your team the same ticket and they will do different amounts of work, and neither of them will be wrong.
**The scope of a piece of work is not a property of the ticket. It is a property of the engineer who picks it up.**
Most scope friction inside a team is not about the feature at all.
It is a collision between two private definitions of what a unit of work is, arriving in the same conversation unnoticed.

## What a One-Line Ticket Actually Contains

Take a plain example: "add pagination to the results endpoint."
Engineer A reads a morning of work.
Accept a page parameter, clamp the values, return a slice, add a test, ship it.
Engineer B reads the same nine words and sees a week.
The endpoint has three consumers, one of which cannot handle a paginated response, so there is a contract change, a migration, a deprecation window, a feature flag, telemetry on page depth, and a documentation update.
Same ticket, same team, two scopes a factor of five apart.

The ticket was not ambiguous about behavior.
It was silent about boundaries, and silence gets filled from somewhere.
Each engineer fills the gaps with personal defaults: the tests they always write, the migrations they always schedule, the risk they personally carry from past incidents, their private definition of what a complete change looks like.
Those defaults are exactly the invisible checklists I described in [Bringing Everyone to the Same Level](../bringing-everyone-to-the-same-level/index.md): knowledge accumulated through scar tissue, living in heads, never written down.
**When the ticket does not say where the work ends, each engineer's history decides.**

## Conversation Hides the Problem, Writing Exposes It

None of the above is a character flaw or a hiring mistake.
It is ordinary language behavior.
Linguists call the shared background that lets a listener fill gaps in a sentence [common ground](https://en.wikipedia.org/wiki/Common_ground_(communication_technique)), and it is always partial.
Spoken teams survive the gaps because speech repairs itself in real time: I say something vague, you frown, I add detail, and thirty seconds later we genuinely share a definition.
The repair is invisible, so the team concludes it has shared definitions.

A written ticket has no repair channel.
The reader cannot frown at the page and get an answer, so the gaps get filled with whatever the reader already believes.
Teams consistently overestimate how much common ground their tickets inherit from their conversations, because the conversation was the only place the common ground existed.
**Words that feel precise to the writer are fertile ground for the reader's defaults, and a ticket is the writer's precision tested against the reader's history.**

## Where the Hidden Variance Bites

Estimation goes first.
When engineers estimate a ticket, they are estimating their own expansion of the ticket, so the points track the person as much as the work.
Averaging divergent estimates, which most planning tools do cheerfully, launders a definition gap into a false consensus number that describes nobody's actual week.

Planning breaks next.
Reassigning a ticket from B to A does not just change who does the work, it silently changes how much work there is.
A capacity plan built on one engineer's expansion collapses when the backlog is executed by another's, and the plan's failure looks like an estimation problem instead of a definition problem.

Review absorbs the rest.
The same pull request reads as incomplete to a reviewer with a wide expansion and as gold-plated to a reviewer with a narrow one.
Many heated review threads are not about code quality at all.
They are scope-definition arguments wearing a code review costume, the first place two private defaults finally meet in writing.

There is a new variant as well.
An LLM agent picking up an underspecified ticket expands the ticket according to its own tendencies, sometimes toward the minimal patch, sometimes toward a sprawling thorough version, and the person who ends up maintaining the result chose neither.
The variance problem has simply gained a class of contributors whose defaults you also do not control, which is one more reason the boundaries need to live in the ticket rather than in anyone's head, as [Who Maintains the Slop?](../who-maintains-the-slop/index.md) argues from the maintenance side.

## Why the Standard Fixes Under-Deliver

Most teams already have a [definition of done](https://en.wikipedia.org/wiki/Definition_of_done), and it helps, but it is coarse.
A single team-wide line rules the outer boundary: code reviewed, tests pass, deployed.
The contested middle, migrations, documentation depth, telemetry, test quality, deprecation paths, stays unruled, and the middle is exactly where A and B diverge.
A boundary drawn only around the whole sprint compresses almost none of the variance inside each unit.

Acceptance criteria do better, and still miss.
Criteria capture the visible behavior of the feature, because visible behavior is what product people can review.
The defaults that actually differ between engineers are invisible precisely because each engineer considers them obvious, and nobody writes down what goes without saying.

Story point averaging is the subtlest failure.
The spread between two trusted engineers' estimates is the most informative artifact the planning meeting produces, and the standard workflow throws the spread away and keeps the average.
**Averaging divergent estimates does not resolve a definition gap, it hides one inside a number.**

## The Spread Is the Signal

The estimation ceremonies that descend from the [wideband delphi](https://en.wikipedia.org/wiki/Wideband_delphi) method, including [planning poker](https://en.wikipedia.org/wiki/Planning_poker), already contain the fix, and most teams use it backwards.
The value of everyone revealing a number at once is not the number.
It is the moment two trusted engineers reveal numbers far apart and the room has to ask why.
That conversation, estimate explained, assumption surfaced, is the scope definition being written in real time.

Treat estimate divergence as a detector, with a working threshold.
**When two engineers who know the codebase estimate the same ticket more than a factor of two apart, the ticket is underspecified, and the correct next step is not to average, it is to write the boundary.**
Spell out what is in and what is out until the estimates converge on their own.
Convergence is evidence of a shared definition; the number that survives is almost a byproduct.
The instinct is the same one behind my rule of thumb for [rough project size estimation](../questions/2020/03/02/index.md): a task estimated at a month is hiding complexity, and divergent estimates are hiding unspecified scope.

## Make the Defaults Explicit Once, Not Every Sprint

Three practices, layered, close most of the gap.

Write in/out lists on the work that matters.
Scope stated as two lists, what this change includes and what it explicitly defers, turns the reader's fill-in-the-gap into a check against a written boundary.
The practice is old and standard: well-bounded stories are meant to be negotiable and small, per Bill Wake's [INVEST criteria](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/), and negotiable requires knowing what is being negotiated.

Keep a done checklist per work type, not just per team.
A bug fix, a feature, and a refactor expand differently: migrations belong to one, rollbacks to another, telemetry to a third.
A short template per class of work encodes the team's answer once, and every future ticket inherits the answer instead of the assignee's mood.
This is the same externalization move as the written scope decision records in [When a Closed Decision Reopens](../when-a-closed-decision-reopens/index.md) and the executable skills in [Bringing Everyone to the Same Level](../bringing-everyone-to-the-same-level/index.md).
**A work-type template is a decision record for scope, written once and applied every time.**

Close the loop with calibration.
Compare planned against actual per ticket class, and when a class runs systematically over or under, ask first whether the template failed to capture what the work really contains, and only then whether the estimates were bad.
Estimates drifting apart again is the signal that a new kind of work has appeared and needs a template of its own.

## What to Do Next

Pick the recurring ticket type where your team's estimates diverge the most.
Ask two engineers who know the area to independently write down everything they would build for the next instance, as bullet lists, before any discussion.
Diff the lists.
Everything present in one list and absent from the other is the real scope disagreement, made visible in fifteen minutes without a single meeting.
Merge the two lists into an agreed in/out template with explicit done criteria for that work type, then run the next instance through the template.
Watch the estimates on the second instance, and the review threads.

You cannot remove the differences between your engineers, and you would not want to.
The engineer who sees the week-long expansion is seeing real coupling that the morning-of-work version will eventually pay for with interest.
**The goal is not to make everyone expand work identically by instinct.
It is to stop renting each engineer's private defaults at sprint-planning prices, and to buy the definition once, in writing, where everyone can read it.**

## See also

- [When a Closed Decision Reopens](../when-a-closed-decision-reopens/index.md) - the same scope ambiguity playing out across time and rooms; this article is the single-sprint version of that failure
- [Bringing Everyone to the Same Level](../bringing-everyone-to-the-same-level/index.md) - the tacit-knowledge variance problem at the execution layer, and how skills externalize what templates externalize at planning time
- [When Engineers Disagree on Best Practices](../when-engineers-disagree-on-best-practices/index.md) - how teams settle the conventions that eventually become shared defaults
- [Rough project size estimation](../questions/2020/03/02/index.md) - my order-of-magnitude estimation heuristic, including the rule that a one-month estimate means the task is hiding complexity
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - why outcome-level planning replaces granular estimation as execution becomes cheap
- [Who Maintains the Slop?](../who-maintains-the-slop/index.md) - what happens to the people who inherit work whose scope someone else, or something else, chose

## References

- [Wikipedia, "Common ground (communication technique)"](https://en.wikipedia.org/wiki/Common_ground_(communication_technique)) - the linguistics concept for the shared background listeners use to fill gaps in speech, and why partial common ground makes every ticket underspecified
- [Bill Wake, "INVEST in Good Stories, and SMART Tasks"](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/) - the canonical criteria for well-bounded stories, including negotiable and small
- [Wikipedia, "Planning poker"](https://en.wikipedia.org/wiki/Planning_poker) - the estimation ceremony whose real output is the divergence conversation, not the consensus number
- [Wikipedia, "Wideband delphi"](https://en.wikipedia.org/wiki/Wideband_delphi) - the estimation method planning poker descends from, designed around surfacing disagreement among estimators
- [Wikipedia, "Definition of done"](https://en.wikipedia.org/wiki/Definition_of_done) - the team-level completion contract, and the reason one team-wide line is too coarse to settle per-ticket boundaries
