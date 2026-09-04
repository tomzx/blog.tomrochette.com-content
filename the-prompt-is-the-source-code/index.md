---

title: "The Prompt Is the Source Code"
created: 2026-08-06
type: post
status: draft
tags: [ai, software-engineering, llm, code-quality, context-engineering, productivity, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is an engineer or tech lead who already uses LLM coding tools and has inherited code they did not write. Builds on "Who Maintains the Slop?" but can be read on its own.
agent_sessions:
  - ses_02af9e36affeF9AzX7wG0wZf1x
---

A year ago, the worst code you inherited still came with a person attached to it.
You could find them, ask why the strange loop was there, and get back some fragment of the reasoning that produced it.
That fallback is going away, faster than most teams have noticed.
**The code you will be asked to maintain next will, by default, carry no recoverable intent from whoever prompted it: no specification, no decision record, no saved conversation, and often no one who remembers being involved.**

The piece this follows, [Who Maintains the Slop?](../who-maintains-the-slop/index.md), described the handoff in which the prompter walks away with the reward and the maintainer is left with the cost.
That argument still assumed there was a prompter somewhere in the building to ask.
This one drops the assumption.
If you plan for a world where the code arrives with nobody and nothing attached to it, everything that matters about maintenance follows from that.

## The Intent Lives in the Prompt, Not the Code

Here is the reframe that makes the rest of this click.
For prompted code, the intent does not live in the code.
It lives in the prompt, the context that was fed in, and the conversation that produced it, and the code itself is the output.
That makes the code the compiled artifact, and the prompt the source.
We have spent decades insisting that source travel with the binary, on the grounds that a binary without its source is an orphan no one can responsibly maintain.
Then we built an entire generation of coding tools whose default is to keep the generated code and throw the prompt away.
**The prompt is the source code, and every team that commits the result without it is deleting its own source one merge at a time.**

## Ask the Author Is Dead

The maintainer's oldest fallback is about to fail, and for two reasons that compound.
For as long as software has been handed off, the escape hatch has been the same move: when the code is unclear, go find the person who wrote it.
The predecessor to this piece already named the first failure.
The prompter did not build a model of the implementation in their head, because they did not build the implementation, so they cannot walk you through it.
The second failure is newer, and it is worse.
Even the part the prompter does remember, the intent, was encoded in a prompt they no longer have, inside a tool whose history they did not save, and reconstructing it from memory would be guesswork.
You cannot ask the author, because the author's useful memory lived in a text box that got cleared the day the feature shipped.
**Once the prompt is gone, there is no one left who knows what the code was for, including the person whose name is on the commit.**

## Intent Collapse

There is a second force pushing the same direction, and it accelerates the loss.
Code no longer sits still between the prompter and the maintainer.
An agent writes the first version, then another agent edits it, then a third refactors it, and each of those passes reads the code, never the original prompt.
Intent degrades every time it is re-encoded through a layer that never saw it.
This is the human-side mirror of [model collapse in code](../model-collapse-in-code/index.md): there the weights lose signal as models train on models, here the purpose loses signal as agents maintain the output of other agents.
The difference is the speed.
Model collapse takes a full training cycle to show itself.
Intent collapse takes a single pull request.
The first prompt is the only place the real intent ever lived in full, and every generation after the first is a translation of a translation, each one a little more certain and a little less grounded in the reason the code exists.
**Left to run, intent collapse turns every codebase into a room full of confident answers to a question no one can remember asking.**

## The Maintainer's Job Becomes Decompilation

Strip the interview fallback away and the maintainer's job changes character.
You are no longer reading code someone else wrote and asking them about it.
You are reverse-engineering a binary back into the intent that produced it, with no symbols, no comments you can trust, and no original to compare against.
We already have a name for that work.
It is decompilation, and historically it has been some of the slowest, most expensive work in software, the thing you did only when there was no alternative, like recovering a lost system from its compiled output.
The premise of this piece is that those conditions are about to become the default rather than the exception.
Maintaining prompted code without the prompt is decompilation, and decompilation is what you reach for when something has gone badly wrong, except now it is just the Tuesday morning ticket queue.
**The cost we used to reserve for disasters is becoming the hourly rate of ordinary maintenance, and almost no one has priced it in.**

## What to Do

The fix is to stop treating the prompt as a means to an end and start treating it as the artifact.
A few concrete moves, each of which closes a gap the current default leaves open.

**Keep the source.**
The prompt, the context, and the transcript that produced a change get committed alongside the code, bound to the commit they generated.
If the change is worth merging, the conversation that produced it is worth keeping, because that conversation is the only record of intent the next maintainer will ever have.
No prompt, no merge is a sterner rule than it sounds, and it eliminates the worst cases outright, the drive-by generation that lands in a shared module with nothing but a diff behind it.

**Bind intent to the artifact, not the author.**
The reason to save the prompt is not nostalgia for who typed it.
It is that intent has to travel with the code, because the author will not.
This is the same argument [Defects Flow Downstream, Fixes Must Flow Upstream](../defects-flow-downstream/index.md) makes for specifications: the durable record has to be attached to the thing being maintained, not parked in a head that will move on.
A prompt bound to the commit survives the author leaving, the tool changing, and the chat history expiring.
One parked in a head survives none of those.

**Assume authorlessness when you read.**
Stop reaching for "ask the author" as a maintenance strategy.
Treat inherited code the way you treat a legacy system with no living expert: characterize what it does, pin the behavior with tests, and reconstruct intent from evidence rather than from an interview that will return nothing useful.
The comfort with opacity that [The Code You Will Never Read](../the-code-you-will-never-read/index.md) argues for is not a compromise in this setting.
It is the only mode that still works once the author is gone and the prompt with them.

**Write the prompt you wish you had inherited.**
Every time you prompt a change through, write the prompt as though the person reading it next knows nothing about your current head, because they will not.
State what the code is for, what it is not for, and where the hard choices were made.
If you cannot write that prompt, you do not understand the change well enough to merge it, and the merge should wait until you can.

## The Source Is the Source

The discipline we built around source code existed for a reason.
A binary without its source is an orphan, and maintaining orphans is the most expensive work there is, which is why we spent decades refusing to do it.
We are now producing prompted code as orphans by default, keeping the binary and discarding the source in the same gesture, and calling the result productivity because the code shipped fast.
The shipped-fast part is real.
The deleted-source part is the bill, and it comes due on someone else's Tuesday, in a currency the original author never had to spend.
**The code you will maintain tomorrow is void of intent because we threw the intent away at the moment of creation, and the fix is not to mourn it but to stop deleting it: keep the prompt, bind it to the commit, and treat the source as the source.**

## See also

- [Who Maintains the Slop?](../who-maintains-the-slop/index.md) - the direct predecessor; this piece hardens its assumption from "the prompter is useless when you ask" to "there is no prompter and no intent left to recover"
- [The Code You Will Never Read](../the-code-you-will-never-read/index.md) - the opacity of generated code; here the point is that the prompt, the one artifact more legible than the code, is the thing we discard
- [Model Collapse in Code](../model-collapse-in-code/index.md) - weights losing signal across training generations; intent collapse is the handoff-side analog, faster and about purpose rather than weights
- [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md) - context determines output at inference time; that same context is the artifact we must preserve, not consume and forget
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - effort belongs at the specification layer; keeping the prompt is the mechanism that makes that specification persist past the merge

## References

- [Wikipedia, "Source code"](https://en.wikipedia.org/wiki/Source_code) - the distinction that anchors the analogy: prompted code is the output, the prompt is the source we keep insisting must travel with it
- [Wikipedia, "Decompiler"](https://en.wikipedia.org/wiki/Decompiler) - the slow, expensive work of recovering intent from a compiled artifact, which is what maintenance becomes once the prompt is gone
- [Wikipedia, "Tacit knowledge"](https://en.wikipedia.org/wiki/Tacit_knowledge) - the knowledge that lived in heads and prompts and was never transferred, the thing the maintainer can no longer recover
- [Wikipedia, "Chinese whispers"](https://en.wikipedia.org/wiki/Chinese_whispers) - the loss of the original message across a chain of re-transmissions, the mechanism behind intent collapse
- [Wikipedia, "Provenance"](https://en.wikipedia.org/wiki/Provenance) - the record of an artifact's origin, which is exactly what a prompt bound to a commit provides and what its absence removes
