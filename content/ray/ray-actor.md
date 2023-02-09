---
title: Ray actor
date: November 8, 2022
---

[Ray](https://www.ray.io) actors are used to parallelize a class instance to perform stateful operations in parallel. Ray will start a remote instance of the class and then execute remote method calls and maintain its own internal state. The example below compares a parallel Ray actor approach to a standard class approach. A computationally expensive task is simulated by using the `sleep()` function.

```python
import ray
import time


@ray.remote
class Counter:

    def __init__(self):
        self.n = 0

    def increment(self):
        time.sleep(1)
        self.n += 1

    def read(self):
        return self.n


class Counter2:

    def __init__(self):
        self.n = 0

    def increment(self):
        time.sleep(1)
        self.n += 1

    def read(self):
        return self.n


def run_ray():
    """
    Execute a Ray actor model in parallel. Compared elapsed time to the
    non-parallel example `run_noray()`.
    """
    ray.init()

    tic = time.perf_counter()

    counters = [Counter.remote() for i in range(4)]
    [c.increment.remote() for c in counters]
    [c.increment.remote() for c in counters]

    futures = [c.read.remote() for c in counters]
    values = ray.get(futures)

    toc = time.perf_counter()

    print(f'Elapsed time {toc - tic:.2f} s')
    print(values)

    ray.shutdown()


def run_noray():
    """
    Excecute several class instances in series, not parallel. Compare elapsed
    time to the Ray parallel example `run_ray()`.
    """
    tic = time.perf_counter()

    counters = [Counter2() for _ in range(4)]
    [c.increment() for c in counters]
    [c.increment() for c in counters]

    values = [c.read() for c in counters]

    toc = time.perf_counter()

    print(f'Elapsed time {toc - tic:.2f} s')
    print(values)


def main():
    """
    Run the Ray example or the non-Ray example.
    """
    # run_ray()
    run_noray()


if __name__ == '__main__':
    main()
```

Results from running the above example on a 6-core MacBook Pro are shown below. As expected, the example that uses the parallel Ray actor has the fastest elapsed time.

```bash
# Results from running the parallel Ray actor
Elapsed time 3.28 s
[2, 2, 2, 2]

# Results from running the non-parallel class approach
Elapsed time 8.02 s
[2, 2, 2, 2]
```
