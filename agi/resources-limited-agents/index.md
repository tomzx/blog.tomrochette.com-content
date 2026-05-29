---
title: Resources limited agents
created: 2016-06-23
tags: [artificial-general-intelligence, partially-ai-generated, llm=glm-5.1]
status: in progress
readability: 3
---

## Context

## Learned in this study

## Things to explore

- How do biological systems (human brain, ant colonies) solve resource limitation problems?
- What is the relationship between resource limits and the emergence of abstraction?
- Can resource constraints actually produce more robust/intelligent behavior than unlimited resources?
- How should an agent decide between acquiring new knowledge vs refining existing knowledge?
- What is the optimal forgetting schedule for different types of knowledge?

# Overview

## What are the impacts of limited computational time and memory space?

Limitations of time and space due to the available resources implies that an agent will need to develop methods to make the most effective use of those two resources [^simon1956].
Furthermore, he may be able to exchange time for space and vice-versa.

A space limited agent may have no choice other than to drop existing knowledge to have some space available in order to do its current computation.
The way existing knowledge may be dropped will depend on the strategy used by the agent and can be referred as knowledge prioritization.
Short term may be prioritized over long term (or the opposite).
A current computation may decide to abort due to resource exhaustion instead of dropping existing knowledge (knowledge preservation).

A time limited agent may need to make use of more rough/imprecise methods in order to rapidly provide a result.

## Resource dimensions

Time and space are the two fundamental computational resources, but several other dimensions constrain an agent in practice [^gershman2015]:

- **Energy/power**: Computation has a physical cost.
An agent operating on a battery or in a thermally constrained environment must account for energy consumption per operation.
This creates a third trade-off axis where an agent may choose less energy-intensive algorithms at the cost of accuracy or completeness.
- **Communication bandwidth**: When an agent is distributed or needs to interact with other agents or external systems, the volume and frequency of information exchange becomes a bottleneck.
An agent may need to compress, summarize, or prioritize which observations to transmit.
- **Attention**: Related to but distinct from time, attention refers to the number of concurrent processes or inputs an agent can monitor.
Even with abundant time, an agent may only track a limited number of streams simultaneously, requiring selective attention mechanisms.

## Time-limited strategies

### Anytime algorithms and progressive refinement

An anytime algorithm is designed to produce a result of improving quality the longer it runs [^dean1988] [^zilberstein1996].
When time is limited, the agent can interrupt the computation at any point and return the best answer found so far.
This is a natural fit for agents that operate under deadlines or in real-time environments.

Progressive refinement extends this idea: the agent first produces a coarse answer quickly, then iteratively refines it if time permits.
The agent can decide whether to refine further or act on the current estimate based on the urgency of the situation and the marginal improvement expected.

### Approximation and heuristic substitution

When exact computation is too expensive, the agent can substitute cheaper approximations.
This includes:

- Using lookup tables or cached results from similar past situations (case-based reasoning).
- Replacing expensive functions with learned surrogate models that are faster to evaluate.
- Applying heuristics or rules of thumb that work well enough in common cases, even if they fail in edge cases.

The risk is that approximation introduces systematic biases.
An agent must learn when its approximations are reliable and when it needs to fall back to more expensive exact methods.

### Bounded rationality and satisficing

Herbert Simon's concept of bounded rationality suggests that agents do not optimize, they satisfice: they search for a solution that is "good enough" given their computational constraints [^simon1955].
A resource-limited agent explicitly models its own computation cost as part of the decision problem, asking not just "what is the best action?" but "what is the best action given that I have only X time to decide?" [^russell1991].

This meta-level reasoning about computation cost is itself expensive, so the agent faces a recursive problem: how much time should it spend deciding how much time to spend deciding?
Practical solutions involve fixed or learned budgets for deliberation.

## Space-limited strategies

### Knowledge prioritization and forgetting

When memory is scarce, the agent must decide what to keep and what to discard.
Several strategies exist:

- **Recency-based**: Drop the oldest knowledge first, assuming recent experience is more relevant.
This is a FIFO approach to memory.
- **Frequency-based**: Retain knowledge that has been accessed or used most often, on the assumption that frequently useful knowledge will continue to be useful.
- **Importance-weighted**: Assign an importance score to each piece of knowledge based on predicted future utility.
This is the most powerful but also the most computationally expensive strategy, as it requires predicting future needs.
- **Surprise/novelty-based**: Prioritize retaining knowledge that was surprising or contradicted expectations [^itti2009], as this may indicate areas where the agent's model is weakest and most in need of correction.

These strategies can be combined.
For instance, an agent might weight importance by recency decay, keeping both important and recent items while discarding items that are neither.

Naively overwriting old knowledge with new knowledge can lead to catastrophic interference, where learning new information destroys previously learned knowledge [^mccloskey1989].
Strategies such as elastic weight consolidation can mitigate this by protecting parameters deemed important for previously learned tasks [^kirkpatrick2017].

### Compression and abstraction

Instead of discarding knowledge, the agent can compress it.
Raw experiences can be summarized into general rules or patterns.
This trades space for accuracy: the compressed representation takes less memory but loses detail.

Abstraction is a form of compression where the agent identifies commonalities across experiences and stores the shared structure rather than each instance.
For example, instead of remembering every instance of opening a door, the agent stores a general "door opening" schema.

Hierarchical compression allows the agent to maintain detail at different levels: high-level summaries in easily accessible memory, with pointers to compressed details that are more expensive to retrieve or reconstruct.

### Externalization and offloading

An agent can extend its effective memory by storing knowledge externally: in the environment (writing notes, arranging objects as reminders), in other agents (delegating memory to trusted collaborators), or in persistent external storage.
The trade-off is that accessing externalized knowledge is slower and may not always be available.

This is how humans operate: we do not memorize all facts, we learn where to find them.
A resource-limited agent benefits from learning retrieval strategies (how to find information) over storage strategies (memorizing everything).

## Energy-limited strategies

Energy constraints arise when an agent operates on a finite power source (battery, solar, thermal budget) or when the cost of computation is non-trivial relative to available energy.
Unlike time, energy is often consumed irreversibly: once spent on a computation, it cannot be recovered.

### Computational frugality

An energy-limited agent must weigh the expected value of each computation against its energy cost.
Low-energy operations (lookup, comparison, threshold-based decisions) should be preferred over high-energy operations (large matrix multiplication, exhaustive search, complex simulation).
The agent can structure its processing pipeline as a cascade of increasingly expensive filters: cheap filters first to eliminate obvious candidates, expensive analysis only on what survives.

### Selective activation

Not all subsystems need to be active at all times.
An energy-limited agent can keep most of its processing in a low-power idle state and activate only the subsystems relevant to the current situation.
This requires a lightweight always-on monitor that detects when a situation warrants deeper processing.
The monitor itself must be extremely cheap to run, otherwise it defeats the purpose.

### Energy-aware scheduling

When multiple tasks compete for limited energy, the agent must schedule them to maximize total utility.
Some tasks have deadlines (respond to a threat before it strikes), while others can be deferred (update a model during idle time).
An energy-aware scheduler considers both the urgency of each task and its energy cost, preferring to batch low-priority work during periods of energy surplus.

### Energy harvesting awareness

In some environments, energy can be replenished (solar charging, docking stations, periods of low activity).
An energy-limited agent can plan around energy availability, scheduling energy-intensive computations for times when energy is abundant and conserving during scarcity.
This introduces a temporal planning dimension: the agent must predict when energy will be available and allocate its computational budget accordingly.

## Communication-limited strategies

Communication bandwidth becomes a bottleneck whenever an agent must exchange information with other agents, external systems, or remote storage.
The constraint may be throughput (limited bits per second), latency (delayed responses), or cost (each message has a price).

### Message compression and summarization

Raw observations can be large and redundant.
Before transmitting, the agent can compress information by extracting only the relevant features or summarizing a sequence of observations into a compact representation.
Lossy compression trades fidelity for bandwidth: the recipient receives an approximation rather than the full detail.
The sender must decide what level of fidelity is sufficient for the recipient's needs.

### Selective reporting

Not all observations are worth communicating.
An agent can filter what it transmits based on relevance, novelty, or expected impact on the recipient.
For example, an agent monitoring a stable system only needs to communicate when something changes, not when everything is normal (event-driven communication).
This reduces bandwidth usage to a fraction of what continuous reporting would require.

### Protocol efficiency

The design of the communication protocol itself affects bandwidth usage.
Fixed-width messages waste space when the content is small.
Verbose encoding (JSON, XML) is human-readable but bandwidth-expensive.
Compact binary encodings or domain-specific protocols can dramatically reduce message size at the cost of generality.
An agent operating under severe bandwidth constraints benefits from learning or evolving a shared codebook with its communication partners, where frequent messages are assigned short codes.

### Predictive pre-filtering

When communication is expensive, the agent can predict what information the recipient already has or can infer, and only transmit the delta.
If two agents share a common model of the world, one agent only needs to communicate the aspects that differ from the shared expectation.
This requires maintaining a model of what the other agent knows (theory of mind), which itself consumes resources but can yield large communication savings.

### Asynchronous batching

When latency is tolerable, an agent can accumulate messages and transmit them in batches rather than individually.
Batching amortizes the fixed overhead of each communication round (connection setup, headers, acknowledgment) across multiple messages.
The trade-off is increased latency for individual messages, which may not be acceptable for time-critical communications.

## Attention-limited strategies

Attention limits the number of concurrent inputs, processes, or goals an agent can actively monitor and reason about.
Even with abundant time and memory, an agent may only have a fixed number of attention slots.

### Priority-based attention allocation

When attention slots are scarce, the agent must allocate them to the inputs or processes with the highest expected value.
This requires a continuous ranking of all candidate attention targets by importance.
Importance can be derived from factors like urgency (a looming deadline), relevance (proximity to current goals), novelty (unexpected observations), or risk (potential threats).
The agent periodically reassesses its allocation as conditions change.

### Habituation and change detection

An efficient attention mechanism does not waste slots monitoring stable, predictable inputs.
Habituation is the process of reducing attention to stimuli that remain constant over time.
The agent redirects freed attention slots to novel or changing inputs.
This mirrors biological attention systems, which are strongly tuned to detect changes rather than steady states.

### Attention cascading

Complex attention tasks can be decomposed into a hierarchy: a broad, cheap attention pass that identifies regions of interest, followed by focused, expensive attention on the most promising regions.
For example, an agent scanning a scene might first run a coarse detector over the entire input, then devote detailed processing only to regions flagged as potentially relevant.
This reduces the number of attention slots needed at the expensive level.

### Context-dependent attention switching

The optimal attention strategy depends on the current context.
During a crisis, the agent should narrow its attention to threat-related inputs.
During exploration, it should broaden attention to detect novel opportunities.
An agent that can dynamically adjust its attention width based on situational demands makes better use of its limited attention budget than one with a fixed allocation strategy.

### Goal-driven filtering

Attention can be guided top-down by the agent's current goals.
Rather than attending to all available inputs equally, the agent selects inputs likely to be relevant to its active goals.
This is efficient when the agent has clear goals, but risks missing important information outside the current goal scope.
A robust agent balances goal-driven attention with a background process that monitors for unexpected but important events.

## Time-space tradeoffs

The classic computer science insight that time and space can often be exchanged applies to agents:

- **Memoization/caching**: Spend more space to save time by storing computed results for reuse.
An agent with abundant memory can cache the results of expensive deliberations, avoiding recomputation when similar situations arise.
- **Recomputation**: Spend more time to save space by discarding stored results and recomputing them when needed.
An agent with abundant time but limited memory can derive facts on demand rather than storing them.
- **Indexing**: Build auxiliary data structures (indexes) that use space but dramatically speed up retrieval.
The agent must decide which access patterns are worth indexing for.

The optimal tradeoff depends on the relative scarcity of each resource and the distribution of future queries.
An agent that frequently encounters similar situations benefits more from caching.
An agent facing novel situations benefits from keeping memory free for new observations.

## Resource-aware meta-reasoning

A sophisticated resource-limited agent needs to reason about its own resource usage [^horvitz1988].
This meta-reasoning involves:

- **Resource monitoring**: Tracking current resource consumption and predicting future needs based on the current task and environment.
- **Strategy selection**: Choosing between multiple available problem-solving strategies based on the resources currently available [^hay2012].
For example, selecting between a fast heuristic and a slow deliberative approach.
- **Budget allocation**: Dividing a finite resource budget across subproblems, allocating more resources to subproblems where additional computation is likely to yield the most improvement.
- **Interruption and switching**: Deciding when to abandon a current line of reasoning that is consuming too many resources and switch to a cheaper alternative.

Meta-reasoning itself consumes resources, creating the danger of infinite regress.
Practical agents use fixed or learned meta-strategies that are cheap to execute.

## Resource constraints as a driver of intelligence

An intriguing possibility is that resource constraints do not merely limit intelligence but actively shape and improve it [^lieder2020].
When an agent cannot afford to process everything or remember everything, it is forced to:

- Identify patterns and regularities (generalization).
- Focus on what matters most (attention and prioritization).
- Develop efficient representations (abstraction).
- Make decisions under uncertainty (heuristics and approximation).

These are precisely the hallmarks of intelligent behavior.
An agent with unlimited resources might simply store all experiences and brute-force all computations, never needing to develop the abstractions and heuristics that constitute understanding.
Resource constraints may be not just a practical limitation but a necessary condition for the emergence of intelligence.

## Resource-limited multi-agent systems

When multiple resource-limited agents collaborate, new dynamics emerge:

- **Specialization**: Agents can divide labor, with each agent developing deep expertise in a narrow area rather than shallow knowledge across all areas.
This is more memory-efficient for the group but creates dependencies.
- **Knowledge sharing**: Agents can query each other instead of each maintaining complete knowledge.
This requires communication protocols and trust mechanisms.
- **Resource pooling**: Agents can share computational resources, with less busy agents taking on work from overloaded agents.
- **Collective memory**: The group can maintain distributed knowledge that no single agent could store, with each agent holding a partial but overlapping subset.

The challenge is coordination overhead: the communication and negotiation required to coordinate multiple agents itself consumes resources, and poorly designed coordination can consume more resources than it saves.

## Implications for AGI design

For artificial general intelligence, resource limitation is not a temporary engineering problem to be solved with better hardware [^russell1995].
It is a fundamental characteristic of any agent that must operate in a complex, open-ended world:

- The world contains far more information than any finite agent can store.
- Decisions often need to be made in real-time, with strict time constraints.
- The space of possible actions and outcomes is too large for exhaustive search.

An AGI architecture must therefore bake in resource-awareness at every level: perception (what to attend to), memory (what to store and retrieve), reasoning (how deeply to deliberate), and action (when to act on imperfect information).
Systems that assume unlimited resources will fail when deployed in the real world.

# See also

- [Compression](../compression/index.md)
- [Memory](../memory/index.md)
- [Intelligence](../intelligence/index.md)

# References

## Bounded rationality and satisficing

[^simon1955]: Simon, H. A. (1955). [A behavioral model of rational choice](https://www.semanticscholar.org/paper/d8237600841361f7811f5fd9effaed9d2e6e34b0). *Quarterly Journal of Economics*.
[^simon1956]: Simon, H. A. (1956). [Rational choice and the structure of the environment](https://www.semanticscholar.org/paper/23a94ce42fe0d50f5c993f34d4c9602f8aeac507). *Psychological Review*.
[^russell1991]: Russell, S., & Wefald, E. (1991). [Do the Right Thing: Studies in Limited Rationality](https://mitpress.mit.edu/9780262681129/). MIT Press.
[^russell1995]: Russell, S., & Subramanian, D. (1995). [Provably bounded-optimal agents](https://doi.org/10.1613/jair.532). *Journal of AI Research*.

## Anytime algorithms and time-limited reasoning

[^dean1988]: Dean, T., & Boddy, M. (1988). [An analysis of time-dependent planning](https://www.semanticscholar.org/paper/143f6b100c13d120e55c3e30e441c4abac7a5db2). *AAAI*.
[^zilberstein1996]: Zilberstein, S. (1996). [Using anytime algorithms in intelligent systems](https://www.semanticscholar.org/paper/ecf9adafc610cd417be2aa4092e809446e0f361f). *AI Magazine*.

## Meta-reasoning and resource-aware computation

[^horvitz1988]: Horvitz, E. J. (1988). [Reasoning about beliefs and actions under computational resource constraints](https://www.semanticscholar.org/paper/da6231ac3da628e748d407c3842bc06b32433ab6). *Uncertainty in AI*.
[^hay2012]: Hay, N., Russell, S., Tolpin, D., & Shimony, S. E. (2012). [Selecting computations: Theory and applications](https://doi.org/10.48550/arXiv.1207.1388). *UAI*.
[^schmidhuber2002]: Schmidhuber, J. (2002). [The Speed Prior: A new simplicity measure yielding near-optimal computable predictions](https://doi.org/10.1007/3-540-45435-3_13). *COLT*.

## Memory and forgetting

[^mccloskey1989]: McCloskey, M., & Cohen, N. J. (1989). [Catastrophic interference in connectionist networks: The sequential learning problem](https://doi.org/10.1016/S0079-7421(89)80010-2). *Psychology of Learning and Motivation*.
[^kirkpatrick2017]: Kirkpatrick, J., et al. (2017). [Overcoming catastrophic forgetting in neural networks](https://www.semanticscholar.org/paper/2e55ba6c97ce5eb55abd959909403fe8da7e9fe9). *PNAS*.

## Attention and surprise

[^itti2009]: Itti, L., & Baldi, P. (2009). [Bayesian surprise attracts human attention](https://www.semanticscholar.org/paper/aebd8bab5cff769fed204dba35112e364a47e504). *Vision Research*.

## Computational rationality and resource constraints as drivers of intelligence

[^gershman2015]: Gershman, S. J., Horvitz, E. J., & Tenenbaum, J. B. (2015). [Computational rationality: A converging paradigm for intelligence in brains, minds, and machines](https://www.semanticscholar.org/paper/afbb25c4346f9a9b75ba5cb751d47845a4a5b584). *Science*.
[^lieder2020]: Lieder, F., & Griffiths, T. L. (2020). [Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources](https://doi.org/10.1017/S0140525X19000674). *Behavioral and Brain Sciences*.
