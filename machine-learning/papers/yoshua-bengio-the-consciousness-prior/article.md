---
title: Yoshua Bengio - The Consciousness Prior (2017)
created: 2017-09-28
taxonomy:
  tag: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview
* Represent conscious states as low-dimensional vectors
* Conscious states are taken from high-dimensional unconscious states
* It is likely that some form of RNN will be used to learn how to extract the conscious states from the unconscious state

# Notes
## 1 Introduction
* Consciousness as defined by Locke: consciousness is "the perception of what passes in a man's own mind", or awareness of an external object or something within oneself

## 2 Consciousness Prior Theory
### 2.1 Subnetworks
* Let $s_t$ be the observed state at time $t$ and let $h_t$ be the high-level representation derived from $s_t$ (and from past observed values $s_{t-k}$ in the partially observable case)
$$
h_t = F(s_t, h_{t-1})
$$
* The conscious state $c_t$ is defined as a very low-dimensional vector which is derived from $h_t$ by a form of attention mechanism applied on $h_t$, taking into account the previous conscious state as context
$$
c_t = C(h_t, c_{t-1}, z_t)
$$
where $z_t$ is a random noise source
* The cognitive interpretation is that the value of $c_t$ corresponds to the content of a thought, a very small subset of all the information available to us unconsciously, but which has been brought to our awreness by a particular form of attention which picks several elements or projections from $h_t$
* The function $C$ is the consciousness RNN and because of its random noise inputs, produces a random choice of the elements on which the attention gets focused

### 2.2 Training Objectives
* To capture the assumption that a conscious thought can encapsulate a statement about the future, we introduce a verifier network which can match a current representation state $h_t$ with a past conscious state $c_{t-k}$:
$$
V(h_t, c_{t-k}) \in \mathbb{R}
$$
* $V(h_t, c_{t-k})$ indicates the consistency of $c_{t-k}$ with $h_t$, e.g., estimating the probability of the corresponding statement being true, given $h_t$
* We would like to define an objective (or reward) function which embodies the idea that the attended (conscious) elements are used in some way whose value can be quantified and optimized
* There are two distinct mechanisms at play which contribute to map the high-level state representation to the objective function
	* the attention mechanism which selects and combines a few elements from the high-level state representation into a low-dimensional "conscious sub-state" object
	* the predictions or actions which are derived from the sequence of these conscious sub-states

# See also

# References
* Bengio, Yoshua. "The Consciousness Prior." arXiv preprint arXiv:1709.08568 (2017).
