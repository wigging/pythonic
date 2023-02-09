---
title: Loop over columns
date: November 7, 2022
---

Loop over columns in an array by iterating over the transpose of the array.

```python
# example.py

import numpy as np

a = np.array([
    [3, 5, 9, 12],
    [2, 8, 1, 4],
    [9, 7, 2, 1]
])

for col in a.T:
    print(col)
```

```python
>>> run example.py
[3 2 9]
[5 8 7]
[9 1 2]
[12  4  1]
```
