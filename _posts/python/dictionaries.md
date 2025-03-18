---
title: Dictionaries in Python
date: November 15, 2022
---

A dictionary can be created with comma-separated key:value pairs within braces or by using the dict type constructor. A value is accessed by specifying its key in square brackets. The order of items in a dictionary is guaranteed as of Python 3.7.

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

The get method can be used to specify a default value when a key doesn't
exist.

```python
>>> time = {'hour': 1, 'min': 34}
>>> time.get('sec', 15)
15
```

The defaultdict is a specialized container type which supplies missing values based on the given default type.

```python
# using defaultdict will return a default value for the missing key
>>> from collections import defaultdict
>>> dd = defaultdict(int)
>>> dd['quantity']
0

# using a regular dictionary will return a key error
>>> d = {}
>>> d['quantity']
KeyError
```

## Combine dictionaries

There are several ways to combine dictionaries but the two examples shown below are the most simple and elegant. One approach is to use the merge operator `|` to merge the dictionaries. This is available in Python 3.9 and above.

```python
# Using the merge operator
>>> dict_one = {'one': 1, 'two': 2}
>>> dict_two = {'three': 3, 'four': 4}
>>> d = dict_one | dict_two
>>> d
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
```

Another approach is to unpack the dictionaries using the double-asterisk operator `**`.

```python
# Using the double-asterisk operator for unpacking
>>> dict_one = {'one': 1, 'two': 2}
>>> dict_two = {'three': 3, 'four': 4}
>>> d = {**dict_one, **dict_two}
>>> d
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
```
