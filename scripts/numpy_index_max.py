"""
Get the index of the maximum value in an array.
"""

import numpy as np

# Example 1
# ----------------------------------------------------------------------------

x = np.array([1, 8, 2.5, 4])
ind = x.argmax()

print('1D array', x)
print('Max value at index', ind)

# Example 2
# ----------------------------------------------------------------------------

y = np.array([1, 8, 2.5, 4, 8])  # index of first occurrence is returned
ind = y.argmax()

print('1D array', y)
print('Max value at index', ind)

# Example 3
# ----------------------------------------------------------------------------

z = np.array([[1, 2.4, 7, 5], [0.2, 8, 7, 4.9], [5, 3.1, 4, 1], [7, 2, 4, 3]])
ind = np.unravel_index(z.argmax(), z.shape)

print('2D array\n', z)
print('Max value at index', ind)
