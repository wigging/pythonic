---
title: Dask array
date: 2021-11-28
---

Dask Array is similar to a NumPy array and allows cutting up a large array into smaller arrays (chunks). This enables working with arrays that are larger than memory. Computations can be applied in parallel for fast execution. Below is an example of using Dask array `map_blocks()` to map a function that returns a single value. Using an 8 CPU core MacBook Pro running macOS v11.6, the serial elapsed time is 513.51 seconds and the Dask elapsed time is 3.21 seconds.

```python
import dask.array as da
import numpy as np
import time
from distributed import Client

def calc_result(p: float) -> float:
    """
    Function to map across an array. Returns a single value.
    """
    time.sleep(1)
    result = p + 1
    return result

def run_serial():
    """
    Non-parallel example (no Dask).
    """
    tic = time.perf_counter()

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
    Parallel example using Dask.
    """
    tic = time.perf_counter()

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
```

Below, is an example of using Dask array `map_blocks()` with a function that returns multiple values as a NumPy array. Using an 8 CPU core MacBook Pro running macOS v11.6, the serial
elapsed time is 513.45 seconds and the Dask elapsed time is 3.20 seconds.

```python
import dask.array as da
import numpy as np
import time
from distributed import Client

def calc_result(p: float) -> float:
    """
    Function to map across an array. Returns two values as an array. This
    could represent a function that returns a tuple.
    """
    time.sleep(1)
    a = p + 1
    b = p + 2
    return np.array([a, b])

def run_serial():
    """
    Non-parallel example (no Dask).
    """
    tic = time.perf_counter()

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
    Parallel example using Dask.
    """
    tic = time.perf_counter()

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
```

## Example code

- [dask_array_1.py](https://github.com/wigging/pythonic/blob/main/examples/dask_array_1.py)
- [dask_array_2.py](https://github.com/wigging/pythonic/blob/main/examples/dask_array_2.py)
