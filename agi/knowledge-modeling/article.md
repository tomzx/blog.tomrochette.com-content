---
title: Knowledge modeling
created: 2015-12-05
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

* Vocabulary
    * Size of vocabulary vs another entity
    * Overlapping/Intersecting vocabulary with another entity

# Overview

$$
V_1 = Vocabulary\ of\ user\ 1 \\
|V_1| = Cadinality\ of\ the\ vocabulary\ of\ entity\ 1
$$

$$
V_2 = Vocabulary\ of\ user\ 2 \\
|V_1| = Cadinality\ of\ the\ vocabulary\ of\ entity\ 2 \\
$$

$$
V_1 \cap V_2 = Common\ vocabulary \\
V_1 \cup V_2 = Shared\ vocabulary \\
V_1 - V_2 = Vocabulary\ only\ in\ V_1 \\
V_2 - V_1 = Vocabulary\ only\ in\ V_2 \\
(V_1 \cup V_2) - (V_1 \cap V_2) = (V_1 - V_2) \cup (V_2 - V_1) = Uncommon\ vocabulary
$$

$$
Jaccard\ index = J(V_1, V_2) = \frac{|V_1 \cap V_2|}{|V_1 \cup V_2|} \\
Size\ relative\ Jaccard\ index = |V_1 \cap V_2| \times J(V_1, V_2) = 2 \frac{|V_1 \cap V_2|}{|V_1 \cup V_2|}
$$

$$
Overlap\ coefficient = overlap(V_1, V_2) = \frac{|V_1 \cap V_2|}{\min(|V_1|, |V_2|)}
$$

# See also

# Sources
