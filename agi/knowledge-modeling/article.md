---
title: Knowledge modeling
todo: rename to language modeling
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
Vocabulary\ of\ entity\ 1 = V_1 \\
Cardinality\ of\ the\ vocabulary\ of\ entity\ 1 = |V_1|
$$

$$
Vocabulary\ of\ entity\ 2 = V_2 \\
Cardinality\ of\ the\ vocabulary\ of\ entity\ 2 = |V_1|
$$

$$
Common\ vocabulary = V_1 \cap V_2 \\
Shared\ vocabulary = V_1 \cup V_2 \\
Vocabulary\ only\ in\ V_1 = V_1 - V_2 \\
Vocabulary\ only\ in\ V_2 = V_2 - V_1 \\
Uncommon\ vocabulary = (V_1 \cup V_2) - (V_1 \cap V_2) = (V_1 - V_2) \cup (V_2 - V_1)
$$

$$
Jaccard\ index = J(V_1, V_2) = \frac{|V_1 \cap V_2|}{|V_1 \cup V_2|} \\
Size\ relative\ Jaccard\ index = |V_1 \cap V_2| \times J(V_1, V_2) = 2 \frac{|V_1 \cap V_2|}{|V_1 \cup V_2|}
$$

$$
Overlap\ coefficient = overlap(V_1, V_2) = \frac{|V_1 \cap V_2|}{\min(|V_1|, |V_2|)}
$$

# See also

# References
* https://en.wikipedia.org/wiki/Jaccard_index