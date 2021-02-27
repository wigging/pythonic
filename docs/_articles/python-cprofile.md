---
title: cProfile
date: 2021-02-27
---

The `cProfile` module provides an interface to profile Python programs. A single function or an entire script or module can be profiled. As an example, the script shown below contains two functions that suspend execution for 2 and 4.5 seconds.

```python
# ztest.py

import time


def slow():
    time.sleep(2)


def slower():
    time.sleep(4.5)


slow()

slower()
```

Use the terminal command given below to profile the script. This will output the profile results to the terminal as total time `tottime` and cumulative time `cumtime`.

```bash
$ python -m cProfile ztest.py

7 function calls in 6.503 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    6.503    6.503 ztest.py:1(<module>)
        1    0.000    0.000    2.002    2.002 ztest.py:4(slow)
        1    0.000    0.000    4.501    4.501 ztest.py:8(slower)
        1    0.000    0.000    6.503    6.503 {built-in method builtins.exec}
        2    6.502    3.251    6.502    3.251 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

The output can be sorted using the sort arguments: `calls`, `cumtime`, `cumulative`, `filename`, `line`, `module`, `name`, `ncalls`, `nfl`, `pcalls`, `stdname`, `time`, and `tottime`. The example below sorts the output based on the total time.

```bash
$ python -m cProfile -s tottime ztest.py

7 function calls in 6.506 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    6.506    3.253    6.506    3.253 {built-in method time.sleep}
        1    0.000    0.000    4.501    4.501 ztest.py:8(slower)
        1    0.000    0.000    6.506    6.506 ztest.py:1(<module>)
        1    0.000    0.000    2.005    2.005 ztest.py:4(slow)
        1    0.000    0.000    6.506    6.506 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

See the [Python documentation](https://docs.python.org/3/library/profile.html) for more information about the profiler.
