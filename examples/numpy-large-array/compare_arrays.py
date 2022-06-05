"""
Compare array values and make sure they are similar.
"""

import numpy as np
import h5py


def main():

    z = 4  # depth
    x = 3  # rows
    y = 2  # columns

    a = np.zeros((z, x, y))

    f = h5py.File('file.hdf5', 'w')
    dset = f.create_dataset('data', shape=(z, x, y), dtype=np.float64)

    r = np.random.rand(x, y)

    for i in range(z):
        a[i] = r
        dset[i, :, :] = r

    print('a is\n', a)
    print('dset is\n', dset[:])
    print('all close =', np.allclose(a, dset[:]))


if __name__ == '__main__':
    main()
