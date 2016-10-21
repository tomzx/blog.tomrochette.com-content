---
title: Automated research
created: 2016-08-26
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context
Scientific research is a method through which state of the art (SotA) techniques, tools and methologies are developed and shared with the scientific community. It consists of numerous steps through which an individual goes in order to familiarize himself with the current SotA.

Currently, such process is generally defined but certainly not globally accepted. Furthermore, and this is the part we are interested in here, most of the process could be automated.

## Learned in this study

## Things to explore
* How is originality produced?
* Can [Parsey McParseface](https://research.googleblog.com/2016/05/announcing-syntaxnet-worlds-most.html) be used to extract references?
* Grammar induction
* Reference consistency verification (are the reference years the same or lower than the paper's publication year?)

## Questions
* How do you limit the depth of related papers?
	* Limit on the number of references per paper
	* Hardcoded/Defined limit
	* Limit on year range
* How should information be fed into the system?
	* Support only arxiv?

# Known
> The class of languages will be considered learnable with respect to the specified method of information presentation if there is an algorithm that the learner can use to make his guesses, the algorithm having the following property: Given any language of the class, there is some finite time after which the guesses will all be the same and they will be correct.[^1]

Given there is a maximum amount of different reference formats, smaller than the number of all valid permutations of the different token types supported, it is thus possible to inductively build a grammar that will allow us to extract the information within the reference correctly, every time.

# Overview
In this article we explore the idea of automating scientifical research. We attempt to cover the various research phases such as papers retrieval, assessment of the domain, determination of the core papers and authors in the field, construction of a bibliography and more.

The purpose of the automation process is to reduce the effort required for an individual to get into a (new) research field. The true endgoal would be to provide topics and receive new, genuine papers on the provided topic generated automatically by the computer through the agglomeration, analysis and synthesis of existing research.

# General research procedure
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

# Alternative approach
* Provide one or many papers which have been of interest to you
	* Go through the general research procedure

# Features extraction
In order to extract meaningful features out of scientific articles, we need to determine the features we are interested in. To do so, we inspect a small amount (~10/50) of articles and extract the elements we want to construct a database with.

## Paper structure
* Paper header
* Paper body
* Paper footer

### Paper header
* Title
* Author(s)
* Email(s)
* Affiliation(s)
* Abstract

### Paper body
* Content
	* Sections
		* Header
		* Body

### Paper footer
* References
* Annexes

#### Reference structure
* Authors
	* Author
		* First name
		* Middle name
		* Last name
* Title
* Publication year
* Journal
* Pages
	* From
	* To
* Conference

# Feature extraction procedures
## Extraction of references from PDF documents
* Create a training set with labels
* Build a tree of the different combinations based on the training data
* Find a way to hierarchically express these combinations

Run the regex on the whole reference for each type of segment to extract, then attempt to construct a reference by making sure that segments do not overlap

# Variables
## Reference
* Position of subsegments (author, title, year)

## Author
* Character sequence
* Length
* Structure class (First( Middle) Last|First (M.) Last|F. (M.) Last|Last, First( Middle)|Last, F.( M.))

# Issues with test data
## Problems
* Different tag names (year vs date)
* Different tagging (all authors under one author tag vs one author per tag)
* Tag formats (space padded tags)
* How should the precision/recall be computed on partial matches?

## Solutions
* Reformat the test data according to our format
* Make test code generalize data

# See also

# Sources
[^1]: Gold, E. Mark. "Language identification in the limit." Information and control 10.5 (1967): 447-474.

* [SCIgen - An Automatic CS Paper Generator](https://pdos.csail.mit.edu/archive/scigen/)
* http://www.cs.cornell.edu/cdlrg/reference%20linking/extraction.pdf
* https://github.com/CrossRef/pdfextract - Crashes on Windows
* https://github.com/metachris/pdfx - Does not extract text reference (only URL/DOI/arxiv)
* http://pythonhosted.org/refextract/ - Not compatible with Python 3.5 (unicode regex)
* http://www.dlib.org/dlib/september13/kern/09kern.html
* http://aye.comp.nus.edu.sg/parsCit/
* http://freecite.library.brown.edu/
* https://www.comp.nus.edu.sg/~kanmy/papers/lrec08b.pdf
* https://anystyle.io/
* http://www.lib.ncsu.edu/tools-citation
* http://pitt.libguides.com/citationhelp
* http://support.ebsco.com/knowledge_base/detail.php?id=5563
* http://www.scientificstyleandformat.org/Tools/SSF-Citation-Quick-Guide.html
* http://citeseerx.ist.psu.edu/index
* http://csxstatic.ist.psu.edu/about/scholarly-information-extraction
* http://www.lib.ncsu.edu/citationbuilder/#/article-journal/apa
* https://www.microsoft.com/en-us/research/project/microsoft-academic-graph/
* https://academicgraph.blob.core.windows.net/graph/index.html
* http://academic.research.microsoft.com/VisualExplorer
* Councill, Isaac G., C. Lee Giles, and Min-Yen Kan. "[ParsCit: an Open-source CRF Reference String Parsing Package](http://svn.tribler.org/abc/branches/leo/p2p-search/lib/parscit-080917/doc/lrec08/lrec08.pdf)." LREC. Vol. 8. 2008.
* Teufel, Simone, and Min-Yen Kan. [Robust argumentative zoning for sensemaking in scholarly documents](http://people.cs.pitt.edu/~litman/courses/nus062615/readings/TeufelKan.pdf). Springer Berlin Heidelberg, 2011.

## Labeled training data
* https://github.com/knmnyn/ParsCit/tree/master/doc
* https://github.com/knmnyn/ParsCit/blob/master/crfpp/taggeddata