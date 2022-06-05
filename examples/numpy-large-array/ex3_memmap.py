"""
Example of building a large NumPy array with random values using memmap.

Steps to run and profile the code:
conda activate memmap
mprof run --output ex3_mprof.dat ex3_memmap.py
mprof plot --output ex3_mprof.pdf ex3_mprof.dat
"""

import numpy as np
import time


def main():

    rng = np.random.default_rng()

    tic = time.perf_counter()

    z = 500
    x = 2000
    y = 2000

    a = np.memmap('file.dat', dtype=np.float32, mode='w+', shape=(z, x, y))

    for i in range(z):
        r = rng.standard_normal((x, y), dtype=np.float32)
        a[i] = r

    toc = time.perf_counter()
    print('elapsed =', round(toc - tic, 2), 'sec')


if __name__ == '__main__':
    main()
