"""
See the `main()` function to run the Ray or the non-Ray example.
"""

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
