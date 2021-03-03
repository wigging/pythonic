---
title: Maximum array
date: 2021-03-02
---

The `maximum` function returns a new array that contains the maximum values of the two given arrays.

```python
>>> import numpy as np

# Create an array using maximum values from two arrays
>>> a = np.array([3, 5, 8, -1, 4.1, -8.5])
>>> b = np.array([10, 2, 8.1, -2, 5, 3])
>>> np.maximum(a, b)
array([10, 5, 8.1, -1, 5, 3])

# Create an array without negative values
>>> a = np.array([3, 5, 8, -1, 4.1, -8.5])
>>> np.maximum(a, 0)
array([3, 5, 8, 0, 4.1, 0])
```
