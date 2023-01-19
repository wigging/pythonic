+++
title = "Counter"
date = 2022-11-08
+++

The `Counter` class counts the number of times an item appears in a list or hashable object. For example, you can count the number of times a string appears in a list or how often a letter occurs in a string.

```python
>>> from collections import Counter

# Example 1

>>> fruits = ['apple', 'orange', 'lemon', 'orange', 'apple', 'apple']
>>> counts = Counter(fruits)

>>> counts
Counter({'apple': 3, 'orange': 2, 'lemon': 1})

>>> counts['orange']
2

# Example 2

>>> string = 'Hello world of worlds'
>>> counts = Counter(string)
>>> counts['o']
4
```
