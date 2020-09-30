---
title: Dictionary
slug: dictionary
layout: section
date: 2020-09-15
---

**Contents**

- [Basics](#basics)
- [Further reading](#further-reading)

## Basics

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

## Further reading

- Collections — Container Datatypes — Python 3.8.6rc1 Documentation. Accessed September 15, 2020. <https://docs.python.org/3/library/collections.html#collections.defaultdict>
