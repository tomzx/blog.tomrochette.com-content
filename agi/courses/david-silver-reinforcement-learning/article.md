---
title: David Silver - Reinforcement learning (2015)
created: 2017-02-04
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* Is it possible to determine the contribution of individual contributors to a project using something like the eligibility traces?

# Overview

# Lecture 1 - Introduction to Reinforcement Learning
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

# Lecture 2 - Markov Decision Processes
## Markov Process
* A Markov Process (or Markov Chain) is a tuple $\langle\mathcal{S}, \mathcal{P}\rangle$
	* $\mathcal{S}$ is a (finite) set of states
	* $\mathcal{P}$ is a transition probability matrix
		* $\mathcal{P}_{ss'} = \mathbb{P}[S_{t+1} = s'\ |\ S_t = s]$

## Markov Reward Process
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

## Value Function
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

## Markov Decision Process
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

## Optimal Value Function
* The optimal state-value function $v_*(s)$ is the maximum value function over all policies
$$
v_*(s) = \max_\pi v_\pi(s)
$$
* The optimal action-value function $q_*(s, a)$ is the maximum action-value function over all policies
$$
q_*(s, a) = \max_\pi q_\pi(s, a)
$$

## Optimal Policy
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

# Lecture 4 - Model-Free Prediction
## Monte-Carlo Reinforcement Learning
* Learns directly from episodes of experience
* Uses the simplest possible idea: value = mean return
* Caveat: can only apply MC to episodic MDPs (episodes must terminate)
* MC policy evaluation uses empirical mean return instead of expected return
* Two dimensions
	* Bootstraping: DP/TD
	* Sampling: MC/TD
* n-Step Return
$$
G_t^{(n)} = R_{t+1} + \gamma R_{t+2} + \dots + \gamma^{n-1} R_{t+n} + \gamma^n V(S_{t+n})
$$
* $\text{TD}(\lambda)$, averaging n-Step Returns using a decay value $\lambda$
$$
G_t^\lambda = (1 - \lambda)\sum_{n=1}^\infty \lambda^{n-1} G_t^{(n)}
$$
* Geometric decaying, why?
	* Memoryless (does not necessitate storage)
* Eligibility traces
	* Frequency heuristic: assign credit to most frequent states
	* Recency heuristic: assign credit to most recent states
	* Combines both heuristics

# Lecture 5 - Model-Free Control
* On-policy learning
	* "Learn on the job"
* Off-policy learning
	* "Look over someone's shoulder"
* $\epsilon$-Greedy Exploration
	* With probability $1 - \epsilon$, choose the greedy action
	* With probability $\epsilon$, choose an action at random
* For any $\epsilon$-greedy policy $\pi$, the $\epsilon$-greedy policy $\pi'$ with respect to $q_\pi$ is an improvement, $v_{\pi'} \ge v_\pi(s)$
* Greedy in the Limit with Infinite Exploration (GLIE)
	* All state-action pairs are explored infinitely many times,
$$
\lim_{k \rightarrow \infty} N_k(s, a) = \infty
$$
	* The policy converges on a greedy policy,
$$
\lim_{k \rightarrow \infty} \pi_k(a\ |\ s) = \boldsymbol{1}(a = \operatorname*{arg\,max}_{a' \in \mathcal{A}} Q_k(s, a'))
$$
* For example, $\epsilon$-greedy is GLIE if $\epsilon$ reduces to zero at $\epsilon_k = \frac{1}{k}$
* SARSA
$$
Q(S, A) \leftarrow Q(S, A) + \alpha(R + \gamma Q(S', A') - Q(S, A))
$$
* Monte-Carlo learning is a really bad idea off-policy, it does not work because over many steps, your target policy and your behavior policy never match enough to be useful

# Lecture 6 - Value Function Approximation
* DQN uses experience replay and fixed Q-targets
	* Take action $a_t$ according to $\epsilon$-greedy policy
	* Store transition $(s_t, a_t, r_{t+1}, s_{t+1})$ in replay memory $\mathcal{D}$
	* Sample random mini-batch of transition (s, a, r, s') from $\mathcal{D}$
	* Compute Q-learning targets with respect to fixed parameters $w^-$
	* Optimize MSE between Q-network and Q-learning targets
$$
\mathcal{L}_i(w_i) = \mathbb{E}_{s, a, r, s' \sim \mathcal{D}_i} \left[\left(r + \gamma \operatorname*{max}_{a'} Q(s', a'; w_i^-) - Q(s, a; w_i)\right)^2\right]
$$

# Lecture 7 - Policy Gradient
* Advantage of policy-based RL
	* Better convergence properties
	* Effective in high-dimensional or continuous action spaces
	* Can learn stochastic policies
* Disadvantages
	* Typically converge to a local rather than global optimum
	* Evaluating a policy is typically inefficient and high variance
* Whenever state aliasing occurs a stochastic policy can do better than a deterministic policy
* For any differentiable policy $\pi_\theta(s, a)$, for any of the policy objective functions $J = J_1$, $J_{avR}$, or $\frac{1}{1-\gamma}J_{aaV}$, the policy gradient is
$$
\underbrace{\nabla_\theta J(\theta)}_{policy\ gradient} = \underbrace{\mathbb{E_{\pi_\theta}}[\underbrace{\nabla_\theta \log \pi_\theta(s, a)}_{score\ function}\underbrace{Q^{\pi_\theta}(s, a)}_{action-value\ function}]}_{expectation\ under\ policy\ \pi_\theta}
$$
* Monte-Carlo Policy Gradient methods are slow because they require many iterations to get to a final solution
* Actor-Critic algorithm:
	* Critic: Updates action-value function parameters $w$
	* Actor: Updates policy parameter $\theta$, in the direction suggested by the critic
$$
\underbrace{\nabla_\theta J(\theta)}_{policy\ gradient} = \underbrace{\mathbb{E_{\pi_\theta}}[\underbrace{\nabla_\theta \log \pi_\theta(s, a)}_{score\ function}\underbrace{Q_{w}(s, a)}_{action-value\ approximator}]}_{expectation\ under\ policy\ \pi_\theta}
$$
* Reduce variance using a baseline
	* A baseline function B(s) is substracted from the policy gradient
	* The goal is to normalize the reward
	* A good baseline is the state value function $B(s) = V^{\pi_\theta}(s)$
	* The advantage function $A^{\pi_\theta}(s, a)$
$$
A^{\pi_\theta}(s, a) = Q^{\pi_\theta}(s, a) - V^{\pi_\theta}(s) \\
\underbrace{\nabla_\theta J(\theta)}_{policy\ gradient} = \underbrace{\mathbb{E_{\pi_\theta}}[\underbrace{\nabla_\theta \log \pi_\theta(s, a)}_{score\ function}\underbrace{A^{\pi_\theta}(s, a)}_{advantage\ function}]}_{expectation\ under\ policy\ \pi_\theta}
$$
* The TD error $\delta_{\pi_\theta}$ is an unbiased estimate of the advantage function
$$
\mathbb{E_{\pi_\theta}}[\delta_{\pi_\theta}\ |\ s, a] = A^{\pi_\theta}(s, a)
$$

# Lecture 8 - Integrating Learning and Planning
* Model-Based RL
	* Advantages
		* Can efficiently learn model by supervised learning methods
		* Can reason about model uncertainty
	* Disadvantages
		* Two sources of approximation error (the model and the value function)
* Model-based RL is only as good as the estimated model
* Model-Free RL
	* No model
	* Learn value function (and/or policy) from real experience
* Model-Based RL (using Sample-Based Planning)
	* Learn a  model from real experience
	* Plan value function (and/or policy) from simulated experience
* Dyna
	* Learn a model from real experience
	* Learn and plan value function (and/or policy) from real and simulated experience
* Monte-Carlo Tree Search explores and expands the most promising parts of the tree while ignoring the parts of the search tree which are useless or providing bad results
* Advantages of Monte-Carlo Tree Search
	* Highly selective best-first search
	* Evaluates states dynamically
	* Uses sampling to break the curse of dimensionality
	* Works for "black-box" models (only requires samples)
	* Computationally efficient, anytime, parallelizable

# Lecture 9 - Exploration and Exploitation
* Three approaches to exploration
	* Random exploration
	* Optimist in the face of uncertainty
	* Information state space
* Two exploration spaces
	* State-action
	* Parameter
* Multi-armed bandit
	* A tuple $\langle \mathcal{A}, \mathcal{R} \rangle$
	* $\mathcal{A}$ is a known set of actions
	* $\mathcal{R}^a(r) = \mathbb{P}[R = r\ |\ A = a]$ is an unknown probability distribution over rewards
	* At each step t the agent selects an action $A_t \in \mathcal{A}$
	* The environment generates a reward $R_t \sim \mathcal{R}^{A_t}$
	* The goal is to maximize cumulative reward $\sum_{\tau = 1}^t R_\tau$
* The action value is the mean reward for action a
$$
q(a) = \mathbb{E}[R|A = a]
$$
* The optimal value $v_*$
$$
v_* = q(a^*) = \max_{a \in \mathcal{A}} q(a)
$$
* The regret is the opportunity loss for one step
$$
I_t = \mathbb{E}[v_* - q(A_t)]
$$
* The total regret is the total opportunity loss
$$
L_t = \mathbb{E}\left[\sum_{\tau = 1}^t v_* - q(A_\tau)\right]
$$
* The asymptotic total regret is at least logarithmic in the number of steps
$$
\lim_{t \rightarrow \infty} L_t \ge \log t \sum_{a|\Delta_a > 0} \frac{\Delta_a}{\text{KL}(\mathcal{R}^a || \mathcal{R}^{a^*})}
$$

# See also

# References
* http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html