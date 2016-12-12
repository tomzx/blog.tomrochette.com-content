---
title: Natural language processing
created: 2015-09-05
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---
## Context

## Learned in this study

## Things to explore

* How did language emerge?
* Structured vs unstructured languages
* Text summarization techniques
* Text understanding
* Text generation
* Determine if two texts are the same or similar
* Char-RNN (https://github.com/karpathy/char-rnn)
* How to properly classify each type of sentence?

# Overview

Being able to understand natural language is an important step in building something one might call intelligent. Language is first and foremost how individual communicates with one another using a common syntax.

Some natural languages are not able to express certain concepts at all while others can greatly define that same concept. From this, one will obviously ask: is there such a thing as a language that can express everything?

# Reading words

Reading a word is basically triggering letter by letter a sub neural network multiple times until the appropriate word is triggered

For instance, reading "word" would trigger all words with the letter "w", then "wo", then "wor" and finally "word". As the same sub neural network gets activated multiple times, its residual activation keeps increasing as more and more letters of the word are read.

# Requirements

* Linguistics
	* Grammar
		* Syntax
	* Semantics

# History of approaches
* Hand/hard coding of large sets of rules (if/then)

# Current *state of the art*
* Based on statistical machine learning
	* Generally grounded in statistical inference
	* Analysis of large corpora of real-world examples
	* Supervised learning using tagged corpus

# Suggested readings

# See also

# References

## General
* https://en.wikipedia.org/wiki/Natural_language_processing

## Summarization/Simplification

* https://en.wikipedia.org/wiki/Automatic_summarization
* https://en.wikipedia.org/wiki/Text_simplification
* http://ultimate-research-assistant.com/
* http://www.wikisummarizer.com/Pages/Default.aspx

## Uncategorized

* https://en.wikipedia.org/wiki/Category:Formal_languages
* https://en.wikipedia.org/wiki/Context-sensitive_grammar