"""
Example of building a large NumPy array with random values using hdf5.

Steps to run and profile the code:
conda activate memmap
mprof run --output ex6_mprof.dat ex6_hdf5.py
mprof plot --output ex6_mprof.pdf ex6_mprof.dat
"""

import numpy as np
import h5py
import time


def main():

    rng = np.random.default_rng()

    tic = time.perf_counter()

    z = 500   # depth
    x = 2000  # rows
    y = 2000  # columns

    f = h5py.File('file.hdf5', 'w')
    dset = f.create_dataset('data', shape=(z, x, y), dtype=np.float32)

    for i in range(z):
        r = rng.standard_normal((x, y), dtype=np.float32)
        dset[i, :, :] = r

    toc = time.perf_counter()
    print('elapsed time =', round(toc - tic, 2), 'sec')

    s = np.float32().nbytes * (z * x * y) / 1e9  # where 1 GB = 1000 MB
    print('calculated storage =', s, 'GB')


if __name__ == '__main__':
    main()
