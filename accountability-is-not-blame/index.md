---

title: "Accountability Is Not Blame: What It Actually Means on a Software Team"
created: 2026-08-20
type: post
status: draft
tags: [software-engineering, teams, culture, accountability, individual-contributor, fully-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader is an individual contributor on a software team who has been told to "take accountability" or "be accountable" without being shown what that concretely requires. No management background needed.
agent_sessions:
  - ses_fe295e083ffe3SKX0hs519Y6Uz
---

At some point someone has told you to be accountable, asked whether you are accountable, or assured you that a process exists to guarantee accountability.
If you are an individual contributor, you may have noticed that nobody can say what any of that requires of you on a given Tuesday.
**The word feels empty because, in most of its uses, it is: accountability as practiced in software teams is usually blame with better manners, and blame genuinely does nothing for a broken system.**
There is a real thing under the word, and this piece is my attempt to dig the real thing out.

## The Feeling Is Correct, and It Is Also the Definition

Start from the observation that prompted this piece: when you cause an incident, being accountable does not really matter, the problem needs to be fixed.
I think that sentence is exactly right, and I also think it is not cynicism.
It is the definition.

Walk through what a broken production system actually needs.
The system needs repair.
The affected users need to be told.
The failure mode needs to be prevented from recurring.
Now add "and someone needs to be accountable" to the list and watch the addition contribute nothing.
The phrase does not restore service, inform a customer, or close the gap.
**At the moment of failure, everything that matters is forward-facing work, and the backward-facing question, whose fault this was, is worthless until the forward work is done.**

Here is the twist.
The observation is not an argument against accountability; the observation is the content of accountability.
**Doing the forward work is what the word usefully names.**
Accountability feels meaningless because teams spend the word on feelings, rituals, and punishments, when the only useful thing the word can name is a set of actions.

## Blame Asks One Question, Accountability Answers Another

Blame asks who caused this.
Blame looks backward, requires a failure to exist first, and produces a person to absorb cost.
Accountability asks who owns what happens next.
Accountability looks forward, can be assigned before anything breaks, and produces work: repair, communication, prevention.

That difference gives you a test for every use of the word.
**If someone's accountability only exists after something breaks, the accountability was blame all along.**
Real accountability is legible before the failure, in who is expected to answer for a thing while the thing still works.
An approver's signature on a pull request fails that test: the signature exists to be pointed at afterward, which is why I called the signature accountability theater in [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md).

## Why Assign It at All

The obvious objection: in practice the fix happens anyway.
Somebody steps up, the outage ends, the users get an email.
If the work gets done regardless, what does the word add?

Watch what actually happens in a team where nobody is assigned the consequences.
The work does not disappear.
The work gets assigned by proximity: the broken thing lands on whoever is standing nearest when the break happens, whoever is on call, whoever knows that corner of the codebase, whoever cares enough not to walk away.
The reward for building the feature went to the feature's author months ago, and the cost of the feature's failure lands on whoever happens to be downstream today.
[Who Maintains the Slop?](../who-maintains-the-slop/index.md) describes the extreme version of that arrangement under generated code: the producer captures the benefit, the maintainer inherits the cost, and maintenance becomes a tax on the people who care, levied by the people who do not.
**The alternative to assigned accountability is not shared ownership; the alternative is assignment by proximity, which is the least fair and least efficient allocation mechanism available.**

Assignment before the failure also buys speed and learning.
When the void opens, who repairs, who decides the mitigation, who tells the customer, who prevents a recurrence: a team that answered those questions in advance skips the negotiation and starts the work.
And an owner who repairs a failure has the context to fix the cause, while a passer-by assigned by proximity patches the symptom and moves on.

## What Accountability Is Made Of, for an Individual Contributor

This is the part nobody explains, so here is the entire content of the word as observable behavior.
If you do these things you are accountable, whatever anyone feels about you.
If you do not do these things you are not accountable, whatever anyone says.

**Before anything breaks, accountability is a claim made out loud.**
You say what you will do and by when.
You flag early when the work slips, while the options are still cheap.
You surface the risks you see while the risks are still welcome news.
None of that is virtue.
A person who claims work out loud can be given autonomy over that work, because the team knows in advance where the answer will come from.

**While the work runs, accountability is decisions that leave a trace.**
Every non-trivial choice gets a sentence of why, somewhere findable.
The record of why is what lets whoever investigates in six months fix the source instead of the symptom, and the record is also what protects you when the memory of the decision has faded and only the consequence remains.

**After something breaks, accountability is three acts.**
Repair: you fix the failure, or you drive the fix to whoever can, and "not my ticket" is not in your vocabulary while the system is down.
Truth: you say what happened, accurately, including your own part in it, without waiting to be asked and without burying the relevant fact on page four of the postmortem.
Prevention: the class of failure gets encoded somewhere permanent, a test, a gate, a runbook, so the same pain cannot recur silently.
That trio is everything "taking accountability" can ask of you after an incident.
The apology is not on the list, and neither is the somber tone in the meeting.
If you do the three acts and someone still wants something from you, what that person wants is a performance of contrition, which is blame in ceremonial dress.

## Why the Team Must Not Punish Any of It

Accountability has a partner clause, and teams that skip the partner clause destroy the whole arrangement.
If telling the truth about your part in a failure gets you punished, even softly, through tone in the meeting, through boring assignments next quarter, through a smaller raise, people do not stop making mistakes.
**People stop reporting the mistakes.**
The casualty is not morale; the casualty is information.
Near-misses go unmentioned, bad news travels slowly, and postmortems name systems while omitting the human decisions underneath, which is where the actual information lives.

Aviation and medicine learned that lesson the hard way and built [just culture](https://en.wikipedia.org/wiki/Just_culture) on top of the lesson: human error is treated as information about the system, and only willful violations draw sanctions.
Google's reliability practice makes the same move with [blameless postmortems](https://sre.google/sre-book/postmortem-culture/), written to identify contributing causes without targeting individuals, precisely because the details worth learning from are the details punishment teaches people to hide.
Research on [psychological safety](https://en.wikipedia.org/wiki/Psychological_safety), the belief that speaking up will not be punished, finds that belief is the strongest predictor of team effectiveness.
The deal is simple: engineers bring the truth fast, and the team answers the truth with system fixes instead of sanctions.
**A team that punishes truth trades a brief feeling of justice for permanent ignorance of its own failures.**

## Accountability Is the Currency That Buys Autonomy

One last reframe, because the word usually arrives with a threat attached and the word deserves better.
A team can only give you independence to the extent you answer for outcomes.
Nobody lets you own a service alone, or a migration, or a customer relationship, without knowing where the answer will come from when the thing breaks.
**Accountability is the currency you pay for autonomy, and you pay the currency in advance.**
The role also survives the shift to agent-driven work: an agent can produce the work, but a person answers for what was decided, which is the one seat [Solo Is a Team Size](../solo-is-a-team-size/index.md) reserves for humans.
So the individual contributor's question, what accountability even means for me, inverts into a better question: how much autonomy do I want?
You buy autonomy with accountability, and the price is posted.

## What to Do Next

Pick the three things you own with real consequences, a service, a pipeline, a migration, a domain.
For each, answer in one sentence: if this breaks at 3 a.m., who is expected to repair, tell the truth, and prevent recurrence?
If the answer is not you, find out whose answer the answer is.
If the answer is nobody, you have found a piece of work waiting to be assigned by proximity.

Before your next claim of "done", say what done includes and what you will still answer for afterward: bugs for a window, the data after the migration, the behavior under load.
The sentence takes ten seconds and converts accountability from a property of your presence into a contract.

After your next incident, run the three acts deliberately.
Drive the repair even if the ticket landed on someone else.
Write the account with your part in it, unprompted.
Encode the prevention before the adrenaline fades.
Then notice whether anything you did was punished, even softly.
If something was, the punishment is the real defect, and the punishment sits upstream of every other one.

## See also

- [Who Maintains the Slop?](../who-maintains-the-slop/index.md) - what assignment by proximity looks like at full strength: the producer captures the benefit and the maintainer inherits the cost
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - the original accountability theater argument: signatures certify presence, not reading, and real responsibility lives upstream in decisions
- [The Merge Gate](../the-merge-gate/index.md) - the approval click as a name on a line that exists to allocate blame after the fact rather than prevent harm before it
- [Solo Is a Team Size](../solo-is-a-team-size/index.md) - accountability as the human seat's role in an agent fleet: a person answers for what was decided
- [What the Author Brings When the Model Writes](../what-the-author-brings-when-the-model-writes/index.md) - the same mechanism in writing: a name with something to lose is what gives words their weight

## References

- [Just culture (Wikipedia)](https://en.wikipedia.org/wiki/Just_culture) - the safety-industry framework separating human error from willful violation, so that truth is never punished
- [Google SRE Book, "Postmortem Culture: Learning from Failure"](https://sre.google/sre-book/postmortem-culture/) - blameless postmortems and why the approach produces the details that punishment suppresses
- [Psychological safety (Wikipedia)](https://en.wikipedia.org/wiki/Psychological_safety) - the belief that speaking up is safe, the strongest known predictor of team effectiveness
