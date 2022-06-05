"""
Example of building a large NumPy array with random values using load with
mmap_mode.

Steps to run and profile the code:
conda activate memmap
mprof run --output ex5_mprof.dat ex5_load.py
mprof plot --output ex5_mprof.pdf ex5_mprof.dat
"""

import numpy as np
import time


def main():

    rng = np.random.default_rng()

    tic = time.perf_counter()

    z = 500     # depth
    x = 2000    # rows
    y = 2000    # columns

    a = np.zeros((z, x, y), dtype=np.float32)
    np.save('file.npy', a)

    b = np.load('file.npy', mmap_mode='r+')

    for i in range(z):
        r = rng.standard_normal((x, y), dtype=np.float32)
        b[i, :, :] = r
        b.flush()

    toc = time.perf_counter()
    print('elapsed =', round(toc - tic, 2), 'sec')


if __name__ == '__main__':
    main()
