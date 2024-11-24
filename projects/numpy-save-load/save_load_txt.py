"""
Example of saving and loading a NumPy array using a text file.
"""

import numpy as np

# Save array to a text file

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

np.savetxt('array.txt', a)

# Load array from a text file

b = np.loadtxt('array.txt')

# Print comparison of `a` and `b`

print('a is\n', a)
print('b is\n', b)
