---
title: Reinforcement learning
created: 2017-02-04
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview
* Environment: A program with a state, which upon receiving input from an agent, runs its program and emits a response (observation) and may update its state
* The environment's program and state is generally smaller than what it can generate, which becomes what the agent can observe. In turn, the job of the agent is to attempt to reconstruct both program and state in order to map from the observable environment the current state of the program, such that the agent may be able to predict exactly how his actions will impact the environment in return. In the perfect case where the agent knows its state and the impact of its actions on the environment, it can thus control the next state such that it is the state desired by the agent

* A state $S_t$ is Markov if and only if
$$
\mathbb{P}[S_{t+1}\ |\ S_t] = \mathbb{P}[S_{t+1}\ |\ S_1, \dots, S_t]
$$
* Markov property: The future is independent of the past given the present
$$
H_{1:t} \rightarrow S_t \rightarrow H_{t+1:\infty}
$$
* The environment state $S_t^e$ is Markov
* The history $H_t$ is Markov

## Components of a reinforcement learning agent
* Policy: agent's behavior function
	* A map from state to action
	* Deterministic policy: $a = \pi(s)$
	* Stochastic policy: $\pi(a\ |\ s) = \mathbb{P}[A = a\ |\ S = s]$
* Value function: how good is each state and/or action
	* Used to evaluate the goodness/badness of states
	* $v_{\pi}(s) = \mathbb{E}_{\pi}[R_t + \gamma R_{t+1} + \gamma ^2 R_{t+2} + \dots\ |\ S_t = s ]$
* Model: agent's representation of the environment
	* Transitions model: $\mathcal{P}$ predicts the next state
		* $\mathcal{P}_{ss'}^a = \mathbb{P}[S' = s'\ |\ S = s, A = a]$
	* Rewards model: $\mathcal{R}$ predicts the next (immediate) reward
		* $\mathcal{R}_{s}^a = \mathbb{E}[R\ |\ S = s, A = a]$

## RL agents categories
* Value based
	* Value function
	* No policy (implicit)
* Policy based
	* Policy
	* No value function
* Actor critic
	* Policy
	* Value function
* Model free
	* Policy and/or value function
	* No model
* Model based
	* Policy and/or value function
	* Model

# Markov Process
* A Markov Process (or Markov Chain) is a tuple $\langle\mathcal{S}, \mathcal{P}\rangle$
	* $\mathcal{S}$ is a (finite) set of states
	* $\mathcal{P}$ is a transition probability matrix
		* $\mathcal{P}_{ss'} = \mathbb{P}[S_{t+1} = s'\ |\ S_t = s]$

# Markov Reward Process
* A Markov Reward Process is a tuple $\langle\mathcal{S}, \mathcal{P}, \mathcal{R}, \gamma\rangle$
	* $\mathcal{S}$ is a (finite) set of states
	* $\mathcal{P}$ is a transition probability matrix
		* $\mathcal{P}_{ss'} = \mathbb{P}[S_{t+1} = s'\ |\ S_t = s]$
	* $\mathcal{R}$ is a reward function, $\mathcal{R}_s = \mathbb{E}[R_{t+1}\ |\ S_t = s]$
	* $\gamma$ is a discount factor, $\gamma \in [0, 1]$
* The return $G_t$ is the total discounted reward from time-step t
$$
G_t = R_{t+1} + \gamma R_{t+2} + \dots = \sum_{k=0}^\infty \gamma^k R_{t+k+1}
$$

# Value Function
* The value function $v(s)$ gives the long term value of state s
* The state value function $v(s)$ of an MRP is the expected return starting from state s
$$
v(s) = \mathbb{E}[G_t\ |\ S_t = s]
$$
* The Bellman equation
$$
\begin{split}
v &= \mathcal{R} + \gamma \mathcal{P}v \\
(I - \gamma \mathcal{P}) &= \mathcal{R} \\
v &= (I - \gamma \mathcal{P})^{-1}\mathcal{R}
\end{split}
$$

# Markov Decision Process
* A Markov Decision Process is a tuple $\langle\mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma\rangle$
	* $\mathcal{S}$ is a finite set of states
	* $\mathcal{A}$ is a finite set of actions
	* $\mathcal{P}$ is a transition probability matrix
		* $\mathcal{P}_{ss'}^a = \mathbb{P}[S_{t+1} = s'\ |\ S_t = s, A_t = a]$
	* $\mathcal{R}$ is a reward function, $\mathcal{R}_s^a = \mathbb{E}[R_{t+1}\ |\ S_t = s]$
	* $\gamma$ is a discount factor, $\gamma \in [0, 1]$
* A policy $\pi$ is a distribution over actions given states
$$
\pi(a\ |\ s) = \mathbb{P}[A_t = a\ |\ S_t = s]
$$
* Policies are stationary (time-independent)
* The state-value function $v_\pi(s)$ of an MDP is the expected return starting from state s, and then following policy $\pi$
$$
v_\pi(s) = \mathbb{E}_\pi[G_t\ |\ S_t = s]
$$
* The action-value function $q_\pi(s, a)$ is the expected return starting from state s
$$
q_\pi(s, a) = \mathbb{E}_\pi[G_t\ |\ S_t = s, A_t = a]
$$

# Optimal Value Function
* The optimal state-value function $v_*(s)$ is the maximum value function over all policies
$$
v_*(s) = \max_\pi v_\pi(s)
$$
* The optimal action-value function $q_*(s, a)$ is the maximum action-value function over all policies
$$
q_*(s, a) = \max_\pi q_\pi(s, a)
$$

# Optimal Policy
* Define a partial ordering over policies
$$
\pi \ge \pi'\ \text{if}\ v_\pi(s) \ge v_{\pi'}(s), \forall s
$$
* For any Markov Decision Process
	* There exists an optimal policy $\pi_*$ that is better than or equal to all other policies, $\pi_* \ge \pi, \forall \pi$
	* All optimal policies achieve the optimal value function, $v_{\pi_*}(s) = v_*(s)$
	* All optimal policies achieve the optimal action-value function, $q_{\pi_*}(s, a) = q_*(s, a)$
* An optimal policy can be found by maximizing over $q_*(s, a)$,
$$
\pi_*(a\ |\ s) =
\begin{cases}
1 & \text{if } a = \operatorname*{arg\,max}_{a \in \mathcal{A}} q_*(s, a) \\
0 & \text{otherwise}
\end{cases}
$$

# 4 Model-Free Prediction
## Monte-Carlo Reinforcement Learning
* Learns directly from episodes of experience
* Uses the simplest possible idea: value = mean return
* Caveat: can only apply MC to episodic MDPs (episodes must terminate)
* MC policy evaluation uses empirical mean return instead of expected return

# See also

# References
* http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html