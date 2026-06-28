---
title: "Learn the Substrate, Not the Syntax: Why Low-Level Languages Still Matter When the Machine Writes the Code"
created: 2026-06-28
type: post
status: finished
tags: [ai, software-engineering, llm, learning, craft, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is a practicing engineer, senior developer, or educator deciding what fundamentals new developers still need now that LLMs produce most of the code. Comfortable with the idea that code generation is being automated; no formal CS background required.
---

The question gets asked as a fork in the road: either drill new developers on low-level languages until they can write a kernel from memory, or accept that writing code is finished and retrain everyone into prompt-shaped product managers.
It is a false dichotomy, and both branches are wrong for the same reason.
**They both confuse the surface of programming with the thing programming was always meant to teach, and that thing is now the only part AI cannot do for you.**

## Two Errors, Shared Confusion

The "teach them everything" camp treats low-level fluency as a production skill.
It points at manual memory management, pointer arithmetic, and hand-rolled data structures as the price of admission to the profession, and it is right that these were once essential.
It is wrong that they still are, as production.
Writing C by hand stopped being the bottleneck the year a model could write it, read it, and port it faster than a careful senior could, and the market has already priced that in.

The "writing code is over" camp takes the same observation and overruns with it.
If production is automated, the argument goes, the developer's job becomes specification and orchestration, and the substrate the code runs on is somebody else's problem, probably the machine's.
This is the AI-maxxing error applied to education, and it is the more dangerous of the two, because it feels like foresight while quietly removing the one capability that becomes scarcer and more valuable exactly as production gets cheap: the mental model of how the system actually behaves.

Both camps make the same mistake the resistor and the maximalist make in [AI-Maxxing and Resistance Are the Same Mistake](/ai-maxxing-vs-fighting-against-it): they argue about how much low-level to use instead of asking what low-level is for.
The answer to that question dissolves the debate.

## What Low-Level Actually Teaches, and Why It Compounds

Strip away the syntax drills and the "implement linked lists in C" hazing, and a low-level language is a teaching apparatus for a small number of durable mental models.
None of them are about the language.
They are about the machine the language sits on top of, and they are exactly the models that become load-bearing once you can no longer trust the code you are reading.

A model of execution.
What lives in memory, what gets allocated where, what a call frame is, what happens when a function returns.
This is not trivia.
It is the difference between an engineer who can read a stack trace and one who can only read an error message, and the generated code that breaks in 2026 breaks in ways that only the first engineer can diagnose.

A model of cost.
Big-O is taught in school and forgotten because it is inert until you have felt a cache miss, an allocation storm, or an N-plus-one query at the boundary between the ORM and the database.
Low-level work is the cheapest known way to make that cost felt in the body, and once it is felt it transfers to every higher language you will ever touch.
When the model produces plausible code that is also quietly quadratic across a network boundary, the person with a cost model catches it and the person without ships it.

A model of failure.
Low-level code fails honestly: a segfault, a leak, a data race, a corrupted pointer.
The cause is concrete and the lesson sticks.
High-level and generated code fails softly, at the seams between abstractions, and the softness is the hazard, because soft failures train nothing and accumulate until they become outages.
The engineer who learned on honest failures can debug the soft ones.
The reverse is not true.

And, most importantly, a model of where the abstractions leak.
Every stack you will ever work on is a tower of abstractions, and every one of them [leaks under stress](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/): the ORM leaks into SQL, the garbage collector leaks into latency, the container leaks into the kernel, the model's confidence leaks into a hallucinated API call.
When a leak surfaces in production, the person who can see through the abstraction to the layer underneath is the person who fixes it.
Everyone else files a ticket and waits.

These four models are not production skills.
They are not even, strictly, low-level skills.
They are durable skills, in the sense [Keeping Up With AI Is a Losing Strategy](/keeping-up-with-ai) draws between the ephemeral and the durable: they do not decay across model generations, and they make every other thing you do, including supervising a model, more effective.
**That is the entire case for low-level in one sentence: it is the most efficient known way to build the models that do not depreciate.**

## Why "Writing Code Is Over" Is the Dangerous Half

Here is the asymmetry that settles which error matters more.

Forgetting low-level syntax is a recoverable error.
The developer who never memorized the C calling conventions can look them up, or ask the model, the day they need them, and the cost is a few minutes.

Losing the mental model is not recoverable in the moment you need it.
When the generated code is failing in production at three in the morning, there is no time to develop an intuition for memory layout, and the model that wrote the code is the same model confidently misdiagnosing it.
You can build a mental model with an LLM as a tutor, over time, the same way you can build one with a good textbook or a patient colleague; the tool is not the obstacle, the hours of deliberate study are.
**What you cannot do is prompt one into existence under time pressure, and using the model to debug its own output already presupposes the very model it would take weeks to grow.**

This is the [shifting bottleneck](/the-shifting-bottleneck) wearing its sharpest face.
Production was the bottom of the stack, and automating it moved the constraint up to verification, and verification is precisely the layer that demands the substrate knowledge the "code is over" camp wants to skip.
The preparation that says "we will not need this because writing is automated" is the preparation that makes you unable to do the job writing's automation created.
You are optimizing away the exact layer the bottleneck landed on.

There is a near-term counter-argument worth taking seriously: that verification gets automated too, and then specification, and so on up the stack.
Even granting that, the same framework says the bottleneck just moves to deciding what to build and whether what was built is correct, which still requires understanding systems deeply.
I cannot find a version of this future in which understanding the substrate stops compounding, only versions in which the surface syntax stops mattering.
Those are different claims, and the debate quietly collapses them into one.

## The Onboarding Hole the Tools Opened

There is a structural reason this question is urgent now, and it is not philosophical.
For most of the profession, a developer built their mental model of systems the only way the model can be built: by struggling with code that broke, reading core dumps, profiling slow paths, and fixing real failures under real pressure, repeatedly, for years.
The struggle was the curriculum, and it was free, because it was simply the job.

The tools have quietly removed the struggle, and with it, the curriculum.
An engineer who starts today can ship a feature without ever reading the code the tool wrote, without ever opening a profiler, without ever needing to understand why the first version was slow, because the tool never produced a slow first version for them to fix.
The onboarding path that used to build the substrate model now bypasses it, and the [onboarding paradox in Software Engineering Teams in the Age of AI](/software-engineering-teams-in-the-age-of-ai) is the downstream symptom: juniors ship faster and understand less, and the understanding gap is invisible until something breaks.

So the question is not whether to teach low-level.
It is whether to teach it deliberately, because the accidental curriculum that used to teach it for free has been automated away.
**A generation that learns to prompt before it learns how a machine actually executes will be fluent at the surface and hollow at the substrate, and the hollowness will only become visible at the moment it becomes expensive, in production, at three in the morning, with no model able to help.**

## The Synthesis: Read the Substrate, Don't Write It

The resolution is not a midpoint between the two camps.
It is a different axis entirely.

Stop teaching new developers to produce low-level code as if they would ship it.
Manual memory management as a daily craft, pointer arithmetic as a drill, hand-rolled allocators as a rite of passage: these are depreciating production skills, and spending years on them is the [two-year test](/ai-maxxing-vs-fighting-against-it) failing in slow motion.
The surface area of low-level is large and mostly irrelevant to the work most developers will actually do, and Brooks's old split between [accidental and essential complexity](https://en.wikipedia.org/wiki/No_Silver_Bullet) still maps onto it cleanly: the syntax and the boilerplate are accidental, and the accident is exactly what the model now absorbs.

Do teach them to read the substrate.
Read a stack trace down to the frame that matters.
Read a flame graph and point at the function that is eating the budget.
Read a heap profile, an strace, a slow query log, a core dump.
Read the source of the standard library they use every day, at least once, until the abstraction stops being magic.
Reading is cheaper than writing, it transfers to every language and every model generation, and it builds exactly the four models above without demanding the years of production fluency the old curriculum required.

The rule of thumb is blunt and useful: **enough low-level to debug, not enough to ship.**
A few focused weeks of C or Rust, or even a careful tour through how the managed language you already use actually executes, is enough to install the models for a working lifetime, provided the engineer keeps reading systems instead of reading only diffs.
A career of writing C, in 2026, is overkill for most roles and a misallocation of the time that should be going into domain depth and judgment.

And for the small fraction of work that genuinely lives at the substrate, embedded, kernels, databases, runtimes, high-frequency paths, the calculus flips and fluency is still required.
The point is not that nobody should write low-level code.
The point is that "should every new developer learn to write low-level code" is the wrong question, asked about the wrong layer, and the answer, which is "no, but every developer should learn to read the machine," is what the two camps keep talking past.

## What to Do on Monday

If you hire or mentor new developers, stop using "do you know C" as a proxy for anything.
It measures syntax, and syntax is cheap.

Instead, hand them a deliberately broken program, one with a memory or concurrency bug hidden behind a clean high-level interface, and watch what they do.
The ones who can form a hypothesis about the layer underneath are the ones who can supervise a machine.
The ones who can only describe the symptom to the model and accept its first confident answer are the ones who will ship that bug to production and then be unable to explain it.

If you are a new developer yourself, do not let the tools talk you out of the substrate.
Generate the boilerplate, take the shortcut, and then, separately, on your own time, read the source of something you depend on until you can explain how it actually works.
The generation is free.
The understanding is not, and it is the only part of this profession that the next ten years will reward more, not less.

The debate between "learn everything low-level" and "writing code is dead" is two ways of staring at the surface.
**The surface is going away.
The substrate is not.
Prepare accordingly.**

## See also

- [The Shifting Bottleneck](/the-shifting-bottleneck) - why automating production moves the constraint to verification, the exact layer where substrate knowledge becomes load-bearing
- [AI-Maxxing and Resistance Are the Same Mistake](/ai-maxxing-vs-fighting-against-it) - the depreciating-versus-compounding two-year test this article applies to low-level skills, and the two-camps-one-error structure it borrows
- [Keeping Up With AI Is a Losing Strategy](/keeping-up-with-ai) - the durable-versus-ephemeral distinction that frames why mental models compound while syntax decays
- [Software Engineering Teams in the Age of AI](/software-engineering-teams-in-the-age-of-ai) - the onboarding paradox this article traces back to its root cause in the vanished struggle curriculum
- [Bringing Everyone to the Same Level](/bringing-everyone-to-the-same-level) - how skills encode the describable process but cannot encode the substrate judgment this article argues we still have to teach by hand

## References

- [Spolsky, "The Law of Leaky Abstractions"](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/) - the original framing for why every abstraction eventually fails at the layer underneath, which is where substrate knowledge pays
- [Wikipedia, "Theory of Constraints"](https://en.wikipedia.org/wiki/Theory_of_constraints) - the framework for why automating code production relocates rather than removes the bottleneck, landing it on verification
- [Wikipedia, "No Silver Bullet"](https://en.wikipedia.org/wiki/No_Silver_Bullet) - Brooks's split between accidental complexity (the syntax and boilerplate AI now handles) and essential complexity (the mental model of the problem it cannot)
- [Wikipedia, "Accidental complexity"](https://en.wikipedia.org/wiki/Accidental_complexity) - the distinction that lets you sort low-level trivia, which is accidental and depreciating, from low-level mental models, which are essential and compounding
- [Wikipedia, "Vibe coding"](https://en.wikipedia.org/wiki/Vibe_coding) - the extreme of the "writing code is over" posture, used here as the steelman argued against rather than a strawman
- [Willison, "Vibe coding"](https://simonwillison.net/2025/Mar/19/vibe-coding/) - a practitioner's account of what you can and cannot safely delegate, and why supervision still requires understanding the output
