---
title: Structuring an AGI research
created: 2015-09-05
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Learned in this study

## Things to explore
* Extract references automatically based on what is said in a text

# Overview

The most general questions every AGI researcher needs to answer include[^1]:
* What is AGI, accurately specified?
* Is it possible to build the AGI as specified?
* If AGI is possible, what is the most plausible way to achieve it?
* Even if we know how to achieve AGI, should we really do it?

A complete AGI work normally includes[^1]:
* a theory of intelligence,
* a formal model of the theory,
* a computational implementation of the model.

---

Define the problems and questions you are trying to solve.

* This is what I am solving
* This is what I am building
* This is how I am solving it
* Here is how we can think about it now

---

* State the problem you want to solve in general terms
* Collect previous work related to your research
* Understand the material
* Implement the ideas found in previous work
* Specify your problem in details
* Think (and use Pólya How to Solve It)
* Implement your idea and compare it/Review
* Report/Publish
* Discuss topic with colleagues

---

* Good research should be novel:
	* Describe state-of-the-art (SoA)
	* Describe state-of-the-pratice (SoP)
	* Describe how your work is different from them
* Good research should be relevant:
	* Consider what problems we face today or are likely to face within some time span
	* Consider what other researchers and practitioners problems are and what they consider important
* Good research should present generalities/principles
* Good research is often systematic and structured
	* Systematic: You have a clear idea of what to do and that this will clearly "cover" the most likely relevant aspects
	* Structured: There is good "logic" and "flow" in what you are trying to do and how you describe it
* Good research claims something and validate those claims

* Focus on a part of your subject area that is limited so that you can go deep in 40-150 papers
* Create a taxonomy of the papers you find

# "Automated" research
* The user defines a topic of interest (ex. artificial general intelligence)
* Automatically
	* Find papers related to the topic and download them
		* Find relevant sources of papers in the domain (arxiv, nature, science, acm, springer, google scholar, etc.)
	* Create a graph of paper references (which paper references which paper)
		* This graph will be used to determine which papers are foundation and which papers are extensions
		* The more a paper is referenced, the more likely is it worth reading
			* Use some algorithms, maybe similar to Google Page Rank to determine the "quality" of the paper
		* References are extracted from the papers themselves (or by using a reference engine)
		* References are cross-referenced
	* Extract writing style (tf-idf, most frequent words, sentence/paragraph/section length) as well as various features (number of charts, tables, figures, etc.)
	* Compile a list of references based on the papers extracted above
	* Compile a list of the more prominent writers in the field/topic
	* Create summaries of the different presented ideas with links to the related articles

## Questions
* How do you limit the depth of related papers?
	* Limit on the number of references per paper
	* Hardcoded/Defined limit
	* Limit on year range

# Sources

[^1]: https://sites.google.com/site/narswang/home/agi-introduction#TOC-Representative-AGI-Projects

* http://www.umiacs.umd.edu/~knkim/HowToPhd.htm
* http://www.robertfeldt.net/advice/feldt_guide_to_starting_a_phd.pdf
* [SCIgen - An Automatic CS Paper Generator](https://pdos.csail.mit.edu/archive/scigen/)

## Automated research
* http://www.cs.cornell.edu/cdlrg/reference%20linking/extraction.pdf
* https://github.com/CrossRef/pdfextract - Crashes on Windows
* https://github.com/metachris/pdfx - Does not extract text reference (only URL/DOI/arxiv)
* http://pythonhosted.org/refextract/ - Not compatible with Python 3.5 (unicode regex)