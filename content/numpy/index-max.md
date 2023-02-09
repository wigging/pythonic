---
title: Index of max value
date: February 6, 2023
---

Use NumPy's `argmax()` function to get the index of the maximum value in an array.

```python
import numpy as np

x = np.array([1, 8, 2.5, 4])
ind = x.argmax()

print('1D array', x)
print('Max value at index', ind)
```

```text
1D array [1 8 2.5 4]
Max value at index 1
```

If there are multiple occurrences of the max value, then the first index is returned.

```python
y = np.array([1, 8, 2.5, 4, 8])  # index of first occurrence is returned
ind = y.argmax()

print('1D array', y)
print('Max value at index', ind)
```

```text
1D array [1 8 2.5 4 8]
Max value at index 1
```

Use the `unravel_index()` function to get the row and column indices of the max value in a two-dimensional array.

```python
z = np.array([[1, 2.4, 7, 5], [0.2, 8, 7, 4.9], [5, 3.1, 4, 1], [7, 2, 4, 3]])
ind = np.unravel_index(z.argmax(), z.shape)

print('2D array\n', z)
print('Max value at index', ind)
```

```text
2D array
[[1   2.4  7  5  ]
 [0.2 8    7  4.9]
 [5   3.1  4  1  ]
 [7   2    4  3  ]]
Max value at index (1, 1)
```
