"""
Example of using the Dask array `map_blocks()` with a function that returns a
single value. Using an 8 CPU core MacBook Pro running macOS v11.6, the serial
elapsed time is 513.51 seconds and the Dask elapsed time is 3.21 seconds.
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
    result = p + 1
    return result


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

    results = []

    for p in params:
        r = calc_result(p)
        results.append(r)

    toc = time.perf_counter()

    print(f'Serial elapsed time {toc - tic:.2f} s')
    print(f'Serial results\n{results}')


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

    futures = da.map_blocks(calc_result, params)
    results = futures.compute()

    toc = time.perf_counter()

    print(f'Dask elapsed time {toc - tic:.2f} s')
    print(f'Dask results\n{results}')


if __name__ == '__main__':
    np.set_printoptions(precision=2)
    run_serial()

    client = Client(n_workers=8)
    run_dask()
    client.close()
