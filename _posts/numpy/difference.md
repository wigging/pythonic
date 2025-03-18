---
title: Set difference of two NumPy arrays
date: November 7, 2022
---

The `setdiff1d` function returns the unique values in array 1 that are not in array 2.

```python
>>> import numpy as np

# Array 1
>>> a = np.array([4, 5, 6.2, 8, 10])

# Array 2
>>> b = np.array([4, 5, 6, 7, 8])

# Return unique values in `a` that are not in `b`
>>> np.setdiff1d(a, b)
array([6.2, 10])
```
