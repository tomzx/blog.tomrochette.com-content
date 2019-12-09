---
title: Set Theory
created: 2016-01-15
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview
* $\aleph_0$ (aleph-0): Cardinality of $\mathbb{N}$
* $c$: Cardinality of $\mathbb{R}$
* $\aleph_0$ and $c$ are called *transfinite numbers*
* Sets of cardinality $\aleph_0$ are said countable
* Sets of cardinality $c$ are said uncountable

* $E$: set
* $e$: element of E
* $e \in E$: $e$ is in the set $E$
* $e \not\in E$: $e$ is not in the set $E$
* card($E$) or $\#E$: cardinality of $E$
* $A \subset B$ when $A$ is in but not equal to $B$
* $A \subseteq B$ when $A$ is in or is equal to $B$

# Definition
* **Set:** A set is a non-ordered collection of distinct objects.
* **Element:** An object of a set.
* **Cardinality:** The number of elements of a set.
* **Empty set:** A set which contains no element (written as $\varnothing$ or $\{\}$).
* **Universal/Referential set:** Reference set that allows construction of other sets in a specific context. Written $\Omega$ or $U$.
* **Extension description:** When the elements of a set are enumerated.
$$
E = \{2, 4, 6, 8, 10\}
$$
* **Comprehension description:** When the elements of a set are specified by their properties.
$$
E = \{2n\ |\ n \in \mathbb{N}, 1 \le n \le 5\}
$$
* **Disjoints sets:** Two sets are *disjoint* if their intersection is empty.
* **Partition:** $n$ sets form a *partition* of a set $E$ if they are disjoint to one another and their union is $E$.
$$
\begin{cases}
	F_1 \cup F_2 \cup\ ...\ \cup F_n& =& E \\
	F_i \cap F_j = \varnothing& if& i \ne j
\end{cases}
$$
* **Cartesian product:** The set of all couples (a, b) that can be generated from the elements $a$ of $A$ and the elements $b$ of $B$.
$$
A \times B = \{(a, b)\ |\ a \in A, b \in B\}
$$
$$
A_1 \times A_2 \times\ ...\ \times A_n = \{(a_1, a_2, ..., a_n)\ |\ a_i \in A_i\}
$$

# Properties of power sets
* If $E_1 = \varnothing$, then $\mathcal{P}(E_1) = \{\varnothing\}$
* If $E_2 = \{1\}$, then $\mathcal{P}(E_2) = \{\varnothing, \{1\}\}$
* If $E_3 = \{1, 2\}$, then $\mathcal{P}(E_3) = \{\varnothing, \{1\}, \{2\}, \{1, 2\}\}$
* If $E_4 = \{1, 2, 3\}$, then $\mathcal{P}(E_4) = \{\varnothing, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}\}$

# Number sets
* $\mathbb{N} = \{0, 1, 3, 4, ...\}$ the set of natural numbers
* $\mathbb{Z} = \{..., 3, 2, 1, 0, 1, 2, 3, ...\}$ the set of integers
* $\mathbb{Q} = \{\frac{a}{b}\ |\ a \in \mathbb{Z}, b \in \mathbb{N}, b \not= 0\}$ the set of rational numbers
* $\mathbb{R}$ the set of real numbers (periodic decimal development)
* $\mathbb{I}$ the set of irrational numbers (non-periodic decimal development)
* $\mathbb{C} = \{a+bi\ |\ a, b \in \mathbb{R}, i^2 = -1\}$ the set of complex numbers

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}
$$

* $E_+ = \{x \in E\ |\ x \ge 0\}$
* $E_- = \{x \in E\ |\ x \le 0\}$
* $E_* = \{x \in E\ |\ x \ne 0\}$
* $E_+^* = \{x \in E\ |\ x \gt 0\}$
* $E_-^* = \{x \in E\ |\ x \lt 0\}$

# Operations on sets
* **Difference:** The elements of $E$ that are not in $F$.
$$
E \setminus F
$$
$$
E \setminus F = \{x \in \Omega\ |\ (x \in E) \wedge (x \not\in F)\}
$$
* **Intersection:** The elements that are common to $E$ and $F$.
$$
E \cap F
$$
$$
E \cap F = \{x \in \Omega\ |\ (x \in E) \wedge (x \in F)\}
$$
* **Union:** The elements that are either or both $E$ and $F$.
$$
E \cup F
$$
$$
E \cup F = \{x \in \Omega\ |\ (x \in E) \vee (x \in F)\}
$$
* **Complement:** The elements that are not in $E$.
$$
E^c\ or\ E'
$$
$$
E^c = E' = \{x \in \Omega\ |\ (x \not\in E)\}
$$

# Families
* $dom(I)$: index
* $I$: index set
* $ran(I)$: indexed set
* function: family
* value of the function $x$ at an index $i$: term of the family, denoted $x_i$

# Composite functions
If $f$ is a function from $X$ to $Y$ and $g$ is a function from $Y$ to $Z$, then every element in the range of $f$ belongs to the domain of $g$, and, consequently, $g(f(x))$ makes sense for each $x$ in $X$. The function $h$ from $X$ to $Z$, defined by $h(x) = g(f(x))$ is called the *composite* of the functions $f$ and $g$; it is denoted by $g \circ f$.

# Notes
## Comprehension description of a set of values with multiples
To describe a set where the values are multiple of a value y, we say

$$
E = \{yx\ |\ x \in \mathbb{N}\}
$$

## Elements of a power set
Let $E = \{1, 2\}$,
$\mathcal{P}(E) = \{\varnothing, \{1\}, \{2\}, \{1, 2\}\}$

* $1 \in E$
* $\{1\} \not\in E$
* $1 \subset E$ (not valid, left part must be a set)
* $\{1\} \subset E$
* $1 \not\in \mathcal{P}(E)$
* $\{1\} \in \mathcal{P}(E)$
* $\{1\} \not\subset \mathcal{P}(E)$ (for the same reason * that $1 \not\in \mathcal{P}(E)$)
* $\{\{1\}\} \subset \mathcal{P}(E)$

# See also

# References
* Bourbonnais, Daniel. Mathématiques pour les sciences. Montréal: Collège Ahuntsic; 2005.
* http://www.settheory.net/