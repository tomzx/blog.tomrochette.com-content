---
title: Pytest with tests files with similar names
created: 2020-02-28
taxonomy:
  type: post
  tag: [Problems, Python]
  status: finished
---

# Problem
I have two test files with the same name and pytest complains. How do I make it work without changing the test filenames?

Example directory structure
```
/path/to/project/tests
├── a/
│   └── test_a.py
└── b/
    └── test_a.py
```

Error message:
```
import file mismatch:
imported module 'test_a' has this __file__ attribute:
  /path/to/project/tests/a/test_a.py
which is not the same as the test file we want to collect:
  /path/to/project/tests/b/test_a.py
HINT: remove __pycache__ / .pyc files and/or use a unique basename for your test file modules
```

# Solution
Add a `__init__.py` to each directories with tests files that have the same name. Technically, you only need to have a `__init__.py` file in one of the two directories, so that one is in a package while the other one is in a different one. Adding it in both simply prevents this issue from occurring again if you were to add a third file `test_a.py`.

```
/path/to/project/tests
├── a/
│   ├── __init__.py
│   └── test_a.py
└── b/
    ├── __init__.py
    └── test_a.py
```
