"""
Basic example of building a large NumPy array with random values. Data type is
defined as `np.float32` for the arrays.

Steps to run and profile the code:
conda activate memmap
mprof run --output ex2_mprof.dat ex2_float32.py
mprof plot --output ex2_mprof.pdf ex2_mprof.dat
"""

import numpy as np
import time


def main():

    rng = np.random.default_rng()

    tic = time.perf_counter()

    z = 500   # depth
    x = 2000  # rows
    y = 2000  # columns

    a = np.zeros((z, x, y), dtype=np.float32)

    for i in range(z):
        r = rng.standard_normal((x, y), dtype=np.float32)
        a[i] = r

    toc = time.perf_counter()
    print('elapsed time =', round(toc - tic, 2), 'sec')

    s = np.float32().nbytes * (z * x * y) / 1e9  # where 1 GB = 1000 MB
    print('calculated storage =', s, 'GB')


if __name__ == '__main__':
    main()
