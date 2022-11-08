---
title: Compare inv and solve functions
date: November 7, 2022
---

Solve equation `A*x=b` for `x` and compare results using the `np.linalg.solve()` function to the `np.linalg.inv()` approach.


```python
import numpy as np
from time import perf_counter

# Check results
# ----------------------------------------------------------------------------

a = np.random.rand(4, 4)
b = np.random.rand(4)

x = np.linalg.solve(a, b)
print('x', x)

x = np.linalg.inv(a) @ b
print('x', x)

# Elapsed time
# ----------------------------------------------------------------------------

n = 5000

a = np.random.rand(n, n)
b = np.random.rand(n)

tic = perf_counter()
x = np.linalg.solve(a, b)
toc = perf_counter()
print(f'Elapsed time for .solve is {toc - tic:.2f} s')

tic = perf_counter()
x = np.linalg.inv(a) @ b
toc = perf_counter()
print(f'Elapsed time for .inv is {toc - tic:.2f} s')
```

The output shown below is from running the example on a MacBook Pro. Using `np.linalg.solve()` is noticeably faster (especially for large arrays) than using the inverse matrix approach.

```
x [-19.96400793 6.3753703 -8.27713073 35.08957403]
x [-19.96400793 6.3753703 -8.27713073 35.08957403]
Elapsed time for .solve is 0.98 s
Elapsed time for .inv is 3.47 s
```
