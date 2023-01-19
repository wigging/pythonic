+++
title = "Full array"
date = 2022-11-07
+++

Use the `full` function in NumPy to create a new array filled with a given value.

```python
>>> import numpy as np

# Create an array of length 10 filled with a value of 3.1
>>> np.full(10, 3.1)
array([3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1])

# Create an array with shape (3, 4) filled with 7
>>> np.full((3, 4), 7)
array([[7, 7, 7, 7],
       [7, 7, 7, 7],
       [7, 7, 7, 7]])

# Create an array where each row is filled with a list
>>> np.full((3, 4), [91, 3, 1, 5])
array([[91,  3,  1,  5],
       [91,  3,  1,  5],
       [91,  3,  1,  5]])
```