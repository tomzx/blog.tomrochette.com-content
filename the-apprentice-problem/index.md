---

title: "The Apprentice Problem: Where Does New Judgment Come From?"
created: 2026-08-25
type: post
status: finished
tags: [ai, software-engineering, llm, learning, career, team-management, apprenticeship, fully-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader is a senior engineer, lead, or manager who has watched junior-level work disappear into automation and wondered who becomes senior next. No management background required.
agent_sessions:
  - ses_fc86479fbffeFATCXXl5ZqLUNX
---

Every senior engineer I know learned the same way: by doing junior work for years.
The bug fixes, the small features, the boring refactors, the reviews where someone senior tore their code apart.
That work was never just output.
It was the training ground where judgment formed under supervision, with real feedback, at low stakes.
**Automate the junior work and you do not just lose the output; you cut the input to the pipeline that produces senior engineers.**
Nobody announces this.
The economics do it quietly, one automated task at a time.

## How Judgment Actually Forms

Judgment is not transferred by explanation.
It is grown by contact with consequences.
The [Dreyfus model of skill acquisition](https://en.wikipedia.org/wiki/Dreyfus_model_of_skill_acquisition) describes the path: novice, advanced beginner, competent, proficient, expert, where each step up is driven less by rules learned and more by experience absorbed.
The rules are the easy part.
What separates a competent engineer from an expert one is the library of felt cases, the bugs chased at 2 a.m., the refactor that made things worse, the outage traced to a decision the engineer personally made.

Apprenticeship was never ceremony.
It was the delivery mechanism for consequences.
A junior shipped a small change, the change broke something, and the feedback arrived fast enough to leave a mark.
Small blast radius, real stakes, tight loop.
[Deliberate practice](https://en.wikipedia.org/wiki/Deliberate_practice) works the same way in every field studied: repetition at the edge of ability, with immediate feedback, is the only known mechanism that builds expertise.

The junior work being automated is not adjacent to that mechanism.
It is that mechanism.

## The Economics Remove Exactly the Wrong Layer

The uncomfortable part is that automating junior work is correct, locally.
When an agent fixes the small bug in an afternoon for cents, paying a junior to spend a week on it looks like charity.
No single manager makes a bad decision.
Every decision is rational, and the aggregate is a pipeline with its input cut.

The pattern is familiar from [The Shifting Bottleneck](../the-shifting-bottleneck/index.md): automate a layer, and the constraint moves up.
But this time the constraint does not just move.
It starves, because the layer above was grown from the layer below.

The danger is the delay.
A pipeline with no input still ships output for years, from the inventory of already-formed senior engineers.
By the time the shortage is visible in hiring metrics, the training ground has been gone for a decade.
**The apprentice problem is a slow-motion staffing crisis that no quarterly review will catch, because the seniors are still performing.**

## The Same Collapse, One Level Up

There is a structural precedent.
[Model collapse in code](../model-collapse-in-code/index.md) describes what happens when models train on their own output: the tails disappear first, the average looks fine, and the distribution narrows with each generation.
An organization that stops training juniors runs the same loop on people.
The seniors encode their judgment into systems and agents, the next engineers learn from those systems instead of from supervised contact with reality, and what they acquire is the smoothed average of their predecessors, rounded off a little more each generation.
The rare cases, the exceptions, the reasons behind the rules are exactly what does not survive the transfer, and exactly what judgment was.

I am not claiming people are models.
I am claiming the loop is the same structure: output consumed as input, without fresh contact with reality, degrades in the tails first.

## What Replaces the Old Apprenticeship

The answer is not to ban agents from junior work, that battle is over and nostalgia is not a strategy.
The answer is that apprenticeship has to become deliberate now that it is no longer incidental.
Three moves cover most of it.

**Make juniors the supervisors, not the supervised writers.**
There is still a mountain of work that needs a human mind: reviewing agent output, verifying claims against evidence, catching the plausible-and-wrong.
Put the junior on that mountain, with a senior reading their verdicts.
The feedback loop is just as tight, judging output and being judged on the judgment, and the skill being trained is the one that actually remains scarce.
The new junior work is acceptance.

**Reserve work for humans on purpose.**
A team that assigns every task to whichever worker is cheapest has decided, implicitly, not to grow anyone.
Some tasks should be reserved for the person who would learn most from them, at a productivity cost the team accepts knowingly.
[Software engineering teams in the age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) makes the general case for keeping friction that pays; this is the specific friction that pays in people.

**Teach judgment directly, out loud.**
The old pipeline taught judgment osmotically, through years of proximity.
The deliberate version is faster and demands more from seniors: decision reviews, where a junior predicts the call before hearing it; postmortems walked through live, not archived; the why behind every convention made explicit instead of encoded and forgotten.
Encoding your judgment into a system, the move [Scaling Yourself Horizontally](../scaling-yourself-horizontally/index.md) argues for, and transferring it to a successor are not the same act, and only one of them renews the supply.

## What to Do Next

If you run a team, trace one recent junior-level task end to end and ask who could do it next year for the first time.
If the answer is nobody, because it will be automated, you have found a hole in the pipeline, and the fix is to route the learning part of that task somewhere it still exists.

If you are early in your career, stop competing with the machines on production and compete on acceptance.
Build the record of catches, verdicts that held up, errors found in output everyone else approved.
That record is the new seniority.

If you are senior, pick one person and start teaching out loud this month, decisions, not syntax.
The foundations are a separate argument, and [Learn the Foundation, Not the Syntax](../learn-the-foundation-not-the-syntax/index.md) makes it, but foundations without felt consequences produce competence without judgment.

The question every organization is currently answering by default is: who is allowed to become senior next?
**Leaving that to the economics of task assignment is how the answer becomes nobody, slowly enough that no one notices until the last senior leaves.**

## See also

- [Scaling Yourself Horizontally](../scaling-yourself-horizontally/index.md) - the upstream piece: encoding judgment into systems, and the warning that cheap systems consume the training ground that produces general judgment
- [Model Collapse in Code](../model-collapse-in-code/index.md) - the same degradation loop at the corpus level, output training output, tails disappearing first
- [Learn the Foundation, Not the Syntax](../learn-the-foundation-not-the-syntax/index.md) - what to teach when production is automated: mental models of execution, cost, and failure rather than syntax
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - the team-level case for keeping friction that pays, of which training juniors is the clearest instance
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - the general pattern of constraints moving up when a layer is automated, here with the twist that the upper layer starves
- [The Acceptance Gap](../the-acceptance-gap/index.md) - the acceptance work that becomes the new junior training ground, generation solved and judgment remaining

## References

- [Dreyfus model of skill acquisition](https://en.wikipedia.org/wiki/Dreyfus_model_of_skill_acquisition) - the novice-to-expert progression, where advancement comes from absorbed experience rather than rules
- [Deliberate practice](https://en.wikipedia.org/wiki/Deliberate_practice) - the research consensus that expertise builds through repetition at the edge of ability with immediate feedback
- [Apprenticeship](https://en.wikipedia.org/wiki/Apprenticeship) - the historical delivery mechanism for learning through supervised real work
