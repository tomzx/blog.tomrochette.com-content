---
title: "Team Maturity Explains the Friction, the Foundation Predicts the House of Cards"
created: 2026-06-30
type: post
status: finished
tags: [ai, software-engineering, llm, team-management, productivity, devops, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is an engineering lead, tech lead, or senior engineer whose team already uses LLM coding tools and who is trying to understand why peer teams get very different results from the same tools.
---

In the age of LLMs, the work that matters at your job is no longer adopting the tools.
It is raising the velocity at which your team can ship features without turning the software it builds into a house of cards.
When two teams hold the same tools and get wildly different outcomes, the first thing to study is the team itself, and Bruce Tuckman's model of group maturity will explain a large share of the gap.
**But it will not explain all of it, because team maturity governs how easily a team absorbs a new practice, not whether the software that practice produces stays standing.**
Maturity is necessary and it is not sufficient, and most organizations are diagnosing only half the problem.

## The Real Job Is Velocity Without Debt

Raw velocity stopped being interesting the year a model could draft a feature in an afternoon.
Anyone can go fast now.
The constraint that separates serious teams from reckless ones is sustainable velocity, the ability to ship quickly and also keep the system survivable as it grows.

This is not a new distinction that AI invented.
The [DORA research program](https://dora.dev/) spent years measuring engineering organizations along two independent axes, throughput and stability, and its central finding was that you have to track both because they are not the same thing.
Throughput is lead time and deployment frequency, how fast work gets out.
Stability is change failure rate and time to restore, how often what you ship breaks and how long it takes to recover when it does.
A team can score high on throughput and low on stability, and that team is not fast.
It is a house of cards being shuffled quickly, and the bill comes due as [rework](../rethinking-code-review-in-the-age-of-llms/index.md), outages, and a codebase nobody is willing to touch.

LLMs supercharge the throughput axis for free.
They do nothing for the stability axis unless your engineering system is built to hold them accountable.
**So the whole question of which teams ship effectively with LLMs collapses into a narrower one: which teams can absorb the throughput multiplier without their stability metrics collapsing?**
That is a property of the team and a property of the code, and the team part is only half of it.

## Why Tuckman Explains So Much of the Adoption Gap

Before the other reasons, it is worth being honest about how much Tuckman's [stages of group development](https://en.wikipedia.org/wiki/Tuckman%27s_stages_of_group_development) actually explain, because the answer is a lot.

A team in the performing stage adopts a new AI practice with low friction for reasons that are structural, not cultural.
Its members have already negotiated how decisions get made, so "which code review workflow do we use now that the model writes most of the code?" gets resolved in one meeting instead of three.
Its conventions are settled and shared, so when an engineer introduces a prompt template or a skill, the rest of the team can tell whether it fits the way they already work.
It has the psychological safety that [Project Aristotle](https://rework.withgoogle.com/print/guides/5727380657274880/) identified as the strongest predictor of team effectiveness, which means an engineer can say "the model's output is wrong here and I do not understand why" without that admission costing them status.

A team still in forming or storming has none of this, and so it pays the adoption tax on every change.
As I argued in [When Engineers Disagree on Best Practices](../when-engineers-disagree-on-best-practices/index.md), a team that has not yet built a repeatable process for resolving disagreements will relitigate the same practice debate over and over, and the debate is rarely about the practice.
It is a proxy for unresolved questions about whose judgment the team trusts.
LLM adoption surfaces a dozen of these questions at once, because it touches review, testing, specification, ownership, and onboarding simultaneously.
A performing team processes all of that in the background.
A storming team drowns in it.

So if your observation is "some teams picked up the new AI workflows easily and others fought about it for two quarters," Tuckman is very likely your explanation.
**Team maturity is the dominant predictor of adoption friction, and adoption friction is the dominant predictor of whether a team even gets to the starting line.**

What it is not the dominant predictor of is what happens after the team starts shipping.

## The House of Cards Is Predicted by the Foundation

Here is the gap maturity cannot close.
A mature, high-trust, psychologically safe team sitting on top of a brittle codebase with no tests and no specification discipline will still ship a house of cards.
It will just do so with impressive cohesion, minimal interpersonal drama, and a strong retrospective culture.
The team dynamics are good and the software is still wrong, because the things that decide whether generated code stays standing are properties of the engineering system, and those properties vary somewhat independently of how well the team gets along.

If you want to know why two mature teams with the same tools ship software of very different durability, look at the foundation.
The factors below are not equal in importance.
Two of them, verification and codebase health, decide whether the software stands up at all, and the other four only improve the quality of what gets built.
No amount of strength in the four can compensate for weakness in the two, because the two are what keep the structure standing.
**For shipping without a house of cards, verification and codebase health outrank team maturity, and the rest exist to support them.**

### The two factors that outrank maturity

These are the load-bearing ones.
A team weak on either of them ships a house of cards regardless of how mature it is, and a team strong on both can survive even rough team dynamics.
Everything else in the foundation eventually feeds into one of these two.

#### Verification is the throttle

Once code writes itself, the bottleneck moves to checking whether the code is correct, and that move is the central claim of [The Shifting Bottleneck](../the-shifting-bottleneck/index.md).
This is where the stability axis lives, and it is why two teams with identical throughput can have radically different change failure rates.

The team with a fast, trustworthy test suite, a CI pipeline that catches real regressions, and a short feedback loop can let the model generate aggressively, because it can verify cheaply.
Every generation is a hypothesis and the test suite is the experiment, and the cost of a wrong generation is seconds.
The team that verifies by reading the diff, or by running the feature once in a staging environment, cannot afford to let the model run.
It hits a ceiling where the human reviewer becomes the bottleneck, and either it slows down to stay safe or it speeds up and ships unverified code.

This is the DORA stability axis measured in engineering practice.
**The team that ships safely with LLMs is usually not the team with the best prompters.
It is the team with the best test suite and the fastest signal**, because that team can convert the throughput multiplier into stable throughput instead of into rework.
Investing in verification infrastructure is now the highest-return thing a team can do to raise its LLM shipping velocity, which is a counterintuitive claim only if you are still measuring velocity as lines produced rather than features landed without rollback.

#### The codebase is the model's context

The other load-bearing factor is that the LLM does not generate code in a vacuum.
It generates code as a continuation of the context it is given, and the largest piece of context is the codebase itself.
A clean, well-factored codebase with clear naming, consistent patterns, and a single way of doing each thing is excellent context, and the model faithfully reproduces its conventions.
A tangled codebase with five competing styles, dead abstractions, and comments that contradict the code is terrible context, and the model faithfully extends the mess.
As I argued in [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md), the context is the entire mechanism by which a frozen set of weights produces behavior relevant to your situation, and the codebase is the part of the context you control.

This is why the same model, the same prompt, and the same engineer produce different quality output on different codebases.
The codebase is doing most of the work, and a codebase that is already a house of cards is a context that asks the model to build more cards.
**You cannot hand an LLM a cathedral built on sand and get back a cathedral built on bedrock.
You get back a taller pile of sand.**
The teams shipping safely are, more often than they realize, the teams whose codebase was already safe to extend, and the LLM is merely making that pre-existing health visible at higher speed.

### The factors that strengthen the foundation

The next four factors do not replace the first two.
They decide how much wrong output the verification layer has to catch, and how high the ceiling on the best possible generation sits.
A team that is strong here and weak on verification still ships a house of cards, just a slightly smaller one.
A team that is weak here and strong on verification stays safe, but slowly, because its loop drowns in bad output it has to reject.

#### Specification discipline separates amplifiers from noise

An LLM is a multiplier on the quality of the instructions it receives, which means the teams that win are the ones that produce high-quality instructions at scale.
This is specification, and it is the skill that [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) names as the highest-leverage capability in the current era.

A team that writes a precise specification before it prompts, one that defines what done means, which invariants must hold, and which edge cases matter, gets an LLM that behaves like an effective pair programmer.
A team that prompts first and specifies never gets a hallucination engine that produces plausible code solving the wrong problem, and the wrongness is often invisible until production.
Specification is also where the human bottleneck genuinely lives now, because writing a precise spec is hard cognitive work that the model cannot do for you until you have done the thinking it depends on.
**Teams that institutionalize specification, through templates, through review of the spec before the implementation, through a skill that enforces the steps, pull away from teams that treat the prompt as the spec, and they pull away fast.**

#### Conventions have to be written down to be inherited

A performing team has settled conventions, and that is exactly what makes the team mature.
But settled conventions that live only inside the senior engineers' heads are invisible to two important workers: the new hire, and the LLM.
Neither of them received the osmosis.

The teams that ship consistent, safe output at scale are the ones that have externalized their conventions into a form the model actually reads.
That means lint rules the CI enforces, architecture decision records that capture why a choice was made, contribution guides that name the patterns to reuse, and, most powerfully, [skills](../bringing-everyone-to-the-same-level/index.md) that encode a team's process as executable steps the agent follows on every run.
A convention in a head is advice the model will ignore.
A convention in a skill or a lint rule is a constraint the model has to satisfy.

This is the mechanism by which a mature team scales its maturity into the model.
A storming team that somehow wrote its conventions down would get more out of the LLM than a performing team that left them tacit, which is a real inversion and a useful diagnostic.
**If your team is mature and your LLM output is still inconsistent, the conventions are probably in the wrong place.**
They are in people, and they need to be in files.

#### Review is a backstop, not the mechanism

The instinct when a tool speeds up code production is to use it to speed up code review, and on this point the instinct is closer to right than wrong, for a reason that is easy to miss.

Code review is a one-time signal.
It catches what one reviewer notices, once, on the diff in front of them, while they happen to be alert.
A specification prevents the whole class of issue from reaching implementation, and a test catches the same bug on every future run, for as long as the codebase exists.
As [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) argues, an hour spent improving the specification outranks an hour spent reviewing the output, because the specification compounds and the review does not.
**For the purpose of shipping without a house of cards, specification is the load-bearing lever, and review is the non-compounding backstop behind it.**

The backstop still has a job, but it is narrower than the one review used to claim.
With generated code the reviewer is the only brain in the loop, so a light, intent-focused check still catches the occasional wrong assumption before it ships.
What it does not do is scale.
If the model produces ten changes a day, ten hours of human review is not a process that survives, and the right response to a repeated class of review comment is to encode it as an automated gate so it never depends on a human noticing again.
The teams that ship safely let the model handle style, keep a thin intent check as the backstop, and spend the freed review hours writing better specifications.
The teams that ship a house of cards inverted this, keeping review heavy while starving the specification that actually prevents the cards.

#### Domain depth and the discipline to build less

Both of the following are judgments the model cannot make for you: what the software should do, and whether it should exist.

The first is that the model produces code that is technically correct and strategically wrong, faster than ever, when nobody on the team deeply understands the business context.
Deciding whether a feature should exist, and what shape it should take, is the part of the pipeline AI cannot do, and it is the bottleneck the throughput multiplier pushes you into, exactly as the shifting bottleneck predicts.
A team with deep domain ownership extends its system coherently.
A team spread thin across too many concerns generates five services where one would do, and each of them is a card.

The second is that cheap implementation makes overbuilding the default temptation.
Every generated feature is surface area for bugs, cognitive load, and future constraints, and the cost of maintaining a feature never approached zero the way the cost of writing it did.
The team with the discipline to say "we do not need this, ship the smaller thing" survives longer than the team that ships everything the model can draft, and that discipline is a product judgment that maturity does not produce on its own.
It comes from somewhere else, usually from someone at the table who has been burned by feature bloat before and is willing to be the friction.

## How Maturity and Foundation Interact

The honest synthesis is that these two layers reinforce each other, and the most effective teams are strong on both, but they fail in characteristically different ways.

A performing team on a clean foundation with strong tests and written conventions is the team that wins this era.
It absorbs new AI practices without friction, and when it ships, the foundation catches what the model gets wrong.
A performing team on a brittle foundation hits a wall it cannot see, because the team dynamics are good and so nobody is arguing, and the stability metrics degrade quietly until a production incident makes them visible.
A storming team on a clean foundation still wastes most of its energy on the wrong fights, but its code tends to survive the fights because the foundation holds.
A storming team on a brittle foundation fails loudly and fast, which is at least easy to diagnose.

The trap is to read every symptom as the layer you already know how to fix.
Engineering management tends to diagnose everything as team dynamics, because that is the toolkit it has, and so it sends a brittle-foundation team to a retrospective when what it needs is a test suite.
Engineering teams tend to diagnose everything as tooling, because that is the toolkit they have, and so they adopt a new model when what they need is a written convention.
**The binding constraint is usually the layer you are not looking at, and maturity is very good at hiding problems in the foundation because a mature team does not complain about them until they break.**

## What to Do on Monday

If you lead a team and want to know whether you are shipping features or shipping cards, a few concrete moves separate the diagnosis from the guesswork.

Measure both DORA axes, not just throughput.
If your deployment frequency is rising and your change failure rate or time to restore is rising with it, you are not getting faster.
You are getting more volatile, and the LLM is the reason.
The stability metrics are the house-of-cards indicator, and they are free to collect.

Treat the codebase as context and pay down the part the model keeps getting wrong.
If the LLM consistently produces bad output in one module, that module is bad context, and the fix is to refactor the module, not to write a longer prompt.
The model is telling you where your code is incoherent, because incoherent code is exactly what it reproduces worst.

Write your conventions down somewhere the model reads them.
A skill, a contribution guide, a lint rule, an architecture decision record, anything that moves a standard out of a head and into the execution path.
The test is whether a new engineer and a fresh agent both produce work that matches the team's patterns on day one without being told.

Keep a thin, intent-level review as a backstop and let the model own style.
If your review comments are still about formatting, you are spending human attention on the part the model already fixed.
Reallocate those hours into specification, which is the lever that compounds.

And write the specification before the prompt, every time.
The spec is the highest-leverage artifact in the pipeline now, and the team that treats it as optional is the team whose LLM output drifts toward plausible-and-wrong.

## The Team That Wins

The teams that win this era are easy to misread.
They look like the most mature teams, and they often are mature, but the maturity is doing a specific job.
It is letting them adopt new practices without bleeding energy, so that they can spend that energy on the foundation that actually decides whether the software stands up.

Maturity is how you remove the friction of getting started.
The codebase, the tests, the specifications, the written conventions, and the intent-level review are how you keep the result from collapsing under its own weight.
**Study your teams, because Tuckman will tell you a lot.
Then study the code they are standing on, because that is what determines whether the velocity they have earned is velocity they get to keep.**

## See also

- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - which processes earn their keep and which to eliminate once execution is cheap, including the case for specification as the highest-leverage skill
- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - why automating production relocates the constraint to verification, the layer where the house of cards is built or caught
- [Bringing Everyone to the Same Level](../bringing-everyone-to-the-same-level/index.md) - how written skills encode a team's process so the model and the new hire inherit the same standards
- [When Engineers Disagree on Best Practices](../when-engineers-disagree-on-best-practices/index.md) - the forming-stage mechanics that make team maturity the dominant predictor of adoption friction
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - the case that specification compounds while review is a one-time signal, which is why the spec outranks the diff
- [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md) - the codebase-as-context claim this article leans on, and the mechanism behind it
- [Learn the Foundation, Not the Syntax](../learn-the-foundation-not-the-syntax/index.md) - the durable mental models that let an engineer catch what the model gets wrong in production

## References

- [Wikipedia, "Tuckman's stages of group development"](https://en.wikipedia.org/wiki/Tuckman%27s_stages_of_group_development) - the forming-storming-norming-performing model that explains why mature teams absorb new practices with low friction
- [Google re:Work, "Guide: Understand team effectiveness"](https://rework.withgoogle.com/print/guides/5727380657274880/) - Project Aristotle's finding that psychological safety is the top predictor of team effectiveness, the performing-stage asset that makes honest disagreement possible
- [DORA, "State of DevOps"](https://dora.dev/) - the research program establishing throughput and stability as independent axes, which is the formal version of velocity-without-the-house-of-cards
- [Google Cloud, "State of DevOps Report"](https://cloud.google.com/devops/state-of-devops) - the annual report tracking how elite teams separate lead time and deployment frequency from change failure rate and time to restore
- [Wikipedia, "Theory of Constraints"](https://en.wikipedia.org/wiki/Theory_of_constraints) - the framework for why removing the production bottleneck relocates rather than eliminates the constraint, landing it on verification
