---
title: Omnifocus "ofocus" format
created: 2020-02-20
taxonomy:
  type: post
  tag: [problems]
  status: finished
  readability: 3
---

# Problem
I use Omnifocus but I'd like to have access to the underlying data and use it in another application. How can I do that?

# Solution
The first step to solve this problem is figuring out if we can access the underlying data easily. Sometimes we're lucky and the data is just a single file with the data in a format that we need to manipulate a little. In other cases, like for the ofocus format, files are organized in a single directory that contains zip archives. Unzipping some of those files we can observe there are two kinds: a master file and many transaction files. By playing around a bit with Omnifocus, we can make all the transactions files disappear, effectively merging them into the master file.

The next step is to look at the content of the master file. This file contains most of what we would expect to find when we use Omnifocus, namely contexts, folders and tasks. By inspecting multiple copies of the same type of entry it is possible to collect the different attributes that constitute them and whether some are optional while others are always present.

When I tried to reverse-engineer the format of ofocus files, I used my own database which contained many entries. This allowed me to quickly find most of the attributes of each type of entry. Another approach would've been to start with a clean database and to create each of the types of entry and create two variants: one with all the attributes defined, the other one with the least amount of attributes necessary.

Once the structure of those entries is identified, it is not too difficult to use reasoning to determine from where certain values come from. In some cases, values are references to other entries, similar to how you would have foreign keys in a database.

With all this knowledge now available to us, it is easy to simply convert the XML file into a JSON file. Once the data is available in JSON, it's slightly easier to work with it in PHP than using XML. By understanding the structure and relationships within the data, it is possible to make use of this data to build your own application that would reproduce the hierarchy of folders/tasks that are displayed inside Omnifocus.

# References
* https://github.com/tomzx/ofocus-format
