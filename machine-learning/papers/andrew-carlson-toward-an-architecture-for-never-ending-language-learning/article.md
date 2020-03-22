---
title: Andrew Carlson - Toward an Architecture for Never-Ending Language Learning (2010)
created: 2017-06-09
taxonomy:
  category: [Machine learning]
  status: finished
---

## Context

## Learned in this study

## Things to explore

# Overview
* A knowledge base of first-order predicate and instance is built by crawling the web
* Using 4 components, NELL extracts textual patterns, queries the Internet for instances of known predicates, classify these instances using a logistic regression model and learns new first-order relations
* After running for 67 days, it learned over 240000 facts with an estimated precision of 74% (90%, 71% and 57% respectively over 3 evaluations)

# Notes
## Introduction
* By a "never-ending language learner" we mean a computer system that runs 24 hours per day, 7 days per week, forever, performing the following two tasks each day:
	* Reading task: extract information from web text to further populate a growing knowledge base of structured facts and knowledge
	* Learning task: learn to better read each day than the day before, as evidenced by its ability to go back to yesterday's text sources and extract more information more accurately

## Implementation
* NELL uses four subsystem components:
	* Coupled Pattern Learner: A free-text extractor which learns and uses contextual patterns like "mayor of X" and "X plays for Y" to extract instances of categories and relations
	* Coupled SEAL: A semi-structured extractor which queries the Internet with sets of beliefs from each category or relation, then mines lists and tables to extract novel instances of the corresponding predicate
	* Coupled Morphological Classifier: A set of binary $L_2$-regularized logistic regression models - one per category - which classify noun phrases based on various morphological features (words, capitalization, affixes, parts-of-speech, etc.)
	* Rule Learner: A first-order relational learning algorithm similar to FOIL, which learns probabilistic Horn clauses

# See also

# References
* Carlson, Andrew, et al. "Toward an Architecture for Never-Ending Language Learning." AAAI. Vol. 5. 2010.
