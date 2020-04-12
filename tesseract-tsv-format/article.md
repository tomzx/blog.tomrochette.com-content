---
title: Tesseract TSV format
created: 2020-04-12
taxonomy:
  type: post-wip
  category: []
  status: draft
---

* level: hierarchical layout (a word is in a line which is in a paragraph, which is in a block which is in a page)
	* 1: page
	* 2: block
	* 3: paragraph
	* 4: line
	* 5: word
* page_num: when provided with a list of images, indicates the number of the file, starting from 1
* block_num: block number, starting from 0
* par_num: paragraph number, starting from 0
* line_num: line number, starting from 0
* word_num: word number, starting from 0
* left: x coordinate in pixels of the text bounding box top left corner, starting from the left of the image
* top: y coordinate of the text bounding box top left corner, starting from the top of the image
* width: width of the text bounding box in pixels
* height: height of the text bounding box in pixels
* conf: confidence value, from 0 to 100, -1 for all level except 5
* text: detected text, empty for all levels except 5
