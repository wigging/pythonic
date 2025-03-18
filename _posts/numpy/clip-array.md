---
title: Clip array values with NumPy
date: November 7, 2022
---

The `clip` function limits the values in an array based on a given interval or minimum or maximum value.

```python
>>> import numpy as np

>>> a = np.array([-2, -5.1, 3, 8, 10.2])
array([-2, -5.1,  3,  8, 10.2])

# Limit min and max values to a given interval
>>> a.clip(1, 7)
array([1, 1, 3, 7, 7])

>>> np.clip(a, 1, 7)
array([1, 1, 3, 7, 7])

# Limit values to a minimum value
>>> a.clip(-1)
array([-1, -1,  3,  8, 10.2])

>>> a.clip(min=-1)
array([-1, -1,  3,  8, 10.2])

# Limit values to a maximum value
>>> a.clip(max=4.5)
array([-2, -5.1,  3,  4.5,  4.5])
```
