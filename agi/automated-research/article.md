---
title: Automated research
created: 2016-08-26
taxonomy:
  category: [Artificial General Intelligence]
  status: in progress
---

## Context

## Learned in this study

## Things to explore
* How is originality produced?
* Can [Parsey McParseface](https://research.googleblog.com/2016/05/announcing-syntaxnet-worlds-most.html) be used to extract references?

# Overview
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

## Alternative approach
* Give one or many papers which have been of interest to you

## Function
* Given an initial set of papers
	* Extract references from found papers
		* Find referenced papers online (google search with filetype:pdf)

## Questions
* How do you limit the depth of related papers?
	* Limit on the number of references per paper
	* Hardcoded/Defined limit
	* Limit on year range

# See also

# Sources
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
* http://www.lib.ncsu.edu/citationbuilder/#/article-journal/apa