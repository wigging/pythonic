---
title: Dictionary
date: 2020-11-27
---

**Contents**

- [Introduction](#introduction)
- [Loop through a dictionary](#loop-through-a-dictionary)
- [Default values](#default-values)

## Introduction

A dictionary can be created with comma-separated key:value pairs within braces or by using the dict type constructor. A value is accessed by specifying its key in square brackets.

```python
>>> d = {'one': 1, 'two': 2, 'three': 3}
>>> d['three']
3

>>> dd = dict(apples=2, oranges=5
>>> dd['oranges']
5
```

## Loop through a dictionary

The items method can be used to loop through a dictionary.

```python
>>> d = {'make': 'Ford', 'model': 'Bronco', 'year': 1977}
>>> for k, v in d.items():
...     print(k, '\t', v)
...
make     Ford
model    Bronco
year     1977
```

## Default values

The defaultdict is a specialized container type which supplies missing values based on the given default type.

```python
from collections import defaultdict

# using defaultdict will return a default value for the missing key
dd = defaultdict(int)
print('defaultdic', dd['item'])

# using a regular dictionary will return a key error
d = {}
print('dict', d['item'])
```
