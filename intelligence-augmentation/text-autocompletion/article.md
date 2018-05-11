---
title: Text autocompletion
created: 2018-05-10
taxonomy:
  category: [Intelligence Augmentation]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
* Words which require you to type them almost completely, such as "used" because "use" is more likely, do not benefit from autocompletion because typing the additional letter is as much work as accepting the autocompletion. However, since the target word ("used") is below the currently typed word, it would require more keystrokes to select (`go down`, `press enter` vs `type d`)
	* In other words, this means that a word list, ordered by most frequent to least frequent based on a document corpus, should drop all the words for which there is an edit distance of 1 with an word with lower index in the list
* Words for which the autocompletion can be done either by 1 keystroke or pressing enter should be configurable by the user (either they don't want to see them, or they want them so they can type or autocomplete)
* All the one letter words should be removed from the dictionary as they cannot benefit from autocompletion

# See also

# References
