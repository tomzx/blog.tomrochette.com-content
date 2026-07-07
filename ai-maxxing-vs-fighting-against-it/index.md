---
title: "AI-Maxxing and Resistance Are the Same Mistake: Optimize Attention, Not AI Quantity"
created: 2026-06-22
type: post
status: finished
tags: [ai, llm, strategy, productivity, judgment, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is a technical practitioner who has integrated LLMs into their daily work and has felt the pull to either automate everything or push back against the automation. No academic background required.
---

Two camps have hardened around LLMs, and they sound like opposites.
One wants AI in everything, automating every task that can be automated, measuring success by how little the human touches.
The other wants AI held at arm's length, preserving the craft, the understanding, and the roles that made the field what it is.
**They are not opposites; they are the same mistake pointed in different directions, and the mistake is optimizing how much AI to use instead of where to spend the attention AI frees up.**

## Two Postures, One Error

AI-maxxing treats the fraction of work delegated to a model as a score to be maximized.
If a task can be automated, it should be, and the human's remaining job is to orchestrate ever more automation.
Its reductio is the self-evolving codebase, the LLM agent company, the one-person team driving a dozen agents in parallel, none of them jokes and all of them early sketches of a real posture.

Resistance treats the fraction of work kept in human hands as a value to be defended.
If a task can be done by hand, it should be, because doing it by hand is what builds the skill and the identity that make the work worth doing.
Its reductio is the engineer in 2026 still typing boilerplate from memory and calling it craft.

Each camp carries a real insight.
The AI-maxxer is right that production has stopped being the bottleneck, and that clinging to manual production is no longer rational.
The resistor is right that not everything delegable should be delegated, because delegation can erode the very capability that makes delegation safe.
**Both are right about the other's blind spot and wrong about their own, because neither is asking the question that actually decides the outcome.**

## The Question Neither Camp Asks

The question that matters is not "how much AI should I use?"
It is "of the things I do, which are depreciating and which are compounding, and does AI move each one in the right direction?"

A depreciating activity is one whose value drops as the environment changes.
Typing boilerplate, memorizing an API, writing the fifth CRUD endpoint of the week: these were valuable when production was scarce, and they are melting in value every month that models get better.
A compounding activity is one whose value rises the more of it you do, and that feeds back into everything else.
Understanding a domain deeply, holding taste about what to build, judging whether a piece of code solves the right problem: these do not decay, and they make every other thing you do more effective.

The right posture falls out of this distinction immediately.
**Delegate depreciating activities ruthlessly, and protect compounding activities ferociously.**

The AI-maxxer breaks this by applying the delegation rule to everything, including the compounding activities, and slowly hollows out the judgment layer that makes the delegation produce anything worth having.
The resistor breaks it by applying the protection rule to everything, including the depreciating activities, and slowly mortgages the future to preserve a capability the market no longer rewards.

## Why AI-Maxxing Is the More Insidious Error

Here is the asymmetry that lifts this out of a polite "both sides" essay.

Resistance is a recoverable error.
The resistor falls behind, notices eventually, and can adopt the tools later.
The depreciating skills they protected are still useful during the transition, and the AI is still there, waiting.
The cost is lost time, which is real but bounded.

AI-maxxing is an insidious error, because it feels like winning the whole time.
The output keeps flowing.
The pull requests keep landing.
The agents keep producing plausible, confident, well-formatted work, and nothing in the loop tells you that the judgment layer underneath has been quietly atrophying.

Delegation is not free even when the model is free.
Every time you delegate a compounding activity, deciding what to build, evaluating whether the generated code is correct, choosing between two architectures, you forgo the practice that built the judgment you would need to evaluate the delegation.
The AI-maxxer assumes judgment persists without exercise.
It does not.
**A mind that never decides what to build loses the ability to tell whether what was built is worth shipping, and no model substitutes for that loss, because using the model well already presupposes it.**

This is the hole I pointed at in [The Shifting Bottleneck](../the-shifting-bottleneck/index.md): when you automate a layer, the bottleneck moves up to a more judgment-heavy layer, it does not disappear.
The difference is that the bottleneck article described the move as something that happens to the system.
AI-maxxing is what happens when you mistake the move for a disappearance, and convince yourself there is no bottleneck left worth staffing.

## Why Resistance Is Wrong, but Less Dangerously

The resistor's error is the mirror image, and it deserves to be named fairly.

Most of what the resistor calls craft is just production, and production has stopped being the scarce thing.
Writing code by hand does not teach the domain faster than reading code, including generated code, with intent.
Memorizing an API does not make you a better architect; it makes you a faster typist, for an API that will be deprecated in eighteen months.
**Protecting a depreciating activity in the name of craft is not craft; it is nostalgia with a deadline.**

The legitimate kernel inside resistance is the fear that delegation erodes capability.
That fear is correct, and the AI-maxxer should borrow it wholesale.
But the answer is not to refuse delegation across the board.
The answer is to refuse it selectively, at exactly the compounding activities where the erosion matters, and to embrace it everywhere else so aggressively that you buy back the time to do the compounding work properly.

The resistor who types their own boilerplate to "stay sharp" ends up with less time for the deep domain work that would actually keep them sharp, and they are protecting the wrong layer.
The AI-maxxer who delegates the deep domain work to "focus on orchestration" ends up with nothing left to orchestrate well, because orchestration without domain depth is just queue management.

## The Test That Settles It

For any activity on your plate, ask one question.
If I let the model do this for the next two years, will the me that emerges be more valuable, or less, than the me that kept doing it by hand?

Boilerplate, scaffolding, routine tests, formatting, summarizing a thread, drafting a first pass at a known pattern: delegate all of it, and the two-year-younger version of you is more valuable, because you spent those two years on something else that compounded.
Deciding what to build, judging whether a design is right, reading a hard paper with the intent of being able to teach it, debugging a subtle failure by reasoning about the system: keep these, even when a model offers to do them, because the two years of practice is the entire asset.

Notice that the test is about the allocation of your attention, not the quantity of AI you use.
An engineer who delegates ninety percent of their work to a model and spends the freed time going deeper on the remaining ten percent is not the AI-maxxer this essay argues against.
They are doing it right, and the high delegation ratio is a symptom of having correctly identified their compounding layer, not a target they are optimizing for.
**The number to watch is not how much you delegate; it is how much of your remaining time lands on compounding work.**

## The Boundary Moves, and That Is the Hard Part

The complication, and the reason this is not a one-time sorting exercise, is that the line between depreciating and compounding is not fixed.

A thing that was compounding yesterday can become depreciating tomorrow.
Writing SQL by hand was once a compounding skill, a path to a deep understanding of how the data informs the business; today the model writes the query and the deep part is knowing what to ask it for and whether the result is truthful.
Reading logs was once a compounding skill; increasingly the model triages them and the deep part is deciding which anomalies matter.
Each shift in capability redraws the line, and the posture that worked last year can become either error in the next.

This is why neither camp has a stable answer.
The AI-maxxer's "delegate everything" is wrong because some of what they delegate is still compounding, and the resistor's "do everything by hand" is wrong because some of what they protect has already stopped compounding.
**The only stable skill is the meta-skill of repeatedly telling the two apart, and that meta-skill is itself compounding, which is the strongest case I can make for spending attention on it.**

## What to Do on Monday

Stop measuring yourself by how much AI you use, in either direction.
Run the inventory instead.
List the activities that fill your week, and mark each one depreciating or compounding, using the two-year test.
Then push hard on both ends: delegate the depreciating ones as aggressively as you can, and ring-fence time for the compounding ones so that the time you bought back actually lands on them.

Do not be surprised if the result is a higher delegation ratio than the resistor would tolerate and a lower one than the AI-maxxer would brag about.
That is what getting it right looks like.
The ratio is an output, not a target.

And watch the boundary.
Re-run the inventory every few months, because the model's growth will have moved it, and an activity that was worth keeping may now be worth delegating, or, more dangerously, the reverse.
The most expensive mistake in either direction is the one you keep making because you sorted the list once and never looked again.

The AI-maxxer and the resistor are each certain they have found the answer, and that certainty is the real cost.
**The correct posture is uncomfortable: delegate like a maximalist, protect like a minimalist, and never stop asking which is which.**

## See also

- [The Shifting Bottleneck](../the-shifting-bottleneck/index.md) - why automating a layer moves the bottleneck up to a more judgment-heavy layer rather than away, the mechanism that makes AI-maxxing hollow
- [Keeping Up With AI Is a Losing Strategy](../keeping-up-with-ai/index.md) - the durable-versus-ephemeral distinction this article generalizes from information consumption to the whole of work
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - which friction is load-bearing and which is waste, the team-level version of the same allocation question
- [The Codebase Gardener](../the-codebase-gardener/index.md) - defending durable standards while letting ephemeral ones go, a concrete instance of the selective-protection posture argued for here
- [Scaling the LLM Agent Company](../scaling-the-llm-agent-company/index.md) - the near-limit of AI-maxxing at organizational scale, and what it still requires of human judgment

## References

- [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law) - why maximizing a proxy (fraction of work delegated) undermines the outcome the proxy stood for
- [Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) - the framework for why removing one bottleneck reveals the next, and why delegation never eliminates the judgment layer
- [Automation bias](https://en.wikipedia.org/wiki/Automation_bias) - the tendency to over-trust automated output, the failure mode that lets AI-maxxing feel like winning while judgment atrophies
- [Satisficing](https://en.wikipedia.org/wiki/Satisficing) - settling for "good enough" outputs, the silent cost of delegating compounding activities to a system that optimizes plausibility
