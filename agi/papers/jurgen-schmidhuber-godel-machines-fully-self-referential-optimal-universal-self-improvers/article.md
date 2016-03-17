---
title: Jürgen Schmidhuber - Gödel Machines: Fully Self-Referential Optimal Universal Self-improvers
created: 2016-01-01
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

## 1 Introduction and Outline
* Optimal, fully self-referential general problem solvers called Gödel machines
* Gödel machines interact with some partially observable environment
* Gödel machines can in principle modify themselves without essential limits besides the limtis of computability
* Their initial algorithm is not hardwired
	* It can completely rewrite itself, only if a proof searched embedded within the initial algorithm can first prove that the rewrite is useful, given a formalized utility function reflecting computation time and expected future success
* The approach (Gödel machines) should yield the first theoretically sound, fully self-referential, optimal, general problem solvers

## 2 Basic Overview, Relation to Previous Work, and Limitations
* We will consider the more general case where the problem solution requires interaction with a dynamic, initially unknown environment that produces a continual stream of inputs and feedback signals, such as in autonomous robot control tasks, where the goal may be to maximize expected cumulative future reward
* This may require the solution of essentially arbitrary problems

## 2.1 Notation and Set-up
* $B = \{0, 1\}$: the binary alphabet
* $B^*$: the set of finite sequences (bitstrings) over the binary alphabet $B$
* $l(q)$: the number of bits in a bitstring q
* $q_n$: the $n$-th bit of $q$
* $\lambda$: the empty string (where $l(\lambda) = 0$)
* $q_{m:n}$: $\lambda$ if $m > n$ and $q_mq_{m+1}...q_n$ otherwise (where $q_0 = q_{0:0} = \lambda$)
* Our hardware has a single life which consists of discrete cycles or time steps $t = 1,2,...$
* Its total lifetime $T$ may or may not be known in advance
* Any time-varying variable $Q$ at time $t$ will be denoted $Q(t)$
* During each cycle our hardware executes an elementary operation which affects its variable state $s \in \mathcal{S} \subset \mathcal{B}^*$ and possibly also the variable environment state $Env \in \mathcal{E}$
* There is a hardwired state transition function $F : \mathcal{S} \times \mathcal{E} \rightarrow \mathcal{S}$
* For $t > 1$, $s(t) = F(s(t - 1), Env(t - 1))$ is the state at a point where the hardware operation of cycle $t - 1$ is finished, but the one of $t$ as not yet started
* $Env(t)$ may depend on past output actions encoded in $s(t - 1)$ and is simultaneously updated or computed by the possibly reactive environment
* 4 variables of interest
	* $time$: At time $t$, it holds a unique binary representation of $t$. We initialize $time(1) = 1$, the bitstring consisting only of a one. The hardware increments $time$ for one cycle to the next. This requires at most $O(\log{t})$ and on average only $O(1)$ computational steps
	* $x$: Holds environmental inputs. For $t > 1$, $x(t)$ may differ from $x(t - 1)$ only if a program running on the Gödel machine has executed a special input-requesting instruction at time $t - 1$.
	* $y(t)$: An output bitstring which may subsequently influence the environment, where $y(1) = 0$ by default
	* $p(1)$: The initial software: a program implementing the original policy for interacting with the environment and for proof searching
* At any given time $t (1 \le t \le T)$, the goal is to maximize future success or utility
* $u(s, Env) : \mathcal{S} \times \mathcal{E} \rightarrow \mathcal{R}$, where $\mathcal{R}$ is the set of real numbers

$$u(s, Env) = E_\mu\left[\sum_{\tau=time}^{T}r(\tau)\middle|s, Env\right]$$

* $r(t)$: a real-valued reward input (encoded within $s(t)$) at time $t$
* $E_\mu(\cdot\ |\ \cdot)$: the conditional expectation operator with respect to some possibly unknown distribution $\mu$ from a set $M$ of possible distributions ($M$ reflects whatever is known about the possibly probabilistic reactions of the environment)
* $time = time(s)$: a function of state $s$ which uniquely identifies the current cycle


# See also

# Sources
* [arXiv:cs/0309048](http://arxiv.org/abs/cs/0309048) [cs.LO]