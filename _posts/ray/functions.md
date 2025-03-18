---
title: Ray functions
date: November 8, 2022
---

To parallelize a function with the [Ray](https://www.ray.io) framework, decorate the function with `@ray.remote` to run the function remotely. Call the function with `.remote()` instead of calling it normally. The remote call yields a future that must be fetched with `ray.get`. The example below compares a parallel Ray function to a standard non-parallel function. A computationally expensive task is simulated by using the `sleep()` function.

```python
import ray
import time


@ray.remote
def squared(x):
    time.sleep(1)
    y = x**2
    return y


def squared2(x):
    time.sleep(1)
    y = x**2
    return y


def run_ray():
    """
    Execute a Python function in parallel using Ray. Compare elapsed time to
    the non-parallel example `run_noray()`.
    """
    ray.init()

    tic = time.perf_counter()

    lazy_values = [squared.remote(x) for x in range(8)]
    values = ray.get(lazy_values)

    toc = time.perf_counter()

    print(f'Elapsed time {toc - tic:.2f} s')
    print(values)

    ray.shutdown()


def run_noray():
    """
    Execute a Python function in series, not in parallel. Compare elapsed time
    to the Ray parallel example `run_ray()`.
    """
    tic = time.perf_counter()

    values = [squared2(x) for x in range(8)]

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

Results from running the above example on a 6-core MacBook Pro are shown below. As expected, the example that uses the parallel Ray function has the fastest elapsed time.

```bash
# Results from running the parallel Ray function
Elapsed time 1.02 s
[0, 1, 4, 9, 16, 25, 36, 49]

# Results from running the non-parallel function
Elapsed time 8.02 s
[0, 1, 4, 9, 16, 25, 36, 49]
```
