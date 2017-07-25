---
title: Computer science curricula 2013
created: 2017-07-15
taxonomy:
  category: [Computer Science]
  status: in progress
---

In the following document, I try to explain to the best of my knowledge various topics that are presented in the [Computer Science Curricula 2013](https://github.com/tomzx/computer-science-curricula-2013). I attempt to rate my understanding of the topic on a scale of 1 to 5, where 1 is "no understanding" and 5 is "perfect understanding". This value is displayed in bracket in front of each statement I make.

# Intelligent Systems
## Fundamental Issues
### What is intelligent behavior?
#### Rational versus non-rational reasoning
[2] Rational reasoning is when something can be explained by a sequence of finite explanations based on logic, one leading to the other, similar to a proof.

 [2] Non-rational reasoning is when something is explained through means such as probabilities.

### Nature of agents
#### Autonomous versus semi-autonomous
[4] Autonomous: An agent that makes decisions without the need of intervention from the part of another agent.

[3] Semi-autonomous: An agent that can make decisions by itself, but may also require the intervention of another agent in certain instances.

#### The importance of perception and environmental interactions
[3] Without perception, an agent cannot interact with its environment. Given an agent can be represented as a function, it would be similar to this function not receiving any argument (observation about the environment state). Agents that do not interact with the world are generally of little value (other than theoretical/experimental).

## Basic Search Strategies
### Problem spaces (states, goals and operators), problem solving by search
[4] A problem space is a graph that represent all the possible states that a problem can be into. An example of a state is a chess board configuration.

[3] A state is the representation of all the critical elements of the problem. In a problem, it is important to ignore the facts that are of no importance, such as the color of the cells of the chess board.

[2] In the problem graph, one can transition from one state to another through operators.

[3] Problem solving by search is the idea of constructing a graph and using the tools provided by graph search algorithms in order to solve a problem.

### Factored representation (factoring state into variables)
[1] I couldn't find anything relevant about factoring state into variables on the Internet.

### Heuristics and informed search (hill-climbing, generic best-first, A\*)
[2] Heuristics are "decisions" or strategies that help guide the behavior of a given algorithm.

[2] When using informed search algorithms, the hope is that we can reduce the amount of tests necessary to find a good solution by making use of the additional information.

### Two-player games (introduction to minimax search)
[2] In two-player games, the purpose of each player is to win. The best strategy, given that you expect your opponent to play optimally (as you would as well) is to pick the action that will maximize some gain. At the same time, you want to minimize the expected gain of your opponent.

### Constraint satisfaction (backtracking and local search methods)
[3] In problems which have constraint, one way to generate a solution is to construct the state tree, and whenever a constraint is violated, to "backtrack" (more back one step) and try an alternative action.

[2] Local search methods will generate an initial assignment, and given that assignment, will try to "correct" the constraint violations by applying legal operations to the state. As operations are performed, the "state pointer" moves from one state to an associated one. Unlike in backtracking, the chain of constraints that have been explored is not fixed.

## Basic Machine Learning
### Definition and examples of broad variety of machine learning tasks, including classification
[2] Regression is the task of determining the degree of association between variables.

[3] Classification is the task of determining to which class a set of observations belongs. Regression is generally used to separate classes in a one-vs-rest fashion.

[2] Examples of machine learning tasks are: generating speech given text, generating text given speech, creating a sentence to describe an image, generate music given a few parameters, extract text from an image, etc.

### Inductive learning
[4] Inductive learning is the process of learning from a set of examples. Given that we have no idea what the function that generated some outputs given inputs, the task of inductive learning is to construct such function using the examples it is given.

### Simple statistical-based learning, such as Naive Bayesian Classifier, decision trees
[1] A Naive Bayesian classifier <tbc></tbc>

[3] Decision trees make use of the features (and their frequency) to determine the most optimal way in which to ask questions about these features in order to better separate the different values it can output. In order to construct the tree, some metric is used to determine the "gain" that would be generated if a given decision were to be the node under consideration.

### Measuring classifier accuracy
[3] The measure of a classifier accuracy is the sum of all the correct classification divided by the number of examples given (incorrect + correct).

## Advanced Search
### Constructing search trees, dynamic search space, combinatorial explosion of search space
[1] Constructing search trees <tbc></tbc>

[1] Dynamic search space <tbc></tbc>

[3] One major issue in search is that given $n$ options, each level of the search tree grows is multiplied by $n$, thus making the number of states grow exponentially. This in turn means that problem of relatively small size can be tackled without too much problem, until a certain point at which they become impossible to deal with due to the shear amount of states that would have to be scanned.

### Stochastic search
#### Simulated annealing
[2] Simulated annealing uses the concept of temperature to stochastically try various state and evaluate them, probabilistically moving to an alternative state. As the temperature decreases, the probability of trying an alternative state than the currently best found decreases.

#### Genetic algorithms
[2] Genetic algorithms combines pairs of states to generate a new state by using both the operation of mutation and crossover. A mutation is a random change within the state while a crossover is the transfer of part of the state from a parent.

#### Monte-Carlo tree search
[2] Monte-Carlo tree search is the exploration of the search tree by randomly exploring the search tree most promising actions. Instead of constructing the whole tree (which may not be possible), the algorithm explores the most promising branches by simulating a possible traversal (from root to leaf). Given the result of this simulation, it is recorded as part of the branch being simulated, such that we have an idea of the potential (in term of probabilities) of each branches.
