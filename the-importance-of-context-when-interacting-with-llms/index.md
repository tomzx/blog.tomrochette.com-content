---
title: "The Importance of Context When Interacting with LLMs"
created: 2026-06-15
type: post
status: finished
tags: [ai, llm, context-engineering, prompt-engineering, rag, fully-ai-generated, llm=glm-5.1]
readability: 4
audience_notes: >
  Assumes familiarity with transformer-based LLMs, basic prompt engineering concepts, and production ML systems. No attempt to explain what an LLM is or how attention works at the architectural level.
---

Most interactions with LLMs fail not because the model lacks capability, but because the user failed to provide enough context for the model to succeed.
Context is not a prompt engineering trick.
**It is the entire mechanism by which a frozen set of weights produces behavior relevant to your specific situation.**

## What Context Means for an LLM

A large language model is a fixed function at inference time.
Its weights were determined during training and do not change.
Everything you want the model to know about your current task, your constraints, your codebase, your domain, and your preferences must be communicated through the context window.

This window has three conceptual regions.
1. The system prompt establishes persistent instructions and persona.
2. The conversation history provides the back-and-forth of the interaction.
3. The retrieved or injected context supplies external knowledge that the model was not trained on.

When people say "prompt engineering," they are usually talking about the system prompt and a handful of few-shot examples.
When people say "RAG," they are talking about dynamically injecting retrieved documents into the third region.
When people say "context engineering," they are talking about the deliberate design of all three regions together.

## In-Context Learning: Why This Works at All

The [GPT-3 paper](https://arxiv.org/abs/2005.14165) demonstrated something surprising: a sufficiently large language model can learn new tasks from examples provided in the prompt, without any gradient updates.
This is in-context learning, and it is the reason context matters so much.

A model that has never seen your internal API conventions can follow them perfectly if you show it three examples.
A model that does not know your company's style guide can adopt it verbatim if you paste it in.
The model is not truly "learning" in the statistical sense.
It is recognizing patterns in the provided context and extending them.

**This means the quality of the context is the quality of the output.**
Vague context produces vague output.
Contradictory context produces contradictory output.
Missing context produces plausible-sounding output that is wrong in ways specific to your situation.

## The Spectrum of Context Strategies

Context can be provided along a spectrum, from minimal to extensive.

**Zero-shot prompting** relies entirely on the model's pre-trained knowledge.
It works for generic tasks (summarize this text, translate this sentence) because the training data likely contained millions of similar examples.
It fails for domain-specific tasks (generate a query against our proprietary schema, review code against our internal standards) because the model has never seen your specific conventions.

**Few-shot prompting** injects examples into the context window.
The [original GPT-3 evaluation](https://arxiv.org/abs/2005.14165) showed that performance scales with the number of examples, but with diminishing returns.
Three to five high-quality examples often capture 80% of the benefit.
**The key insight: example quality matters more than example quantity.**
One example that perfectly demonstrates the desired behavior outperforms ten mediocre ones.

**Retrieval-augmented generation (RAG)** dynamically fetches relevant documents and injects them into the context.
The [original RAG paper](https://arxiv.org/abs/2005.11401) showed that combining a parametric model with non-parametric retrieval produces better grounded answers than either alone.
RAG addresses the fundamental limitation that a model's training data is a snapshot in time and cannot contain proprietary or recent information.

**Long-context ingestion** bypasses retrieval by stuffing everything into a large context window.
Models like Gemini with million-token contexts make this technically feasible.
The question is whether it is effective.
[Liu et al.](https://arxiv.org/abs/2307.03172) demonstrated that models suffer from a "lost in the middle" effect: information at the beginning and end of the context is retrieved more reliably than information in the middle.
**Simply increasing the window does not linearly increase the model's ability to use the information.**

**Context engineering** is the emerging discipline of orchestrating all of these strategies deliberately.
It recognizes that context is not just "what you put in the prompt," but a system that includes retrieval logic, example selection, conversation management, and information ordering.

## Where Context Breaks Down

Understanding the failure modes of context is as important as understanding how to provide it.

**Attention dilution.**
Every token in the context window competes for the model's finite attention.
Adding irrelevant context does not just waste tokens.
It actively degrades performance on the relevant portions.
[Liu et al.'s "Lost in the Middle"](https://arxiv.org/abs/2307.03172) showed that even when the relevant information is present in the context, retrieval accuracy drops when the context is cluttered with noise.
The lesson: more context is not always better.
**The right context, curated and ordered, outperforms a dump of everything that might be relevant.**

**Instruction following degrades at scale.**
System prompts and instructions are more reliably followed when they are prominent in the context.
As the context window fills with retrieved documents, conversation history, and examples, the model's adherence to its original instructions weakens.
This is why many production systems re-inject key instructions at the end of long contexts, not just the beginning.

**Stale context.**
In a long agent session, early conversation turns become increasingly irrelevant.
The model continues to weigh them in its attention computation.
This leads to drift, where the model brings up constraints or preferences from turn 3 that are no longer applicable at turn 30.
Effective agent systems summarize or prune earlier context to maintain relevance.

**Implicit context gaps.**
The most dangerous context failures are the ones you do not notice.
You assume the model knows that your API returns snake_case JSON, that your timestamps are in UTC, that your user IDs are integers not strings.
The model does not know these things unless you tell it.
Each implicit assumption is a potential bug in generated code or a hallucinated fact in generated text.

## Practical Context Design

**For engineers building with LLMs, context design is the highest-leverage activity.**
Here are concrete patterns that work.

**Layer your context deliberately.**
Start with a system prompt that defines the task, constraints, and output format.
Follow with retrieved documents that are directly relevant to the current query.
Then provide conversation history, pruned to the most recent and relevant turns.
End by restating the specific question or instruction.
This ordering respects the model's attention patterns, which weight the beginning and end of context most heavily.

**Curate your examples.**
A few-shot example should demonstrate the hardest case, not the easiest.
If your task involves edge cases (empty inputs, special characters, ambiguous queries), show examples of those.
Showing five variations of the happy path teaches the model less than one example of each difficult variant.

**Use structured context.**
When injecting retrieved information, format it consistently.
Markdown headers, delimited sections, and numbered lists give the model explicit boundaries between pieces of information.
A blob of unstructured text forces the model to spend attention on parsing structure rather than reasoning about content.

**Separate context from instruction.**
Mixing "here is some reference information" with "now do this task" in the same unstructured block reduces reliability.
Explicitly mark where context ends and instructions begin.
Many production systems use XML tags or special tokens for this purpose.

**Test your context independently.**
Before deploying an LLM pipeline, test whether the model can answer simple factual questions based solely on the provided context.
If it cannot reliably retrieve a fact that is clearly present in the context, the context is too long, too noisy, or poorly structured.
This is a fast diagnostic that catches many context problems before they become production incidents.

## Context Engineering as a Discipline

The shift from "prompt engineering" to "context engineering" reflects a maturation in how we think about LLM interactions.
Prompt engineering suggests that the right magic words unlock better performance.
**Context engineering recognizes that the entire information environment determines the output.**

This distinction matters because it changes where you invest effort.
If you believe in magic prompts, you spend your time iterating on wording.
If you believe in context engineering, you invest in retrieval systems, example libraries, context ordering, and information architecture.

The results from [Anthropic's work on contextual retrieval](https://www.anthropic.com/research/contextual-retrieval) illustrate this well.
By adding a small amount of context to each retrieved chunk (explaining how it relates to the broader document), they reduced retrieval failure rates by 67%.
Not by changing the model.
Not by changing the prompt.
By changing how context was prepared and presented.

[Chain-of-thought prompting](https://arxiv.org/abs/2201.11903) is another example.
The model's reasoning improves not because you asked it to "think step by step" as a magic incantation, but because you expanded the context window with intermediate reasoning steps.
The model uses its own generated context as additional input for subsequent tokens.
Context is not just what you provide.
It is also what the model generates and then consumes.

## The Uncomfortable Implication

**If context determines output quality, then the ceiling on LLM performance in production is not the model's capability.**
**It is the quality of the context pipeline feeding it.**

This is uncomfortable because it means the hardest engineering problem in LLM applications is not model selection or fine-tuning.
It is information retrieval, information architecture, and information presentation.
These are old problems from search engineering and information science, now applied to a new interface.

The engineers who build the best LLM products will not necessarily be the ones who understand transformer architectures most deeply.
They will be the ones who can design systems that surface the right information, at the right time, in the right format, and place it where the model will actually attend to it.

**Context is not a feature you add to an LLM application.**
**It is the application.**

## References

- [Brown et al., "Language Models are Few-Shot Learners"](https://arxiv.org/abs/2005.14165) -- established in-context learning as a core capability of large language models
- [Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"](https://arxiv.org/abs/2005.11401) -- introduced RAG as a method for grounding LLM outputs in retrieved documents
- [Liu et al., "Lost in the Middle: How Language Models Use Long Contexts"](https://arxiv.org/abs/2307.03172) -- demonstrated positional bias in how models attend to long contexts
- [Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"](https://arxiv.org/abs/2201.11903) -- showed that intermediate reasoning steps in context improve model performance
- [Anthropic, "Contextual Retrieval"](https://www.anthropic.com/research/contextual-retrieval) -- demonstrated that context preparation significantly reduces retrieval failure rates
