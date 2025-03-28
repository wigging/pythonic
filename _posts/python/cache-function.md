---
title: Cache Function in Python
date: January 13, 2024
---

The [functools](https://docs.python.org/3/library/functools.html) module provides a `@cache` decorator to store the results of an expensive function; also known as memoize.

## No function cache

This example calls a function several times. The function sleeps for 2 seconds to represent an expensive task being performed.

```python
import time


def coeffs_one(method):
    """
    Get the a and b coefficients for a given method.
    """
    time.sleep(2)

    if method == "yaws":
        a, b = 1, 2
    elif method == "graham":
        a, b = 2, 4
    else:
        a, b = 0, 0

    return a, b


for _ in range(3):
    ti = time.perf_counter()
    a, b = coeffs_one("graham")
    tf = time.perf_counter()
    print(f"a is {a} | b is {b} | Elapsed {tf - ti:.4f} s")
```

The output is shown below. Notice the elapsed time for each run is 2 seconds.

```text
a is 2 | b is 4 | Elapsed 2.0036 s
a is 2 | b is 4 | Elapsed 2.0032 s
a is 2 | b is 4 | Elapsed 2.0044 s
```

## Using function cache

This example calls a function several times and uses the `@cache` decorator to store the results.

```python
import time
from functools import cache


@cache
def coeffs_two(method):
    """
    Get the a and b coefficients for a given method.
    """
    time.sleep(2)

    if method == "yaws":
        a, b = 1, 2
    elif method == "graham":
        a, b = 2, 4
    else:
        a, b = 0, 0

    return a, b


for _ in range(3):
    ti = time.perf_counter()
    a, b = coeffs_two("graham")
    tf = time.perf_counter()
    print(f"a is {a} | b is {b} | Elapsed {tf - ti:.4f} s")
```

The output for this example is shown below. Notice the elapsed time for the second and third runs is zero because the function results are cached.

```text
a is 2 | b is 4 | Elapsed 2.0001 s
a is 2 | b is 4 | Elapsed 0.0000 s
a is 2 | b is 4 | Elapsed 0.0000 s
```
