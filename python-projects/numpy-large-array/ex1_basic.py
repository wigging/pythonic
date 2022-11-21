"""
Basic example of building a large NumPy array with random values. Notice that
`np.random.rand()` creates an array of `np.float64` values.

Steps to run and profile the code:
conda activate memmap
mprof run --output ex1_mprof.dat ex1_basic.py
mprof plot --output ex1_mprof.pdf ex1_mprof.dat
"""

import numpy as np
import time


def main():

    tic = time.perf_counter()

    z = 500   # depth
    x = 2000  # rows
    y = 2000  # columns

    a = np.zeros((z, x, y))

    for i in range(z):
        r = np.random.rand(x, y)
        a[i] = r

    toc = time.perf_counter()
    print('elapsed time =', round(toc - tic, 2), 'sec')

    s = np.float64().nbytes * (z * x * y) / 1e9  # where 1 GB = 1000 MB
    print('calculated storage =', s, 'GB')


if __name__ == '__main__':
    main()
