"""
Example of building a large NumPy array with random values using zarr.

Steps to run and profile the code:
conda activate memmap
mprof run --output ex4_mprof.dat ex4_zarr.py
mprof plot --output ex4_mprof.pdf ex4_mprof.dat
"""

import numpy as np
import zarr
import time


def main():

    rng = np.random.default_rng()

    tic = time.perf_counter()

    z = 500
    x = 2000
    y = 2000

    # a = zarr.open('file.zarr', mode='w', shape=(z, x, y), dtype=np.float32)
    a = zarr.open('file.zarr', mode='w', shape=(z, x, y), chunks=(10, 100, 100), dtype=np.float32)
    # a = zarr.open('file.zarr', mode='w', shape=(z, x, y), chunks=(100, None, None), dtype=np.float32)
    # a = zarr.open('file.zarr', mode='w', shape=(z, x, y), dtype=np.float32)

    for i in range(z):
        r = rng.standard_normal((x, y), dtype=np.float32)
        a[i] = r

    toc = time.perf_counter()
    print('elapsed =', round(toc - tic, 2), 'sec')


if __name__ == '__main__':
    main()
