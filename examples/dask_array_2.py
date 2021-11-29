"""
Example of using Dask array `map_blocks()` with a function that returns a
tuple value. Using an 8 CPU core MacBook Pro running macOS v11.6, the serial
elapsed time is 513.45 seconds and the Dask elapsed time is 3.20 seconds.
"""

import dask.array as da
import numpy as np
import time
from distributed import Client


def calc_result(p: float) -> float:
    """
    Function to map across an array.
    """
    time.sleep(1)
    a = p + 1
    b = p + 2
    return np.array([a, b])


def run_serial():
    """
    Non-parallel example (no Dask). Compare results and elapsed time to the
    Dask example.
    """
    tic = time.perf_counter()

    # Use these parameters to compare results to Dask example
    # params = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Use these parameters to compare elapsed time to Dask example
    params = np.random.random(512) * 10

    results_a = []
    results_b = []

    for p in params:
        a, b = calc_result(p)
        results_a.append(a)
        results_b.append(b)

    toc = time.perf_counter()

    print(f'Serial elapsed time {toc - tic:.2f} s')
    print(f'params\n{params}')
    print(f'results_a\n{results_a}')
    print(f'results_b\n{results_b}')


def run_dask():
    """
    Parallel example using Dask. Compare results and elapsed time to the
    serial example.
    """
    tic = time.perf_counter()

    # Use these parameters to compare results to serial example
    # params = da.from_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Use these parameters to compare elapsed time to serial example
    ps = np.random.random(512) * 10
    params = da.from_array(ps, chunks=64)

    futures = da.map_blocks(calc_result, params, new_axis=1)
    ab = futures.compute()
    results_a = ab[::2].flatten()
    results_b = ab[1::2].flatten()

    toc = time.perf_counter()

    print(f'Dask elapsed time {toc - tic:.2f} s')
    print(f'params\n{np.array(params)}')
    print(f'results_a\n{results_a}')
    print(f'results_b\n{results_b}')


if __name__ == '__main__':
    np.set_printoptions(precision=2)
    run_serial()

    client = Client(n_workers=8)
    run_dask()
    client.close()
