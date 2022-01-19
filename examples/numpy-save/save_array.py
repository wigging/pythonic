"""
Example of saving and loading a single NumPy array.
"""

import numpy as np

# Save an array named `z` to an `.npy` file

z = np.array([[3, 4, 8.91], [1.05, 2, 7], [5.4, 3, 1]])

with open('zarray.npy', 'wb') as file:
    np.save(file, z)

# Load the array data from the `.npy` file into `zz`

with open('zarray.npy', 'rb') as file:
    zz = np.load(file)

# Print results

print('z is\n', z)
print('zz is\n', zz)
